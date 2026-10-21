---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments
title: REST Resource: projects.locations.apps.deployments \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:50.394051+00:00
---

# REST Resource: projects.locations.apps.deployments  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.deployments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Deployment
    * JSON representation
  * ExperimentConfig
    * JSON representation
  * ExperimentConfig.VersionRelease
    * JSON representation
  * ExperimentConfig.State
  * ExperimentConfig.VersionRelease.TrafficAllocation
    * JSON representation
  * WhatsAppCredentials
    * JSON representation
  * InstagramCredentials
    * JSON representation
  * Deployment.Modality
  * AgentRegistryDeployment
    * JSON representation
  * Methods



## Resource: Deployment

A deployment represents an immutable, queryable version of the app. It is used to deploy an app version with a specific channel profile.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "appVersion": string,
      "channelProfile": {
        object ([ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ChannelProfile))
      },
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "experimentConfig": {
        object ([ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#ExperimentConfig))
      },
      "whatsappCredentials": {
        object ([WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#WhatsAppCredentials))
      },
      "instagramCredentials": {
        object ([InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#InstagramCredentials))
      },
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings))
      },
      "modality": enum ([Deployment.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#Deployment.Modality)),
      "agentRegistryDeployment": {
        object ([AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#AgentRegistryDeployment))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`displayName` |  `string` Required. Display name of the deployment.  
`appVersion` |  `string` Optional. The resource name of the app version to deploy. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}` Use `projects/{project}/locations/{location}/apps/{app}/versions/-` to use the draft app.  
`channelProfile` |  `object (`[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ChannelProfile)`)` Required. The channel profile used in the deployment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this deployment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this deployment was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`experimentConfig` |  `object (`[ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#ExperimentConfig)`)` Optional. Experiment configuration for the deployment.  
`whatsappCredentials` |  `object (`[WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#WhatsAppCredentials)`)` Optional. Input only. Ephemeral WhatsApp credentials required when configuring a WhatsApp channel profile.  
`instagramCredentials` |  `object (`[InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#InstagramCredentials)`)` Optional. Input only. Ephemeral Instagram credentials required when configuring a Instagram channel profile.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings)`)` Optional. Model settings for the deployment. Overrides model settings configured at the app/agent levels. Note: Deployment-level model settings override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`modality` |  `enum (`[Deployment.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#Deployment.Modality)`)` Optional. The modality of the deployment. Note: Deployment-level modality override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`agentRegistryDeployment` |  `object (`[AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#AgentRegistryDeployment)`)` Optional. Configuration for deploying this deployment to Agent Registry. If present, this deployment will be published to Agent Registry.  
  
## ExperimentConfig

Experiment for the deployment.

JSON representation  
---  
      
    
    {
      "versionRelease": {
        object ([ExperimentConfig.VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#ExperimentConfig.VersionRelease))
      }
    }  
  
Fields  
---  
`versionRelease` |  `object (`[ExperimentConfig.VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#ExperimentConfig.VersionRelease)`)` Optional. Version release for the experiment.  
  
## ExperimentConfig.VersionRelease

Version release for the experiment.

JSON representation  
---  
      
    
    {
      "state": enum ([ExperimentConfig.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#ExperimentConfig.State)),
      "trafficAllocations": [
        {
          object ([ExperimentConfig.VersionRelease.TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#ExperimentConfig.VersionRelease.TrafficAllocation))
        }
      ]
    }  
  
Fields  
---  
`state` |  `enum (`[ExperimentConfig.State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#ExperimentConfig.State)`)` Optional. State of the version release.  
`trafficAllocations[]` |  `object (`[ExperimentConfig.VersionRelease.TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments#ExperimentConfig.VersionRelease.TrafficAllocation)`)` Optional. Traffic allocations for the version release.  
  
## ExperimentConfig.State

State of the experiment.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`PENDING` | Deprecated: This state is no longer used.  
`RUNNING` | Running state. Experiment is running and valid.  
`DONE` | Deprecated: This state is no longer used.  
`EXPIRED` | Deprecated: This state is no longer used.  
  
## ExperimentConfig.VersionRelease.TrafficAllocation

Traffic allocation for the version release.

JSON representation  
---  
      
    
    {
      "id": string,
      "trafficPercentage": integer,
      "appVersion": string
    }  
  
Fields  
---  
`id` |  `string` Optional. Id of the traffic allocation. Free format string, up to 128 characters.  
`trafficPercentage` |  `integer` Optional. Traffic percentage of the traffic allocation. Must be between 0 and 100.  
`appVersion` |  `string` Optional. App version of the traffic allocation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
  
## WhatsAppCredentials

Ephemeral Meta credentials for WhatsApp native integration.

JSON representation  
---  
      
    
    {
      "authCode": string,
      "pin": string,
      "phoneNumber": string,
      "businessAccountId": string,
      "wabaId": string,
      "conversationProfileId": string
    }  
  
Fields  
---  
`authCode` |  `string` Required. The Meta auth code provided by the embedded signup flow.  
`pin` |  `string` Required. The 6-digit PIN created by the user for two-step verification.  
`phoneNumber` |  `string` Required. The phone number to register with WhatsApp.  
`businessAccountId` |  `string` Required. The Business Account ID to use for the phone number.  
`wabaId` |  `string` Required. The WhatsApp Business Account ID.  
`conversationProfileId` |  `string` Optional. The Conversation Profile ID to use for the deployment.  
  
## InstagramCredentials

Ephemeral Meta credentials for Instagram native integration.

JSON representation  
---  
      
    
    {
      "authCode": string,
      "conversationProfileId": string
    }  
  
Fields  
---  
`authCode` |  `string` Required. The Meta auth code provided by the embedded signup flow.  
`conversationProfileId` |  `string` Optional. The Conversation Profile ID to use for the deployment.  
  
## Deployment.Modality

The modality of the deployment.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`MODALITY_TEXT` | Text modality.  
`MODALITY_VOICE` | Voice modality.  
`MODALITY_VIDEO` | Video modality.  
  
## AgentRegistryDeployment

Configuration and status for Agent Registry deployment.

JSON representation  
---  
      
    
    {
      "agentRegistryServiceName": string
    }  
  
Fields  
---  
`agentRegistryServiceName` |  `string` Optional. Output only. The resource name of the deployed Agent Registry service. Format: `projects/{project}/locations/{location}/services/{service}`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments/create)`

|  Creates a new deployment in the given app.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments/delete)`

|  Deletes the specified deployment.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments/get)`

|  Gets details of the specified deployment.  
  
### `[getExtendedAgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments/getExtendedAgentCard)`

|  Gets the extended agent card for the authenticated agent.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments/list)`

|  Lists deployments in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.deployments/patch)`

|  Updates the specified deployment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
