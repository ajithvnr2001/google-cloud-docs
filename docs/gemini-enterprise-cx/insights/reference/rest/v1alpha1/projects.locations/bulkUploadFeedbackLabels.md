---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/bulkUploadFeedbackLabels/
title: Method: projects.locations.bulkUploadFeedbackLabels \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:57:45.434902+00:00
---

# Method: projects.locations.bulkUploadFeedbackLabels  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations/bulkUploadFeedbackLabels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.bulkUploadFeedbackLabels Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Upload feedback labels from an external source in bulk. Currently supports labeling Quality AI example conversations.

### HTTP request

`POST https://{endpoint}/v1alpha1/{parent=projects/*/locations/*}:bulkUploadFeedbackLabels`

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
      "validateOnly": boolean,
    
      // Union field source can be only one of the following:
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/GcsSource))
      },
      "sheetsSource": {
        object ([SheetsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SheetsSource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`validateOnly` |  `boolean` Optional. If set, upload will not happen and the labels will be validated. If not set, then default behavior will be to upload the labels after validation is complete.  
Union field `source`. Configuration for an external data store containing objects that will be converted to FeedbackLabels. `source` can be only one of the following:  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/GcsSource)`)` A cloud storage bucket source.  
`sheetsSource` |  `object (`[SheetsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SheetsSource)`)` A sheets document source.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedFeedbackLabels.upload`
  * `contactcenterinsights.feedbackLabels.upload`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
