---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/summary_class/
title: Package Classes (0.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:33.973318+00:00
---

# Package Classes (0.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/summary_class/)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/summary_class/)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/summary_class/)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/summary_class/)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/summary_class/)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/summary_class/)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/summary_class/)



Summary of entries of Classes for langchain-google-bigtable.

## Classes 

### [BigtableChatMessageHistory](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.chat_message_history.BigtableChatMessageHistory)

Chat message history that stores history in Bigtable.

### [BigtableEngine](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine.BigtableEngine)

Manages the client and execution context, handling the

async/sync conversion via a background event loop.

This class is the core of the async/sync interoperability, providing a reusable component that can be shared across multiple store instances to conserve resources.

### [BigtableByteStore](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore)

LangChain Key-value store implementation for Google Cloud Bigtable, supporting both sync and async methods using BigtableEngine.

### [BigtableLoader](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableLoader)

Load from the Google Cloud Platform `Bigtable`.

### [BigtableSaver](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableSaver)

Load from the Google Cloud Platform `Bigtable`.

### [Encoding](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.Encoding)

An enumeration.

### [MetadataMapping](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.MetadataMapping)

MetadataMapping(column_family: 'str', column_name: 'str', metadata_key: 'str', encoding: 'Encoding', custom_encoding_func: 'Callable[[Any], bytes]' = <function MetadataMapping.__not_implemented at 0x7f0c18356560>, custom_decoding_func: 'Callable[[bytes], Any]' = <function MetadataMapping.__not_implemented at 0x7f0c18356560>)

### [BigtableVectorStore](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store.BigtableVectorStore)

A vector store implementation using Google Cloud Bigtable.

This class provides the main user-facing interface, conforming to the `langchain_core.vectorstores.VectorStore` standard, and handles both synchronous and asynchronous operations by wrapping an async core.

## Modules 

### [chat_message_history](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.chat_message_history)

Bigtable-based chat message history

### [engine](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.engine)

API documentation for `engine` module.

### [key_value_store](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store)

API documentation for `key_value_store` module.

### [loader](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader)

API documentation for `loader` module.

### [vector_store](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.vector_store)

API documentation for `vector_store` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
