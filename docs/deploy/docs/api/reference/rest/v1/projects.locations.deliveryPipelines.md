---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines
title: REST Resource: projects.locations.deliveryPipelines \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:56.464055+00:00
---

# REST Resource: projects.locations.deliveryPipelines  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.deliveryPipelines Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DeliveryPipeline
    * JSON representation
    * SerialPipeline
      * JSON representation
    * Stage
      * JSON representation
    * Strategy
      * JSON representation
    * Standard
      * JSON representation
    * Verify
      * JSON representation
    * Predeploy
      * JSON representation
    * Postdeploy
      * JSON representation
    * Analysis
      * JSON representation
    * Canary
      * JSON representation
    * RuntimeConfig
      * JSON representation
    * KubernetesConfig
      * JSON representation
    * GatewayServiceMesh
      * JSON representation
    * RouteDestinations
      * JSON representation
    * ServiceNetworking
      * JSON representation
    * CloudRunConfig
      * JSON representation
    * CanaryDeployment
      * JSON representation
    * CustomCanaryDeployment
      * JSON representation
    * PhaseConfig
      * JSON representation
    * DeployParameters
      * JSON representation
    * PipelineCondition
      * JSON representation
    * PipelineReadyCondition
      * JSON representation
    * TargetsTypeCondition
      * JSON representation
  * Methods



## Resource: DeliveryPipeline

A `DeliveryPipeline` resource in the Cloud Deploy API.

A `DeliveryPipeline` defines a pipeline through which a Skaffold configuration can progress.

JSON representation  
---  
      
    
    {
      "name": string,
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
      "createTime": string,
      "updateTime": string,
      "condition": {
        object ([PipelineCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.PipelineCondition))
      },
      "etag": string,
      "suspended": boolean,
    
      // Union field pipeline can be only one of the following:
      "serialPipeline": {
        object ([SerialPipeline](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.SerialPipeline))
      }
      // End of list of possible types for union field pipeline.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the `DeliveryPipeline`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}`. The `deliveryPipeline` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`  
`uid` |  `string` Output only. Unique identifier of the `DeliveryPipeline`.  
`description` |  `string` Optional. Description of the `DeliveryPipeline`. Max length is 255 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the pipeline was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Most recent time at which the pipeline was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`condition` |  `object (`[PipelineCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.PipelineCondition)`)` Output only. Information around the state of the Delivery Pipeline.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`suspended` |  `boolean` Optional. When suspended, no new releases or rollouts can be created, but in-progress ones will complete.  
Union field `pipeline`. The ordering configuration of the `DeliveryPipeline`. `pipeline` can be only one of the following:  
`serialPipeline` |  `object (`[SerialPipeline](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.SerialPipeline)`)` Optional. SerialPipeline defines a sequential set of stages for a `DeliveryPipeline`.  
  
### SerialPipeline

SerialPipeline defines a sequential set of stages for a `DeliveryPipeline`.

JSON representation  
---  
      
    
    {
      "stages": [
        {
          object ([Stage](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Stage))
        }
      ]
    }  
  
Fields  
---  
`stages[]` |  `object (`[Stage](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Stage)`)` Optional. Each stage specifies configuration for a `Target`. The ordering of this list defines the promotion flow.  
  
### Stage

Stage specifies a location to which to deploy.

JSON representation  
---  
      
    
    {
      "targetId": string,
      "profiles": [
        string
      ],
      "strategy": {
        object ([Strategy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Strategy))
      },
      "deployParameters": [
        {
          object ([DeployParameters](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.DeployParameters))
        }
      ]
    }  
  
Fields  
---  
`targetId` |  `string` Optional. The targetId to which this stage points. This field refers exclusively to the last segment of a target name. For example, this field would just be `my-target` (rather than `projects/project/locations/location/targets/my-target`). The location of the `Target` is inferred to be the same as the location of the `DeliveryPipeline` that contains this `Stage`.  
`profiles[]` |  `string` Optional. Skaffold profiles to use when rendering the manifest for this stage's `Target`.  
`strategy` |  `object (`[Strategy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Strategy)`)` Optional. The strategy to use for a `Rollout` to this stage.  
`deployParameters[]` |  `object (`[DeployParameters](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.DeployParameters)`)` Optional. The deploy parameters to use for the target in this stage.  
  
### Strategy

Strategy contains deployment strategy information.

JSON representation  
---  
      
    
    {
    
      // Union field deployment_strategy can be only one of the following:
      "standard": {
        object ([Standard](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Standard))
      },
      "canary": {
        object ([Canary](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Canary))
      }
      // End of list of possible types for union field deployment_strategy.
    }  
  
Fields  
---  
Union field `deployment_strategy`. Deployment strategy details. `deployment_strategy` can be only one of the following:  
`standard` |  `object (`[Standard](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Standard)`)` Optional. Standard deployment strategy executes a single deploy and allows verifying the deployment.  
`canary` |  `object (`[Canary](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Canary)`)` Optional. Canary deployment strategy provides progressive percentage based deployments to a Target.  
  
### Standard

Standard represents the standard deployment strategy.

JSON representation  
---  
      
    
    {
      "verify": boolean,
      "verifyConfig": {
        object ([Verify](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Verify))
      },
      "predeploy": {
        object ([Predeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Predeploy))
      },
      "postdeploy": {
        object ([Postdeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Postdeploy))
      },
      "analysis": {
        object ([Analysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Analysis))
      }
    }  
  
Fields  
---  
`verify` |  `boolean` Optional. Whether to verify a deployment via `skaffold verify`.  
`verifyConfig` |  `object (`[Verify](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Verify)`)` Optional. Configuration for the verify job. Cannot be set if `verify` is set to true.  
`predeploy` |  `object (`[Predeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Predeploy)`)` Optional. Configuration for the predeploy job. If this is not configured, the predeploy job will not be present.  
`postdeploy` |  `object (`[Postdeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Postdeploy)`)` Optional. Configuration for the postdeploy job. If this is not configured, the postdeploy job will not be present.  
`analysis` |  `object (`[Analysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Analysis)`)` Optional. Configuration for the analysis job. If this is not configured, the analysis job will not be present.  
  
### Verify

Verify contains the verify job configuration information.

JSON representation  
---  
      
    
    {
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
        }
      ]
    }  
  
Fields  
---  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Optional. The tasks that will run as a part of the verify job. The tasks are executed sequentially in the order specified.  
  
### Predeploy

Predeploy contains the predeploy job configuration information.

JSON representation  
---  
      
    
    {
      "actions": [
        string
      ],
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
        }
      ]
    }  
  
Fields  
---  
`actions[]` |  `string` Optional. A sequence of Skaffold custom actions to invoke during execution of the predeploy job.  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Optional. The tasks that will run as a part of the predeploy job. The tasks are executed sequentially in the order specified. Only one of `actions` or `tasks` can be specified.  
  
### Postdeploy

Postdeploy contains the postdeploy job configuration information.

JSON representation  
---  
      
    
    {
      "actions": [
        string
      ],
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
        }
      ]
    }  
  
Fields  
---  
`actions[]` |  `string` Optional. A sequence of Skaffold custom actions to invoke during execution of the postdeploy job.  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Optional. The tasks that will run as a part of the postdeploy job. The tasks are executed sequentially in the order specified. Only one of `actions` or `tasks` can be specified.  
  
### Analysis

Analysis contains the configuration for the set of analyses to be performed on the target.

JSON representation  
---  
      
    
    {
      "duration": string,
      "googleCloud": {
        object ([GoogleCloudAnalysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/GoogleCloudAnalysis))
      },
      "customChecks": [
        {
          object ([CustomCheck](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomCheck))
        }
      ]
    }  
  
Fields  
---  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The amount of time in minutes the analysis on the target will last. If all analysis checks have successfully completed before the specified duration, the analysis is successful. If a check is still running while the specified duration passes, it will wait for that check to complete to determine if the analysis is successful. The maximum duration is 48 hours.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`googleCloud` |  `object (`[GoogleCloudAnalysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/GoogleCloudAnalysis)`)` Optional. Google Cloud - based analysis checks.  
`customChecks[]` |  `object (`[CustomCheck](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomCheck)`)` Optional. Custom analysis checks from 3P metric providers.  
  
### Canary

Canary represents the canary deployment strategy.

JSON representation  
---  
      
    
    {
      "runtimeConfig": {
        object ([RuntimeConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.RuntimeConfig))
      },
    
      // Union field mode can be only one of the following:
      "canaryDeployment": {
        object ([CanaryDeployment](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.CanaryDeployment))
      },
      "customCanaryDeployment": {
        object ([CustomCanaryDeployment](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.CustomCanaryDeployment))
      }
      // End of list of possible types for union field mode.
    }  
  
Fields  
---  
`runtimeConfig` |  `object (`[RuntimeConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.RuntimeConfig)`)` Optional. Runtime specific configurations for the deployment strategy. The runtime configuration is used to determine how Cloud Deploy will split traffic to enable a progressive deployment.  
Union field `mode`. The mode to use for the canary deployment strategy. `mode` can be only one of the following:  
`canaryDeployment` |  `object (`[CanaryDeployment](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.CanaryDeployment)`)` Optional. Configures the progressive based deployment for a Target.  
`customCanaryDeployment` |  `object (`[CustomCanaryDeployment](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.CustomCanaryDeployment)`)` Optional. Configures the progressive based deployment for a Target, but allows customizing at the phase level where a phase represents each of the percentage deployments.  
  
### RuntimeConfig

RuntimeConfig contains the runtime specific configurations for a deployment strategy.

JSON representation  
---  
      
    
    {
    
      // Union field runtime_config can be only one of the following:
      "kubernetes": {
        object ([KubernetesConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.KubernetesConfig))
      },
      "cloudRun": {
        object ([CloudRunConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.CloudRunConfig))
      }
      // End of list of possible types for union field runtime_config.
    }  
  
Fields  
---  
Union field `runtime_config`. The runtime configuration details. `runtime_config` can be only one of the following:  
`kubernetes` |  `object (`[KubernetesConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.KubernetesConfig)`)` Optional. Kubernetes runtime configuration.  
`cloudRun` |  `object (`[CloudRunConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.CloudRunConfig)`)` Optional. Cloud Run runtime configuration.  
  
### KubernetesConfig

KubernetesConfig contains the Kubernetes runtime configuration.

JSON representation  
---  
      
    
    {
    
      // Union field service_definition can be only one of the following:
      "gatewayServiceMesh": {
        object ([GatewayServiceMesh](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.GatewayServiceMesh))
      },
      "serviceNetworking": {
        object ([ServiceNetworking](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.ServiceNetworking))
      }
      // End of list of possible types for union field service_definition.
    }  
  
Fields  
---  
Union field `service_definition`. The service definition configuration. `service_definition` can be only one of the following:  
`gatewayServiceMesh` |  `object (`[GatewayServiceMesh](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.GatewayServiceMesh)`)` Optional. Kubernetes Gateway API service mesh configuration.  
`serviceNetworking` |  `object (`[ServiceNetworking](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.ServiceNetworking)`)` Optional. Kubernetes Service networking configuration.  
  
### GatewayServiceMesh

Information about the Kubernetes Gateway API service mesh configuration.

JSON representation  
---  
      
    
    {
      "httpRoute": string,
      "service": string,
      "deployment": string,
      "routeUpdateWaitTime": string,
      "stableCutbackDuration": string,
      "podSelectorLabel": string,
      "routeDestinations": {
        object ([RouteDestinations](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.RouteDestinations))
      }
    }  
  
Fields  
---  
`httpRoute` |  `string` Required. Name of the Gateway API HTTPRoute.  
`service` |  `string` Required. Name of the Kubernetes Service.  
`deployment` |  `string` Required. Name of the Kubernetes Deployment whose traffic is managed by the specified HTTPRoute and Service.  
`routeUpdateWaitTime` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The time to wait for route updates to propagate. The maximum configurable time is 3 hours, in seconds format. If unspecified, there is no wait time.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`stableCutbackDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The amount of time to migrate traffic back from the canary Service to the original Service during the stable phase deployment. If specified, must be between 15s and 3600s. If unspecified, there is no cutback time.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`podSelectorLabel` |  `string` Optional. The label to use when selecting Pods for the Deployment and Service resources. This label must already be present in both resources.  
`routeDestinations` |  `object (`[RouteDestinations](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.RouteDestinations)`)` Optional. Route destinations allow configuring the Gateway API HTTPRoute to be deployed to additional clusters. This option is available for multi-cluster service mesh set ups that require the route to exist in the clusters that call the service. If unspecified, the HTTPRoute will only be deployed to the Target cluster.  
  
### RouteDestinations

Information about route destinations for the Gateway API service mesh.

JSON representation  
---  
      
    
    {
      "destinationIds": [
        string
      ],
      "propagateService": boolean
    }  
  
Fields  
---  
`destinationIds[]` |  `string` Required. The clusters where the Gateway API HTTPRoute resource will be deployed to. Valid entries include the associated entities IDs configured in the Target resource and "@self" to include the Target cluster.  
`propagateService` |  `boolean` Optional. Whether to propagate the Kubernetes Service to the route destination clusters. The Service will always be deployed to the Target cluster even if the HTTPRoute is not. This option may be used to facilitate successful DNS lookup in the route destination clusters. Can only be set to true if destinations are specified.  
  
### ServiceNetworking

Information about the Kubernetes Service networking configuration.

JSON representation  
---  
      
    
    {
      "service": string,
      "deployment": string,
      "disablePodOverprovisioning": boolean,
      "podSelectorLabel": string
    }  
  
Fields  
---  
`service` |  `string` Required. Name of the Kubernetes Service.  
`deployment` |  `string` Required. Name of the Kubernetes Deployment whose traffic is managed by the specified Service.  
`disablePodOverprovisioning` |  `boolean` Optional. Whether to disable Pod overprovisioning. If Pod overprovisioning is disabled then Cloud Deploy will limit the number of total Pods used for the deployment strategy to the number of Pods the Deployment has on the cluster.  
`podSelectorLabel` |  `string` Optional. The label to use when selecting Pods for the Deployment resource. This label must already be present in the Deployment.  
  
### CloudRunConfig

CloudRunConfig contains the Cloud Run runtime configuration.

JSON representation  
---  
      
    
    {
      "automaticTrafficControl": boolean,
      "canaryRevisionTags": [
        string
      ],
      "priorRevisionTags": [
        string
      ],
      "stableRevisionTags": [
        string
      ]
    }  
  
Fields  
---  
`automaticTrafficControl` |  `boolean` Optional. Whether Cloud Deploy should update the traffic stanza in a Cloud Run Service on the user's behalf to facilitate traffic splitting. This is required to be true for CanaryDeployments, but optional for CustomCanaryDeployments.  
`canaryRevisionTags[]` |  `string` Optional. A list of tags that are added to the canary revision while the canary phase is in progress.  
`priorRevisionTags[]` |  `string` Optional. A list of tags that are added to the prior revision while the canary phase is in progress.  
`stableRevisionTags[]` |  `string` Optional. A list of tags that are added to the final stable revision when the stable phase is applied.  
  
### CanaryDeployment

CanaryDeployment represents the canary deployment configuration

JSON representation  
---  
      
    
    {
      "percentages": [
        integer
      ],
      "verify": boolean,
      "verifyConfig": {
        object ([Verify](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Verify))
      },
      "predeploy": {
        object ([Predeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Predeploy))
      },
      "postdeploy": {
        object ([Postdeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Postdeploy))
      },
      "analysis": {
        object ([Analysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Analysis))
      }
    }  
  
Fields  
---  
`percentages[]` |  `integer` Required. The percentage based deployments that will occur as a part of a `Rollout`. List is expected in ascending order and each integer n is 0 <= n < 100\. If the GatewayServiceMesh is configured for Kubernetes, then the range for n is 0 <= n <= 100.  
`verify` |  `boolean` Optional. Whether to run verify tests after each percentage deployment via `skaffold verify`.  
`verifyConfig` |  `object (`[Verify](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Verify)`)` Optional. Configuration for the verify job. Cannot be set if `verify` is set to true.  
`predeploy` |  `object (`[Predeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Predeploy)`)` Optional. Configuration for the predeploy job of the first phase. If this is not configured, there will be no predeploy job for this phase.  
`postdeploy` |  `object (`[Postdeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Postdeploy)`)` Optional. Configuration for the postdeploy job of the last phase. If this is not configured, there will be no postdeploy job for this phase.  
`analysis` |  `object (`[Analysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Analysis)`)` Optional. Configuration for the analysis job. If configured, the analysis will run after each percentage deployment.  
  
### CustomCanaryDeployment

CustomCanaryDeployment represents the custom canary deployment configuration.

JSON representation  
---  
      
    
    {
      "phaseConfigs": [
        {
          object ([PhaseConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.PhaseConfig))
        }
      ]
    }  
  
Fields  
---  
`phaseConfigs[]` |  `object (`[PhaseConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.PhaseConfig)`)` Required. Configuration for each phase in the canary deployment in the order executed.  
  
### PhaseConfig

PhaseConfig represents the configuration for a phase in the custom canary deployment.

JSON representation  
---  
      
    
    {
      "phaseId": string,
      "percentage": integer,
      "profiles": [
        string
      ],
      "verify": boolean,
      "verifyConfig": {
        object ([Verify](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Verify))
      },
      "predeploy": {
        object ([Predeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Predeploy))
      },
      "postdeploy": {
        object ([Postdeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Postdeploy))
      },
      "analysis": {
        object ([Analysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Analysis))
      }
    }  
  
Fields  
---  
`phaseId` |  `string` Required. The ID to assign to the `Rollout` phase. This value must consist of lower-case letters, numbers, and hyphens, start with a letter and end with a letter or a number, and have a max length of 63 characters. In other words, it must match the following regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`.  
`percentage` |  `integer` Required. Percentage deployment for the phase.  
`profiles[]` |  `string` Optional. Skaffold profiles to use when rendering the manifest for this phase. These are in addition to the profiles list specified in the `DeliveryPipeline` stage.  
`verify` |  `boolean` Optional. Whether to run verify tests after the deployment via `skaffold verify`.  
`verifyConfig` |  `object (`[Verify](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Verify)`)` Optional. Configuration for the verify job. Cannot be set if `verify` is set to true.  
`predeploy` |  `object (`[Predeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Predeploy)`)` Optional. Configuration for the predeploy job of this phase. If this is not configured, there will be no predeploy job for this phase.  
`postdeploy` |  `object (`[Postdeploy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Postdeploy)`)` Optional. Configuration for the postdeploy job of this phase. If this is not configured, there will be no postdeploy job for this phase.  
`analysis` |  `object (`[Analysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.Analysis)`)` Optional. Configuration for the analysis job of this phase. If this is not configured, there will be no analysis job for this phase.  
  
### DeployParameters

DeployParameters contains deploy parameters information.

JSON representation  
---  
      
    
    {
      "values": {
        string: string,
        ...
      },
      "matchTargetLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`values` |  `map (key: string, value: string)` Required. Values are deploy parameters in key-value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`matchTargetLabels` |  `map (key: string, value: string)` Optional. Deploy parameters are applied to targets with match labels. If unspecified, deploy parameters are applied to all targets (including child targets of a multi-target).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### PipelineCondition

PipelineCondition contains all conditions relevant to a Delivery Pipeline.

JSON representation  
---  
      
    
    {
      "pipelineReadyCondition": {
        object ([PipelineReadyCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.PipelineReadyCondition))
      },
      "targetsPresentCondition": {
        object ([TargetsPresentCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/TargetsPresentCondition))
      },
      "targetsTypeCondition": {
        object ([TargetsTypeCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.TargetsTypeCondition))
      }
    }  
  
Fields  
---  
`pipelineReadyCondition` |  `object (`[PipelineReadyCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.PipelineReadyCondition)`)` Details around the Pipeline's overall status.  
`targetsPresentCondition` |  `object (`[TargetsPresentCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/TargetsPresentCondition)`)` Details around targets enumerated in the pipeline.  
`targetsTypeCondition` |  `object (`[TargetsTypeCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline.TargetsTypeCondition)`)` Details on the whether the targets enumerated in the pipeline are of the same type.  
  
### PipelineReadyCondition

PipelineReadyCondition contains information around the status of the Pipeline.

JSON representation  
---  
      
    
    {
      "status": boolean,
      "updateTime": string
    }  
  
Fields  
---  
`status` |  `boolean` True if the Pipeline is in a valid state. Otherwise at least one condition in `PipelineCondition` is in an invalid state. Iterate over those conditions and see which condition(s) has status = false to find out what is wrong with the Pipeline.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time the condition was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### TargetsTypeCondition

TargetsTypeCondition contains information on whether the Targets defined in the Delivery Pipeline are of the same type.

JSON representation  
---  
      
    
    {
      "status": boolean,
      "errorDetails": string
    }  
  
Fields  
---  
`status` |  `boolean` True if the targets are all a comparable type. For example this is true if all targets are GKE clusters. This is false if some targets are Cloud Run targets and others are GKE clusters.  
`errorDetails` |  `string` Human readable error message.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/create)`

|  Creates a new DeliveryPipeline in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/delete)`

|  Deletes a single DeliveryPipeline.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/get)`

|  Gets details of a single DeliveryPipeline.  
  
### `[getIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/list)`

|  Lists DeliveryPipelines in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/patch)`

|  Updates the parameters of a single DeliveryPipeline.  
  
### `[rollbackTarget](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/rollbackTarget)`

|  Creates a `Rollout` to roll back the specified target.  
  
### `[setIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
