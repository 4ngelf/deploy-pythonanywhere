import os.path
import sys
import argparse
import json

from http.client import HTTPException

from . import (AUTHOR, VERSION, LICENSE)

# from client import deploy

def parse_args():
    prog = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(
        prog = prog,
        description="Cli client to deploy to pythonanywhere",
        epilog=f"Author: {AUTHOR}\n License: {LICENSE}\nVersion: {prog} {VERSION}")

    parser.add_argument(
        "-k",
        "--key",
        action='store',
        default='-',
        help="Use given key")
    parser.add_argument(
        "pre_command",
        action="store",
        default='git pull origin',
        dest="command"
        help="command to execute before restarting webapp. default='git pull origin'" )
    return parser.parse_args()

def main():
    args = parse_args()
    key = key if args.key != "-" else sys.stdin.readline()

    try:
        result = json.loads('{"version":"0.1.0","ok":true}')
        # result = deploy(key)
    except HTTPException as e:
        raise e, "Couldn't connect to pythonanywhere server"

    # TODO: handle invalid json
    
    # TODO: handle error on deploy
    # example:
    # if !result["ok"]:
    #     raise f"[Error] pythonanywhere server failed to deploy with {result["err"]}."

    if result["ok"]:
        print("[Success] deploy to pythonanywhere successful")

    return 0

if __name__ == "__main__":
    sys.exit(main())
