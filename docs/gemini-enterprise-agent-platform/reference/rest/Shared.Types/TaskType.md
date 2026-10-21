---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TaskType/
title: TaskType \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:56:45.414117+00:00
---

# TaskType  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TaskType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TaskType Stay organized with collections  Save and categorize content based on your preferences. 

Represents the downstream task the embeddings will be used for. Specifying the task type helps the model generate embeddings that are optimized for your use case. New task types may be added in the future.

Enums  
---  
`DEFAULT` | Task type not specified. The model will use a default value suitable for semantic similarity and retrieval.  
`RETRIEVAL_QUERY` | Specifies the given text is a query in a search/retrieval setting. Use this task type for embeddings that will be used to search a corpus of documents.  
`RETRIEVAL_DOCUMENT` | Specifies the given text is a document from the corpus being searched. Use this task type for texts that are part of a corpus that will be searched.  
`SEMANTIC_SIMILARITY` | Use this task type for Semantic Textual Similarity (STS). These embeddings will be compared with each other to measure semantic similarity.  
`CLASSIFICATION` | Specifies that the given text will be classified. Use this task type to generate embeddings that will be used as input to a classification model (e.g., classifying text as spam or not spam).  
`CLUSTERING` | Specifies that the embeddings will be used for clustering. Use this task type to generate embeddings that will be used to group similar texts together.  
`QUESTION_ANSWERING` | Specifies that the embeddings will be used for question answering. Use this task type to generate embeddings for texts that are part of a question answering system.  
`FACT_VERIFICATION` | Specifies that the embeddings will be used for fact verification. Use this task type to generate embeddings for texts that are part of a fact verification system.  
`CODE_RETRIEVAL_QUERY` | Specifies that the embeddings will be used for code retrieval. Use this task type for embeddings that will be used to search a corpus of code.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
