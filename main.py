import json
import os
import sys

from utils import run


def main():
    try:
        pr_id = json.loads(sys.argv[1])['event']['number']
    except Exception as _:
        pr_id = None
    print(f'pr_id: {pr_id}')

    with open('settings.json', 'r') as f:
        settings = json.load(f)

    run(['mkdir', '-p', settings['tmp_pred_path']])
    run(['rm', '-rf', os.path.join(settings['tmp_pred_path'], '*')])
    cmd = [
        'singularity', 'run', '--nv', '--pwd', settings['run']['pwd'],
        '--bind', f"{settings['tmp_pred_path']}:{settings['run']['pred_path']},"
                  f"{settings['val_rgb_path']}:{settings['run']['rgb_path']},"
                  f"demo.py:/workspace/synboost/main.py",
        settings['sif_path']
    ]
    run(cmd)


if __name__ == '__main__':
    main()
