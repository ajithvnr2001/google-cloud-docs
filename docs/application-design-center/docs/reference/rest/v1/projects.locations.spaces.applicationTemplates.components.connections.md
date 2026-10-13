---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections
title: REST Resource: projects.locations.spaces.applicationTemplates.components.connections \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:02.096067+00:00
---

# REST Resource: projects.locations.spaces.applicationTemplates.components.connections  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.applicationTemplates.components.connections Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Connection
    * JSON representation
  * Methods



## Resource: Connection

Connection resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "destinationComponentUri": string,
      "createTime": string,
      "updateTime": string,
      "sourceComponentParameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ],
      "destinationComponentParameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The connection name.  
`destinationComponentUri` |  `string` Required. The destination component URI used to generate the connection. Format is `projects/$project/locations/$location/spaces/$space/applicationTemplates/$applicationTemplate/components/$component`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The connection creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The connection update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sourceComponentParameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Optional. The parameters of the connection associated with the source component.  
`destinationComponentParameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Optional. The parameters of the connection associated with the destination component.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/create)`

|  Creates a connection.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/delete)`

|  Deletes a connection.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/get)`

|  Gets details about a connection.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/list)`

|  Lists connections in an application template.  
  
### `[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/patch)`

|  Updates a connection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
