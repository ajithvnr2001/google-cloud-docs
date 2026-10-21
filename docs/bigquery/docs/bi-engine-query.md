---
url: https://docs.cloud.google.com/bigquery/docs/bi-engine-query/
title: https://docs.cloud.google.com/bigquery/docs/bi-engine-query/
method: httpx+scrapegraph (scrapling: scrapling empty html | crawl4ai: crawl4ai failed: Unexpected error in _crawl_web at line 778 in _crawl_web (../../../usr/local/lib/python3.10/dist-packages/crawl4ai/async_crawler_strategy.py):
Error: Failed on navigating ACS-GOTO:
Page.goto: Download is starting
Call log:
  - navigating to "https://docs.cloud.google.com/bigquery/docs/bi-engine-query/", waiting until "domcontentloaded"


Code context:
 773                                   tag="GOTO",
 774                                   params={"url": url},
 775                               )
 776                               response = None
 777                           else:
 778 →                             raise RuntimeError(f"Failed on navigating ACS-GOTO:\n{str(e)}")
 779   
 780                       # ──────────────────────────────────────────────────────────────
 781                       # Walk the redirect chain.  Playwright returns only the last
 782                       # hop, so we trace the `request.redirected_from` links until the
 783                       # first response that differs from the final one and surface its)
fetched_at: 2026-10-17T08:51:43.378398+00:00
---

# https://docs.cloud.google.com/bigquery/docs/bi-engine-query/

> Source: https://docs.cloud.google.com/bigquery/docs/bi-engine-query/


