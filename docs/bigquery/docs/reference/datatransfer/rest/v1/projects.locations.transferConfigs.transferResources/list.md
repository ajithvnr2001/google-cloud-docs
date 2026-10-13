---
url: https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs.transferResources/list/
title: Method: transferResources.list \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:55.600989+00:00
---

# Method: transferResources.list  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs.transferResources/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback 

#  Method: transferResources.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



**Full name** : projects.locations.transferConfigs.transferResources.list

Returns information about transfer resources.

### HTTP request

Choose an endpoint:

globalasia-south1asia-south2europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central2northamerica-northeast1northamerica-northeast2us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`GET https://bigquerydatatransfer.googleapis.com/v1/{parent=projects/*/locations/*/transferConfigs/*}/transferResources`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of transfer configuration for which transfer resources should be retrieved. The name should be in one of the following forms:

  * `projects/{project}/transferConfigs/{transferConfig}`
  * `projects/{project}/locations/{locationId}/transferConfigs/{transferConfig}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `bigquery.transfers.get`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of transfer resources to return. The maximum value is 1000; values above 1000 will be coerced to 1000. The default page size is the maximum value of 1000 results.  
`pageToken` |  `string` Optional. A page token, received from a previous `transferResources.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `transferResources.list` must match the call that provided the page token.  
`filter` |  `string` Optional. Filter for the transfer resources. Currently supported filters include:

  * Resource name: `name` \- Wildcard supported
  * Resource type: `type`
  * Resource destination: `destination`
  * Latest resource state: `latest_status_detail.state`
  * Last update time: `update_time` \- RFC-3339 format
  * Parent table name: `hierarchy_detail.partition_detail.table`

Multiple filters can be applied using the `AND/OR` operator.Examples:

  * `name="*123" AND (type="TABLE" OR latest_status_detail.state="SUCCEEDED")`
  * `update_time >= "2012-04-21T11:30:00-04:00"`
  * `hierarchy_detail.partition_detail.table = "table1"`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListTransferResourcesResponse](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/ListTransferResourcesResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-11 UTC."],[],[]] 
