---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations
title: REST Resource: projects.locations.authorizedViewSets.authorizedViews.conversations \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:59.963283+00:00
---

# REST Resource: projects.locations.authorizedViewSets.authorizedViews.conversations  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.authorizedViewSets.authorizedViews.conversations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Conversation
    * JSON representation
    * CallMetadata
      * JSON representation
    * ConversationDataSource
      * JSON representation
    * GcsSource
      * JSON representation
    * DialogflowSource
      * JSON representation
    * QualityMetadata
      * JSON representation
    * Transcript
      * JSON representation
    * TranscriptSegment
      * JSON representation
    * WordInfo
      * JSON representation
    * ConversationParticipant
      * JSON representation
    * DialogflowSegmentMetadata
      * JSON representation
    * ConversationSummarizationSuggestionData
      * JSON representation
    * RuntimeAnnotation
      * JSON representation
    * ArticleSuggestionData
      * JSON representation
    * FaqAnswerData
      * JSON representation
    * SmartReplyData
      * JSON representation
    * SmartComposeSuggestionData
      * JSON representation
    * DialogflowInteractionData
      * JSON representation
    * AnswerFeedback
      * JSON representation
    * CorrectnessLevel
    * UserInput
      * JSON representation
    * QuerySource
    * DialogflowIntent
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
  
### CallMetadata

Call-specific metadata.

JSON representation  
---  
      
    
    {
      "customerChannel": integer,
      "agentChannel": integer
    }  
  
Fields  
---  
`customerChannel` |  `integer` The audio channel that contains the customer.  
`agentChannel` |  `integer` The audio channel that contains the agent.  
  
### ConversationDataSource

The conversation source, which is a combination of transcript and audio.

JSON representation  
---  
      
    
    {
      "metadataUri": string,
    
      // Union field source can be only one of the following:
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.GcsSource))
      },
      "dialogflowSource": {
        object ([DialogflowSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.DialogflowSource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`metadataUri` |  `string` Cloud Storage URI that points to a file that contains the conversation metadata.  
Union field `source`. The source of the conversation. `source` can be only one of the following:  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.GcsSource)`)` A Cloud Storage location specification for the audio and transcript.  
`dialogflowSource` |  `object (`[DialogflowSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.DialogflowSource)`)` The source when the conversation comes from Dialogflow.  
  
### GcsSource

A Cloud Storage source of conversation data.

JSON representation  
---  
      
    
    {
      "audioUri": string,
      "transcriptUri": string
    }  
  
Fields  
---  
`audioUri` |  `string` Cloud Storage URI that points to a file that contains the conversation audio.  
`transcriptUri` |  `string` Immutable. Cloud Storage URI that points to a file that contains the conversation transcript.  
  
### DialogflowSource

A Dialogflow source of conversation data.

JSON representation  
---  
      
    
    {
      "dialogflowConversation": string,
      "audioUri": string
    }  
  
Fields  
---  
`dialogflowConversation` |  `string` Output only. The name of the Dialogflow conversation that this conversation resource is derived from. Format: projects/{project}/locations/{location}/conversations/{conversation}  
`audioUri` |  `string` Cloud Storage URI that points to a file that contains the conversation audio.  
  
### QualityMetadata

Conversation metadata related to quality management.

JSON representation  
---  
      
    
    {
      "customerSatisfactionRating": integer,
      "waitDuration": string,
      "menuPath": string,
      "agentInfo": [
        {
          object ([AgentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AgentInfo))
        }
      ]
    }  
  
Fields  
---  
`customerSatisfactionRating` |  `integer` An arbitrary integer value indicating the customer's satisfaction rating.  
`waitDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The amount of time the customer waited to connect with an agent.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`menuPath` |  `string` An arbitrary string value specifying the menu path the customer took.  
`agentInfo[]` |  `object (`[AgentInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AgentInfo)`)` Information about agents involved in the call.  
  
### Transcript

A message representing the transcript of a conversation.

JSON representation  
---  
      
    
    {
      "transcriptSegments": [
        {
          object ([TranscriptSegment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.TranscriptSegment))
        }
      ]
    }  
  
Fields  
---  
`transcriptSegments[]` |  `object (`[TranscriptSegment](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.TranscriptSegment)`)` A list of sequential transcript segments that comprise the conversation.  
  
### TranscriptSegment

A segment of a full transcript.

JSON representation  
---  
      
    
    {
      "messageTime": string,
      "text": string,
      "confidence": number,
      "words": [
        {
          object ([WordInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.WordInfo))
        }
      ],
      "languageCode": string,
      "channelTag": integer,
      "segmentParticipant": {
        object ([ConversationParticipant](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ConversationParticipant))
      },
      "dialogflowSegmentMetadata": {
        object ([DialogflowSegmentMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.DialogflowSegmentMetadata))
      },
      "sentiment": {
        object ([SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData))
      }
    }  
  
Fields  
---  
`messageTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time that the message occurred, if provided.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`text` |  `string` The text of this segment.  
`confidence` |  `number` A confidence estimate between 0.0 and 1.0 of the fidelity of this segment. A default value of 0.0 indicates that the value is unset.  
`words[]` |  `object (`[WordInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.WordInfo)`)` A list of the word-specific information for each word in the segment.  
`languageCode` |  `string` The language code of this segment as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".  
`channelTag` |  `integer` For conversations derived from multi-channel audio, this is the channel number corresponding to the audio from that channel. For audioChannelCount = N, its output values can range from '1' to 'N'. A channel tag of 0 indicates that the audio is mono.  
`segmentParticipant` |  `object (`[ConversationParticipant](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ConversationParticipant)`)` The participant of this segment.  
`dialogflowSegmentMetadata` |  `object (`[DialogflowSegmentMetadata](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.DialogflowSegmentMetadata)`)` CCAI metadata relating to the current transcript segment.  
`sentiment` |  `object (`[SentimentData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/SentimentData)`)` The sentiment for this transcript segment.  
  
### WordInfo

Word-level info for words in a transcript.

JSON representation  
---  
      
    
    {
      "startOffset": string,
      "endOffset": string,
      "word": string,
      "confidence": number
    }  
  
Fields  
---  
`startOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Time offset of the start of this word relative to the beginning of the total conversation.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`endOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Time offset of the end of this word relative to the beginning of the total conversation.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`word` |  `string` The word itself. Includes punctuation marks that surround the word.  
`confidence` |  `number` A confidence estimate between 0.0 and 1.0 of the fidelity of this word. A default value of 0.0 indicates that the value is unset.  
  
### ConversationParticipant

The call participant speaking for a given utterance.

JSON representation  
---  
      
    
    {
      "dialogflowParticipant": string,
      "obfuscatedExternalUserId": string,
      "role": enum ([Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Role)),
    
      // Union field participant can be only one of the following:
      "dialogflowParticipantName": string,
      "userId": string
      // End of list of possible types for union field participant.
    }  
  
Fields  
---  
`dialogflowParticipant  
**(deprecated)**` |  `string` This item is deprecated!Deprecated. Use `dialogflowParticipantName` instead. The name of the Dialogflow participant. Format: projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant}  
`obfuscatedExternalUserId` |  `string` Obfuscated user ID from Dialogflow.  
`role` |  `enum (`[Role](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/Role)`)` The role of the participant.  
Union field `participant`.`participant` can be only one of the following:  
`dialogflowParticipantName` |  `string` The name of the participant provided by Dialogflow. Format: projects/{project}/locations/{location}/conversations/{conversation}/participants/{participant}  
`userId` |  `string` A user-specified ID representing the participant.  
  
### DialogflowSegmentMetadata

Metadata from Dialogflow relating to the current transcript segment.

JSON representation  
---  
      
    
    {
      "smartReplyAllowlistCovered": boolean
    }  
  
Fields  
---  
`smartReplyAllowlistCovered` |  `boolean` Whether the transcript segment was covered under the configured smart reply allowlist in Agent Assist.  
  
### ConversationSummarizationSuggestionData

Conversation summarization suggestion data.

JSON representation  
---  
      
    
    {
      "text": string,
      "textSections": {
        string: string,
        ...
      },
      "confidence": number,
      "metadata": {
        string: string,
        ...
      },
      "answerRecord": string,
      "conversationModel": string,
      "generatorId": string
    }  
  
Fields  
---  
`text` |  `string` The summarization content that is concatenated into one string.  
`textSections` |  `map (key: string, value: string)` The summarization content that is divided into sections. The key is the section's name and the value is the section's content. There is no specific format for the key or value.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`confidence` |  `number` The confidence score of the summarization.  
`metadata` |  `map (key: string, value: string)` A map that contains metadata about the summarization and the document from which it originates.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`answerRecord` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answerRecord}  
`conversationModel` |  `string` The name of the model that generates this summary. Format: projects/{project}/locations/{location}/conversationModels/{conversationModel}  
`generatorId` |  `string` Agent Assist generator ID.  
  
### RuntimeAnnotation

An annotation that was generated during the customer and agent interaction.

JSON representation  
---  
      
    
    {
      "annotationId": string,
      "createTime": string,
      "startBoundary": {
        object ([AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotationBoundary))
      },
      "endBoundary": {
        object ([AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotationBoundary))
      },
      "answerFeedback": {
        object ([AnswerFeedback](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.AnswerFeedback))
      },
      "userInput": {
        object ([UserInput](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.UserInput))
      },
    
      // Union field data can be only one of the following:
      "articleSuggestion": {
        object ([ArticleSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ArticleSuggestionData))
      },
      "faqAnswer": {
        object ([FaqAnswerData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.FaqAnswerData))
      },
      "smartReply": {
        object ([SmartReplyData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.SmartReplyData))
      },
      "smartComposeSuggestion": {
        object ([SmartComposeSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.SmartComposeSuggestionData))
      },
      "dialogflowInteraction": {
        object ([DialogflowInteractionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.DialogflowInteractionData))
      },
      "conversationSummarizationSuggestion": {
        object ([ConversationSummarizationSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ConversationSummarizationSuggestionData))
      }
      // End of list of possible types for union field data.
    }  
  
Fields  
---  
`annotationId` |  `string` The unique identifier of the annotation. Format: projects/{project}/locations/{location}/conversationDatasets/{dataset}/conversationDataItems/{data_item}/conversationAnnotations/{annotation}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which this annotation was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startBoundary` |  `object (`[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotationBoundary)`)` The boundary in the conversation where the annotation starts, inclusive.  
`endBoundary` |  `object (`[AnnotationBoundary](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnnotationBoundary)`)` The boundary in the conversation where the annotation ends, inclusive.  
`answerFeedback` |  `object (`[AnswerFeedback](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.AnswerFeedback)`)` The feedback that the customer has about the answer in `data`.  
`userInput` |  `object (`[UserInput](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.UserInput)`)` Explicit input used for generating the answer  
Union field `data`. The data in the annotation. `data` can be only one of the following:  
`articleSuggestion` |  `object (`[ArticleSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ArticleSuggestionData)`)` Agent Assist Article Suggestion data.  
`faqAnswer` |  `object (`[FaqAnswerData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.FaqAnswerData)`)` Agent Assist FAQ answer data.  
`smartReply` |  `object (`[SmartReplyData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.SmartReplyData)`)` Agent Assist Smart Reply data.  
`smartComposeSuggestion` |  `object (`[SmartComposeSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.SmartComposeSuggestionData)`)` Agent Assist Smart Compose suggestion data.  
`dialogflowInteraction` |  `object (`[DialogflowInteractionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.DialogflowInteractionData)`)` Dialogflow interaction data.  
`conversationSummarizationSuggestion` |  `object (`[ConversationSummarizationSuggestionData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.ConversationSummarizationSuggestionData)`)` Conversation summarization suggestion data.  
  
### ArticleSuggestionData

Agent Assist Article Suggestion data.

JSON representation  
---  
      
    
    {
      "title": string,
      "uri": string,
      "confidenceScore": number,
      "metadata": {
        string: string,
        ...
      },
      "queryRecord": string,
      "source": string
    }  
  
Fields  
---  
`title` |  `string` Article title.  
`uri` |  `string` Article URI.  
`confidenceScore` |  `number` The system's confidence score that this article is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
`metadata` |  `map (key: string, value: string)` Map that contains metadata about the Article Suggestion and the document that it originates from.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`queryRecord` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answerRecord}  
`source` |  `string` The knowledge document that this answer was extracted from. Format: projects/{project}/knowledgeBases/{knowledgeBase}/documents/{document}  
  
### FaqAnswerData

Agent Assist frequently-asked-question answer data.

JSON representation  
---  
      
    
    {
      "answer": string,
      "confidenceScore": number,
      "question": string,
      "metadata": {
        string: string,
        ...
      },
      "queryRecord": string,
      "source": string
    }  
  
Fields  
---  
`answer` |  `string` The piece of text from the `source` knowledge base document.  
`confidenceScore` |  `number` The system's confidence score that this answer is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
`question` |  `string` The corresponding FAQ question.  
`metadata` |  `map (key: string, value: string)` Map that contains metadata about the FAQ answer and the document that it originates from.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`queryRecord` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answerRecord}  
`source` |  `string` The knowledge document that this answer was extracted from. Format: projects/{project}/knowledgeBases/{knowledgeBase}/documents/{document}.  
  
### SmartReplyData

Agent Assist Smart Reply data.

JSON representation  
---  
      
    
    {
      "reply": string,
      "confidenceScore": number,
      "metadata": {
        string: string,
        ...
      },
      "queryRecord": string
    }  
  
Fields  
---  
`reply` |  `string` The content of the reply.  
`confidenceScore` |  `number` The system's confidence score that this reply is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
`metadata` |  `map (key: string, value: string)` Map that contains metadata about the Smart Reply and the document from which it originates.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`queryRecord` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answerRecord}  
  
### SmartComposeSuggestionData

Agent Assist Smart Compose suggestion data.

JSON representation  
---  
      
    
    {
      "suggestion": string,
      "confidenceScore": number,
      "metadata": {
        string: string,
        ...
      },
      "queryRecord": string
    }  
  
Fields  
---  
`suggestion` |  `string` The content of the suggestion.  
`confidenceScore` |  `number` The system's confidence score that this suggestion is a good match for this conversation, ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
`metadata` |  `map (key: string, value: string)` Map that contains metadata about the Smart Compose suggestion and the document from which it originates.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`queryRecord` |  `string` The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answerRecord}  
  
### DialogflowInteractionData

Dialogflow interaction data.

JSON representation  
---  
      
    
    {
      "dialogflowIntentId": string,
      "confidence": number
    }  
  
Fields  
---  
`dialogflowIntentId` |  `string` The Dialogflow intent resource path. Format: projects/{project}/agent/{agent}/intents/{intent}  
`confidence` |  `number` The confidence of the match ranging from 0.0 (completely uncertain) to 1.0 (completely certain).  
  
### AnswerFeedback

The feedback that the customer has about a certain answer in the conversation.

JSON representation  
---  
      
    
    {
      "correctnessLevel": enum ([CorrectnessLevel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.CorrectnessLevel)),
      "clicked": boolean,
      "displayed": boolean
    }  
  
Fields  
---  
`correctnessLevel` |  `enum (`[CorrectnessLevel](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.CorrectnessLevel)`)` The correctness level of an answer.  
`clicked` |  `boolean` Indicates whether an answer or item was clicked by the human agent.  
`displayed` |  `boolean` Indicates whether an answer or item was displayed to the human agent in the agent desktop UI.  
  
### CorrectnessLevel

The correctness level of an answer.

Enums  
---  
`CORRECTNESS_LEVEL_UNSPECIFIED` | Correctness level unspecified.  
`NOT_CORRECT` | Answer is totally wrong.  
`PARTIALLY_CORRECT` | Answer is partially correct.  
`FULLY_CORRECT` | Answer is fully correct.  
  
### UserInput

Explicit input used for generating the answer

JSON representation  
---  
      
    
    {
      "query": string,
      "generatorName": string,
      "querySource": enum ([QuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.QuerySource))
    }  
  
Fields  
---  
`query` |  `string` Query text. Article Search uses this to store the input query used to generate the search results.  
`generatorName` |  `string` The resource name of associated generator. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`querySource` |  `enum (`[QuerySource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations#Conversation.QuerySource)`)` Query source for the answer.  
  
### QuerySource

The source of the query.

Enums  
---  
`QUERY_SOURCE_UNSPECIFIED` | Unknown query source.  
`AGENT_QUERY` | The query is from agents.  
`SUGGESTED_QUERY` | The query is a query from previous suggestions, e.g. from a preceding suggestions.suggestKnowledgeAssist response.  
  
### DialogflowIntent

The data for a Dialogflow intent. Represents a detected intent in the conversation, e.g. MAKES_PROMISE.

JSON representation  
---  
      
    
    {
      "displayName": string
    }  
  
Fields  
---  
`displayName` |  `string` The human-readable name of the intent.  
  
## Methods  
  
---  
  
### `[bulkAnalyze](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/bulkAnalyze)`

|  Analyzes multiple conversations in a single request.  
  
### `[calculateStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/calculateStats)`

|  Gets conversation statistics.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/delete)`

|  Deletes a conversation.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/get)`

|  Gets a conversation.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.authorizedViewSets.authorizedViews.conversations/list)`

|  Lists conversations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
