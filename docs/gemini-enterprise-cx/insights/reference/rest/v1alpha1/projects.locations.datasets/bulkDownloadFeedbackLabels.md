---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/bulkDownloadFeedbackLabels/
title: Method: projects.locations.datasets.bulkDownloadFeedbackLabels \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:19:02.161291+00:00
---

# Method: projects.locations.datasets.bulkDownloadFeedbackLabels  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.datasets/bulkDownloadFeedbackLabels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.datasets.bulkDownloadFeedbackLabels Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Download feedback labels in bulk from an external source. Currently supports exporting Quality AI example conversations with transcripts and question bodies.

### HTTP request

`POST https://{endpoint}/v1alpha1/{parent=projects/*/locations/*/datasets/*}:bulkDownloadFeedbackLabels`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource for new feedback labels.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": string,
      "maxDownloadCount": integer,
      "feedbackLabelType": enum ([FeedbackLabelType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/FeedbackLabelType)),
      "conversationFilter": string,
      "templateQaScorecardId": [
        string
      ],
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/GcsDestination))
      },
      "sheetsDestination": {
        object ([SheetsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SheetsDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
`filter` |  `string` Optional. A filter to reduce results to a specific subset. Supports disjunctions (OR) and conjunctions (AND).Supported fields:

  * `issueModelId`
  * `qaQuestionId`
  * `qaScorecardId`
  * `min_create_time`
  * `max_create_time`
  * `min_update_time`
  * `max_update_time`
  * `feedbackLabelType`: QUALITY_AI, TOPIC_MODELING

  
`maxDownloadCount` |  `integer` Optional. Limits the maximum number of feedback labels that will be downloaded. The first `N` feedback labels will be downloaded.  
`feedbackLabelType` |  `enum (`[FeedbackLabelType](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/FeedbackLabelType)`)` Optional. The type of feedback labels that will be downloaded.  
`conversationFilter` |  `string` Optional. Filter parent conversations to download feedback labels for. When specified, the feedback labels will be downloaded for the conversations that match the filter. If `templateQaScorecardId` is set, all the conversations that match the filter will be paired with the questions under the scorecard for labeling.  
`templateQaScorecardId[]` |  `string` Optional. If set, a template for labeling conversations and scorecard questions will be created from the conversationFilter and the questions under the scorecard(s). The feedback label `filter` will be ignored.  
Union field `destination`. Configuration for an external data store to which the feedback labels will be written to. `destination` can be only one of the following:  
`gcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/GcsDestination)`)` A cloud storage bucket destination.  
`sheetsDestination` |  `object (`[SheetsDestination](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SheetsDestination)`)` A sheets document destination.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.download`
  * `contactcenterinsights.feedbackLabels.download`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
