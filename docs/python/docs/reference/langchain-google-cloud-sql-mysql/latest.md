---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mysql/latest/
title: Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:36.773887+00:00
---

# Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mysql/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.3.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mysql/latest/)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mysql/0.2.3/)



# Cloud SQL for MySQL for LangChain

[![image](https://img.shields.io/badge/support-preview-orange.svg)](https://cloud.google.com/products#product-launch-stages) [![image](https://img.shields.io/pypi/v/langchain-google-cloud-sql-mysql.svg)](https://pypi.org/project/langchain-google-cloud-sql-mysql/) [![image](https://img.shields.io/pypi/pyversions/langchain-google-cloud-sql-mysql.svg)](https://pypi.org/project/langchain-google-cloud-sql-mysql/)

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mysql/latest)

  * [Product Documentation](https://cloud.google.com/sql/mysql)




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Google Cloud SQL Admin API.](https://console.cloud.google.com/flows/enableapi?apiid=sqladmin.googleapis.com)

  4. [Setup Authentication.](https://googleapis.dev/python/google-api-core/latest/auth.html)




### Supported Cloud SQL Maintenance Versions

This LangChain integration is only supported for Cloud SQL maintenance versions between **MYSQL_8_0_36.R20240401.03_00** and **MYSQL_8_0_36.R20241208.01_00**

### Installation

Install this library in a [virtualenv](https://virtualenv.pypa.io/en/latest/) using pip. [virtualenv](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. The basic problem it addresses is one of dependencies and versions, and indirectly permissions.

With [virtualenv](https://virtualenv.pypa.io/en/latest/), it’s possible to install this library without needing system install permissions, and without clashing with the installed system dependencies.

#### Supported Python Versions

Python >= 3.9

#### Mac/Linux
    
    
    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install langchain-google-cloud-sql-mysql
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install langchain-google-cloud-sql-mysql
    

### Vector Store Usage

Use a vector store to store embedded data and perform vector search.
    
    
    from langchain_google_cloud_sql_mysql import MySQLEngine, MySQLVectorStore
    from langchain_google_vertexai import VertexAIEmbeddings
    
    engine = MySQLEngine.from_instance("project-id", "region", "my-instance", "my-database")
    engine.init_vectorstore_table(
        table_name="my-table-name",
        vector_size=768
    )
    vectorstore = MySQLVectorStore(
        engine,
        embedding_service=VertexAIEmbeddings(model_name="textembedding-gecko@003"),
        table_name="my-table-name"
    )
    

See the full [Vector Store](https://github.com/googleapis/langchain-google-cloud-sql-mysql-python/blob/main/docs/vector_store.ipynb) tutorial.

### Document Loader Usage

Use a document loader to load data as LangChain `Document`s.
    
    
    from langchain_google_cloud_sql_mysql import MySQLEngine, MySQLLoader
    
    engine = MySQLEngine.from_instance("project-id", "region", "my-instance", "my-database")
    loader = MySQLLoader(
        engine,
        table_name="my-table-name"
    )
    docs = loader.lazy_load()
    

See the full [Document Loader](https://github.com/googleapis/langchain-google-cloud-sql-mysql-python/blob/main/docs/document_loader.ipynb) tutorial.

### Chat Message History Usage

Use `ChatMessageHistory` to store messages and provide conversation history to LLMs.
    
    
    from langchain_google_cloud_sql_mysql import MySQLChatMessageHistory, MySQLEngine
    
    engine = MySQLEngine.from_instance("project-id", "region", "my-instance", "my-database")
    history = MySQLChatMessageHistory(
        engine,
        table_name="my-message-store",
        session_id="my-session-id"
    )
    

See the full [Chat Message History](https://github.com/googleapis/langchain-google-cloud-sql-mysql-python/blob/main/docs/chat_message_history.ipynb) tutorial.

### Contributions

Contributions to this library are always welcome and highly encouraged.

See [CONTRIBUTING](https://github.com/googleapis/langchain-google-cloud-sql-mysql-python/blob/main/CONTRIBUTING.md) for more information how to get started.

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. See [Code of Conduct](https://github.com/googleapis/langchain-google-cloud-sql-mysql-python/blob/main/CODE_OF_CONDUCT.md) for more information.

## License

Apache 2.0 - See [LICENSE](https://github.com/googleapis/langchain-google-cloud-sql-mysql-python/blob/main/LICENSE) for more information.

## Disclaimer

This is not an officially supported Google product.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
