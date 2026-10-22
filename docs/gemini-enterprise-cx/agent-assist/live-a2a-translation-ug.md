---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/live-a2a-translation-ug/
title: Live A2A translation user guide \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:53.684778+00:00
---

# Live A2A translation user guide  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/live-a2a-translation-ug/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Live A2A translation user guide Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature has limited access. Contact your Google Cloud representative to access private GA features.

Live audio-to-audio (A2A) translation allows agents to communicate seamlessly with customers in their own language. Follow these steps to enable live A2A translation for your customer service setup.

## Before you begin

Ensure you have access to the following before you start the set-up process:

  * [Google Cloud console](https://console.cloud.google.com/) with appropriate permissions.
  * [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs/overview) (`gcloud`) installed and configured.
  * `jq` installed for JSON processing.
  * Allowlist for translation features on your project.



## Step 1: Create a conversation profile and phone number

Follow this process to attach a phone number to a conversation profile without using API calls.

  1. Navigate to the [Conversational Agents (Dialogflow CX) console](https://conversational-agents.cloud.google.com/projects).
  2. Select your project that is on the allowlist: `YOUR_PROJECT_ID`.
  3. Click **Create agent** > **Build your own**.
  4. Choose the **Global** (Global serving, data-at-rest in US) region.
  5. Choose **Flow** instead of **Playbook** , then click **Create**.
  6. Select **Integration** in the panel.
  7. Click **Manage** > **Create** to obtain a new phone number.
  8. In the **Conversation Profile** settings, fill out the **Display Name**. Make a note of this name for later use.
  9. Save the phone number.



## Step 2: Create a generator

  1. Navigate to the [Agent Assist console](https://agentassist.cloud.google.com/).
  2. Choose the same project: `YOUR_PROJECT_ID`.
  3. Go to **Live Translation**.
  4. Click **Create** and enter a name for the generator.
  5. Choose your two languages.
  6. Select **Voice** in the translation channel.
  7. Select **True** for **Conference Mode**.
  8. Click **Save**.



## Step 3: Configure your conversation profile

Follow [these instructions](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform#connect_an_agent_application_to_a_gtp_phone_number) to create a conversation profile with a Google Telephony Platform (GTP) number attached to it. This will create a conversation profile with a virtual agent.

**Note:** Attaching a phone number to the conversation profile creates a virtual agent with a conversation profile. This virtual agent is not needed for A2A workflow, but this is the best UI to get a phone number and link it to the conversation profile.

The following steps help you to configure the conversation profile you created in step 1.

  1. Navigate to **Conversation profiles** > **Suggestion types**.
  2. Select **Live translation** and the generator you created in step 2.
  3. Enable **Advanced suggestion settings** to use unredacted conversation data for suggestion.
  4. Enable **Telephony settings** to use the [bidirectional streaming API](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/bidi-stream-api).
  5. Disable the **Virtual agent** in **Choose to use Dialogflow** , unless you want to configure a custom voice translation announcement (as described in optional step 5). If you want an announcement, keep the **Virtual agent** enabled.
  6. In **Voice Configuration** > **Speech to Text Configuration** , set:
  7. **Audio Encoding** : Linear 16
  8. **Sample Rate Hertz** : 16000
  9. Click **Save**.



## Step 4: Verify the translation

Call the phone number you created in step 1 to verify if the translation is working as expected.

## Optional Step 5: Configure a voice translation announcement

By default, conference mode directly translates audio streams without playing a preliminary greeting. If you kept the virtual agent enabled in step 3, follow these steps to configure a welcome announcement that plays before the live audio translation stage.

### Navigate to the Start Route

  1. Open the [Conversational Agents (Dialogflow CX) Console](https://conversational-agents.cloud.google.com/projects) and select your agent.
  2. In the **Build** tab, select the **Default Start Flow**.
  3. Click the **Start** page.
  4. Click the **Default Welcome Intent** route in the Routes section.



### Update the Fulfillment

  1. Navigate to the **Fulfillment** section of this route.
  2. In the **Agent dialogue** > **Text response** section, remove any existing generic greeting (for example: _Hi, how can I help you?_).
  3. Enter your custom voice translation announcement (for example: _This is an AI-powered translation service_.)
  4. On the same **Fulfillment** panel, click **Add dialogue response** and select **Live agent handoff**.
  5. In the **Metadata/Payload** field for the Live agent handoff, enter an empty JSON object:{}
  6. Click **Save**.



### Verify the announcement

When you place a test call, you should hear the announcement first. The empty JSON payload then initiates an immediate handoff, which transitions the call to the `AGENT_ASSIST_STAGE` where A2A Live Translation begins.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
