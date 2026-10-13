---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesRequest
title: Class SearchResourcesRequest (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:53.495717+00:00
---

# Class SearchResourcesRequest (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchResourcesRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    SearchResourcesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The SearchResources method's request.

## Attributes  
  
---  
**Name** | **Description**  
`location` |  `str`   
Required. The resource name of the location which will be of the type `projects/{project_id}/locations/{location_id}`. This field is used to identify the instance of API-Hub in which resources should be searched.   
`query` |  `str`   
Required. The free text search query. This query can contain keywords which could be related to any detail of the API-Hub resources such display names, descriptions, attributes etc.   
`filter` |  `str`   
Optional. An expression that filters the list of search results. A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be `=`. Filters are not case sensitive. The following field names are eligible for filtering: \\* `resource_type` \- The type of resource in the search results. Must be one of the following: `Api`, `ApiOperation`, `Deployment`, `Definition`, `Spec` or `Version`. This field can only be specified once in the filter. Here are is an example: \- `resource_type = Api` \- The resource_type is *Api*.   
`page_size` |  `int`   
Optional. The maximum number of search results to return. The service may return fewer than this value. If unspecified at most 10 search results will be returned. If value is negative then `INVALID_ARGUMENT` error is returned. The maximum value is 25; values above 25 will be coerced to 25. While paginating, you can specify a new page size parameter for each page of search results to be listed.   
`page_token` |  `str`   
Optional. A page token, received from a previous `SearchResources][SearchResources]` call. Specify this parameter to retrieve the next page of transactions. When paginating, you must specify the `page_token` parameter and all the other parameters except page_size should be specified with the same value which was used in the previous call. If the other fields are set with a different value than the previous call then `INVALID_ARGUMENT` error is returned.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
