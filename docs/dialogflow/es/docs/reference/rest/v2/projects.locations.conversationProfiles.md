---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles
title: REST Resource: projects.locations.conversationProfiles \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:26.233139+00:00
---

# REST Resource: projects.locations.conversationProfiles  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.locations.conversationProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConversationProfile
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
  
## Methods  
  
---  
  
### `[clearSuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/clearSuggestionFeatureConfig)`

|  Clears a suggestion feature from a conversation profile for the given participant role.  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/create)`

|  Creates a conversation profile in the specified project.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/delete)`

|  Deletes the specified conversation profile.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/get)`

|  Retrieves the specified conversation profile.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/list)`

|  Returns the list of all conversation profiles in the specified project.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/patch)`

|  Updates the specified conversation profile.  
  
### `[setSuggestionFeatureConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.conversationProfiles/setSuggestionFeatureConfig)`

|  Adds or updates a suggestion feature in a conversation profile.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-14 UTC."],[],[]] 
