---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/list/
title: Method: projects.locations.orders.hardwareGroups.list \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:38.367742+00:00
---

# Method: projects.locations.orders.hardwareGroups.list  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups/list/




#  Method: projects.locations.orders.hardwareGroups.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists hardware groups in a given order.

### HTTP request

`GET https://gdchardwaremanagement.googleapis.com/v1alpha/{parent=projects/*/locations/*/orders/*}/hardwareGroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The order to list hardware groups in. Format: `projects/{project}/locations/{location}/orders/{order}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering condition. See [AIP-160](https://google.aip.dev/160).  
`orderBy` |  `string` Optional. Hint for how to order the results.  
  
### Request body

The request body must be empty.

### Response body

A list of hardware groups.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "hardwareGroups": [
        {
          object ([HardwareGroup](https://docs.cloud.google.com/distributed-cloud/edge/1.10.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups#HardwareGroup))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`hardwareGroups[]` |  `object (`[HardwareGroup](https://docs.cloud.google.com/distributed-cloud/edge/1.10.0/docs/reference/hardware/rest/v1alpha/projects.locations.orders.hardwareGroups#HardwareGroup)`)` The list of hardware groups.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `gdchardwaremanagement.hardwareGroups.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
