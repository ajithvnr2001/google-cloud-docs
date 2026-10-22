---
url: https://docs.cloud.google.com/dialogflow/es/docs/intents-matching/
title: Intent matching \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:27.180123+00:00
---

# Intent matching  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/intents-matching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Intent matching Stay organized with collections  Save and categorize content based on your preferences. 

When an end-user writes or says something, referred to as an _end-user expression_ , Dialogflow compares the expression to the [training phrases](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases) for each intent to find the best match. Matching an intent is also known as _intent classification_. This document describes the factors used to match an intent.

## Matching algorithms

Dialogflow uses two algorithms to match intents: _rule-based grammar matching_ and _ML matching_. Dialogflow simultaneously attempts both algorithms and chooses the best result.

**Note:** ML matching can be [disabled for an intent](https://docs.cloud.google.com/dialogflow/docs/intents-settings#disable-ml), but this is rarely a good option.

The following table lists the pros and cons of these algorithms:

Algorithm | Pros | Cons  
---|---|---  
Rule-based grammar matching | 

  * Accurate with a small or large number of [training phrase](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases) examples.
  * Models are updated quickly.

| 

  * Does not support the [automated expansion](https://docs.cloud.google.com/dialogflow/docs/entities-options#expansion) entity option.

  
ML matching | 

  * Accurate with a large number of [training phrase](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases) examples.
  * Matching is fast.

| 

  * Inaccurate with a small number of [training phrase](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases) examples.
  * Models are updated slowly.
  * Less accurate than grammar matching for agents with [training phrases](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases) in template mode.

  
  
## Intent detection confidence

When searching for a matching intent, Dialogflow scores potential matches with an _intent detection confidence_ , also known as the _confidence score_. These values range from 0.0 (completely uncertain) to 1.0 (completely certain). Without taking the other factors described in this document into account, once intents are scored, there are three possible outcomes:

  * If the highest scoring intent has a confidence score greater than or equal to the [ML Classification Threshold](https://docs.cloud.google.com/dialogflow/docs/agents-settings#ml) setting, it is returned as a match.
  * If no intents meet the threshold, a [fallback intent](https://docs.cloud.google.com/dialogflow/docs/intents-default#fallback) is matched.
  * If no intents meet the threshold and no fallback intent is defined, no intent is matched.



## Intent priority

You can set [priorities](https://docs.cloud.google.com/dialogflow/docs/intents-settings#priority) for intents. When two or more intents match the same end-user expression with similar confidence scores, priority is used to select the best match. Otherwise, the confidence score for intent matching is more important than priority.

## Knowledge connectors

[Knowledge connectors](https://docs.cloud.google.com/dialogflow/docs/knowledge-connectors) complement defined intents. They parse _knowledge documents_ (for example, FAQs) to find information related to end-user expressions.

If a defined intent and a knowledge document are both potential matches, the match confidence of each and the [knowledge results preference](https://docs.cloud.google.com/dialogflow/docs/knowledge-connectors#settings) are used to determine which match is the selected match.

## Context

While [contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-overview) are active, Dialogflow is more likely to match intents that are configured with [input contexts](https://docs.cloud.google.com/dialogflow/docs/contexts-input-output#input_contexts) that correspond to the currently active contexts.

## Fallback intents

[Fallback intents](https://docs.cloud.google.com/dialogflow/docs/intents-default#fallback) have the lowest priority for intent matching.

[ Previous arrow_back  Default intents  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-default)

[ Next Intent settings  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
