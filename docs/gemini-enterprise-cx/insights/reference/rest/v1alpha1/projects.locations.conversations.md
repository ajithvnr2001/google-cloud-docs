---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations
title: REST Resource: projects.locations.conversations \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:57:56.233481+00:00
---

# REST Resource: projects.locations.conversations  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.conversations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Conversation
    * JSON representation
  * Methods



## Resource: Conversation

The conversation resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "dataSource": {
        object ([ConversationDataSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ConversationDataSource))
      },
      "createTime": string,
      "updateTime": string,
      "startTime": string,
      "languageCode": string,
      "agentId": string,
      "labels": {
        string: string,
        ...
      },
      "qualityMetadata": {
        object ([QualityMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.QualityMetadata))
      },
      "metadataJson": string,
      "transcript": {
        object ([Transcript](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.Transcript))
      },
      "medium": enum ([Medium](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Medium)),
      "duration": string,
      "turnCount": integer,
      "latestAnalysis": {
        object ([Analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis))
      },
      "latestSummary": {
        object ([ConversationSummarizationSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ConversationSummarizationSuggestionData))
      },
      "runtimeAnnotations": [
        {
          object ([RuntimeAnnotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.RuntimeAnnotation))
        }
      ],
      "dialogflowIntents": {
        string: {
          object ([DialogflowIntent](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.DialogflowIntent))
        },
        ...
      },
      "obfuscatedUserId": string,
    
      // Union field metadata can be only one of the following:
      "callMetadata": {
        object ([CallMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.CallMetadata))
      }
      // End of list of possible types for union field metadata.
    
      // Union field expiration can be only one of the following:
      "expireTime": string,
      "ttl": string
      // End of list of possible types for union field expiration.
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation}  
`dataSource` |  `object (`[ConversationDataSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ConversationDataSource)`)` The source of the audio and transcription for the conversation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the conversation was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time at which the conversation was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the conversation started.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`languageCode` |  `string` A user-specified language code for the conversation.  
`agentId` |  `string` An opaque, user-specified string representing the human agent who handled the conversation.  
`labels` |  `map (key: string, value: string)` A map for the user to specify any custom fields. A maximum of 100 labels per conversation is allowed, with a maximum of 256 characters per entry.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`qualityMetadata` |  `object (`[QualityMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.QualityMetadata)`)` Conversation metadata related to quality management.  
`metadataJson` |  `string` Input only. JSON metadata encoded as a string. This field is primarily used by Insights integrations with various telephony systems and must be in one of Insight's supported formats.  
`transcript` |  `object (`[Transcript](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.Transcript)`)` Output only. The conversation transcript.  
`medium` |  `enum (`[Medium](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Medium)`)` Immutable. The conversation medium, if unspecified will default to PHONE_CALL.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration of the conversation.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`turnCount` |  `integer` Output only. The number of turns in the conversation.  
`latestAnalysis` |  `object (`[Analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations.analyses#Analysis)`)` Output only. The conversation's latest analysis, if one exists.  
`latestSummary` |  `object (`[ConversationSummarizationSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ConversationSummarizationSuggestionData)`)` Output only. Latest summary of the conversation.  
`runtimeAnnotations[]` |  `object (`[RuntimeAnnotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.RuntimeAnnotation)`)` Output only. The annotations that were generated during the customer and agent interaction.  
`dialogflowIntents` |  `map (key: string, value: object (`[DialogflowIntent](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.DialogflowIntent)`))` Output only. All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/{project}/agent/{agent}/intents/{intent}An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`obfuscatedUserId` |  `string` Obfuscated user ID which the customer sent to us.  
Union field `metadata`. Metadata that applies to the conversation. `metadata` can be only one of the following:  
`callMetadata` |  `object (`[CallMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.CallMetadata)`)` Call-specific metadata.  
Union field `expiration`. A time to live expiration setting, can be either a specified timestamp or a duration from the time that the conversation creation request was received. Conversations with an expiration set will be removed up to 24 hours after the specified time. `expiration` can be only one of the following:  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ttl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## Methods  
  
---  
  
### `[bulkAnalyze](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/bulkAnalyze)`

|  Analyzes multiple conversations in a single request.  
  
### `[bulkDelete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/bulkDelete)`

|  Deletes multiple conversations in a single request.  
  
### `[calculateStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/calculateStats)`

|  Gets conversation statistics.  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/create)`

|  Creates a conversation.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/delete)`

|  Deletes a conversation.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/get)`

|  Gets a conversation.  
  
### `[ingest](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/ingest)`

|  Imports conversations and processes them according to the user's configuration.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/list)`

|  Lists conversations.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/patch)`

|  Updates a conversation.  
  
### `[upload](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/upload)`

|  Create a long-running conversation upload operation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
