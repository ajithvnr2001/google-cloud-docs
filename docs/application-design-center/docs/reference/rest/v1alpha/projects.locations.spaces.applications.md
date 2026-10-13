---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications
title: REST Resource: projects.locations.spaces.applications \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:30.055309+00:00
---

# REST Resource: projects.locations.spaces.applications  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.applications Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Application
    * JSON representation
  * Methods



## Resource: Application

Represents the application resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "source": {
        object (DeploymentSource)
      },
      "appParameters": [
        {
          object (Parameter)
        }
      ],
      "componentParameters": [
        {
          object (ComponentParameters)
        }
      ],
      "serviceAccount": string,
      "displayName": string,
      "description": string,
      "attributes": {
        object ([Attributes](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes))
      },
      "scope": {
        object ([Scope](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Scope))
      },
      "importExistingResources": boolean,
      "previewReference": string,
      "deploymentRevision": string,
      "apphubApplication": string,
      "serializedApplicationTemplate": {
        object (SerializedApplicationTemplate)
      },
      "state": enum (State),
      "deploymentMetadata": {
        object (DeploymentMetadata)
      },
      "projectParameters": [
        {
          object (ProjectParameters)
        }
      ],
      "deploymentRegion": string,
      "updatedTemplateRevision": {
        object (UpdatedTemplateRevision)
      },
      "deploymentProject": string,
      "connectionConfigs": [
        {
          object (ConnectionConfig)
        }
      ],
      "artifactLocation": {
        object (ArtifactLocation)
      },
      "type": enum (ApplicationType),
      "deploymentTarget": {
        object (DeploymentTarget)
      },
      "compositionType": enum (ApplicationCompositionType),
      "compositeApplicationParameters": {
        object (CompositeApplicationParameters)
      },
      "deploymentGroupMetadata": {
        object (DeploymentGroupMetadata)
      },
      "paramsUpdateStrategy": enum (UpdateStrategy)
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the application. Format: projects/{project}/locations/{location}/spaces/{space}/applications/{application}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`source` |  `object (`DeploymentSource`)` Required. The application deployment source.  
`appParameters[]` |  `object (`Parameter`)` Optional. A list of parameters to attach to the deployment source object, which is a catalog entry or application template snapshot.  
`componentParameters[]` |  `object (`ComponentParameters`)` Optional. A list of component parameters to associate with the application.  
`serviceAccount` |  `string` Optional. Your own service account that you use to deploy an application.  
`displayName` |  `string` Optional. Display name of the application.  
`description` |  `string` Optional. Description of the application.  
`attributes` |  `object (`[Attributes](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes)`)` Optional. Attributes of the application.  
`scope` |  `object (`[Scope](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Scope)`)` Required. Scope of the application.  
`importExistingResources` |  `boolean` Optional. Import existing resources into the application.  
`previewReference` |  `string` Output only. Preview reference for the application.  
`deploymentRevision` |  `string` Output only. [Output only] Optional Infra Manager deployment Id with revision  
`apphubApplication` |  `string` Output only. The App Hub App associated with the application.  
`serializedApplicationTemplate` |  `object (`SerializedApplicationTemplate`)` Output only. [Output only] Serialized application template.  
`state` |  `enum (`State`)` Output only. Deployment state of the application.  
`deploymentMetadata` |  `object (`DeploymentMetadata`)` Output only. Deployment metadata of the application.  
`projectParameters[]` |  `object (`ProjectParameters`)` Output only. List of project parameters for the application.  
`deploymentRegion` |  `string` Optional. The region where the application is deployed.  
`updatedTemplateRevision` |  `object (`UpdatedTemplateRevision`)` Output only. The updated template revision because of which the application is outdated.  
`deploymentProject` |  `string` Optional. Deployment project of the application.  
`connectionConfigs[]` |  `object (`ConnectionConfig`)` Optional. Connection configuration for the application.  
`artifactLocation` |  `object (`ArtifactLocation`)` Output only. Details of the location where the IaC for this application was last successfully exported.  
`type` |  `enum (`ApplicationType`)` Optional. The type of the application.  
`deploymentTarget` |  `object (`DeploymentTarget`)` Optional. The deployment target of the application.  
`compositionType` |  `enum (`ApplicationCompositionType`)` Output only. The composition type of the application: STANDARD OR COMPOSITE.  
`compositeApplicationParameters` |  `object (`CompositeApplicationParameters`)` Optional. Parameters that are required for composite applications.  
`deploymentGroupMetadata` |  `object (`DeploymentGroupMetadata`)` Output only. The deployment group metadata of the application. This is applicable only for composite applications.  
`paramsUpdateStrategy` |  `enum (`UpdateStrategy`)` Optional. Specifies the strategy to use when updating the application parameters while updating the application template revision.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/create)`

|  Creates an application.  
  
### `[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/delete)`

|  Deletes an application.  
  
### `[deploy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/deploy)`

|  Deploys an application.  
  
### `[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/fetchAssessmentReport)`

|  Fetches the assessment report of a deployed application if present.  
  
### `[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/generate)`

|  Generates Terraform files for an application.  
  
### `[generateAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/generateAssessmentReport)`

|  Generate assessment reports of an application.  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/get)`

|  Gets details about an application.  
  
### `[importIaC](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/importIaC)`

|  Imports IaC for an application resource.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/list)`

|  Lists applications in a given space.  
  
### `[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/patch)`

|  Updates an application.  
  
### `[preview](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/preview)`

|  Previews deployment of an application.  
  
### `[register](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/register)`

|  Register deployed application from terraform state file with App Hub.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
