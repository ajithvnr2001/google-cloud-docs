---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Settings/
title: Settings \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:49:37.904588+00:00
---

# Settings  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Settings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AnalysisConfig
    * JSON representation



The CCAI Insights project wide settings. Use these settings to configure the behavior of Insights. View these settings with [`getsettings`](https://cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/getSettings) and change the settings with [`updateSettings`](https://cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations/updateSettings).

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "languageCode": string,
      "conversationTtl": string,
      "pubsubNotificationSettings": {
        string: string,
        ...
      },
      "analysisConfig": {
        object ([AnalysisConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Settings#AnalysisConfig))
      },
      "redactionConfig": {
        object ([RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/RedactionConfig))
      },
      "speechConfig": {
        object ([SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SpeechConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the settings resource. Format: projects/{project}/locations/{location}/settings  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the settings was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the settings were last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`languageCode` |  `string` A language code to be applied to each transcript segment unless the segment already specifies a language code. Language code defaults to "en-US" if it is neither specified on the segment nor here.  
`conversationTtl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The default TTL for newly-created conversations. If a conversation has a specified expiration, that value will be used instead. Changing this value will not change the expiration of existing conversations. Conversations with no expire time persist until they are deleted.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`pubsubNotificationSettings` |  `map (key: string, value: string)` A map that maps a notification trigger to a Pub/Sub topic. Each time a specified trigger occurs, Insights will notify the corresponding Pub/Sub topic.Keys are notification triggers. Supported keys are:

  * "all-triggers": Notify each time any of the supported triggers occurs.
  * "create-analysis": Notify each time an analysis is created.
  * "create-conversation": Notify each time a conversation is created.
  * "export-insights-data": Notify each time an export is complete.
  * "ingest-conversations": Notify each time an IngestConversations LRO is complete.
  * "update-conversation": Notify each time a conversation is updated via UpdateConversation.
  * "upload-conversation": Notify when an UploadConversation LRO is complete.

Values are Pub/Sub topics. The format of each Pub/Sub topic is: projects/{project}/topics/{topic}An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`analysisConfig` |  `object (`[AnalysisConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Settings#AnalysisConfig)`)` Default analysis settings.  
`redactionConfig` |  `object (`[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/RedactionConfig)`)` Default DLP redaction resources to be applied while ingesting conversations. This applies to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversations coming from CCAI Platform.  
`speechConfig` |  `object (`[SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SpeechConfig)`)` Optional. Default Speech-to-Text resources to use while ingesting audio files. Optional, CCAI Insights will create a default if not provided. This applies to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversations coming from CCAI Platform.  
  
## AnalysisConfig

Default configuration when creating Analyses in Insights.

JSON representation  
---  
      
    
    {
      "runtimeIntegrationAnalysisPercentage": number,
      "uploadConversationAnalysisPercentage": number,
      "annotatorSelector": {
        object ([AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotatorSelector))
      }
    }  
  
Fields  
---  
`runtimeIntegrationAnalysisPercentage` |  `number` Percentage of conversations created using Dialogflow runtime integration to analyze automatically, between [0, 100].  
`uploadConversationAnalysisPercentage` |  `number` Percentage of conversations created using the UploadConversation endpoint to analyze automatically, between [0, 100].  
`annotatorSelector` |  `object (`[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotatorSelector)`)` To select the annotators to run and the phrase matchers to use (if any). If not specified, all annotators will be run.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
