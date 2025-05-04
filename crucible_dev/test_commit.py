#!/usr/bin/env python3
import sys
import json
import time
import argparse

import requests

def post_commit(user_id: str, message: str, timestamp: float):
    url = "http://localhost:8000/commits/new"
    payload = {
        "user_id": user_id,
        "message": message,
        "timestamp": timestamp
    }
    resp = requests.post(url, json=payload)
    resp.raise_for_status()
    return resp.json()

def main():
    parser = argparse.ArgumentParser(description="Test committing a message to Qdrant via FastAPI")
    parser.add_argument("user_id", help="User ID for the commit")
    parser.add_argument("message", help="Commit message text")
    parser.add_argument("--timestamp", type=float, default=time.time(),
                        help="Unix timestamp for the commit (default: now)")
    args = parser.parse_args()

    result = post_commit(args.user_id, args.message, args.timestamp)
    print("Response:", json.dumps(result, indent=2))

if __name__ == "__main__":
    main()