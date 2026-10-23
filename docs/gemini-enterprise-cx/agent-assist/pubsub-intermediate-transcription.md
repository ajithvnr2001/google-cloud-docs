---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pubsub-intermediate-transcription/
title: Pub/Sub intermediate transcription \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:32.922903+00:00
---

# Pub/Sub intermediate transcription  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pubsub-intermediate-transcription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Pub/Sub intermediate transcription Stay organized with collections  Save and categorize content based on your preferences. 

An intermediate transcript is an interim result of speech recognition from the [Cloud Speech-to-Text API](https://docs.cloud.google.com/speech-to-text/docs/reference/rest). The intermediate transcript can change upon further analysis of the audio. Configure intermediate transcription delivery with a [Cloud Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic) or use gRPC for [voice transcription](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription) delivery.

You can configure [delivery of the final result of speech recognition](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pub-sub) with `ConversationProfile.newMessageEventNotificationConfig` or with gRPC responses.

## Create or update your conversation profile

Follow these steps when you create or update a conversation profile. Agent Assist does not redact intermediate transcripts.

### Console

  1. Within the Agent Assist console, click **Conversation profiles**.
  2. Click the name of a profile or **\+ Create**.
  3. Navigate to **Pub/Sub notifications** , and select **Transcription intermediate result notifications**.
  4. Enter the Pub/Sub topic you created for receiving intermediate transcripts, and select your message format.
  5. Click **Save**.



### REST

  1. Configure a Pub/Sub topic for receiving intermediate transcriptions with `ConversationProfile.newRecognitionResultNotificationConfig`.

**Note:** You can configure the redaction of final transcripts with [`use_redacted_data`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#notificationconfig) at `newMessageEventNotificationConfig`.

Example Configuration:
    
    
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
      "topic": "projects/PROJECT_ID/topics/NEW_MESSAGE_TOPIC_ID",
      "messageFormat": "JSON"
    },
    "newRecognitionResultNotificationConfig": {
      "topic": "projects/PROJECT_ID/topics/INTERMEDIATE_TRANSCRIPT_TOPIC_ID",
      "messageFormat": "JSON"
    },
    "languageCode": "en-US"
    }

## Optional: Enable message ordering

Conversation ID is the ordering key for published Pub/Sub transcript messages. To receive the messages in order, [set the message ordering property](https://docs.cloud.google.com/pubsub/docs/ordering#enable_message_ordering) on the subscription you receive messages from.

## Optional: Fetch more information

Dialogflow appends conversation IDs, message IDs, participant IDs, and participant roles to the [Pub/Sub messages](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage#attributes) as attributes. You can access these attributes with [`PubsubMessage.attributes`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage#attributes) or you can fetch them together with the following Pub/Sub message data by [subscribing with custom attributes](https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscriber-async-pull-custom-attributes).

  * The attribute key of participant ids: `participant_id`
  * The attribute key of message ids: `message_id`
  * The attribute key of conversation ids: `conversation_id`
  * The attribute key of participant roles: `participant_role`



The following is an example of a set of attributes: {`"conversation_id": "c_id"`, `"participant_id": "p_id"`}

## Optional: Subscription configurations

Follow these guidelines to customize your Pub/Sub subscription for handling transcript delivery:

  * [Handle message failures with subscription retry policy](https://docs.cloud.google.com/pubsub/docs/handling-failures#subscription_retry_policy)
  * [Replay previously-acked messages or purge messages](https://docs.cloud.google.com/pubsub/docs/replay-overview)
  * [Forward undelivered messages to a topic for unprocessed messages](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
