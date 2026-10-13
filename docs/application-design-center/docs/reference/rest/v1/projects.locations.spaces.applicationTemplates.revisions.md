---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions
title: REST Resource: projects.locations.spaces.applicationTemplates.revisions \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:11.493493+00:00
---

# REST Resource: projects.locations.spaces.applicationTemplates.revisions  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.applicationTemplates.revisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ApplicationTemplateRevision
    * JSON representation
  * Methods



## Resource: ApplicationTemplateRevision

Application template revision resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "snapshot": {
        object ([SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate))
      },
      "artifactLocation": {
        object ([ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The application template revision name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The application template revision creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`snapshot` |  `object (`[SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate)`)` Output only. The serialized application template.  
`artifactLocation` |  `object (`[ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation)`)` Output only. Details of the location where the IaC for this ApplicationTemplate Revision was last successfully exported.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/delete)`

|  Deletes an application template revision.  
  
### `[export](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/export)`

|  Exports Terraform files for an application template revision.  
  
### `[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/generate)`

|  Generates Terraform files for an application template revision.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/get)`

|  Gets details about an application template revision.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/list)`

|  Lists application template revisions in a given application template.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
