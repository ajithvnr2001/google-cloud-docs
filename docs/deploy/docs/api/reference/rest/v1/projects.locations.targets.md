---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets
title: REST Resource: projects.locations.targets \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:02.201134+00:00
---

# REST Resource: projects.locations.targets  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.targets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Target
    * JSON representation
    * GkeCluster
      * JSON representation
    * AnthosCluster
      * JSON representation
    * CloudRunLocation
      * JSON representation
    * MultiTarget
      * JSON representation
    * CustomTarget
      * JSON representation
    * AssociatedEntities
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

A `Target` resource in the Cloud Deploy API.

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
      "associatedEntities": {
        string: {
          object ([AssociatedEntities](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.AssociatedEntities))
        },
        ...
      },
      "etag": string,
      "executionConfigs": [
        {
          object ([ExecutionConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.ExecutionConfig))
        }
      ],
      "deployParameters": {
        string: string,
        ...
      },
    
      // Union field deployment_target can be only one of the following:
      "gke": {
        object ([GkeCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.GkeCluster))
      },
      "anthosCluster": {
        object ([AnthosCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.AnthosCluster))
      },
      "run": {
        object ([CloudRunLocation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.CloudRunLocation))
      },
      "multiTarget": {
        object ([MultiTarget](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.MultiTarget))
      },
      "customTarget": {
        object ([CustomTarget](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.CustomTarget))
      }
      // End of list of possible types for union field deployment_target.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the `Target`. Format is `projects/{project}/locations/{location}/targets/{target}`. The `target` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`  
`targetId` |  `string` Output only. Resource id of the `Target`.  
`uid` |  `string` Output only. Unique identifier of the `Target`.  
`description` |  `string` Optional. Description of the `Target`. Max length is 255 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`requireApproval` |  `boolean` Optional. Whether or not the `Target` requires approval.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `Target` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Most recent time at which the `Target` was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`associatedEntities` |  `map (key: string, value: object (`[AssociatedEntities](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.AssociatedEntities)`))` Optional. Map of entity IDs to their associated entities. Associated entities allows specifying places other than the deployment target for specific features. For example, the Gateway API canary can be configured to deploy the HTTPRoute to a different cluster(s) than the deployment cluster using associated entities. An entity ID must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`executionConfigs[]` |  `object (`[ExecutionConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.ExecutionConfig)`)` Optional. Configurations for all execution that relates to this `Target`. Each `ExecutionEnvironmentUsage` value may only be used in a single configuration; using the same value multiple times is an error. When one or more configurations are specified, they must include the `RENDER` and `DEPLOY` `ExecutionEnvironmentUsage` values. When no configurations are specified, execution will use the default specified in `DefaultPool`.  
`deployParameters` |  `map (key: string, value: string)` Optional. The deploy parameters to use for this target.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `deployment_target`. Destination to which the Skaffold configuration is applied during a rollout. `deployment_target` can be only one of the following:  
`gke` |  `object (`[GkeCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.GkeCluster)`)` Optional. Information specifying a GKE Cluster.  
`anthosCluster` |  `object (`[AnthosCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.AnthosCluster)`)` Optional. Information specifying an Anthos Cluster.  
`run` |  `object (`[CloudRunLocation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.CloudRunLocation)`)` Optional. Information specifying a Cloud Run deployment target.  
`multiTarget` |  `object (`[MultiTarget](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.MultiTarget)`)` Optional. Information specifying a multiTarget.  
`customTarget` |  `object (`[CustomTarget](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.CustomTarget)`)` Optional. Information specifying a Custom Target.  
  
### GkeCluster

Information specifying a GKE Cluster.

JSON representation  
---  
      
    
    {
      "cluster": string,
      "internalIp": boolean,
      "proxyUrl": string,
      "dnsEndpoint": boolean
    }  
  
Fields  
---  
`cluster` |  `string` Optional. Information specifying a GKE Cluster. Format is `projects/{projectId}/locations/{locationId}/clusters/{cluster_id}`.  
`internalIp` |  `boolean` Optional. If true, `cluster` is accessed using the private IP address of the control plane endpoint. Otherwise, the default IP address of the control plane endpoint is used. The default IP address is the private IP address for clusters with private control-plane endpoints and the public IP address otherwise.Only specify this option when `cluster` is a [private GKE cluster](https://cloud.google.com/kubernetes-engine/docs/concepts/private-cluster-concept). Note that `internalIp` and `dnsEndpoint` cannot both be set to true.  
`proxyUrl` |  `string` Optional. If set, used to configure a [proxy](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/#proxy) to the Kubernetes server.  
`dnsEndpoint` |  `boolean` Optional. If set, the cluster will be accessed using the DNS endpoint. Note that both `dnsEndpoint` and `internalIp` cannot be set to true.  
  
### AnthosCluster

Information specifying an Anthos Cluster.

JSON representation  
---  
      
    
    {
      "membership": string
    }  
  
Fields  
---  
`membership` |  `string` Optional. Membership of the GKE Hub-registered cluster to which to apply the Skaffold configuration. Format is `projects/{project}/locations/{location}/memberships/{membership_name}`.  
  
### CloudRunLocation

Information specifying where to deploy a Cloud Run Service.

JSON representation  
---  
      
    
    {
      "location": string
    }  
  
Fields  
---  
`location` |  `string` Required. The location for the Cloud Run Service. Format must be `projects/{project}/locations/{location}`.  
  
### MultiTarget

Information specifying a multiTarget.

JSON representation  
---  
      
    
    {
      "targetIds": [
        string
      ]
    }  
  
Fields  
---  
`targetIds[]` |  `string` Required. The targetIds of this multiTarget.  
  
### CustomTarget

Information specifying a Custom Target.

JSON representation  
---  
      
    
    {
      "customTargetType": string
    }  
  
Fields  
---  
`customTargetType` |  `string` Required. The name of the CustomTargetType. Format must be `projects/{project}/locations/{location}/customTargetTypes/{customTargetType}`.  
  
### AssociatedEntities

Information about entities associated with a `Target`.

JSON representation  
---  
      
    
    {
      "gkeClusters": [
        {
          object ([GkeCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.GkeCluster))
        }
      ],
      "anthosClusters": [
        {
          object ([AnthosCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.AnthosCluster))
        }
      ]
    }  
  
Fields  
---  
`gkeClusters[]` |  `object (`[GkeCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.GkeCluster)`)` Optional. Information specifying GKE clusters as associated entities.  
`anthosClusters[]` |  `object (`[AnthosCluster](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.AnthosCluster)`)` Optional. Information specifying Anthos clusters as associated entities.  
  
### ExecutionConfig

Configuration of the environment to use when calling Skaffold.

JSON representation  
---  
      
    
    {
      "usages": [
        enum ([ExecutionEnvironmentUsage](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.ExecutionEnvironmentUsage))
      ],
      "workerPool": string,
      "serviceAccount": string,
      "artifactStorage": string,
      "executionTimeout": string,
      "verbose": boolean,
    
      // Union field execution_environment can be only one of the following:
      "defaultPool": {
        object ([DefaultPool](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.DefaultPool))
      },
      "privatePool": {
        object ([PrivatePool](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.PrivatePool))
      }
      // End of list of possible types for union field execution_environment.
    }  
  
Fields  
---  
`usages[]` |  `enum (`[ExecutionEnvironmentUsage](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.ExecutionEnvironmentUsage)`)` Required. Usages when this configuration should be applied.  
`workerPool` |  `string` Optional. The resource name of the `WorkerPool`, with the format `projects/{project}/locations/{location}/workerPools/{workerPool}`. If this optional field is unspecified, the default Cloud Build pool will be used.  
`serviceAccount` |  `string` Optional. Google service account to use for execution. If unspecified, the project execution service account ([-compute@developer.gserviceaccount.com](mailto:-compute@developer.gserviceaccount.com)) is used.  
`artifactStorage` |  `string` Optional. Cloud Storage location in which to store execution outputs. This can either be a bucket ("gs://my-bucket") or a path within a bucket ("gs://my-bucket/my-dir"). If unspecified, a default bucket located in the same region will be used.  
`executionTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Execution timeout for a Cloud Build Execution. This must be between 10m and 24h in seconds format. If unspecified, a default timeout of 1h is used.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`verbose` |  `boolean` Optional. If true, additional logging will be enabled when running builds in this execution environment.  
Union field `execution_environment`. Details of the environment. `execution_environment` can be only one of the following:  
`defaultPool` |  `object (`[DefaultPool](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.DefaultPool)`)` Optional. Use default Cloud Build pool.  
`privatePool` |  `object (`[PrivatePool](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target.PrivatePool)`)` Optional. Use private Cloud Build pool.  
  
### ExecutionEnvironmentUsage

Possible usages of this configuration.

Enums  
---  
`EXECUTION_ENVIRONMENT_USAGE_UNSPECIFIED` | Default value. This value is unused.  
`RENDER` | Use for rendering.  
`DEPLOY` | Use for deploying and deployment hooks.  
`VERIFY` | Use for deployment verification.  
`PREDEPLOY` | Use for predeploy job execution.  
`POSTDEPLOY` | Use for postdeploy job execution.  
`ANALYSIS` | Use for analysis job execution.  
  
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
  
### `[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/create)`

|  Creates a new Target in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/delete)`

|  Deletes a single Target.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/get)`

|  Gets details of a single Target.  
  
### `[getIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/list)`

|  Lists Targets in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/patch)`

|  Updates the parameters of a single Target.  
  
### `[setIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
