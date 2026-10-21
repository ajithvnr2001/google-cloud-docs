---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-format-strings/
title: Format strings \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:28.606154+00:00
---

# Format strings  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-format-strings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Format strings Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to format strings when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

To format a **String** column, follow these steps:

  1. [Go to the Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Format** and select an option—for example, **TitleCase**. The options are explained in the following sections.



Wrangler performs the transformation on the column's values in Preview mode and adds the corresponding directive to the recipe. When you run the data pipeline, the transformation is applied to all values in the column.

## Change the case of the strings

To change the letter case, follow the steps in the preceding section and choose one of the following options.

Option | Description  
---|---  
**UPPERCASE** | Changes the letter case of strings to all-uppercase—for example, `1800 Amphibious Blvd.` changes to `1800 AMPHIBIOUS BLVD.`  
**lowercase** | Changes the letter case of strings to all-lowercase—for example, `1800 Amphibious Blvd.` changes to `1800 amphibious blvd.`  
**TitleCase** | Changes the letter case to capitalize the first letter of each word—for example, `1800 amphibious blvd.` changes to `1800 Amphibious Blvd.`  
  
## Concatenate the strings

To append characters to the beginning or end of all string values in a column, follow these steps:

  1. [Go to the Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Click **Format > Concatenate**.
  4. In the **Add** field, enter the string to add to the existing values.
  5. Select where to add the new value in the string by choosing **at the beginning** or **at the end**.
  6. Optional: to create a new column for the concatenated strings, select the **Copy to a new column** checkbox.

**Tip:** To prevent adding characters to null or blank values, filter out the null and blank values before performing this task.

**Example**

This example shows the input and output values when you add the string `NEW-` to the beginning of each value in a column:

Input | Output  
---|---  
`bread` | `NEW-bread`  
`butter` | `NEW-butter`  
  
## Trim spaces from the strings

To trim spaces, follow the steps to format a string column at the beginning of this page and choose one of the following options:

Option | Description  
---|---  
**Trim whitespace** | Removes trailing and leading spaces (`trim`).  
**Trim leading whitespace** | Removes leading spaces (`ltrim`).  
**Trim trailing whitespace** | Removes trailing spaces (`rtrim`).  
  
## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
