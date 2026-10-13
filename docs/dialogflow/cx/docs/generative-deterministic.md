---
url: https://docs.cloud.google.com/dialogflow/cx/docs/generative-deterministic/
title: Generative versus deterministic \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:31.792158+00:00
---

# Generative versus deterministic  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/generative-deterministic/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Generative versus deterministic Stay organized with collections  Save and categorize content based on your preferences. 

During a conversation, Dialogflow CX agents always use language models for understanding end-user intention, but you can decide whether and how language models are used for agent responses. You can choose from fully generative, partly generative, and deterministic features when designing your agent.

This guide provides an overview of these features and helps you decide which features to use.

## Fully generative

The fully generative features are built on [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) large language models (LLMs) for understanding end-user intention and generating agent responses. These features provide natural conversations.

The following is an overview of the fully generative features:

  * **[Playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook)** provide a way to create virtual agents using LLMs. Provide natural language instructions and structured data. This reduces virtual agent creation and maintenance time, and lets you create new types of conversational experiences for your business.
  * **[Data stores](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store)** parse and comprehend your public or private content, such as websites or internal documents. Once this information is indexed, your agent can answer questions and have conversations about the content.



## Deterministic flows

If you require more deterministic control over the conversation and all agent responses, you can design your agent with flows:

  * **[Flows](https://docs.cloud.google.com/dialogflow/cx/docs/basics)** use language models to understand end-user intention, which can be non-deterministic. However, once intention is established, you have complete control over the conversation flow and agent responses. Designing an agent with deterministic flows takes more design time, but it is a good option for agents that require explicit control over agent responses.



## Partly generative flows

Flows include optional generative features that you can use when you don't need deterministic control over agent responses in certain scenarios.

These features are as follows:

  * **[Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators)** generate agent responses. Instead of providing the agent response explicitly, you provide an LLM prompt that can handle many scenarios, including conversation summarization, question answering, customer information retrieval, and escalation to a human.
  * **[Generative fallback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generative-fallback)** generates agent responses when end-user input does not match an expected intention. You can enable generative fallback in certain scenarios by providing an LLM prompt to generate the response.



[ Next Setup and cleanup  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
