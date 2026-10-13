---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/summary_method/
title: Package Methods (0.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:35.083221+00:00
---

# Package Methods (0.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/summary_method/)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/summary_method/)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/summary_method/)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/summary_method/)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/summary_method/)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/summary_method/)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/summary_method/)



Summary of entries of Methods for langchain-google-bigtable.

## 

### langchain_google_bigtable.chat_message_history.init_chat_history_table
    
    
    init_chat_history_table(
        instance_id: str,
        table_id: str,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
    ) -> None

Create a table to store chat history.

See more: [langchain_google_bigtable.chat_message_history.init_chat_history_table](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.chat_message_history#langchain_google_bigtable_chat_message_history_init_chat_history_table)

### langchain_google_bigtable.key_value_store.init_key_value_store_table
    
    
    init_key_value_store_table(
        instance_id: str,
        table_id: str,
        project_id: typing.Optional[str] = None,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        column_families: typing.List[str] = ["kv"],
    ) -> None

Create a table for saving of LangChain Key-value pairs.

See more: [langchain_google_bigtable.key_value_store.init_key_value_store_table](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store#langchain_google_bigtable_key_value_store_init_key_value_store_table)

### langchain_google_bigtable.loader.init_document_table
    
    
    init_document_table(
        instance_id: str,
        table_id: str,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        content_column_family: str = "langchain",
        metadata_mappings: typing.List[
            langchain_google_bigtable.loader.MetadataMapping
        ] = [],
        metadata_as_json_column_family: typing.Optional[str] = None,
    ) -> None

Create a table for saving of langchain documents.

See more: [langchain_google_bigtable.loader.init_document_table](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader#langchain_google_bigtable_loader_init_document_table)

### langchain_google_bigtable.vector_store.init_vector_store_table
    
    
    init_vector_store_table(
        instance_id: str,
        table_id: str,
        project_id: typing.Optional[str] = None,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        content_column_family: str = "langchain",
        embedding_column_family: str = "langchain",
    ) -> None

Creates a Bigtable table with the necessary column families for the vector store.

See more: [langchain_google_bigtable.vector_store.init_vector_store_table](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store#langchain_google_bigtable_vector_store_init_vector_store_table)

### langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory.add_message
    
    
    add_message(message: langchain_core.messages.base.BaseMessage) -> None

Write a message to the table.

See more: [langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory.add_message](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory#langchain_google_bigtable_chat_message_history_BigtableChatMessageHistory_add_message)

### langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory.add_messages
    
    
    add_messages(
        messages: typing.Sequence[langchain_core.messages.base.BaseMessage],
    ) -> None

Write messages to the table.

See more: [langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory.add_messages](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory#langchain_google_bigtable_chat_message_history_BigtableChatMessageHistory_add_messages)

### langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory.clear
    
    
    clear() -> None

Clear session memory from DB.

See more: [langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory.clear](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory#langchain_google_bigtable_chat_message_history_BigtableChatMessageHistory_clear)

### langchain_google_bigtable.engine.BigtableEngine
    
    
    BigtableEngine(
        key: object,
        client: typing.Optional[
            google.cloud.bigtable.data._async.client.BigtableDataClientAsync
        ],
        loop: typing.Optional[asyncio.events.AbstractEventLoop],
        thread: typing.Optional[threading.Thread],
    )

Initializes the engine with a running event loop and a client.

See more: [langchain_google_bigtable.engine.BigtableEngine](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine_BigtableEngine)

### langchain_google_bigtable.engine.BigtableEngine.__start_background_loop
    
    
    __start_background_loop(
        project_id: typing.Optional[str],
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Any] = None,
        **kwargs: typing.Any
    ) -> concurrent.futures._base.Future

Creates and starts the default background loop and thread.

See more: [langchain_google_bigtable.engine.BigtableEngine.__start_background_loop](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine___start_background_loop)

### langchain_google_bigtable.engine.BigtableEngine._create
    
    
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

Asynchronously instantiates the BigtableEngine Object.

See more: [langchain_google_bigtable.engine.BigtableEngine._create](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine__create)

### langchain_google_bigtable.engine.BigtableEngine._run_as_async
    
    
    _run_as_async(coro: typing.Any) -> typing.Any

Runs a coroutine on the background loop without blocking the main loop.

See more: [langchain_google_bigtable.engine.BigtableEngine._run_as_async](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine__run_as_async)

### langchain_google_bigtable.engine.BigtableEngine._run_as_sync
    
    
    _run_as_sync(coro: typing.Any) -> typing.Any

Runs a coroutine on the background loop and waits for the result.

See more: [langchain_google_bigtable.engine.BigtableEngine._run_as_sync](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine__run_as_sync)

### langchain_google_bigtable.engine.BigtableEngine.async_initialize
    
    
    async_initialize(
        project_id: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Any] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.engine.BigtableEngine

Creates a BigtableEngine instance with a background event loop and a new data client asynchronously .

See more: [langchain_google_bigtable.engine.BigtableEngine.async_initialize](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine_async_initialize)

### langchain_google_bigtable.engine.BigtableEngine.close
    
    
    close() -> None

Closes the underlying client for this specific engine instance.

See more: [langchain_google_bigtable.engine.BigtableEngine.close](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine_close)

### langchain_google_bigtable.engine.BigtableEngine.get_async_table
    
    
    get_async_table(
        instance_id: str,
        table_id: str,
        app_profile_id: typing.Optional[str] = None,
        **kwargs: typing.Any
    ) -> google.cloud.bigtable.data._async.client.TableAsync

Returns the table using this class's client.

See more: [langchain_google_bigtable.engine.BigtableEngine.get_async_table](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine_get_async_table)

### langchain_google_bigtable.engine.BigtableEngine.initialize
    
    
    initialize(
        project_id: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        client_options: typing.Optional[typing.Any] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.engine.BigtableEngine

Creates a BigtableEngine instance with a background event loop and a new data client synchronously.

See more: [langchain_google_bigtable.engine.BigtableEngine.initialize](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine_initialize)

### langchain_google_bigtable.engine.BigtableEngine.shutdown_default_loop
    
    
    shutdown_default_loop() -> None

Closes the default class-level shared loop and terminates the thread associated with it.

See more: [langchain_google_bigtable.engine.BigtableEngine.shutdown_default_loop](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine#langchain_google_bigtable_engine_BigtableEngine_shutdown_default_loop)

### langchain_google_bigtable.key_value_store.BigtableByteStore._get_async_store
    
    
    _get_async_store(
        **kwargs: typing.Any,
    ) -> langchain_google_bigtable.async_key_value_store.AsyncBigtableByteStore

Returns a AsyncBigtableByteStore object to be used for data operations.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore._get_async_store](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore__get_async_store)

### langchain_google_bigtable.key_value_store.BigtableByteStore.amdelete
    
    
    amdelete(keys: typing.Sequence[str]) -> None

Asynchronously deletes key-value pairs from the Bigtable.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.amdelete](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_amdelete)

### langchain_google_bigtable.key_value_store.BigtableByteStore.amget
    
    
    amget(keys: typing.Sequence[str]) -> typing.List[typing.Optional[bytes]]

Asynchronously retrieves values for a sequence of keys.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.amget](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_amget)

### langchain_google_bigtable.key_value_store.BigtableByteStore.amset
    
    
    amset(key_value_pairs: typing.Sequence[typing.Tuple[str, bytes]]) -> None

Asynchronously stores key-value pairs in the Bigtable.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.amset](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_amset)

### langchain_google_bigtable.key_value_store.BigtableByteStore.ayield_keys
    
    
    ayield_keys(*, prefix: typing.Optional[str] = None) -> typing.AsyncIterator[str]

Asynchronously yields keys matching a given prefix.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.ayield_keys](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_ayield_keys)

### langchain_google_bigtable.key_value_store.BigtableByteStore.create
    
    
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

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.create](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_create)

### langchain_google_bigtable.key_value_store.BigtableByteStore.create_sync
    
    
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

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.create_sync](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_create_sync)

### langchain_google_bigtable.key_value_store.BigtableByteStore.get_engine
    
    
    get_engine() -> langchain_google_bigtable.engine.BigtableEngine

Returns the BigtableEngine being used for this object.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.get_engine](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_get_engine)

### langchain_google_bigtable.key_value_store.BigtableByteStore.mdelete
    
    
    mdelete(keys: typing.Sequence[str]) -> None

Synchronously deletes key-value pairs from the Bigtable.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.mdelete](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_mdelete)

### langchain_google_bigtable.key_value_store.BigtableByteStore.mget
    
    
    mget(keys: typing.Sequence[str]) -> typing.List[typing.Optional[bytes]]

Synchronously retrieves values for a sequence of keys.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.mget](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_mget)

### langchain_google_bigtable.key_value_store.BigtableByteStore.mset
    
    
    mset(key_value_pairs: typing.Sequence[typing.Tuple[str, bytes]]) -> None

Synchronously stores key-value pairs in the Bigtable.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.mset](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_mset)

### langchain_google_bigtable.key_value_store.BigtableByteStore.yield_keys
    
    
    yield_keys(*, prefix: typing.Optional[str] = None) -> typing.Iterator[str]

Synchronously yields keys matching a given prefix.

See more: [langchain_google_bigtable.key_value_store.BigtableByteStore.yield_keys](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore#langchain_google_bigtable_key_value_store_BigtableByteStore_yield_keys)

### langchain_google_bigtable.loader.BigtableLoader
    
    
    BigtableLoader(
        instance_id: str,
        table_id: str,
        row_set: typing.Optional[google.cloud.bigtable.row_set.RowSet] = None,
        filter: typing.Optional[google.cloud.bigtable.row_filters.RowFilter] = None,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        content_encoding: langchain_google_bigtable.loader.Encoding = Encoding.UTF8,
        content_column_family: str = "langchain",
        content_column_name: str = "content",
        metadata_mappings: typing.List[
            langchain_google_bigtable.loader.MetadataMapping
        ] = [],
        metadata_as_json_column_family: typing.Optional[str] = None,
        metadata_as_json_column_name: typing.Optional[str] = None,
        metadata_as_json_encoding: langchain_google_bigtable.loader.Encoding = Encoding.UTF8,
    )

Initialize Bigtable document loader.

See more: [langchain_google_bigtable.loader.BigtableLoader](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableLoader#langchain_google_bigtable_loader_BigtableLoader_BigtableLoader)

### langchain_google_bigtable.loader.BigtableLoader.lazy_load
    
    
    lazy_load() -> typing.Iterator[langchain_core.documents.base.Document]

A lazy loader for Documents.

See more: [langchain_google_bigtable.loader.BigtableLoader.lazy_load](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableLoader#langchain_google_bigtable_loader_BigtableLoader_lazy_load)

### langchain_google_bigtable.loader.BigtableLoader.load
    
    
    load() -> typing.List[langchain_core.documents.base.Document]

Load data into Document objects.

See more: [langchain_google_bigtable.loader.BigtableLoader.load](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableLoader#langchain_google_bigtable_loader_BigtableLoader_load)

### langchain_google_bigtable.loader.BigtableSaver
    
    
    BigtableSaver(
        instance_id: str,
        table_id: str,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        content_encoding: langchain_google_bigtable.loader.Encoding = Encoding.UTF8,
        content_column_family: str = "langchain",
        content_column_name: str = "content",
        metadata_mappings: typing.List[
            langchain_google_bigtable.loader.MetadataMapping
        ] = [],
        metadata_as_json_column_family: typing.Optional[str] = None,
        metadata_as_json_column_name: typing.Optional[str] = None,
        metadata_as_json_encoding: langchain_google_bigtable.loader.Encoding = Encoding.UTF8,
    )

Initialize Bigtable document saver.

See more: [langchain_google_bigtable.loader.BigtableSaver](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableSaver#langchain_google_bigtable_loader_BigtableSaver_BigtableSaver)

### langchain_google_bigtable.loader.BigtableSaver.add_documents
    
    
    add_documents(docs: typing.List[langchain_core.documents.base.Document]) -> None

Save documents in the DocumentSaver table.

See more: [langchain_google_bigtable.loader.BigtableSaver.add_documents](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableSaver#langchain_google_bigtable_loader_BigtableSaver_add_documents)

### langchain_google_bigtable.loader.BigtableSaver.delete
    
    
    delete(docs: typing.List[langchain_core.documents.base.Document]) -> None

Delete all instances of a document from the DocumentSaver table by matching the entire Document object.

See more: [langchain_google_bigtable.loader.BigtableSaver.delete](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableSaver#langchain_google_bigtable_loader_BigtableSaver_delete)

### langchain_google_bigtable.vector_store.BigtableVectorStore
    
    
    BigtableVectorStore(instance_id: str, table_id: str, embedding_service: langchain_core.embeddings.embeddings.Embeddings, collection: str, content_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='content', column_family='langchain', encoding=

Initializes the BigtableVectorStore.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_BigtableVectorStore)

### langchain_google_bigtable.vector_store.BigtableVectorStore._get_async_store
    
    
    _get_async_store() -> (
        langchain_google_bigtable.async_vector_store.AsyncBigtableVectorStore
    )

Lazily initializes and returns the underlying async store.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore._get_async_store](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore__get_async_store)

### langchain_google_bigtable.vector_store.BigtableVectorStore.aadd_documents
    
    
    aadd_documents(
        documents: typing.List[langchain_core.documents.base.Document],
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> typing.List[str]

Run more documents through the embeddings and add to the vectorstore.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.aadd_documents](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_aadd_documents)

### langchain_google_bigtable.vector_store.BigtableVectorStore.aadd_texts
    
    
    aadd_texts(
        texts: typing.Iterable[str],
        metadatas: typing.Optional[typing.List[dict]] = None,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> typing.List[str]

Run more texts through the embeddings and add to the vectorstore.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.aadd_texts](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_aadd_texts)

### langchain_google_bigtable.vector_store.BigtableVectorStore.add_documents
    
    
    add_documents(
        documents: typing.List[langchain_core.documents.base.Document],
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> typing.List[str]

Run more documents through the embeddings and add to the vectorstore.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.add_documents](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_add_documents)

### langchain_google_bigtable.vector_store.BigtableVectorStore.add_texts
    
    
    add_texts(
        texts: typing.Iterable[str],
        metadatas: typing.Optional[typing.List[typing.Dict]] = None,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> typing.List[str]

Run more texts through the embeddings and add to the vectorstore.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.add_texts](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_add_texts)

### langchain_google_bigtable.vector_store.BigtableVectorStore.adelete
    
    
    adelete(
        ids: typing.Optional[typing.List[str]] = None, **kwargs: typing.Any
    ) -> typing.Optional[bool]

Delete by vector ID.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.adelete](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_adelete)

### langchain_google_bigtable.vector_store.BigtableVectorStore.afrom_documents
    
    
    afrom_documents(
        documents: typing.List[langchain_core.documents.base.Document],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Return VectorStore initialized from documents and embeddings.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.afrom_documents](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_afrom_documents)

### langchain_google_bigtable.vector_store.BigtableVectorStore.afrom_texts
    
    
    afrom_texts(
        texts: typing.List[str],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        metadatas: typing.Optional[typing.List[dict]] = None,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Return VectorStore initialized from texts and embeddings.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.afrom_texts](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_afrom_texts)

### langchain_google_bigtable.vector_store.BigtableVectorStore.aget_by_ids
    
    
    aget_by_ids(
        ids: typing.Sequence[str],
    ) -> typing.List[langchain_core.documents.base.Document]

Return documents by their IDs.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.aget_by_ids](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_aget_by_ids)

### langchain_google_bigtable.vector_store.BigtableVectorStore.amax_marginal_relevance_search
    
    
    amax_marginal_relevance_search(
        query: str,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs selected using the maximal marginal relevance.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.amax_marginal_relevance_search](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_amax_marginal_relevance_search)

### langchain_google_bigtable.vector_store.BigtableVectorStore.amax_marginal_relevance_search_by_vector
    
    
    amax_marginal_relevance_search_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs selected using the maximal marginal relevance.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.amax_marginal_relevance_search_by_vector](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_amax_marginal_relevance_search_by_vector)

### langchain_google_bigtable.vector_store.BigtableVectorStore.as_retriever
    
    
    as_retriever(
        **kwargs: typing.Any,
    ) -> langchain_core.vectorstores.base.VectorStoreRetriever

Return VectorStoreRetriever initialized from this VectorStore.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.as_retriever](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_as_retriever)

### langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search
    
    
    asimilarity_search(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs most similar to query.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_asimilarity_search)

### langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search_by_vector
    
    
    asimilarity_search_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs most similar to embedding vector.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search_by_vector](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_asimilarity_search_by_vector)

### langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search_with_relevance_scores
    
    
    asimilarity_search_with_relevance_scores(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Return docs and relevance scores in the range [0, 1].

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search_with_relevance_scores](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_asimilarity_search_with_relevance_scores)

### langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search_with_score
    
    
    asimilarity_search_with_score(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Run similarity search with distance.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search_with_score](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_asimilarity_search_with_score)

### langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search_with_score_by_vector
    
    
    asimilarity_search_with_score_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Run similarity search with distance by vector.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.asimilarity_search_with_score_by_vector](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_asimilarity_search_with_score_by_vector)

### langchain_google_bigtable.vector_store.BigtableVectorStore.close
    
    
    close() -> None

Close the engine connection.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.close](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_close)

### langchain_google_bigtable.vector_store.BigtableVectorStore.create
    
    
    create(instance_id: str, table_id: str, embedding_service: langchain_core.embeddings.embeddings.Embeddings, collection: str, engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None, content_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='content', column_family='langchain', encoding=

Asynchronously initializes the engine and creates an instance of the vector store.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.create](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_create)

### langchain_google_bigtable.vector_store.BigtableVectorStore.create_sync
    
    
    create_sync(instance_id: str, table_id: str, embedding_service: langchain_core.embeddings.embeddings.Embeddings, collection: str, engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None, content_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='content', column_family='langchain', encoding=

Synchronously initializes the engine and creates an instance of the vector store.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.create_sync](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_create_sync)

### langchain_google_bigtable.vector_store.BigtableVectorStore.delete
    
    
    delete(
        ids: typing.Optional[typing.List[str]] = None, **kwargs: typing.Any
    ) -> typing.Optional[bool]

Delete by vector ID.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.delete](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_delete)

### langchain_google_bigtable.vector_store.BigtableVectorStore.from_documents
    
    
    from_documents(
        documents: typing.List[langchain_core.documents.base.Document],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Return VectorStore initialized from documents and embeddings.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.from_documents](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_from_documents)

### langchain_google_bigtable.vector_store.BigtableVectorStore.from_texts
    
    
    from_texts(
        texts: typing.List[str],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        metadatas: typing.Optional[typing.List[dict]] = None,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Return VectorStore initialized from texts and embeddings.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.from_texts](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_from_texts)

### langchain_google_bigtable.vector_store.BigtableVectorStore.get_by_ids
    
    
    get_by_ids(
        ids: typing.Sequence[str],
    ) -> typing.List[langchain_core.documents.base.Document]

Return documents by their IDs.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.get_by_ids](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_get_by_ids)

### langchain_google_bigtable.vector_store.BigtableVectorStore.get_engine
    
    
    get_engine() -> typing.Optional[langchain_google_bigtable.engine.BigtableEngine]

Get the BigtableEngine instance.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.get_engine](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_get_engine)

### langchain_google_bigtable.vector_store.BigtableVectorStore.max_marginal_relevance_search
    
    
    max_marginal_relevance_search(
        query: str,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs selected using the maximal marginal relevance.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.max_marginal_relevance_search](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_max_marginal_relevance_search)

### langchain_google_bigtable.vector_store.BigtableVectorStore.max_marginal_relevance_search_by_vector
    
    
    max_marginal_relevance_search_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs selected using the maximal marginal relevance.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.max_marginal_relevance_search_by_vector](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_max_marginal_relevance_search_by_vector)

### langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search
    
    
    similarity_search(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs most similar to query.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_similarity_search)

### langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search_by_vector
    
    
    similarity_search_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs most similar to embedding vector.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search_by_vector](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_similarity_search_by_vector)

### langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search_with_relevance_scores
    
    
    similarity_search_with_relevance_scores(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Return docs and relevance scores in the range [0, 1].

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search_with_relevance_scores](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_similarity_search_with_relevance_scores)

### langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search_with_score
    
    
    similarity_search_with_score(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Run similarity search with distance.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search_with_score](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_similarity_search_with_score)

### langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search_with_score_by_vector
    
    
    similarity_search_with_score_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Run similarity search with distance by vector.

See more: [langchain_google_bigtable.vector_store.BigtableVectorStore.similarity_search_with_score_by_vector](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore#langchain_google_bigtable_vector_store_BigtableVectorStore_similarity_search_with_score_by_vector)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
