---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages
title: REST Resource: projects.locations.fleetPackages \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:24.470695+00:00
---

# REST Resource: projects.locations.fleetPackages  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)



Send feedback 

#  REST Resource: projects.locations.fleetPackages Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: FleetPackage
    * JSON representation
  * ResourceBundleSelector
    * JSON representation
  * ResourceBundleTag
    * JSON representation
  * CloudBuildRepository
    * JSON representation
  * Target
    * JSON representation
  * Fleet
    * JSON representation
  * LabelSelector
    * JSON representation
  * VariantSelector
    * JSON representation
  * FleetPackageInfo
    * JSON representation
  * State
  * FleetPackageError
    * JSON representation
  * State
  * Methods



## Resource: FleetPackage

A `FleetPackage` resource in the Config Delivery API.

A `FleetPackage` defines a package through which Kubernetes configuration is deployed to a fleet of Kubernetes clusters.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "resourceBundleSelector": {
        object ([ResourceBundleSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#ResourceBundleSelector))
      },
      "target": {
        object ([Target](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#Target))
      },
      "rolloutStrategy": {
        object ([RolloutStrategy](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/RolloutStrategy))
      },
      "variantSelector": {
        object ([VariantSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#VariantSelector))
      },
      "info": {
        object ([FleetPackageInfo](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#FleetPackageInfo))
      },
      "deletionPropagationPolicy": enum ([DeletionPropagationPolicy](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/DeletionPropagationPolicy)),
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#State_1))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the `FleetPackage`. Format is `projects/{project}/locations/{location}/fleetPackages/{fleetPackage}`. The `fleetPackage` component must match `[a-z][a-z0-9\-]{0,62}`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `FleetPackage` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Most recent time at which the `FleetPackage` was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels are attributes that can be set and used by both the user and by Config Delivery. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`resourceBundleSelector` |  `object (`[ResourceBundleSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#ResourceBundleSelector)`)` Required. Information specifying the source of Kubernetes configuration to deploy.  
`target` |  `object (`[Target](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#Target)`)` Optional. Configuration to select target clusters to deploy Kubernetes configuration to.  
`rolloutStrategy` |  `object (`[RolloutStrategy](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/RolloutStrategy)`)` Optional. The strategy to use to deploy Kubernetes configuration to clusters.  
`variantSelector` |  `object (`[VariantSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#VariantSelector)`)` Required. Information specifying how to map a `ResourceBundle` variant to a target cluster.  
`info` |  `object (`[FleetPackageInfo](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#FleetPackageInfo)`)` Output only. Information containing the rollout status of the `FleetPackage` across all the target clusters.  
`deletionPropagationPolicy` |  `enum (`[DeletionPropagationPolicy](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/DeletionPropagationPolicy)`)` Optional. Information around how to handle Kubernetes resources at the target clusters when the `FleetPackage` is deleted.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#State_1)`)` Optional. The desired state of the fleet package.  
  
## ResourceBundleSelector

Information specifying the source of Kubernetes configuration to deploy.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "resourceBundle": {
        object ([ResourceBundleTag](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#ResourceBundleTag))
      },
      "cloudBuildRepository": {
        object ([CloudBuildRepository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#CloudBuildRepository))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Source can be a directly pushed `ResourceBundle` or `CloudBuildRepository` containing the Kubernetes configuration. `source` can be only one of the following:  
`resourceBundle` |  `object (`[ResourceBundleTag](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#ResourceBundleTag)`)` Information specifying `ResourceBundle`.  
`cloudBuildRepository` |  `object (`[CloudBuildRepository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#CloudBuildRepository)`)` Information specifying `CloudBuildRepository`.  
  
## ResourceBundleTag

ResourceBundleTag contains the information to refer to a release for a `ResourceBundle`.

JSON representation  
---  
      
    
    {
      "name": string,
      "tag": string
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the `ResourceBundle`. Format is projects/{p}/locations/{l}/resourceBundles/{r}.  
`tag` |  `string` Required. The Git tag for a version of the release in a ResourceBundle. The tag must follow the semantic versioning format vX.Y.Z.  
  
## CloudBuildRepository

CloudBuildRepository contains information about fetching Kubernetes configuration from a `CloudBuildRepository`.

JSON representation  
---  
      
    
    {
      "name": string,
      "path": string,
      "tag": string,
      "serviceAccount": string,
    
      // Union field variants can be only one of the following:
      "variantsPattern": string
      // End of list of possible types for union field variants.
    }  
  
Fields  
---  
`name` |  `string` Required. Name of the cloud build repository. Format is projects/{p}/locations/{l}/connections/{c}/repositories/{r}.  
`path` |  `string` Optional. Path to the directory or file within the repository that contains the Kubernetes configuration. If unspecified, path is assumed to the top level root directory of the repository.  
`tag` |  `string` Required. Git tag of the underlying git repository. The git tag must be in the semantic version format `vX.Y.Z`.  
`serviceAccount` |  `string` Required. Google service account to use in CloudBuild triggers to fetch and store Kubernetes configuration.  
Union field `variants`. Specifies configuration for how to find variants in the repository. `variants` can be only one of the following:  
`variantsPattern` |  `string` Optional. Glob pattern that will be used to find variants in the repository. Examples: `variants/*.yaml`, `us-*`  
  
## Target

The target defines different ways to target set of Kubernetes clusters.

JSON representation  
---  
      
    
    {
    
      // Union field target can be only one of the following:
      "fleet": {
        object ([Fleet](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#Fleet))
      }
      // End of list of possible types for union field target.
    }  
  
Fields  
---  
Union field `target`. Target for the fleet package. `target` can be only one of the following:  
`fleet` |  `object (`[Fleet](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#Fleet)`)` GKE fleet information to target rollout of the FleetPackage.  
  
## Fleet

The fleet where the `FleetPackage` should be deployed.

JSON representation  
---  
      
    
    {
      "project": string,
      "selector": {
        object ([LabelSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#LabelSelector))
      }
    }  
  
Fields  
---  
`project` |  `string` Required. The host project for the GKE fleet. Format is `projects/{project}`.  
`selector` |  `object (`[LabelSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#LabelSelector)`)` Optional. Selector allows targeting a subset of fleet members using their labels.  
  
## LabelSelector

A label selector is a label query over a set of resources. An empty label selector matches all objects.

JSON representation  
---  
      
    
    {
      "matchLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`matchLabels` |  `map (key: string, value: string)` Optional. Map of {key,value} pairs. Each {key,value} pair must match an existing label key and value exactly in order to satisfy the match.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## VariantSelector

VariantSelector contains information for selecting a variant in `ResourceBundle` to deploy to a target cluster.

JSON representation  
---  
      
    
    {
    
      // Union field strategy can be only one of the following:
      "variantNameTemplate": string
      // End of list of possible types for union field strategy.
    }  
  
Fields  
---  
Union field `strategy`. strategy for selecting a variant. `strategy` can be only one of the following:  
`variantNameTemplate` |  `string` Required. variantNameTemplate is a template that can refer to variables containing cluster membership metadata such as location, name, and labels to generate the name of the variant for a target cluster. The variable syntax is similar to the unix shell variables.Available variables are `${membership.name}`, `${membership.location}`, `${membership.project}` and `${membership.labels['label_name']}`.If you want to deploy a specific variant, say "default" to all the clusters, you can use "default" (string without any variables) as the variantNameTemplate.  
  
## FleetPackageInfo

FleetPackageInfo represents the status of the `FleetPackage` across all the target clusters.

JSON representation  
---  
      
    
    {
      "activeRollout": string,
      "lastCompletedRollout": string,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#State)),
      "errors": [
        {
          object ([FleetPackageError](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#FleetPackageError))
        }
      ]
    }  
  
Fields  
---  
`activeRollout` |  `string` Optional. The active rollout, if any. Format is `projects/{project}/locations/{location}/fleetPackages/{fleetPackage}/rollouts/{rollout}`.  
`lastCompletedRollout` |  `string` Optional. The last completed rollout, if any. Format is `projects/{project}/locations/{location}/fleetPackages/{fleetPackage}/rollouts/{rollout}`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#State)`)` Optional. Output only. The current state of the `FleetPackage`.  
`errors[]` |  `object (`[FleetPackageError](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages#FleetPackageError)`)` Optional. Output only. Errors encountered during configuration deployment (if any).  
  
## State

Possible values for the `FleetPackage` state.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | `FleetPackage` is active.  
`SUSPENDED` | `FleetPackage` is suspended.  
`FAILED` | `FleetPackage` has failed to reconcile.  
`DELETING` | `FleetPackage` is being deleted.  
  
## FleetPackageError

Information representing an error encountered during rolling out configurations.

JSON representation  
---  
      
    
    {
      "errorMessage": string
    }  
  
Fields  
---  
`errorMessage` |  `string` Optional. A description of the error.  
  
## State

State indicates the desired state for the fleet package. Unspecified value is equivalent to `ACTIVE`. If state is set to `SUSPENDED`, active rollout (if any) will continue but no new rollouts will be scheduled.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | `FleetPackage` is intended to be active.  
`SUSPENDED` | `FleetPackage` is intended to be suspended.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages/create)`

|  Creates a new FleetPackage in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages/delete)`

|  Deletes a single FleetPackage.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages/get)`

|  Gets details of a single FleetPackage.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages/list)`

|  Lists FleetPackages in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rest/v1/projects.locations.fleetPackages/patch)`

|  Updates the parameters of a single FleetPackage.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-28 UTC."],[],[]] 
