---
url: https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.DataSource.DataRefreshType
title: Class DataRefreshType (3.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:38.682026+00:00
---

# Class DataRefreshType (3.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerydatatransfer/latest/google.cloud.bigquery_datatransfer_v1.types.DataSource.DataRefreshType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataRefreshType (3.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.24.0 (latest)  3.23.0  3.22.0  3.21.0  3.20.0  3.19.2  3.18.0  3.17.1  3.16.0  3.15.7  3.14.1  3.13.0  3.12.1  3.11.2  3.10.1  3.9.0  3.8.0  3.7.3  3.6.2  3.5.0  3.4.1  3.3.4  3.2.0  3.1.1  3.0.1  2.1.2  2.0.0  1.1.3  1.0.0  0.4.1 
    
    
    DataRefreshType(value)

Represents how the data source supports data auto refresh.

## Enums  
  
---  
**Name** | **Description**  
`DATA_REFRESH_TYPE_UNSPECIFIED` | The data source won't support data auto refresh, which is default value.  
`SLIDING_WINDOW` | The data source supports data auto refresh, and runs will be scheduled for the past few days. Does not allow custom values to be set for each transfer config.  
`CUSTOM_SLIDING_WINDOW` | The data source supports data auto refresh, and runs will be scheduled for the past few days. Allows custom values to be set for each transfer config.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
