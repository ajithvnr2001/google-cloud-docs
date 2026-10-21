---
url: https://docs.cloud.google.com/dialogflow/es/docs/entities-options/
title: Entity options \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:37.658901+00:00
---

# Entity options  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/entities-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Entity options Stay organized with collections  Save and categorize content based on your preferences. 

There are several entity options that change the behavior of entity matching and data extraction. These options are pre-configured for [system entities](https://docs.cloud.google.com/dialogflow/docs/entities-system), so you can not change them for system entities. However, you can change them for your own [custom entities](https://docs.cloud.google.com/dialogflow/docs/entities-custom). You can create different kinds of entities, depending on the options selected:

  * Map entity
  * List entity
  * Composite entity (a special kind of list entity)
  * Regexp entity



There are also two options that do not determine the kind of entity, but do affect the behavior of entity matching:

  * Automated expansion
  * Fuzzy matching



This document describes each of these options.

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access entity options data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Entities** in the left sidebar menu.
  4. Select the **Custom** tab for [custom entities](https://docs.cloud.google.com/dialogflow/docs/entities-custom) defined for your agent or the **System** tab for [system entities](https://docs.cloud.google.com/dialogflow/docs/entities-system) used by your agent.
  5. See the following checkbox options for any existing entities: 
     * **Define synonyms**
     * **Regexp entity** (custom entity only)
     * **Allow automated expansion** (custom entity only)
     * **Fuzzy matching** (custom entity only)



If you are building an agent using the API instead of the console, see the [EntityTypes reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes). The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API.

## Map entity

_Map entities_ provide a map from reference values to synonyms for each reference value. Each map entity entry contains a single reference value and a list of synonyms. For example, each of the following rows are entity entries for a `size` entity type:

Reference value | Synonyms  
---|---  
S | S, small, tiny, little  
M | M, medium, average  
L | L, large, huge, big  
  
Notice that the reference value is included in the synonym list for each entity entry above. In order for a reference value to be matched, it needs to be included as a synonym itself. When you initially enter a reference value with the console, it is automatically added as a synonym.

If any of the synonyms are matched for an end-user expression part, the associated reference value is extracted for the match and is used to resolve the associated [parameter value](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#values).

It is okay for the reference value to be omitted from the synonym list. This just means that it is not matched to an end-user expression part, but it is used as the extracted value when one of its synonyms is matched. This is desirable when you use special strings for reference values that are not typed or spoken by end-users.

Many system entities are map entities. For example, the `@sys.date` system entity matches common date inputs like "January 1, 2015" or "The first of January of 2015". Both of those inputs are mapped to a reference value in ISO-8601 format: "2015-01-01T12:00:00-03:00".

To create a map entity:

  * Using the console, uncheck the **Regexp entity** option and check the **Define synonyms** option.
  * Using the API, set the [`EntityType`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes) `kind` field to `KIND_MAP`.



## List entity

_List entities_ provide a list of single value entity entries. They do not have reference values and synonyms. For example, each of the following rows are entity entries for a `material` entity type:

Value  
---  
fabric  
wood  
metal  
  
If any value is matched for an end-user expression part, the value is extracted for the match and is used to resolve the associated [parameter value](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#values).

Many system entities are list entities. For example, the `@sys.color` system entity matches common color inputs like "red" or "blue". When a color is matched, the extracted value does not map to any reference value. For example, shades of red, such as "scarlet" or "crimson", are not mapped to "red" and are extracted as their original values "scarlet" and "crimson".

To create a list entity:

  * Using the console, uncheck the **Regexp entity** option and uncheck the **Define synonyms** option.
  * Using the API, set the [`EntityType`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes) `kind` field to `KIND_LIST`.



## Composite entity

A _composite entity_ is a special kind of list entity. Entity entries for list entities typically contain simple words or phrases, but they may also contain other entity types. When an entity type is referenced in another entity type, the reference is called an _alias_. When a list entity contains aliases to other entity types, it is called a composite entity.

When creating an alias, you supply the name of the referenced entity type and a property name of your choosing. When a composite entity is matched at runtime, the extracted value is returned as a JSON object, with alias property names used as JSON property names. The format for entering an alias is:
    
    
    @entity-name:property-name

For example, you could create a `place` entity type that matches either a city or a state with the following entity entries:

Value  
---  
@sys.geo-city:city  
@sys.geo-state:state  
  
If an end-user expression contains a "Nashville" part, the `place` entity type is matched. The extracted value is returned as: `{"city": "Nashville"}`.

You can also use multiple entity aliases in an entity entry. Consider the following `move` custom entity type that contains aliases to a `direction` entity type and the `@sys.number` system entity type:

**Direction custom map entity type:**

Reference value | Synonyms  
---|---  
forward | forward, forwards  
back | back, backward, backwards  
  
**Move custom list entity type:**

Value  
---  
@sys.number:steps steps @direction:direction  
  
If the `move` entity is matched to an end-user expression that contains "five steps backward", the `move` entity will be matched. The extracted value is returned as: `{"steps": 5, "direction": "back"}`.

Many system entities are composite entities. For example, the `@sys.unit-currency` system entity is used for matching amounts of money with a currency name. It matches end-user expressions like "50 euros" or "twenty dollars and five cents". The extracted value is returned as a JSON object like: `{"amount": 50, "currency": "EUR"}`

## Regexp entity

With _regexp entities_ , you can provide regular expressions for matching. For more information, see [Regexp entities](https://docs.cloud.google.com/dialogflow/docs/entities-regexp).

To create a regexp entity:

  * Using the console, check the **Regexp entity** option.
  * Using the API, set the [`EntityType`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes) `kind` field to `KIND_REGEXP`.



## Automated expansion

You can enable automated expansion for a custom entity type. When enabled, your agent can recognize values that have not been explicitly provided. For example, consider a shopping list entity type:

Value  
---  
bread  
butter  
milk  
apple  
ice cream  
  
If an end-user expression is "I need to buy some carrots", "carrots" will be matched for this entity type, even though it's not provided. The agent recognizes that "carrots" is contextually similar to other values.

You should follow the best practices when considering automated expansion:

  * Enabling automated expansion doesn't guarantee entity extraction. For a finite list, you should provide the complete list instead of providing a partial list and enabling automated expansion.
  * If you enable automated expansion in more than one entity, it may cause conflicts and unexpected classification results.
  * To ensure better parameter extraction quality, it is crucial to provide diverse training data which cover all the use-cases in which a given entity can be found in the expected agent's traffic. With not enough examples, automated entities expansion might not work as expected.



To enable automated expansion:

  * Using the console, check the **Allow automated expansion** option.
  * Using the API, set the [`EntityType`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes) `autoExpansionMode` field to `AUTO_EXPANSION_MODE_DEFAULT`.



## Fuzzy matching

You can enable _fuzzy matching_ for a custom entity. With fuzzy matching enabled, the ordering of the words in a value or synonym does not matter. For more information, see [Fuzzy matching](https://docs.cloud.google.com/dialogflow/docs/entities-fuzzy).

To enable fuzzy matching:

  * Using the console, check the **Fuzzy matching** option.
  * Using the API, set the [`EntityType`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes) `enableFuzzyExtraction` field to `true`.



[ Previous arrow_back  Entities  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-overview)

[ Next System entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-system)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
