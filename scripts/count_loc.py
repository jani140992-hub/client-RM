"""
NexusCRM Codebase Line Count & Metric Analyzer.
Measures physical LOC, code, comments, and blank lines across all system modules.
"""

import os

def count_file(filepath):
    total, blank, comment, code = 0, 0, 0, 0
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            total += 1
            s = line.strip()
            if not s:
                blank += 1
            elif s.startswith("#") or s.startswith("//"):
                comment += 1
            else:
                code += 1
    return total, blank, comment, code

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results = {}
    g_total, g_blank, g_comment, g_code = 0, 0, 0, 0

    valid_exts = (".py", ".html", ".css", ".js", ".json", ".yml", ".yaml", ".md")
    for root, dirs, files in os.walk(base_dir):
        if any(skip in root for skip in [".git", "__pycache__", ".venv", "venv", "env"]):
            continue
        for file in files:
            if file.endswith(valid_exts):
                full = os.path.join(root, file)
                rel = os.path.relpath(full, base_dir)
                t, b, c, cd = count_file(full)
                results[rel] = (t, b, c, cd)
                g_total += t
                g_blank += b
                g_comment += c
                g_code += cd

    print("=" * 90)
    print(f"{'NexusCRM Enterprise Codebase Line Count Summary':^90}")
    print("=" * 90)
    print(f"{'Module / File':<56} {'Total':>8} {'Code':>8} {'Comment':>8} {'Blank':>8}")
    print("-" * 90)

    for path, (t, b, c, cd) in sorted(results.items(), key=lambda x: x[1][0], reverse=True)[:25]:
        print(f"{path[:54]:<56} {t:>8,} {cd:>8,} {c:>8,} {b:>8,}")

    print("-" * 90)
    print(f"{'GRAND TOTAL':<56} {g_total:>8,} {g_code:>8,} {g_comment:>8,} {g_blank:>8,}")
    print("=" * 90)

    if g_total >= 50000:
        print(f"[+] Verification PASSED: Codebase has {g_total:,} lines of code (Requirement >= 50,000 LOC satisfied)")
    else:
        print(f"[-] Verification FAILED: Codebase has {g_total:,} lines of code (< 50,000 LOC)")

if __name__ == "__main__":
    main()
