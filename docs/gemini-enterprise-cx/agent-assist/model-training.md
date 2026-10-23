---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training/
title: Train a Smart Reply model & manage allowlists \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:02.275183+00:00
---

# Train a Smart Reply model & manage allowlists  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Train a Smart Reply model & manage allowlists Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial guides you through training and deploying a model using the Agent Assist Console. You can use the console to train a model and test its performance, but be aware that all runtime operations must be carried out by calling the API directly. See the Agent Assist [how-to guides](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/how-to) for instructions.

## Create & train a new model

Navigate to the [Agent Assist Console](https://agentassist.cloud.google.com). Select the Smart Reply card in the center of the screen and click **Get started**. The Console tutorial walks you through the process of creating a dataset, training & deploying a Smart Reply model, and creating a conversation profile. You can do this using either a model that you create (trained your own data or the public conversation dataset), or test the Smart Reply feature using a demo model. After you have deployed your model, return to this guide for details about [allowlist management](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training#model_allowlist_management).

## Model allowlist management

When a Smart Reply model is created using the Agent Assist console, the creation process also generates a list of potential suggestions that can be surfaced to agents during a conversation. This resource is called the **allowlist**. The allowlist contains all possible suggestions that were generated using your selected conversation dataset.

To access a model's allowlist, navigate to the **Models** menu, then click on the model's name. You will be brought to the model's **Details** page. There are tabs for each of the three sections in the allowlist: **Unreviewed** , **Allowed** , and **Blocked**. Each message in the allowlist can belong to one of these three lists. Blocked suggestions cannot be suggested to agents at runtime. Only suggestions that appear on the **Allowed** and **Unreviewed** lists are surfaced during a conversation. By default, all suggestions on the allowlist are set to **Unreviewed** when a model is created.

### Message grouping

An allowlist might have 50,000+ messages. To make them easier to manage, Agent Assist automatically groups messages with similar meaning. You can see a message's similar messages by clicking on the **Show (X) similar messages** link to the right of the message:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa8.png)

### Message search, edits, and creation

You can search all messages in an allowlist using the **search entries** bar at the top of the page. You can also edit individual messages by hovering over a message and clicking the pencil icon that appears. A window containing the message's text appears:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa8_1.png)

We recommend that you edit only for spelling and grammar, and do not change the meaning of the message. The more the edited text deviates from the meaning in the model, the less likely that message is to be surfaced.

You also have the ability to create a new message by clicking the **+Add a message** button at the top right of the page. Similarly to edited messages, created messages are less likely to be surfaced during runtime.

### Allow or block messages

When you select one or more messages in the **Unreviewed messages** list, **MOVE TO ALLOWED** and **MOVE TO BLOCKED** buttons will appear at the top right of the page. You can also move individual messages to the allowed or blocked lists by clicking on the three vertical dots to the far right of the model's name:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aa7.png)

## What's next

Use your deployed model to create a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
