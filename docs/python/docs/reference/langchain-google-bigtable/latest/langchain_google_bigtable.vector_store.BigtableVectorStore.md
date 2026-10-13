---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore
title: Class BigtableVectorStore (0.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:37.199814+00:00
---

# Class BigtableVectorStore (0.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BigtableVectorStore (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/langchain_google_bigtable.vector_store.BigtableVectorStore)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/langchain_google_bigtable.vector_store.BigtableVectorStore)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/langchain_google_bigtable.vector_store.BigtableVectorStore)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/langchain_google_bigtable.vector_store.BigtableVectorStore)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/langchain_google_bigtable.vector_store.BigtableVectorStore)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/langchain_google_bigtable.vector_store.BigtableVectorStore)


    
    
    BigtableVectorStore(instance_id: str, table_id: str, embedding_service: langchain_core.embeddings.embeddings.Embeddings, collection: str, content_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='content', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), embedding_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='embedding', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), project_id: typing.Optional[str] = None, metadata_mappings: typing.Optional[typing.List[langchain_google_bigtable.async_vector_store.VectorMetadataMapping]] = None, metadata_as_json_column: typing.Optional[langchain_google_bigtable.async_vector_store.ColumnConfig] = None, engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None, app_profile_id: typing.Optional[str] = None, **kwargs: typing.Any)

A vector store implementation using Google Cloud Bigtable.

This class provides the main user-facing interface, conforming to the `langchain_core.vectorstores.VectorStore` standard, and handles both synchronous and asynchronous operations by wrapping an async core.

## Properties 

### embeddings

Access the query embedding object.

**Returns**  
---  
**Type** | **Description**  
`(Embeddings)` | The embedding service object.  
  
## Methods 

### BigtableVectorStore
    
    
    BigtableVectorStore(instance_id: str, table_id: str, embedding_service: langchain_core.embeddings.embeddings.Embeddings, collection: str, content_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='content', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), embedding_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='embedding', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), project_id: typing.Optional[str] = None, metadata_mappings: typing.Optional[typing.List[langchain_google_bigtable.async_vector_store.VectorMetadataMapping]] = None, metadata_as_json_column: typing.Optional[langchain_google_bigtable.async_vector_store.ColumnConfig] = None, engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None, app_profile_id: typing.Optional[str] = None, **kwargs: typing.Any)

Initializes the BigtableVectorStore.

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `str`   
Your Bigtable instance ID.  
`table_id` |  `str`   
The ID of the table to use for the vector store.  
`embedding_service` |  `Embeddings`   
The embedding service to use.  
`collection` |  `str`   
A name for the collection of vectors for this store. Internally, this is used as the row key prefix.  
`content_column` |  `ColumnConfig`   
Configuration for the document content column.  
`embedding_column` |  `ColumnConfig`   
Configuration for the vector embedding column.  
`project_id` |  `Optional[str]`   
Your Google Cloud project ID.  
`metadata_mappings` |  `Optional[List[VectorMetadataMapping]]`   
Mappings for storing metadata in separate columns.  
`metadata_as_json_column` |  `Optional[ColumnConfig]`   
Configuration for storing all metadata in a single JSON column.  
`engine` |  `Optional[BigtableEngine]`   
The BigtableEngine to use for connecting to Bigtable.  
`app_profile_id` |  `Optional[str]`   
The Bigtable app profile ID to use for requests.  
`\*\*kwargs` |  `Any`   
Additional arguments for engine creation if an engine is not provided.  
  
### _get_async_store
    
    
    _get_async_store() -> (
        langchain_google_bigtable.async_vector_store.AsyncBigtableVectorStore
    )

Lazily initializes and returns the underlying async store.

**Returns**  
---  
**Type** | **Description**  
`(AsyncBigtableVectorStore)` | The initialized asynchronous vector store.  
  
### aadd_documents
    
    
    aadd_documents(
        documents: typing.List[langchain_core.documents.base.Document],
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> typing.List[str]

Run more documents through the embeddings and add to the vectorstore.

**Parameters**  
---  
**Name** | **Description**  
`documents` |  `List[Document]`   
A list of documents to add.  
`ids` |  `Optional[list]`   
list of IDs for the documents.  
`\*\*kwargs` |  `Any`   
Additional arguments.  
**Returns**  
---  
**Type** | **Description**  
`(List[str])` | A list of the row keys of the added documents.  
  
### aadd_texts
    
    
    aadd_texts(
        texts: typing.Iterable[str],
        metadatas: typing.Optional[typing.List[dict]] = None,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> typing.List[str]

Run more texts through the embeddings and add to the vectorstore.

**Parameters**  
---  
**Name** | **Description**  
`texts` |  `Iterable[str]`   
An iterable of texts to add.  
`metadatas` |  `Optional[List[dict]]`   
Optional list of metadatas.  
`ids` |  `Optional[list]`   
list of IDs for the texts.  
`\*\*kwargs` |  `Any`   
Additional arguments.  
**Returns**  
---  
**Type** | **Description**  
`(List[str])` | A list of the row keys of the added texts.  
  
### add_documents
    
    
    add_documents(
        documents: typing.List[langchain_core.documents.base.Document],
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> typing.List[str]

Run more documents through the embeddings and add to the vectorstore.

**Parameters**  
---  
**Name** | **Description**  
`documents` |  `List[Document]`   
A list of documents to add.  
`ids` |  `Optional[list]`   
list of IDs for the documents.  
`\*\*kwargs` |  `Any`   
Additional arguments.  
**Returns**  
---  
**Type** | **Description**  
`(List[str])` | A list of the row keys of the added documents.  
  
### add_texts
    
    
    add_texts(
        texts: typing.Iterable[str],
        metadatas: typing.Optional[typing.List[typing.Dict]] = None,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> typing.List[str]

Run more texts through the embeddings and add to the vectorstore.

**Parameters**  
---  
**Name** | **Description**  
`texts` |  `Iterable[str]`   
An iterable of texts to add.  
`metadatas` |  `Optional[List[Dict]]`   
Optional list of metadatas.  
`ids` |  `Optional[list]`   
list of IDs for the texts.  
`\*\*kwargs` |  `Any`   
Additional arguments.  
**Returns**  
---  
**Type** | **Description**  
`(List[str])` | A list of the row keys of the added texts.  
  
### adelete
    
    
    adelete(
        ids: typing.Optional[typing.List[str]] = None, **kwargs: typing.Any
    ) -> typing.Optional[bool]

Delete by vector ID.

**Parameters**  
---  
**Name** | **Description**  
`ids` |  `Optional[List[str]]`   
A list of document IDs to delete.  
`\*\*kwargs` |  `Any`   
Additional arguments.  
**Returns**  
---  
**Type** | **Description**  
`(Optional[bool])` | True if the deletion was successful.  
  
### afrom_documents
    
    
    afrom_documents(
        documents: typing.List[langchain_core.documents.base.Document],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Return VectorStore initialized from documents and embeddings. This is an asynchronous method that creates the store and adds documents.

**Parameters**  
---  
**Name** | **Description**  
`documents` |  `List[Document]`   
List of documents to add.  
`embedding` |  `Embeddings`   
The embedding service to use. ids (Optional[list]): list of IDs for the documents.  
`\*\*kwargs` |  `Any`   
Keyword arguments to pass to the `create` method.  
**Returns**  
---  
**Type** | **Description**  
`(BigtableVectorStore)` | An instance of the vector store.  
  
### afrom_texts
    
    
    afrom_texts(
        texts: typing.List[str],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        metadatas: typing.Optional[typing.List[dict]] = None,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Return VectorStore initialized from texts and embeddings.

**Parameters**  
---  
**Name** | **Description**  
`texts` |  `List[str]`   
List of text strings to add.  
`embedding` |  `Embeddings`   
The embedding service to use.  
`metadatas` |  `Optional[List[dict]]`   
Optional list of metadata for each text.  
`ids` |  `Optional[list]`   
list of IDs for the texts.  
`\*\*kwargs` |  `Any`   
Keyword arguments to pass to the `acreate` method.  
**Returns**  
---  
**Type** | **Description**  
`(BigtableVectorStore)` | An instance of the vector store.  
  
### aget_by_ids
    
    
    aget_by_ids(
        ids: typing.Sequence[str],
    ) -> typing.List[langchain_core.documents.base.Document]

Return documents by their IDs.

**Parameter**  
---  
**Name** | **Description**  
`ids` |  `List[str]`   
A list of document IDs to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of the retrieved documents.  
  
### amax_marginal_relevance_search
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
The text to search for.  
`k` |  `int`   
The number of results to return.  
`fetch_k` |  `int`   
The number of documents to fetch for MMR.  
`lambda_mult` |  `float`   
The lambda multiplier for MMR.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of documents selected by MMR.  
  
### amax_marginal_relevance_search_by_vector
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`embedding` |  `List[float]`   
The embedding vector to search for.  
`k` |  `int`   
The number of results to return.  
`fetch_k` |  `int`   
The number of documents to fetch for MMR.  
`lambda_mult` |  `float`   
The lambda multiplier for MMR.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of documents selected by MMR.  
  
### as_retriever
    
    
    as_retriever(
        **kwargs: typing.Any,
    ) -> langchain_core.vectorstores.base.VectorStoreRetriever

Return VectorStoreRetriever initialized from this VectorStore.

**Parameter**  
---  
**Name** | **Description**  
`\*\*kwargs` |  `Any`   
Keyword arguments to pass to the retriever.  
**Returns**  
---  
**Type** | **Description**  
`(VectorStoreRetriever)` | The initialized retriever.  
  
### asimilarity_search
    
    
    asimilarity_search(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs most similar to query.

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
The text to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of documents most similar to the query.  
  
### asimilarity_search_by_vector
    
    
    asimilarity_search_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs most similar to embedding vector.

**Parameters**  
---  
**Name** | **Description**  
`embedding` |  `List[float]`   
The embedding vector to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of documents most similar to the embedding.  
  
### asimilarity_search_with_relevance_scores
    
    
    asimilarity_search_with_relevance_scores(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Return docs and relevance scores in the range [0, 1].

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
The text to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Tuple[Document, float]])` | A list of tuples containing the document and its relevance score.  
  
### asimilarity_search_with_score
    
    
    asimilarity_search_with_score(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Run similarity search with distance.

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
The text to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Tuple[Document, float]])` | A list of tuples containing the document and its distance score.  
  
### asimilarity_search_with_score_by_vector
    
    
    asimilarity_search_with_score_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Run similarity search with distance by vector.

**Parameters**  
---  
**Name** | **Description**  
`embedding` |  `List[float]`   
The embedding vector to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Tuple[Document, float]])` | A list of tuples containing the document and its distance score.  
  
### close
    
    
    close() -> None

Close the engine connection.

### create
    
    
    create(instance_id: str, table_id: str, embedding_service: langchain_core.embeddings.embeddings.Embeddings, collection: str, engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None, content_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='content', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), embedding_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='embedding', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), project_id: typing.Optional[str] = None, metadata_mappings: typing.Optional[typing.List[langchain_google_bigtable.async_vector_store.VectorMetadataMapping]] = None, metadata_as_json_column: typing.Optional[langchain_google_bigtable.async_vector_store.ColumnConfig] = None, app_profile_id: typing.Optional[str] = None, credentials: typing.Optional[google.auth.credentials.Credentials] = None, client_options: typing.Optional[typing.Dict[str, typing.Any]] = None, **kwargs: typing.Any) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Asynchronously initializes the engine and creates an instance of the vector store.

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `str`   
Your Bigtable instance ID.  
`table_id` |  `str`   
The ID of the table to use for the vector store.  
`embedding_service` |  `Embeddings`   
The embedding service to use.  
`collection` |  `str`   
A name for the collection of vectors for this store. Internally, this is used as the row key prefix.  
`engine` |  `Optional[BigtableEngine]`   
An optional, existing BigtableEngine.  
`content_column` |  `ColumnConfig`   
Configuration for the document content column.  
`embedding_column` |  `ColumnConfig`   
Configuration for the vector embedding column.  
`project_id` |  `Optional[str]`   
Your Google Cloud project ID.  
`query_parameters` |  `Optional[QueryParameters]`   
Default QueryParameters for searches.  
`metadata_mappings` |  `Optional[List[VectorMetadataMapping]]`   
Mappings for metadata columns.  
`metadata_as_json_column` |  `Optional[ColumnConfig]`   
Configuration for a single JSON metadata column.  
`app_profile_id` |  `Optional[str]`   
The Bigtable app profile ID to use.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
Custom credentials to use.  
`client_options` |  `Optional[Dict[str, Any]]`   
Client options for the Bigtable client.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments for engine initialization.  
**Returns**  
---  
**Type** | **Description**  
`(BigtableVectorStore)` | An instance of the vector store.  
  
### create_sync
    
    
    create_sync(instance_id: str, table_id: str, embedding_service: langchain_core.embeddings.embeddings.Embeddings, collection: str, engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None, content_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='content', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), embedding_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='embedding', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), project_id: typing.Optional[str] = None, metadata_mappings: typing.Optional[typing.List[langchain_google_bigtable.async_vector_store.VectorMetadataMapping]] = None, metadata_as_json_column: typing.Optional[langchain_google_bigtable.async_vector_store.ColumnConfig] = None, app_profile_id: typing.Optional[str] = None, credentials: typing.Optional[google.auth.credentials.Credentials] = None, client_options: typing.Optional[typing.Dict[str, typing.Any]] = None, **kwargs: typing.Any) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Synchronously initializes the engine and creates an instance of the vector store.

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `str`   
Your Bigtable instance ID.  
`table_id` |  `str`   
The ID of the table to use for the vector store.  
`embedding_service` |  `Embeddings`   
The embedding service to use.  
`collection` |  `str`   
A name for the collection of vectors for this store. Internally, this is used as the row key prefix.  
`engine` |  `Optional[BigtableEngine]`   
An optional, existing BigtableEngine.  
`content_column` |  `ColumnConfig`   
Configuration for the document content column.  
`embedding_column` |  `ColumnConfig`   
Configuration for the vector embedding column.  
`project_id` |  `Optional[str]`   
Your Google Cloud project ID.  
`metadata_mappings` |  `Optional[List[VectorMetadataMapping]]`   
Mappings for metadata columns.  
`metadata_as_json_column` |  `Optional[ColumnConfig]`   
Configuration for a single JSON metadata column.  
`app_profile_id` |  `Optional[str]`   
The Bigtable app profile ID to use.  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
Custom credentials to use.  
`client_options` |  `Optional[Dict[str, Any]]`   
Client options for the Bigtable client.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments for engine initialization.  
**Returns**  
---  
**Type** | **Description**  
`(BigtableVectorStore)` | An instance of the vector store.  
  
### delete
    
    
    delete(
        ids: typing.Optional[typing.List[str]] = None, **kwargs: typing.Any
    ) -> typing.Optional[bool]

Delete by vector ID.

**Parameters**  
---  
**Name** | **Description**  
`ids` |  `Optional[List[str]]`   
A list of document IDs to delete.  
`\*\*kwargs` |  `Any`   
Additional arguments.  
**Returns**  
---  
**Type** | **Description**  
`(Optional[bool])` | True if the deletion was successful.  
  
### from_documents
    
    
    from_documents(
        documents: typing.List[langchain_core.documents.base.Document],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Return VectorStore initialized from documents and embeddings. This is a synchronous method that creates the store and adds documents.

**Parameters**  
---  
**Name** | **Description**  
`documents` |  `List[Document]`   
List of documents to add.  
`embedding` |  `Embeddings`   
The embedding service to use.  
`ids` |  `Optional[list]`   
list of IDs for the texts.  
`\*\*kwargs` |  `Any`   
Keyword arguments to pass to the `create_sync` method.  
**Returns**  
---  
**Type** | **Description**  
`(BigtableVectorStore)` | An instance of the vector store.  
  
### from_texts
    
    
    from_texts(
        texts: typing.List[str],
        embedding: langchain_core.embeddings.embeddings.Embeddings,
        metadatas: typing.Optional[typing.List[dict]] = None,
        ids: typing.Optional[list] = None,
        **kwargs: typing.Any
    ) -> langchain_google_bigtable.vector_store.BigtableVectorStore

Return VectorStore initialized from texts and embeddings.

**Parameters**  
---  
**Name** | **Description**  
`texts` |  `List[str]`   
List of text strings to add.  
`embedding` |  `Embeddings`   
The embedding service to use.  
`metadatas` |  `Optional[List[dict]]`   
Optional list of metadata for each text.  
`ids` |  `Optional[list]`   
list of IDs for the texts.  
`\*\*kwargs` |  `Any`   
Keyword arguments to pass to the `create_sync` factory method.  
**Returns**  
---  
**Type** | **Description**  
`(BigtableVectorStore)` | An instance of the vector store.  
  
### get_by_ids
    
    
    get_by_ids(
        ids: typing.Sequence[str],
    ) -> typing.List[langchain_core.documents.base.Document]

Return documents by their IDs.

**Parameter**  
---  
**Name** | **Description**  
`ids` |  `List[str]`   
A list of document IDs to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of the retrieved documents.  
  
### get_engine
    
    
    get_engine() -> typing.Optional[langchain_google_bigtable.engine.BigtableEngine]

Get the BigtableEngine instance.

**Returns**  
---  
**Type** | **Description**  
`(Optional[BigtableEngine])` | The engine instance if it exists.  
  
### max_marginal_relevance_search
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
The text to search for.  
`k` |  `int`   
The number of results to return.  
`fetch_k` |  `int`   
The number of documents to fetch for MMR.  
`lambda_mult` |  `float`   
The lambda multiplier for MMR.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of documents selected by MMR.  
  
### max_marginal_relevance_search_by_vector
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`embedding` |  `List[float]`   
The embedding vector to search for.  
`k` |  `int`   
The number of results to return.  
`fetch_k` |  `int`   
The number of documents to fetch for MMR.  
`lambda_mult` |  `float`   
The lambda multiplier for MMR.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of documents selected by MMR.  
  
### similarity_search
    
    
    similarity_search(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs most similar to query.

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
The text to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of documents most similar to the query.  
  
### similarity_search_by_vector
    
    
    similarity_search_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[langchain_core.documents.base.Document]

Return docs most similar to embedding vector.

**Parameters**  
---  
**Name** | **Description**  
`embedding` |  `List[float]`   
The embedding vector to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Document])` | A list of documents most similar to the embedding.  
  
### similarity_search_with_relevance_scores
    
    
    similarity_search_with_relevance_scores(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Return docs and relevance scores in the range [0, 1].

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
The text to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Tuple[Document, float]])` | A list of tuples containing the document and its relevance score.  
  
### similarity_search_with_score
    
    
    similarity_search_with_score(
        query: str,
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Run similarity search with distance.

**Parameters**  
---  
**Name** | **Description**  
`query` |  `str`   
The text to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Tuple[Document, float]])` | A list of tuples containing the document and its distance score.  
  
### similarity_search_with_score_by_vector
    
    
    similarity_search_with_score_by_vector(
        embedding: typing.List[float],
        k: int = 4,
        query_parameters: typing.Optional[
            langchain_google_bigtable.async_vector_store.QueryParameters
        ] = None,
        **kwargs: typing.Any
    ) -> typing.List[typing.Tuple[langchain_core.documents.base.Document, float]]

Run similarity search with distance by vector.

**Parameters**  
---  
**Name** | **Description**  
`embedding` |  `List[float]`   
The embedding vector to search for.  
`k` |  `int`   
The number of results to return.  
`query_parameters` |  `Optional[QueryParameters]`   
Custom query parameters for this search.  
`\*\*kwargs` |  `Any`   
Additional keyword arguments (e.g., filter).  
**Returns**  
---  
**Type** | **Description**  
`(List[Tuple[Document, float]])` | A list of tuples containing the document and its distance score.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
