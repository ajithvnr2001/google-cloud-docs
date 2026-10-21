---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-extract-fields/
title: Extract data from fields \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:30.120237+00:00
---

# Extract data from fields  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-extract-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Extract data from fields Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to extract and transform data from a field (a cell) when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

To perform transformations on this data, you split it into separate columns. In Wrangler, you can extract data from a column and create new columns for the extracted data. You can extract values based on patterns, delimiters, or positions.

## Extract data using patterns

You can extract data from fields in columns of the string data type with the following patterns:

  * Credit cards
  * Date
  * Date time
  * Email
  * URLs from HTML anchors
  * IPv4 address
  * ISBN codes
  * Mac address
  * N digits number
  * SSN
  * Start and End pattern
  * Time



To extract data based on a pattern, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Extract fields > Using patterns** and select an option—for example, **URL**.
  4. Optional: click **Show pattern** to view the regular expression for the pattern.
  5. Click **Extract**.



Wrangler extracts the fields based on the chosen pattern and adds the `extract-regex-groups` directive to the recipe. When you run the data pipeline, Cloud Data Fusion applies the transformation to all rows in the column.

In the following example, a column contains a number, followed by an email address:

Emails  
---  
1 222larabrown@gmail.com  
2 cloudysanfrancisco@gmail.com  
  
To extract the email address, select the **Email** pattern. When you click **Extract** , Wrangler retains the original column and creates a new column containing only the email addresses:

Emails | Emails_1  
---|---  
1 222larabrown@gmail.com | 222larabrown@gmail.com  
2 cloudysanfrancisco@gmail.com | cloudysanfrancisco@gmail.com  
  
## Extract data with delimiters

You can extract data into two or more columns based on the following delimiters:

  * Comma
  * Tab
  * Pipe
  * Whitespace
  * Custom separator

**Note:** If you select the **Custom separator** option, define the delimiter with a regular expression. It supports standard Java regular expression constructs.

If a value doesn't have the delimiter, no value is added to corresponding field in the new column.

To extract values based on a delimiter:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Extract fields > Using delimiters** and select an option—for example, **Comma**.
  4. Click **Extract**.



Wrangler extracts the fields based on the selected delimiter and adds the `split-to-columns` directive to the recipe. When you run the data pipeline, Cloud Data Fusion transforms all values in the column.

In the following example, a column contains multiple names separated by commas:

ID | Name  
---|---  
1 | Lee,Lucian,Luka  
2 | Mahan,Noam,Nur  
  
In this example, using the comma delimiters pattern extracts the values in the original `Name` column into three new columns:

ID | Name | Name_1 | Name_2 | Name_3  
---|---|---|---|---  
1 | Lee,Lucian,Luka | Lee | Lucian | Luka  
2 | Mahan,Noam,Nur | Mahan | Noam | Nur  
  
## Extract data by position

You can extract part of a string based on its position in the string.

To extract data based on its position:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Extract fields > Using positions**. Column values you can extract appear with a blue background.
  4. In any cell of the column, select the characters to extract.
  5. In the **Name of destination column** field, enter a name.
  6. Click **Apply**.



The chosen portion of the value is extracted from each row in the column.

Wrangler extracts the fields based on the selected pattern and adds the `cut-character` directive to the recipe. When you run the data pipeline, Cloud Data Fusion applies the transformation to all values in the column.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
