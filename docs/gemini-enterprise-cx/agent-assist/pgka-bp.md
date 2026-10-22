---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka-bp/
title: Best practices: (Proactive) generative knowledge assist \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:54.272668+00:00
---

# Best practices: (Proactive) generative knowledge assist  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka-bp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Best practices: (Proactive) generative knowledge assist Stay organized with collections  Save and categorize content based on your preferences. 

Generative knowledge assist synthesizes information you provide with an ongoing conversation and available customer metadata to give relevant and timely answers to your agent's questions. Proactive generative knowledge assist follows an ongoing conversation between your agent and a customer to proactively provide search query suggestions and answers.

Follow the recommendations in this document so that generative knowledge assist and proactive generative knowledge assist provide enhanced, accurate, and useful information for your business needs.

## Golden set

A golden set is a small portion of your data used as examples to evaluate the performance of an Agent Assist feature. For (proactive) generative knowledge assist, your golden set consists of more than one example that includes a portion of a conversation, an agent or suggested question, and the suggested response. 

Construct a golden set comprising about 20-30 examples which represent your business needs.

### Evaluation

Sometimes the golden set response is different, but the suggested response might be relevant. To increase the number of correctly recommended articles, include between two and five relevant articles to your golden set examples. In other words, increase the number of sources cited and evaluated to more than one.

## Datastore models

To enhance summary and knowledge assist performance, upgrade your Datastore agent to use the latest Gemini model.

Follow these steps to upgrade your Datastore model.

  1. Open Dialogflow.

[Dialogflow](https://dialogflow.cloud.google.com/cx/projects)

  2. Go to and click the **Datastore model selection** > **Select the latest Gemini Model**.

  3. Choose the latest version of the Gemini model.




### Summary customization

Use Gemini models to customize the suggested summary behavior based on your business requirements. For information on the list of supported Gemini models, see [Select summarization model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#summarization-model-selection).

In addition, you can use custom summarization prompts to specify the behavior you want.

Follow these steps to enable custom summarization prompts.

  1. Open Dialogflow.

[Dialogflow](https://dialogflow.cloud.google.com/cx/projects)

  2. Go to **Summarization prompt**.

  3. Click **Create a custom prompt**.




### Datastore confidence score

If you choose the medium confidence level for Datastore in a Dialogflow agent, you get a higher number of suggestions that might be relevant. This can be helpful until you can enrich article metadata.

Follow these steps to enable medium confidence level.

  1. Open Dialogflow.

[Dialogflow](https://dialogflow.cloud.google.com/cx/projects)

  2. Go to **Grounding**.

  3. Select **Enable Grounding**.

  4. Select the option **Medium: We have medium confidence that the response is grounded.**




### Document enrichment

Custom summarization prompts and medium confidence levels produce the response summary and filter both generative knowledge assist and proactive generative knowledge assist. However, they don't impact source retrieval from generative knowledge assist. You can solve this by adding metadata and annexures in documents to enhance discoverability.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
