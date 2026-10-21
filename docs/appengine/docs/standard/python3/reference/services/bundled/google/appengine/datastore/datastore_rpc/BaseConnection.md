---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/BaseConnection/
title: google.appengine.datastore.datastore_rpc.BaseConnection \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:27:05.050815+00:00
---

# google.appengine.datastore.datastore_rpc.BaseConnection  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/datastore/datastore_rpc/BaseConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.datastore.datastore_rpc.BaseConnection Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L987-L2080) Datastore connection base class. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.datastore.datastore_rpc.BaseConnection(
        adapter=None, config=None, _api_version=_DATASTORE_V3
    )
    

NOTE: Do not instantiate this class; use Connection or TransactionalConnection instead. This is not a traditional database connection -- with App Engine, in the end the connection is always implicit in the process state. There is also no intent to be compatible with PEP 249 (Python's Database-API). But it is a useful abstraction to have an explicit object that manages the database interaction, and especially transactions. Other settings related to the App Engine datastore are also stored here (e.g. the RPC timeout). A similar class in the Java API to the App Engine datastore is DatastoreServiceConfig (but in Java, transaction state is always held by the current thread). To use transactions, call connection.new_transaction(). This returns a new connection (an instance of the TransactionalConnection subclass) which you should use for all operations in the transaction. This model supports multiple unrelated concurrent transactions (but not nested transactions as this concept is commonly understood in the relational database world). When the transaction is done, call .commit() or .rollback() on the transactional connection. If .commit() returns False, the transaction failed and none of your operations made it to the datastore; if it returns True, all your operations were committed. The transactional connection cannot be used once .commit() or .rollback() is called. Transactions are created lazily. The first operation that requires a transaction handle will issue the low-level BeginTransaction request and wait for it to return. Transactions keep track of the entity group. All operations within a transaction must use the same entity group. An entity group (currently) comprises an app id, a namespace, and a top-level key (a kind and an id or name). The first operation performed determines the entity group. There is some special-casing when the first operation is a put() of an entity with an incomplete key; in this case the entity group is determined after the operation returns. NOTE: the datastore stubs in the dev_appserver currently support only a single concurrent transaction. Specifically, the (old) file stub locks up if an attempt is made to start a new transaction while a transaction is already in use, whereas the sqlite stub fails an assertion. | 

## Args  
  
---  
  
`adapter` |  Optional AbstractAdapter subclass instance; default IdentityAdapter.   
`config` |  Optional Configuration object.   
  
## Attributes  
  
---  
  
`adapter` |  The adapter used by this connection.   
`config` |  The default configuration used by this connection.   
  
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
  
### `async_delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1909-L1976)
    
    
    async_delete(
        config, keys, extra_hook=None
    )
    

Asynchronous Delete operation.

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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1798-L1871)
    
    
    async_put(
        config, entities, extra_hook=None
    )
    

Asynchronous Put operation.

Args  
---  
config: A Configuration object or None. Defaults are taken from the connection's default configuration. entities: An iterable of user-level entity objects. extra_hook: Optional function to be called on the result once the RPC has completed.   
`Returns` |  A MultiRpc object.   
  
NOTE: If any of the entities has an incomplete key, this will _not_ patch up those entities with the complete key.

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

### `wait_for_all_pending_rpcs`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/datastore/datastore_rpc.py#L1158-L1188)
    
    
    wait_for_all_pending_rpcs()
    

Wait for all currently pending RPCs to complete.

## Class Variables  
  
---  
  
DEFAULT_MAX_ENTITY_GROUPS_PER_RPC |  `10`  
HIGH_REPLICATION_DATASTORE |  `2`  
MAX_ALLOCATE_IDS_KEYS |  `500`  
MAX_DELETE_KEYS |  `500`  
MAX_GET_KEYS |  `1000`  
MAX_PUT_ENTITIES |  `500`  
MAX_RPC_BYTES |  `1048576`  
UNKNOWN_DATASTORE |  `0`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
