---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates
title: REST Resource: projects.locations.spaces.applicationTemplates \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:07.161241+00:00
---

# REST Resource: projects.locations.spaces.applicationTemplates  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.applicationTemplates Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ApplicationTemplate
    * JSON representation
  * Methods



## Resource: ApplicationTemplate

Application template resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "applicationParameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ],
      "iacFormat": enum ([IACFormat](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/IACFormat)),
      "serializedApplicationTemplate": {
        object ([SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate))
      },
      "latestRevision": string,
      "artifactLocation": {
        object ([ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation))
      },
      "compositionType": enum ([ApplicationCompositionType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationCompositionType)),
      "rootInputVariables": [
        {
          object ([ComponentVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentVariable))
        }
      ],
      "rootOutputVariables": [
        {
          object ([ComponentVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentVariable))
        }
      ],
      "saasRuntimeContext": {
        object ([SaaSRuntimeContext](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SaaSRuntimeContext))
      },
      "latestSystemRevisionUri": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Application template name.  
`displayName` |  `string` Optional. Application template display name.  
`description` |  `string` Optional. Application template description.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Application template creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Application template update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`applicationParameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Optional. Parameters to apply to all components in an application. You can specify projectID and region.  
`iacFormat` |  `enum (`[IACFormat](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/IACFormat)`)` Output only. The IaC format of the application template.  
`serializedApplicationTemplate` |  `object (`[SerializedApplicationTemplate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SerializedApplicationTemplate)`)` Output only. The serialized application template.  
`latestRevision` |  `string` Output only. The latest application template revision.  
`artifactLocation` |  `object (`[ArtifactLocation](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ArtifactLocation)`)` Output only. Details of the location where the IaC for this ApplicationTemplate was last successfully exported.  
`compositionType` |  `enum (`[ApplicationCompositionType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ApplicationCompositionType)`)` Optional. Immutable. The composition type of the applicationTemplate: STANDARD OR COMPOSITE. This is a create time only param.  
`rootInputVariables[]` |  `object (`[ComponentVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentVariable)`)` Optional. Root level input variables of the application template.  
`rootOutputVariables[]` |  `object (`[ComponentVariable](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentVariable)`)` Optional. Root level output variables of the application template.  
`saasRuntimeContext` |  `object (`[SaaSRuntimeContext](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/SaaSRuntimeContext)`)` Optional. SaaS runtime context for the application template.  
`latestSystemRevisionUri` |  `string` Output only. The URI of the most recent System Revision generated for this ApplicationTemplate. This ID corresponds to the `name` field in the ApplicationTemplateSystemRevision resource.  
  
## Methods  
  
---  
  
### `[commit](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/commit)`

|  Commits an application template to create a new revision.  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/create)`

|  Creates an application template.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/delete)`

|  Deletes an application template.  
  
### `[export](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/export)`

|  Exports Terraform files for an application template.  
  
### `[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/generate)`

|  Generates Terraform files for an application template.  
  
### `[generateAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/generateAssessmentReport)`

|  Generate assessment reports of an application template.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/get)`

|  Gets details about an application template.  
  
### `[import](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/import)`

|  Imports to an existing application template from a given shared template.  
  
### `[importIaC](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/importIaC)`

|  Imports IaC for an application template.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/list)`

|  Lists application templates in a given space.  
  
### `[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/patch)`

|  Updates an application template.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
