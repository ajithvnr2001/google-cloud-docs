---
url: https://docs.cloud.google.com/data-studio/use-controls-across-data-sources/
title: Filter across data sources \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:52.748206+00:00
---

# Filter across data sources  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/use-controls-across-data-sources/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Filter across data sources Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to enable a filter control on a report to filter charts that are based on different data sources. For example, you can make a filter control work across charts that are based on Google Sheets and BigQuery data sources. You do this by overriding field IDs at the report level.

## The problem

As noted in the [About controls](https://docs.cloud.google.com/data-studio/about-controls#filters_are_based_field_id_not_display_name) page, fields from different data sources can have differing field IDs that are separate from their display names. Since filter controls are based on the field ID, filtering across data sources may fail.

### The solution

If a control isn't filtering all the charts that you expect, it's likely because the field IDs don't match. You can fix this by assigning the same ID to the fields that are used in the charts. If a filter control isn't filtering all the charts that you expect, it's likely because the field IDs don't match. You can fix this by assigning the same ID to the fields that are used in the charts.

## Before you begin

Ensure you have a report that contains charts using two or more different data sources.

## Override a field name or ID

To override a field's display name or ID, perform the following steps:

  1. In the menu, go to **Resource** > **Manage field names and IDs**.
  2. Click **Add field override**.
  3. From the **Select a field** drop-down, choose the field that you want to override.
  4. Optional: In the **New display name** field, enter a new name for the field.
  5. In the **New ID** field, enter a new ID for the field.



## Notes and limitations

When changing field IDs, keep in mind the following points:

  * You can change a field ID only at the report level. You can't override a field ID at the chart or data source level.
  * Changing a field ID that is already in use in the report breaks any charts that use that field. You must manually select the new field in each broken chart to fix it.
  * When you change multiple fields to use the same field ID, be sure that the fields are of the same data type.



## Related resources

  * Learn more about [working with data sources](https://docs.cloud.google.com/data-studio/edit-a-data-source-article).
  * Learn how to [add filter controls to reports](https://docs.cloud.google.com/data-studio/about-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
