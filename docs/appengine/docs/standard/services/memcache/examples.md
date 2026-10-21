---
url: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/examples/
title: Memcache Examples \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:50.605621+00:00
---

# Memcache Examples  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Memcache Examples Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This page provides code examples in Python code for using Memcache. Memcache is a high-performance, distributed memory object caching system that provides fast access to cached data. To learn more about memcache, read the [Memcache Overview](https://docs.cloud.google.com/appengine/docs/standard/services/memcache).

## The memcache Pattern

Memcache is typically used with the following pattern:

  * The application receives a query from the user or the application.
  * The application checks whether the data needed to satisfy that query is in memcache. 
    * If the data is in memcache, the application uses that data.
    * If the data is not in memcache, the application queries the datastore and stores the results in memcache for future requests.



The pseudocode below represents a typical memcache request:
    
    
    def get_data():
        data = memcache.get('key')
        if data is not None:
            return data
        else:
            data = query_for_data()
            memcache.add('key', data, 60)
        return data

`ndb` internally uses memcache to speed up queries. However, if you wish, you can also explicitly add memcache calls to gain more control about the speed-ups.

## Caching data

The following example demonstrates several ways to set values in memcache using the Python API.
    
    
    # Add a value if it doesn't exist in the cache
    # with a cache expiration of 1 hour.
    memcache.add(key="weather_USA_98105", value="raining", time=3600)
    
    # Set several values, overwriting any existing values for these keys.
    memcache.set_multi(
        {"USA_98115": "cloudy", "USA_94105": "foggy", "USA_94043": "sunny"},
        key_prefix="weather_",
        time=3600
    )
    
    # Atomically increment an integer value.
    memcache.set(key="counter", value=0)
    memcache.incr("counter")
    memcache.incr("counter")
    memcache.incr("counter")

To learn more about the `add()`, `set_multi()`, and `set()` methods, see the [memcache Python API documentation](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache).

**Note:** The standard Python [pickle](https://docs.python.org/3.8/library/pickle.html) module is used to auto pickle and depickle data moved into and out of memcache.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
