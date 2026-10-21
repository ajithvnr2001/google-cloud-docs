---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/list/
title: Method: projects.locations.privateClouds.subnets.list \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:22:23.356176+00:00
---

# Method: projects.locations.privateClouds.subnets.list  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  Method: projects.locations.privateClouds.subnets.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists subnets in a given private cloud.

### HTTP request

`GET https://vmwareengine.googleapis.com/v1/{parent=projects/*/locations/*/privateClouds/*}/subnets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the private cloud to be queried for subnets. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `vmwareengine.subnets.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of subnets to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.  
`pageToken` |  `string` A page token, received from a previous `ListSubnetsRequest` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListSubnetsRequest` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[VmwareEngine.ListSubnets](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets/list#google.cloud.vmwareengine.v1.VmwareEngine.ListSubnets)`

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "subnets": [
        {
          object ([Subnet](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets#Subnet))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`subnets[]` |  `object (`[Subnet](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateClouds.subnets#Subnet)`)` A list of subnets.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Locations that could not be reached when making an aggregated query using wildcards.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
