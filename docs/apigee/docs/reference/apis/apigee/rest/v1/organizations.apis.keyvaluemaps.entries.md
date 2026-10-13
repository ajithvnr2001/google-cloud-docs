---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries
title: REST Resource: organizations.apis.keyvaluemaps.entries \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:23.628575+00:00
---

# REST Resource: organizations.apis.keyvaluemaps.entries  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.apis.keyvaluemaps.entries Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: KeyValueEntry
    * JSON representation
  * Methods



## Resource: KeyValueEntry

Key value map pair where the value represents the data associated with the corresponding key.

**Note** : Supported for Apigee hybrid 1.8.x and higher.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Resource URI that can be used to identify the scope of the key value map entries.  
`value` |  `string` Required. Data or payload that is being retrieved and associated with the unique key.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/create)`

|  Creates key value entries in a key value map scoped to an organization, environment, or API proxy.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/delete)`

|  Deletes a key value entry from a key value map scoped to an organization, environment, or API proxy.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/get)`

|  Get the key value entry value for a key value map scoped to an organization, environment, or API proxy.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/list)`

|  Lists key value entries for key values maps scoped to an organization, environment, or API proxy.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apis.keyvaluemaps.entries/update)`

|  Update key value entry scoped to an organization, environment, or API proxy for an existing key.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
