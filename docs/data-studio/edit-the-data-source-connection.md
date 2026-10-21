---
url: https://docs.cloud.google.com/data-studio/edit-the-data-source-connection/
title: Edit the data source connection \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:26.423186+00:00
---

# Edit the data source connection  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/edit-the-data-source-connection/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Edit the data source connection Stay organized with collections  Save and categorize content based on your preferences. 

You can change a data source's connection to the underlying data. This lets you connect to different data using an existing data source.

Editing the data source connection lets you:

  * Reestablish a broken connection to your data.
  * Connect to a different account, Google Sheet, database table, and such.
  * Edit a BigQuery custom query connection.
  * Use a different connector.



## Example

Suppose you have a data source based on an unfiltered Google Analytics web property and have created a Data Studio report based on that data source. Now, say you create a new filtered property in your Analytics account, and want to use that data with your existing report. To bring in the new filtered data and leave any configuration changes intact (such as calculated fields, renamed fields, or changed aggregations), you can reconnect the data source to the new property.

**Warning:** Editing a data source connection can have a big impact on your reports. **Proceed with caution.**

## Who can reconnect a data source

Anyone who can edit the data source can edit its connection. For embedded data sources, this includes report editors. For reusable data sources, you must have [Can Edit permission](https://docs.cloud.google.com/data-studio/roles-and-permissions) to the data source.

## How to reconnect a data source

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. In the upper left, click **EDIT CONNECTION**.
  3. Select the new dataset.
  4. In the upper right, click **RECONNECT**. Data Studio shows the fields changed by this action, if any.
  5. Click **APPLY**.



## Effects of reconnecting a data source

  * New fields from the dataset are added to the data source.
  * Fields that have been removed from the dataset are removed from the data source.
  * Fields that have been removed from the data source are added back to the data source.
  * If there are changes to the fields or the underlying dataset, you become the new [credentials owner](https://docs.cloud.google.com/data-studio/data-credentials). If the data source uses service account credentials, and you don't have permission to use that service account, you become the new credentials owner.
  * Other changes you've made to the data source, such as renaming fields, changing field types or aggregations, and adding descriptions, are not affected.
  * Any reports using to this data source continue to do so, however, you may need to fix any charts broken by the field changes.

**Important:** If any of the removed dimensions or metrics are used in calculated fields, those calculated fields are disabled. You can edit or remove them, as needed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
