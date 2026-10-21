---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes/list/
title: Method: projects.locations.nodeTypes.list \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:37:14.613472+00:00
---

# Method: projects.locations.nodeTypes.list  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  Method: projects.locations.nodeTypes.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists node types

### HTTP request

`GET https://vmwareengine.googleapis.com/v1/{parent=projects/*/locations/*}/nodeTypes`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the location to be queried for node types. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-central1-a` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `vmwareengine.nodeTypes.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of node types to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.  
`pageToken` |  `string` A page token, received from a previous `nodeTypes.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `nodeTypes.list` must match the call that provided the page token.  
`filter` |  `string` A filter expression that matches resources returned in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be `=`, `!=`, `>`, or `<`.For example, if you are filtering a list of node types, you can exclude the ones named `standard-72` by specifying `name != "standard-72"`.To filter on multiple expressions, provide each separate expression within parentheses. For example:
    
    
    (name = "standard-72")
    (virtualCpuCount > 2)
    

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example:
    
    
    (name = "standard-96") AND
    (virtualCpuCount > 2) OR
    (name = "standard-72")
      
  
### Request body

The request body must be empty.

### Response body

Response message for `[VmwareEngine.ListNodeTypes](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes/list#google.cloud.vmwareengine.v1.VmwareEngine.ListNodeTypes)`

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "nodeTypes": [
        {
          object ([NodeType](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes#NodeType))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`nodeTypes[]` |  `object (`[NodeType](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes#NodeType)`)` A list of Node Types.  
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
