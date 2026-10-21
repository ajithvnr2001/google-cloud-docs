---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs
title: REST Resource: projects.locations.insightsConfigs \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:42:46.678418+00:00
---

# REST Resource: projects.locations.insightsConfigs  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.insightsConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: InsightsConfig
    * JSON representation
  * Projects
    * JSON representation
  * ArtifactConfig
    * JSON representation
  * GoogleArtifactRegistry
    * JSON representation
  * GoogleArtifactAnalysis
    * JSON representation
  * State
  * Methods



## Resource: InsightsConfig

The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "runtimeConfigs": [
        {
          object ([RuntimeConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig))
        }
      ],
      "artifactConfigs": [
        {
          object ([ArtifactConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#ArtifactConfig))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#State)),
      "annotations": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      },
      "reconciling": boolean,
      "errors": [
        {
          object ([Status](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/Status))
        }
      ],
    
      // Union field insights_config_context can be only one of the following:
      "appHubApplication": string,
      "projects": {
        object ([Projects](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#Projects))
      }
      // End of list of possible types for union field insights_config_context.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the InsightsConfig. Format: projects/{project}/locations/{location}/insightsConfigs/{insightsConfig}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`runtimeConfigs[]` |  `object (`[RuntimeConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig)`)` Output only. The runtime configurations where the application is deployed.  
`artifactConfigs[]` |  `object (`[ArtifactConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#ArtifactConfig)`)` Optional. The artifact configurations of the artifacts that are deployed.  
`state` |  `enum (`[State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#State)`)` Optional. Output only. The state of the InsightsConfig.  
`annotations` |  `map (key: string, value: string)` Optional. User specified annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Set of labels associated with an InsightsConfig.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`reconciling` |  `boolean` Output only. Reconciling (<https://google.aip.dev/128#reconciliation)>. Set to true if the current state of InsightsConfig does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.  
`errors[]` |  `object (`[Status](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/Status)`)` Output only. Any errors that occurred while setting up the InsightsConfig. Each error will be in the format: `field_name: errorMessage`, e.g. GetAppHubApplication: Permission denied while getting App Hub application. Please grant permissions to the P4SA.  
Union field `insights_config_context`. The context of the InsightsConfig. `insights_config_context` can be only one of the following:  
`appHubApplication` |  `string` Optional. The name of the App Hub Application. Format: projects/{project}/locations/{location}/applications/{application}  
`projects` |  `object (`[Projects](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#Projects)`)` Optional. The projects to track with the InsightsConfig.  
  
## Projects

Projects represents the projects to track with the InsightsConfig.

JSON representation  
---  
      
    
    {
      "projectIds": [
        string
      ]
    }  
  
Fields  
---  
`projectIds[]` |  `string` Optional. The project IDs. Format: {project}  
  
## ArtifactConfig

The artifact config of the artifact that is deployed.

JSON representation  
---  
      
    
    {
      "uri": string,
    
      // Union field artifact_storage can be only one of the following:
      "googleArtifactRegistry": {
        object ([GoogleArtifactRegistry](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#GoogleArtifactRegistry))
      }
      // End of list of possible types for union field artifact_storage.
    
      // Union field artifact_metadata_storage can be only one of the following:
      "googleArtifactAnalysis": {
        object ([GoogleArtifactAnalysis](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#GoogleArtifactAnalysis))
      }
      // End of list of possible types for union field artifact_metadata_storage.
    }  
  
Fields  
---  
`uri` |  `string` Required. Immutable. The URI of the artifact that is deployed. e.g. `us-docker.pkg.dev/my-project/my-repo/image`. The URI does not include the tag / digest because it captures a lineage of artifacts.  
Union field `artifact_storage`. The storage location of the artifact. `artifact_storage` can be only one of the following:  
`googleArtifactRegistry` |  `object (`[GoogleArtifactRegistry](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#GoogleArtifactRegistry)`)` Optional. Set if the artifact is stored in Artifact registry.  
Union field `artifact_metadata_storage`. The storage location of the artifact metadata. `artifact_metadata_storage` can be only one of the following:  
`googleArtifactAnalysis` |  `object (`[GoogleArtifactAnalysis](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs#GoogleArtifactAnalysis)`)` Optional. Set if the artifact metadata is stored in Artifact analysis.  
  
## GoogleArtifactRegistry

Google Artifact Registry configurations.

JSON representation  
---  
      
    
    {
      "projectId": string,
      "artifactRegistryPackage": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. The host project of Artifact Registry.  
`artifactRegistryPackage` |  `string` Required. Immutable. The name of the artifact registry package.  
  
## GoogleArtifactAnalysis

Google Artifact Analysis configurations.

JSON representation  
---  
      
    
    {
      "projectId": string
    }  
  
Fields  
---  
`projectId` |  `string` Required. The project id of the project where the provenance is stored.  
  
## State

The state of the InsightsConfig.

Enums  
---  
`STATE_UNSPECIFIED` | No state specified.  
`PENDING` | The InsightsConfig is pending application discovery/runtime discovery.  
`COMPLETE` | The initial discovery process is complete.  
`ERROR` | The InsightsConfig is in an error state.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/create)`

|  Creates a new InsightsConfig in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/delete)`

|  Deletes a single Insight.  
  
### `[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/get)`

|  Gets details of a single Insight.  
  
### `[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/list)`

|  Lists InsightsConfigs in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs/patch)`

|  Updates the parameters of a single InsightsConfig.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-18 UTC."],[],[]] 
