---
url: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/create-customize-agent/
title: Before you begin \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:49.718401+00:00
---

# Before you begin  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/create-customize-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Before you begin Stay organized with collections  Save and categorize content based on your preferences. 

Before trying this tutorial, you should be familiar with Dialogflow basics covered in [Quickstarts](https://docs.cloud.google.com/dialogflow/docs/quick).

## Create an agent

Use the [Dialogflow ES console](https://dialogflow.cloud.google.com) to create an agent named "PackageTracker". If you are unsure how to do this, revisit the [Quickstarts](https://docs.cloud.google.com/dialogflow/docs/quick).

If you prefer to work with an existing agent, that is okay too. Just be sure that you [enable auto speech adaptation](https://docs.cloud.google.com/dialogflow/es/docs/speech-adaptation#enable_or_disable_auto_speech_adaptation) in the agent settings. This is enabled by default for new agents.

# Create a sequence recognizer entity

The core function of this agent is understanding alphanumeric sequences over voice. Specifically, you'll set up the agent to listen for a handful of characters at a time, eventually putting all sub-sequences together before validating the final sequence against a data store. Let's start by defining an entity to recognize the partial sequences.

## Create the regexp sequence entities

We need to use a regexp entity to capture sequences so that auto speech adaptation will know to listen for "ABC" instead of "a bee sea".

These entities must conform to the [auto speech adaptation regexp enitity guidelines](https://docs.cloud.google.com/dialogflow/es/docs/speech-adaptation#regexp_entities) to ensure the speech recognition is tuned to recognize spelled-out sequences.

### Partial sequence entity

We'll set up the entity to accept any alphanumeric sequence of at least 3 characters. Later, you'll add a webhook so that you can validate the final sequence against a data store or API.

  1. Create a new entity. We'll name it "alphanumeric" because it will accept any alphanumeric input.
  2. Check the box for **Regexp entity**
  3. Add a single entry, `^[a-zA-Z0-9]{3}[a-zA-Z0-9]*$`
  4. Click **SAVE**.



![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/tutorials/sequences/alphanumeric.png)

Notice that the regexp you added is very strict in that it is looking only for a string of alphanumerics, without any spaces or dashes. This is important for two reasons:

  1. This regexp follows the auto speech adaptation [requirements](https://docs.cloud.google.com/dialogflow/es/docs/speech-adaptation#regexp_entities) for enabling the "spelled-out sequence" recognizer mode.
  2. By not looking for spaces and only looking for entire phrases (`^`...`$`), you allow end-users to easily exit the sequence recognition. For example, when you prompt "what's your order number" and an end-user replies "no I want to place an order", the regexp will reject and Dialogflow will know to look for another intent that might match that phrase.



If you are only interested in numeric values, you could create a more tailored entity like `[0-9]{3}[0-9]*`, or even just use the built-in `@sys.number-sequence` entity.

The rest of the tutorial assumes you are collecting alphanumeric sequences. Jump to the next section to see how to set up intents to collect these sequences.

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences)

[ Next Creating the sequence flow intents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/sequences/create-intent-with-parameters)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
