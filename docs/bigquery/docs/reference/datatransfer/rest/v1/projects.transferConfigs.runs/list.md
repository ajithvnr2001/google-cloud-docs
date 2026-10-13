---
url: https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.transferConfigs.runs/list/
title: Method: runs.list \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:08.932707+00:00
---

# Method: runs.list  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.transferConfigs.runs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback 

#  Method: runs.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



**Full name** : projects.transferConfigs.runs.list

Returns information about running and completed transfer runs.

### HTTP request

Choose an endpoint:

globalasia-south1asia-south2europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central2northamerica-northeast1northamerica-northeast2us-central1us-central2us-east1us-east4us-east5us-east7us-south1us-west1us-west2us-west3us-west4us-west8

  
`GET https://bigquerydatatransfer.googleapis.com/v1/{parent=projects/*/transferConfigs/*}/runs`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of transfer configuration for which transfer runs should be retrieved. If you are using the regionless method, the location must be `US` and the name should be in the following form:

  * `projects/{projectId}/transferConfigs/{configId}`

If you are using the regionalized method, the name should be in the following form:

  * `projects/{projectId}/locations/{locationId}/transferConfigs/{configId}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `bigquery.transfers.get`

  
  
### Query parameters

Parameters  
---  
`states[]` |  `enum (`[TransferState](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/TransferState)`)` When specified, only transfer runs with requested states are returned.  
`pageToken` |  `string` Pagination token, which can be used to request a specific page of `ListTransferRunsRequest` list results. For multiple-page results, `ListTransferRunsResponse` outputs a `next_page` token, which can be used as the `pageToken` value to request the next page of list results.  
`pageSize` |  `integer` Page size. The default page size is the maximum value of 1000 results.  
`runAttempt` |  `enum (`[RunAttempt](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/RunAttempt)`)` Indicates how run attempts are to be pulled.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListTransferRunsResponse](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/ListTransferRunsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-11 UTC."],[],[]] 
