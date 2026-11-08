#!/usr/bin/env python3
"""Local technical video check. No network, upload, visual score or source edits."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def positive(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError('Expected a positive finite number')
    return number


def number(value):
    try:
        parsed = float(Fraction(str(value)))
        return parsed if math.isfinite(parsed) else None
    except (ValueError, ZeroDivisionError):
        return None


def run(argv, timeout):
    return subprocess.run(argv, capture_output=True, text=True, timeout=timeout, check=True)


def inspect(args):
    source = args.video.resolve()
    if not source.is_file():
        raise ValueError('Input must be an existing local video file')
    report = {
        'source': str(source), 'size_bytes': source.stat().st_size,
        'scope': 'Technical metadata and full-file decoding; no visual or audio quality judgment',
        'checks': [], 'not_checked': ['Visual defects', 'Text readability', 'Scene structure',
                                    'Audio quality and clipping', 'Pixel fidelity', 'Constant frame rate'],
    }
    digest = hashlib.sha256()
    with source.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(block)
    report['sha256'] = digest.hexdigest()
    missing = [name for name in ('ffprobe', 'ffmpeg') if not shutil.which(name)]
    if missing:
        report.update(status='unverified', reason='Missing local tools: ' + ', '.join(missing))
        return report
    try:
        raw = json.loads(run(['ffprobe', '-v', 'error', '-count_frames', '-show_streams',
                              '-show_format', '-of', 'json', str(source)], args.timeout).stdout)
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        report.update(status='unverified', reason='Probe did not complete', error_type=type(exc).__name__)
        return report
    streams = raw.get('streams', [])
    video = next((s for s in streams if s.get('codec_type') == 'video'), None)
    audio = [s for s in streams if s.get('codec_type') == 'audio']
    if not video:
        report.update(status='failed', reason='No video stream')
        return report
    measured = {
        'width': video.get('width'), 'height': video.get('height'), 'video_codec': video.get('codec_name'),
        'duration_seconds': number(video.get('duration') or raw.get('format', {}).get('duration')),
        'average_fps': number(video.get('avg_frame_rate')), 'average_fps_ratio': video.get('avg_frame_rate'),
        'decoded_video_frames': number(video.get('nb_read_frames')), 'pixel_format': video.get('pix_fmt'),
        'container_family': raw.get('format', {}).get('format_name'),
        'audio_streams': [{'codec': a.get('codec_name'), 'channels': a.get('channels'),
                           'sample_rate': a.get('sample_rate')} for a in audio],
    }
    report['measured'] = measured
    for label, actual, expected, tolerance in [
        ('width', measured['width'], args.expect_width, 0),
        ('height', measured['height'], args.expect_height, 0),
        ('duration_seconds', measured['duration_seconds'], args.expect_duration, args.duration_tolerance),
        ('average_fps', measured['average_fps'], args.expect_fps, 0.01),
    ]:
        if expected is not None:
            report['checks'].append({'property': label, 'expected': expected, 'actual': actual,
                                     'tolerance': tolerance,
                                     'status': 'unverified' if actual is None else 'passed' if abs(actual - expected) <= tolerance else 'failed'})
    if args.expect_audio:
        report['checks'].append({'property': 'audio_present', 'expected': True, 'actual': bool(audio),
                                 'status': 'passed' if audio else 'failed'})
    try:
        run(['ffmpeg', '-hide_banner', '-nostdin', '-v', 'error', '-xerror', '-threads', '2',
             '-i', str(source), '-map', '0:v:0', '-map', '0:a?', '-f', 'null', '-'], args.timeout)
        decode = {'property': 'complete_decode', 'status': 'passed'}
    except subprocess.TimeoutExpired:
        decode = {'property': 'complete_decode', 'status': 'unverified', 'reason': 'Decode timeout; partial decoding is not a pass'}
    except subprocess.CalledProcessError:
        decode = {'property': 'complete_decode', 'status': 'failed', 'reason': 'FFmpeg reported a decoding error'}
    report['checks'].append(decode)
    statuses = [check['status'] for check in report['checks']]
    report['status'] = 'failed' if 'failed' in statuses else 'unverified' if 'unverified' in statuses else 'passed'
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--expect-width', type=int)
    parser.add_argument('--expect-height', type=int)
    parser.add_argument('--expect-duration', type=positive)
    parser.add_argument('--expect-fps', type=positive)
    parser.add_argument('--expect-audio', action='store_true')
    parser.add_argument('--duration-tolerance', type=positive, default=0.05, help='Seconds; default 0.05')
    parser.add_argument('--timeout', type=positive, default=120, help='Seconds per subprocess')
    args = parser.parse_args()
    if any(value is not None and value <= 0 for value in (args.expect_width, args.expect_height)):
        parser.error('Expected dimensions must be positive')
    try:
        report = inspect(args)
    except (ValueError, OSError) as exc:
        parser.exit(2, f'Unable to inspect the local file: {exc}\n')
    args.output.mkdir(parents=True, exist_ok=True)
    output = args.output / 'render-check.json'
    temporary = output.with_suffix('.tmp')
    temporary.write_text(json.dumps(report, indent=2) + '\n')
    temporary.replace(output)
    print(json.dumps({'status': report['status'], 'report': str(output.resolve()), 'scope': report['scope']}))
    return {'passed': 0, 'failed': 1, 'unverified': 2}[report['status']]


if __name__ == '__main__':
    sys.exit(main())
