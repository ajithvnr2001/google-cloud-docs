---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/upload/
title: Method: projects.locations.conversations.upload \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:07:30.922536+00:00
---

# Method: projects.locations.conversations.upload  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.conversations.upload Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Create a long-running conversation upload operation. This method differs from `conversations.create` by allowing audio transcription and optional DLP redaction.

### HTTP request

`POST https://{endpoint}/v1alpha1/{parent=projects/*/locations/*}/conversations:upload`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the conversation.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "conversation": {
        object ([Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation))
      },
      "conversationId": string,
      "redactionConfig": {
        object ([RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/RedactionConfig))
      },
      "speechConfig": {
        object ([SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SpeechConfig))
      }
    }  
  
Fields  
---  
`conversation` |  `object (`[Conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation)`)` Required. The conversation resource to create.  
`conversationId` |  `string` Optional. A unique ID for the new conversation. This ID will become the final component of the conversation's resource name. If no ID is specified, a server-generated ID will be used.This value should be 4-64 characters and must match the regular expression `^[a-z0-9-]{4,64}$`. Valid characters are `[a-z][0-9]-`  
`redactionConfig` |  `object (`[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/RedactionConfig)`)` Optional. DLP settings for transcript redaction. Will default to the config specified in Settings.  
`speechConfig` |  `object (`[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SpeechConfig)`)` Optional. Speech-to-Text configuration. Will default to the config specified in Settings.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedConversations.upload`
  * `contactcenterinsights.datasetConversations.upload`
  * `contactcenterinsights.conversations.upload`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
