#!/usr/bin/env python3
"""Coverage audit: every sitemap canonical URL must be either visited or recorded-as-failed.
Writes missing_urls.txt (feed to final_gapfill.py) and prints a report.
Run: python3 verify_coverage.py [--fill]
"""
import sqlite3, pathlib, sys
from urllib.parse import urljoin, urldefrag

ROOT = pathlib.Path(__file__).resolve().parent
DOCS_BASE = "https://docs.cloud.google.com"


def canon(u, base=DOCS_BASE):
    abs_u, _ = urldefrag(urljoin(base, u.strip()))
    p = __import__("urllib.parse", fromlist=["urlparse"]).urlparse(abs_u)
    path = p.path
    if path.endswith("/index.md"):
        path = path[: -len("/index.md")] + "/"
    elif path.endswith("/index"):
        path = path[: -len("/index")] + "/"
    elif path in ("/index.md", "/index"):
        path = "/"
    elif path.endswith(".md"):
        path = path[:-3]
        if not path.endswith("/"):
            path = path + "/"
    c = f"{p.scheme}://{p.netloc}{path}"
    return c if c.endswith("/") or "." in c.rsplit("/", 1)[-1] else c + "/"


def main():
    fill = "--fill" in sys.argv
    urls = set()
    for f in sorted((ROOT / "seeds").glob("sitemap_*.txt")):
        for l in f.read_text().splitlines():
            if l.strip():
                urls.add(canon(l))
    print("unique sitemap urls:", len(urls), flush=True)
    con = sqlite3.connect(ROOT / "crawl_state.db")
    have, failed = set(), set()
    for i in range(0, len(urls), 3000):
        chunk = list(urls)[i:i + 3000]
        q = f"SELECT url FROM visited WHERE url IN ({','.join('?' * len(chunk))})"
        have |= {r[0] for r in con.execute(q, chunk)}
        qf = f"SELECT url FROM failed WHERE url IN ({','.join('?' * len(chunk))})"
        failed |= {r[0] for r in con.execute(qf, chunk)}
    missing = [u for u in urls if u not in have and u not in failed]
    print(f"visited {len(have)} | failed-recorded {len(failed & urls)} | missing {len(missing)}")
    print(f"coverage: {100 * (len(urls) - len(missing)) / len(urls):.3f}% (missing treated as binary/pdf if gapfill fails)")
    (ROOT / "missing_urls.txt").write_text("\n".join(sorted(missing)) + "\n")
    from collections import Counter
    ext = Counter(("pdf" if u.lower().endswith(".pdf") else
                   u.rsplit(".", 1)[-1].lower() if "." in u.rsplit("/", 1)[-1] else "html") for u in missing)
    print("missing by type:", ext.most_common(8))
    if fill and missing:
        print("run next: python3 final_gapfill.py")


if __name__ == "__main__":
    main()
