---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/TransactionalConnection/
title: google.appengine.datastore.datastore_rpc.TransactionalConnection \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:42:17.349189+00:00
---

# google.appengine.datastore.datastore_rpc.TransactionalConnection  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/TransactionalConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_rpc.TransactionalConnection Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L2338-L2720) A connection specific to one transaction. Inherits From: [`BaseConnection`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/BaseConnection), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_rpc.TransactionalConnection(
        adapter=None,
        config=None,
        transaction=None,
        entity_group=None,
        _api_version=_DATASTORE_V3,
        previous_transaction=None,
        mode=TransactionMode.UNKNOWN
    )
    

It is possible to pass the transaction and entity group to the constructor, but typically the transaction is lazily created by _get_transaction() when the first operation is started. | 

## Args  
  
---  
  
`adapter` |  Optional AbstractAdapter subclass instance; default IdentityAdapter.   
`config` |  Optional Configuration object.   
`transaction` |  Optional datastore_db.Transaction object.   
`entity_group` |  Deprecated, do not use.   
`previous_transaction` |  Optional datastore_db.Transaction object representing the transaction being reset.   
`mode` |  Optional datastore_db.TransactionMode representing the transaction mode.   
  
## Raises  
  
---  
  
`datastore_errors.BadArgumentError` |  If previous_transaction and transaction are both set.   
  
## Attributes  
  
---  
  
`adapter` |  The adapter used by this connection.   
`config` |  The default configuration used by this connection.   
`finished` |   
`transaction` |  The current transaction. None when state == FINISHED.   
  
## Methods

### `async_begin_transaction`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L2008-L2072)
    
    
    async_begin_transaction(
        config, app, previous_transaction=None, mode=TransactionMode.UNKNOWN
    )
    

Asynchronous BeginTransaction operation.

Args  
---  
  
`config` |  A configuration object or None. Defaults are taken from the connection's default configuration.   
`app` |  Application ID.   
`previous_transaction` |  The transaction to reset.   
`mode` |  The transaction mode.   
  
Returns  
---  
A MultiRpc object.   
  
### `async_commit`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L2610-L2656)
    
    
    async_commit(
        config
    )
    

Asynchronous Commit operation.

Args  
---  
  
`config` |  A Configuration object or None. Defaults are taken from the connection's default configuration.   
  
Returns  
---  
A MultiRpc object.   
  
### `async_delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L2552-L2586)
    
    
    async_delete(
        config, keys, extra_hook=None
    )
    

Transactional asynchronous Delete operation.

Args  
---  
  
`config` |  A Configuration object or None. Defaults are taken from the connection's default configuration.   
`keys` |  An iterable of user-level key objects.   
`extra_hook` |  Optional function to be called once the RPC has completed.   
  
Returns  
---  
A MultiRpc object.   
  
### `async_get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1560-L1640)
    
    
    async_get(
        config, keys, extra_hook=None
    )
    

Asynchronous Get operation.

Args  
---  
  
`config` |  A Configuration object or None. Defaults are taken from the connection's default configuration.   
`keys` |  An iterable of user-level key objects.   
`extra_hook` |  Optional function to be called on the result once the RPC has completed.   
  
Returns  
---  
A MultiRpc object.   
  
### `async_get_indexes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1754-L1771)
    
    
    async_get_indexes(
        config, extra_hook=None, _app=None
    )
    

Asynchronous get indexes operation.

Args  
---  
  
`config` |  A Configuration object or None. Defaults are taken from the connection's default configuration.   
`extra_hook` |  Optional function to be called once the RPC has completed.   
  
Returns  
---  
A MultiRpc object.   
  
### `async_put`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L2462-L2502)
    
    
    async_put(
        config, entities, extra_hook=None
    )
    

Transactional asynchronous Put operation.

Args  
---  
config: A Configuration object or None. Defaults are taken from the connection's default configuration. entities: An iterable of user-level entity objects. extra_hook: Optional function to be called on the result once the RPC has completed.   
`Returns` |  A MultiRpc object.   
  
NOTE: If any of the entities has an incomplete key, this will _not_ patch up those entities with the complete key.

### `async_rollback`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L2682-L2716)
    
    
    async_rollback(
        config
    )
    

Asynchronous Rollback operation.

Args  
---  
config: A Configuration object or None. Defaults are taken from the connection's default configuration.   
`Returns` |  A MultiRpc object.   
  
### `begin_transaction`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1987-L2006)
    
    
    begin_transaction(
        app, previous_transaction=None, mode=TransactionMode.UNKNOWN
    )
    

Synchronous BeginTransaction operation.

NOTE: In most cases the new_transaction() method is preferred, since that returns a TransactionalConnection object which will begin the transaction lazily.

Args  
---  
  
`app` |  Application ID.   
`previous_transaction` |  The transaction to reset.   
`mode` |  The transaction mode.   
  
Returns  
---  
An object representing a transaction or None.   
  
### `check_rpc_success`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1343-L1367)
    
    
    check_rpc_success(
        rpc
    )
    

Check for RPC success and translate exceptions.

This wraps rpc.check_success() and should be called instead of that.

This also removes the RPC from the list of pending RPCs, once it has completed.

Args  
---  
  
`rpc` |  A UserRPC or MultiRpc object.   
  
Raises  
---  
Nothing if the call succeeded; various datastore_errors.Error subclasses if ApplicationError was raised by rpc.check_success().   
  
### `commit`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L2595-L2608)
    
    
    commit()
    

Synchronous Commit operation.

Returns  
---  
True if the transaction was successfully committed. False if the backend reported a concurrent transaction error.   
  
### `create_rpc`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1193-L1231)
    
    
    create_rpc(
        config=None, service_name=None
    )
    

Create an RPC object using the configuration parameters.

Internal only.

Args  
---  
  
`config` |  Optional Configuration object.   
`service_name` |  Optional datastore service name.   
  
Returns  
---  
A new UserRPC object with the designated settings.   
  
#### NOTES:

(1) The RPC object returned can only be used to make a single call (for details see apiproxy_stub_map.UserRPC).

(2) To make a call, use one of the specific methods on the Connection object, such as conn.put(entities). This sends the call to the server but does not wait. To wait for the call to finish and get the result, call rpc.get_result().

### `delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1898-L1907)
    
    
    delete(
        keys
    )
    

Synchronous Delete operation.

Args  
---  
  
`keys` |  An iterable of user-level key objects.   
  
Returns  
---  
None.   
  
### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1547-L1558)
    
    
    get(
        keys
    )
    

Synchronous Get operation.

Args  
---  
  
`keys` |  An iterable of user-level key objects.   
  
Returns  
---  
A list of user-level entity objects and None values, corresponding 1:1 to the argument keys. A None means there is no entity for the corresponding key.   
  
### `get_datastore_type`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1150-L1156)
    
    
    get_datastore_type(
        app=None
    )
    

Tries to get the datastore type for the given app.

This function is only guaranteed to return something other than UNKNOWN_DATASTORE when running in production and querying the current app.

### `get_indexes`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1746-L1752)
    
    
    get_indexes()
    

Synchronous get indexes operation.

Returns  
---  
user-level indexes representation   
  
### `get_pending_rpcs`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1146-L1148)
    
    
    get_pending_rpcs()
    

Return (a copy of) the list of currently pending RPCs.

### `is_pending`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1126-L1144)
    
    
    is_pending(
        rpc
    )
    

Check whether an RPC object is currently pending.

Note that 'pending' in this context refers to an RPC associated with this connection for which _remove_pending() hasn't been called yet; normally this is called by check_rpc_success() which itself is called by the various result hooks. A pending RPC may be in the RUNNING or FINISHING state.

If the argument is a MultiRpc object, this returns true if at least one of its wrapped RPCs is pending.

### `make_rpc_call`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1304-L1338)
    
    
    make_rpc_call(
        config,
        method,
        request,
        response,
        get_result_hook=None,
        user_data=None,
        service_name=None
    )
    

Make an RPC call.

Internal only.

Except for the added config argument, this is a thin wrapper around UserRPC.make_call().

Args  
---  
  
`config` |  A Configuration object or None. Defaults are taken from the connection's default configuration.   
`method` |  The method name.   
`request` |  The request protocol buffer.   
`response` |  The response protocol buffer.   
`get_result_hook` |  Optional get-result hook function. If not None, this must be a function with exactly one argument, the RPC object (self). Its return value is returned from get_result().   
`user_data` |  Optional additional arbitrary data for the get-result hook function. This can be accessed as rpc.user_data. The type of this value is up to the service module.   
  
Returns  
---  
The UserRPC object used for the call.   
  
### `put`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1783-L1796)
    
    
    put(
        entities
    )
    

Synchronous Put operation.

Args  
---  
  
`entities` |  An iterable of user-level entity objects.   
  
Returns  
---  
A list of user-level key objects, corresponding 1:1 to the argument entities.   
  
NOTE: If any of the entities has an incomplete key, this will _not_ patch up those entities with the complete key.

### `rollback`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L2675-L2680)
    
    
    rollback()
    

Synchronous Rollback operation.

### `wait_for_all_pending_rpcs`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1158-L1188)
    
    
    wait_for_all_pending_rpcs()
    

Wait for all currently pending RPCs to complete.

## Class Variables  
  
---  
  
CLOSED |  `3`  
COMMIT_IN_FLIGHT |  `1`  
DEFAULT_MAX_ENTITY_GROUPS_PER_RPC |  `10`  
FAILED |  `2`  
HIGH_REPLICATION_DATASTORE |  `2`  
MAX_ALLOCATE_IDS_KEYS |  `500`  
MAX_DELETE_KEYS |  `500`  
MAX_GET_KEYS |  `1000`  
MAX_PUT_ENTITIES |  `500`  
MAX_RPC_BYTES |  `1048576`  
OPEN |  `0`  
UNKNOWN_DATASTORE |  `0`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
