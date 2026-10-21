---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_file_stub/DatastoreFileStub/
title: google.appengine.api.datastore_file_stub.DatastoreFileStub \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:37:59.168262+00:00
---

# google.appengine.api.datastore_file_stub.DatastoreFileStub  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/datastore_file_stub/DatastoreFileStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.datastore_file_stub.DatastoreFileStub Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_file_stub.py#L297-L755) Persistent stub for the Python datastore API. Inherits From: [`BaseDatastore`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseDatastore), [`BaseTransactionManager`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseTransactionManager), [`BaseIndexManager`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/BaseIndexManager), [`APIProxyStub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/apiproxy_stub/APIProxyStub), [`DatastoreStub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_stub_util/DatastoreStub), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.datastore_file_stub.DatastoreFileStub(
        app_id,
        datastore_file,
        history_file=None,
        require_indexes=False,
        service_name='datastore_v3',
        trusted=False,
        consistency_policy=None,
        save_changes=True,
        root_path=None,
        use_atexit=True,
        auto_id_policy=datastore_stub_util.SEQUENTIAL
    )
    

Stores all entities in memory, and persists them to a file as pickled protocol buffers. A `DatastoreFileStub` instance handles a single app's data and is backed by files on disk. | 

## Args  
  
---  
  
`app_id` |  String   
`datastore_file` |  String. Stores all entities across sessions. Use `None` not to use a file.   
`history_file` |  DEPRECATE`. No-op. </td> </tr><tr> <td>`require_indexes`</td> <td> Bool. Default is`False`. If`True`, composite indexes must exist in`index.yaml`for queries that need them. </td> </tr><tr> <td>`service_name`</td> <td> Service name is expected for all calls. </td> </tr><tr> <td>`trusted`</td> <td> Bool. Default is`False`. If`True`, this stub allows an app to access the data of another app. </td> </tr><tr> <td>`consistency_policy`</td> <td> The consistency policy to use or`None`to use the default. Consistency policies can be found in`datastore_stub_util.*ConsistencyPolicy`. </td> </tr><tr> <td>`save_changes`</td> <td> Bool. Default is`True`. If this stub should modify`datastore_file`when entities are changed. </td> </tr><tr> <td>`root_path`</td> <td> String. The root path of the app. </td> </tr><tr> <td>`use_atexit`</td> <td> Bool. Indicates if the stub should save itself atexit. </td> </tr><tr> <td>`auto_id_policy`</td> <td> Enum. <a href="../../../../google/appengine/datastore/datastore_stub_util#SEQUENTIAL"><code>datastore_stub_util.SEQUENTIAL</code></a> or`.SCATTERED`.   
  
## Methods

### `BeginTransaction`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2190-L2223)
    
    
    BeginTransaction(
        app,
        allow_multiple_eg,
        previous_transaction=None,
        mode=datastore_pb.BeginTransactionRequest.UNKNOWN
    )
    

Start a transaction on the given app.

Args  
---  
  
`app` |  A string representing the app for which to start the transaction.   
`allow_multiple_eg` |  True if transactions can span multiple entity groups.   
`previous_transaction` |  The transaction to reset.   
`mode` |  Mode of the transaction.   
  
Returns  
---  
A datastore_pb.Transaction() for the created transaction   
  
### `Clear`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_file_stub.py#L389-L401)
    
    
    Clear()
    

Clears the datastore by deleting all currently stored entities and queries.

### `Close`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2995-L2997)
    
    
    Close()
    

Closes the Datastore, writing any buffered data.

### `CreateIndex`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L2442-L2471)
    
    
    CreateIndex(
        index, trusted=False, calling_app=None
    )
    

### `CreateRPC`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L87-L93)
    
    
    CreateRPC()
    

Creates RPC object instance.

Returns  
---  
An instance of RPC.   
  
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

### `MakeSyncCall`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_file_stub.py#L590-L598)
    
    
    MakeSyncCall(
        service, call, request, response, request_id=None
    )
    

The main RPC entry point. Service must be datastore_v3.

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
  
### `QueryHistory`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3272-L3277)
    
    
    QueryHistory()
    

Returns a dict that maps Query PBs to times they've been run.

### `Read`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_file_stub.py#L463-L497)
    
    
    Read()
    

Reads the datastore and history files into memory.

The in-memory query history is cleared, but the datastore is _not_ cleared; the entities in the files are merged into the entities in memory. If you want them to overwrite the in-memory datastore, call `Clear()` before calling `Read()`.

If the datastore file contains an entity with the same app name, kind, and key as an entity already in the datastore, the entity from the file overwrites the entity in the datastore.

Also sets each `ID` counter to one greater than the highest `ID` allocated so far in that counter's `ID` space.

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
  
### `SetError`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/apiproxy_stub.py#L145-L163)
    
    
    SetError(
        error, method=None, error_rate=1
    )
    

Set an error condition that may be raised when calls made to stub.

If a method is specified, the error will only apply to that call. The error rate is applied to the method specified or all calls if method is not set.

Args  
---  
  
`error` |  An instance of [`apiproxy_errors.Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/runtime/apiproxy_errors/Error) or `None` for no error.   
`method` |  A string representing the method that the error will affect.   
`error_rate` |  a number from `[0, 1]` that sets the chance of the error, defaults to `1`.   
  
### `SetTrusted`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_stub_util.py#L3284-L3293)
    
    
    SetTrusted(
        trusted
    )
    

Set/clear the trusted bit in the stub.

This bit indicates that the app calling the stub is trusted. A trusted app can write to datastores of other apps.

Args  
---  
  
`trusted` |  boolean.   
  
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_file_stub.py#L499-L505)
    
    
    Write()
    

Writes out the datastore and history files.

**Important:** If the files already exist, this method overwrites them.

### `assertPbIsInitialized`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/datastore_file_stub.py#L600-L604)
    
    
    assertPbIsInitialized(
        pb
    )
    

Raises an exception if the given `PB` is not initialized and valid.

## Class Variables  
  
---  
  
DELETED |  `3`  
ERROR |  `4`  
READ_ERROR_MSG |  `('Data in %s is corrupt or a different version. Try running with the ' '--clear_datastore flag.\n' '%r')`  
READ_PB_EXCEPTIONS |  `(<class 'google.protobuf.message.DecodeError'>, <class 'LookupError'>, <class 'TypeError'>, <class 'ValueError'>)`  
READ_PY250_MSG |  `('Are you using FloatProperty and/or GeoPtProperty? Unfortunately loading ' 'float values from the datastore file does not work with Python 2.5.0. Please ' 'upgrade to a newer Python 2.5 release or use the --clear_datastore flag.\n')`  
READ_WRITE |  `2`  
THREADSAFE |  `False`  
WRITE_ONLY |  `1`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
