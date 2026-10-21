---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases
title: REST Resource: projects.locations.deliveryPipelines.releases \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:24.110159+00:00
---

# REST Resource: projects.locations.deliveryPipelines.releases  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.deliveryPipelines.releases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Release
    * JSON representation
  * BuildArtifact
    * JSON representation
  * RenderState
  * TargetArtifact
    * JSON representation
  * PhaseArtifact
    * JSON representation
  * TargetRender
    * JSON representation
  * TargetRenderState
  * RenderMetadata
    * JSON representation
  * CloudRunRenderMetadata
    * JSON representation
  * KubernetesRenderMetadata
    * JSON representation
  * FailureCause
  * ReleaseCondition
    * JSON representation
  * ReleaseReadyCondition
    * JSON representation
  * SkaffoldSupportedCondition
    * JSON representation
  * SkaffoldSupportState
  * ToolVersionSupportedCondition
    * JSON representation
  * ToolVersionSupportState
  * ToolVersions
    * JSON representation
  * Methods



## Resource: Release

A `Release` resource in the Cloud Deploy API.

A `Release` defines a specific Skaffold configuration instance that can be deployed.

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
      "abandoned": boolean,
      "createTime": string,
      "renderStartTime": string,
      "renderEndTime": string,
      "skaffoldConfigUri": string,
      "skaffoldConfigPath": string,
      "buildArtifacts": [
        {
          object ([BuildArtifact](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#BuildArtifact))
        }
      ],
      "deliveryPipelineSnapshot": {
        object ([DeliveryPipeline](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline))
      },
      "targetSnapshots": [
        {
          object ([Target](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target))
        }
      ],
      "customTargetTypeSnapshots": [
        {
          object ([CustomTargetType](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType))
        }
      ],
      "renderState": enum ([RenderState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#RenderState)),
      "etag": string,
      "skaffoldVersion": string,
      "targetArtifacts": {
        string: {
          object ([TargetArtifact](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#TargetArtifact))
        },
        ...
      },
      "targetRenders": {
        string: {
          object ([TargetRender](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#TargetRender))
        },
        ...
      },
      "condition": {
        object ([ReleaseCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ReleaseCondition))
      },
      "deployParameters": {
        string: string,
        ...
      },
      "toolVersions": {
        object ([ToolVersions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersions))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the `Release`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}`. The `release` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`  
`uid` |  `string` Output only. Unique identifier of the `Release`.  
`description` |  `string` Optional. Description of the `Release`. Max length is 255 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`abandoned` |  `boolean` Output only. Indicates whether this is an abandoned release.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `Release` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`renderStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the render began.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`renderEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the render completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`skaffoldConfigUri` |  `string` Optional. Cloud Storage URI of tar.gz archive containing Skaffold configuration.  
`skaffoldConfigPath` |  `string` Optional. Filepath of the Skaffold config inside of the config URI.  
`buildArtifacts[]` |  `object (`[BuildArtifact](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#BuildArtifact)`)` Optional. List of artifacts to pass through to Skaffold command.  
`deliveryPipelineSnapshot` |  `object (`[DeliveryPipeline](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines#DeliveryPipeline)`)` Output only. Snapshot of the parent pipeline taken at release creation time.  
`targetSnapshots[]` |  `object (`[Target](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets#Target)`)` Output only. Snapshot of the targets taken at release creation time.  
`customTargetTypeSnapshots[]` |  `object (`[CustomTargetType](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes#CustomTargetType)`)` Output only. Snapshot of the custom target types referenced by the targets taken at release creation time.  
`renderState` |  `enum (`[RenderState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#RenderState)`)` Output only. Current state of the render operation.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`skaffoldVersion` |  `string` Optional. The Skaffold version to use when operating on this release, such as "1.20.0". Not all versions are valid; Cloud Deploy supports a specific set of versions.If unset, the most recent supported Skaffold version will be used.  
`targetArtifacts` |  `map (key: string, value: object (`[TargetArtifact](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#TargetArtifact)`))` Output only. Map from target ID to the target artifacts created during the render operation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`targetRenders` |  `map (key: string, value: object (`[TargetRender](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#TargetRender)`))` Output only. Map from target ID to details of the render operation for that target.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`condition` |  `object (`[ReleaseCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ReleaseCondition)`)` Output only. Information around the state of the Release.  
`deployParameters` |  `map (key: string, value: string)` Optional. The deploy parameters to use for all targets in this release.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`toolVersions` |  `object (`[ToolVersions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersions)`)` Optional. The tool versions to use for this release and all subsequent operations involving this release. If unset, tool versions are frozen when the release is created.  
  
## BuildArtifact

Description of an a image to use during Skaffold rendering.

JSON representation  
---  
      
    
    {
      "image": string,
      "tag": string
    }  
  
Fields  
---  
`image` |  `string` Optional. Image name in Skaffold configuration.  
`tag` |  `string` Optional. Image tag to use. This will generally be the full path to an image, such as "gcr.io/my-project/busybox:1.2.3" or "gcr.io/my-project/busybox@sha256:abc123".  
  
## RenderState

Valid states of the render operation.

Enums  
---  
`RENDER_STATE_UNSPECIFIED` | The render state is unspecified.  
`SUCCEEDED` | All rendering operations have completed successfully.  
`FAILED` | All rendering operations have completed, and one or more have failed.  
`IN_PROGRESS` | Rendering has started and is not complete.  
  
## TargetArtifact

The artifacts produced by a target render operation.

JSON representation  
---  
      
    
    {
      "skaffoldConfigPath": string,
      "manifestPath": string,
      "phaseArtifacts": {
        string: {
          object ([PhaseArtifact](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#PhaseArtifact))
        },
        ...
      },
    
      // Union field uri can be only one of the following:
      "artifactUri": string
      // End of list of possible types for union field uri.
    }  
  
Fields  
---  
`skaffoldConfigPath` |  `string` Output only. File path of the resolved Skaffold configuration for the stable phase, relative to the URI.  
`manifestPath` |  `string` Output only. File path of the rendered manifest relative to the URI for the stable phase.  
`phaseArtifacts` |  `map (key: string, value: object (`[PhaseArtifact](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#PhaseArtifact)`))` Output only. Map from the phase ID to the phase artifacts for the `Target`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `uri`.`uri` can be only one of the following:  
`artifactUri` |  `string` Output only. URI of a directory containing the artifacts. This contains deployment configuration used by Skaffold during a rollout, and all paths are relative to this location.  
  
## PhaseArtifact

Contains the paths to the artifacts, relative to the URI, for a phase.

JSON representation  
---  
      
    
    {
      "skaffoldConfigPath": string,
      "manifestPath": string,
      "jobManifestsPath": string
    }  
  
Fields  
---  
`skaffoldConfigPath` |  `string` Output only. File path of the resolved Skaffold configuration relative to the URI.  
`manifestPath` |  `string` Output only. File path of the rendered manifest relative to the URI.  
`jobManifestsPath` |  `string` Output only. File path of the directory of rendered job manifests relative to the URI. This is only set if it is applicable.  
  
## TargetRender

Details of rendering for a single target.

JSON representation  
---  
      
    
    {
      "renderingBuild": string,
      "renderingState": enum ([TargetRenderState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#TargetRenderState)),
      "metadata": {
        object ([RenderMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#RenderMetadata))
      },
      "failureCause": enum ([FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#FailureCause)),
      "failureMessage": string
    }  
  
Fields  
---  
`renderingBuild` |  `string` Output only. The resource name of the Cloud Build `Build` object that is used to render the manifest for this target. Format is `projects/{project}/locations/{location}/builds/{build}`.  
`renderingState` |  `enum (`[TargetRenderState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#TargetRenderState)`)` Output only. Current state of the render operation for this Target.  
`metadata` |  `object (`[RenderMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#RenderMetadata)`)` Output only. Metadata related to the `Release` render for this Target.  
`failureCause` |  `enum (`[FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#FailureCause)`)` Output only. Reason this render failed. This will always be unspecified while the render in progress.  
`failureMessage` |  `string` Output only. Additional information about the render failure, if available.  
  
## TargetRenderState

Valid states of the render operation.

Enums  
---  
`TARGET_RENDER_STATE_UNSPECIFIED` | The render operation state is unspecified.  
`SUCCEEDED` | The render operation has completed successfully.  
`FAILED` | The render operation has failed.  
`IN_PROGRESS` | The render operation is in progress.  
  
## RenderMetadata

RenderMetadata includes information associated with a `Release` render.

JSON representation  
---  
      
    
    {
      "cloudRun": {
        object ([CloudRunRenderMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#CloudRunRenderMetadata))
      },
      "custom": {
        object ([CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata))
      },
      "kubernetes": {
        object ([KubernetesRenderMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#KubernetesRenderMetadata))
      }
    }  
  
Fields  
---  
`cloudRun` |  `object (`[CloudRunRenderMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#CloudRunRenderMetadata)`)` Output only. Metadata associated with rendering for Cloud Run.  
`custom` |  `object (`[CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata)`)` Output only. Custom metadata provided by user-defined render operation.  
`kubernetes` |  `object (`[KubernetesRenderMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#KubernetesRenderMetadata)`)` Output only. Metadata associated with rendering for a Kubernetes cluster (GKE or GKE Enterprise target).  
  
## CloudRunRenderMetadata

CloudRunRenderMetadata contains Cloud Run information associated with a `Release` render.

JSON representation  
---  
      
    
    {
      "service": string,
      "revision": string,
      "job": string,
      "workerPool": string
    }  
  
Fields  
---  
`service` |  `string` Output only. The name of the Cloud Run Service in the rendered manifest. Format is `projects/{project}/locations/{location}/services/{service}`.  
`revision` |  `string` Output only. The name of the Cloud Run Revision in the rendered manifest. Format is `projects/{project}/locations/{location}/services/{service}/revisions/{revision}`.  
`job` |  `string` Output only. The name of the Cloud Run Job in the rendered manifest. Format is `projects/{project}/locations/{location}/jobs/{job}`.  
`workerPool` |  `string` Output only. The name of the Cloud Run Worker Pool in the rendered manifest. Format is `projects/{project}/locations/{location}/workerPools/{workerPool}`.  
  
## KubernetesRenderMetadata

KubernetesRenderMetadata contains Kubernetes information associated with a `Release` render.

JSON representation  
---  
      
    
    {
      "deployment": string,
      "canaryDeployment": string,
      "kubernetesNamespace": string
    }  
  
Fields  
---  
`deployment` |  `string` Output only. Name of the Kubernetes Deployment that will be applied to the GKE cluster. Only set if a single Deployment was provided in the rendered manifest.  
`canaryDeployment` |  `string` Output only. Name of the canary version of the Kubernetes Deployment that will be applied to the GKE cluster. Only set if a canary deployment strategy was configured.  
`kubernetesNamespace` |  `string` Output only. Namespace the Kubernetes resources will be applied to in the GKE cluster. Only set if applying resources to a single namespace.  
  
## FailureCause

Well-known rendering failures.

Enums  
---  
`FAILURE_CAUSE_UNSPECIFIED` | No reason for failure is specified.  
`CLOUD_BUILD_UNAVAILABLE` | Cloud Build is not available, either because it is not enabled or because Cloud Deploy has insufficient permissions. See [required permission](https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions).  
`EXECUTION_FAILED` | The render operation did not complete successfully; check Cloud Build logs.  
`CLOUD_BUILD_REQUEST_FAILED` | Cloud Build failed to fulfill Cloud Deploy's request. See failureMessage for additional details.  
`VERIFICATION_CONFIG_NOT_FOUND` | The render operation did not complete successfully because the verification stanza required for verify was not found on the Skaffold configuration.  
`CUSTOM_ACTION_NOT_FOUND` | The render operation did not complete successfully because the custom action(s) required for Rollout jobs were not found in the Skaffold configuration. See failureMessage for additional details.  
`DEPLOYMENT_STRATEGY_NOT_SUPPORTED` | Release failed during rendering because the release configuration is not supported with the specified deployment strategy.  
`RENDER_FEATURE_NOT_SUPPORTED` | The render operation had a feature configured that is not supported.  
  
## ReleaseCondition

ReleaseCondition contains all conditions relevant to a Release.

JSON representation  
---  
      
    
    {
      "releaseReadyCondition": {
        object ([ReleaseReadyCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ReleaseReadyCondition))
      },
      "skaffoldSupportedCondition": {
        object ([SkaffoldSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#SkaffoldSupportedCondition))
      },
      "dockerVersionSupportedCondition": {
        object ([ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition))
      },
      "helmVersionSupportedCondition": {
        object ([ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition))
      },
      "kptVersionSupportedCondition": {
        object ([ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition))
      },
      "kubectlVersionSupportedCondition": {
        object ([ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition))
      },
      "kustomizeVersionSupportedCondition": {
        object ([ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition))
      },
      "skaffoldVersionSupportedCondition": {
        object ([ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition))
      }
    }  
  
Fields  
---  
`releaseReadyCondition` |  `object (`[ReleaseReadyCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ReleaseReadyCondition)`)` Details around the Releases's overall status.  
`skaffoldSupportedCondition` |  `object (`[SkaffoldSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#SkaffoldSupportedCondition)`)` Details around the support state of the release's Skaffold version.  
`dockerVersionSupportedCondition` |  `object (`[ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition)`)` Output only. Details around the support state of the release's Docker version.  
`helmVersionSupportedCondition` |  `object (`[ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition)`)` Output only. Details around the support state of the release's Helm version.  
`kptVersionSupportedCondition` |  `object (`[ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition)`)` Output only. Details around the support state of the release's kpt version.  
`kubectlVersionSupportedCondition` |  `object (`[ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition)`)` Output only. Details around the support state of the release's Kubectl version.  
`kustomizeVersionSupportedCondition` |  `object (`[ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition)`)` Output only. Details around the support state of the release's Kustomize version.  
`skaffoldVersionSupportedCondition` |  `object (`[ToolVersionSupportedCondition](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportedCondition)`)` Output only. Details around the support state of the release's Skaffold version.  
  
## ReleaseReadyCondition

ReleaseReadyCondition contains information around the status of the Release. If a release is not ready, you cannot create a rollout with the release.

JSON representation  
---  
      
    
    {
      "status": boolean
    }  
  
Fields  
---  
`status` |  `boolean` True if the Release is in a valid state. Otherwise at least one condition in `ReleaseCondition` is in an invalid state. Iterate over those conditions and see which condition(s) has status = false to find out what is wrong with the Release.  
  
## SkaffoldSupportedCondition

SkaffoldSupportedCondition contains information about when support for the release's version of Skaffold ends.

JSON representation  
---  
      
    
    {
      "status": boolean,
      "skaffoldSupportState": enum ([SkaffoldSupportState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#SkaffoldSupportState)),
      "maintenanceModeTime": string,
      "supportExpirationTime": string
    }  
  
Fields  
---  
`status` |  `boolean` True if the version of Skaffold used by this release is supported.  
`skaffoldSupportState` |  `enum (`[SkaffoldSupportState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#SkaffoldSupportState)`)` The Skaffold support state for this release's version of Skaffold.  
`maintenanceModeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which this release's version of Skaffold will enter maintenance mode.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`supportExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which this release's version of Skaffold will no longer be supported.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## SkaffoldSupportState

The support state of a specific Skaffold version.

Enums  
---  
`SKAFFOLD_SUPPORT_STATE_UNSPECIFIED` | Default value. This value is unused.  
`SKAFFOLD_SUPPORT_STATE_SUPPORTED` | This Skaffold version is currently supported.  
`SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE` | This Skaffold version is in maintenance mode.  
`SKAFFOLD_SUPPORT_STATE_UNSUPPORTED` | This Skaffold version is no longer supported.  
  
## ToolVersionSupportedCondition

ToolVersionSupportedCondition contains information about when support for the release's version of a tool ends.

JSON representation  
---  
      
    
    {
      "status": boolean,
      "toolVersionSupportState": enum ([ToolVersionSupportState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportState)),
      "maintenanceModeTime": string,
      "supportExpirationTime": string
    }  
  
Fields  
---  
`status` |  `boolean` Output only. True if the version of Tool used by this release is supported.  
`toolVersionSupportState` |  `enum (`[ToolVersionSupportState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases#ToolVersionSupportState)`)` Output only. The tool support state for this release's version of the tool.  
`maintenanceModeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this release's version of the tool will enter maintenance mode.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`supportExpirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this release's version of the tool will no longer be supported.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ToolVersionSupportState

The support state of a specific tool version.

Enums  
---  
`TOOL_VERSION_SUPPORT_STATE_UNSPECIFIED` | Default value. This value is unused.  
`TOOL_VERSION_SUPPORT_STATE_SUPPORTED` | This tool version is currently supported.  
`TOOL_VERSION_SUPPORT_STATE_MAINTENANCE_MODE` | This tool version is in maintenance mode.  
`TOOL_VERSION_SUPPORT_STATE_UNSUPPORTED` | This tool version is no longer supported.  
  
## ToolVersions

Details of ToolVersions for the release.

JSON representation  
---  
      
    
    {
      "docker": string,
      "helm": string,
      "kpt": string,
      "kubectl": string,
      "kustomize": string,
      "skaffold": string
    }  
  
Fields  
---  
`docker` |  `string` Optional. The Docker version to use for Cloud Deploy operations.  
`helm` |  `string` Optional. The Helm version to use for Cloud Deploy operations.  
`kpt` |  `string` Optional. The kpt version to use for Cloud Deploy operations.  
`kubectl` |  `string` Optional. The Kubectl version to use for Cloud Deploy operations.  
`kustomize` |  `string` Optional. The Kustomize version to use for Cloud Deploy operations.  
`skaffold` |  `string` Optional. The Skaffold version to use for Cloud Deploy operations.  
  
## Methods  
  
---  
  
### `[abandon](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/abandon)`

|  Abandons a Release in the Delivery Pipeline.  
  
### `[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/create)`

|  Creates a new Release in a given project and location.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/get)`

|  Gets details of a single Release.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/list)`

|  Lists Releases in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
