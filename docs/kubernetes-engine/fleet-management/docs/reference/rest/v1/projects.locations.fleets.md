---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets
title: REST Resource: projects.locations.fleets \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:56.700450+00:00
---

# REST Resource: projects.locations.fleets  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  REST Resource: projects.locations.fleets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Fleet
    * JSON representation
  * FleetLifecycleState
    * JSON representation
  * FleetLifecycleState.Code
  * DefaultClusterConfig
    * JSON representation
  * SecurityPostureConfig
    * JSON representation
  * SecurityPostureConfig.Mode
  * SecurityPostureConfig.VulnerabilityMode
  * BinaryAuthorizationConfig
    * JSON representation
  * BinaryAuthorizationConfig.EvaluationMode
  * BinaryAuthorizationConfig.PolicyBinding
    * JSON representation
  * CompliancePostureConfig
    * JSON representation
  * CompliancePostureConfig.Mode
  * CompliancePostureConfig.ComplianceStandard
    * JSON representation
  * Methods



## Resource: Fleet

Fleet contains the Fleet-wide metadata and configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "uid": string,
      "state": {
        object ([FleetLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#FleetLifecycleState))
      },
      "defaultClusterConfig": {
        object ([DefaultClusterConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#DefaultClusterConfig))
      },
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The full, unique resource name of this fleet in the format of `projects/{project}/locations/{location}/fleets/{fleet}`.Each Google Cloud project can have at most one fleet resource, named "default".  
`displayName` |  `string` Optional. A user-assigned display name of the Fleet. When present, it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point.Example: `Production Fleet`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the Fleet was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the Fleet was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. When the Fleet was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. Google-generated UUID for this resource. This is unique across all Fleet resources. If a Fleet resource is deleted and another resource with the same name is created, it gets a different uid.  
`state` |  `object (`[FleetLifecycleState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#FleetLifecycleState)`)` Output only. State of the namespace resource.  
`defaultClusterConfig` |  `object (`[DefaultClusterConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#DefaultClusterConfig)`)` Optional. The default cluster configurations to apply across the fleet.  
`labels` |  `map (key: string, value: string)` Optional. Labels for this Fleet.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## FleetLifecycleState

FleetLifecycleState describes the state of a Fleet resource.

JSON representation  
---  
      
    
    {
      "code": enum ([FleetLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#FleetLifecycleState.Code))
    }  
  
Fields  
---  
`code` |  `enum (`[FleetLifecycleState.Code](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#FleetLifecycleState.Code)`)` Output only. The current state of the Fleet resource.  
  
## FleetLifecycleState.Code

Code describes the state of a Fleet resource.

Enums  
---  
`CODE_UNSPECIFIED` | The code is not set.  
`CREATING` | The fleet is being created.  
`READY` | The fleet active.  
`DELETING` | The fleet is being deleted.  
`UPDATING` | The fleet is being updated.  
  
## DefaultClusterConfig

DefaultClusterConfig describes the default cluster configurations to be applied to all clusters born-in-fleet.

JSON representation  
---  
      
    
    {
      "securityPostureConfig": {
        object ([SecurityPostureConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#SecurityPostureConfig))
      },
      "binaryAuthorizationConfig": {
        object ([BinaryAuthorizationConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#BinaryAuthorizationConfig))
      },
      "compliancePostureConfig": {
        object ([CompliancePostureConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#CompliancePostureConfig))
      }
    }  
  
Fields  
---  
`securityPostureConfig` |  `object (`[SecurityPostureConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#SecurityPostureConfig)`)` Enable/Disable Security Posture features for the cluster.  
`binaryAuthorizationConfig` |  `object (`[BinaryAuthorizationConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#BinaryAuthorizationConfig)`)` Optional. Enable/Disable binary authorization features for the cluster.  
`compliancePostureConfig` |  `object (`[CompliancePostureConfig](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#CompliancePostureConfig)`)` Optional. Enable/Disable Compliance Posture features for the cluster. Note that on fleets.patch, only full replacement of this field is allowed. Users are not allowed for partial updates through field mask.  
  
## SecurityPostureConfig

SecurityPostureConfig defines the flags needed to enable/disable features for the Security Posture API.

JSON representation  
---  
      
    
    {
      "mode": enum ([SecurityPostureConfig.Mode](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#SecurityPostureConfig.Mode)),
      "vulnerabilityMode": enum ([SecurityPostureConfig.VulnerabilityMode](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#SecurityPostureConfig.VulnerabilityMode))
    }  
  
Fields  
---  
`mode` |  `enum (`[SecurityPostureConfig.Mode](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#SecurityPostureConfig.Mode)`)` Sets which mode to use for Security Posture features.  
`vulnerabilityMode` |  `enum (`[SecurityPostureConfig.VulnerabilityMode](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#SecurityPostureConfig.VulnerabilityMode)`)` Sets which mode to use for vulnerability scanning.  
  
## SecurityPostureConfig.Mode

Mode defines enablement mode for GKE Security posture features.

Enums  
---  
`MODE_UNSPECIFIED` | Default value not specified.  
`DISABLED` | Disables Security Posture features on the cluster.  
`BASIC` | Applies Security Posture features on the cluster.  
`ENTERPRISE` | Applies the Security Posture off cluster Enterprise level features.  
  
## SecurityPostureConfig.VulnerabilityMode

VulnerabilityMode defines enablement mode for vulnerability scanning.

Enums  
---  
`VULNERABILITY_MODE_UNSPECIFIED` | Default value not specified.  
`VULNERABILITY_DISABLED` | Disables vulnerability scanning on the cluster.  
`VULNERABILITY_BASIC` | Applies basic vulnerability scanning on the cluster.  
`VULNERABILITY_ENTERPRISE` | Applies the Security Posture's vulnerability on cluster Enterprise level features.  
  
## BinaryAuthorizationConfig

BinaryAuthorizationConfig defines the fleet level configuration of binary authorization feature.

JSON representation  
---  
      
    
    {
      "evaluationMode": enum ([BinaryAuthorizationConfig.EvaluationMode](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#BinaryAuthorizationConfig.EvaluationMode)),
      "policyBindings": [
        {
          object ([BinaryAuthorizationConfig.PolicyBinding](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#BinaryAuthorizationConfig.PolicyBinding))
        }
      ]
    }  
  
Fields  
---  
`evaluationMode` |  `enum (`[BinaryAuthorizationConfig.EvaluationMode](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#BinaryAuthorizationConfig.EvaluationMode)`)` Optional. Mode of operation for binauthz policy evaluation.  
`policyBindings[]` |  `object (`[BinaryAuthorizationConfig.PolicyBinding](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#BinaryAuthorizationConfig.PolicyBinding)`)` Optional. Binauthz policies that apply to this cluster.  
  
## BinaryAuthorizationConfig.EvaluationMode

Binary Authorization mode of operation.

Enums  
---  
`EVALUATION_MODE_UNSPECIFIED` | Default value  
`DISABLED` | Disable BinaryAuthorization  
`POLICY_BINDINGS` | Use Binary Authorization with the policies specified in policyBindings.  
  
## BinaryAuthorizationConfig.PolicyBinding

Binauthz policy that applies to this cluster.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` The relative resource name of the binauthz platform policy to audit. GKE platform policies have the following format: `projects/{project_number}/platforms/gke/policies/{policyId}`.  
  
## CompliancePostureConfig

CompliancePostureConfig defines the settings needed to enable/disable features for the Compliance Posture.

JSON representation  
---  
      
    
    {
      "mode": enum ([CompliancePostureConfig.Mode](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#CompliancePostureConfig.Mode)),
      "complianceStandards": [
        {
          object ([CompliancePostureConfig.ComplianceStandard](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#CompliancePostureConfig.ComplianceStandard))
        }
      ]
    }  
  
Fields  
---  
`mode` |  `enum (`[CompliancePostureConfig.Mode](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#CompliancePostureConfig.Mode)`)` Defines the enablement mode for Compliance Posture.  
`complianceStandards[]` |  `object (`[CompliancePostureConfig.ComplianceStandard](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets#CompliancePostureConfig.ComplianceStandard)`)` List of enabled compliance standards.  
  
## CompliancePostureConfig.Mode

Enums  
---  
`MODE_UNSPECIFIED` | Default value not specified.  
`DISABLED` | Disables Compliance Posture features on the cluster.  
`ENABLED` | Enables Compliance Posture features on the cluster.  
  
## CompliancePostureConfig.ComplianceStandard

JSON representation  
---  
      
    
    {
      "standard": string
    }  
  
Fields  
---  
`standard` |  `string` Name of the compliance standard.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/create)`

|  Creates a fleet.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/delete)`

|  Removes a Fleet.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/get)`

|  Returns the details of a fleet.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/list)`

|  Returns all fleets within an organization or a project that the caller has access to.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/patch)`

|  Updates a fleet.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
