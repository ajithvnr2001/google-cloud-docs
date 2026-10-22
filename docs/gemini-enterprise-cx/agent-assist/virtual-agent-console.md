---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/virtual-agent-console/
title: Implement virtual Agent Assist using the console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:34.396869+00:00
---

# Implement virtual Agent Assist using the console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/virtual-agent-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Implement virtual Agent Assist using the console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature has limited access. Contact your Google Cloud representative to access private GA features.

The **Virtual Agent Assist** feature follows a conversation and uses a [Dialogflow virtual agent](https://docs.cloud.google.com/dialogflow/docs/agents-overview) to provide workflow support to human agents and detect intents for data analysis.

While [virtual agents](https://docs.cloud.google.com/dialogflow/cx/docs) interact with customers on their own to attempt to resolve issues before escalating to a human agent, the virtual Agent Assist feature involves human-human interactions only. The assistant works in the background to detect intents, automatically extract and save relevant numbers and other information, automatically look up customer information, and more. It displays this information to the human agent to assist with their interaction with the customer and reduce the need for the human agent to type their own responses and seek out information on their own.

This guide walks you through the process of enabling **Virtual Agent Assist** and testing your results in the simulator using the [Agent Assist console](https://agentassist.cloud.google.com). If you prefer, you can also perform all of the following actions by calling the API directly.

**Note:** Be aware that all runtime operations must be carried out by calling the API directly.

## Before you begin

  1. If you are using the publicly-available conversation dataset, review the [documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format) that guides you through using these resources.
  2. If you are using your own data you must have completed one of the following (you can use any combination of datasets or smart reply models with Virtual Agent Assist): 
     * To implement FAQ assist or article suggestion you must create a [knowledge base](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/knowledge-base) with documents in it.
     * To implement smart reply you must [train a smart reply model and manage its allowlist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training).
  3. Create a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) that includes one or more knowledge bases or models. Leave the **Virtual Agent Assist** field unchecked for now, but set all other parameters that you'd like to test using the simulator.



## Create a virtual agent

  1. Navigate to either the [Dialogflow ES](https://dialogflow.cloud.google.com) or [Dialogflow CX](https://dialogflow.cloud.google.com/cx).

For simplicity, this tutorial outlines Agent Assist implementation using a Dialogflow CX agent. You can also access both consoles by navigating to the navigation menu icon at the top left of the [Agent Assist console](https://agentassist.cloud.google.com):

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aapriv1.png)

  2. Choose the same project that you intend to use with your Agent Assist data. If you have already created agents for use with this project, they will appear in a list. To create a new agent, click the **Create agent** button at the top right of the page. In the window that appears, enter a new agent name:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aapriv2.png)

  3. The new agent now appears in the list of virtual agents associated with that project. Click the three vertical dots to the right of the agent you'd like to use and click **Copy name** to copy the agent's name to your clipboard:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aapriv3.png)




## Associate your virtual agent with a conversation profile

  1. Navigate back to the Agent Assist console and select the same project that you used to create your virtual agent. Click **Conversation profiles** and select the conversation profile that you created as part of the before you begin steps and would like to use to implement virtual Agent Assist. Check the **Virtual Agent Assist** field and paste the agent's name into the empty **Dialogflow agent** field that appears:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv4.png)

  2. Make sure that you have selected the **Inline suggestions** option under **Retrieval method** and click **Save**.




## Test your Virtual Agent Assist results using the simulator

  1. On the **conversation profiles** page, click the three vertical dots to the right of your conversation profile and click **Use simulator** to test your Agent Assist performance.

**Note:** You have the option of testing either voice or text data. This tutorial demonstrates the feature using text data; contact your Google representative to use this feature with voice data.

The Simulator page appears:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv5.png)

The left column contains the chat transcript between the customer and agent, while the right column contains virtual Agent Assist suggestions. To select which features you'd like to test at any given time, check the box next to each feature to include in the simulation. For example, you might have created a conversation profile that configures smart reply, virtual Agent Assist and FAQ Assist. To test only smart reply and virtual Agent Assist, make sure only those two options are checked.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv6.png)

  2. The following example walks through a scenario in which a customer is planning international travel. It uses a conversation profile with both virtual Agent Assist and smart reply configured.

If the customer types _I'm traveling to Japan next Monday_ , a detected intent is identified. The intent is the virtual agent's best estimate of the customer's intention in each chat message. The agent clicks the intent and two input fields appear, **destination** and **arrival_date** :

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv7.png)

The fields are already automatically filled in using data from the customer's message. The agent checks that both are correct and clicks **Next** to bring up a suggested reply to the customer:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv8.png)

  3. The agent can click the blue arrow to the right of the text prompt to automatically copy it into the **Agent** reply box. After the message is sent additional follow-up questions appear in bubbles under the agent's reply box. Hovering the cursor over each bubble displays the replies confidence score.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv9.png)

  4. When the customer replies with their phone number, that information is automatically populated into the **Collect Customer Line** field in the virtual Agent Assist column. When the agent clicks **Next** , a new prompt _When do you plan to return?_ appears. The agent copies it to the chat, sends it to the customer, and the returned date is again automatically populated to the input field. The agent is next prompted to ask the customer whether they would like to purchase an international phone plan. When the customer responds _Yes_ , a **confirmation:yes** button appears under the prompt. The agent clicks this button to move on to the next Agent Assist suggestion.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/priv/images/aapriv10.png)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
