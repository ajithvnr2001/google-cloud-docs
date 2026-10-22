---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-nice/
title: Agent Assist for Salesforce voice integration with NiCE CXone \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:23.338706+00:00
---

# Agent Assist for Salesforce voice integration with NiCE CXone  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-voice-nice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist for Salesforce voice integration with NiCE CXone Stay organized with collections  Save and categorize content based on your preferences. 

This voice integration uses the [NiCE CXone Agent for Service Cloud Voice (BYOT)](https://help.nicecxone.com/content/agent/agentforscv/agentforservicecloudvoiceagent.htm) Salesforce App to allow your agents to accept NiCE CXone calls in Salesforce Service Cloud Voice. Agent Assist uses the voice call stream from [NiCE CXone Agent Assist Hub](https://help.nicecxone.com/content/aiassistantsandbots/agentassisthub/agentassisthub.htm) to provide suggestions to your agents in the [Salesforce Lightning Service Console](https://help.salesforce.com/s/articleView?id=service.console_lex_service_intro.htm&type=5). The following diagram illustrates this integration architecture:

![Architecture for the Agent Assist and NiCE CXone integration with Salesforce](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/salesforce_nice_voice_architecture.jpg)

**Figure 1.** Integration architecture for Salesforce voice with Agent Assist and NiCE CXone.

## Before you begin

To integrate Agent Assist UI modules with Salesforce, you need access to the following resources:

  * [Salesforce and Agent Assist resources](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-byb)
  * [Agent Assist for Salesforce app](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup)
  * [NiCE CXone instance](https://www.nice.com/products)
  * [NiCE CXone Agent Assist Hub add-on license](https://www.nice.com/products/agent-assist-hub)

The NiCE CXone Agent Assist Hub add-on allows your NiCE CXone instance to send voice call media streams to Agent Assist. NiCE CXone is a licensed product.

  * [NiCE business unit](https://help.nicecxone.com/content/acd/businessunits/businessunit.htm) number

  * [NiCE point of contact (POC) phone number](https://help.nicecxone.com/content/acd/channels/additionalchannelfeatures/pointsofcontact/pointsofcontact.htm)

The number that you use to test this Agent Assist integration is the one your end users call to talk to your agents.




## Step 1: Configure NiCE CXone Studio and NiCE CXone Agent Assist Hub

This step describes all the configurations necessary in your NiCE CXone instance.

### Configure call flow with NiCE CXone Studio

Configure a programmatic call flow with [NiCE CXone Studio](https://help.nicecxone.com/content/studio/studio.htm) to route incoming calls to your agents and send the call media streams to Agent Assist. Follow these steps to configure your NiCE CXone Studio call flow:

  1. Sign in to the NiCE CXone console.
  2. Click apps to open the **Applications** menu > **Omnichannel Routing** > **Studio**.
  3. On the Studio page, create a **New Script**.



Configure this call flow with the following NiCE CXone Studio activators and actions:

  * [**Begin**](https://help.nicecxone.com/content/Studio/actionscx/begin/begin.htm): This becomes active when a call comes into your NiCE POC phone number.
  * [**Reqagent**](https://help.nicecxone.com/content/Studio/actions/reqagent/reqagent.htm): This action sends the call to a specific skill. Select the skill associated with the agents who you would like to receive calls.
  * [**Music**](https://help.nicecxone.com/content/studio/actions/music/music.htm): This action plays hold music.
  * [**Wait**](https://help.nicecxone.com/content/studio/actions/wait/wait.htm): This action suspends the flow until something else is activated.



Next, use the following NiCE CXone Studio activators and actions to configure what happens when an agent answers an incoming call:

  * [**Onanswer**](https://help.nicecxone.com/content/studio/actions/onanswer/onanswer.htm): This action is activated when an agent answers a call.
  * [**Ziptone**](https://help.nicecxone.com/content/studio/actions/ziptone/ziptone.htm): This plays a beep when an agent picks up the phone in a NiCE CXone agent desktop, such as the NiCE CXone Agent for Service Cloud Voice (BYOT) softphone.
  * [**Agent Assist**](https://help.incontact.com/Content/Studio/Actions/AgentAssistV1/AgentAssistV1.htm): This action requires a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile). This action is responsible for creating a conversation and sending an incoming call's media streams to Dialogflow, so that the Agent Assist UI modules LWC can render the transcript and Agent Assist suggestions in Salesforce. See the [NiCE CXone Studio integration documentation](https://help.staging.nice-incontact.com/content/studio/integrations/agentassisthub/googleccai.htm) for configuration details.



You can also configure Agent Assist for outbound calls with the following NiCE CXone Studio activators and actions:

  * [**Placecall**](https://help.nicecxone.com/content/studio/actions/placecall/placecall.htm): You can use this action to initiate the call and connect the Agent Assist action to the `OnAnswer` branch of `Placecall`.
  * [**Onanswer**](https://help.nicecxone.com/content/studio/actions/onanswer/onanswer.htm)
  * [**Agent Assist**](https://help.incontact.com/Content/Studio/Actions/AgentAssistV1/AgentAssistV1.htm): Activate this action when the remote party answers an outbound call.



## Step 2: Install a NiCE CXone Agent for Service Cloud Voice (BYOT)

Salesforce provides the add-on license Service Cloud Voice (SCV), which allows integration of third-party softphones with your Salesforce instance. NiCE CXone provides a SCV add-on called NiCE CXone Agent for Service Cloud Voice (BYOT). Follow NiCE's documentation to [set up NiCE CXone Agent for Service Cloud Voice (BYOT)](https://help.nicecxone.com/content/agent/agentapplicationadministration/agentforscv/setupagentforscv.htm) in your SCV-enabled Salesforce instance.

## Step 3: Add Agent Assist module to a record page

Add Agent Assist to the [voice call record page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup#record-pages) for it to be visible to human agents.

## Step 4: Agent Assist for Salesforce settings

Configure [Agent Assist for Salesforce settings](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup#configure-aa-settings).

### Add the NiCE CXone `conversationIDPrefix` to skillsets

  1. When you create a [skillset](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup#skillsets), add `conversationIDPrefix` in the following code:
         
         BusNo-{NiceBusinessUnitNumber}_ContactId-
         

  2. Replace {NiceBusinessUnitNumber} with your NiCE Business Unit number. The resulting value should look like the following:
         
         BusNo-1234567_ContactId-
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
