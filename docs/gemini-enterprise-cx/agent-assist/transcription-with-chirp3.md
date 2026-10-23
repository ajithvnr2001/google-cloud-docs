---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription-with-chirp3/
title: Use transcription with Speech-to-Text Chirp 3 \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:05.402874+00:00
---

# Use transcription with Speech-to-Text Chirp 3  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription-with-chirp3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Use transcription with Speech-to-Text Chirp 3 Stay organized with collections  Save and categorize content based on your preferences. 

Chirp 3, the latest generation of Google's multilingual Automatic Speech Recognition (ASR)-specific generative models offered by Google Cloud's Speech-to-Text (STT) API v2, is available for [Voice transcription](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/transcription).

## Set up

Follow these steps to enable transcription with Speech-to-Text Chirp 3.

### Console

When you create or update a conversation profile using the [Agent Assist console](https://agentassist.cloud.google.com/), follow these steps to configure Speech-to-Text settings to use the Chirp 3 model.

  1. Click **Conversation profiles**.
  2. Click the name of your profile.
  3. Navigate to the **Speech to Text Config** section.
  4. Choose **Chirp 3** for the model.
  5. (Optional) Select **Use Long Form Model for AA Telephony SipRec Integration** if the audio is transmitted through Telephony Integration.
  6. (Optional) Configure **Language Code** and up to one **Alternative Language Codes** for [language-restricted transcription](https://docs.cloud.google.com/speech-to-text/v2/docs/chirp_3-model#perform_a_language-restricted_transcription).
  7. (Optional) Configure **auto** as the language code for [language-agnostic transcription](https://docs.cloud.google.com/speech-to-text/v2/docs/chirp_3-model#perform_a_language-agnostic_transcription).
  8. (Optional) Configure **Phrases for speech adaptation** to improve accuracy with [model adaptation](https://docs.cloud.google.com/speech-to-text/v2/docs/chirp_3-model#improve_accuracy_with_model_adaptation).



### REST API

You can call the API directly to create or update a conversation profile. Enable STT V2 with the `ConversationProfile.sttConfig.useSttV2` field, as shown in the following example. Example Configuration: 
    
    
    {
    "name": "projects/PROJECT_ID/locations/global/conversationProfiles/CONVERSATION_PROFILE_ID",f
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
    "sttConfig": {
      "model": "chirp_3",
      "useSttV2": true,
    },
    "languageCode": "en-US"
    }

## Best practices

Follow these suggestions to get the most from voice transcription with Chirp 3 model.

### Audio streaming

To maximize Chirp 3 performance, send audio in near real time. This means if you have X seconds of audio, stream it in roughly X seconds. Break your audio into small chunks, each with a frame size of 100 ms. For more audio streaming best practices, see the [Speech-to-Text documentation](https://docs.cloud.google.com/speech-to-text/v2/docs/best-practices).

### Use speech adaptation

Use transcription with Chirp 3 speech adaptation only with inline phrases configured in the conversation profile.

### Use without extended streaming

When you use Chirp 3 for voice transcription, avoid enabling [extended streaming](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/extended-streaming). Extended streaming requires a model that supports the [single utterance](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#google.cloud.speech.v1.StreamingRecognitionConfig.FIELDS.bool.google.cloud.speech.v1.StreamingRecognitionConfig.single_utterance) configuration.

## Regional and language support

Chirp 3 is available for all [Speech-to-Text languages](https://docs.cloud.google.com/speech-to-text/v2/docs/chirp_3-model#language_availability_for_transcription) with different launch readiness, and in all [Agent Assist regions](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/regionalization) except `northamerica-northeast1`, `northamerica-northeast2`, and `asia-south1`.

## Quotas

The number of transcription requests using the Chirp 3 model is limited by the `SttV2StreamingRequestsPerMinutePerResourceTypePerRegion` quota with `chirp_3` labeled as the resource type. See the Google Cloud [quotas guide](https://docs.cloud.google.com/docs/quotas/view-manage#managing_your_quota_console) for information on quota usage and how to request a quota increase.

For quotas, transcription requests to the global and US multi-region Dialogflow endpoints are in the `us-central1` region.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
