---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments
title: REST Resource: organizations.envgroups.attachments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:43.180052+00:00
---

# REST Resource: organizations.envgroups.attachments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.envgroups.attachments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EnvironmentGroupAttachment
    * JSON representation
  * Methods



## Resource: EnvironmentGroupAttachment

EnvironmentGroupAttachment is a resource which defines an attachment of an environment to an environment group.

JSON representation  
---  
      
    
    {
      "name": string,
      "environment": string,
      "createdAt": string,
      "environmentGroupId": string
    }  
  
Fields  
---  
`name` |  `string` ID of the environment group attachment.  
`environment` |  `string` Required. ID of the attached environment.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The time at which the environment group attachment was created as milliseconds since epoch.  
`environmentGroupId` |  `string` Output only. ID of the environment group.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/create)`

|  Creates a new attachment of an environment to an environment group.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/delete)`

|  Deletes an environment group attachment.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/get)`

|  Gets an environment group attachment.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments/list)`

|  Lists all attachments of an environment group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
