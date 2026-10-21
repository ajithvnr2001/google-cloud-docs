---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/list/
title: Method: feedbackEntries.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:55:28.450366+00:00
---

# Method: feedbackEntries.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: feedbackEntries.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.reasoningEngines.feedbackEntries.list

Lists FeedbackEntries in a ReasoningEngine.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/feedbackEntries`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the ReasoningEngine from which to list FeedbackEntries.Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}`

### Query parameters

| `pageSize` `integer` Optional. The maximum number of FeedbackEntries to return per page. | `pageToken` `string` Optional. A page token, received from a previous feedbackEntries.list call. | `filter` `string` Optional. Standard list filter.Supported fields:

  * `sessionId`
  * `userId`
  * `feedbackType`
  * `feedbackLabels`: Supports the HAS operator (`:`). For example: `feedbackLabels:"inaccurate"`.
  * `createTime`
  * `updateTime`

Example: `feedbackType="THUMBS_DOWN" AND feedbackLabels:"hallucination"`. | `orderBy` `string` Optional. A comma-separated list of fields to order results by, sorted in ascending order by default. Append `desc` after a field name to sort that field in descending order.Supported fields:

  * `createTime`
  * `updateTime`

Example: `createTime desc`.

### Request body

The request body must be empty.

### Response body

Response message for feedbackEntries.list. If successful, the response body contains data with the following structure: | Fields  
  
`feedbackEntries[]` `object (`[FeedbackEntry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries#FeedbackEntry)`)` The page of FeedbackEntries matching the request. | `nextPageToken` `string` A token to retrieve the next page. Absence of this field indicates there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "feedbackEntries": [
        {
          object ([FeedbackEntry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries#FeedbackEntry))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
