---
url: https://docs.cloud.google.com/python/docs/reference/llama-index-alloydb-pg/latest/
title: AlloyDB for PostgreSQL for LlamaIndex \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:37.547147+00:00
---

# AlloyDB for PostgreSQL for LlamaIndex  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/llama-index-alloydb-pg/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  AlloyDB for PostgreSQL for LlamaIndex Stay organized with collections  Save and categorize content based on your preferences. 

0.3.1 (latest)  0.3.0  0.2.3 

[![image](https://img.shields.io/badge/support-preview-orange.svg)](https://github.com/googleapis/google-cloud-python/blob/main/README.rst#stability-levels) [![image](https://img.shields.io/pypi/v/llama-index-alloydb-pg.svg)](https://pypi.org/project/llama-index-alloydb-pg/) [![image](https://img.shields.io/pypi/pyversions/llama-index-alloydb-pg.svg)](https://pypi.org/project/llama-index-alloydb-pg/)

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/llama-index-alloydb-pg/latest)

  * [Product Documentation](https://cloud.google.com/alloydb)




The **AlloyDB for PostgreSQL for LlamaIndex** package provides a first class experience for connecting to AlloyDB instances from the LlamaIndex ecosystem while providing the following benefits:

  * **Simplified & Secure Connections**: easily and securely create shared connection pools to connect to Google Cloud databases utilizing IAM for authorization and database authentication without needing to manage SSL certificates, configure firewall rules, or enable authorized networks.

  * **Better integration with AlloyDB** : built-in methods to take advantage of AlloyDB’s advanced indexing and scalability capabilities.

  * **Improved metadata handling** : store metadata in columns instead of JSON, resulting in significant performance improvements.

  * **Clear separation** : clearly separate table and extension creation, allowing for distinct permissions and streamlined workflows.




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the AlloyDB API.](https://console.cloud.google.com/flows/enableapi?apiid=alloydb.googleapis.com)

  4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

#### Supported Python Versions

Python >= 3.10

#### Mac/Linux
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install llama-index-alloydb-pg
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install llama-index-alloydb-pg
    

## Example Usage

Code samples and snippets live in the [samples/](https://github.com/googleapis/llama-index-alloydb-pg-python/tree/main/samples) folder.

### Vector Store Usage

Use a vector store to store embedded data and perform vector search.
    
    
    import google.auth
    from llama_index.core import Settings
    from llama_index.embeddings.vertex import VertexTextEmbedding
    from llama_index_alloydb_pg import AlloyDBEngine, AlloyDBVectorStore
    
    
    credentials, project_id = google.auth.default()
    engine = await AlloyDBEngine.afrom_instance(
       "project-id", "region", "my-cluster", "my-instance", "my-database"
    )
    Settings.embed_model = VertexTextEmbedding(
       model_name="textembedding-gecko@003",
       project="project-id",
       credentials=credentials,
    )
    
    vector_store = await AlloyDBVectorStore.create(
       engine=engine, table_name="vector_store"
    )
    

### Chat Store Usage

A chat store serves as a centralized interface to store your chat history.
    
    
    from llama_index.core.memory import ChatMemoryBuffer
    from llama_index_cloud_sql_pg import AlloyDBChatStore, AlloyDBEngine
    
    
    engine = await AlloyDBEngine.afrom_instance(
       "project-id", "region", "my-cluster", "my-instance", "my-database"
    )
    chat_store = await AlloyDBChatStore.create(
       engine=engine, table_name="chat_store"
    )
    memory = ChatMemoryBuffer.from_defaults(
       token_limit=3000,
       chat_store=chat_store,
       chat_store_key="user1",
    )
    

### Document Reader Usage

A Reader ingest data from different data sources and data formats into a simple Document representation.
    
    
    from llama_index.core.memory import ChatMemoryBuffer
    from llama_index_cloud_sql_pg import AlloyDBReader, AlloyDBEngine
    
    
    engine = await AlloyDBEngine.afrom_instance(
       "project-id", "region", "my-cluster", "my-instance", "my-database"
    )
    reader = await AlloyDBReader.create(
       engine=engine, table_name="my-db-table"
    )
    documents = reader.load_data()
    

### Document Store Usage

Use a document store to make storage and maintenance of data easier.
    
    
    from llama_index_alloydb_pg import AlloyDBEngine, AlloyDBDocumentStore
    
    
    engine = await AlloyDBEngine.afrom_instance(
       "project-id", "region", "my-cluster", "my-instance", "my-database"
    )
    doc_store = await AlloyDBDocumentStore.create(
       engine=engine, table_name="doc_store"
    )
    

### Index Store Usage

Use an index store to keep track of indexes built on documents.
    
    
    from llama_index_alloydb_pg import AlloyDBIndexStore, AlloyDBEngine
    
    
    engine = await AlloyDBEngine.from_instance(
       "project-id", "region", "my-cluster", "my-instance", "my-database"
    )
    index_store = await AlloyDBIndexStore.create(
       engine=engine, table_name="index_store"
    )
    

### Contributions

Contributions to this library are always welcome and highly encouraged.

See [CONTRIBUTING](https://github.com/googleapis/llama-index-alloydb-pg-python/tree/main/CONTRIBUTING.md) for more information how to get started.

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. See [Code of Conduct](https://github.com/googleapis/llama-index-alloydb-pg-python/tree/main/CODE_OF_CONDUCT.md) for more information.

## License

Apache 2.0 - See [LICENSE](https://github.com/googleapis/llama-index-alloydb-pg-python/tree/main/LICENSE) for more information.

## Disclaimer

This is not an officially supported Google product.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
