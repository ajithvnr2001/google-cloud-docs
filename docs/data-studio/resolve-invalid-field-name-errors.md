---
url: https://docs.cloud.google.com/data-studio/resolve-invalid-field-name-errors/
title: Resolve invalid field name errors \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:18:33.560220+00:00
---

# Resolve invalid field name errors  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/resolve-invalid-field-name-errors/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Resolve invalid field name errors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to fix a chart on your report that displays an "Invalid field name error."

## Why it breaks

Certain connectors support characters in their field names that Data Studio is unable to process. For example, Data Studio does not handle BigQuery fields that contain Unicode characters and special characters including ampersands, colons, among other characters.

[Learn more about BigQuery flexible column names](https://docs.cloud.google.com/bigquery/docs/schemas#flexible-column-names).

## Solution

To resolve this issue, rename the fields from the underlying dataset and then [reconnect](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection) the data source.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
