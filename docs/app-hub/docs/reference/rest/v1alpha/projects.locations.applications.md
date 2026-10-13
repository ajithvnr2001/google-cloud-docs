---
url: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications
title: REST Resource: projects.locations.applications \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:57.319542+00:00
---

# REST Resource: projects.locations.applications  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Reference ](https://docs.cloud.google.com/app-hub/docs/apis)



Send feedback 

#  REST Resource: projects.locations.applications Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Application
    * JSON representation
  * Scope
    * JSON representation
  * Type
  * State
  * Methods



## Resource: Application

Application defines the governance boundary for App Hub entities that perform a logical end-to-end business function. App Hub supports application level IAM permission to align with governance requirements.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "attributes": {
        object ([Attributes](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/Attributes))
      },
      "createTime": string,
      "updateTime": string,
      "scope": {
        object ([Scope](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications#Scope))
      },
      "uid": string,
      "state": enum ([State](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of an Application. Format: `"projects/{host-project-id}/locations/{location}/applications/{application-id}"`  
`displayName` |  `string` Optional. User-defined name for the Application. Can have a maximum length of 63 characters.  
`description` |  `string` Optional. User-defined description of an Application. Can have a maximum length of 2048 characters.  
`attributes` |  `object (`[Attributes](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/Attributes)`)` Optional. Consumer provided attributes.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`scope` |  `object (`[Scope](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications#Scope)`)` Required. Immutable. Defines what data can be included into this Application. Limits which Services and Workloads can be registered.  
`uid` |  `string` Output only. A universally unique identifier (in UUID4 format) for the `Application`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications#State)`)` Output only. Application state.  
  
## Scope

Scope of an application.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications#Type))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications#Type)`)` Required. Scope Type.  
  
## Type

Scope Type.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`REGIONAL` | Regional type.  
`GLOBAL` | Global type.  
  
## State

Application state.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`CREATING` | The Application is being created.  
`ACTIVE` | The Application is ready to register Services and Workloads.  
`DELETING` | The Application is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications/create)`

|  Creates an Application in a host project and location.  
  
### `[delete](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications/delete)`

|  Deletes an Application in a host project and location.  
  
### `[get](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications/get)`

|  Gets an Application in a host project and location.  
  
### `[getIamPolicy](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications/list)`

|  Lists Applications in a host project and location.  
  
### `[patch](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications/patch)`

|  Updates an Application in a host project and location.  
  
### `[setIamPolicy](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1alpha/projects.locations.applications/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
