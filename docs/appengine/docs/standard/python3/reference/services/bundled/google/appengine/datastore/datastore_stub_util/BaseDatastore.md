---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseDatastore/
title: google.appengine.datastore.datastore_stub_util.BaseDatastore \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:38:18.339844+00:00
---

# google.appengine.datastore.datastore_stub_util.BaseDatastore  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseDatastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_stub_util.BaseDatastore Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2536-L3056) A base implementation of a Datastore. Inherits From: [`BaseTransactionManager`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseTransactionManager), [`BaseIndexManager`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseIndexManager), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_stub_util.BaseDatastore(
        require_indexes=False,
        consistency_policy=None,
        use_atexit=True,
        auto_id_policy=SEQUENTIAL
    )
    

This class implements common functions associated with a datastore and enforces security restrictions passed on by a stub or client. It is designed to be shared by any number of threads or clients serving any number of apps. If an app is not specified explicitly it is pulled from the env and assumed to be untrusted.

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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2575-L2578)
    
    
    Clear()
    

Clears out all stored values.

### `Close`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2995-L2997)
    
    
    Close()
    

Closes the Datastore, writing any buffered data.

### `CreateIndex`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2442-L2471)
    
    
    CreateIndex(
        index, trusted=False, calling_app=None
    )
    

### `Delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2836-L2888)
    
    
    Delete(
        raw_keys, cost, transaction=None, trusted=False, calling_app=None
    )
    

Deletes the entities associated with the given keys.

Args  
---  
  
`raw_keys` |  A list of unverified entity_pb2.Reference objects.   
`cost` |  Out param. The cost of putting the provided entities.   
`transaction` |  The datastore_pb.Transaction() to use or None.   
`trusted` |  If the calling app is trusted.   
`calling_app` |  The app requesting the results or None to pull the app from the environment.   
  
Returns  
---  
A list of versions numbers at which the entities were deleted, one for each given keys. Every version numbers are None if a transaction is given.   
  
### `DeleteIndex`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2498-L2512)
    
    
    DeleteIndex(
        index, trusted=False, calling_app=None
    )
    

### `Flush`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2254-L2269)
    
    
    Flush()
    

Applies all outstanding transactions.

### `Get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2668-L2724)
    
    
    Get(
        raw_keys,
        transaction=None,
        eventual_consistency=False,
        trusted=False,
        calling_app=None
    )
    

Get the entity records for the given keys.

Args  
---  
  
`raw_keys` |  A list of unverified entity_pb2.Reference objects.   
`transaction` |  The datastore_pb.Transaction to use or None.   
`eventual_consistency` |  If we should allow stale, potentially inconsistent results.   
`trusted` |  If the calling app is trusted.   
`calling_app` |  The app requesting the results or None to pull the app from the environment.   
  
Returns  
---  
A list containing the records in the same order as the list of keys.   
  
### `GetIndexes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2473-L2478)
    
    
    GetIndexes(
        app, trusted=False, calling_app=None
    )
    

Get the CompositeIndex objects for the given app.

### `GetQueryCursor`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2589-L2639)
    
    
    GetQueryCursor(
        raw_query, trusted=False, calling_app=None
    )
    

Execute a query.

Args  
---  
  
`raw_query` |  The non-validated datastore_pb.Query to run.   
`trusted` |  If the calling app is trusted.   
`calling_app` |  The app requesting the results or None to pull the app from the environment.   
  
Returns  
---  
A BaseCursor that can be used to retrieve results.   
  
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

### `Put`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2745-L2834)
    
    
    Put(
        raw_entities, cost, transaction=None, trusted=False, calling_app=None
    )
    

Writes the given given entities.

Updates an entity's key and entity_group in place if needed

Args  
---  
  
`raw_entities` |  A list of unverified entity_pb2.EntityProto objects.   
`cost` |  Out param. The cost of putting the provided entities.   
`transaction` |  The datastore_pb.Transaction() to use or None.   
`trusted` |  If the calling app is trusted.   
`calling_app` |  The app requesting the results or None to pull the app from the environment.   
  
Returns  
---  
A list of tuple (entity_pb2.Reference, version number) that indicates where each entity was stored and at which version. When a transaction is provided, all version numbers are None.   
  
### `SetAutoIdPolicy`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2975-L2987)
    
    
    SetAutoIdPolicy(
        auto_id_policy
    )
    

Set value of _auto_id_policy flag (default SEQUENTIAL).

SEQUENTIAL auto ID assignment behavior will eventually be deprecated and the default will be SCATTERED.

Args  
---  
  
`auto_id_policy` |  string constant.   
  
Raises  
---  
  
`TypeError` |  if auto_id_policy is not one of SEQUENTIAL or SCATTERED.   
  
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
  
### `Touch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2890-L2902)
    
    
    Touch(
        raw_keys, trusted=False, calling_app=None
    )
    

Applies all outstanding writes.

### `UpdateIndex`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2480-L2496)
    
    
    UpdateIndex(
        index, trusted=False, calling_app=None
    )
    

### `Write`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2991-L2993)
    
    
    Write()
    

Writes the datastore to disk.

## Class Variables  
  
---  
  
DELETED |  `3`  
ERROR |  `4`  
READ_WRITE |  `2`  
WRITE_ONLY |  `1`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
