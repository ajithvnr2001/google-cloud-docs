---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets
title: REST Resource: projects.locations.deliveryPipelines.targets \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:39:06.158685+00:00
---

# REST Resource: projects.locations.deliveryPipelines.targets  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)



Send feedback 

#  REST Resource: projects.locations.deliveryPipelines.targets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Target
    * JSON representation
    * GKECluster
      * JSON representation
    * GkeCluster
      * JSON representation
    * ExecutionConfig
      * JSON representation
    * ExecutionEnvironmentUsage
    * DefaultPool
      * JSON representation
    * PrivatePool
      * JSON representation
  * Methods



## Resource: Target

A `Target` resource in the Google Cloud Deploy API.

A `Target` defines a location to which a Skaffold configuration can be deployed.

JSON representation  
---  
      
    
    {
      "name": string,
      "targetId": string,
      "uid": string,
      "description": string,
      "annotations": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      },
      "requireApproval": boolean,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "executionConfigs": [
        {
          object ([ExecutionConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.ExecutionConfig))
        }
      ],
    
      // Union field deployment_target can be only one of the following:
      "gkeCluster": {
        object ([GKECluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.GKECluster))
      },
      "cluster": {
        object ([GkeCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.GkeCluster))
      },
      "gke": {
        object ([GkeCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.GkeCluster))
      }
      // End of list of possible types for union field deployment_target.
    }  
  
Fields  
---  
`name` |  `string` Optional. Name of the `Target`. Format is projects/{project}/locations/{location}/ deliveryPipelines/{deliveryPipeline}/targets/[a-z][a-z0-9-]{0,62}.  
`targetId` |  `string` Output only. Resource id of the `Target`.  
`uid` |  `string` Output only. Unique identifier of the `Target`.  
`description` |  `string` Optional. Description of the `Target`. Max length is 255 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user, and not by Google Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are attributes that can be set and used by both the user and by Google Cloud Deploy. Labels must meet the following constraints: Each resource is limited to 64 labels. Keys must conform to the regexp: [a-zA-Z][a-zA-Z0-9_-]{0,62} Values must conform to the regexp: [a-zA-Z0-9_-]{0,63} Both keys and values are additionally constrained to be <= 128 bytes in size.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`requireApproval` |  `boolean` Optional. Whether or not the `Target` requires approval.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Time at which the `Target` was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Most recent time at which the `Target` was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`etag` |  `string` Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`executionConfigs[]` |  `object (`[ExecutionConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.ExecutionConfig)`)` Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`.  
Union field `deployment_target`. Destination to which the Skaffold configuration is applied during a rollout. `deployment_target` can be only one of the following:  
`gkeCluster` |  `object (`[GKECluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.GKECluster)`)` Information specifying a GKE Cluster.  
`cluster` |  `object (`[GkeCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.GkeCluster)`)` Information specifying a GKE Cluster.  
`gke` |  `object (`[GkeCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.GkeCluster)`)` Information specifying a GKE Cluster.  
  
### GKECluster

Information specifying a GKE Cluster.

JSON representation  
---  
      
    
    {
      "project": string,
      "cluster": string,
      "location": string
    }  
  
Fields  
---  
`project` |  `string` Project in which the cluster is located.  
`cluster` |  `string` Name of the cluster.  
`location` |  `string` Location of the cluster.  
  
### GkeCluster

Information specifying a GKE Cluster.

JSON representation  
---  
      
    
    {
      "cluster": string
    }  
  
Fields  
---  
`cluster` |  `string` Information specifying a GKE Cluster. Format is `projects/{projectId}/locations/{locationId}/clusters/{cluster_id}.  
  
### ExecutionConfig

Configuration of the environment to use when calling Skaffold.

JSON representation  
---  
      
    
    {
      "usages": [
        enum ([ExecutionEnvironmentUsage](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.ExecutionEnvironmentUsage))
      ],
    
      // Union field execution_environment can be only one of the following:
      "defaultPool": {
        object ([DefaultPool](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.DefaultPool))
      },
      "privatePool": {
        object ([PrivatePool](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.PrivatePool))
      }
      // End of list of possible types for union field execution_environment.
    }  
  
Fields  
---  
`usages[]` |  `enum (`[ExecutionEnvironmentUsage](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.ExecutionEnvironmentUsage)`)` Required. Usages when this configuration should be applied.  
Union field `execution_environment`. Details of the environment. `execution_environment` can be only one of the following:  
`defaultPool` |  `object (`[DefaultPool](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.DefaultPool)`)` Optional. Use default Cloud Build pool.  
`privatePool` |  `object (`[PrivatePool](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets#Target.PrivatePool)`)` Optional. Use private Cloud Build pool.  
  
### ExecutionEnvironmentUsage

Possible usages of this configuration.

Enums  
---  
`EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED` | Default value. This value is unused.  
`RENDER` | Use for rendering.  
`DEPLOY` | Use for deploying and deployment hooks.  
  
### DefaultPool

Execution using the default Cloud Build pool.

JSON representation  
---  
      
    
    {
      "serviceAccount": string,
      "artifactStorage": string
    }  
  
Fields  
---  
`serviceAccount` |  `string` Optional. Google service account to use for execution. If unspecified, the project execution service account ([-compute@developer.gserviceaccount.com](mailto:-compute@developer.gserviceaccount.com)) will be used.  
`artifactStorage` |  `string` Optional. Cloud Storage location where execution outputs should be stored. This can either be a bucket ("gs://my-bucket") or a path within a bucket ("gs://my-bucket/my-dir"). If unspecified, a default bucket located in the same region will be used.  
  
### PrivatePool

Execution using a private Cloud Build pool.

JSON representation  
---  
      
    
    {
      "workerPool": string,
      "serviceAccount": string,
      "artifactStorage": string
    }  
  
Fields  
---  
`workerPool` |  `string` Required. Resource name of the Cloud Build worker pool to use. The format is `projects/{project}/locations/{location}/workerPools/{pool}`.  
`serviceAccount` |  `string` Optional. Google service account to use for execution. If unspecified, the project execution service account ([-compute@developer.gserviceaccount.com](mailto:-compute@developer.gserviceaccount.com)) will be used.  
`artifactStorage` |  `string` Optional. Cloud Storage location where execution outputs should be stored. This can either be a bucket ("gs://my-bucket") or a path within a bucket ("gs://my-bucket/my-dir"). If unspecified, a default bucket located in the same region will be used.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets/create)`

|  Creates a new Target in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets/delete)`

|  Deletes a single shared Target.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets/get)`

|  Gets details of a single shared Target.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets/list)`

|  Lists Targets in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.targets/patch)`

|  Updates the parameters of a shared single Target.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
