---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-spanner/latest/
title: Spanner for LangChain \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:38.459647+00:00
---

# Spanner for LangChain  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-spanner/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Spanner for LangChain Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 

[![image](https://img.shields.io/badge/support-preview-orange.svg)](https://cloud.google.com/products#product-launch-stages) [![image](https://img.shields.io/pypi/v/langchain-google-spanner.svg)](https://pypi.org/project/langchain-google-spanner/) [![image](https://img.shields.io/pypi/pyversions/langchain-google-spanner.svg)](https://pypi.org/project/langchain-google-spanner/)

  * [Client Library Documentation](https://cloud.google.com/python/docs/reference/langchain-google-spanner/latest)

  * [Product Documentation](https://cloud.google.com/spanner)




## Quick Start

In order to use this library, you first need to go through the following steps:

  1. [Select or create a Cloud Platform project.](https://console.cloud.google.com/project)

  2. [Enable billing for your project.](https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project)

  3. [Enable the Google Cloud Spanner API.](https://console.cloud.google.com/flows/enableapi?apiid=spanner.googleapis.com)

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
    <your-env>/bin/pip install langchain-google-spanner
    

#### Windows
    
    
    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install langchain-google-spanner
    

### Vector Store Usage

Use a vector store to store embedded data and perform vector search.
    
    
    from langchain_google_spanner import SpannerVectorstore
    from langchain.embeddings import VertexAIEmbeddings
    
    embeddings_service = VertexAIEmbeddings(model_name="textembedding-gecko@003")
    vectorstore = SpannerVectorStore(
        instance_id="my-instance",
        database_id="my-database",
        table_name="my-table",
        embeddings=embedding_service
    )
    

See the full [Vector Store](https://github.com/googleapis/langchain-google-spanner-python/blob/main/docs/vector_store.ipynb) tutorial.

### Document Loader Usage

Use a document loader to load data as LangChain `Document`s.
    
    
    from langchain_google_spanner import SpannerLoader
    
    
     loader = SpannerLoader(
         instance_id="my-instance",
         database_id="my-database",
         query="SELECT * from my_table_name"
     )
     docs = [loader](https://docs.cloud.google.com/python/docs/reference/langchain-google-spanner/latest).lazy_load()
    

See the full [Document Loader](https://github.com/googleapis/langchain-google-spanner-python/blob/main/docs/document_loader.ipynb) tutorial.

### Chat Message History Usage

Use `ChatMessageHistory` to store messages and provide conversation history to LLMs.
    
    
    from langchain_google_spanner import SpannerChatMessageHistory
    
    
     history = SpannerChatMessageHistory(
         instance_id="my-instance",
         database_id="my-database",
         table_name="my_table_name",
         session_id="my-session_id"
     )
    

See the full [Chat Message History](https://github.com/googleapis/langchain-google-spanner-python/blob/main/docs/chat_message_history.ipynb) tutorial.

### Spanner Graph Store Usage

Use `SpannerGraphStore` to store nodes and edges extracted from documents.
    
    
    from langchain_google_spanner import SpannerGraphStore
    
    
     graph = SpannerGraphStore(
         instance_id="my-instance",
         database_id="my-database",
         graph_name="my_graph",
     )
    

See the full [Spanner Graph Store](https://github.com/googleapis/langchain-google-spanner-python/blob/main/docs/graph_store.ipynb) tutorial.

### Spanner Graph QA Chain Usage

Use `SpannerGraphQAChain` for question answering over a graph stored in Spanner Graph.
    
    
    from langchain_google_spanner import SpannerGraphStore, SpannerGraphQAChain
    from langchain_google_vertexai import ChatVertexAI
    
    
    graph = SpannerGraphStore(
        instance_id="my-instance",
        database_id="my-database",
        graph_name="my_graph",
    )
    llm = ChatVertexAI()
    chain = SpannerGraphQAChain.from_llm(
        llm,
        graph=graph,
        allow_dangerous_requests=True
    )
    chain.invoke("query=Where does Sarah's sibling live?")
    

See the full [Spanner Graph QA Chain](https://github.com/googleapis/langchain-google-spanner-python/blob/main/docs/graph_qa_chain.ipynb) tutorial.

### Spanner Graph Retrievers Usage

Use `SpannerGraphTextToGQLRetriever` to translate natural language question to GQL and query SpannerGraphStore.
    
    
    from langchain_google_spanner import SpannerGraphStore, SpannerGraphTextToGQLRetriever
    from langchain_google_vertexai import ChatVertexAI
    
    
    graph = SpannerGraphStore(
        instance_id="my-instance",
        database_id="my-database",
        graph_name="my_graph",
    )
    llm = ChatVertexAI()
    retriever = SpannerGraphTextToGQLRetriever.from_params(
        graph_store=graph,
        llm=llm
    )
    retriever.invoke("Where does Elias Thorne's sibling live?")
    

Use `SpannerGraphVectorContextRetriever` to perform vector search on embeddings that are stored in the nodes in a SpannerGraphStore. If expand_by_hops is provided, the nodes and edges at a distance upto the expand_by_hops from the nodes found in the vector search will also be returned.
    
    
    from langchain_google_spanner import SpannerGraphStore, SpannerGraphVectorContextRetriever
    from langchain_google_vertexai import ChatVertexAI, VertexAIEmbeddings
    
    
    graph = SpannerGraphStore(
        instance_id="my-instance",
        database_id="my-database",
        graph_name="my_graph",
    )
    embedding_service = VertexAIEmbeddings(model_name="text-embedding-004")
    retriever = SpannerGraphVectorContextRetriever.from_params(
            graph_store=graph,
            embedding_service=embedding_service,
            label_expr="Person",
            embeddings_column="embeddings",
            top_k=1,
            expand_by_hops=1,
        )
    retriever.invoke("Who lives in desert?")
    

### Contributions

Contributions to this library are always welcome and highly encouraged.

See [CONTRIBUTING](https://github.com/googleapis/langchain-google-spanner-python/blob/main/CONTRIBUTING.md) for more information how to get started.

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. See [Code of Conduct](https://github.com/googleapis/langchain-google-spanner-python/blob/main/CODE_OF_CONDUCT.md) for more information.

## License

Apache 2.0 - See [LICENSE](https://github.com/googleapis/langchain-google-spanner-python/blob/main/LICENSE) for more information.

## Disclaimer

This is not an officially supported Google product.

## Limitations

  * Approximate Nearest Neighbors (ANN) strategies are only supported for the GoogleSQL dialect

  * ANN’s ALTER VECTOR INDEX is not yet supported by [Google Cloud Spanner](about:invalid#zCSafez)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
