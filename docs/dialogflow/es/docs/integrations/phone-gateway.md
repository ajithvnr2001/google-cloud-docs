---
url: https://docs.cloud.google.com/dialogflow/es/docs/integrations/phone-gateway/
title: Dialogflow phone gateway \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:10.373767+00:00
---

# Dialogflow phone gateway  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/integrations/phone-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Dialogflow phone gateway Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Dialogflow phone gateway feature provides a telephone interface to your agent. It's used to build conversational IVR (interactive voice response) solutions that integrate with the rest of your call center network. You can select a telephone number hosted by Google.

For phone gateway pricing and quota information, see the [Pricing](https://cloud.google.com/dialogflow/pricing) and [Quotas and Limits](https://docs.cloud.google.com/dialogflow/quotas) pages.

## Limitations

### Language support

This integration only supports use of one language per agent.

If [enhanced speech models](https://docs.cloud.google.com/dialogflow/docs/data-logging) are enabled for the agent, then this integration only supports the following languages:

  * English (en)
  * English - US (en-US)



If enhanced speech models are disabled for the agent, see the **Phone** column on the [Language reference](https://docs.cloud.google.com/dialogflow/docs/reference/language) page for a list of supported languages.

### Phone number support

Only US phone numbers are supported, both for incoming calls and for call transfers.

## Before you begin

You should do the following before reading this guide:

  1. Read [Dialogflow basics](https://docs.cloud.google.com/dialogflow/docs/basics).
  2. Perform [setup steps](https://docs.cloud.google.com/dialogflow/docs/quick/setup).



## Create an agent

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com). 
  2. Sign in to the console if prompted. For more information, see the [Dialogflow console overview](https://docs.cloud.google.com/dialogflow/docs/console). 
  3. In the sidebar menu, expand **Loading agents**. 
  4. Click **Create new agent**. 
  5. Enter the agent name, default language, and default time zone. 
  6. Enter an existing project. To let the Dialogflow console create a project, select **Create a new Google project**. 
  7. Click **Create**. 



## Enable beta features

Ensure that beta features are enabled: 

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Click the settings _settings_ button next to the agent's name.
  4. Scroll down while on the **General** tab and ensure that **Beta Features** is enabled.
  5. If you have made changes, click **Save**.



## Set up a phone gateway

To set up your gateway, follow these steps:

  1. Select a provider: 
     1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
     2. Select your agent.
     3. Click **Integrations**.   
![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/integrations-left-panel.png)
     4. Click **Dialogflow Phone Gateway**.   
![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/telephony-integration-button.png)
  2. Configure Phone Gateway: 
     1. Select the language.
     2. Select the country code for the telephone number.
     3. (Optional) Select preferred area codes.
     4. Click **Next**.   
![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/telephony-1.png)
  3. Select a number: 
     1. Choose a telephone number from the list.
     2. Click **Create**.   
![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/telephony-2.png)
  4. Complete setup: 
     1. The gateway is now active.
     2. Optionally, change the [environment](https://docs.cloud.google.com/dialogflow/docs/agents-versions).
     3. Save the displayed telephone number and close the dialog window. You can click the **Dialogflow Phone Gateway** integrations button again to retrieve this information.   
![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/telephony-3.png)



## Call the telephone number

You can now call the number and follow the simple voice prompts. The interactions are defined in your agent.

**Note:** There are [quotas and limits](https://docs.cloud.google.com/dialogflow/quotas) for this feature. If you receive a busy signal or the call drops, you may have exceeded your quota.**Note:** If you decide to delete your agent but keep using your Google Cloud project, disable the Phone Gateway integration before the agent deletion.

## Examine the intents

Now that you have a working phone gateway agent, let's look at the intents you imported. This will help you understand how to build your own Phone Gateway agents.

### Welcome the caller

When you called the number, the agent greeted you and provided a list of options. Follow these steps to see how this was configured:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select your agent.
  3. Click **Intents**.
  4. Click **Default Welcome Intent**.
  5. Scroll down to the **Events** section. Notice that both **Welcome (`WELCOME`)** and **Telephony Welcome (`TELEPHONY_WELCOME`)** [events](https://docs.cloud.google.com/dialogflow/docs/events-overview) are present, which means that all types of welcome events will trigger this intent. As an alternative, you could create separate intents, each dedicated to a specific welcome event.
  6. Scroll down to the **Responses** section and click the **Dialogflow Phone Gateway** tab.
  7. Notice that the **Synthesize speech** response contains the welcome message you heard when calling the number.



### Response to test command

After you responded with "test," the agent presented a new list of options. Follow these steps to see how this was configured:

  1. Click **Intents**.
  2. Click **Test Telephony Intent**.
  3. Scroll down to the **Responses** section and click the **Dialogflow Phone Gateway** tab.
  4. Note that the **Synthesize speech** response contains the response you heard after you said "test."



### Setting context

After saying "test," there are two possible commands you can make: "transfer" or "terminate." This is not a limitation of Phone Gateway agents; it's how this intent is defined. The intents associated with these commands are provided with [context](https://docs.cloud.google.com/dialogflow/docs/contexts-overview). Follow these steps to see how this was configured:

  1. Scroll to the **Context** section at the top.
  2. Notice the **TestTelephonyIntent-followup** output context.
  3. Click **Intents**.
  4. Click the expansion button next to **Test Telephony Intent**.
  5. Click **Test Telephony Intent - Terminate**
  6. Scroll to the **Context** section at the top.
  7. Notice the **TestTelephonyIntent-followup** input context.



### Terminate the call

When you responded with "terminate," the agent said "goodbye" and terminated the call. Follow these steps to see how this was configured:

  1. Scroll down to the **Training phrases** section and note the phrases used to terminate the call.
  2. Scroll down to the **Responses** section and click the **Dialogflow Phone Gateway** tab.
  3. Notice that the **Synthesize speech** response contains "goodbye."
  4. Notice that **Set this intent as end of conversation** is enabled. If this is enabled, Dialogflow terminates the phone call after playing all other audio prompts. 

**Note:** If you are using [fulfillment](https://docs.cloud.google.com/dialogflow/docs/fulfillment-overview), you can terminate a call by setting the `end_interaction` field of the [WebhookResponse](https://docs.cloud.google.com/dialogflow/docs/reference/rpc/google.cloud.dialogflow.v2beta1#webhookresponse) message.

## Phone gateway rich response messages

The intents for this example use [Rich response messages](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages) for Phone Gateway responses. These are the types that you can use:

  * [Play audio](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#audio): Plays the audio file provided. Specify the URI to a Cloud Storage object containing the audio to be played. For example, 'gs://bucket/object'. The object must contain a single channel (mono) of linear PCM audio (2 bytes/sample) at 8kHz.
  * [Synthesize speech](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#tts): Synthesizes the supplied text to audio and plays it. Alternatively, you can enable **Use response from the DEFAULT tab as the first response** , which will use the default response to synthesize a speech response. If you only define default responses and don't enable **Use response from the DEFAULT tab as the first response** , only the text populated in `QueryResult.fulfillment_text` (populated with a randomly selected text response) is synthesized to audio.
  * [Transfer call](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#transfer): Transfers the caller to another number. The time duration spent on the transferred call is included in the total call duration, and Dialogflow [charges](https://cloud.google.com/dialogflow/pricing) are applied until the call is ended.

**Note:** When you add a rich message, you can hover over the **?** button to get more information about the message and its inputs.

## Agent settings

You can control various aspects of speech synthesis. See [Agent speech settings](https://docs.cloud.google.com/dialogflow/docs/agents-settings#speech).

## Use the Dialogflow simulator

When testing or experimenting with a phone gateway agent, you don't need to make a phone call. You can interact with the agent and receive audio responses using the [Dialogflow simulator](https://docs.cloud.google.com/dialogflow/docs/console#simulator):

  1. Type "hello" and press the **return key**.
  2. Change **Default Response** to **Dialogflow Phone Gateway**.
  3. Click the **Play Audio** button to hear the agent response.
  4. Continue the conversation with the agent.



## Toll-free numbers

You can request a phone number with an 833 area code. Note that toll-free numbers are [priced higher](https://cloud.google.com/dialogflow/pricing).

## Events

The following [events](https://docs.cloud.google.com/dialogflow/docs/events-overview) are invoked by this integration:

Event | Description  
---|---  
`TELEPHONY_WELCOME` | Triggered when someone calls the phone number associated with your Dialogflow agent.  
  
## Agent warmup

When an end-user calls a Dialogflow Phone Gateway agent, Dialogflow starts by loading the agent for a quick response to the initial end-user utterance. While the agent is loading, the phone keeps ringing. Dialogflow accomplishes this by sending a detect intent request to your agent. The text of this request is `TELEPHONY_WARMUP`.

## Retrieve caller phone number

If you use the Dialogflow Essentials [edition](https://docs.cloud.google.com/dialogflow/docs/editions#cmp), you can retrieve the `caller_id` value from the `OriginalDetectIntentRequest.payload` field in the [webhook request](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-webhook#webhook_request). In the Dialogflow Trial edition, the `caller_id` value is redacted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
