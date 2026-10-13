---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors
title: REST Resource: organizations.datacollectors \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:31.246472+00:00
---

# REST Resource: organizations.datacollectors  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.datacollectors Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DataCollector
    * JSON representation
  * Type
  * Methods



## Resource: DataCollector

Data collector configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum ([Type](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors#Type)),
      "createdAt": string,
      "lastModifiedAt": string
    }  
  
Fields  
---  
`name` |  `string` ID of the data collector. Must begin with `dc_`.  
`description` |  `string` A description of the data collector.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors#Type)`)` Immutable. The type of data this data collector will collect.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The time at which the data collector was created in milliseconds since the epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The time at which the Data Collector was last updated in milliseconds since the epoch.  
  
## Type

Supported data types.

Enums  
---  
`TYPE_UNSPECIFIED` | For future compatibility.  
`INTEGER` | For integer values.  
`FLOAT` | For float values.  
`STRING` | For string values.  
`BOOLEAN` | For boolean values.  
`DATETIME` | For datetime values.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/create)`

|  Creates a new data collector.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/delete)`

|  Deletes a data collector.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/get)`

|  Gets a data collector.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/list)`

|  Lists all data collectors.  
  
### `[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.datacollectors/patch)`

|  Updates a data collector.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
