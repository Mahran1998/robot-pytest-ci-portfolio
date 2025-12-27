from __future__ import annotations
import sys
import time
import requests

def main():
    if len(sys.argv) < 3:
        print("Usage: wait_for_http.py <url> <timeout_seconds>", file=sys.stderr)
        return 2

    url = sys.argv[1]
    timeout = int(sys.argv[2])

    deadline = time.time() + timeout
    last_err = None

    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=2)
            if r.status_code < 500:
                print(f"OK: {url} -> {r.status_code}")
                return 0
        except Exception as e:
            last_err = e
        time.sleep(1)

    print(f"ERROR: timeout waiting for {url}. last_err={last_err}", file=sys.stderr)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
