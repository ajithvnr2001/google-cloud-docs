---
url: https://docs.cloud.google.com/data-studio/refresh-data-source-fields/
title: Refresh data source fields \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:16.913552+00:00
---

# Refresh data source fields  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/refresh-data-source-fields/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Refresh data source fields Stay organized with collections  Save and categorize content based on your preferences. 

If you add, remove, or change the fields in your underlying dataset, report editors can refresh the data source to see those changes in Data Studio.

**Important:** Refreshing fields applies only if the structure (schema) of your [dataset](https://docs.cloud.google.com/data-studio/dataset) changes. To see new data in the report, [refresh the report data](https://docs.cloud.google.com/data-studio/manage-data-freshness).

## When to refresh data source fields

Data Studio doesn't automatically detect schema changes in your dataset.

If you perform one of the following tasks, you should refresh the data source fields so that they both match:

  * Adding new fields to the dataset
  * Removing fields from the dataset
  * Renaming fields in the dataset
  * Reordering fields in the dataset



For example, if you add new columns to a Google Sheet, or modify the SQL query that is used in a custom BigQuery connection to return more or fewer fields, you should refresh the data source.

**Important:** If the structure of your dataset changes but you **don't refresh** , your data source and the dataset will be out of sync. This can cause unpredictable results.

### To refresh data source fields

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. In the bottom left corner, click **REFRESH FIELDS**.
  3. If changes are found, click **APPLY**.



![](https://docs.cloud.google.com/static/data-studio/images/refresh-ds-fields.png)

## Effects of refreshing data source fields

**Important:** Refreshing fields can cause significant changes to the data source and any reports that use it. **These changes, once made, cannot be undone**. Proceed with caution.

When you refresh data source fields, the following actions occur:

  * New fields from the dataset are added to the data source. Only fields containing data are added (empty fields are ignored).
  * Fields that have been removed from the dataset are removed from the data source.
  * Fields that have been removed from the data source are added back to the data source.
  * Fields that have been renamed are treated as if you've removed the old field and added a new one. The new name is NOT applied to the old field.
  * Reordered fields are not listed in the changes found but the changed order is applied to the internal structure of the data source (you won't see this change).
  * Reports already added to this data source remain attached, however, you may need to fix any charts broken by the field changes.
  * Calculated fields that use a removed or renamed field are disabled. You can edit or remove the calculated field, as needed.
  * Charts that use a removed or renamed field will show a configuration error. You can edit or remove the chart, as needed.

**Note:** Changing field types or aggregations in the dataset are not detected by refreshing fields. You'll need to reconnect the data source to see these changes. See the next section.

### A note on changing languages and refreshing fields

Google Analytics and Google Ad Manager both support dynamic interface language switching: if you [change your Google language](https://support.google.com/accounts/answer/32047), you'll see those products appear in the new language (provided that language is supported by Analytics or Google Ad Manager).

Similarly, if you create an Analytics or Google Ad Manager data source in one language, switching languages and refreshing the data source fields changes the displayed field names to the selected language.

For example, suppose you create an Analytics data source while your Google language is set to English. The data source field names will appear in English. If you then change your language to Italian and refresh the data source fields, the displayed names now appear in Italian. Note that any dimensions or metrics you've explicitly renamed in the data source will revert to their default names in the new language, but calculated fields, and fields you've renamed in the report, won't be changed. [Learn more about changing your Google language](https://support.google.com/accounts/answer/32047).

## Related resource

[Edit the data source connection](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
