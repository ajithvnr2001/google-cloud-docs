---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/HybridContentItem/
title: HybridContentItem \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:45.577103+00:00
---

# HybridContentItem  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/HybridContentItem/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  HybridContentItem Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * HybridFindingDetails
    * JSON representation



An individual hybrid item to inspect. Will be stored temporarily during processing.

JSON representation  
---  
      
    
    {
      "item": {
        object ([ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem))
      },
      "findingDetails": {
        object ([HybridFindingDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/HybridContentItem#HybridFindingDetails))
      }
    }  
  
Fields  
---  
`item` |  `object (`[ContentItem](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentItem)`)` The item to inspect.  
`findingDetails` |  `object (`[HybridFindingDetails](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/HybridContentItem#HybridFindingDetails)`)` Supplementary information that will be added to each finding.  
  
## HybridFindingDetails

Populate to associate additional data with each finding.

JSON representation  
---  
      
    
    {
      "containerDetails": {
        object ([Container](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Container))
      },
      "fileOffset": string,
      "rowOffset": string,
      "tableOptions": {
        object ([TableOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#TableOptions))
      },
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`containerDetails` |  `object (`[Container](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Container)`)` Details about the container where the content being inspected is from.  
`fileOffset` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Offset in bytes of the line, from the beginning of the file, where the finding is located. Populate if the item being scanned is only part of a bigger item, such as a shard of a file and you want to track the absolute position of the finding.  
`rowOffset` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Offset of the row for tables. Populate if the row(s) being scanned are part of a bigger dataset and you want to keep track of their absolute position.  
`tableOptions` |  `object (`[TableOptions](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#TableOptions)`)` If the container is a table, additional information to make findings meaningful such as the columns that are primary keys. If not known ahead of time, can also be set within each inspect hybrid call and the two will be merged. Note that identifyingFields will only be stored to BigQuery, and only if the BigQuery action has been included.  
`labels` |  `map (key: string, value: string)` Labels to represent user provided metadata about the data being inspected. If configured by the job, some key values may be required. The labels associated with `Finding`'s produced by hybrid inspection.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.No more than 10 labels can be associated with a given finding.Examples:

  * `"environment" : "production"`
  * `"pipeline" : "etl"`

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
