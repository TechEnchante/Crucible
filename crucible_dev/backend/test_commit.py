#!/usr/bin/env python3
import argparse
import time
import sys
import json

try:
    import requests
except ImportError:
    print("Please install requests first: pip install requests", file=sys.stderr)
    sys.exit(1)

def post_commit(url: str, user_id: str, message: str, timestamp: float):
    payload = {
        "user_id": user_id,
        "message": message,
        "timestamp": timestamp
    }
    resp = requests.post(url, json=payload)
    try:
        resp.raise_for_status()
    except requests.HTTPError:
        print(f"ERROR: {resp.status_code} – {resp.text}", file=sys.stderr)
        sys.exit(1)
    return resp.json()

def main():
    parser = argparse.ArgumentParser(
        description="Test the /commits/new endpoint"
    )
    parser.add_argument(
        "-u", "--user-id", required=True,
        help="User ID for the commit"
    )
    parser.add_argument(
        "-m", "--message", required=True,
        help="Commit message text"
    )
    parser.add_argument(
        "-t", "--timestamp", type=float, default=time.time(),
        help="Unix timestamp for the commit (default: now)"
    )
    parser.add_argument(
        "-U", "--url", default="http://localhost:8000/commits/new",
        help="Full URL of the commit endpoint"
    )
    args = parser.parse_args()

    result = post_commit(args.url, args.user_id, args.message, args.timestamp)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    #Manual Test
    url       = "http://localhost:8000/commits/new"
    user_id   = "alice"
    message   = "UUID test"
    timestamp = time.time()

    result = post_commit(url, user_id, message, timestamp)
    print(json.dumps(result, indent=2))