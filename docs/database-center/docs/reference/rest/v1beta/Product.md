---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product/
title: Product \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:28.900048+00:00
---

# Product  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Product Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Product specification for databasecenter resources.

JSON representation  
---  
      
    
    {
      "type": enum ([ProductType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ProductType)),
      "engine": enum ([Engine](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Engine)),
      "version": string,
      "minorVersion": string
    }  
  
Fields  
---  
`type` |  `enum (`[ProductType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ProductType)`)` Optional. Type of specific database product. It could be CloudSQL, AlloyDB etc..  
`engine` |  `enum (`[Engine](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Engine)`)` Optional. The specific engine that the underlying database is running.  
`version` |  `string` Optional. Version of the underlying database engine. Example values: For MySQL, it could be "8.0", "5.7" etc. For Postgres, it could be "14", "15" etc.  
`minorVersion` |  `string` Optional. Minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
