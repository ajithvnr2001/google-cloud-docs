---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/restrictAllowedResources/
title: Method: organizations.locations.workloads.restrictAllowedResources \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:26.269959+00:00
---

# Method: organizations.locations.workloads.restrictAllowedResources  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/restrictAllowedResources/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  Method: organizations.locations.workloads.restrictAllowedResources Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * RestrictionType



Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

### HTTP request

`POST https://{endpoint}/v1beta1/{name=organizations/*/locations/*/workloads/*}:restrictAllowedResources`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the Workload. This is the workloads's relative path in the API, formatted as "organizations/{organization_id}/locations/{locationId}/workloads/{workload_id}". For example, "organizations/123/locations/us-east1/workloads/assured-workload-1".  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "restrictionType": enum ([RestrictionType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/restrictAllowedResources#RestrictionType))
    }  
  
Fields  
---  
`restrictionType` |  `enum (`[RestrictionType](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/restrictAllowedResources#RestrictionType)`)` Required. The type of restriction for using gcp products in the Workload environment.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `assuredworkloads.workload.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## RestrictionType

The type of restriction.

Enums  
---  
`RESTRICTION_TYPE_UNSPECIFIED` | Unknown restriction type.  
`ALLOW_ALL_GCP_RESOURCES` | Allow the use all of all gcp products, irrespective of the compliance posture. This effectively removes gcp.restrictServiceUsage OrgPolicy on the AssuredWorkloads Folder.  
`ALLOW_COMPLIANT_RESOURCES` | Based on Workload's compliance regime, allowed list changes. See - <https://cloud.google.com/assured-workloads/docs/supported-products> for the list of supported resources.  
`APPEND_COMPLIANT_RESOURCES` | Similar to ALLOW_COMPLIANT_RESOURCES but adds the list of compliant resources to the existing list of compliant resources. Effective org-policy of the Folder is considered to ensure there is no disruption to the existing customer workflows.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
