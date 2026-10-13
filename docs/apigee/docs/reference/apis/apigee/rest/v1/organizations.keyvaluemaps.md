---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps
title: REST Resource: organizations.keyvaluemaps \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:37.294843+00:00
---

# REST Resource: organizations.keyvaluemaps  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.keyvaluemaps Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: KeyValueMap
    * JSON representation
  * Methods



## Resource: KeyValueMap

Collection of key/value string pairs.

JSON representation  
---  
      
    
    {
      "name": string,
      "encrypted": boolean,
      "maskedValues": boolean
    }  
  
Fields  
---  
`name` |  `string` Required. ID of the key value map.  
`encrypted` |  `boolean` Required. Flag that specifies whether entry values will be encrypted. This field is retained for backward compatibility and the value of encrypted will always be `true`. Apigee X and hybrid do not support unencrypted key value maps.  
`maskedValues` |  `boolean` Optional. Flag that specifies whether entry values will be masked when returned.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/create)`

|  Creates a key value map in an organization.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/delete)`

|  Deletes a key value map from an organization.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/get)`

|  Get the key value map scoped to an organization, environment, or API proxy.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/list)`

|  Lists key value maps in an organization.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.keyvaluemaps/update)`

|  Update the key value map scoped to an organization, environment, or API proxy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
