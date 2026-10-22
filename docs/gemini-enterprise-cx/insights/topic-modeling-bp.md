---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-bp/
title: Topic modeling best practices \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:51.218810+00:00
---

# Topic modeling best practices  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-bp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Topic modeling best practices Stay organized with collections  Save and categorize content based on your preferences. 

Follow these best practice guidelines to get the most out of your topic models.

## Fine-tune a topic model

The best way to improve topic assignments is to fine-tune your model. Follow these guidelines to optimize your topic model when adding, editing, and removing topics.

### Add or edit a topic

Avoid adding duplicate or similar topics because they will negatively impact the quality of topic inferences. When creating or changing a topic, apply the following naming and description guidelines.

#### Name

  * Use short, descriptive topics of three to six words, such as _troubleshooting remote control_ or _inquiring about billing policy_.

  * Avoid generic or abstract names, such as _Sales_.




Optionally, follow these best practices:

  * Use readily available custom topic names, such as _Billing_.

  * Add a short description to the topic name, as in "Billing Errors and Refunds".

  * Choose a suitable model configuration based on the results you want.




##### Example

A credit card support center runs topic modeling on their archived support call logs. The modeling creates a topic from a cluster of conversations and names it _Credit card over the limit inquiries_. The business shortens the name to _Credit limit inquiries_.

#### Description

  * Use a general description followed by a few examples.

  * Avoid including personal information like names, dates, or locations.

  * Too much detail, such as "don't include X topic", can negatively impact topic inference.




##### Examples

  * The customer is inquiring about their landline phone service. They may want to cancel it or consult about the current billing.

  * The customer is inquiring about their bill. They may want to know the amount or the due date.




### Remove secondary topics

After you've deployed your topic model and completed an analysis, check the topic distribution in the **Topic Model Deployed data** page. Secondary topics might be the dominant topic in deployed results because they can be common and have stronger matches. Topics that match to a high proportion (more than 30%) of your sample conversations are likely secondary topics. Carefully examine these topics and delete them if they aren't relevant.

Whether or not irrelevant secondary topics exist highly depends on the input data. If all the major topics on the **Deployed data** page have a relatively even distribution, and each topic only matches to a small proportion (less than 20%) of conversations, then there are probably no secondary topics to delete.

## Training data

For voice data, the quality of Speech-to-Text outputs is critical to the performance of the topic model. Follow these guidelines to improve the quality of your training data.

### Conversations

  * Avoid using duplicate conversations in the dataset.

  * Each conversation should contain at least 10 total turns, with 5 from the agent and 5 from the customer.

  * Use redacted conversations, but check the [Cloud Data Loss Prevention](https://cloud.google.com/security/products/dlp) redaction quality. Sometimes redaction removes important information from the transcripts, which can affect the length of your training conversations.

  * Make sure almost all the conversations are in the same language.




### Speaker roles

Make sure that the conversation's speaker [roles](https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-data-format#json-entry) are assigned properly after the conversation is ingested.

  * Accurately label conversation turns as coming from a customer or an agent. Conversations with only one role won't be used in training.

  * Use `AGENT` for human roles and `AUTOMATED_AGENT` for virtual ones.

  * Use `END_USER` or `CUSTOMER` for customer roles.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
