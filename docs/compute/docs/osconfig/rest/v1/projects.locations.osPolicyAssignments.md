---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments
title: REST Resource: projects.locations.osPolicyAssignments \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:31.667605+00:00
---

# REST Resource: projects.locations.osPolicyAssignments  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.locations.osPolicyAssignments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: OSPolicyAssignment
    * JSON representation
  * Methods



## Resource: OSPolicyAssignment

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
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/create)`

|  Create an OS policy assignment.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/delete)`

|  Delete the OS policy assignment.  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/get)`

|  Retrieve an existing OS policy assignment.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/list)`

|  List the OS policy assignments under the parent resource.  
  
### `[listRevisions](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/listRevisions)`

|  List the OS policy assignment revisions for a given OS policy assignment.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/patch)`

|  Update an existing OS policy assignment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
