---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/hybrid/
title: Data store hybrid agents \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:15.620214+00:00
---

# Data store hybrid agents  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/hybrid/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Data store hybrid agents Stay organized with collections  Save and categorize content based on your preferences. 

If you have an existing Dialogflow CX agent, you can upgrade this agent to a _hybrid agent_ , which combines the power of precise conversation controls (such as flows, parameters, intents, conditions, and transitions) with data store handler generative features.

When you upgrade, you can delete or disable intent routes for certain conversation scenarios because data store handlers manage them more easily.

## Recommended scenarios

The following scenarios are recommended for data store handlers:

  * Questions that can be answered by your organization's documents or website.
  * FAQs that don't require database lookups.



The following scenarios are not recommended for data store handlers:

  * Content that doesn't have answers to chosen questions.
  * Questions that require database lookups or server requests.
  * Scenarios that require data redaction.
  * Scenarios that require deterministic agent responses.



## Input evaluation order

Dialogflow CX evaluates end-user input for hybrid agents in the following order:

  1. Parameter input while form filling.
  2. Intent matches for [routes in scope](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route).
  3. Data store handler with FAQ data store content.
  4. Data store handler with unstructured data store content.



[ Previous arrow_back  Data store performance improvements  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/performance)

[ Next Data store search configuration  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/search-configure)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
