---
url: https://docs.cloud.google.com/data-studio/data-control/
title: Data control \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:40.625309+00:00
---

# Data control  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/data-control/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data control Stay organized with collections  Save and categorize content based on your preferences. 

The data control lets you select the dataset that is used by a report without having to edit the data source connection. This lets you quickly share reports with viewers who want to use that report with their own data. Using a data control eliminates the need to create separate reports and data sources for your various accounts.

## How the data control works

The data control lets a report viewer change the [dataset](https://docs.cloud.google.com/data-studio/dataset) used by a specific type of [data source](https://docs.cloud.google.com/data-studio/data-source). To understand how the data control works, it's helpful to review how reports without a data control behave:

**Without a data control** , each data source in the report connects to a specific dataset. For example, a Google Analytics data source connects to a single Analytics reporting view, a Google Ads data source connects to a single account or manager account, etc. Every chart or control in the report gets its data from that one specific dataset. The only way the report can display different data is to edit it and select a different data source, or to reconnect the data source to a different dataset.

**When you add a data control** of a particular type, the original dataset remains as the default. But, anyone viewing the report can use the data control to change to a different dataset to which they have access.

**Note:** Data controls only show the accounts to which you have access. 

The data control doesn't give you access to other people's data. As always, access to data is governed by the [credentials](https://docs.cloud.google.com/data-studio/data-credentials) of the data source.

You can have multiple data controls in a single report. The data control supports the following datasets:

  * Google Analytics (Universal Analytics and Google Analytics 4)
  * Google Ads
  * Attribution 360 (TV Attribution)
  * Google Ad Manager
  * Campaign Manager 360
  * Search Console
  * YouTube



### Example

You've created a report based on a YouTube data source that connects to your marketing video channel. Anyone viewing the report can only see the data from the marketing channel dataset.

You then add a YouTube data control to the report. All of the charts on the page with the data control continue to show your marketing channel data, because the marketing channel is the default dataset for that data source.

Finally, you share the report with Alicia, who has access to the product support video channel. She sees the default marketing channel data, but can use the data control to switch the report to display the support channel data.

## Data control scope

By default, a data control of a given connector type affects all the charts on the current page that are based on that type. For example, a YouTube data control affects all the charts based on a YouTube data source, a Search Console data control affects the charts based on a Search Console data source, etc. Just like filter controls and date range controls, you can limit the scope of a data control so that it affects only charts [grouped](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components#group_ungroup) with the data control. This lets you use multiple groups of data controls and charts to display data from different accounts on the same page.

To have a data control affect the entire report, make it a [report-level](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components#make_report-level_make_page-level) component. The data control then appears on every page.

## Bookmark a view

The data control stores the selected account in the URL, allowing you to save the configuration by bookmarking the current report. This lets you quickly return to a particular version of the report or share that version with others by sending them the bookmarked link.

## Use Cases

The following examples demonstrate the applications of the data control in different use cases.

### Support cross-functional use of data

Suppose your organization tracks digital analytics for distinct Marketing and Sales websites, and a Support mobile app. You could build a single default report to be shared across your organization and include a data control in the report. Users in each department could use data controls to select the Analytics and Google Ads accounts that are relevant to them.

![The Search for your Google Analytics View drop-down list displays the views an example user can access, including 1 Master View, Analytics Academy, Custom Dimension View, and Data Import Text.](https://docs.cloud.google.com/static/data-studio/images/data-control-example-2017-06-07.png)

### Help new users see their data in Data Studio

Even if someone doesn't know how to use Data Studio, any report that includes a data control can show them their own data. This lets you create public reports which the user can then adapt to their own data. When the user first comes to Data Studio, they are prompted to authorize access to the relevant accounts. They can then use the data controls you've placed on the report to select one of their own accounts.

## Limits of the data control

  * If someone switches to a dataset that doesn't contain the metrics or dimensions used in your charts, they will see errors in those charts. For example, if you include a custom dimension from Google Analytics in your chart, but the user switches to a view that doesn't contain that custom dimension, the chart may break.
  * Data controls don't work in [embedded reports](https://docs.cloud.google.com/data-studio/embed-a-report).



## Related resources

  * [Configure report components](https://docs.cloud.google.com/data-studio/configure-report-components)
  * [Google product connectors](https://docs.cloud.google.com/data-studio/connect-to-google-ads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
