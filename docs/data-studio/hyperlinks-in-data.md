---
url: https://docs.cloud.google.com/data-studio/hyperlinks-in-data/
title: Hyperlinks in data \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:30:09.496181+00:00
---

# Hyperlinks in data  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/hyperlinks-in-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Hyperlinks in data Stay organized with collections  Save and categorize content based on your preferences. 

You can display clickable links in your data using a table. You can create links in two ways:

  * Directly from your dataset, using the URL field type
  * Generating the link using the `HYPERLINK` function

**Important:** When users click an external link, Data Studio displays a redirect notice.

## URL field type

When you create a data source, Data Studio will detect valid URLs in the dataset and assign the URL field type to that dimension. (If Data Studio doesn't detect the URLs automatically, you can set the field type to URL manually.)

URL fields display the full link in charts. In tables, this link is clickable.

## `HYPERLINK` function

The `HYPERLINK` function lets you construct links in calculated fields. The `HYPERLINK` function takes a URL and a link label as input. The output is a clickable link when displayed in a table (in other charts, the link text is not clickable).

Only certain protocols are supported in both URL fields and the `HYPERLINK` function. See the [`HYPERLINK` documentation page](https://docs.cloud.google.com/data-studio/hyperlink) for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
