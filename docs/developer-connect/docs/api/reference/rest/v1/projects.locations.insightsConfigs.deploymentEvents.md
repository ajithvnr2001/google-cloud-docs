---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents
title: REST Resource: projects.locations.insightsConfigs.deploymentEvents \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:12:05.262240+00:00
---

# REST Resource: projects.locations.insightsConfigs.deploymentEvents  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.insightsConfigs.deploymentEvents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DeploymentEvent
    * JSON representation
  * State
  * ArtifactDeployment
    * JSON representation
  * Methods



## Resource: DeploymentEvent

The DeploymentEvent resource represents the deployment of the artifact within the InsightsConfig resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "runtimeConfig": {
        object ([RuntimeConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig))
      },
      "runtimeDeploymentUri": string,
      "state": enum ([State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents#State)),
      "artifactDeployments": [
        {
          object ([ArtifactDeployment](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents#ArtifactDeployment))
        }
      ],
      "deployTime": string,
      "undeployTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the DeploymentEvent. This name is provided by Developer Connect insights. Format: projects/{project}/locations/{location}/insightsConfigs/{insightsConfig}/deploymentEvents/{uuid}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of the DeploymentEvent.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The update time of the DeploymentEvent.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`runtimeConfig` |  `object (`[RuntimeConfig](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/RuntimeConfig)`)` Output only. The runtime configurations where the DeploymentEvent happened.  
`runtimeDeploymentUri` |  `string` Output only. The runtime assigned URI of the DeploymentEvent. For GKE, this is the fully qualified replica set uri. e.g. container.googleapis.com/projects/{project}/locations/{location}/clusters/{cluster}/k8s/namespaces/{namespace}/apps/replicasets/{replica-set-id} For Cloud Run, this is the revision name.  
`state` |  `enum (`[State](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents#State)`)` Output only. The state of the DeploymentEvent.  
`artifactDeployments[]` |  `object (`[ArtifactDeployment](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents#ArtifactDeployment)`)` Output only. The artifact deployments of the DeploymentEvent. Each artifact deployment contains the artifact uri and the runtime configuration uri. For GKE, this would be all the containers images that are deployed in the pod.  
`deployTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the DeploymentEvent was deployed. This would be the min of all ArtifactDeployment deploy_times.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`undeployTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the DeploymentEvent was undeployed, all artifacts are considered undeployed once this time is set. This would be the max of all ArtifactDeployment undeploy_times. If any ArtifactDeployment is still active (i.e. does not have an undeployTime), this field will be empty.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

The state of the DeploymentEvent.

Enums  
---  
`STATE_UNSPECIFIED` | No state specified.  
`STATE_ACTIVE` | The deployment is active in the runtime.  
`STATE_INACTIVE` | The deployment is not in the runtime.  
  
## ArtifactDeployment

The ArtifactDeployment resource represents the deployment of the artifact within the InsightsConfig resource.

JSON representation  
---  
      
    
    {
      "id": string,
      "artifactReference": string,
      "artifactAlias": string,
      "sourceCommitUris": [
        string
      ],
      "deployTime": string,
      "undeployTime": string,
      "containerStatusSummary": string
    }  
  
Fields  
---  
`id` |  `string` Output only. Unique identifier of `ArtifactDeployment`.  
`artifactReference` |  `string` Output only. The artifact that is deployed.  
`artifactAlias` |  `string` Output only. The artifact alias in the deployment spec, with Tag/SHA. e.g. us-docker.pkg.dev/my-project/my-repo/image:1.0.0  
`sourceCommitUris[]` |  `string` Output only. The source commits at which this artifact was built. Extracted from provenance.  
`deployTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the deployment was deployed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`undeployTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the deployment was undeployed, all artifacts are considered undeployed once this time is set.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`containerStatusSummary` |  `string` Output only. The summary of container status of the artifact deployment. Format as `ContainerStatusState-Reason : restartCount` e.g. "Waiting-ImagePullBackOff : 3"  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents/get)`

|  Gets a single Deployment Event.  
  
### `[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.insightsConfigs.deploymentEvents/list)`

|  Lists Deployment Events in a given insights config.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-18 UTC."],[],[]] 
