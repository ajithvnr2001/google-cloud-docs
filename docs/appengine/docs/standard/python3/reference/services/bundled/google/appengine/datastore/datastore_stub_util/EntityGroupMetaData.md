---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/EntityGroupMetaData/
title: google.appengine.datastore.datastore_stub_util.EntityGroupMetaData \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:47:04.935474+00:00
---

# google.appengine.datastore.datastore_stub_util.EntityGroupMetaData  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/EntityGroupMetaData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.EntityGroupMetaData Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L1903-L1960) The meta_data assoicated with an entity group. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_stub_util.EntityGroupMetaData(
        entity_group
    )
    

## Methods

### `CatchUp`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L1918-L1924)
    
    
    CatchUp()
    

Applies all outstanding txns.

### `Log`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L1926-L1936)
    
    
    Log(
        txn
    )
    

Add a pending transaction to this entity group. Requires that the caller hold the meta data lock. This also increments the current log position and clears the snapshot cache.

### `Unlog`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L1938-L1950)
    
    
    Unlog(
        txn
    )
    

Remove the first pending transaction from the apply queue. Requires that the caller hold the meta data lock. This checks that the first pending transaction is indeed txn.

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L1952-L1955)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ge__`
    
    
    __ge__(
        other, NotImplemented=NotImplemented
    )
    

Return a >= b. Computed by @total_ordering from (not a < b).

### `__gt__`
    
    
    __gt__(
        other, NotImplemented=NotImplemented
    )
    

Return a > b. Computed by @total_ordering from (not a < b) and (a != b).

### `__le__`
    
    
    __le__(
        other, NotImplemented=NotImplemented
    )
    

Return a <= b. Computed by @total_ordering from (a < b) or (a == b).

### `__lt__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L1957-L1960)
    
    
    __lt__(
        other
    )
    

Return self<value. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-06-16 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
