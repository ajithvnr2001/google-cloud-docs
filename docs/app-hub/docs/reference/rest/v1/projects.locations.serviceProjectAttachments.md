---
url: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments
title: REST Resource: projects.locations.serviceProjectAttachments \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:42.449022+00:00
---

# REST Resource: projects.locations.serviceProjectAttachments  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Reference ](https://docs.cloud.google.com/app-hub/docs/apis)



Send feedback 

#  REST Resource: projects.locations.serviceProjectAttachments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ServiceProjectAttachment
    * JSON representation
  * State
  * Methods



## Resource: ServiceProjectAttachment

ServiceProjectAttachment represents an attachment from a service project to a host project. Service projects contain the underlying cloud infrastructure resources, and expose these resources to the host project through a ServiceProjectAttachment. With the attachments, the host project can provide an aggregated view of resources across all service projects.

JSON representation  
---  
      
    
    {
      "name": string,
      "serviceProject": string,
      "createTime": string,
      "uid": string,
      "state": enum ([State](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of a ServiceProjectAttachment. Format: `"projects/{host-project-id}/locations/global/serviceProjectAttachments/{service-project-id}."`  
`serviceProject` |  `string` Required. Immutable. Service project name in the format: `"projects/abc"` or `"projects/123"`. As input, project name with either project id or number are accepted. As output, this field will contain project number.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. A globally unique identifier (in UUID4 format) for the `ServiceProjectAttachment`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments#State)`)` Output only. ServiceProjectAttachment state.  
  
## State

ServiceProjectAttachment state.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`CREATING` | The ServiceProjectAttachment is being created.  
`ACTIVE` | The ServiceProjectAttachment is ready. This means Services and Workloads under the corresponding ServiceProjectAttachment is ready for registration.  
`DELETING` | The ServiceProjectAttachment is being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments/create)`

|  Attaches a service project to the host project.  
  
### `[delete](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments/delete)`

|  Deletes a service project attachment.  
  
### `[get](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments/get)`

|  Gets a service project attachment.  
  
### `[list](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/projects.locations.serviceProjectAttachments/list)`

|  Lists service projects attached to the host project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
