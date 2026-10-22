---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache/
title: AnywhereCache \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:38:04.104177+00:00
---

# AnywhereCache  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  AnywhereCache Stay organized with collections  Save and categorize content based on your preferences. 

The AnywhereCache resource represents a [Rapid Cache cache instance](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) in Cloud Storage.

To try out the methods for this resource, see Methods.

## Resource representation
    
    
    {
      "kind": "storage#AnywhereCache"
      "id": string,
      "selfLink": string,
      "bucket": string,
      "zone": string,
      "state": string,
      "createTime": datetime,
      "updateTime": datetime,
      "ttl": string,
      "ingestOnWrite": boolean,
      "pendingUpdate": boolean
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For caches, this is always "`storage#anywhereCache`". |   
`id` | `string` | The ID of the cache instance, formatted as `BUCKET_NAME/ANYWHERE_CACHE_ZONE_ID`. For example, `example-bucket/us-east1-b`. |   
`selfLink` | `string` | The link (URI) of this cache. |   
`bucket` | `string` | The name of the bucket that owns the cache instance. For example, `example-bucket`. | Writeable  
`zone` | `string` | The zone in which the cache instance is running. For example, `us-east1-b`. | Writeable  
`state` | `string` | The status of the cache instance. Can be `CREATING`, `RUNNING`, or `DISABLED`. |   
`createTime` | `datetime` | The creation time of the cache instance. |   
`updateTime` | `datetime` | The last modification time of the cache instance. |   
`ttl` | `string` | The TTL (time to live) of data in the cache, in seconds. | Writeable  
`ingestOnWrite` | `boolean` | Whether or not the cache ingests data as the data is written to the bucket. | Writeable  
`pendingUpdate` | `boolean` | True if the cache instance has an active `UpdateAnywhereCache` [long-running operation](https://google.aip.dev/151) attached. |   
  
## Methods

[create](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/create)
    Create a Rapid Cache cache.
[disable](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/disable)
    Disable a Rapid Cache cache.
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/get)
    Get a Rapid Cache cache.
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/list)
    Retrieve a list of Rapid Cache caches.
[resume](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/resume)
    Resume the data ingestion of a Rapid Cache cache, or revoke the disablement of the cache.
[update](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/update)
    Update a Rapid Cache cache.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
