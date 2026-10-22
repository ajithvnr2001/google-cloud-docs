---
url: https://docs.cloud.google.com/dialogflow/es/docs/entities-regexp/
title: Regexp entities \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:11.736900+00:00
---

# Regexp entities  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/entities-regexp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Regexp entities Stay organized with collections  Save and categorize content based on your preferences. 

Some entities need to match patterns rather than specific terms. For example, national identification numbers, IDs, license plates, and so on. With _regexp entities_ , you can provide [regular expressions](https://github.com/google/re2/wiki/Syntax) for matching.

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access entity data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Entities** in the left sidebar menu.



If you are building an agent using the API instead of the console, see the [EntityTypes reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes). The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API.

## Compound regular expressions

Each regexp entity corresponds to a single pattern, but you can provide multiple regular expressions if they all represent variations of a single pattern. During agent training, all regular expressions of a single entity are combined with the alternation operator (`|`) to form one _compound regular expression_.

For example, if you provide the following regular expressions for a phone number:

  * `^[2-9]\d{2}-\d{3}-\d{4}$`
  * `^(1?(-?\d{3})-?)?(\d{3})(-?\d{4})$`



The compound regular expression becomes:

  * `^[2-9]\d{2}-\d{3}-\d{4}$|^(1?(-?\d{3})-?)?(\d{3})(-?\d{4})$`



The ordering of regular expressions matters. Each of the regular expressions in the compound regular expression are processed in order. Searching stops once a valid match is found. For example, for an end user expression of "Seattle":

  * `Sea|Seattle` matches "Sea"
  * `Seattle|Sea` matches "Seattle"



## Special handling for speech recognition

**Note:** Enabling [auto speech adaptation](https://docs.cloud.google.com/dialogflow/es/docs/speech-adaptation) is recommended when using regexp entities. Also see the speech adaptation [regexp-specific guidelines](https://docs.cloud.google.com/dialogflow/es/docs/speech-adaptation#regexp-entities).

If your agent uses speech recognition (also known as audio input, speech-to-text, or STT), your regular expressions will need special handling when matching letters and numbers. A spoken end-user utterance is first processed by the speech recognizer before entities are matched. When an utterance contains a series of letters or numbers, the recognizer may pad each character with spaces. In addition, the recognizer may interpret digits in word form. For example, an end-user utterance of "My ID is 123" may be recognized as any of the following:

  * "My ID is 123"
  * "My ID is 1 2 3"
  * "My ID is one two three"



To accommodate three digit numbers, you could use the following regular expressions:
    
    
    \d{3}
    
    
    \d \d \d
    
    
    (zero|one|two|three|four|five|six|seven|eight|nine) (zero|one|two|three|four|five|six|seven|eight|nine) (zero|one|two|three|four|five|six|seven|eight|nine)

## Create a regexp entity

To create a regexp entity:

  1. Open an existing entity or create a new one.
  2. Check **Regexp entity**.
  3. Enter one or more regular expressions in the entries table.
  4. Click **Save**.



![Screenshot of regexp entity](https://docs.cloud.google.com/static/dialogflow/es/docs/images/entities-regexp.png)

If you are using the API to create or update entities, use `KIND_REGEXP` for the entity kind field.

## Limitations

The following limitations apply:

  * [Fuzzy matching](https://docs.cloud.google.com/dialogflow/docs/entities-fuzzy) cannot be enabled for regexp entities. These features are mutually exclusive.
  * Each agent can have a maximum of 50 regexp entities.
  * The compound regular expression for an entity has a maximum length of 2000 characters.



[ Previous arrow_back  Session entities  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-session)

[ Next Fuzzy matching  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-fuzzy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
