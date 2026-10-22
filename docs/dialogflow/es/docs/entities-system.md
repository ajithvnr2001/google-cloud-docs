---
url: https://docs.cloud.google.com/dialogflow/es/docs/entities-system/
title: System entities \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:38.369072+00:00
---

# System entities  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/entities-system/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  System entities Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow provides many _system entities_ to extract common types from end-user expressions. For example, the `@sys.color` type can be used to extract values like "red" or "blue". You can see the full list of system entities in the [System entity reference](https://docs.cloud.google.com/dialogflow/docs/reference/system-entities).

For most applications, the values provided by system entities work well. However, your application may need to add additional values for system entities. For example, you may want to add "blue-green" to the list of values for `@sys.color`. Some system entities can be extended for this purpose. The [System entity reference](https://docs.cloud.google.com/dialogflow/docs/reference/system-entities) lists the system entities that can be extended. The remaining sections of this document describe how to extend system entities.

System entity support differs for each language. See the [system entity limitations](https://docs.cloud.google.com/dialogflow/es/docs/reference/system-entities#limits) for details.

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access system entity data for your agent:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Entities** in the left sidebar menu.
  4. Select the **System** tab for system entities.



If you are building an agent using the API instead of the console, see the [EntityTypes reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes). The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API.

## Extend a system entity from the entities page

From the entities page, you can view system entities used by your agent and extend them by following these steps:

  1. Use the system entity in one of your [parameters](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters).
  2. Select **Entities** in the left sidebar menu.
  3. Select the **System** tab for system entities.
  4. The system entities currently used by your agent are listed. Entities shown in a grey font color are not extendable, and entities shown in a normal font color are extendable.
  5. You can select an extendable entity and update the extended values.
  6. Provide entity entries using the values you want to extend the entity with.



![Screenshot of system entities tab](https://docs.cloud.google.com/static/dialogflow/es/docs/images/entities-system-tabs.png)

## Extend a system entity with the API

If you are using the API to extend system entities, create system entity extensions similar to how you create [custom entities](https://docs.cloud.google.com/dialogflow/docs/entities-custom). Provide the name of the system entity you wish to extend, and provide the values you want to extend it with. If you attempt to extend a system entity that is not extendable, you will receive an error.

## Extend a system entity while annotating a training phrase

From the intent page's training phrase section, you can extend a system entity while [annotating a training phrase](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases#annotation). If you manually annotate a training phrase part with an extendable system entity that does not include the selected value, you will be prompted to add this value to the system entity.

[ Previous arrow_back  Entity options  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-options)

[ Next Custom entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-custom)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
