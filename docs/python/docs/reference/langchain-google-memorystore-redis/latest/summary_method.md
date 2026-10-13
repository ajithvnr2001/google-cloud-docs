---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/summary_method/
title: Package Methods (0.3.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:47.938180+00:00
---

# Package Methods (0.3.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.3.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/summary_method/)
  * [ 0.2.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/0.2.0/summary_method/)



Summary of entries of Methods for langchain-google-memorystore-redis.

## 

### langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory
    
    
    MemorystoreChatMessageHistory(
        client: typing.Union[redis.client.Redis, redis.cluster.RedisCluster],
        session_id: str,
        ttl: typing.Optional[int] = None,
    )

Initializes the chat message history for Memorystore for Redis.

See more: [langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory#langchain_google_memorystore_redis_chat_message_history_MemorystoreChatMessageHistory_MemorystoreChatMessageHistory)

### langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory.add_message
    
    
    add_message(message: langchain_core.messages.base.BaseMessage) -> None

Append one message to this session.

See more: [langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory.add_message](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory#langchain_google_memorystore_redis_chat_message_history_MemorystoreChatMessageHistory_add_message)

### langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory.clear
    
    
    clear() -> None

Clear all messages in this session.

See more: [langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory.clear](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.chat_message_history.MemorystoreChatMessageHistory#langchain_google_memorystore_redis_chat_message_history_MemorystoreChatMessageHistory_clear)

### langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader
    
    
    MemorystoreDocumentLoader(
        client: typing.Union[redis.client.Redis, redis.cluster.RedisCluster],
        key_prefix: str,
        content_fields: typing.Set[str],
        metadata_fields: typing.Optional[typing.Set[str]] = None,
        batch_size: int = 100,
    )

Initializes the Document Loader for Memorystore for Redis.

See more: [langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader#langchain_google_memorystore_redis_loader_MemorystoreDocumentLoader_MemorystoreDocumentLoader)

### langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader._construct_document
    
    
    _construct_document(stored_value) -> langchain_core.documents.base.Document

Construct a Document from stored value.

See more: [langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader._construct_document](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader#langchain_google_memorystore_redis_loader_MemorystoreDocumentLoader__construct_document)

### langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader._decode_if_json_parsable
    
    
    _decode_if_json_parsable(s: str) -> typing.Union[str, dict]

Decode a JSON string to a dict if it is JSON.

See more: [langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader._decode_if_json_parsable](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader#langchain_google_memorystore_redis_loader_MemorystoreDocumentLoader__decode_if_json_parsable)

### langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader.lazy_load
    
    
    lazy_load() -> typing.Iterator[langchain_core.documents.base.Document]

Lazy load the Documents and yield them one by one.

See more: [langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader.lazy_load](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader#langchain_google_memorystore_redis_loader_MemorystoreDocumentLoader_lazy_load)

### langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader.load
    
    
    load() -> typing.List[langchain_core.documents.base.Document]

Load all Documents using a Redis pipeline for efficiency.

See more: [langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader.load](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.loader.MemorystoreDocumentLoader#langchain_google_memorystore_redis_loader_MemorystoreDocumentLoader_load)

### langchain_google_memorystore_redis.vectorstore.FLATConfig
    
    
    FLATConfig(
        name: str,
        field_name: typing.Optional[str] = None,
        vector_size: int = 128,
        distance_strategy: langchain_community.vectorstores.utils.DistanceStrategy = DistanceStrategy.COSINE,
    )

Initializes the FLATConfig object.

See more: [langchain_google_memorystore_redis.vectorstore.FLATConfig](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.FLATConfig#langchain_google_memorystore_redis_vectorstore_FLATConfig_FLATConfig)

### langchain_google_memorystore_redis.vectorstore.IndexConfig
    
    
    IndexConfig(name: str, field_name: str, type: str)

Initializes the IndexConfig object.

See more: [langchain_google_memorystore_redis.vectorstore.IndexConfig](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.IndexConfig#langchain_google_memorystore_redis_vectorstore_IndexConfig_IndexConfig)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore._similarity_search_by_vector_with_score_and_embeddings
    
    
    _similarity_search_by_vector_with_score_and_embeddings(
        query_embedding: typing.List[float], k: int = 4, **kwargs: typing.Any
    ) -> typing.List[
        typing.Tuple[langchain_core.documents.base.Document, float, typing.List[float]]
    ]

Performs a similarity search by a vector with score and embeddings, offering various customization options via keyword arguments.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore._similarity_search_by_vector_with_score_and_embeddings](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore__similarity_search_by_vector_with_score_and_embeddings)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.add_texts
    
    
    add_texts(
        texts: typing.Iterable[str],
        metadatas: typing.Optional[typing.List[dict]] = None,
        ids: typing.Optional[typing.List[str]] = None,
        batch_size: typing.Optional[int] = 1000,
        **kwargs: typing.Any
    ) -> typing.List[str]

Adds a collection of texts along with their metadata to a vector store, generating unique keys for each entry if not provided.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.add_texts](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_add_texts)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.delete
    
    
    delete(
        ids: typing.Optional[typing.List[str]] = None, **kwargs: typing.Any
    ) -> typing.Optional[bool]

Delete by vector ID or other criteria.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.delete](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_delete)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.drop_index
    
    
    drop_index(
        client: typing.Union[redis.client.Redis, redis.cluster.RedisCluster],
        index_name: str,
        index_only: bool = True,
    )

Drops an index from the Redis database.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.drop_index](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_drop_index)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.from_texts
    
    
    from_texts(
        texts: typing.List[str],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        metadatas: typing.Optional[typing.List[dict]] = None,
        ids: typing.Optional[typing.List[str]] = None,
        client: typing.Optional[
            typing.Union[redis.client.Redis, redis.cluster.RedisCluster]
        ] = None,
        index_name: typing.Optional[str] = None,
        **kwargs: typing.Any
    ) -> langchain_google_memorystore_redis.vectorstore.RedisVectorStore

Creates an instance of RedisVectorStore from provided texts.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.from_texts](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_from_texts)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.init_index
    
    
    init_index(
        client: typing.Union[redis.client.Redis, redis.cluster.RedisCluster],
        index_config: langchain_google_memorystore_redis.vectorstore.IndexConfig,
    )

Initializes a named VectorStore index in Redis with specified configurations.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.init_index](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_init_index)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.max_marginal_relevance_search
    
    
    max_marginal_relevance_search(
        query: str,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Performs a search to find documents that are both relevant to the query and diverse among each other based on Maximal Marginal Relevance (MMR).

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.max_marginal_relevance_search](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_max_marginal_relevance_search)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.similarity_search
    
    
    similarity_search(
        query: str, k: int = 4, **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Conducts a similarity search based on the specified query, returning a list of the top 'k' documents that are most similar to the query.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.similarity_search](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_similarity_search)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.similarity_search_by_vector
    
    
    similarity_search_by_vector(
        embedding: typing.List[float], k: int = 4, **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Performs a similarity search for the given embedding and returns the top k most similar Document objects, discarding their similarity scores.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.similarity_search_by_vector](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_similarity_search_by_vector)

### langchain_google_memorystore_redis.vectorstore.RedisVectorStore.similarity_search_with_score
    
    
    similarity_search_with_score(
        query: str, k: int = 4, **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Performs a similarity search using the given query, returning documents and their similarity scores.

See more: [langchain_google_memorystore_redis.vectorstore.RedisVectorStore.similarity_search_with_score](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/langchain_google_memorystore_redis.vectorstore.RedisVectorStore#langchain_google_memorystore_redis_vectorstore_RedisVectorStore_similarity_search_with_score)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
