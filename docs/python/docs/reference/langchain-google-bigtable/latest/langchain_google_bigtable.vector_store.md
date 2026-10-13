---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store
title: Module vector_store (0.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:36.266692+00:00
---

# Module vector_store (0.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module vector_store (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/langchain_google_bigtable.vector_store)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/langchain_google_bigtable.vector_store)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/langchain_google_bigtable.vector_store)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/langchain_google_bigtable.vector_store)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/langchain_google_bigtable.vector_store)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/langchain_google_bigtable.vector_store)



API documentation for `vector_store` module.

## Classes 

### [BigtableVectorStore](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore)
    
    
    BigtableVectorStore(instance_id: str, table_id: str, embedding_service: langchain_core.embeddings.embeddings.Embeddings, collection: str, content_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='content', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), embedding_column: langchain_google_bigtable.async_vector_store.ColumnConfig = ColumnConfig(column_qualifier='embedding', column_family='langchain', encoding=<Encoding.UTF8: 'utf-8'>), project_id: typing.Optional[str] = None, metadata_mappings: typing.Optional[typing.List[langchain_google_bigtable.async_vector_store.VectorMetadataMapping]] = None, metadata_as_json_column: typing.Optional[langchain_google_bigtable.async_vector_store.ColumnConfig] = None, engine: typing.Optional[langchain_google_bigtable.engine.BigtableEngine] = None, app_profile_id: typing.Optional[str] = None, **kwargs: typing.Any)

A vector store implementation using Google Cloud Bigtable.

This class provides the main user-facing interface, conforming to the `langchain_core.vectorstores.VectorStore` standard, and handles both synchronous and asynchronous operations by wrapping an async core.

## Modules Functions 

### init_vector_store_table
    
    
    init_vector_store_table(
        instance_id: str,
        table_id: str,
        project_id: typing.Optional[str] = None,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        content_column_family: str = "langchain",
        embedding_column_family: str = "langchain",
    ) -> None

Creates a Bigtable table with the necessary column families for the vector store.

It always creates the "md" column family for metadata and allows you to specify the name of the column family used for content and embeddings.

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `str`   
The ID of the Bigtable instance.  
`table_id` |  `str`   
The ID of the table to create.  
`project_id` |  `Optional[str]`   
Your Google Cloud project ID.  
`client` |  `Optional[bigtable.Client]`   
An optional pre-configured Bigtable admin client.  
`content_column_family` |  `str`   
The name of the column family to store document content. Defaults to "langchain".  
`embedding_column_family` |  `str`   
The name of the column family to store embeddings. Defaults to "langchain".  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the table already exists.  
`PermissionDenied` | If the client lacks permission to create the table.  
`GoogleAPIError` | If any other Google Cloud API error occurs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
