---
url: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements
title: REST Resource: folders.locations.entitlements \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:08.956206+00:00
---

# REST Resource: folders.locations.entitlements  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: folders.locations.entitlements Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Entitlement
    * JSON representation
    * AccessControlEntry
      * JSON representation
    * ApprovalWorkflow
      * JSON representation
    * ManualApprovals
      * JSON representation
    * Step
      * JSON representation
    * State
    * RequesterJustificationConfig
      * JSON representation
    * NotMandatory
    * Unstructured
    * AdditionalNotificationTargets
      * JSON representation
  * Methods



## Resource: Entitlement

An entitlement defines the eligibility of a set of users to obtain predefined access for some time possibly after going through an approval workflow.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "eligibleUsers": [
        {
          object ([AccessControlEntry](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.AccessControlEntry))
        }
      ],
      "approvalWorkflow": {
        object ([ApprovalWorkflow](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.ApprovalWorkflow))
      },
      "privilegedAccess": {
        object ([PrivilegedAccess](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/PrivilegedAccess))
      },
      "maxRequestDuration": string,
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.State)),
      "requesterJustificationConfig": {
        object ([RequesterJustificationConfig](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.RequesterJustificationConfig))
      },
      "additionalNotificationTargets": {
        object ([AdditionalNotificationTargets](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.AdditionalNotificationTargets))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the entitlement. Possible formats:

  * `organizations/{organization-number}/locations/{region}/entitlements/{entitlement-id}`
  * `folders/{folder-number}/locations/{region}/entitlements/{entitlement-id}`
  * `projects/{project-id|project-number}/locations/{region}/entitlements/{entitlement-id}`

  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`eligibleUsers[]` |  `object (`[AccessControlEntry](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.AccessControlEntry)`)` Optional. Who can create grants using this entitlement. This list should contain at most one entry.  
`approvalWorkflow` |  `object (`[ApprovalWorkflow](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.ApprovalWorkflow)`)` Optional. The approvals needed before access are granted to a requester. No approvals are needed if this field is null.  
`privilegedAccess` |  `object (`[PrivilegedAccess](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/PrivilegedAccess)`)` Required. The access granted to a requester on successful approval.  
`maxRequestDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. The maximum amount of time that access is granted for a request. A requester can ask for a shorter duration but never a longer one. The supported range is between 30 minutes and 168 hours (7 days).A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.State)`)` Output only. Current state of this entitlement.  
`requesterJustificationConfig` |  `object (`[RequesterJustificationConfig](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.RequesterJustificationConfig)`)` Required. The manner in which the requester should provide a justification for requesting access.  
`additionalNotificationTargets` |  `object (`[AdditionalNotificationTargets](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.AdditionalNotificationTargets)`)` Optional. Additional email addresses to be notified based on actions taken.  
`etag` |  `string` An `etag` is used for optimistic concurrency control as a way to prevent simultaneous updates to the same entitlement. An `etag` is returned in the response to `entitlements.get` and the caller should put the `etag` in the request to `entitlements.patch` so that their change is applied on the same version. If this field is omitted or if there is a mismatch while updating an entitlement, then the server rejects the request.  
  
### AccessControlEntry

`AccessControlEntry` is used to control who can do some operation.

JSON representation  
---  
      
    
    {
      "principals": [
        string
      ]
    }  
  
Fields  
---  
`principals[]` |  `string` Optional. Users who are allowed for the operation. Each entry should be a valid v1 IAM principal identifier. The format for these is documented at: <https://cloud.google.com/iam/docs/principal-identifiers#v1>  
  
### ApprovalWorkflow

Different types of approval workflows that can be used to gate privileged access granting.

JSON representation  
---  
      
    
    {
    
      // Union field approval_workflow can be only one of the following:
      "manualApprovals": {
        object ([ManualApprovals](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.ManualApprovals))
      }
      // End of list of possible types for union field approval_workflow.
    }  
  
Fields  
---  
Union field `approval_workflow`.`approval_workflow` can be only one of the following:  
`manualApprovals` |  `object (`[ManualApprovals](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.ManualApprovals)`)` An approval workflow where users designated as approvers review and act on the grants.  
  
### ManualApprovals

A manual approval workflow where users who are designated as approvers need to call the `ApproveGrant`/`DenyGrant` APIs for a grant. The workflow can consist of multiple serial steps where each step defines who can act as approver in that step and how many of those users should approve before the workflow moves to the next step.

This can be used to create approval workflows such as:

  * Require an approval from any user in a group G.
  * Require an approval from any k number of users from a Group G.
  * Require an approval from any user in a group G and then from a user U.



A single user might be part of the `approvers` ACL for multiple steps in this workflow, but they can only approve once and that approval is only considered to satisfy the approval step at which it was granted.

JSON representation  
---  
      
    
    {
      "requireApproverJustification": boolean,
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.Step))
        }
      ]
    }  
  
Fields  
---  
`requireApproverJustification` |  `boolean` Optional. Do the approvers need to provide a justification for their actions?  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.Step)`)` Optional. List of approval steps in this workflow. These steps are followed in the specified order sequentially. Only 1 step is supported.  
  
### Step

Step represents a logical step in a manual approval workflow.

JSON representation  
---  
      
    
    {
      "approvers": [
        {
          object ([AccessControlEntry](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.AccessControlEntry))
        }
      ],
      "approvalsNeeded": integer,
      "approverEmailRecipients": [
        string
      ],
      "id": string
    }  
  
Fields  
---  
`approvers[]` |  `object (`[AccessControlEntry](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.AccessControlEntry)`)` Optional. The potential set of approvers in this step. This list must contain at most one entry.  
`approvalsNeeded` |  `integer` Required. How many users from the above list need to approve. If there aren't enough distinct users in the list, then the workflow indefinitely blocks. Should always be greater than 0. 1 is the only supported value.  
`approverEmailRecipients[]` |  `string` Optional. Additional email addresses to be notified when a grant is pending approval.  
`id` |  `string` Output only. Step ID used to identify the step in the workflow.  
  
### State

Different states an entitlement can be in.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state. This value is never returned by the server.  
`CREATING` | The entitlement is being created.  
`AVAILABLE` | The entitlement is available for requesting access.  
`DELETING` | The entitlement is being deleted.  
`DELETED` | The entitlement has been deleted.  
`UPDATING` | The entitlement is being updated.  
  
### RequesterJustificationConfig

Defines how a requester must provide a justification when requesting access.

JSON representation  
---  
      
    
    {
    
      // Union field justification_type can be only one of the following:
      "notMandatory": {
        object ([NotMandatory](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.NotMandatory))
      },
      "unstructured": {
        object ([Unstructured](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.Unstructured))
      }
      // End of list of possible types for union field justification_type.
    }  
  
Fields  
---  
Union field `justification_type`. This is a required field and the user must explicitly opt out if a justification from the requester isn't mandatory. `justification_type` can be only one of the following:  
`notMandatory` |  `object (`[NotMandatory](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.NotMandatory)`)` This option means the requester isn't required to provide a justification.  
`unstructured` |  `object (`[Unstructured](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements#Entitlement.Unstructured)`)` This option means the requester must provide a string as justification. If this is selected, the server allows the requester to provide a justification but doesn't validate it.  
  
### NotMandatory

This type has no fields.

The justification is not mandatory but can be provided in any of the supported formats.

### Unstructured

This type has no fields.

The requester has to provide a justification in the form of a string.

### AdditionalNotificationTargets

`AdditionalNotificationTargets` includes email addresses to be notified.

JSON representation  
---  
      
    
    {
      "adminEmailRecipients": [
        string
      ],
      "requesterEmailRecipients": [
        string
      ]
    }  
  
Fields  
---  
`adminEmailRecipients[]` |  `string` Optional. Additional email addresses to be notified when a principal (requester) is granted access.  
`requesterEmailRecipients[]` |  `string` Optional. Additional email address to be notified about an eligible entitlement.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements/create)`

|  Creates a new entitlement in a given project, folder, organization, and in a given location.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements/delete)`

|  Deletes a single entitlement.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements/get)`

|  Gets details of a single entitlement.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements/list)`

|  Lists the entitlements in a given project, folder, organization, and in a given location.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements/patch)`

|  Updates the entitlement specified in the request.  
  
### `[search](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1beta/folders.locations.entitlements/search)`

|  `SearchEntitlements` returns entitlements on which the caller has the specified access.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-13 UTC."],[],[]] 
