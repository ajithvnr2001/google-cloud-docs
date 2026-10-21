---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/functions/
title: Functions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:56.086513+00:00
---

# Functions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Functions Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

The `google.appengine.api.search` package includes the following function:

get_indexes(namespace='', offset=None, limit=None, start_index_name=None, include_start_index=True, index_name_prefix=None, fetch_schema=False, deadline=None)

Return list of available indexes.

**Note:** There is also a corresponding asynchronous method, `get_indexes_async()`, which is identical except it returns a future. To get the actual result, call `get_result()` on the returned value; that call will block.
    

Arguments

namespace
    

Namespace of indexes to return. If not set, the current namespace is used.

offset
    

Offset of first index to return.

limit
    

Number of indexes to return.

start_index_name
    

Name of first index to return.

include_start_index
    

If `true`, include index specified by `start_index_name` in results.

index_name_prefix
    

Prefix for selecting indexes to return.

fetch_schema
    

Specifies whether to fetch the schema for each index.

deadline
    

Deadline for RPC call in seconds.

Result value

    

`[GetResponse](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/getresponseclass)` object representing a list of indexes. If fetch_schema==true, each index will contain its schema.

Exceptions

TypeError
    

Invalid argument passed.

InternalError
    

Request failed on internal servers.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
