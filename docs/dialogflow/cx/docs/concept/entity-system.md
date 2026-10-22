---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system/
title: System entities \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:55.271927+00:00
---

# System entities  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  System entities Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow CX provides many _system entities_ to extract common types from end-user expressions. For example, the `@sys.color` type can be used to extract values like "red" or "blue". You can see the full list of system entities in the [System entity reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities).

For most applications, the values provided by system entities work well. However, your application may need to add additional values for system entities. For example, you may want to add "blue-green" to the list of values for `@sys.color`. Some system entities can be extended for this purpose. The [System entity reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities) lists the system entities that can be extended.

System entity support differs for [languages](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) and [regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region). See the [system entity limitations](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities#limits) for details.

## Extend a system entity

To extend a system entity:

###  Console 

  1. Use the system entity in one of your [parameters](https://docs.cloud.google.com/dialogflow/docs/intents-actions-parameters).
  2. Select the **Manage** tab.
  3. Click **Entity Types**.
  4. Select the **System** tab for system entities.
  5. The system entities currently used by your agent are listed. Entities shown in a grey font color are not extendable, and entities shown in a normal font color are extendable.
  6. You can select an extendable entity and update the extended values.
  7. Provide entity entries using the values you want to extend the entity with.



![Screenshot of system entities tab](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/cx-entity-system-list.png)

###  API 

Creating system entity extensions is similar to how you create [custom entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom). Provide the name of the system entity you wish to extend, and provide the values you want to extend it with. If you attempt to extend a system entity that is not extendable, you will receive an error.

[ Previous arrow_back  Entity options  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-options)

[ Next Custom entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
