---
url: https://docs.cloud.google.com/dialogflow/es/docs/entities-overview/
title: Entities \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:27.923119+00:00
---

# Entities  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/entities-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Entities Stay organized with collections  Save and categorize content based on your preferences. 

Each intent [parameter](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters#params) has a type, called the _entity type_ , which dictates exactly how data from an end-user expression is extracted. 

Dialogflow provides predefined [system entities](https://docs.cloud.google.com/dialogflow/docs/entities-system) that can match many common types of data. For example, there are system entities for matching dates, times, colors, email addresses, and so on. You can also create your own [custom entities](https://docs.cloud.google.com/dialogflow/docs/entities-custom) for matching custom data. For example, you could define a _vegetable_ entity that can match the types of vegetables available for purchase with a grocery store agent. 

## Entity terminology

The term _entity_ is used in this documentation and in the Dialogflow Console to describe the general concept of entities. When discussing entity details, it's important to understand more specific terms:

  * **Entity type** : Defines the type of information you want to extract from user input. For example, _vegetable_ could be the name of an entity type. Clicking **Create Entity** from the Dialogflow Console creates an _entity type_. When using the API, the term _entity type_ refers to the [`EntityType`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes) type.

  * **Entity entry** : For each entity type, there are many _entity entries_. Each entity entry provides a set of words or phrases that are considered equivalent. For example, if _vegetable_ is an entity type, you could define these three entity entries:

    * carrot
    * scallion, green onion
    * bell pepper, sweet pepper

When editing an entity type from the Dialogflow Console, each row of the display is an _entity entry_. When using the API, the term _entity entry_ refers to the `Entity` type (`EntityType.Entity` or `EntityType_Entity` for some client library languages).

  * **Entity reference value and synonyms** : Some entity entries have multiple words or phrases that are considered equivalent, like the _scallion_ example above. For these entity entries, you provide one _reference value_ and one or more _synonyms_.




[ Previous arrow_back  Intent settings  ](https://docs.cloud.google.com/dialogflow/es/docs/intents-settings)

[ Next Entity options  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-options)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
