---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules
title: REST Resource: projects.locations.instances.alertGroupingRules \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:31.860108+00:00
---

# REST Resource: projects.locations.instances.alertGroupingRules  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.alertGroupingRules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AlertGroupingRule
    * JSON representation
  * AlertGroupingCategory
  * AlertGroupingType
  * CategoryDetail
    * JSON representation
  * Methods



## Resource: AlertGroupingRule

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. AlertGroupingRule - Chronicle Alert Grouping Rule. Types of AlertGroupingRules: general, case-spesific

JSON representation  
---  
      
    
    {
      "name": string,
      "entityType": [
        string
      ],
      "categoryDetails": [
        {
          object ([CategoryDetail](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules#CategoryDetail))
        }
      ],
      "category": enum ([AlertGroupingCategory](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules#AlertGroupingCategory)),
      "groupingType": enum ([AlertGroupingType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules#AlertGroupingType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the AlertGroupingRule. Format: projects/{project}/locations/{location}/instances/{instance}/alertGroupingRules/{alertGroupingRule}  
`entityType[]` |  `string` Required. AlertGroupingRule associated with the entityType.  
`categoryDetails[]` |  `object (`[CategoryDetail](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules#CategoryDetail)`)` Required. Defines the AlertGroupingRule category details list.  
`category` |  `enum (`[AlertGroupingCategory](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules#AlertGroupingCategory)`)` Required. The category of the new stage to create.  
`groupingType` |  `enum (`[AlertGroupingType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules#AlertGroupingType)`)` Required. Defines the AlertGroupingRule groupingType in the lifetime of a case.  
  
## AlertGroupingCategory

The category of the new stage to create.

Enums  
---  
`ALL` | All categories.  
`ALERT_TYPE` | Alert type.  
`PRODUCT_NAME` | Product name.  
`DATA_SOURCE` | Data source.  
  
## AlertGroupingType

Defines the AlertGroupingRule groupingType in the lifetime of a case.

Enums  
---  
`ENTITIES` | Entities.  
`SOURCE_GROUPING_IDENTIFIER` | Source grouping identifier.  
`NONE` | None.  
  
## CategoryDetail

Represents details of a category within an AlertGroupingRule.

JSON representation  
---  
      
    
    {
      "identifier": string,
      "displayName": string
    }  
  
Fields  
---  
`identifier` |  `string` Required. Unique identifier for the category detail.  
`displayName` |  `string` Required. Human-readable name for the category detail.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules/create)`

|  Creates a new alert grouping rule.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules/delete)`

|  Deletes an alert grouping rule.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules/get)`

|  Gets an alert grouping rule.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules/list)`

|  Lists alert grouping rules.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.alertGroupingRules/patch)`

|  Updates an existing alert grouping rule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
