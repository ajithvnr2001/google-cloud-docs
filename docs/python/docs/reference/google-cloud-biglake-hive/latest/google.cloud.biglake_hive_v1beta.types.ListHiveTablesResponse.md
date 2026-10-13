---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-biglake-hive/latest/google.cloud.biglake_hive_v1beta.types.ListHiveTablesResponse
title: Class ListHiveTablesResponse (0.3.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:45.172473+00:00
---

# Class ListHiveTablesResponse (0.3.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-biglake-hive/latest/google.cloud.biglake_hive_v1beta.types.ListHiveTablesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListHiveTablesResponse (0.3.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.5 (latest)  0.3.4  0.2.0  0.1.0 
    
    
    ListHiveTablesResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Response message for the ListHiveTables method.

## Attributes  
  
---  
**Name** | **Description**  
`tables` |  `MutableSequence[[google.cloud.biglake_hive_v1beta.types.HiveTable](https://docs.cloud.google.com/python/docs/reference/google-cloud-biglake-hive/latest/google.cloud.biglake_hive_v1beta.types.HiveTable)]`   
Output only. The tables from the specified project, catalog and database.   
`next_page_token` |  `str`   
Output only. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
