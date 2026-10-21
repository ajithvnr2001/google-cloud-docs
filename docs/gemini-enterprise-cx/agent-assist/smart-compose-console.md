---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-console/
title: Create a smart compose model using the console \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:31.525420+00:00
---

# Create a smart compose model using the console  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Create a smart compose model using the console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature is no longer supported. For an alternative, use [smart reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-reply).

This tutorial guides you through training and deploying a **Smart Compose** model using the Agent Assist console. If you prefer, you can also perform all of the following actions by calling the API directly. You can use the console to train a model and test its performance. All runtime operations must be carried out by calling the API directly. See the [smart compose how-to guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/how-to) for instructions.

## Before you begin

  1. If you are using the publicly-available conversation dataset, review the [documentation](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format) that guides you through using these resources.
  2. If you are using your own data, make sure that you have created one or more [conversation datasets](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-dataset). At least one conversation dataset is required for model training.



## Create and train a smart compose model

The process of creating a smart compose model using the [Agent Assist console](https://agentassist.cloud.google.com) is the same as creating a Smart reply model. Navigate to the [smart reply model training tutorial](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training) and follow the instructions for [creating & training](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training#create_train_a_new_model) a new model, then [deploying](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training) it. Instead of selecting **Smart Reply** when you choose your model type, select **Smart Compose**.

## Smart compose model allowlist management

Smart compose model allowlist management is broadly similar to [smart reply allowlist management](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/model-training#model_allowlist_management), but with a few different capabilities. The following features are unique to Smart Compose and operate in addition to smart reply allowlist functionality.

### Message grouping

As with smart reply allowlists, smart compose allowlists are grouped according to similar messages. You can click **Show [X] similar messages** next to a message to see the other messages in the group. Smart compose allowlists display an additional icon next to some messages:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aapriv18.png)

Clicking this icon brings up a group of substrings of that parent message that are also included in the allowlist. The following example shows the substrings for the parent message _goodbye for now._. In addition to the parent message, there is one substring, _bye for now._ :

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/aapriv19.png)

### Message searching, editing, and creation

If you search for a word or string of words in a smart compose allowlist, results are returned as a list of parent messages containing that string (if the string has any parent messages). Continuing the previous example, if you search for the string _bye for now._ , the result returned will be _goodbye for now._. You can view the string _bye for now._ by clicking the substring icon.

Message editing is disabled for smart compose, so you cannot edit any of the messages. Like smart reply, however, you can create new messages and add them to a smart compose allowlist if necessary.

## What's next

[Create a conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile) for your smart compose model and test its performance using the [Agent Assist simulator](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/smart-compose-simulator).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
