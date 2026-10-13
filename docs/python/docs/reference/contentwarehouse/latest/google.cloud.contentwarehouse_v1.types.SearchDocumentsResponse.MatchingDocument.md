---
url: https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.SearchDocumentsResponse.MatchingDocument
title: Class MatchingDocument (0.11.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:56.640285+00:00
---

# Class MatchingDocument (0.11.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.SearchDocumentsResponse.MatchingDocument

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MatchingDocument (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.11.0  0.10.0  0.9.0  0.8.0  0.7.16  0.6.0  0.5.1  0.4.1  0.3.1  0.2.1  0.1.0 
    
    
    MatchingDocument(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Document entry with metadata inside SearchDocumentsResponse

## Attributes  
  
---  
**Name** | **Description**  
`document` |  `[google.cloud.contentwarehouse_v1.types.Document](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.Document)`   
Document that matches the specified SearchDocumentsRequest. This document only contains indexed metadata information.   
`search_text_snippet` |  `str`   
Contains snippets of text from the document full raw text that most closely match a search query's keywords, if available. All HTML tags in the original fields are stripped when returned in this field, and matching query keywords are enclosed in HTML bold tags. If the question-answering feature is enabled, this field will instead contain a snippet that answers the user's natural-language query. No HTML bold tags will be present, and highlights in the answer snippet can be found in QAResult.highlights.   
`qa_result` |  `[google.cloud.contentwarehouse_v1.types.QAResult](https://docs.cloud.google.com/python/docs/reference/contentwarehouse/latest/google.cloud.contentwarehouse_v1.types.QAResult)`   
Experimental. Additional result info if the question-answering feature is enabled.   
`matched_token_page_indices` |  `MutableSequence[int]`   
Return the 1-based page indices where those pages have one or more matched tokens.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
