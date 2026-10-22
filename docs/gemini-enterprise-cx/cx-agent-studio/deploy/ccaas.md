---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/ccaas/
title: Google Cloud CCaaS \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:32.644584+00:00
---

# Google Cloud CCaaS  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/ccaas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Google Cloud CCaaS Stay organized with collections  Save and categorize content based on your preferences. 

This guide walks you through the process of connecting an agent application to a [Google Cloud CCaaS](https://cloud.google.com/contact-center/ccai-platform/docs) instance.

## Before you begin

  1. Follow the steps on the [setup and cleanup](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/setup) page to create or configure the project you'd like to use for the deployment. This project must be associated with both your agent application and Google Cloud CCaaS instance and be in the same `region`. Check your project to make sure of the following: 
     * The `Dialogflow API` is enabled.
     * The service account you will use for the deployment has the `Dialogflow API Admin` (`roles/dialogflow.admin`) permission.
  2. [Create and configure](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/create-agent) a CX Agent Studio agent application to use in the deployment.
  3. [Create and configure](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started) a Google Cloud CCaaS contact center to use in the deployment.
  4. The code snippets in this guide assume that you have the [gcloud CLI installed](https://docs.cloud.google.com/sdk/docs/install) and necessary permissions configured.



## Connect an agent application to a new conversation profile

Google Cloud CCaaS uses a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/basics#conversation_profiles) with [`useBidiStreaming`](https://docs.cloud.google.com/dialogflow/priv/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.ConversationProfile) enabled to communicate with CX Agent Studio.

### Example request

The following sample creates a conversation profile with `useBidiStreaming`:

  * PROJECT_ID: Your Google Cloud project ID.
  * REGION: Only `us` and `eu` multi-regions are supported.
  * AGENT_NAME: The name of the CX Agent Studio deployment or agent you want to associate with the conversation profile.
  * CONVERSATION_PROFILE_NAME: Replace this value with the name you want to give the conversation profile.


    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-User-Project: PROJECT_ID" \
      -H "Content-Type: application/json; charset=utf-8" \
      -d '{
            "displayName": "CONVERSATION_PROFILE_NAME",
            "languageCode": "en-US",
            "useBidiStreaming": true,
            "automatedAgentConfig": {
                "agent": "AGENT_NAME"
            }
          }' \
     https://REGION-dialogflow.googleapis.com/v2beta1/projects/PROJECT_ID/locations/REGION/conversationProfiles

### Example response
    
    
    {
      "name": "projects/ccaip-apps-incub-0fcb/locations/global/conversationProfiles/bAp81fGqTg-sp3TUNYTZlw",
      "displayName": "CONVERSATION_PROFILE_NAME",
      "automatedAgentConfig": {
        "agent": "projects/ccaip-apps-incub-0fcb/locations/global/apps/6afaa63d-49a3-4b89-8923-18cbe9b48ae5"
      },
      "languageCode": "en-US",
      "createTime": "2025-08-21T22:11:12.782515Z",
      "updateTime": "2025-08-21T22:11:12.782515Z",
      "useBidiStreaming": true
    }

## Connect an agent application to a pre-existing conversation profile

The conversation profile must be associated with an agent application and configured to enable [`useBidiStreaming`](https://docs.cloud.google.com/dialogflow/priv/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.ConversationProfile).

The following sample creates a conversation profile with `useBidiStreaming`:

### Connect agent application sample request

  * PROJECT_ID: Your Google Cloud project ID.
  * INTEGRATION_ID: Returned in the response. This is the integration ID of your new conversation profile.
  * REGION: Only `us` and `eu` multi-regions are supported.
  * APP_ID: The ID value of the CX Agent Studio agent application you want to associate with the conversation profile.


    
    
    curl -X PATCH \
      -H "x-goog-user-project: PROJECT_ID" \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -d '{"automatedAgentConfig": {"agent": "APP_ID"}}' "https://REGION-dialogflow.googleapis.com/v2beta1/INTEGRATION_ID?updateMask=automatedAgentConfig.agent"

### Connect agent application sample response
    
    
    {
      "name": "projects/ccaip-apps-incub-0fcb/locations/us/conversationProfiles/FRDHwh2gS-O1n5SpoxKLfg",
      "displayName": "bdsac_us_polysynth_agent",
      "automatedAgentConfig": {
        "agent": "projects/ccaip-apps-incub-0fcb/locations/us/apps/6afaa63d-49a3-4b89-8923-18cbe9b48ae5"
      },
      "humanAgentAssistantConfig": {
        "humanAgentSuggestionConfig": {},
        "messageAnalysisConfig": {}
      },
      "sttConfig": {
        "model": "telephony",
        "useLongFormModel": true
      },
      "languageCode": "en-US",
      "updateTime": "2025-08-06T21:35:13.388052Z",
      "telephonySttConfig": {}
    }

### Enable `useBidiStreaming` sample request

  * PROJECT_ID: Your Google Cloud project ID.
  * INTEGRATION_ID: Returned in the response. This is the integration ID of your new conversation profile.
  * REGION: Only `us` and `eu` multi-regions are supported.


    
    
    curl -X PATCH \
      -H "x-goog-user-project:PROJECT_ID" \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -d '{ "useBidiStreaming": true }' "https://REGION-dialogflow.googleapis.com/v2beta1/INTEGRATION_ID?updateMask=useBidiStreaming"

### Enable `useBidiStreaming` sample response
    
    
    {
      "name": "projects/ccaip-apps-incub-0fcb/locations/us/conversationProfiles/FRDHwh2gS-O1n5SpoxKLfg",
      "displayName": "bdsac_us_polysynth_agent",
      "automatedAgentConfig": {
        "agent": "projects/ccaip-apps-incub-0fcb/locations/us/apps/6afaa63d-49a3-4b89-8923-18cbe9b48ae5"
      },
      "humanAgentAssistantConfig": {
        "humanAgentSuggestionConfig": {},
        "messageAnalysisConfig": {}
      },
      "sttConfig": {
        "model": "telephony",
        "useLongFormModel": true
      },
      "languageCode": "en-US",
      "updateTime": "2025-08-06T21:54:12.206269Z",
      "telephonySttConfig": {},
      "useBidiStreaming": true
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
