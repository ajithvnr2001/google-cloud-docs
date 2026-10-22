---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-basics/
title: Topic modeling basics \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:51.571103+00:00
---

# Topic modeling basics  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-basics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Topic modeling basics Stay organized with collections  Save and categorize content based on your preferences. 

Topic modeling determines the primary and secondary call drivers in contact center conversations. These call drivers are called topics.

## Conversations

A conversation is an interaction between a contact center agent and an end user. Topic modeling analyzes conversations in the form of chat or voice call transcripts created using the Contact Center AI Insights API.

For more information, see the [`Conversations`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations) reference documentation.

## Topics

A topic describes the main subject discussed in a group of conversations, also called a primary call driver. Topic modeling creates topics by analyzing the key subjects from each of your conversations and creating clusters of similar subjects. Topic modeling then identifies the number of distinct clusters and attempts to generate a name for each one. Names represent a topic which in turn is represented by an [Issue resource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels.issues).

When topic modeling creates a set of topic names, you can review the names and the conversations it has labeled with that name. Topic modeling can also show you the snippet from the most representative conversation for a topic.

### Secondary topics

Topic modeling can also identify secondary topics, which might be less interesting from an analysis perspective. Secondary topics are frequently related to regular process steps that happen in a conversation, such as authentication, confirmation, and collecting feedback.

Secondary topics can sometimes crowd out the more interesting primary topics, which makes it harder to spot the primary ones.

## Topic models

The first step to identifying the topics in conversations is to create a topic model in Customer Experience Insights. A topic model contains a list of topics based on a group of conversations. From a topic model, you can generate a report identifying the topics within the model as well as the names and descriptions of each topic.

Topic models are represented by [`issueModels`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.issueModels) resources.

You can perform the following operations on topic models:

  * Deploy
  * Fine-tune
  * Undeploy
  * Delete



## Fine-tune a topic model

After you create a topic model, you can review and modify the list of topics to fine-tune your model. There are three main techniques for fine-tuning a topic model to improve future topic assignments:

  * Add a new topic.
  * Edit an existing topic's name and description.
  * Remove an existing topic.



All these actions affect adjusted topic distributions.

When you perform any of these fine-tuning actions, a new analysis follows the updated topic list, which means the existing analysis is unchanged. To apply a new change to an existing analysis, follow the instructions in [Topic modeling instructions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling#reanalyze_a_conversation).

## Topic inference

You can deploy a topic model to your project, which lets you infer topics in real-time during a new conversation. Topic modeling uses LLM-based topic inference, which provides a prioritized list of topics. It also scores each topic by relevance.

This score only represents topic order for one model. You can't compare topic scores across multiple models. For example, when you analyze a conversation with multiple topic models, the highest score from each model is equally the primary topic for that conversation.

After you deploy your topic model, you can analyze each new conversation or set of conversations in bulk. The analysis determines which topic from your list applies to each conversation.

**Note:** Customer Experience Insights supports topic inference in [38 Gemini languages](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models#languages-gemini).

## What's next

  * [Topic modeling instructions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling)
  * [Topic modeling best practices](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-bp)
  * [Export and import a topic model](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-export-import)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
