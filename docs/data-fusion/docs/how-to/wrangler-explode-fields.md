---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-explode-fields/
title: Explode data from fields \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:30.051590+00:00
---

# Explode data from fields  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-explode-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Explode data from fields Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to separate data from a field (a cell) into multiple rows when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

## Separate delimited text

You can separate the values from a cell into new rows if the values are separated by the following delimiters:

  * Comma
  * Tab
  * Pipe
  * Whitespace
  * Custom separator



If a cell doesn't contain the chosen delimiter, no new row is inserted.

To split values based on a delimiter, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Click **Explode > Delimited text**.
  4. Choose a delimiter—for example **Pipe**.
  5. Click **Extract**.

**Note:** If you select Custom separator, define the delimiter with a regular expression.



Wrangler splits the fields based on the selected delimiter and adds the `split-to-row` directive to the recipe. When you run the data pipeline, Cloud Data Fusion applies the transformation to all values in the column.

In this example, a dataset has a column of string values containing the comma delimiter:

ID | Name  
---|---  
1 | Lee,Lucian,Luka  
2 | Mahan,Noam  
  
To divide the value into separate rows, Wrangler deletes the original column and creates a new column with one row for each value. The other column values from the original row are copied into the new rows:

ID | Name_1  
---|---  
1 | Lee  
1 | Lucian  
1 | Luka  
2 | Mahan  
2 | Noam  
  
## Separate arrays

The `flatten` directive separates items in arrays, such as `["ELEMENT_1", "ELEMENT_2", "ELEMENT_3"]`, into new rows. The other column values from the original record are copied into the new records.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
