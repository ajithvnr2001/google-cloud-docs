---
url: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.SearchEntriesRequest
title: Class SearchEntriesRequest (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:04.304545+00:00
---

# Class SearchEntriesRequest (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.SearchEntriesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchEntriesRequest (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.2  2.9.0  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.2  2.1.0  2.0.1  1.13.0  1.12.3  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.2  1.5.1  1.4.3  1.3.0  1.2.0  1.1.3  1.0.1  0.2.1  0.1.0 
    
    
    SearchEntriesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. The project to which the request should be attributed in the following form: `projects/{project}/locations/global`.   
`query` |  `str`   
Required. The query against which entries in scope should be matched. The query syntax is defined in `Search syntax for Dataplex Universal Catalog   
`page_size` |  `int`   
Optional. Number of results in the search page. If <=0, then="" defaults="" to="" 10.="" max="" limit="" for="" page_size="" is="" 1000.="" throws="" an="" invalid="" argument="" for="" page_size=""> 1000\.   
`page_token` |  `str`   
Optional. Page token received from a previous `SearchEntries` call. Provide this to retrieve the subsequent page.   
`order_by` |  `str`   
Optional. Specifies the ordering of results. Supported values are: \- `relevance` \- `last_modified_timestamp` \- `last_modified_timestamp asc`  
`scope` |  `str`   
Optional. The scope under which the search should be operating. It must either be `organizations/` or `projects/`. If it is unspecified, it defaults to the organization where the project provided in `name` is located.   
`semantic_search` |  `bool`   
Optional. Specifies whether the search should understand the meaning and intent behind the query, rather than just matching keywords.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
