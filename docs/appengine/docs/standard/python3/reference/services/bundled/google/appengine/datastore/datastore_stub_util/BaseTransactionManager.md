---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseTransactionManager/
title: google.appengine.datastore.datastore_stub_util.BaseTransactionManager \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:05:04.987947+00:00
---

# google.appengine.datastore.datastore_stub_util.BaseTransactionManager  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseTransactionManager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.BaseTransactionManager Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2150-L2391) A class that manages the state of transactions. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_stub_util.BaseTransactionManager(
        consistency_policy=None
    )
    

This includes creating consistent snap shots for transactions.

## Methods

### `BeginTransaction`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2190-L2223)
    
    
    BeginTransaction(
        app,
        allow_multiple_eg,
        previous_transaction=None,
        mode=datastore_pb.BeginTransactionRequest.UNKNOWN
    )
    

Start a transaction on the given app. | Args  
---  
  
`app` |  A string representing the app for which to start the transaction.   
`allow_multiple_eg` |  True if transactions can span multiple entity groups.   
`previous_transaction` |  The transaction to reset.   
`mode` |  Mode of the transaction.   
  
Returns  
---  
A datastore_pb.Transaction() for the created transaction   
  
### `Clear`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2183-L2188)
    
    
    Clear()
    

Discards any pending transactions and resets the meta data.

### `Flush`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2254-L2269)
    
    
    Flush()
    

Applies all outstanding transactions.

### `GetTxn`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2225-L2241)
    
    
    GetTxn(
        transaction, request_trusted, request_app
    )
    

Gets the LiveTxn object associated with the given transaction.

Args  
---  
  
`transaction` |  The datastore_pb.Transaction() to look up.   
`request_trusted` |  A boolean indicating If the requesting app is trusted.   
`request_app` |  A string representing the app making the request.   
  
Returns  
---  
The associated LiveTxn object.   
  
### `Groom`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2243-L2252)
    
    
    Groom()
    

Attempts to apply any outstanding transactions.

The consistency policy determins if a transaction should be applied.

### `SetConsistencyPolicy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2168-L2181)
    
    
    SetConsistencyPolicy(
        policy
    )
    

Set the consistency to use.

Causes all data to be flushed.

Args  
---  
  
`policy` |  A obj inheriting from BaseConsistencyPolicy.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
