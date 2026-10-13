---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore
title: Class BigtableByteStore (0.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:35.308826+00:00
---

# Class BigtableByteStore (0.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BigtableByteStore (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/langchain_google_bigtable.key_value_store.BigtableByteStore)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/langchain_google_bigtable.key_value_store.BigtableByteStore)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/langchain_google_bigtable.key_value_store.BigtableByteStore)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/langchain_google_bigtable.key_value_store.BigtableByteStore)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/langchain_google_bigtable.key_value_store.BigtableByteStore)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/langchain_google_bigtable.key_value_store.BigtableByteStore)


    
    
    BigtableByteStore(
        engine: langchain_google_bigtable.engine.BigtableEngine,
        instance_id: str,
        table_id: str,
        column_family: str = "kv",
        column_qualifier: bytes = b"val",
        app_profile_id: typing.Optional[str] = None,
    )

LangChain Key-value store implementation for Google Cloud Bigtable, supporting both sync and async methods using BigtableEngine.

## Methods 

### _get_async_store
    
    
    _get_async_store(
        **kwargs: typing.Any,
    ) -> langchain_google_bigtable.async_key_value_store.AsyncBigtableByteStore

Returns a AsyncBigtableByteStore object to be used for data operations. If one is not available, a new one is created.

### amdelete
    
    
    amdelete(keys: typing.Sequence[str]) -> None

Asynchronously deletes key-value pairs from the Bigtable.

### amget
    
    
    amget(keys: typing.Sequence[str]) -> typing.List[typing.Optional[bytes]]

Asynchronously retrieves values for a sequence of keys.

It only reads the most recent version for each key.

### amset
    
    
    amset(key_value_pairs: typing.Sequence[typing.Tuple[str, bytes]]) -> None

Asynchronously stores key-value pairs in the Bigtable.

**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If any key is not a string or any value is not bytes.  
  
### ayield_keys
    
    
    ayield_keys(*, prefix: typing.Optional[str] = None) -> typing.AsyncIterator[str]

Asynchronously yields keys matching a given prefix. It only yields the row keys that match the given prefix.

### create
    
    
    create(
        instance_id: str,
        table_id: str,
        *,
        engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None,
        project_id: typing.Optional[str] = None,
        app_profile_id: typing.Optional[str] = None,
        column_family: str = "kv",
        column_qualifier: typing.Union[str, bytes] = b"val",
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.key_value_store.BigtableByteStore

Creates an async-initialized instance of the BigtableByteStore.

This is the standard entry point for asynchronous applications. It will create a new BigtableEngine if one is not provided.

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `str`   
The ID of the Bigtable instance to connect to.  
`table_id` |  `str`   
The ID of the table to use for storing data.  
`engine` |  `BigtableEngine None`   
An optional, existing BigtableEngine to share resources with. If you don't provide an engine, a new one will be created automatically. You can retrieve the created engine by calling the `get_engine()` method on the returned store and reuse it for other stores.  
`project_id` |  `str None`   
The Google Cloud project ID. This is optional and will only be used if an engine is not provided.  
`app_profile_id` |  `str None`   
An optional Bigtable app profile ID for routing requests.  
`column_family` |  `str None`   
The column family to use for storing values. Defaults to "kv".  
`column_qualifier` |  `str None`   
The column qualifier to use for storing values. Can be a string or bytes. Defaults to "val".  
`credentials` |  `google.auth.credentials.Credentials None`   
An optional `google.auth.credentials.Credentials` object to use for authentication. If not provided, the default credentials will be used from the environment.  
`client_options` |  `dict[str, Any] None`   
An optional dictionary of client options to pass to the `BigtableDataClientAsync`.  
  
### create_sync
    
    
    create_sync(
        instance_id: str,
        table_id: str,
        *,
        engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None,
        project_id: typing.Optional[str] = None,
        app_profile_id: typing.Optional[str] = None,
        column_family: str = "kv",
        column_qualifier: typing.Union[str, bytes] = b"val",
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.key_value_store.BigtableByteStore

Creates a sync-initialized instance of the BigtableByteStore.

This is the standard entry point for synchronous applications. It will create a new BigtableEngine if one is not provided.

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `str`   
The ID of the Bigtable instance to connect to.  
`table_id` |  `str`   
The ID of the table to use for storing data.  
`engine` |  `BigtableEngine None`   
An optional, existing BigtableEngine to share resources with. If you don't provide an engine, a new one will be created automatically. You can retrieve the created engine by calling the `get_engine()` method on the returned store and reuse it for other stores.  
`project_id` |  `str None`   
The Google Cloud project ID. This is optional and will only be used if an engine is not provided.  
`app_profile_id` |  `str None`   
An optional Bigtable app profile ID for routing requests.  
`column_family` |  `str None`   
The column family to use for storing values. Defaults to "kv".  
`column_qualifier` |  `str None`   
The column qualifier to use for storing values. Can be a string or bytes. Defaults to "val".  
`credentials` |  `google.auth.credentials.Credentials None`   
An optional `google.auth.credentials.Credentials` object to use for authentication. If not provided, the default credentials will be used from the environment.  
`client_options` |  `dict[str, Any] None`   
An optional dictionary of client options to pass to the `BigtableDataClientAsync`.  
  
### get_engine
    
    
    get_engine() -> langchain_google_bigtable.engine.BigtableEngine

Returns the BigtableEngine being used for this object.

### mdelete
    
    
    mdelete(keys: typing.Sequence[str]) -> None

Synchronously deletes key-value pairs from the Bigtable.

### mget
    
    
    mget(keys: typing.Sequence[str]) -> typing.List[typing.Optional[bytes]]

Synchronously retrieves values for a sequence of keys.

It only reads the most recent version for each key.

### mset
    
    
    mset(key_value_pairs: typing.Sequence[typing.Tuple[str, bytes]]) -> None

Synchronously stores key-value pairs in the Bigtable.

**Exceptions**  
---  
**Type** | **Description**  
`TypeError` | If any key is not a string or any value is not bytes.  
  
### yield_keys
    
    
    yield_keys(*, prefix: typing.Optional[str] = None) -> typing.Iterator[str]

Synchronously yields keys matching a given prefix. It only yields the keys that match the given prefix.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
