---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances
title: REST Resource: projects.locations.instanceOSPoliciesCompliances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:51:31.612505+00:00
---

# REST Resource: projects.locations.instanceOSPoliciesCompliances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.locations.instanceOSPoliciesCompliances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: InstanceOSPoliciesCompliance
    * JSON representation
  * OSPolicyComplianceState
  * OSPolicyCompliance
    * JSON representation
  * OSPolicyResourceCompliance
    * JSON representation
  * OSPolicyResourceConfigStep
    * JSON representation
  * Type
  * Outcome
  * ExecResourceOutput
    * JSON representation
  * Methods



## Resource: InstanceOSPoliciesCompliance

This item is deprecated!

This API resource represents the OS policies compliance data for a Compute Engine virtual machine (VM) instance at a given point in time.

A Compute Engine VM can have multiple OS policy assignments, and each assignment can have multiple OS policies. As a result, multiple OS policies could be applied to a single VM.

You can use this API resource to determine both the compliance state of your VM as well as the compliance state of an individual OS policy.

For more information, see [View compliance](https://cloud.google.com/compute/docs/os-configuration-management/view-compliance).

JSON representation  
---  
      
    
    {
      "name": string,
      "instance": string,
      "state": enum ([OSPolicyComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyComplianceState)),
      "detailedState": string,
      "detailedStateReason": string,
      "osPolicyCompliances": [
        {
          object ([OSPolicyCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyCompliance))
        }
      ],
      "lastComplianceCheckTime": string,
      "lastComplianceRunId": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The `InstanceOSPoliciesCompliance` API resource name.Format: `projects/{project_number}/locations/{location}/instanceOSPoliciesCompliances/{instance_id}`  
`instance` |  `string` Output only. The Compute Engine VM instance name.  
`state` |  `enum (`[OSPolicyComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyComplianceState)`)` Output only. Compliance state of the VM.  
`detailedState` |  `string` Output only. Detailed compliance state of the VM. This field is populated only when compliance state is `UNKNOWN`.It may contain one of the following values:

  * `no-compliance-data`: Compliance data is not available for this VM.
  * `no-agent-detected`: OS Config agent is not detected for this VM.
  * `config-not-supported-by-agent`: The version of the OS Config agent running on this VM does not support configuration management.
  * `inactive`: VM is not running.
  * `internal-service-errors`: There were internal service errors encountered while enforcing compliance.
  * `agent-errors`: OS config agent encountered errors while enforcing compliance.

  
`detailedStateReason` |  `string` Output only. The reason for the `detailedState` of the VM (if any).  
`osPolicyCompliances[]` |  `object (`[OSPolicyCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyCompliance)`)` Output only. Compliance data for each `OSPolicy` that is applied to the VM.  
`lastComplianceCheckTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of the last compliance check for the VM.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastComplianceRunId` |  `string` Output only. Unique identifier for the last compliance run. This id will be logged by the OS config agent during a compliance run and can be used for debugging and tracing purpose.  
  
## OSPolicyComplianceState

This item is deprecated!

Supported OSPolicy compliance states.

Enums  
---  
`OS_POLICY_COMPLIANCE_STATE_UNSPECIFIED` | Default value. This value is unused.  
`COMPLIANT` | Compliant state.  
`NON_COMPLIANT` | Non-compliant state  
`UNKNOWN` | Unknown compliance state.  
`NO_OS_POLICIES_APPLICABLE` | No applicable OS policies were found for the instance. This state is only applicable to the instance.  
  
## OSPolicyCompliance

This item is deprecated!

Compliance data for an OS policy

JSON representation  
---  
      
    
    {
      "osPolicyId": string,
      "osPolicyAssignment": string,
      "state": enum ([OSPolicyComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyComplianceState)),
      "osPolicyResourceCompliances": [
        {
          object ([OSPolicyResourceCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyResourceCompliance))
        }
      ]
    }  
  
Fields  
---  
`osPolicyId` |  `string` The OS policy id  
`osPolicyAssignment` |  `string` Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to.Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{osPolicyAssignmentId@revisionId}`  
`state` |  `enum (`[OSPolicyComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyComplianceState)`)` Compliance state of the OS policy.  
`osPolicyResourceCompliances[]` |  `object (`[OSPolicyResourceCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyResourceCompliance)`)` Compliance data for each `OSPolicyResource` that is applied to the VM.  
  
## OSPolicyResourceCompliance

This item is deprecated!

Compliance data for an OS policy resource.

JSON representation  
---  
      
    
    {
      "osPolicyResourceId": string,
      "configSteps": [
        {
          object ([OSPolicyResourceConfigStep](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyResourceConfigStep))
        }
      ],
      "state": enum ([OSPolicyComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyComplianceState)),
    
      // Union field output can be only one of the following:
      "execResourceOutput": {
        object ([ExecResourceOutput](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#ExecResourceOutput))
      }
      // End of list of possible types for union field output.
    }  
  
Fields  
---  
`osPolicyResourceId` |  `string` The id of the OS policy resource.  
`configSteps[]` |  `object (`[OSPolicyResourceConfigStep](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyResourceConfigStep)`)` Ordered list of configuration steps taken by the agent for the OS policy resource.  
`state` |  `enum (`[OSPolicyComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#OSPolicyComplianceState)`)` Compliance state of the OS policy resource.  
Union field `output`. Resource specific output. `output` can be only one of the following:  
`execResourceOutput` |  `object (`[ExecResourceOutput](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#ExecResourceOutput)`)` ExecResource specific output.  
  
## OSPolicyResourceConfigStep

This item is deprecated!

Step performed by the OS Config agent for configuring an `OSPolicyResource` to its desired state.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#Type)),
      "outcome": enum ([Outcome](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#Outcome)),
      "errorMessage": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#Type)`)` Configuration step type.  
`outcome` |  `enum (`[Outcome](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#Outcome)`)` Outcome of the configuration step.  
`errorMessage` |  `string` An error message recorded during the execution of this step. Only populated when outcome is FAILED.  
  
## Type

This item is deprecated!

Supported configuration step types

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`VALIDATION` | Validation to detect resource conflicts, schema errors, etc.  
`DESIRED_STATE_CHECK` | Check the current desired state status of the resource.  
`DESIRED_STATE_ENFORCEMENT` | Enforce the desired state for a resource that is not in desired state.  
`DESIRED_STATE_CHECK_POST_ENFORCEMENT` | Re-check desired state status for a resource after enforcement of all resources in the current configuration run.This step is used to determine the final desired state status for the resource. It accounts for any resources that might have drifted from their desired state due to side effects from configuring other resources during the current configuration run.  
  
## Outcome

This item is deprecated!

Supported outcomes for a configuration step.

Enums  
---  
`OUTCOME_UNSPECIFIED` | Default value. This value is unused.  
`SUCCEEDED` | The step succeeded.  
`FAILED` | The step failed.  
  
## ExecResourceOutput

This item is deprecated!

ExecResource specific output.

JSON representation  
---  
      
    
    {
      "enforcementOutput": string
    }  
  
Fields  
---  
`enforcementOutput` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output from Enforcement phase output file (if run). Output size is limited to 100K bytes.A base64-encoded string.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances/get)   
**(deprecated)**`

|  Get OS policies compliance data for the specified Compute Engine VM instance.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances/list)   
**(deprecated)**`

|  List OS policies compliance data for all Compute Engine VM instances in the specified zone.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
