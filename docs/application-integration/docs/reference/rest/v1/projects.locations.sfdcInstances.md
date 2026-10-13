---
url: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances
title: REST Resource: projects.locations.sfdcInstances \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:23.098847+00:00
---

# REST Resource: projects.locations.sfdcInstances  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback 

#  REST Resource: projects.locations.sfdcInstances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SfdcInstance
    * JSON representation
  * Methods



## Resource: SfdcInstance

The SfdcInstance resource use to hold channels and connection config data.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "sfdcOrgId": string,
      "authConfigId": [
        string
      ],
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "serviceAuthority": string
    }  
  
Fields  
---  
`name` |  `string` Resource name of the SFDC instance projects/{project}/locations/{location}/sfdcInstances/{sfdcInstance}.  
`displayName` |  `string` Optional. User selected unique name/alias to easily reference an instance.  
`description` |  `string` Optional. A description of the sfdc instance.  
`sfdcOrgId` |  `string` The SFDC Org id. This is defined in salesforce.  
`authConfigId[]` |  `string` A list of AuthConfigs that can be tried to open the channel to SFDC  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the instance is createdUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the instance was last updatedUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time when the instance was deleted. Empty if not deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`serviceAuthority` |  `string` Optional. URL used for API calls after authentication (the login authority is configured within the referenced AuthConfig).  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances/create)`

|  Creates an sfdc instance record.  
  
### `[delete](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances/delete)`

|  Deletes an sfdc instance.  
  
### `[get](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances/get)`

|  Gets an sfdc instance.  
  
### `[list](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances/list)`

|  Lists all sfdc instances that match the filter.  
  
### `[patch](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.sfdcInstances/patch)`

|  Updates an sfdc instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-22 UTC."],[],[]] 
