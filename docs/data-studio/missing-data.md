---
url: https://docs.cloud.google.com/data-studio/missing-data/
title: Missing data \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:44:45.332930+00:00
---

# Missing data  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/missing-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Missing data Stay organized with collections  Save and categorize content based on your preferences. 

There can be several reasons why reports or data sources don't show all the information that you expect. This page provides an overview of issues to troubleshoot for when your reports or data sources may showing missing or incomplete data.

## Missing data in reports

The following sections provide potential issues to check for in reports when data is incomplete or missing.

### Is the data out-of-date?

If the report is missing some recently added data, [try refreshing the report data](https://docs.cloud.google.com/data-studio/manage-data-freshness).

**Note:** You must be an editor of the report to refresh the data.

### Is the data filtered?

Edit the report, then click **Resources > Manage Added Filters** to see if there are any filter properties in the report. If there are, check their setup to make sure that's not the cause of the missing data.

## Missing fields in data sources

The following sections provide potential issues to check for in data sources when data is incomplete or missing.

### Is the data source out of sync with the dataset?

If the data source is missing some recently added fields (columns), [try refreshing data source fields](https://docs.cloud.google.com/data-studio/refresh-data-source-fields).

### Is your Google Sheets data source missing rows or columns?

If the rows (data) or columns (fields) of your Sheets data source are still not appearing after [refreshing the report data](https://docs.cloud.google.com/data-studio/manage-data-freshness), make sure the data source connection includes the proper range and options. You must be the owner of the data source to do this.

  1. Edit the data source.
  2. On the left, click **EDIT CONNECTION**.
  3. Review the connection options, on the right. Be sure any specified range includes all your data, and that you are including hidden and filtered fields, if appropriate.



![Connector options in the EDIT CONNECTION menu.](https://docs.cloud.google.com/static/data-studio/images/sheets-ds-options-2018-07-20.png)

### Is it a connector limitation?

Connectors that are based on fixed schemas, which include many of the Google product connectors, may not deliver all the fields of the underlying dataset. If your data source appears to be missing fields that you know are in the original product, it's possible that field is not supported in Data Studio. You can [check the issue tracker](https://issuetracker.google.com/issues?q=status:open%20componentid:196095) to see if the field has already been requested, or if not, file a feature request.

[Learn more about connectors, data sources, and credentials](https://docs.cloud.google.com/data-studio/about-connectors-data-sources-and-credentials).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
