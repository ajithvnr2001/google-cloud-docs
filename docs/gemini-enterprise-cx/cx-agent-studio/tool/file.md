---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/file/
title: File search tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:24.876899+00:00
---

# File search tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  File search tools Stay organized with collections  Save and categorize content based on your preferences. 

Using the file search tool, you can upload files and use them as a resource for Retrieval Augmented Generation (RAG). File search tools is a simpler alternative to [Data store tools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/data-store).

When uploading files, you can select either local files for upload or an existing [RAG knowledge base](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/manage-your-rag-corpus). If you select local files, a RAG knowledge base is created for you.

## Configuration

The tool requires the following configuration items:

  * **Name** : Descriptive name that helps AI understand the tool's job.
  * **Description** : Description of the tool that helps AI decide when to use the tool.
  * **Location** : Location of the automatically created knowledge base when you are uploading a local file.
  * **Files** : Select either local file or RAG Knowledge Base, then upload a file or select the knowledge base.



## Output

The tool performs a search on the connected RAG knowledge base and retrieves relevant search results. It then produces an optimized prompt, incorporating the user's query, retrieved search results, and instructions for writing a good-quality answer. The calling agent may use this output to produce an answer.

## Limitations

RAG knowledge bases are restricted to [these regions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/rag-overview#supported-regions).

## Billing

Use of RAG Engine will incur additional costs from that product in addition to the costs associated with use of CX Agent Studio.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
