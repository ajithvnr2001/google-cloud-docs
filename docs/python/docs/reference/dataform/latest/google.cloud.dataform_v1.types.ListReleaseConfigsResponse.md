---
url: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.ListReleaseConfigsResponse
title: Class ListReleaseConfigsResponse (0.11.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:54.964733+00:00
---

# Class ListReleaseConfigsResponse (0.11.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.ListReleaseConfigsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListReleaseConfigsResponse (0.11.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.4 (latest)  0.11.3  0.10.0  0.9.0  0.8.0  0.7.0  0.6.2  0.5.16  0.4.1  0.3.0  0.2.3  0.1.0 
    
    
    ListReleaseConfigsResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

`ListReleaseConfigs` response message.

## Attributes  
  
---  
**Name** | **Description**  
`release_configs` |  `MutableSequence[[google.cloud.dataform_v1.types.ReleaseConfig](https://docs.cloud.google.com/python/docs/reference/dataform/latest/google.cloud.dataform_v1.types.ReleaseConfig)]`   
List of release configs.   
`next_page_token` |  `str`   
A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.   
`unreachable` |  `MutableSequence[str]`   
Locations which could not be reached.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
