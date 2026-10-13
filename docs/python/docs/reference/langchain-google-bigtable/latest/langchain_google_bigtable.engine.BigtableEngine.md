---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine
title: Class BigtableEngine (0.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:35.738071+00:00
---

# Class BigtableEngine (0.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BigtableEngine (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/langchain_google_bigtable.engine.BigtableEngine)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/langchain_google_bigtable.engine.BigtableEngine)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/langchain_google_bigtable.engine.BigtableEngine)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/langchain_google_bigtable.engine.BigtableEngine)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/langchain_google_bigtable.engine.BigtableEngine)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/langchain_google_bigtable.engine.BigtableEngine)


    
    
    BigtableEngine(
        key: object,
        client: typing.Optional[
            google.cloud.bigtable.data._async.client.BigtableDataClientAsync
        ],
        loop: typing.Optional[asyncio.events.AbstractEventLoop],
        thread: typing.Optional[threading.Thread],
    )

Manages the client and execution context, handling the

async/sync conversion via a background event loop.

This class is the core of the async/sync interoperability, providing a reusable component that can be shared across multiple store instances to conserve resources.

## Properties 

### async_client

The data client property of this class.

## Methods 

### BigtableEngine
    
    
    BigtableEngine(
        key: object,
        client: typing.Optional[
            google.cloud.bigtable.data._async.client.BigtableDataClientAsync
        ],
        loop: typing.Optional[asyncio.events.AbstractEventLoop],
        thread: typing.Optional[threading.Thread],
    )

Initializes the engine with a running event loop and a client.

**Parameters**  
---  
**Name** | **Description**  
`key` |  `object`   
object to prevent direct constructor usage.  
`client` |  `BigtableDataClientAsync`   
The async Bigtable data client.  
`loop` |  `Optional[asyncio.AbstractEventLoop]`   
The asyncio event loop running in the background thread.  
`thread` |  `Optional[Thread]`   
The background thread hosting the event loop.  
  
### __start_background_loop
    
    
    __start_background_loop(
        project_id: typing.Optional[str],
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Any] = None,
        **kwargs: typing.Any
    ) -> concurrent.futures._base.Future

Creates and starts the default background loop and thread

### _create
    
    
    _create(
        project_id: typing.Optional[str] = None,
        loop: typing.Optional[asyncio.events.AbstractEventLoop] = None,
        thread: typing.Optional[threading.Thread] = None,
        client: typing.Optional[
            google.cloud.bigtable.data._async.client.BigtableDataClientAsync
        ] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Any] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.engine.BigtableEngine

Asynchronously instantiates the BigtableEngine Object

### _run_as_async
    
    
    _run_as_async(coro: typing.Any) -> typing.Any

Runs a coroutine on the background loop without blocking the main loop.

This is used for calling from an existing asynchronous context.

### _run_as_sync
    
    
    _run_as_sync(coro: typing.Any) -> typing.Any

Runs a coroutine on the background loop and waits for the result.

This is the core mechanism for providing a synchronous API.

### async_initialize
    
    
    async_initialize(
        project_id: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Any] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.engine.BigtableEngine

Creates a BigtableEngine instance with a background event loop and a new data client asynchronously

**Parameters**  
---  
**Name** | **Description**  
`project_id` |  `Optional[str]`   
Google Cloud Project ID.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
credentials to pass into the data client for this engine.  
`client_options` |  `Optional[Any]`   
Client options used to set user options for the client.  
  
### close
    
    
    close() -> None

Closes the underlying client for this specific engine instance.

### get_async_table
    
    
    get_async_table(
        instance_id: str,
        table_id: str,
        app_profile_id: typing.Optional[str] = None,
        **kwargs: typing.Any
    ) -> google.cloud.bigtable.data._async.client.TableAsync

Returns the table using this class's client

### initialize
    
    
    initialize(
        project_id: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Any] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.engine.BigtableEngine

Creates a BigtableEngine instance with a background event loop and a new data client synchronously.

**Parameters**  
---  
**Name** | **Description**  
`project_id` |  `Optional[str]`   
Google Cloud Project ID.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
credentials to pass into the data client for this engine.  
`client_options` |  `Optional[Any]`   
Client options used to set user options for the client.  
  
### shutdown_default_loop
    
    
    shutdown_default_loop() -> None

Closes the default class-level shared loop and terminates the thread associated with it.

Note: Calling this method will prevent any new BigtableEngine instances from using the shared event loop. Additionally, after this method is called it will not be possible to run more coroutines in the previous loop.

**Exceptions**  
---  
**Type** | **Description**  
`Exception` | If the thread does not terminate within the timeout period.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
