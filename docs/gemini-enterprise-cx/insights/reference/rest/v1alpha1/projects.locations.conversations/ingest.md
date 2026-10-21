---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/ingest/
title: Method: projects.locations.conversations.ingest \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:40:06.675588+00:00
---

# Method: projects.locations.conversations.ingest  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/ingest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.conversations.ingest Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Imports conversations and processes them according to the user's configuration.

### HTTP request

`POST https://{endpoint}/v1alpha1/{parent=projects/*/locations/*}/conversations:ingest`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource for new conversations.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "conversationConfig": {
        object ([ConversationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/ConversationConfig))
      },
      "redactionConfig": {
        object ([RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/RedactionConfig))
      },
      "speechConfig": {
        object ([SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SpeechConfig))
      },
    
      // Union field source can be only one of the following:
      "gcsSource": {
        object (GcsSource)
      }
      // End of list of possible types for union field source.
    
      // Union field object_config can be only one of the following:
      "transcriptObjectConfig": {
        object ([TranscriptObjectConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/TranscriptObjectConfig))
      }
      // End of list of possible types for union field object_config.
      "sampleSize": integer
    }  
  
Fields  
---  
`conversationConfig` |  `object (`[ConversationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/ConversationConfig)`)` Configuration that applies to all conversations.  
`redactionConfig` |  `object (`[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/RedactionConfig)`)` Optional. DLP settings for transcript redaction. Optional, will default to the config specified in Settings.  
`speechConfig` |  `object (`[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SpeechConfig)`)` Optional. Default Speech-to-Text configuration. Optional, will default to the config specified in Settings.  
Union field `source`. Configuration for an external data store containing objects that will be converted to conversations. `source` can be only one of the following:  
`gcsSource` |  `object (`GcsSource`)` A cloud storage bucket source. Note that any previously ingested objects from the source will be skipped to avoid duplication.  
Union field `object_config`. Configuration for converting individual `source` objects to conversations. `object_config` can be only one of the following:  
`transcriptObjectConfig` |  `object (`[TranscriptObjectConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/TranscriptObjectConfig)`)` Configuration for when `source` contains conversation transcripts.  
`sampleSize` |  `integer` Optional. If set, this fields indicates the number of objects to ingest from the Cloud Storage bucket. If empty, the entire bucket will be ingested. Unless they are first deleted, conversations produced through sampling won't be ingested by subsequent ingest requests.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.datasetConversations.create`
  * `contactcenterinsights.conversations.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
