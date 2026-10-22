---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway/
title: Dialogflow CX Phone Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:22.088304+00:00
---

# Dialogflow CX Phone Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Dialogflow CX Phone Gateway Stay organized with collections  Save and categorize content based on your preferences. 

The Dialogflow CX Phone Gateway feature provides a telephone interface to your agent. It is used to build conversational IVR (interactive voice response) solutions that integrate with the rest of your call center network. With the phone gateway, you can select a telephone number hosted by Google and connect it to your agent.

Also see [Call companion](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion).

## Limitations

The following limitations apply:

  * This integration currently works only with agents created in the `global` [region](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region). If you need a local telephone number hosted in a specific region, please reach out to your Google account team.
  * Only US phone numbers are supported.
  * There are [quotas and limits](https://docs.cloud.google.com/dialogflow/quotas) for this feature. If you receive a busy signal or the call drops, you may have exceeded your quota.
  * [Partial response](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) is supported for all routes except the [Default welcome intent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#welcome) route on the [Default start flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#start)'s start page.
  * This integration uses the [`phone_call`](https://docs.cloud.google.com/speech-to-text/docs/speech-to-text-requests#select-model) speech model, even if other speech models are specified in the console or in the conversation profile, unless you enable the [**Override request-level speech model**](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#stt-model-selection) setting.



## Supported languages

The Dialogflow CX Phone Gateway feature supports all [languages that provide both STT and TTS](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language).

## Set up a phone gateway

To set up your gateway, follow these steps:

  1. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects). Choose your Google Cloud project and select your agent.
  2. Select the **Manage** tab. Click **Integrations** in the left sidebar menu and click **Try it** for **CX Phone Gateway**.
  3. Click **+Create**. 
     1. Select the country code for the phone number.
     2. Optional. Select preferred area codes.
     3. Click **Request**.
  4. Select a number. 
     1. Choose a telephony number from the list.
     2. Enter a display name for configuring the conversation profile associated with the phone number.
     3. Optional. Click **Show more settings** and update the settings.
     4. Click **Save**.
  5. Completion: 
     1. The gateway is now active.
     2. You can click the phone number under the **Phone Numbers** page to check and update settings.



## Call the telephone number

You can now call the number and follow the simple voice prompts. If the agent reaches end session state, the call ends.

## Retrieve caller phone number

You can retrieve the `caller_id` value from the payload field.

## Play pre-recorded audio

You can use fulfillment options to [play pre-recorded audio](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#audio). The audio must contain a single channel (mono) of [μ-law](https://en.wikipedia.org/wiki/%CE%9C-law_algorithm) encoded audio at 8kHz and be hosted on [Cloud Storage](https://docs.cloud.google.com/storage/docs).

## Transfer a call

You can use fulfillment options to [transfer a call](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#transfer).

## Webhook request payload

If you have configured a [webhook](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook), this integration will populate the `WebhookRequest.payload` field with the caller ID of the end-user. The format looks like the following:
    
    
    "payload": {
      "telephony": {
        "caller_id": "+18558363987"
      }
    }
    

## Delete a number

You can click the **Delete** icon of a phone number to delete that number.

## Delete an agent

You can delete agents by deleting your Google Cloud project. If you want to keep using your Google Cloud project, you must delete all the phone numbers associated with your phone gateway agent before you [delete the agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#del).

Please see Delete a number section for phone number deletion.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
