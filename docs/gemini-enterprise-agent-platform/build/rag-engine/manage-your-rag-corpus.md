---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/manage-your-rag-corpus/
title: Manage your RAG knowledge base (corpus) \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:43:14.980911+00:00
---

# Manage your RAG knowledge base (corpus)  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/manage-your-rag-corpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Manage your RAG knowledge base (corpus) Stay organized with collections  Save and categorize content based on your preferences. 

The [VPC-SC security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) and CMEK are supported by Agent Platform RAG Engine. Data residency and AXT security controls aren't supported.

This page describes how you can manage your corpus for RAG tasks by performing corpus management and file management.

## Corpus management

A corpus, also referred to as an index, is a collection of documents or source of information. The corpus can be queried to retrieve relevant contexts for response generation. When creating a corpus for the first time, the process might take an additional minute.

The following corpus operations are supported:

Operation | Description | Parameters | Examples  
---|---|---|---  
Create a RAG corpus. |  Create a RAG corpus to import or upload documents. If you're using VPC-SC and it's the first time that you've called `createRagCorpus` and the call returns an error, then just wait a few minutes and retry.  |  [ Create parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora/create) [ Create parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora/create)  
Update a RAG corpus. |  Update a previously-created RAG corpus to import or upload documents.  |  [ Update parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora/patch) [ Update parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora/patch)  
List a RAG corpus. | List all of the RAG corpora. |  [ List parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora/list) [ List parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora/list)  
Get a RAG corpus. | Get the metadata describing the RAG corpus. |  [ Get parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora/get) [ Get parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora/get)  
Delete a RAG corpus. | Delete the RAG corpus. |  [ Delete parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora/delete) [ Delete parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora/delete)  
  
Concurrent operations on corpora aren't supported. For more information, see the [RAG API reference for v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora) or [RAG API reference for v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora).

### File management

The following file operations are supported:

Operation | Description | Parameters | Examples  
---|---|---|---  
Upload a RAG file. |  Upload a file from local storage with additional information that provides context to the LLM to generate more accurate responses.  |  [ Upload parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/media/upload) [ Upload parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/media/upload)  
Import RAG files. |  Import a set of files from some other storage into a storage location.  |  [ Import parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles/import) [ Import parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/import)  
List RAG files. | List all of the files in the RAG corpus. |  [ List parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles/list) [ List parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/list)  
Get a RAG file. | Get details about a RAG file for use by the LLM. |  [ Get parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles/get) [ Get parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/get)  
Delete a RAG file. | Delete a file from the RAG corpus. |  [ Delete parameters v1beta1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.ragCorpora.ragFiles/delete) [ Delete parameters v1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.ragCorpora.ragFiles/delete)  
  
## What's next

  * [RAG Engine on Gemini Enterprise Agent Platform quotas](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas#rag-engine-quotas)

  * To learn more about the RAG Engine on Gemini Enterprise Agent Platform, see the following:

    * [`RagEngineConfig`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagEngineConfig)

    * [`RagChunk`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagChunk)

    * [`RagContexts`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagContexts)

    * [`RagFileTransformationConfig`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagFileTransformationConfig)

    * [`RagQuery`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/RagQuery)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
