---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult
title: Class SearchResult (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:43.958192+00:00
---

# Class SearchResult (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchResult (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    SearchResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

## Attributes  
  
---  
**Name** | **Description**  
`document` |  `str`   
Document resource name.   
`uri` |  `str`   
URI for the document.   
`title` |  `str`   
Title.   
`snippet_info` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult.SnippetInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult.SnippetInfo)]`   
If citation_type is DOCUMENT_LEVEL_CITATION, populate document level snippets.   
`chunk_info` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult.ChunkInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.Answer.Step.Action.Observation.SearchResult.ChunkInfo)]`   
If citation_type is CHUNK_LEVEL_CITATION and chunk mode is on, populate chunk info.   
`struct_data` |  `google.protobuf.struct_pb2.Struct`   
Data representation. The structured JSON data for the document. It's populated from the struct data from the Document, or the Chunk in search result.   
  
## Classes 

### ChunkInfo
    
    
    ChunkInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Chunk information.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### SnippetInfo
    
    
    SnippetInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Snippet information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
