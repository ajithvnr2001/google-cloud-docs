---
url: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/assets/list/
title: Method: assets.list \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:04.425545+00:00
---

# Method: assets.list  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/assets/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Reference ](https://docs.cloud.google.com/asset-inventory/docs/asset-types)



Send feedback 

#  Method: assets.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists assets with time and resource types and returns paged results in response.

### HTTP request

`GET https://cloudasset.googleapis.com/v1/{parent=*/*}/assets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the organization, folder, or project the assets belong to. Format: "organizations/[organization-number]" (such as "organizations/123"), "projects/[project-id]" (such as "projects/my-project-id"), "projects/[project-number]" (such as "projects/12345"), or "folders/[folder-number]" (such as "folders/12345"). Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `cloudasset.assets.listResource`
  * `cloudasset.assets.listIamPolicy`
  * `cloudasset.assets.listOrgPolicy`
  * `cloudasset.assets.listAccessPolicy`
  * `cloudasset.assets.listOSInventories`

  
  
### Query parameters

Parameters  
---  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`assetTypes[]` |  `string` A list of asset types to take a snapshot for. For example: "compute.googleapis.com/Disk".Regular expression is also supported. For example:

  * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
  * ".*Instance" snapshots resources whose asset type ends with "Instance".
  * ".*Instance.*" snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types.  
`contentType` |  `enum (`[ContentType](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/feeds#ContentType)`)` Asset content type. If not specified, no content but the asset name will be returned.  
`pageSize` |  `integer` The maximum number of assets to be returned in a single response. Default is 100, minimum is 1, and maximum is 1000.  
`pageToken` |  `string` The `nextPageToken` returned from the previous `ListAssetsResponse`, or unspecified for the first `ListAssetsRequest`. It is a continuation of a prior `assets.list` call, and the API should return the next page of assets.  
`relationshipTypes[]` |  `string` A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if contentType=RELATIONSHIP. * If specified: it snapshots specified relationships. It returns an error if any of the [relationshipTypes] doesn't belong to the supported relationship types of the [assetTypes] or if any of the [assetTypes] doesn't belong to the source types of the [relationshipTypes]. * Otherwise: it snapshots the supported relationships for all [assetTypes] or returns an error if any of the [assetTypes] has no relationship support. An unspecified asset types field means all supported assetTypes. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.  
  
### Request body

The request body must be empty.

### Response body

assets.list response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "readTime": string,
      "assets": [
        {
          object ([Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`readTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time the snapshot was taken.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`assets[]` |  `object (`[Asset](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/Asset)`)` Assets.  
`nextPageToken` |  `string` Token to retrieve the next page of results. It expires 72 hours after the page token for the first page is generated. Set to empty if there are no remaining results.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
