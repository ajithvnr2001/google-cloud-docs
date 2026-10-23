---
url: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/using/
title: Using Memcache \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:09.888228+00:00
---

# Using Memcache  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/memcache/using/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Using Memcache Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

This page describes how to configure and monitor the memcache service for your application using the Google Cloud console. It also describes how to use the App Engine memcache Python API to set and retrieve cached values and use the compare-and-set feature to handle concurrent write requests to the same memcache key. To learn more about memcache, read the [Memcache Overview](https://docs.cloud.google.com/appengine/docs/standard/services/memcache).

## Configure memcache

  1. Go to the Memcache page in the Google Cloud console.  
[Go to the Memcache page](https://console.cloud.google.com/appengine/memcache)
  2. Select the memcache service level you want to use: 
     * **Shared** (default) - free and provides cache capacity on a best-effort basis.
     * **Dedicated** \- billed by the GB-hour of cache size and provides a fixed cache capacity assigned exclusively to your application.



Learn more about available service classes in Memcache Overview.

## Cache and retrieve values

### Cache a value

Use `add()` to add a key's value if and only if it doesn't already exist, with an optional expiration time:
    
    
    memcache.add(key="[KEY]", value="[VALUE]", time=[EXPIRATION_TIME])
    

For example, to add the value `raining` to the key `weather_USA_98105` with an expiration time of one hour from when the value is written:
    
    
    memcache.add(key="weather_USA_98105", value="raining", time=3600)
    

Learn more about `add()` and other methods for setting values in the [memcache Python API documentation](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/add).

See other examples of caching values in [Memcache Examples](https://docs.cloud.google.com/appengine/docs/standard/services/memcache/examples).

### Look up cached values

Use `get()` to look up the value of a single key:
    
    
    memcache.get(key="[KEY]")
    

For example, to get the value of the key `weather_USA_98105`:
    
    
    memcache.get(key="weather_USA_98105")
    

Learn more about `get()` and other methods for looking up values in the [memcache Python API documentation](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/memcache/get).

## Monitor memcache in the Google Cloud console

  1. Go to the Memcache page in the Google Cloud console.  
[Go to the Memcache page](https://console.cloud.google.com/appengine/memcache)  

  2. Look at the following reports: 
     * **Memcache service level** : Shows if your application is using the Shared or Dedicated service level. If you are an owner of the project, you can switch between the two. Learn more about the [service levels](https://docs.cloud.google.com/appengine/docs/standard/services/memcache/#service_levels).
     * **Hit ratio** : Shows the percentage of data requests that were served from the cache, as well as the raw number of data requests that were served from the cache.
     * **Items in the cache**.
     * **Oldest item age** : The age of the oldest cached item. Note that the age of an item is reset every time it is used, either read or written.
     * **Total cache size**.
  3. You can take any of the following actions:

     * **New key** : Add a new key to the cache.
     * **Find a key** : Retrieve an existing key.
     * **Flush cache** : Remove all the key-value pairs from the cache.
  4. (Dedicated memcache only) Look through the list of **Hot keys**.

     * "Hot keys" are keys that receive more than 100 queries per second (QPS) in the memcache.
     * This list includes up to 100 hot keys, sorted by highest QPS.



## Handle concurrent writes

To use the compare and set feature to handle writes from multiple requests to the same memcache key:

  1. Instantiate a memcache `Client` object.
  2. Use a retry loop (preferably with a limit on the number of retries and using exponential backoff) 
     1. Within the retry loop, get the key using `gets()` or `get_multi()` with the `for_cas` parameter set to `True`.
     2. Within the retry loop, update the key value using `cas()` or `cas_multi()`.



The following snippet shows one way to use the compare and set feature:
    
    
    def bump_counter(key):
       client = memcache.Client()
       while True: # Retry loop
         counter = client.gets(key)
         if counter is None: raise KeyError('Uninitialized counter')
         if client.cas(key, counter+1):
            break
    

The retry loop is necessary because without the loop this code doesn't actually avoid race conditions, it just detects them! The memcache service guarantees that when used in the pattern shown here (that is, using `gets()` and `cas()`), if two (or more) different client instances happen to be involved in a race condition, only the first one to execute the `cas()` operation succeeds (return `True`), while the second one (and subsequent ones) fails (return `False`).

Another refinement you should add to this sample code is to set a limit on the number of retries, to avoid an infinite loop in worst-case scenarios where there is a lot of contention for the same counter. An example of when such contention could occur is if there are more requests trying to update the counter than the memcache service can process in real time.

Learn more about compare and set in the [Memcache Overview](https://docs.cloud.google.com/appengine/docs/standard/services/memcache#compare_and_set).

## What's next

  * Learn more about memcache in the [Memcache Overview](https://docs.cloud.google.com/appengine/docs/standard/services/memcache). 
  * See code examples of using memcache in Python in [Memcache Examples](https://docs.cloud.google.com/appengine/docs/standard/services/memcache/examples). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
