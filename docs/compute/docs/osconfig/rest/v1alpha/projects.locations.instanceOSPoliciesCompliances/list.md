---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances/list/
title: Method: projects.locations.instanceOSPoliciesCompliances.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:21.538623+00:00
---

# Method: projects.locations.instanceOSPoliciesCompliances.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: projects.locations.instanceOSPoliciesCompliances.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



ListInstanceOSPoliciesCompliances is deprecated. Instead, use ListOSPolicyAssignmentReports.

List OS policies compliance data for all Compute Engine VM instances in the specified zone.

### HTTP request

`GET https://osconfig.googleapis.com/v1alpha/{parent=projects/*/locations/*}/instanceOSPoliciesCompliances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name.Format: `projects/{project}/locations/{location}`For `{project}`, either Compute Engine project-number or project-id can be provided.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of results to return.  
`pageToken` |  `string` A pagination token returned from a previous call to `instanceOSPoliciesCompliances.list` that indicates where this listing should continue from.  
`filter` |  `string` If provided, this field specifies the criteria that must be met by a `InstanceOSPoliciesCompliance` API resource to be included in the response.  
  
### Request body

The request body must be empty.

### Response body

This item is deprecated!

A response message for listing OS policies compliance data for all Compute Engine VMs in the given location.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instanceOsPoliciesCompliances": [
        {
          object ([InstanceOSPoliciesCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#InstanceOSPoliciesCompliance))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`instanceOsPoliciesCompliances[]` |  `object (`[InstanceOSPoliciesCompliance](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances#InstanceOSPoliciesCompliance)`)` List of instance OS policies compliance objects.  
`nextPageToken` |  `string` The pagination token to retrieve the next page of instance OS policies compliance objects.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
