---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.assets.actions/list/
title: Method: projects.locations.lakes.zones.assets.actions.list \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:15.954913+00:00
---

# Method: projects.locations.lakes.zones.assets.actions.list  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones.assets.actions/list/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.lakes.zones.assets.actions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists action resources in an asset.

### HTTP request

`GET https://dataplex.googleapis.com/v1/{parent=projects/*/locations/*/lakes/*/zones/*/assets/*}/actions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the parent asset: `projects/{projectNumber}/locations/{locationId}/lakes/{lakeId}/zones/{zoneId}/assets/{assetId}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dataplex.assetActions.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of actions to return. The service may return fewer than this value. If unspecified, at most 10 actions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. Page token received from a previous `actions.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `actions.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListActionsResponse](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/ListActionsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`
  * ` https://www.googleapis.com/auth/dataplex.read-write`
  * ` https://www.googleapis.com/auth/dataplex.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
