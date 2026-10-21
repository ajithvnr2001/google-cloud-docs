---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/listAllFeedbackLabels/
title: Method: projects.locations.listAllFeedbackLabels \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:57.532152+00:00
---

# Method: projects.locations.listAllFeedbackLabels  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/listAllFeedbackLabels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.listAllFeedbackLabels Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



List all feedback labels by project number.

### HTTP request

`GET https://{endpoint}/v1/{parent=projects/*/locations/*}:listAllFeedbackLabels`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of all feedback labels per project.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of feedback labels to return in the response. A valid page size ranges from 0 to 100,000 inclusive. If the page size is zero or unspecified, a default page size of 100 will be chosen. Note that a call might return fewer results than the requested page size.  
`pageToken` |  `string` Optional. The value returned by the last `ListAllFeedbackLabelsResponse`. This value indicates that this is a continuation of a prior `locations.listAllFeedbackLabels` call and that the system should return the next page of data.  
`filter` |  `string` Optional. A filter to reduce results to a specific subset in the entire project. Supports disjunctions (OR) and conjunctions (AND).Supported fields:

  * `issueModelId`
  * `qaQuestionId`
  * `min_create_time`
  * `max_create_time`
  * `min_update_time`
  * `max_update_time`
  * `feedbackLabelType`: QUALITY_AI, TOPIC_MODELING

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListAllFeedbackLabelsResponse](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/ListAllFeedbackLabelsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.list`
  * `contactcenterinsights.datasetFeedbackLabels.list`
  * `contactcenterinsights.feedbackLabels.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
