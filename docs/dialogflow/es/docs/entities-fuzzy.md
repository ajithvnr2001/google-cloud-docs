---
url: https://docs.cloud.google.com/dialogflow/es/docs/entities-fuzzy/
title: Fuzzy matching \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:15.128481+00:00
---

# Fuzzy matching  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/entities-fuzzy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Fuzzy matching Stay organized with collections  Save and categorize content based on your preferences. 

By default, entity matching requires an exact match for one of the entity entries. This works well for single-word entity entry values and synonyms but may present a problem for multi-word values and synonyms. For example, consider a _ball_ entity that should be matched for the following end-user expression parts:

  * "ball"
  * "red ball"
  * "ball red"
  * "small ball"
  * "ball small"
  * "small red ball"
  * "small ball red"
  * "red small ball"
  * "red ball small"
  * "ball small red"
  * "ball red small"



For a match to occur, you normally need to define an entity entry value and synonyms for each of these permutations. However, with fuzzy matching enabled, the ordering of the words in a value or synonym does not matter. The following will trigger a match for all of the examples above:

  * "ball"
  * "red ball"
  * "small ball"
  * "small red ball"



## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access entity data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Entities** in the left sidebar menu.



If you are building an agent using the API instead of the console, see the [EntityTypes reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes). The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API.

## Create a fuzzy matching entity

To create a fuzzy matching entity:

  1. Open an existing entity or create a new one.
  2. Check **Fuzzy matching**.
  3. Enter one or more entries in the table.
  4. Click **Save**.



If you are using the API to create or update entities, set the `enable_fuzzy_extraction` field to true for the `EntityType`.

## Limitations

The following limitations apply:

  * Fuzzy matching cannot be enabled for [regexp entities](https://docs.cloud.google.com/dialogflow/docs/entities-regexp). These features are mutually exclusive.
  * Fuzzy matching should not be enabled for entities which are used to match strict values like IDs, national identification numbers, and so on.



## Partial matches

When you define synonyms that contain multiple words, Dialogflow will attempt to match end-user input to the closest matching synonym, which may include partial matches. For example, if you define a synonym as "cold brew coffee", and the end-user input is "cold coffee", the associated entity will be matched unless there is a better match.

## Spell correction

When end-user input could be considered a misspelling of an entity synonym, the associated entity may be matched. For example, if you define a synonym as "lumber", and the end-user input is "number", the associated entity may be matched.

[ Previous arrow_back  Regexp entities  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-regexp)

[ Next Export and import entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-export)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
