---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups
title: REST Resource: organizations.appgroups \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:25.990892+00:00
---

# REST Resource: organizations.appgroups  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.appgroups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AppGroup
    * JSON representation
  * Methods



## Resource: AppGroup

AppGroup contains the request/response fields representing the logical grouping of apps. Note that appgroup_id, createTime and updateTime cannot be changed by the user, and gets updated by the system. The name and the organization once provided cannot be edited subsequently.

JSON representation  
---  
      
    
    {
      "appGroupId": string,
      "name": string,
      "channelUri": string,
      "channelId": string,
      "displayName": string,
      "organization": string,
      "status": string,
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ],
      "createdAt": string,
      "lastModifiedAt": string,
      "email": string
    }  
  
Fields  
---  
`appGroupId` |  `string` Output only. Internal identifier that cannot be edited  
`name` |  `string` Immutable. Name of the AppGroup. Characters you can use in the name are restricted to: A-Z0-9._-$ %.  
`channelUri` |  `string` A reference to the associated storefront/marketplace.  
`channelId` |  `string` channel identifier identifies the owner maintaing this grouping.  
`displayName` |  `string` app group name displayed in the UI  
`organization` |  `string` Immutable. the org the app group is created  
`status` |  `string` Valid values are `active` or `inactive`. Note that the status of the AppGroup should be updated via UpdateAppGroupRequest by setting the action as `active` or `inactive`.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` A list of attributes  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Created time as milliseconds since epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Modified time as milliseconds since epoch.  
`email` |  `string` Optional. Email of the AppGroup.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/create)`

|  Creates an AppGroup.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/delete)`

|  Deletes an AppGroup.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/get)`

|  Returns the AppGroup details for the provided AppGroup name in the request URI.  
  
### `[getBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/getBalance)`

|  Gets the account balance for the AppGroup.  
  
### `[getMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/getMonetizationConfig)`

|  Gets the monetization configuration for the AppGroup.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/list)`

|  Lists all AppGroups in an organization.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/update)`

|  Updates an AppGroup.  
  
### `[updateMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups/updateMonetizationConfig)`

|  Updates the monetization configuration for the AppGroup.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
