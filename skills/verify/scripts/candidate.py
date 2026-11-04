"""Read-only identity for a Git candidate. Requires Python 3 and Git."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import sys


def git(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, check=False
    )
    if result.returncode:
        raise ValueError("Git could not resolve the repository or requested revision")
    return result.stdout


def fingerprint(repo, base):
    root = Path(os.fsdecode(git(repo, "rev-parse", "--show-toplevel").rstrip(b"\r\n")))
    head = git(root, "rev-parse", "--verify", "HEAD^{commit}").strip().decode("ascii")
    baseline = git(root, "rev-parse", "--verify", base + "^{commit}").strip().decode("ascii")
    index = git(root, "ls-files", "--stage", "-z")
    if any(entry.startswith(b"160000 ") for entry in index.split(b"\0")):
        raise ValueError("Submodules require a recursive snapshot; this helper refuses partial identity")
    names = sorted(set(filter(None, git(
        root, "ls-files", "--cached", "--others", "--exclude-standard", "-z"
    ).split(b"\0"))))
    digest = hashlib.sha256()

    def add(data):
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)

    for item in (b"gentle-stack-candidate-v1", baseline.encode(), head.encode(), index):
        add(item)
    for name in names:
        path = root / os.fsdecode(name)
        add(name)
        try:
            mode = path.lstat().st_mode
        except FileNotFoundError:
            add(b"missing")
            continue
        if stat.S_ISLNK(mode):
            add(b"symlink")
            add(os.fsencode(os.readlink(path)))
        elif stat.S_ISREG(mode):
            add(b"executable" if mode & stat.S_IXUSR else b"regular")
            file_hash = hashlib.sha256()
            with path.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    file_hash.update(chunk)
            add(file_hash.digest())
        else:
            raise ValueError("Unsupported file type; use a snapshot covering all review inputs")
    return {
        "schema": "gentle-stack-candidate-v1",
        "repository": str(root),
        "base": baseline,
        "head": head,
        "fingerprint": digest.hexdigest(),
        "file_count": len(names),
        "coverage": "index and tracked/non-ignored untracked working files",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".")
    parser.add_argument("--base", required=True, help="Review base revision; reuse resolved commit ID")
    args = parser.parse_args()
    try:
        print(json.dumps(fingerprint(args.repo, args.base), ensure_ascii=True))
    except (OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
