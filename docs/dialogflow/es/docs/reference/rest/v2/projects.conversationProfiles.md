---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles
title: REST Resource: projects.conversationProfiles \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:20.264378+00:00
---

# REST Resource: projects.conversationProfiles  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.conversationProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConversationProfile
    * JSON representation
    * AutomatedAgentConfig
      * JSON representation
    * HumanAgentAssistantConfig
      * JSON representation
    * NotificationConfig
      * JSON representation
    * MessageFormat
    * SuggestionConfig
      * JSON representation
    * SuggestionFeatureConfig
      * JSON representation
    * SuggestionFeature
      * JSON representation
    * Type
    * RaiSettings
      * JSON representation
    * RaiCategoryConfig
      * JSON representation
    * RaiCategory
    * SensitivityLevel
    * SuggestionTriggerSettings
      * JSON representation
    * SuggestionQueryConfig
      * JSON representation
    * KnowledgeBaseQuerySource
      * JSON representation
    * DocumentQuerySource
      * JSON representation
    * DialogflowQuerySource
      * JSON representation
    * HumanAgentSideConfig
      * JSON representation
    * ContextFilterSettings
      * JSON representation
    * Sections
      * JSON representation
    * SectionType
    * ConversationModelConfig
      * JSON representation
    * ConversationProcessConfig
      * JSON representation
    * MessageAnalysisConfig
      * JSON representation
    * HumanAgentHandoffConfig
      * JSON representation
    * LivePersonConfig
      * JSON representation
    * SalesforceLiveAgentConfig
      * JSON representation
    * LoggingConfig
      * JSON representation
    * SpeechToTextConfig
      * JSON representation
    * SpeechModelVariant
    * AudioEncoding
    * GeminiAsrConfig
      * JSON representation
    * StartSensitivity
    * EndSensitivity
    * SipConfig
      * JSON representation
  * Methods



## Resource: ConversationProfile

Defines the services to connect to incoming Dialogflow conversations.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "automatedAgentConfig": {
        object ([AutomatedAgentConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.AutomatedAgentConfig))
      },
      "humanAgentAssistantConfig": {
        object ([HumanAgentAssistantConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig))
      },
      "humanAgentHandoffConfig": {
        object ([HumanAgentHandoffConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentHandoffConfig))
      },
      "notificationConfig": {
        object ([NotificationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.NotificationConfig))
      },
      "loggingConfig": {
        object ([LoggingConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.LoggingConfig))
      },
      "newMessageEventNotificationConfig": {
        object ([NotificationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.NotificationConfig))
      },
      "newRecognitionResultNotificationConfig": {
        object ([NotificationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.NotificationConfig))
      },
      "sttConfig": {
        object ([SpeechToTextConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SpeechToTextConfig))
      },
      "languageCode": string,
      "sipConfig": {
        object ([SipConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SipConfig))
      },
      "timeZone": string,
      "securitySettings": string,
      "ttsConfig": {
        object ([SynthesizeSpeechConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SynthesizeSpeechConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of this conversation profile. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
`displayName` |  `string` Required. Human readable name for this profile. Max length 1024 bytes.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time of the conversation profile.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time of the conversation profile.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`automatedAgentConfig` |  `object (`[AutomatedAgentConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.AutomatedAgentConfig)`)` Configuration for an automated agent to use with this profile.  
`humanAgentAssistantConfig` |  `object (`[HumanAgentAssistantConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig)`)` Configuration for agent assistance to use with this profile.  
`humanAgentHandoffConfig` |  `object (`[HumanAgentHandoffConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentHandoffConfig)`)` Configuration for connecting to a live agent.Currently, this feature is not general available, please contact Google to get access.  
`notificationConfig` |  `object (`[NotificationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.NotificationConfig)`)` Configuration for publishing conversation lifecycle events.  
`loggingConfig` |  `object (`[LoggingConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.LoggingConfig)`)` Configuration for logging conversation lifecycle events.  
`newMessageEventNotificationConfig` |  `object (`[NotificationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.NotificationConfig)`)` Configuration for publishing new message events. Event will be sent in format of `[ConversationEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent)`  
`newRecognitionResultNotificationConfig` |  `object (`[NotificationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.NotificationConfig)`)` Optional. Configuration for publishing transcription intermediate results. Event will be sent in format of `[ConversationEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent)`. If configured, the following information will be populated as `[ConversationEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent)` Pub/Sub message attributes: - "participant_id" - "participantRole" - "message_id"  
`sttConfig` |  `object (`[SpeechToTextConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SpeechToTextConfig)`)` Settings for speech transcription.  
`languageCode` |  `string` Language code for the conversation profile. If not specified, the language is en-US. Language at ConversationProfile should be set for all non en-US languages. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".  
`sipConfig` |  `object (`[SipConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SipConfig)`)` Optional. Configuration for SIP connections.  
`timeZone` |  `string` The time zone of this conversational profile from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. Defaults to America/New_York.  
`securitySettings` |  `string` Name of the CX SecuritySettings reference for the agent. Format: `projects/<Project ID>/locations/<Location ID>/securitySettings/<Security Settings ID>`.  
`ttsConfig` |  `object (`[SynthesizeSpeechConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SynthesizeSpeechConfig)`)` Configuration for Text-to-Speech synthesization.Used by Phone Gateway to specify synthesization options. If agent defines synthesization options as well, agent settings overrides the option here.  
  
### AutomatedAgentConfig

Defines the Automated Agent to connect to a conversation.

JSON representation  
---  
      
    
    {
      "agent": string,
      "sessionTtl": string
    }  
  
Fields  
---  
`agent` |  `string` Required. ID of the Dialogflow agent environment to use.This project needs to either be the same project as the conversation or you need to grant `service-<Conversation Project Number>@gcp-sa-dialogflow.iam.gserviceaccount.com` the `Dialogflow API Service Agent` role in this project.

  * For ES agents, use format: `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID or '-'>`. If environment is not specified, the default `draft` environment is used. Refer to [DetectIntentRequest](https://docs.cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2#google.cloud.dialogflow.v2.DetectIntentRequest) for more details.
  * For CX agents, use format `projects/<Project ID>/locations/<Location ID>/agents/<Agent ID>/environments/<Environment ID or '-'>`. If environment is not specified, the default `draft` environment is used.

  
`sessionTtl` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Configure lifetime of the Dialogflow session. By default, a Dialogflow CX session remains active and its data is stored for 30 minutes after the last request is sent for the session. This value should be no longer than 1 day.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### HumanAgentAssistantConfig

Defines the Human Agent Assist to connect to a conversation.

JSON representation  
---  
      
    
    {
      "notificationConfig": {
        object ([NotificationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.NotificationConfig))
      },
      "humanAgentSuggestionConfig": {
        object ([SuggestionConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionConfig))
      },
      "endUserSuggestionConfig": {
        object ([SuggestionConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionConfig))
      },
      "messageAnalysisConfig": {
        object ([MessageAnalysisConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.MessageAnalysisConfig))
      }
    }  
  
Fields  
---  
`notificationConfig` |  `object (`[NotificationConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.NotificationConfig)`)` Pub/Sub topic on which to publish new agent assistant events.  
`humanAgentSuggestionConfig` |  `object (`[SuggestionConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionConfig)`)` Configuration for agent assistance of human agent participant.  
`endUserSuggestionConfig` |  `object (`[SuggestionConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionConfig)`)` Configuration for agent assistance of end user participant.Currently, this feature is not general available, please contact Google to get access.  
`messageAnalysisConfig` |  `object (`[MessageAnalysisConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.MessageAnalysisConfig)`)` Configuration for message analysis.  
  
### NotificationConfig

Defines notification behavior.

JSON representation  
---  
      
    
    {
      "topic": string,
      "messageFormat": enum ([MessageFormat](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.MessageFormat))
    }  
  
Fields  
---  
`topic` |  `string` Name of the Pub/Sub topic to publish conversation events like `[CONVERSATION_STARTED](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Type#ENUM_VALUES.CONVERSATION_STARTED)` as serialized `[ConversationEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent)` protos.For telephony integration to receive notification, make sure either this topic is in the same project as the conversation or you grant `service-<Conversation Project Number>@gcp-sa-dialogflow.iam.gserviceaccount.com` the `Dialogflow Service Agent` role in the topic project.For chat integration to receive notification, make sure API caller has been granted the `Dialogflow Service Agent` role for the topic.Format: `projects/<Project ID>/locations/<Location ID>/topics/<Topic ID>`.  
`messageFormat` |  `enum (`[MessageFormat](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.MessageFormat)`)` Format of message.  
  
### MessageFormat

Format of cloud pub/sub message.

Enums  
---  
`MESSAGE_FORMAT_UNSPECIFIED` | If it is unspecified, PROTO will be used.  
`PROTO` | Pub/Sub message will be serialized proto.  
`JSON` | Pub/Sub message will be json.  
  
### SuggestionConfig

Detail human agent assistant config.

JSON representation  
---  
      
    
    {
      "featureConfigs": [
        {
          object ([SuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionFeatureConfig))
        }
      ],
      "groupSuggestionResponses": boolean,
      "generators": [
        string
      ],
      "disableHighLatencyFeaturesSyncDelivery": boolean,
      "skipEmptyEventBasedSuggestion": boolean,
      "useUnredactedConversationData": boolean,
      "enableAsyncToolCall": boolean,
      "companionAgent": string
    }  
  
Fields  
---  
`featureConfigs[]` |  `object (`[SuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionFeatureConfig)`)` Configuration of different suggestion features. One feature can have only one config.  
`groupSuggestionResponses` |  `boolean` If `groupSuggestionResponses` is false, and there are multiple `featureConfigs` in `event based suggestion` or StreamingAnalyzeContent, we will try to deliver suggestions to customers as soon as we get new suggestion. Different type of suggestions based on the same context will be in separate Pub/Sub event or `StreamingAnalyzeContentResponse`.If `groupSuggestionResponses` set to true. All the suggestions to the same participant based on the same context will be grouped into a single Pub/Sub event or StreamingAnalyzeContentResponse.  
`generators[]` |  `string` Optional. List of various generator resource names used in the conversation profile.  
`disableHighLatencyFeaturesSyncDelivery` |  `boolean` Optional. When disableHighLatencyFeaturesSyncDelivery is true and using the AnalyzeContent API, we will not deliver the responses from high latency features in the API response. The humanAgentAssistantConfig.notification_config must be configured and enableEventBasedSuggestion must be set to true to receive the responses from high latency features in Pub/Sub. High latency feature(s): KNOWLEDGE_ASSIST  
`skipEmptyEventBasedSuggestion` |  `boolean` Optional. Enable skipping event based suggestion if the suggestion is empty.For example, with this field disabled, Knowledge Assist feature sends a Pub/Sub message when there are no suggestions. Enabling this field will change the behavior to skip the Pub/Sub message in this situation.  
`useUnredactedConversationData` |  `boolean` Optional. If true, use unredacted transcript data (Supported features: AI_COACH) and use unredacted ingested context (Supported features: All Agent Assist features)  
`enableAsyncToolCall  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: This field is not consulted for tool execution. Configure asynchronous execution per tool using `CesToolSpec.async_execution` or `ToolsetTool.async_execution` instead.  
`companionAgent` |  `string` Optional. The resource name of the companion agent to link. This is only supported for `humanAgentSuggestionConfig`. Format: `projects/{project}/locations/{location}/companionAgents/{companionAgent}`  
  
### SuggestionFeatureConfig

Config for suggestion features.

JSON representation  
---  
      
    
    {
      "suggestionFeature": {
        object ([SuggestionFeature](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionFeature))
      },
      "enableEventBasedSuggestion": boolean,
      "disableAgentQueryLogging": boolean,
      "enableQuerySuggestionWhenNoAnswer": boolean,
      "enableConversationAugmentedQuery": boolean,
      "enableQuerySuggestionOnly": boolean,
      "enableResponseDebugInfo": boolean,
      "raiSettings": {
        object ([RaiSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.RaiSettings))
      },
      "suggestionTriggerEvent": enum ([TriggerEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/TriggerEvent)),
      "disableQuerySearchContext": boolean,
      "suggestionTriggerSettings": {
        object ([SuggestionTriggerSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionTriggerSettings))
      },
      "queryConfig": {
        object ([SuggestionQueryConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionQueryConfig))
      },
      "conversationModelConfig": {
        object ([ConversationModelConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.ConversationModelConfig))
      },
      "conversationProcessConfig": {
        object ([ConversationProcessConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.ConversationProcessConfig))
      }
    }  
  
Fields  
---  
`suggestionFeature` |  `object (`[SuggestionFeature](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionFeature)`)` The suggestion feature.  
`enableEventBasedSuggestion` |  `boolean` Automatically iterates all participants and tries to compile suggestions.Supported features: ARTICLE_SUGGESTION, FAQ, DIALOGFLOW_ASSIST, KNOWLEDGE_ASSIST.  
`disableAgentQueryLogging` |  `boolean` Optional. Disable the logging of search queries sent by human agents. It can prevent those queries from being stored at answer records.Supported features: KNOWLEDGE_SEARCH.  
`enableQuerySuggestionWhenNoAnswer` |  `boolean` Optional. Enable query suggestion even if we can't find its answer. By default, queries are suggested only if we find its answer. Supported features: KNOWLEDGE_ASSIST  
`enableConversationAugmentedQuery` |  `boolean` Optional. Enable including conversation context during query answer generation. Supported features: KNOWLEDGE_SEARCH.  
`enableQuerySuggestionOnly` |  `boolean` Optional. Enable query suggestion only. Supported features: KNOWLEDGE_ASSIST  
`enableResponseDebugInfo` |  `boolean` Optional. Enable returning detailed reasons for suggestion results.For example, with this field disabled, Knowledge Search feature returns NotFound error when no answer is found for the input query. Enabling this field will change the behavior to return an OK response with detailed information indicating the lack of results.Supported features: KNOWLEDGE_SEARCH, KNOWLEDGE_ASSIST  
`raiSettings` |  `object (`[RaiSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.RaiSettings)`)` Optional. Settings for Responsible AI checks. Supported features: KNOWLEDGE_ASSIST  
`suggestionTriggerEvent` |  `enum (`[TriggerEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/TriggerEvent)`)` Optional. The trigger event for suggestion. If unspecified, it will be `CUSTOMER_MESSAGE`. Supported features: KNOWLEDGE_ASSIST For KNOWLEDGE_ASSIST, these four trigger events are supported: 1. TRIGGER_EVENT_UNSPECIFIED 2. END_OF_UTTERANCE 3. CUSTOMER_MESSAGE 4. AGENT_MESSAGE  
`disableQuerySearchContext` |  `boolean` Optional. If true, disable appending available search context to the search query. Supported features: KNOWLEDGE_ASSIST  
`suggestionTriggerSettings` |  `object (`[SuggestionTriggerSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionTriggerSettings)`)` Settings of suggestion trigger.Currently, only ARTICLE_SUGGESTION and FAQ will use this field.  
`queryConfig` |  `object (`[SuggestionQueryConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionQueryConfig)`)` Configs of query.  
`conversationModelConfig` |  `object (`[ConversationModelConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.ConversationModelConfig)`)` Configs of custom conversation model.  
`conversationProcessConfig` |  `object (`[ConversationProcessConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.ConversationProcessConfig)`)` Configs for processing conversation.  
  
### SuggestionFeature

The type of Human Agent Assistant API suggestion to perform, and the maximum number of results to return for that type. Multiple `Feature` objects can be specified in the `features` list.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.Type))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.Type)`)` Type of Human Agent Assistant API feature to request.  
  
### Type

Defines the type of Human Agent Assistant feature.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified feature type.  
`ARTICLE_SUGGESTION` | Run article suggestion model for chat.  
`FAQ` | Run FAQ model for chat.  
`SMART_REPLY` | Run smart reply model for chat.  
`CONVERSATION_SUMMARIZATION` | Run conversation summarization model for chat.  
`KNOWLEDGE_SEARCH` | Run knowledge search with text input from agent or text generated query.  
`KNOWLEDGE_ASSIST` | Run knowledge assist with automatic query generation.  
  
### RaiSettings

Settings for Responsible AI checks.

JSON representation  
---  
      
    
    {
      "raiCategoryConfigs": [
        {
          object ([RaiCategoryConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.RaiCategoryConfig))
        }
      ]
    }  
  
Fields  
---  
`raiCategoryConfigs[]` |  `object (`[RaiCategoryConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.RaiCategoryConfig)`)` Configuration for a set of RAI categories.  
  
### RaiCategoryConfig

Configuration for a specific RAI category.

JSON representation  
---  
      
    
    {
      "category": enum ([RaiCategory](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.RaiCategory)),
      "sensitivityLevel": enum ([SensitivityLevel](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SensitivityLevel))
    }  
  
Fields  
---  
`category` |  `enum (`[RaiCategory](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.RaiCategory)`)` Optional. The RAI category.  
`sensitivityLevel` |  `enum (`[SensitivityLevel](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SensitivityLevel)`)` Optional. The sensitivity level for this category.  
  
### RaiCategory

Enum for RAI category.

Enums  
---  
`RAI_CATEGORY_UNSPECIFIED` | Default value.  
`DANGEROUS_CONTENT` | Dangerous content.  
`SEXUALLY_EXPLICIT` | Sexually explicit content.  
`HARASSMENT` | Harassment content.  
`HATE_SPEECH` | Hate speech content.  
  
### SensitivityLevel

Enum for user-configurable sensitivity levels.

Enums  
---  
`SENSITIVITY_LEVEL_UNSPECIFIED` | Default value. If unspecified, the default behavior is: - DANGEROUS_CONTENT: BLOCK_FEW - SEXUALLY_EXPLICIT: BLOCK_SOME - HARASSMENT: BLOCK_SOME - HATE_SPEECH: BLOCK_SOME  
`BLOCK_MOST` | Block most potentially sensitive responses.  
`BLOCK_SOME` | Block some potentially sensitive responses.  
`BLOCK_FEW` | Block a few potentially sensitive responses.  
`BLOCK_NONE` | No filtering for this category.  
  
### SuggestionTriggerSettings

Settings of suggestion trigger.

JSON representation  
---  
      
    
    {
      "noSmalltalk": boolean,
      "onlyEndUser": boolean
    }  
  
Fields  
---  
`noSmalltalk` |  `boolean` Do not trigger if last utterance is small talk.  
`onlyEndUser` |  `boolean` Only trigger suggestion if participant role of last utterance is END_USER.  
  
### SuggestionQueryConfig

Config for suggestion query.

JSON representation  
---  
      
    
    {
      "maxResults": integer,
      "confidenceThreshold": number,
      "contextFilterSettings": {
        object ([ContextFilterSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.ContextFilterSettings))
      },
      "sections": {
        object ([Sections](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.Sections))
      },
      "contextSize": integer,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "knowledgeBaseQuerySource": {
        object ([KnowledgeBaseQuerySource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.KnowledgeBaseQuerySource))
      },
      "documentQuerySource": {
        object ([DocumentQuerySource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.DocumentQuerySource))
      },
      "dialogflowQuerySource": {
        object ([DialogflowQuerySource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.DialogflowQuerySource))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`maxResults` |  `integer` Maximum number of results to return. Currently, if unset, defaults to 10. And the max number is 20.  
`confidenceThreshold` |  `number` Confidence threshold of query result.Agent Assist gives each suggestion a score in the range [0.0, 1.0], based on the relevance between the suggestion and the current conversation context. A score of 0.0 has no relevance, while a score of 1.0 has high relevance. Only suggestions with a score greater than or equal to the value of this field are included in the results.For a baseline model (the default), the recommended value is in the range [0.05, 0.1].For a custom model, there is no recommended value. Tune this value by starting from a very low value and slowly increasing until you have desired results.If this field is not set, it defaults to 0.0, which means that all suggestions are returned.Supported features: ARTICLE_SUGGESTION, FAQ, SMART_REPLY, SMART_COMPOSE, KNOWLEDGE_SEARCH, KNOWLEDGE_ASSIST, ENTITY_EXTRACTION.  
`contextFilterSettings` |  `object (`[ContextFilterSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.ContextFilterSettings)`)` Determines how recent conversation context is filtered when generating suggestions. If unspecified, no messages will be dropped.  
`sections` |  `object (`[Sections](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.Sections)`)` Optional. The customized sections chosen to return when requesting a summary of a conversation.  
`contextSize` |  `integer` Optional. The number of recent messages to include in the context. Supported features: KNOWLEDGE_ASSIST.  
Source of query. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`knowledgeBaseQuerySource` |  `object (`[KnowledgeBaseQuerySource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.KnowledgeBaseQuerySource)`)` Query from knowledgebase. It is used by: ARTICLE_SUGGESTION, FAQ.  
`documentQuerySource` |  `object (`[DocumentQuerySource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.DocumentQuerySource)`)` Query from knowledge base document. It is used by: SMART_REPLY, SMART_COMPOSE.  
`dialogflowQuerySource` |  `object (`[DialogflowQuerySource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.DialogflowQuerySource)`)` Query from Dialogflow agent. It is used by DIALOGFLOW_ASSIST.  
End of mutually exclusive fields.  
  
### KnowledgeBaseQuerySource

Knowledge base source settings.

Supported features: ARTICLE_SUGGESTION, FAQ.

JSON representation  
---  
      
    
    {
      "knowledgeBases": [
        string
      ]
    }  
  
Fields  
---  
`knowledgeBases[]` |  `string` Required. Knowledge bases to query. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<Knowledge Base ID>`. Currently, at most 5 knowledge bases are supported.  
  
### DocumentQuerySource

Document source settings.

Supported features: SMART_REPLY, SMART_COMPOSE.

JSON representation  
---  
      
    
    {
      "documents": [
        string
      ]
    }  
  
Fields  
---  
`documents[]` |  `string` Required. Knowledge documents to query from. Format: `projects/<Project ID>/locations/<Location ID>/knowledgeBases/<KnowledgeBase ID>/documents/<Document ID>`. Currently, at most 5 documents are supported.  
  
### DialogflowQuerySource

Dialogflow source setting.

Supported feature: DIALOGFLOW_ASSIST.

JSON representation  
---  
      
    
    {
      "agent": string,
      "humanAgentSideConfig": {
        object ([HumanAgentSideConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentSideConfig))
      }
    }  
  
Fields  
---  
`agent` |  `string` Required. The name of a Dialogflow virtual agent used for end user side intent detection and suggestion. Format: `projects/<Project ID>/locations/<Location ID>/agent`. When multiple agents are allowed in the same Dialogflow project.  
`humanAgentSideConfig` |  `object (`[HumanAgentSideConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentSideConfig)`)` Optional. The Dialogflow assist configuration for human agent.  
  
### HumanAgentSideConfig

The configuration used for human agent side Dialogflow assist suggestion.

JSON representation  
---  
      
    
    {
      "agent": string
    }  
  
Fields  
---  
`agent` |  `string` Optional. The name of a dialogflow virtual agent used for intent detection and suggestion triggered by human agent. Format: `projects/<Project ID>/locations/<Location ID>/agent`.  
  
### ContextFilterSettings

Settings that determine how to filter recent conversation context when generating suggestions.

JSON representation  
---  
      
    
    {
      "dropHandoffMessages": boolean,
      "dropVirtualAgentMessages": boolean,
      "dropIvrMessages": boolean
    }  
  
Fields  
---  
`dropHandoffMessages` |  `boolean` If set to true, the last message from virtual agent (hand off message) and the message before it (trigger message of hand off) are dropped.  
`dropVirtualAgentMessages` |  `boolean` If set to true, all messages from virtual agent are dropped.  
`dropIvrMessages` |  `boolean` If set to true, all messages from ivr stage are dropped.  
  
### Sections

Custom sections to return when requesting a summary of a conversation. This is only supported when `baselineModelVersion` == '2.0'.

Supported features: CONVERSATION_SUMMARIZATION, CONVERSATION_SUMMARIZATION_VOICE.

JSON representation  
---  
      
    
    {
      "sectionTypes": [
        enum ([SectionType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SectionType))
      ]
    }  
  
Fields  
---  
`sectionTypes[]` |  `enum (`[SectionType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SectionType)`)` The selected sections chosen to return when requesting a summary of a conversation. A duplicate selected section will be treated as a single selected section. If section types are not provided, the default will be {SITUATION, ACTION, RESULT}.  
  
### SectionType

Selectable sections to return when requesting a summary of a conversation.

Enums  
---  
`SECTION_TYPE_UNSPECIFIED` | Undefined section type, does not return anything.  
`SITUATION` | What the customer needs help with or has question about. Section name: "situation".  
`ACTION` | What the agent does to help the customer. Section name: "action".  
`RESOLUTION` | Result of the customer service. A single word describing the result of the conversation. Section name: "resolution".  
`REASON_FOR_CANCELLATION` | Reason for cancellation if the customer requests for a cancellation. "N/A" otherwise. Section name: "reason_for_cancellation".  
`CUSTOMER_SATISFACTION` | "Unsatisfied" or "Satisfied" depending on the customer's feelings at the end of the conversation. Section name: "customer_satisfaction".  
`ENTITIES` | Key entities extracted from the conversation, such as ticket number, order number, dollar amount, etc. Section names are prefixed by "entities/".  
  
### ConversationModelConfig

Custom conversation models used in agent assist feature.

Supported feature: ARTICLE_SUGGESTION, SMART_COMPOSE, SMART_REPLY, CONVERSATION_SUMMARIZATION

JSON representation  
---  
      
    
    {
      "model": string,
      "baselineModelVersion": string
    }  
  
Fields  
---  
`model` |  `string` Conversation model resource name. Format: `projects/<Project ID>/conversationModels/<Model ID>`.  
`baselineModelVersion` |  `string` Version of current baseline model. It will be ignored if `[model](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.ConversationModelConfig.FIELDS.model)` is set. Valid versions are:

  * Article Suggestion baseline model:
  * 0.9
  * 1.0 (default)
  * Summarization baseline model:
  * 1.0

  
  
### ConversationProcessConfig

Config to process conversation.

JSON representation  
---  
      
    
    {
      "recentSentencesCount": integer
    }  
  
Fields  
---  
`recentSentencesCount` |  `integer` Number of recent non-small-talk sentences to use as context for article and FAQ suggestion  
  
### MessageAnalysisConfig

Configuration for analyses to run on each conversation message.

JSON representation  
---  
      
    
    {
      "enableEntityExtraction": boolean,
      "enableSentimentAnalysis": boolean,
      "enableSentimentAnalysisV3": boolean
    }  
  
Fields  
---  
`enableEntityExtraction` |  `boolean` Enable entity extraction in conversation messages on [agent assist stage](https://cloud.google.com/dialogflow/priv/docs/contact-center/basics#stages). If unspecified, defaults to false.Currently, this feature is not general available, please contact Google to get access.  
`enableSentimentAnalysis` |  `boolean` Enable sentiment analysis in conversation messages on [agent assist stage](https://cloud.google.com/dialogflow/priv/docs/contact-center/basics#stages). If unspecified, defaults to false. Sentiment analysis inspects user input and identifies the prevailing subjective opinion, especially to determine a user's attitude as positive, negative, or neutral: <https://cloud.google.com/natural-language/docs/basics#sentimentAnalysis> For `Participants.StreamingAnalyzeContent` method, result will be in `StreamingAnalyzeContentResponse.message.SentimentAnalysisResult`. For `[Participants.AnalyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent#google.cloud.dialogflow.v2.Participants.AnalyzeContent)` method, result will be in `[AnalyzeContentResponse.message.SentimentAnalysisResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AnalyzeContentResponse#FIELDS.message)` For `[Conversations.ListMessages](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.messages/list#google.cloud.dialogflow.v2.Conversations.ListMessages)` method, result will be in `[ListMessagesResponse.messages.SentimentAnalysisResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ListMessagesResponse#FIELDS.messages)` If Pub/Sub notification is configured, result will be in `[ConversationEvent.new_message_payload.SentimentAnalysisResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent#FIELDS.new_message_payload)`.  
`enableSentimentAnalysisV3` |  `boolean` Optional. Enables sentiment analysis for audio input and conversation messages. If unspecified, defaults to false. If this flag is set to true, other 'enableSentimentAnalysis' fields will be ignored.Sentiment analysis inspects user input and identifies the prevailing subjective opinion, especially to determine a user's attitude as positive, negative, or neutral. <https://cloud.google.com/natural-language/docs/basics#sentimentAnalysis> For `Participants.StreamingAnalyzeContent` method, result will be in `StreamingAnalyzeContentResponse.message.SentimentAnalysisResult`. For `[Participants.AnalyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent#google.cloud.dialogflow.v2.Participants.AnalyzeContent)` method, result will be in `[AnalyzeContentResponse.message.SentimentAnalysisResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AnalyzeContentResponse#FIELDS.message)` For `[Conversations.ListMessages](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.messages/list#google.cloud.dialogflow.v2.Conversations.ListMessages)` method, result will be in `[ListMessagesResponse.messages.SentimentAnalysisResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ListMessagesResponse#FIELDS.messages)` If Pub/Sub notification is configured, result will be in `[ConversationEvent.new_message_payload.SentimentAnalysisResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent#FIELDS.new_message_payload)`.  
  
### HumanAgentHandoffConfig

Defines the hand off to a live agent, typically on which external agent service provider to connect to a conversation.

Currently, this feature is not general available, please contact Google to get access.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "livePersonConfig": {
        object ([LivePersonConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.LivePersonConfig))
      },
      "salesforceLiveAgentConfig": {
        object ([SalesforceLiveAgentConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SalesforceLiveAgentConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Required. Specifies which agent service to connect for human agent handoff. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`livePersonConfig` |  `object (`[LivePersonConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.LivePersonConfig)`)` Uses [LivePerson](https://www.liveperson.com).  
`salesforceLiveAgentConfig` |  `object (`[SalesforceLiveAgentConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SalesforceLiveAgentConfig)`)` Uses Salesforce Live Agent.  
End of mutually exclusive fields.  
  
### LivePersonConfig

Configuration specific to [LivePerson](https://www.liveperson.com).

JSON representation  
---  
      
    
    {
      "accountNumber": string
    }  
  
Fields  
---  
`accountNumber` |  `string` Required. Account number of the LivePerson account to connect. This is the account number you input at the login page.  
  
### SalesforceLiveAgentConfig

Configuration specific to Salesforce Live Agent.

JSON representation  
---  
      
    
    {
      "organizationId": string,
      "deploymentId": string,
      "buttonId": string,
      "endpointDomain": string
    }  
  
Fields  
---  
`organizationId` |  `string` Required. The organization ID of the Salesforce account.  
`deploymentId` |  `string` Required. Live Agent deployment ID.  
`buttonId` |  `string` Required. Live Agent chat button ID.  
`endpointDomain` |  `string` Required. Domain of the Live Agent endpoint for this agent. You can find the endpoint URL in the `Live Agent settings` page. For example if URL has the form <https://d.la4-c2-phx.salesforceliveagent.com/...>, you should fill in d.la4-c2-phx.salesforceliveagent.com.  
  
### LoggingConfig

Defines logging behavior for conversation lifecycle events.

JSON representation  
---  
      
    
    {
      "enableStackdriverLogging": boolean
    }  
  
Fields  
---  
`enableStackdriverLogging` |  `boolean` Whether to log conversation events like `[CONVERSATION_STARTED](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Type#ENUM_VALUES.CONVERSATION_STARTED)` to Stackdriver in the conversation project as JSON format `[ConversationEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent)` protos.  
  
### SpeechToTextConfig

Configures speech transcription for `[ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile)`.

JSON representation  
---  
      
    
    {
      "speechModelVariant": enum ([SpeechModelVariant](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SpeechModelVariant)),
      "model": string,
      "phraseSets": [
        string
      ],
      "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.AudioEncoding)),
      "sampleRateHertz": integer,
      "languageCode": string,
      "enableWordInfo": boolean,
      "useTimeoutBasedEndpointing": boolean,
      "geminiAsrConfig": {
        object ([GeminiAsrConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.GeminiAsrConfig))
      },
      "useGeminiAsr": boolean
    }  
  
Fields  
---  
`speechModelVariant` |  `enum (`[SpeechModelVariant](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SpeechModelVariant)`)` The speech model used in speech to text. `SPEECH_MODEL_VARIANT_UNSPECIFIED`, `USE_BEST_AVAILABLE` will be treated as `USE_ENHANCED`. It can be overridden in `AnalyzeContentRequest` and `StreamingAnalyzeContentRequest` request. If enhanced model variant is specified and an enhanced version of the specified model for the language does not exist, then it would emit an error.  
`model` |  `string` Which Speech model to select. Select the model best suited to your domain to get best results. If a model is not explicitly specified, then Dialogflow auto-selects a model based on other parameters in the SpeechToTextConfig and Agent settings. If enhanced speech model is enabled for the agent and an enhanced version of the specified model for the language does not exist, then the speech is recognized using the standard version of the specified model. Refer to [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics#select-model) for more details. If you specify a model, the following models typically have the best performance:

  * phone_call (best for Agent Assist and telephony)
  * latest_short (best for Dialogflow non-telephony)
  * command_and_search

Leave this field unspecified to use [Agent Speech settings](https://cloud.google.com/dialogflow/cx/docs/concept/agent#settings-speech) for model selection.  
`phraseSets[]` |  `string` List of names of Cloud Speech phrase sets that are used for transcription. For phrase set limitations, please refer to [Cloud Speech API quotas and limits](https://cloud.google.com/speech-to-text/quotas#content).  
`audioEncoding` |  `enum (`[AudioEncoding](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.AudioEncoding)`)` Audio encoding of the audio content to process.  
`sampleRateHertz` |  `integer` Sample rate (in Hertz) of the audio content sent in the query. Refer to [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics) for more details.  
`languageCode` |  `string` The language of the supplied audio. Dialogflow does not do translations. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language. If not specified, the default language configured at `[ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile)` is used.  
`enableWordInfo` |  `boolean` If `true`, Dialogflow returns `[SpeechWordInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent#SpeechWordInfo)` in `[StreamingRecognitionResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent#StreamingRecognitionResult)` with information about the recognized speech words, e.g. start and end time offsets. If false or unspecified, Speech doesn't return any word-level information.  
`useTimeoutBasedEndpointing` |  `boolean` Use timeout based endpointing, interpreting endpointer sensitivity as seconds of timeout value.  
`geminiAsrConfig` |  `object (`[GeminiAsrConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.GeminiAsrConfig)`)` Optional. Configuration for using Gemini ASR models served via Vertex AI, overriding the default Gemini ASR model or providing additional advanced parameters. This field is only used when `useGeminiAsr` is true.  
`useGeminiAsr` |  `boolean` Optional. If true, Gemini ASR will be used for transcription instead of Cloud Speech-to-Text.  
  
### SpeechModelVariant

Variant of the specified `[Speech model](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/InputAudioConfig#FIELDS.model)` to use.

See the [Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/enhanced-models) for which models have different variants. For example, the "phone_call" model has both a standard and an enhanced variant. When you use an enhanced model, you will generally receive higher quality results than for a standard model.

Enums  
---  
`SPEECH_MODEL_VARIANT_UNSPECIFIED` | No model variant specified. In this case Dialogflow defaults to USE_BEST_AVAILABLE.  
`USE_BEST_AVAILABLE` | Use the best available variant of the [Speech model][model] that the caller is eligible for.Please see the [Dialogflow docs](https://cloud.google.com/dialogflow/docs/data-logging) for how to make your project eligible for enhanced models.  
`USE_STANDARD` | Use standard model variant even if an enhanced model is available. See the [Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/enhanced-models) for details about enhanced models.  
`USE_ENHANCED` | Use an enhanced model variant:

  * If an enhanced variant does not exist for the given `[model](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/InputAudioConfig#FIELDS.model)` and request language, Dialogflow falls back to the standard variant.

The [Cloud Speech documentation](https://cloud.google.com/speech-to-text/docs/enhanced-models) describes which models have enhanced variants.

  * If the API caller isn't eligible for enhanced models, Dialogflow returns an error. Please see the [Dialogflow docs](https://cloud.google.com/dialogflow/docs/data-logging) for how to make your project eligible.

  
  
### AudioEncoding

Audio encoding of the audio content sent in the conversational query request. Refer to the [Cloud Speech API documentation](https://cloud.google.com/speech-to-text/docs/basics) for more details.

Enums  
---  
`AUDIO_ENCODING_UNSPECIFIED` | Not specified.  
`AUDIO_ENCODING_LINEAR_16` | Uncompressed 16-bit signed little-endian samples (Linear PCM).  
`AUDIO_ENCODING_FLAC` | [`FLAC`](https://xiph.org/flac/documentation.html) (Free Lossless Audio Codec) is the recommended encoding because it is lossless (therefore recognition is not compromised) and requires only about half the bandwidth of `LINEAR16`. `FLAC` stream encoding supports 16-bit and 24-bit samples, however, not all fields in `STREAMINFO` are supported.  
`AUDIO_ENCODING_MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`AUDIO_ENCODING_AMR` | Adaptive Multi-Rate Narrowband codec. `sampleRateHertz` must be 8000.  
`AUDIO_ENCODING_AMR_WB` | Adaptive Multi-Rate Wideband codec. `sampleRateHertz` must be 16000.  
`AUDIO_ENCODING_OGG_OPUS` | Opus encoded audio frames in Ogg container ([OggOpus](https://wiki.xiph.org/OggOpus)). `sampleRateHertz` must be 16000.  
`AUDIO_ENCODING_SPEEX_WITH_HEADER_BYTE` | Although the use of lossy encodings is not recommended, if a very low bitrate encoding is required, `OGG_OPUS` is highly preferred over Speex encoding. The [Speex](https://speex.org/) encoding supported by Dialogflow API has a header byte in each block, as in MIME type `audio/x-speex-with-header-byte`. It is a variant of the RTP Speex encoding defined in [RFC 5574](https://tools.ietf.org/html/rfc5574). The stream is a sequence of blocks, one block per RTP packet. Each block starts with a byte containing the length of the block, in bytes, followed by one or more frames of Speex data, padded to an integral number of bytes (octets) as specified in RFC 5574. In other words, each RTP header is replaced with a single byte containing the block length. Only Speex wideband is supported. `sampleRateHertz` must be 16000.  
`AUDIO_ENCODING_ALAW` | 8-bit samples that compand 13-bit audio samples using G.711 PCMU/a-law.  
  
### GeminiAsrConfig

Configuration for using Gemini ASR models served via Vertex AI. This message is used to override the default Gemini ASR model or provide additional advanced parameters.

JSON representation  
---  
      
    
    {
      "modelId": string,
      "silenceDurationMs": integer,
      "prefixPaddingMs": integer,
      "startOfSpeechSensitivity": enum ([StartSensitivity](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.StartSensitivity)),
      "endOfSpeechSensitivity": enum ([EndSensitivity](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.EndSensitivity))
    }  
  
Fields  
---  
`modelId` |  `string` Optional. The Gemini ASR model ID used for transcription. This value overrides the default model ID configured on the server. Example: "gemini-3-flash-lite-asr-preview"  
`silenceDurationMs` |  `integer` Optional. The required duration of detected silence (or non-speech) before end-of-speech is committed.  
`prefixPaddingMs` |  `integer` Optional. The required duration of detected speech before start-of-speech is committed.  
`startOfSpeechSensitivity` |  `enum (`[StartSensitivity](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.StartSensitivity)`)` Optional. Start of speech sensitivity.  
`endOfSpeechSensitivity` |  `enum (`[EndSensitivity](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.EndSensitivity)`)` Optional. End of speech sensitivity.  
  
### StartSensitivity

Start of speech sensitivity.

Enums  
---  
`START_SENSITIVITY_UNSPECIFIED` | The default is START_SENSITIVITY_LOW.  
`START_SENSITIVITY_HIGH` | Automatic detection will detect the start of speech more often.  
`START_SENSITIVITY_LOW` | Automatic detection will detect the start of speech less often.  
  
### EndSensitivity

End of speech sensitivity.

Enums  
---  
`END_SENSITIVITY_UNSPECIFIED` | The default is END_SENSITIVITY_LOW.  
`END_SENSITIVITY_HIGH` | Automatic detection ends speech more often.  
`END_SENSITIVITY_LOW` | Automatic detection ends speech less often.  
  
### SipConfig

Defines the SIP configuration.

JSON representation  
---  
      
    
    {
      "createConversationOnTheFly": boolean,
      "inactiveStart": boolean,
      "maxAudioRecordingDuration": string,
      "allowVirtualAgentInteraction": boolean,
      "keepConversationRunning": boolean,
      "copyInboundCallLegHeaders": [
        string
      ],
      "ignoreReinviteMediaDirection": boolean
    }  
  
Fields  
---  
`createConversationOnTheFly` |  `boolean` Asks Dialogflow Telephony to create the conversation provided in the SIP header on the fly when the call comes in.  
`inactiveStart` |  `boolean` Starts the conversation with inactive SDP directives  
`maxAudioRecordingDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Max duration for audio recording. Overrides the default value of 15 min. Max value is 8 hours.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`allowVirtualAgentInteraction` |  `boolean` Allows interactions with a Dialogflow virtual agent even if the call is connected for SIPREC purposes.  
`keepConversationRunning` |  `boolean` Keeps the conversation running even if the call is disconnected.  
`copyInboundCallLegHeaders[]` |  `string` List of inbound call leg headers to be copied to outbound call legs created later.  
`ignoreReinviteMediaDirection` |  `boolean` Ignores any media direction in the reINVITE SDP offer. Reuse the previous media direction.  
  
## Methods  
  
---  
  
### `[clearSuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/clearSuggestionFeatureConfig)`

|  Clears a suggestion feature from a conversation profile for the given participant role.  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/create)`

|  Creates a conversation profile in the specified project.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/delete)`

|  Deletes the specified conversation profile.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/get)`

|  Retrieves the specified conversation profile.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/list)`

|  Returns the list of all conversation profiles in the specified project.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/patch)`

|  Updates the specified conversation profile.  
  
### `[setSuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles/setSuggestionFeatureConfig)`

|  Adds or updates a suggestion feature in a conversation profile.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
