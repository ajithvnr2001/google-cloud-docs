---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/resources/searchAll/
title: Method: resources.searchAll \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:07.081268+00:00
---

# Method: resources.searchAll  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/resources/searchAll/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: resources.searchAll Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * StandardResourceMetadata
    * JSON representation
  * Try it!



Searches all the resources within a given accessible Resource Manager scope (project/folder/organization). This RPC gives callers especially administrators the ability to search all the resources within a scope, even if they don't have `.get` permission of all the resources. Callers should have `cloudasset.assets.searchAllResources` permission on the requested scope, otherwise the request will be rejected.

### HTTP request

`GET https://cloudasset.googleapis.com/v1p1beta1/{scope=*/*}/resources:searchAll`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`scope` |  `string` Required. The relative name of an asset. The search is limited to the resources within the `scope`. The allowed value must be:

  * Organization number (such as "organizations/123")
  * Folder number (such as "folders/1234")
  * Project number (such as "projects/12345")
  * Project ID (such as "projects/abc")

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scope`:

  * `cloudasset.assets.searchAllResources`

  
  
### Query parameters

Parameters  
---  
`query` |  `string` Optional. The query statement.  
`assetTypes[]` |  `string` Optional. A list of asset types that this request searches for. If empty, it will search all the supported asset types.  
`pageSize` |  `integer` Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `nextPageToken` is returned.  
`pageToken` |  `string` Optional. If present, then retrieve the next batch of results from the preceding call to this method. `pageToken` must be the value of `nextPageToken` from the previous response. The values of all other method parameters, must be identical to those in the previous call.  
`orderBy` |  `string` Optional. A comma separated list of fields specifying the sorting order of the results. The default order is ascending. Add `DESC` after the field name to indicate descending order. Redundant space characters are ignored. For example, `location DESC , name`.  
  
### Request body

The request body must be empty.

### Response body

Search all resources response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([StandardResourceMetadata](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/resources/searchAll#StandardResourceMetadata))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`results[]` |  `object (`[StandardResourceMetadata](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1p1beta1/resources/searchAll#StandardResourceMetadata)`)` A list of resource that match the search query.  
`nextPageToken` |  `string` If there are more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## StandardResourceMetadata

The standard metadata of a cloud resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "assetType": string,
      "project": string,
      "displayName": string,
      "description": string,
      "additionalAttributes": [
        string
      ],
      "location": string,
      "labels": {
        string: string,
        ...
      },
      "networkTags": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` The full resource name. For example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See [Resource Names](https://cloud.google.com/apis/design/resource_names#full_resource_name) for more information.  
`assetType` |  `string` The type of this resource. For example: "compute.googleapis.com/Disk".  
`project` |  `string` The project that this resource belongs to, in the form of `projects/{projectNumber}`.  
`displayName` |  `string` The display name of this resource.  
`description` |  `string` One or more paragraphs of text description of this resource. Maximum length could be up to 1M bytes.  
`additionalAttributes[]` |  `string` Additional searchable attributes of this resource. Informational only. The exact set of attributes is subject to change. For example: project id, DNS name etc.  
`location` |  `string` Location can be "global", regional like "us-east1", or zonal like "us-west1-b".  
`labels` |  `map (key: string, value: string)` Labels associated with this resource. See [Labelling and grouping Google Cloud resources](https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`networkTags[]` |  `string` Network tags associated with this resource. Like labels, network tags are a type of annotations used to group Google Cloud resources. See [Labelling Google Cloud resources](lhttps://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources) for more information.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-30 UTC."],[],[]] 
