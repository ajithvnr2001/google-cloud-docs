---
url: https://docs.cloud.google.com/dialogflow/es/docs/entities-custom/
title: Custom entities \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:38.982442+00:00
---

# Custom entities  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/entities-custom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Custom entities Stay organized with collections  Save and categorize content based on your preferences. 

You can create custom entities for matching data specific to your agent. For example, you could define a `vegetable` entity type that can match the types of vegetables available for purchase with a grocery store agent.

**Note:** When building your agent, it's best to define your entities prior to adding [training phrases](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases) to your intents. The console will automatically annotate your training phrases with existing entities. However, if you create entities after training phrases, you can manually annotate the phrases.

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access custom entity data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Entities** in the left sidebar menu.
  4. Select the **Custom** tab for custom entities.



If you are building an agent using the API instead of the console, see the [EntityTypes reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes). The API field names are similar to the console field names. The instructions below highlight any important differences between the console and the API.

## Create custom entities

To create a custom [map entity](https://docs.cloud.google.com/dialogflow/docs/entities-options#map):

  1. Click **Create entity**.
  2. Enter a name for the entity.
  3. Note that **Define synonyms** is already checked.
  4. Click the first row and provide a reference value in the left column.
  5. Click the next column or press **Enter** and provide synonyms.
  6. Continue adding rows for other entity entries.
  7. Click **Save**.



![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/entities-create.png)

## Batch operations

You can move, copy, or delete multiple entities using batch operations:

  * **Copy** : Copies selected entities to the target agent.
  * **Move** : Moves selected entities to the target agent.
  * **Delete** : Permanently deletes the selected entities. This cannot be undone.



The following additional options are prompted for copy and move operations:

  * **Copy related entities** : Moves or copies entities used in [composite entities](https://docs.cloud.google.com/dialogflow/docs/entities-options#comp).
  * **Overwrite entities** : Overwrites entities with the same name.



To copy, move, or delete multiple entities:

  1. Hover you mouse over the list and select one or more entities. This reveals the batch options.
  2. Choose the desired action.
  3. Select the desired options in the dialog.
  4. Click **Start**.



## Limitations

The following limitations apply:

  * Custom entity type names are unique for each agent. Entity type names should start with a letter and can contain the following: `A-Z`, `a-z`, `0-9`, `_` (underscore), `-` (dash). Entity reference and synonym values have no such limitation.



[ Previous arrow_back  System entities  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-system)

[ Next Session entities  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-session)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
