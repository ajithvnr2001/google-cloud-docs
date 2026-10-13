---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/
title: Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:33.685516+00:00
---

# Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.3.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest/)
  * [ 0.2.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/0.2.0/)



# Memorystore for Redis for LangChain

[![image](https://img.shields.io/badge/support-preview-orange.svg)](https://cloud.google.com/products#product-launch-stages) [![image](https://img.shields.io/pypi/v/langchain-google-memorystore-redis.svg)](https://pypi.org/project/langchain-google-memorystore-redis/) [![image](https://img.shields.io/pypi/pyversions/langchain-google-memorystore-redis.svg)](https://pypi.org/project/langchain-google-memorystore-redis/)

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/langchain-google-memorystore-redis/latest)

  * [Product Documentation](https://cloud.google.com/memorystore)




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Google Memorystore for Redis API.](https://console.cloud.google.com/flows/enableapi?apiid=memorystore.googleapis.com)

  4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

#### Supported Python Versions

Python >= 3.8

#### Mac/Linux
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install langchain-google-memorystore-redis
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install langchain-google-memorystore-redis
    

### Vector Store Usage

Use a vector store to store embedded data and perform vector search.
    
    
    from langchain_google_memorystore_redis import RedisVectorStore
    
    redis_client = redis.from_url("redis://127.0.0.1:6379")
    
    embeddings_service = VertexAIEmbeddings(model_name="textembedding-gecko@003")
    vectorstore = RedisVectorStore(
        client=redis_client,
        index_name="my_vector_index",
        embeddings=embeddings_service
    )
    

You can also use a clustered client:
    
    
    from langchain_google_memorystore_redis import RedisVectorStore
    
    redis_client = redis.cluster.RedisCluster.from_url("redis://127.0.0.1:6379")
    
    embeddings_service = VertexAIEmbeddings(model_name="textembedding-gecko@003")
    vectorstore = RedisVectorStore(
        client=redis_client,
        index_name="my_vector_index",
        embeddings=embeddings_service
    )
    

See the full [Vector Store](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/docs/vector_store.ipynb) tutorial.

### Document Loader Usage

Use a document loader to load data as LangChain `Document`s.
    
    
    from langchain_google_memorystore_redis import MemorystoreDocumentLoader
    
    
    loader = MemorystoreDocumentLoader(
        client=redis_client,
        key_prefix="docs:",
        content_fields=set(["page_content"]),
    )
    docs = loader.lazy_load()
    

See the full [Document Loader](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/docs/document_loader.ipynb) tutorial.

### Chat Message History Usage

Use `ChatMessageHistory` to store messages and provide conversation history to LLMs.
    
    
    from langchain_google_memorystore_redis import MemorystoreChatMessageHistory
    
    
    history = MemorystoreChatMessageHistory(
        client=redis_client,
        session_id="my-session_id"
    )
    

See the full [Chat Message History](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/docs/chat_message_history.ipynb) tutorial.

### Contributions

Contributions to this library are always welcome and highly encouraged.

See [CONTRIBUTING](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/CONTRIBUTING.md) for more information how to get started.

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. See [Code of Conduct](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/CODE_OF_CONDUCT.md) for more information.

## License

Apache 2.0 - See [LICENSE](https://github.com/googleapis/langchain-google-memorystore-redis-python/blob/main/LICENSE) for more information.

## Disclaimer

This is not an officially supported Google product.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
