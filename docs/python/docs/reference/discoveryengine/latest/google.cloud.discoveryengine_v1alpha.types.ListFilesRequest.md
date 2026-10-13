---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListFilesRequest
title: Class ListFilesRequest (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:06:29.646312+00:00
---

# Class ListFilesRequest (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.ListFilesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListFilesRequest (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    ListFilesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for SessionService.ListFiles method.

## Attributes  
  
---  
**Name** | **Description**  
`parent` |  `str`   
Required. The resource name of the Session. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}` Name of the session resource to which the file belong.   
`filter` |  `str`   
Optional. The filter syntax consists of an expression language for constructing a predicate from one or more fields of the files being filtered. Filter expression is case-sensitive. Currently supported field names are: \- upload_time \- last_add_time \- last_use_time \- file_name \- mime_type Some examples of filters would be: \- "file_name = 'file_1'" \- "file_name = 'file_1' AND mime_type = 'text/plain'" \- "last_use_time > '2025-06-14T12:00:00Z'" For a full description of the filter format, please see https://google.aip.dev/160.   
`page_size` |  `int`   
Optional. The maximum number of files to return. The service may return fewer than this value. If unspecified, at most 100 files will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. If user specifies a value less than or equal to 0 - the request will be rejected with an INVALID_ARGUMENT error.   
`page_token` |  `str`   
Optional. A page token received from a previous `ListFiles` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListFiles` must match the call that provided the page token (except `page_size`, which may differ).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
