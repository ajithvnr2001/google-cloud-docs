---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/acknowledge/
title: Method: organizations.locations.workloads.violations.acknowledge \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:30.117772+00:00
---

# Method: organizations.locations.workloads.violations.acknowledge  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/acknowledge/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  Method: organizations.locations.workloads.violations.acknowledge Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * AcknowledgeType



Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted.

### HTTP request

`POST https://{endpoint}/v1/{name=organizations/*/locations/*/workloads/*/violations/*}:acknowledge`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Violation to acknowledge. Format: organizations/{organization}/locations/{location}/workloads/{workload}/violations/{violation}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "comment": string,
      "nonCompliantOrgPolicy": string,
      "acknowledgeType": enum ([AcknowledgeType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/acknowledge#AcknowledgeType))
    }  
  
Fields  
---  
`comment` |  `string` Required. Business justification explaining the need for violation acknowledgement  
`nonCompliantOrgPolicy  
**(deprecated)**` |  `string` Optional. This field is deprecated and will be removed in future version of the API. Name of the OrgPolicy which was modified with non-compliant change and resulted in this violation. Format: projects/{project_number}/policies/{constraintName} folders/{folderId}/policies/{constraintName} organizations/{organization_id}/policies/{constraintName}  
`acknowledgeType` |  `enum (`[AcknowledgeType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/acknowledge#AcknowledgeType)`)` Optional. Acknowledge type of specified violation.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `assuredworkloads.violations.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AcknowledgeType

Acknowledge type values.

Enums  
---  
`ACKNOWLEDGE_TYPE_UNSPECIFIED` | Acknowledge type unspecified.  
`SINGLE_VIOLATION` | Acknowledge only the specific violation.  
`EXISTING_CHILD_RESOURCE_VIOLATIONS` | Acknowledge specified orgPolicy violation and also associated resource violations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-27 UTC."],[],[]] 
