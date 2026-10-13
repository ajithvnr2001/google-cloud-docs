---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextEmbeddingInput
title: Class TextEmbeddingInput (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:19.000550+00:00
---

# Class TextEmbeddingInput (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextEmbeddingInput

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TextEmbeddingInput (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    TextEmbeddingInput(
        text: str,
        task_type: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
    )

Structural text embedding input.

## Attributes  
  
---  
**Name** | **Description**  
`text` |  `str`   
The main text content to embed.   
`task_type` |  `Optional[str]`   
The name of the downstream task the embeddings will be used for. Valid values: RETRIEVAL_QUERY Specifies the given text is a query in a search/retrieval setting. RETRIEVAL_DOCUMENT Specifies the given text is a document from the corpus being searched. SEMANTIC_SIMILARITY Specifies the given text will be used for STS. CLASSIFICATION Specifies that the given text will be classified. CLUSTERING Specifies that the embeddings will be used for clustering. QUESTION_ANSWERING Specifies that the embeddings will be used for question answering. FACT_VERIFICATION Specifies that the embeddings will be used for fact verification. CODE_RETRIEVAL_QUERY Specifies that the embeddings will be used for code retrieval.   
`title` |  `Optional[str]`   
Optional identifier of the text content.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
