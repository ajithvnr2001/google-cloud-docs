---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/gemini-transcribe-live/
title: Gemini transcribe live \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:56.903782+00:00
---

# Gemini transcribe live  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/gemini-transcribe-live/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Gemini transcribe live Stay organized with collections  Save and categorize content based on your preferences. 

Use Gemini to instantly convert streaming audio into text for live conversations. Gemini transcribe live offers reliable instant intermediate transcriptions. It is optimized for real-time streaming transcription through the `StreamingAnalyzeContent (SAC)` or `BidiStreamingAnalyzeContent (Bidi-SAC)` APIs. To ensure optimal performance use up to 100 phrase sets or adaptation terms.

## Set up guide

Follow these steps to enable Gemini transcribe live.

### Console

When you [create or update a conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) in the [Agent Assist console](https://agentassist.cloud.google.com/), follow these steps to use the Gemini model for Speech-to-Text API.

  1. Navigate to **Conversation profiles** and select your profile.
  2. Enable **Use Bidirectional Streaming API** in **Telephony settings** if you are using the Bidi-SAC API.
  3. In the **Speech to Text Config** section, choose the **Gemini transcribe live** model.
  4. Set the **Language**.
  5. Set **Audio encoding** and **Sample rate** to match your input audio format.
  6. Select **Use Long Form Model for AA Telephony SipRec Integration**.
  7. (Optional) Configure **Phrases for speech adaptation** to improve accuracy with model adaptation. Each term must be less than or equal to 100 terms and each term must be less than or equal to 100 characters.



### REST API

You can call the API directly to create or update a conversation profile, as shown in the following example.

Example configuration:
    
    
    {
    "name": "projects/PROJECT_ID/locations/global/conversationProfiles/CONVERSATION_PROFILE_ID",
        "display_name": "CONVERSATION_PROFILE_NAME",
        "stt_config": {
            "use_long_form_model": true,
            "audio_encoding": "AUDIO_ENCODING_",
            "sample_rate_hertz": ,
            "use_gemini_asr": true
        },
        "language_code": "en-US"
    }
    

**Note:** The `model_id` field in `GeminiAsrConfig` remains in preview, which applies wherever you set it. You can set `model_id` in the conversation profile (`stt_config.gemini_asr_config`), or per request (`InputAudioConfig.gemini_asr_config` and the voice session config in `BidiStreamingAnalyzeContentRequest`). Leave `model_id` unset to use the default model.

## Regional and language support

To support all Agent Assist regions, Gemini transcribe live remaps traffic to the Vertex AI supported global, US, and EU regions. See the [supported languages list](https://docs.cloud.google.com/speech-to-text/docs/models/chirp-3#language_availability_for_transcription) for available languages.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
