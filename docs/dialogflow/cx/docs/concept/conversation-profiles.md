---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-profiles/
title: Conversation profiles \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:54.940931+00:00
---

# Conversation profiles  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-profiles/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Conversation profiles Stay organized with collections  Save and categorize content based on your preferences. 

Conversation profiles provide some important characteristics about conversations between end-users and agents. They can be created in conjunction with either [Dialogflow CX Phone Gateway integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway) or [Agent Assist](https://docs.cloud.google.com/agent-assist/docs/conversation-profile). The Dialogflow CX Phone Gateway conversation profiles are relevant if you want to use [Call companion](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion). Agent Assist conversation profiles can be linked to either Dialogflow CX or Dialogflow ES agents in the [Agent Assist console](https://agentassist.cloud.google.com/). You can also link conversation profiles to Dialogflow CX agents in Conversational Agents console, as described in the agent linking section.

To see a list of conversation profiles that have already been created for a specific project and region and to create new ones, open an agent associated with the project and region, and click **Conversation profiles** in the left navigation. For example, to see all conversation profiles created in a project for the `global` region, open an agent associated with the `global` region in that project and click **Conversation profiles**.

## Create a conversation profile

The following fields are required to create a new conversation profile:

  * **Display name** : Display name for the conversation profile.
  * **Language** : Language for the conversation profile.
  * **Enable Call companion** : Enable this to use call companion for Dialogflow CX Phone Gateway. You can create the conversation profile without enabling this field, but the conversation profile will only be available for use with Agent Assist, not the Dialogflow CX agent.



## Agent linking

To link a conversation profile to an agent:

  1. Select the conversation profile.
  2. Click **Link with agent**.
  3. Select the agent.
  4. Click **Select**.
  5. Click **Save**.



To change the linked agent:

  1. Click **Linked with ...**.
  2. Click **Switch agent**.
  3. Select the agent.
  4. Click **Select**.
  5. Click **Save**.



To unlink an agent from a conversation profile:

  1. Click **Linked with ...**.
  2. Click **Unlink from this agent**.
  3. Click **Save**.



[ Previous arrow_back  Continuous tests and deployment  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/continuous-tests)

[ Next Training  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/training)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
