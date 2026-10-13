---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups
title: REST Resource: organizations.envgroups \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:42.586387+00:00
---

# REST Resource: organizations.envgroups  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.envgroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EnvironmentGroup
    * JSON representation
  * Methods



## Resource: EnvironmentGroup

EnvironmentGroup configuration. An environment group is used to group one or more Apigee environments under a single host name.

JSON representation  
---  
      
    
    {
      "name": string,
      "hostnames": [
        string
      ],
      "createdAt": string,
      "lastModifiedAt": string,
      "state": enum (State)
    }  
  
Fields  
---  
`name` |  `string` ID of the environment group.  
`hostnames[]` |  `string` Required. Host names for this environment group.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The time at which the environment group was created as milliseconds since epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The time at which the environment group was last updated as milliseconds since epoch.  
`state` |  `enum (`State`)` Output only. State of the environment group. Values other than ACTIVE means the resource is not ready to use.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/create)`

|  Creates a new environment group.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/delete)`

|  Deletes an environment group.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/get)`

|  Gets an environment group.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/list)`

|  Lists all environment groups.  
  
### `[patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/patch)`

|  Updates an environment group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
