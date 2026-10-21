---
url: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/python/index.txt
title: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/python/index.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-15T00:42:41.746896+00:00
---

# https://docs.cloud.google.com/appengine/docs/standard/services/memcache/python/index.txt

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/python/index.txt


    // [START using_compare_and_set]
    def bump_counter(key):
       client = memcache.Client()
       while True: # Retry loop
         counter = client.gets(key)
         if counter is None: raise KeyError('Uninitialized counter')
         if client.cas(key, counter+1):
            break
    // [END using_compare_and_set]
    
