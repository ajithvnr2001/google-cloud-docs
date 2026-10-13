---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.answerRecords/list/
title: Method: projects.locations.answerRecords.list \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:00.007326+00:00
---

# Method: projects.locations.answerRecords.list  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.answerRecords/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.locations.answerRecords.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Returns the list of all answer records in the specified project in reverse chronological order.

### HTTP request

`GET https://{endpoint}/v2beta1/{parent=projects/*/locations/*}/answerRecords`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project to list all answer records for in reverse chronological order. Format: `projects/<Project ID>/locations/<Location ID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.answerrecords.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. Filters to restrict results to specific answer records. The expression has the following syntax: [AND ] ...The following fields and operators are supported: * conversationId with equals(=) operatorExamples:

  * "conversationId=bar" matches answer records in the projects/foo/locations/global/conversations/bar conversation (assuming the parent is projects/foo/locations/global).

For more information about filtering, see [API Filtering](https://aip.dev/160).  
`pageSize` |  `integer` Optional. The maximum number of records to return in a single page. The server may return fewer records than this. If unspecified, we use 10. The maximum is 100.  
`pageToken` |  `string` Optional. The `[ListAnswerRecordsResponse.next_page_token](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ListAnswerRecordsResponse#FIELDS.next_page_token)` value returned from a previous list request used to continue listing on the next page.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListAnswerRecordsResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ListAnswerRecordsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
