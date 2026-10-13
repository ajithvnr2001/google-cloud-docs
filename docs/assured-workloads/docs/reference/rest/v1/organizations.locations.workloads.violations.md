---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations
title: REST Resource: organizations.locations.workloads.violations \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:29.519023+00:00
---

# REST Resource: organizations.locations.workloads.violations  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.workloads.violations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Violation
    * JSON representation
  * State
  * Remediation
    * JSON representation
  * Instructions
    * JSON representation
  * Gcloud
    * JSON representation
  * Console
    * JSON representation
  * RemediationType
  * ExceptionContext
    * JSON representation
  * ViolationType
  * Methods



## Resource: Violation

Workload monitoring Violation.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "beginTime": string,
      "updateTime": string,
      "resolveTime": string,
      "category": string,
      "state": enum ([State](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#State)),
      "orgPolicyConstraint": string,
      "auditLogLink": string,
      "nonCompliantOrgPolicy": string,
      "remediation": {
        object ([Remediation](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#Remediation))
      },
      "acknowledged": boolean,
      "exceptionAuditLogLink": string,
      "exceptionContexts": [
        {
          object ([ExceptionContext](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#ExceptionContext))
        }
      ],
      "violationType": enum ([ViolationType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#ViolationType)),
      "associatedOrgPolicyViolationId": string,
      "parentProjectNumber": string,
      "resourceType": string,
      "resourceName": string,
      "acknowledgementTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Immutable. Name of the Violation. Format: organizations/{organization}/locations/{location}/workloads/{workload_id}/violations/{violations_id}  
`description` |  `string` Output only. Description for the Violation. e.g. OrgPolicy gcp.resourceLocations has non compliant value.  
`beginTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time of the event which triggered the Violation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time when the Violation record was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`resolveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time of the event which fixed the Violation. If the violation is ACTIVE this will be empty.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`category` |  `string` Output only. Category under which this violation is mapped. e.g. Location, Service Usage, Access, Encryption, etc.  
`state` |  `enum (`[State](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#State)`)` Output only. State of the violation  
`orgPolicyConstraint  
**(deprecated)**` |  `string` This item is deprecated!Output only. Immutable. The org-policy-constraint that was incorrectly changed, which resulted in this violation.  
`auditLogLink` |  `string` Output only. Immutable. Audit Log Link for violated resource Format: <https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{timeRange}{folder>}  
`nonCompliantOrgPolicy` |  `string` Output only. Immutable. Name of the OrgPolicy which was modified with non-compliant change and resulted this violation. Format: projects/{project_number}/policies/{constraintName} folders/{folderId}/policies/{constraintName} organizations/{organization_id}/policies/{constraintName}  
`remediation` |  `object (`[Remediation](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#Remediation)`)` Output only. Compliance violation remediation  
`acknowledged` |  `boolean` A boolean that indicates if the violation is acknowledged  
`exceptionAuditLogLink` |  `string` Output only. Immutable. Audit Log link to find business justification provided for violation exception. Format: <https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{protoPayload.methodName}{timeRange}{organization>}  
`exceptionContexts[]` |  `object (`[ExceptionContext](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#ExceptionContext)`)` Output only. List of all the exception detail added for the violation.  
`violationType` |  `enum (`[ViolationType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#ViolationType)`)` Output only. Type of the violation  
`associatedOrgPolicyViolationId` |  `string` Optional. Output only. Violation Id of the org-policy violation due to which the resource violation is caused. Empty for org-policy violations.  
`parentProjectNumber` |  `string` Optional. Output only. Parent project number where resource is present. Empty for org-policy violations.  
`resourceType` |  `string` Optional. Output only. Type of the resource like compute.googleapis.com/Disk, etc. Empty for org-policy violations.  
`resourceName` |  `string` Optional. Output only. Name of the resource like //storage.googleapis.com/myprojectxyz-testbucket. Empty for org-policy violations.  
`acknowledgementTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when this violation was acknowledged first. Check exceptionContexts to find the last time the violation was acknowledged when there are more than one violations. This field will be absent when acknowledged field is marked as false.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## State

Violation State Values

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`RESOLVED` | Violation is resolved.  
`UNRESOLVED` | Violation is Unresolved  
`EXCEPTION` | Violation is Exception  
  
## Remediation

Represents remediation guidance to resolve compliance violation for AssuredWorkload

JSON representation  
---  
      
    
    {
      "instructions": {
        object ([Instructions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#Instructions))
      },
      "compliantValues": [
        string
      ],
      "remediationType": enum ([RemediationType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#RemediationType))
    }  
  
Fields  
---  
`instructions` |  `object (`[Instructions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#Instructions)`)` Required. Remediation instructions to resolve violations  
`compliantValues[]` |  `string` Values that can resolve the violation For example: for list org policy violations, this will either be the list of allowed or denied values  
`remediationType` |  `enum (`[RemediationType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#RemediationType)`)` Output only. Reemediation type based on the type of org policy values violated  
  
## Instructions

Instructions to remediate violation

JSON representation  
---  
      
    
    {
      "gcloudInstructions": {
        object ([Gcloud](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#Gcloud))
      },
      "consoleInstructions": {
        object ([Console](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#Console))
      }
    }  
  
Fields  
---  
`gcloudInstructions` |  `object (`[Gcloud](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#Gcloud)`)` Remediation instructions to resolve violation via gcloud cli  
`consoleInstructions` |  `object (`[Console](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations#Console)`)` Remediation instructions to resolve violation via cloud console  
  
## Gcloud

Remediation instructions to resolve violation via gcloud cli

JSON representation  
---  
      
    
    {
      "gcloudCommands": [
        string
      ],
      "steps": [
        string
      ],
      "additionalLinks": [
        string
      ]
    }  
  
Fields  
---  
`gcloudCommands[]` |  `string` Gcloud command to resolve violation  
`steps[]` |  `string` Steps to resolve violation via gcloud cli  
`additionalLinks[]` |  `string` Additional urls for more information about steps  
  
## Console

Remediation instructions to resolve violation via cloud console

JSON representation  
---  
      
    
    {
      "consoleUris": [
        string
      ],
      "steps": [
        string
      ],
      "additionalLinks": [
        string
      ]
    }  
  
Fields  
---  
`consoleUris[]` |  `string` Link to console page where violations can be resolved  
`steps[]` |  `string` Steps to resolve violation via cloud console  
`additionalLinks[]` |  `string` Additional urls for more information about steps  
  
## RemediationType

Classifying remediation into various types based on the kind of violation. For example, violations caused due to changes in boolean org policy requires different remediation instructions compared to violation caused due to changes in allowed values of list org policy.

Enums  
---  
`REMEDIATION_TYPE_UNSPECIFIED` | Unspecified remediation type  
`REMEDIATION_BOOLEAN_ORG_POLICY_VIOLATION` | Remediation type for boolean org policy  
`REMEDIATION_LIST_ALLOWED_VALUES_ORG_POLICY_VIOLATION` | Remediation type for list org policy which have allowed values in the monitoring rule  
`REMEDIATION_LIST_DENIED_VALUES_ORG_POLICY_VIOLATION` | Remediation type for list org policy which have denied values in the monitoring rule  
`REMEDIATION_RESTRICT_CMEK_CRYPTO_KEY_PROJECTS_ORG_POLICY_VIOLATION` | Remediation type for gcp.restrictCmekCryptoKeyProjects  
`REMEDIATION_RESOURCE_VIOLATION` | Remediation type for resource violation.  
`REMEDIATION_RESOURCE_VIOLATION_NON_CMEK_SERVICES` | Remediation type for resource violation due to gcp.restrictNonCmekServices  
  
## ExceptionContext

Violation exception detail.

JSON representation  
---  
      
    
    {
      "comment": string,
      "acknowledgementTime": string,
      "userName": string
    }  
  
Fields  
---  
`comment` |  `string` Business justification provided towards the acknowledgement of the violation.  
`acknowledgementTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the violation was acknowledged.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`userName` |  `string` Name of the user (or service account) who acknowledged the violation.  
  
## ViolationType

Violation Type Values

Enums  
---  
`VIOLATION_TYPE_UNSPECIFIED` | Unspecified type.  
`ORG_POLICY` | Org Policy Violation.  
`RESOURCE` | Resource Violation.  
  
## Methods  
  
---  
  
### `[acknowledge](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/acknowledge)`

|  Acknowledges an existing violation.  
  
### `[get](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/get)`

|  Retrieves Assured Workload Violation based on ID.  
  
### `[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/list)`

|  Lists the Violations in the AssuredWorkload Environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-27 UTC."],[],[]] 
