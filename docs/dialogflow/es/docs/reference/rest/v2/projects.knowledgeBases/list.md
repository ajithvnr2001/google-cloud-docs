---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases/list/
title: Method: projects.knowledgeBases.list \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:27.353522+00:00
---

# Method: projects.knowledgeBases.list  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.knowledgeBases/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.knowledgeBases.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Returns the list of all knowledge bases of the specified agent.

### HTTP request

`GET https://{endpoint}/v2/{parent=projects/*}/knowledgeBases`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project to list of knowledge bases for. Format: `projects/<Project ID>/locations/<Location ID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dialogflow.knowledgeBases.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return in a single page. By default 10 and at most 100.  
`pageToken` |  `string` The nextPageToken value returned from a previous list request.  
`filter` |  `string` The filter expression used to filter knowledge bases returned by the list method. The expression has the following syntax: [AND ] ...The following fields and operators are supported:

  * displayName with has(:) operator
  * languageCode with equals(=) operator

Examples:

  * 'languageCode=en-us' matches knowledge bases with en-us language code.
  * 'displayName:articles' matches knowledge bases whose display name contains "articles".
  * 'displayName:"Best Articles"' matches knowledge bases whose display name contains "Best Articles".
  * 'languageCode=en-gb AND displayName=articles' matches all knowledge bases whose display name contains "articles" and whose language code is "en-gb".

Note: An empty filter string (i.e. "") is a no-op and will result in no filtering.For more information about filtering, see [API Filtering](https://aip.dev/160).  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListKnowledgeBasesResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ListKnowledgeBasesResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
