---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-console/
title: Train a Summarization custom model for chat \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:41.850033+00:00
---

# Train a Summarization custom model for chat  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Train a Summarization custom model for chat Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature is no longer supported. For an alternative, use [summarization with custom sections](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections).

The **Agent Assist Summarization** feature lets you provide conversation summaries to your agents after each conversation is completed. The summaries help agents create their conversation notes and understand end-user communication history. For example, a summary output about a conversation might look similar to the following:

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/summarization.png)

This tutorial guides you through training and deploying a Summarization model using the Agent Assist console. You can use it to train a model and test its performance, but be aware that all runtime operations must be carried out by calling the API directly. See the Agent Assist [Summarization how-to guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections) for instructions.

If preferred, you can also create and deploy a Summarization model by [calling the API directly](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections)

## Before you begin

  1. If you are using your own data, make sure that you have [formatted it correctly](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format#summarization_data_format) and uploaded it to a Cloud Storage bucket.



## Create & train a new model

Navigate to the [Agent Assist console](https://agentassist.cloud.google.com). Select the Summarization card in the center of the screen and click **Get started**. You can create your own custom model using one or more datasets.

## What's next

After you have deployed your model, you can then proceed to [create a conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
