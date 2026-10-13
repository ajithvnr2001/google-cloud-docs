---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions
title: REST Resource: projects.locations.instances.remediationPlans.remediationActions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:57.724569+00:00
---

# REST Resource: projects.locations.instances.remediationPlans.remediationActions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.remediationPlans.remediationActions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RemediationAction
    * JSON representation
    * ActionOriginType
    * ActionInstanceCreator
  * Methods



## Resource: RemediationAction

Represents a SecOps single remediation action, part of a Remediation Plan.

JSON representation  
---  
      
    
    {
      "name": string,
      "integrationId": string,
      "integrationInstance": string,
      "displayName": string,
      "type": enum ([ActionOriginType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions#RemediationAction.ActionOriginType)),
      "creator": enum ([ActionInstanceCreator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions#RemediationAction.ActionInstanceCreator)),
      "actionReasoning": string,
      "parameters": {
        object
      },
      "targetEntities": [
        {
          object
        }
      ],
      "actionGeneration": {
        object
      },
      "additionalData": {
        object
      },
      "metadata": {
        object
      },
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name of the remediation plan action.  
`integrationId` |  `string` Optional. Integration identifier (name, e.g. "GoogleCloudIAM").  
`integrationInstance` |  `string` Optional. Integration instance (e.g. "prod-tenant-1").  
`displayName` |  `string` Optional. Name of the action (e.g. "Disable Service Account").  
`type` |  `enum (`[ActionOriginType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions#RemediationAction.ActionOriginType)`)` Optional. Origin type of the action.  
`creator` |  `enum (`[ActionInstanceCreator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions#RemediationAction.ActionInstanceCreator)`)` Optional. Source of who added this action to the plan.  
`actionReasoning` |  `string` Optional. Reasoning explaining why this specific action was proposed.  
`parameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Action parameters. Struct enables JSON dynamic storage.  
`targetEntities[]` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Target entities for this action.  
`actionGeneration` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Field to store json with python code and action definition for dynamic scripts.  
`additionalData` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Additional unstructured data.  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Metadata for the action.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Modification time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### ActionOriginType

The origin type of the actions whether existing or generated code.

Enums  
---  
`ACTION_ORIGIN_TYPE_UNSPECIFIED` | Unspecified type.  
`ACTION_ORIGIN_TYPE_GENERATED` | Action was dynamically generated (drafted) by the LLM.  
`ACTION_ORIGIN_TYPE_EXISTING` | Action pre-existed in the integrations repository (Partner/Community).  
  
### ActionInstanceCreator

The creator of the action instance whether the user or the AI agent.

Enums  
---  
`ACTION_INSTANCE_CREATOR_UNSPECIFIED` | Unspecified user type.  
`ACTION_INSTANCE_CREATOR_USER` | Manually attached by the user (SOC analyst).  
`ACTION_INSTANCE_CREATOR_AI` | Automatically attached by the Remediation Agent (AI).  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions/create)`

|  Creates a manual Remediation Action under a plan.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions/get)`

|  Retrieves an individual Remediation Action.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.remediationPlans.remediationActions/list)`

|  Lists Remediation Actions under a plan.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
