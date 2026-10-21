---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-options/
title: Entity options \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:38.267334+00:00
---

# Entity options  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-options/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Entity options Stay organized with collections  Save and categorize content based on your preferences. 

There are several entity options that change the behavior of entity matching and data extraction. These options are pre-configured for [system entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system), so you can not change them for system entities. However, you can change them for your own [custom entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom). You can create different kinds of entities, depending on the options selected:

  * Map entity
  * List entity
  * Composite entity (a special kind of list entity)
  * Regexp entity



There are other options that do not determine the kind of entity, but do affect the behavior of entity matching:

  * Automated expansion
  * Fuzzy matching
  * Redact in log
  * Entity exclusions



This document describes each of these options.

## Where to find this data

When building an agent, it is most common to use the [Dialogflow CX console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console). The following instructions focus on using the console. To access entity options data:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your Google Cloud project.
  3. Select your agent.
  4. Select the **Manage** tab.
  5. Click **Entity Types**.
  6. See the following options for any existing entities (some of these may only be visible after expanding **Advanced options**): 
     * **Entities only (no synonyms)**
     * **Regexp entities**
     * **Automatically add entities**
     * **Fuzzy matching**
     * **Redact in log**
     * **Entity exclusions**



If you are building an agent using the API instead of the console, see the `EntityType` type. The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API. Go to the EntityType API reference

**Select a protocol and version for the EntityType reference:**

Protocol | V3 | V3beta1  
---|---|---  
REST |  [EntityType resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes) |  [EntityType resource](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/projects.locations.agents.entityTypes)  
RPC |  [EntityType interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.EntityTypes) |  [EntityType interface](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#google.cloud.dialogflow.cx.v3beta1.EntityTypes)  
C++ |  [EntityTypesClient](https://googleapis.dev/cpp/google-cloud-dialogflow_cx/latest/classgoogle_1_1cloud_1_1dialogflow__cx_1_1EntityTypesClient.html) |  Not available   
C# |  [EntityTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.EntityTypesClient) |  Not available   
Go |  [EntityTypesClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dialogflow/latest/cx/apiv3#cloud_google_com_go_dialogflow_cx_apiv3_EntityTypesClient) |  Not available   
Java |  [EntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.EntityTypesClient) |  [EntityTypesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.EntityTypesClient)  
Node.js |  [EntityTypesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3.EntityTypesClient.html) |  [EntityTypesClient](https://googleapis.dev/nodejs/dialogflow-cx/latest/v3beta1.EntityTypesClient.html)  
PHP |  Not available  |  Not available   
Python |  [EntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.services.entity_types.EntityTypesClient) |  [EntityTypesClient](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.entity_types.EntityTypesClient)  
Ruby |  Not available  |  Not available   
  
Close

## Map entity

_Map entities_ provide a map from reference values to synonyms for each reference value. Each map entity entry contains a single reference value and a list of synonyms. Optionally, you can also [set a DTMF pattern for each entity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf).

For example, each of the following rows are entity entries for a `size` entity type:

Entity | Synonyms | DTMF Pattern  
---|---|---  
S | S, small, tiny, little |   
M | M, medium, average |   
L | L, large, huge, big |   
  
Notice that the reference value is included in the synonym list for each entity entry above. In order for a reference value to be matched, it needs to be included as a synonym itself. When you initially enter a reference value with the console, it is automatically added as a synonym.

If any of the synonyms are matched for an end-user input part, the associated reference value is extracted for the match and is used to resolve the associated [parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) value.

It is okay for the reference value to be omitted from the synonym list. This just means that it is not matched to an end-user input part, but it is used as the extracted value when one of its synonyms is matched. This is desirable when you use special strings for reference values that are not typed or spoken by end-users.

Many system entities are map entities. For example, the `@sys.date` system entity matches common date inputs like "January 1, 2015" or "The first of January of 2015". Both of those inputs are mapped to a reference value in ISO-8601 format: "2015-01-01T12:00:00-03:00".

To create a map entity:

  * Using the console, uncheck the **Regexp entities** option and uncheck the **Entities only** option.
  * Using the API, set the `EntityType.kind` field to `KIND_MAP`.



### Use AI generation to auto-generate synonyms

Instead of entering synonyms manually, you can use an AI generator to auto-generate synonyms for your reference value. To do this, check the **Auto-generate X syonyms per entity** checkbox when you create a new reference value. The default value is 3 synonyms. Generating more than 15 synonyms at a time can lead to errors. As a best practice, be sure to fill in the entity type's **Description** field to generate more accurate synonyms for your reference value.

For information about using this feature to auto-generate and auto-translate data for non-default languages, see the [multilingual agents documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#ai_generate_language-specific_data)

## List entity

_List entities_ provide a list of single value entity entries. They do not have reference values and synonyms. For example, each of the following rows are entity entries for a `material` entity type:

Value  
---  
fabric  
wood  
metal  
  
If any value is matched for an end-user input part, the value is extracted for the match and is used to resolve the associated [parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) value.

Many system entities are list entities. For example, the `@sys.color` system entity matches common color inputs like "red" or "blue". When a color is matched, the extracted value does not map to any reference value. For example, shades of red, such as "scarlet" or "crimson", are not mapped to "red" and are extracted as their original values "scarlet" and "crimson".

To create a list entity:

  * Using the console, uncheck the **Regexp entities** option and check the **Entities only** option.
  * Using the API, set the `EntityType.kind` field to `KIND_LIST`.



## Composite entity

A _composite entity_ is a special kind of list entity. Entity entries for list entities typically contain simple words or phrases, but they may also contain other entity types. When an entity type is referenced in another entity type, the reference is called an _alias_. When a list entity contains aliases to other entity types, it is called a composite entity.

When creating an alias, you supply the name of the referenced entity type and a property name of your choosing. When a composite entity is matched at runtime, the extracted value is returned as a JSON object, with alias property names used as JSON property names. The format for entering an alias is:
    
    
    @entity-name:property-name

For example, you could create a `place` entity type that matches either a city or a state with the following entity entries:

Value  
---  
@sys.geo-city:city  
@sys.geo-state:state  
  
If an end-user input contains a "Nashville" part, the `place` entity type is matched. The extracted value is returned as: `{"city": "Nashville"}`.

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
  
If the `move` entity is matched to an end-user input that contains "five steps backward", the `move` entity will be matched. The extracted value is returned as: `{"steps": 5, "direction": "back"}`.

Many system entities are composite entities. For example, the `@sys.unit-currency` system entity is used for matching amounts of money with a currency name. It matches end-user inputs like "50 euros" or "twenty dollars and five cents". The extracted value is returned as a JSON object like: `{"amount": 50, "currency": "EUR"}`

## Regexp entity

With _regexp entities_ , you can provide regular expressions for matching. For more information, see [Regexp entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-regexp).

To create a regexp entity:

  * Using the console, check the **Regexp entities** option.
  * Using the API, set the `EntityType.kind` field to `KIND_REGEXP`.



## Automated expansion (automatically add entities)

You can enable automated expansion for a custom entity type. When enabled, your agent can recognize values that have not been explicitly provided. For example, consider a shopping list entity type:

Value  
---  
bread  
butter  
milk  
apple  
ice cream  
  
If an end-user input is "I need to buy some carrots", "carrots" will be matched for this entity type, even though it's not provided. The agent recognizes that "carrots" is contextually similar to other values.

You should follow the best practices when considering automated expansion:

  * Enabling automated expansion doesn't guarantee entity extraction. For a finite list, you should provide the complete list instead of providing a partial list and enabling automated expansion.
  * If you enable automated expansion in more than one entity, it may cause conflicts and unexpected classification results.
  * To ensure better parameter extraction quality, it is crucial to provide diverse training data which cover all the use-cases in which a given entity can be found in the expected agent's traffic. With not enough examples, automated entities expansion might not work as expected.



To enable automated expansion:

  * Using the console, check the **Automatically add entities** option.
  * Using the API, set the `EntityType.autoExpansionMode` field to `AUTO_EXPANSION_MODE_DEFAULT`.



## Fuzzy matching

You can enable _fuzzy matching_ for a custom entity. With fuzzy matching enabled, the ordering of the words in a value or synonym does not matter. For more information, see [Fuzzy matching](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-fuzzy).

To enable fuzzy matching:

  * Using the console, check the **Fuzzy matching** option.
  * Using the API, set the `EntityType.enableFuzzyExtraction` field to `true`.



## Redact in log

If you enable entity redaction, all runtime extracted parameter values for the entity type will be redacted when logging.

As an alternative, you can [redact individual parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#redact).

## Entity exclusions

You can add entity exclusions, which are phrases that shouldn't be matched. For example, if you have a size entity type with entity _giant_ (an adjective), you might consider adding _giants_ (a noun) as an exclusion.

[ Previous arrow_back  Entities  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity)

[ Next System entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
