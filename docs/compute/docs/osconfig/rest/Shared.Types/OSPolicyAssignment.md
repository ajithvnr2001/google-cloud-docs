---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment/
title: OSPolicyAssignment \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:13.453045+00:00
---

# OSPolicyAssignment  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  OSPolicyAssignment Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * InstanceFilter
    * JSON representation
  * LabelSet
    * JSON representation
  * Inventory
    * JSON representation
  * Rollout
    * JSON representation



OS policy assignment is an API resource that is used to apply a set of OS policies to a dynamically targeted group of Compute Engine VM instances.

An OS policy is used to define the desired state configuration for a Compute Engine VM instance through a set of configuration resources that provide capabilities such as installing or removing software packages, or executing a script.

For more information about the OS policy resource definitions and examples, see [OS policy and OS policy assignment](https://cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies).

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "osPolicies": [
        {
          object ([OSPolicy](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy))
        }
      ],
      "instanceFilter": {
        object ([InstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#InstanceFilter))
      },
      "rollout": {
        object ([Rollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#Rollout))
      },
      "revisionId": string,
      "revisionCreateTime": string,
      "etag": string,
      "rolloutState": enum ([RolloutState](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/RolloutState)),
      "baseline": boolean,
      "deleted": boolean,
      "reconciling": boolean,
      "uid": string
    }  
  
Fields  
---  
`name` |  `string` Resource name.Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{osPolicyAssignmentId}`This field is ignored when you create an OS policy assignment.  
`description` |  `string` OS policy assignment description. Length of the description is limited to 1024 characters.  
`osPolicies[]` |  `object (`[OSPolicy](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicy)`)` Required. List of OS policies to be applied to the VMs.  
`instanceFilter` |  `object (`[InstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#InstanceFilter)`)` Required. Filter to select VMs.  
`rollout` |  `object (`[Rollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#Rollout)`)` Required. Rollout to deploy the OS policy assignment. A rollout is triggered in the following situations: 1) OSPolicyAssignment is created. 2) OSPolicyAssignment is updated and the update contains changes to one of the following fields: - instanceFilter - osPolicies 3) OSPolicyAssignment is deleted.  
`revisionId` |  `string` Output only. The assignment revision ID A new revision is committed whenever a rollout is triggered for a OS policy assignment  
`revisionCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp that the revision was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` The etag for this OS policy assignment. If this is provided on update, it must match the server's etag.  
`rolloutState` |  `enum (`[RolloutState](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/RolloutState)`)` Output only. OS policy assignment rollout state  
`baseline` |  `boolean` Output only. Indicates that this revision has been successfully rolled out in this zone and new VMs will be assigned OS policies from this revision.For a given OS policy assignment, there is only one revision with a value of `true` for this field.  
`deleted` |  `boolean` Output only. Indicates that this revision deletes the OS policy assignment.  
`reconciling` |  `boolean` Output only. Indicates that reconciliation is in progress for the revision. This value is `true` when the `rolloutState` is one of: * IN_PROGRESS * CANCELLING  
`uid` |  `string` Output only. Server generated unique id for the OS policy assignment resource.  
  
## InstanceFilter

Filters to select target VMs for an assignment.

If more than one filter criteria is specified below, a VM will be selected if and only if it satisfies all of them.

JSON representation  
---  
      
    
    {
      "all": boolean,
      "inclusionLabels": [
        {
          object ([LabelSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#LabelSet))
        }
      ],
      "exclusionLabels": [
        {
          object ([LabelSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#LabelSet))
        }
      ],
      "inventories": [
        {
          object ([Inventory](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#Inventory))
        }
      ]
    }  
  
Fields  
---  
`all` |  `boolean` Target all VMs in the project. If true, no other criteria is permitted.  
`inclusionLabels[]` |  `object (`[LabelSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#LabelSet)`)` List of label sets used for VM inclusion.If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.  
`exclusionLabels[]` |  `object (`[LabelSet](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#LabelSet)`)` List of label sets used for VM exclusion.If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.  
`inventories[]` |  `object (`[Inventory](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/OSPolicyAssignment#Inventory)`)` List of inventories to select VMs.A VM is selected if its inventory data matches at least one of the following inventories.  
  
## LabelSet

Message representing label set. * A label is a key value pair set for a VM. * A LabelSet is a set of labels. * Labels within a LabelSet are ANDed. In other words, a LabelSet is applicable for a VM only if it matches all the labels in the LabelSet. * Example: A LabelSet with 2 labels: `env=prod` and `type=webserver` will only be applicable for those VMs with both labels present.

JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`labels` |  `map (key: string, value: string)` Labels are identified by key/value pairs in this map. A VM should contain all the key/value pairs specified in this map to be selected.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## Inventory

VM inventory details.

JSON representation  
---  
      
    
    {
      "osShortName": string,
      "osVersion": string
    }  
  
Fields  
---  
`osShortName` |  `string` Required. The OS short name  
`osVersion` |  `string` The OS versionPrefix matches are supported if asterisk(*) is provided as the last character. For example, to match all versions with a major version of `7`, specify the following value for this field `7.*`An empty string matches all OS versions.  
  
## Rollout

Message to configure the rollout at the zonal level for the OS policy assignment.

JSON representation  
---  
      
    
    {
      "disruptionBudget": {
        object ([FixedOrPercent](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/FixedOrPercent))
      },
      "minWaitDuration": string
    }  
  
Fields  
---  
`disruptionBudget` |  `object (`[FixedOrPercent](https://docs.cloud.google.com/compute/docs/osconfig/rest/Shared.Types/FixedOrPercent)`)` Required. The maximum number (or percentage) of VMs per zone to disrupt at any given moment.  
`minWaitDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. This determines the minimum duration of time to wait after the configuration changes are applied through the current rollout. A VM continues to count towards the `disruptionBudget` at least until this duration of time has passed after configuration changes are applied.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
