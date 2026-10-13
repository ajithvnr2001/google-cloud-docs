---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/
title: Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:31.876640+00:00
---

# Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/)



# Bigtable for LangChain

[![image](https://img.shields.io/badge/support-preview-orange.svg)](https://cloud.google.com/products#product-launch-stages) [![image](https://img.shields.io/pypi/v/langchain-google-bigtable.svg)](https://pypi.org/project/langchain-google-bigtable/) [![image](https://img.shields.io/pypi/pyversions/langchain-google-bigtable.svg)](https://pypi.org/project/langchain-google-bigtable/)

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/langchain-google-bigtable/latest)

  * [Product Documentation](https://cloud.google.com/bigtable)




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Google Cloud Bigtable API.](https://console.cloud.google.com/flows/enableapi?apiid=bigtable.googleapis.com)

  4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

#### Supported Python Versions

Python >= 3.9

#### Mac/Linux
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install langchain-google-bigtable
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install langchain-google-bigtable
    

### Vector Store Usage

Use `BigtableVectorStore` to store documents and their vector embeddings, allowing you to search for the most similar or relevant documents from your database.

  * **Full VectorStore Implementation:** Supports all methods from the LangChain `VectorStore` abstract class.

  * **Async/Sync Support:** All methods are available in both asynchronous and synchronous versions.

  * **Metadata Filtering:** Supports filtering on metadata fields, including logical AND/OR combinations and filtering on document IDs with a specific prefix.

  * **Multiple Distance Strategies:** Supports both Cosine and Euclidean distance for similarity search.

  * **Customizable Storage:** Full control over how content, embeddings, and metadata are stored in Bigtable columns.



    
    
    from langchain_google_bigtable import BigtableVectorStore, BigtableEngine
    
    # Your embedding service and other configurations
    # embedding_service = ...
    
    engine = await BigtableEngine.async_initialize(project_id="your-project-id")
    vector_store = await BigtableVectorStore.create(
        engine=engine,
        instance_id="your-instance-id",
        table_id="your-table-id",
        embedding_service=embedding_service,
        collection="your_collection_name",
    )
    

See the full [Vector Store](https://colab.research.google.com/github/googleapis/langchain-google-bigtable-python/blob/main/docs/vector_store.ipynb) tutorial.

### Key-value Store Usage

Use `BigtableByteStore` for a key-value store in LangChain

  * **ByteStore Interface:** Follows LangChain’s `ByteStore` for string keys and byte values.

  * **Sync/Async:** Supports both synchronous and asynchronous operations.

  * **BigtableEngine:** Manages execution context.



    
    
    from langchain_google_bigtable import BigtableByteStore, BigtableEngine
    
    engine = await BigtableEngine.async_initialize(project_id="your-project-id")
    store = await BigtableByteStore.create(
        engine=engine,
        instance_id="your-instance-id",
        table_id="your-table-id",
    )
    await store.amset([("key", b"value")])
    retrieved = await store.amget(["key"])
    

See the full [Key-value Store](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/docs/key_value_store.ipynb) tutorial.

### Document Loader Usage

Use a document loader to load data as LangChain `Document`s.
    
    
    from langchain_google_bigtable import BigtableLoader
    
    
    loader = BigtableLoader(
        instance_id="my-instance",
        table_id="my-table-name"
    )
    docs = loader.lazy_load()
    

See the full [Document Loader](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/docs/document_loader.ipynb) tutorial.

### Chat Message History Usage

Use `ChatMessageHistory` to store messages and provide conversation history to LLMs.
    
    
    from langchain_google_bigtable import BigtableChatMessageHistory
    
    
    history = BigtableChatMessageHistory(
        instance_id="my-instance",
        table_id="my-message-store",
        session_id="my-session_id"
    )
    

See the full [Chat Message History](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/docs/chat_message_history.ipynb) tutorial.

### Contributions

Contributions to this library are always welcome and highly encouraged.

See [CONTRIBUTING](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/CONTRIBUTING.md) for more information how to get started.

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. See [Code of Conduct](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/CODE_OF_CONDUCT.md) for more information.

## License

Apache 2.0 - See [LICENSE](https://github.com/googleapis/langchain-google-bigtable-python/blob/main/LICENSE) for more information.

## Disclaimer

This is not an officially supported Google product.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
