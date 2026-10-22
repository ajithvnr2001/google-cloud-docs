---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/fine-tune-rag-transformations/
title: Fine-tune RAG transformations \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:41:08.473428+00:00
---

# Fine-tune RAG transformations  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/fine-tune-rag-transformations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Fine-tune RAG transformations Stay organized with collections  Save and categorize content based on your preferences. 

The [VPC-SC security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) and CMEK are supported by Agent Platform RAG Engine. Data residency and AXT security controls aren't supported.

After a document is ingested, RAG Engine on Gemini Enterprise Agent Platform runs a set of transformations to prepare the data for indexing. You can control your use cases using the following parameters:

Parameter | Description  
---|---  
`chunk_size` |  When documents are ingested into an index, they're split into chunks. The `chunk_size` parameter (in tokens) specifies the size of the chunk. The default chunk size is 1,024 tokens.   
`chunk_overlap` |  By default, documents are split into chunks with a certain amount of overlap to improve relevance and retrieval quality. The default chunk overlap is 256 tokens.   
  
A smaller chunk size means the embeddings are more precise. A larger chunk size means that the embeddings might be more general but might miss specific details.

For example, if you convert 1,000 words into an embedding array that was meant for 200 words, you might lose details. The embedding capacity is fixed for each chunk. A large chunk of text may not fit into a small-window model.

## What's next

  * Use [Document AI layout parser with RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/layout-parser-integration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
