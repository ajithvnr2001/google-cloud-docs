---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BigQuerySource/
title: BigQuerySource \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:19.746737+00:00
---

# BigQuerySource  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/BigQuerySource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  BigQuerySource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



BigQuery source import data from.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "datasetId": string,
      "tableId": string,
      "gcsStagingDir": string,
      "dataSchema": string,
    
      // Union field partition can be only one of the following:
      "partitionDate": {
        object ([Date](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/Date))
      }
      // End of list of possible types for union field partition.
    }  
  
Fields  
---  
`projectId` |  `string` The project ID (can be project # or ID) that the BigQuery source is in with a length limit of 128 characters. If not specified, inherits the project ID from the parent request.  
`datasetId` |  `string` Required. The BigQuery data set to copy the data from with a length limit of 1,024 characters.  
`tableId` |  `string` Required. The BigQuery table to copy the data from with a length limit of 1,024 characters.  
`gcsStagingDir` |  `string` Intermediate Cloud Storage directory used for the import with a length limit of 2,000 characters. Can be specified if one wants to have the BigQuery export to a specific Cloud Storage directory.  
`dataSchema` |  `string` The schema to use when parsing the data from the source.Supported values for product imports:

  * `product` (default): One JSON `[Product](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product)` per line. Each product must have a valid `[Product.id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products#Product.FIELDS.id)`.
  * `product_merchant_center`: See [Importing catalog data from Merchant Center](https://cloud.google.com/retail/recommendations-ai/docs/upload-catalog#mc).

Supported values for user events imports:

  * `user_event` (default): One JSON `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent)` per line.
  * `user_event_ga360`: The schema is available here: <https://support.google.com/analytics/answer/3437719>.
  * `user_event_ga4`: The schema is available here: <https://support.google.com/analytics/answer/7029846>.

Supported values for autocomplete imports:

  * `suggestions` (default): One JSON completion suggestion per line.
  * `denylist`: One JSON deny suggestion per line.
  * `allowlist`: One JSON allow suggestion per line.

  
Union field `partition`. BigQuery table partition info. Leave this empty if the BigQuery table is not partitioned. `partition` can be only one of the following:  
`partitionDate` |  `object (`[Date](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/Date)`)` BigQuery time partitioned table's _PARTITIONDATE in YYYY-MM-DD format.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
