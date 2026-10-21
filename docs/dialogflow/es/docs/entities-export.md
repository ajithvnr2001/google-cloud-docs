---
url: https://docs.cloud.google.com/dialogflow/es/docs/entities-export/
title: Export and import entities \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:38.786340+00:00
---

# Export and import entities  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/entities-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Export and import entities Stay organized with collections  Save and categorize content based on your preferences. 

You can export and import entities to simplify creation or movement of large amounts of entity data.

## Where to find this data

When building an agent, it is most common to use the Dialogflow ES console ([visit documentation](https://docs.cloud.google.com/dialogflow/docs/console), [open console](https://dialogflow.cloud.google.com)). The instructions below focus on using the console. To access entity options data:

  1. Go to the [Dialogflow ES console](https://dialogflow.cloud.google.com).
  2. Select an agent.
  3. Select **Entities** in the left sidebar menu.
  4. Select the **Custom** tab for [custom entities](https://docs.cloud.google.com/dialogflow/docs/entities-custom) defined for your agent or the **System** tab for [system entities](https://docs.cloud.google.com/dialogflow/docs/entities-system) used by your agent.



## Format

The hand-editable import/export format is either JSON or CSV.

### JSON format

See the [`EntityType`](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#entitytypes) REST reference.

### CSV format

The CSV content should have the following format:

  * Each entity entry is on one line and ends with a newline.
  * Each value should be enclosed in double quotes.
  * Each value should be separated by commas.
  * For a [map entity](https://docs.cloud.google.com/dialogflow/docs/entities-options#map): 
    * The reference value should be at the beginning of the line, followed by synonyms.
    * Include the reference value twice if you want it to be matched by the entity.
  * For a [list entity](https://docs.cloud.google.com/dialogflow/docs/entities-options#list): 
    * Each line contains a single value.



For example, the following are two map entity entries:
    
    
    "New York City", "New York City", "NYC", "New York City, USA"
    "Philadelphia", "Philadelphia", "Philly", "Philadelphia, USA"
    

## Export

To export an entity:

  1. Hover your mouse over an entity and click the cloud download _cloud_download_ icon.
  2. Choose **JSON** or **CSV** for the format.
  3. Choose a location on your system to save the file.



## Import

To import an entity:

  1. Click the more _more_vert_ icon.
  2. Click **Upload entity** and choose the file.



[ Previous arrow_back  Fuzzy matching  ](https://docs.cloud.google.com/dialogflow/es/docs/entities-fuzzy)

[ Next Contexts  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/contexts-overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
