---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pub-sub/
title: Enable Cloud Pub/Sub notifications for CCAI Agent Assist events \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:33:47.599005+00:00
---

# Enable Cloud Pub/Sub notifications for CCAI Agent Assist events  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pub-sub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Enable Cloud Pub/Sub notifications for CCAI Agent Assist events Stay organized with collections  Save and categorize content based on your preferences. 

Enabling [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub) notifications lets you receive a notification each time an Agent Assist event completes. You can configure Agent Assist to send a notification for all events or only specified events, including Agent Assist suggestions, conversation lifecycle information, and live transcripts.

## Prerequisites

  1. Enable the [Dialogflow API](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2-overview).
  2. Follow the instructions to [create a Cloud Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic-console).



## Enable Cloud Pub/Sub notifications

You can configure Agent Assist to send a notification for _all events_ or for _specified events_ in your **conversation profile**.

A [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) configures a set of parameters that control the suggestions or notifications made to an agent during a conversation. You have the option of configuring [Cloud Pub/Sub](https://docs.cloud.google.com/pubsub) notifications either using the [Agent Assist console](https://agentassist.cloud.google.com) or by calling the API directly. You can configure each type of notification separately, using the topics that you've created.

For more details about Cloud Pub/Sub configuration parameters, see the [`conversationProfile` reference documentation](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles).

### Enable Cloud Pub/Sub notifications using the Agent Assist console

**Note:** You can use the Agent Assist simulator to create a conversation. In this case, notifications for live transcripts and suggestions are published to Google internal Pub/Sub topics instead of the ones you configured in your conversation profiles.

When you create a new conversation profile using the [Agent Assist console](https://agentassist.cloud.google.com), you can select which notification types you'd like to receive using the topics you've created:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/console-pubsub.png)

### Enable Cloud Pub/Sub notifications using the API

If you prefer to call the API directly to create or update a conversation profile, check this section for the locations you should configure in the [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) resource.

The following example is configured to enable all Cloud Pub/Sub notifications that match a designated `TOPIC_ID`.
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/conversationProfiles/CONVERSATION_PROFILE_ID",
      "displayName": "CONVERSATION_PROFILE_NAME",
      "automatedAgentConfig": {
      },
      "humanAgentAssistantConfig": {
        "notificationConfig": {
          "topic": "projects/PROJECT_ID/topics/FEATURE_SUGGESTION_TOPIC_ID",
          "messageFormat": "JSON"
        },
        "humanAgentSuggestionConfig": {
          "featureConfigs": [{
            "enableEventBasedSuggestion": true,
            "suggestionFeature": {
              "type": "ARTICLE_SUGGESTION"
            },
            "conversationModelConfig": {
            }
          }]
        },
        "messageAnalysisConfig": {
        }
      },
      "notificationConfig": {
        "topic": "projects/PROJECT_ID/topics/CONVERSARION_LIFECYCLE_TOPIC_ID",
        "messageFormat": "JSON"
      },
      "newMessageEventNotificationConfig": {
        "topic": "projects/PROJECT_ID/topics/LIVE_TRANSCRIPT_TOPIC_ID",
        "messageFormat": "JSON"
      },
      "newRecognitionResultNotificationConfig": {
        "topic": "projects/PROJECT_ID/topics/NEW_RECOGNITION_RESULT_TOPIC_ID",
        "messageFormat": "JSON"
      },
      "languageCode": "en-US"
    }

### Configuration of the Cloud Pub/Sub message

Notification | Trigger | Configuration in [`ConversationProfile`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles)  
---|---|---  
suggestion_event | When Agent Assist generates a suggestion | [`ConversationProfile.humanAgentAssistantConfig.notificationConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.HumanAgentAssistantConfig.FIELDS.notification_config)  
Set [`SuggestionFeatureConfig.enableEventBasedSuggestion`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.SuggestionFeatureConfig.FIELDS.enable_event_based_suggestion) to true for selected features  
  
**Supported features: ARTICLE_SUGGESTION, FAQ AND DIALOGFLOW_ASSIST**  
life_cycle_event | When conversation open or close | [`ConversationProfile.notificationConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.FIELDS.notification_config)  
new_message_event | When a new message/utterance transcript appears | [`ConversationProfile.newMessageEventNotificationConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.FIELDS.new_message_event_notification_config)  
new_recognition_result_event | When an intermediate transcript is available | [`ConversationProfile.newRecognitionResultNotificationConfig`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile.FIELDS.new_recognition_result_notification_config)  
  
### Content of the Cloud Pub/Sub message

The content of the [Cloud Pub/Sub message](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage) depends on the event that triggers that Cloud Pub/Sub notification.

Notification | Message Data | Message Data Example  
---|---|---  
suggestion_event | [`HumanAgentAssistantEvent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/HumanAgentAssistantEvent) | {  
"conversation": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID",  
"participant": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID/participants/PARTICIPANT_ID",  
"suggestionResults": [[`SuggestionResult`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AnalyzeContentResponse#SuggestionResult)]  
}  
life_cycle_event | [`ConversationEvent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent) | {  
"conversation": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID",  
"type": "CONVERSATION_STARTED"  
}  
new_message_event | [`ConversationEvent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent) | {  
"conversation": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID",  
"type": "NEW_MESSAGE",  
"newMessagePayload": [`Message`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Message)  
}  
new_recognition_result_event | [`ConversationEvent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent) | {  
"conversation": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID",  
"type": "NEW_RECOGNITION_RESULT",  
"newRecognitionResultPayload": [`StreamingRecognitionResult`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent#StreamingRecognitionResult)  
}  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
