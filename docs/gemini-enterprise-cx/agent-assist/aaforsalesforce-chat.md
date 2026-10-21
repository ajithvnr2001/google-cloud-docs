---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-chat/
title: Agent Assist for Salesforce chat integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:25.909011+00:00
---

# Agent Assist for Salesforce chat integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist for Salesforce chat integration Stay organized with collections  Save and categorize content based on your preferences. 

Agent Assist uses UI modules to provide information, suggestions, and responses to human agents during chat conversations in Salesforce messaging. Follow these steps to integrate Agent Assist into your Salesforce messaging experience.

## Before you begin

Follow the instructions in the [Salesforce integration setup guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup) to integrate Agent Assist UI modules with Salesforce.

## Enhanced chat

Enhanced Chat is a Salesforce feature that serves as a messaging channel so agents can handle customer service chat conversations directly from your website or mobile app. Enhanced Chat offers key capabilities such as autonomous issue resolution, escalation to service representatives, and interactive content. Follow these steps to enable Enhanced Chat in your Salesforce account and connect it with Agent Assist.

### Step 1: Install messaging component

Follow these steps to install messaging components:

  1. Go to the Salesforce website and sign in.

[Salesforce](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tao000004NWzNAAW)

  2. Click apps **App Launcher**.

  3. In the search field, enter **Agent Assist Settings** , and click the result.

  4. Click **Messaging** > **Install**.




### Step 2: Enable digital experience

Follow these steps to activate the digital experience needed to support enhanced chat and messaging capabilities:

  1. Navigate to **Setup** > **Quick find** and enter a search for **Digital experience**.
  2. Enable **Enable digital experience**.
  3. Click **Save**.



### Step 3: Configure a user

Follow these steps to configure a user for enhanced chat:

  1. Navigate to **Setup** > Quick find, and enter **Users**.
  2. Choose an option: 
     * Click **Users** page and confirm that **Service cloud user** is enabled.
     * Click **Edit** and enable **Service cloud user**.
  3. Navigate to the **User** page > **Permission set license assignments**.
  4. Click **Edit assignments**.
  5. Confirm the user is **Enhanced chat user** and **Messaging user**.
  6. Navigate to the **User** page > **Permission set assignments**.
  7. Confirm the user has Agent Assist messaging permissions. Agent Assist messaging displays the **Available (messaging)** and **Busy** statuses.



### Step 4: Create a messaging channel

When you create a messaging channel, Salesforce messaging automatically generates an embedded service deployment. Follow these steps to create a messaging channel and embedded service deployment:

  1. Navigate to **Setup** > **Messaging settings**.
  2. Click **New channel**.
  3. For built-in channels, select **Enhance chat**.
  4. Enter the following details to create a new channel:

     * **Name** : GCP Messaging Channel
     * **Developer Name** : (automatically generated) `GCP_Messaging_Channel`
     * **Domain name** : The name of the site on which you installed the chat widget
     * **Routing Type** : Omni-queue
     * **Queue** : Agent Assist
  5. Click **Save**.




### Step 5: Publish embedded service deployment

The embedded service deployment you generated in the previous step is inactive. Follow these steps to activate it:

  1. Navigate to **Quick find** > **Embedded service**.
  2. Select **Embedded Service deployment** > **`GCP_Messaging_Channel`**.
  3. Click **Publish**.



## Create messaging session record page

If you're using enhanced chat, you can edit your existing [record page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup#record-pages) and [add an Agent Assist UI module](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-setup#add-aa-ui-module).

## Add omnichannel utility bar to service console

Follow the Salesforce instructions to [add the omni-channel utility bar to the service console app](https://help.salesforce.com/s/articleView?id=service.omnichannel_add_utility_to_console.htm&type=5). This utility bar provides the tools for agents to manage their presence and accept messages.

## Test enhanced chat

Follow these steps to test your messenger:

  1. Navigate to **Quick find** > **Embedded service deployments**.
  2. Click **`GCP_Messaging_Channel`** > **Test Enhanced Web Chat** , and a new window opens.
  3. Follow the instructions in the new window.
  4. Click the chat widget to start a sample conversation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
