---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport/
title: OSPolicyAssignmentReport \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:37.168974+00:00
---

# OSPolicyAssignmentReport  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  OSPolicyAssignmentReport Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * OSPolicyCompliance
    * JSON representation
  * ComplianceState
  * OSPolicyResourceCompliance
    * JSON representation
  * OSPolicyResourceConfigStep
    * JSON representation
  * Type
  * ComplianceState
  * ExecResourceOutput
    * JSON representation



A report of the OS policy assignment status for a given instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "instance": string,
      "osPolicyAssignment": string,
      "osPolicyCompliances": [
        {
          object ([OSPolicyCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#OSPolicyCompliance))
        }
      ],
      "updateTime": string,
      "lastRunId": string
    }  
  
Fields  
---  
`name` |  `string` The `OSPolicyAssignmentReport` API resource name.Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/osPolicyAssignments/{osPolicyAssignmentId}/report`  
`instance` |  `string` The Compute Engine VM instance name.  
`osPolicyAssignment` |  `string` Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to.Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{osPolicyAssignmentId@revisionId}`  
`osPolicyCompliances[]` |  `object (`[OSPolicyCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#OSPolicyCompliance)`)` Compliance data for each `OSPolicy` that is applied to the VM.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp for when the report was last generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastRunId` |  `string` Unique identifier of the last attempted run to apply the OS policies associated with this assignment on the VM.This ID is logged by the OS Config agent while applying the OS policies associated with this assignment on the VM. NOTE: If the service is unable to successfully connect to the agent for this run, then this id will not be available in the agent logs.  
  
## OSPolicyCompliance

Compliance data for an OS policy

JSON representation  
---  
      
    
    {
      "osPolicyId": string,
      "complianceState": enum ([ComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#ComplianceState)),
      "complianceStateReason": string,
      "osPolicyResourceCompliances": [
        {
          object ([OSPolicyResourceCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#OSPolicyResourceCompliance))
        }
      ]
    }  
  
Fields  
---  
`osPolicyId` |  `string` The OS policy id  
`complianceState` |  `enum (`[ComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#ComplianceState)`)` The compliance state of the OS policy.  
`complianceStateReason` |  `string` The reason for the OS policy to be in an unknown compliance state. This field is always populated when `complianceState` is `UNKNOWN`.If populated, the field can contain one of the following values:

  * `vm-not-running`: The VM was not running.
  * `os-policies-not-supported-by-agent`: The version of the OS Config agent running on the VM does not support running OS policies.
  * `no-agent-detected`: The OS Config agent is not detected for the VM.
  * `resource-execution-errors`: The OS Config agent encountered errors while executing one or more resources in the policy. See `osPolicyResourceCompliances` for details.
  * `task-timeout`: The task sent to the agent to apply the policy timed out.
  * `unexpected-agent-state`: The OS Config agent did not report the final status of the task that attempted to apply the policy. Instead, the agent unexpectedly started working on a different task. This mostly happens when the agent or VM unexpectedly restarts while applying OS policies.
  * `internal-service-errors`: Internal service errors were encountered while attempting to apply the policy.
  * `os-policy-execution-pending`: OS policy was assigned to the given VM, but was not executed yet. Typically this is a transient condition that will go away after the next policy execution cycle.

  
`osPolicyResourceCompliances[]` |  `object (`[OSPolicyResourceCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#OSPolicyResourceCompliance)`)` Compliance data for each resource within the policy that is applied to the VM.  
  
## ComplianceState

Possible compliance states for an os policy.

Enums  
---  
`UNKNOWN` | The policy is in an unknown compliance state.Refer to the field `complianceStateReason` to learn the exact reason for the policy to be in this compliance state.  
`COMPLIANT` | Policy is compliant.The policy is compliant if all the underlying resources are also compliant.  
`NON_COMPLIANT` | Policy is non-compliant.The policy is non-compliant if one or more underlying resources are non-compliant.  
  
## OSPolicyResourceCompliance

Compliance data for an OS policy resource.

JSON representation  
---  
      
    
    {
      "osPolicyResourceId": string,
      "configSteps": [
        {
          object ([OSPolicyResourceConfigStep](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#OSPolicyResourceConfigStep))
        }
      ],
      "complianceState": enum ([ComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#ComplianceState_1)),
      "complianceStateReason": string,
    
      // Union field output can be only one of the following:
      "execResourceOutput": {
        object ([ExecResourceOutput](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#ExecResourceOutput))
      }
      // End of list of possible types for union field output.
    }  
  
Fields  
---  
`osPolicyResourceId` |  `string` The ID of the OS policy resource.  
`configSteps[]` |  `object (`[OSPolicyResourceConfigStep](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#OSPolicyResourceConfigStep)`)` Ordered list of configuration completed by the agent for the OS policy resource.  
`complianceState` |  `enum (`[ComplianceState](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#ComplianceState_1)`)` The compliance state of the resource.  
`complianceStateReason` |  `string` A reason for the resource to be in the given compliance state. This field is always populated when `complianceState` is `UNKNOWN`.The following values are supported when `complianceState == UNKNOWN`

  * `execution-errors`: Errors were encountered by the agent while executing the resource and the compliance state couldn't be determined.
  * `execution-skipped-by-agent`: Resource execution was skipped by the agent because errors were encountered while executing prior resources in the OS policy.
  * `os-policy-execution-attempt-failed`: The execution of the OS policy containing this resource failed and the compliance state couldn't be determined.
  * `os-policy-execution-pending`: OS policy that owns this resource was assigned to the given VM, but was not executed yet.

  
Union field `output`. Resource specific output. `output` can be only one of the following:  
`execResourceOutput` |  `object (`[ExecResourceOutput](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#ExecResourceOutput)`)` ExecResource specific output.  
  
## OSPolicyResourceConfigStep

Step performed by the OS Config agent for configuring an `OSPolicy` resource to its desired state.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#Type)),
      "errorMessage": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/OSPolicyAssignmentReport#Type)`)` Configuration step type.  
`errorMessage` |  `string` An error message recorded during the execution of this step. Only populated if errors were encountered during this step execution.  
  
## Type

Supported configuration step types

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`VALIDATION` | Checks for resource conflicts such as schema errors.  
`DESIRED_STATE_CHECK` | Checks the current status of the desired state for a resource.  
`DESIRED_STATE_ENFORCEMENT` | Enforces the desired state for a resource that is not in desired state.  
`DESIRED_STATE_CHECK_POST_ENFORCEMENT` | Re-checks the status of the desired state. This check is done for a resource after the enforcement of all OS policies.This step is used to determine the final desired state status for the resource. It accounts for any resources that might have drifted from their desired state due to side effects from executing other resources.  
  
## ComplianceState

Possible compliance states for a resource.

Enums  
---  
`UNKNOWN` | The resource is in an unknown compliance state.To get more details about why the policy is in this state, review the output of the `complianceStateReason` field.  
`COMPLIANT` | Resource is compliant.  
`NON_COMPLIANT` | Resource is non-compliant.  
  
## ExecResourceOutput

ExecResource specific output.

JSON representation  
---  
      
    
    {
      "enforcementOutput": string
    }  
  
Fields  
---  
`enforcementOutput` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output from enforcement phase output file (if run). Output size is limited to 100K bytes.A base64-encoded string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
