---
url: https://docs.cloud.google.com/data-studio/connect-to-display--video-360/
title: Connect to Display & Video 360 \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:23.971703+00:00
---

# Connect to Display & Video 360  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-display--video-360/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Display & Video 360 Stay organized with collections  Save and categorize content based on your preferences. 

Display & Video 360 offers a single tool for planning campaigns, designing and managing creative, organizing and applying audience data, finding and buying inventory, and measuring and optimizing campaigns.

You can use the Display & Video 360 connector to visualize your Display & Video 360 data and perform the following tasks in Data Studio:

  * Style and brand your reports to match your guidelines.
  * Create compelling and informative reports that can include data from multiple other sources, such Google Ads and Google Analytics.
  * Share your insights, even with people who don't have direct access to that data.
  * Data Studio reports stay current as your data changes; no need to rerun or download the report.



## How to connect to Display & Video 360

You can connect a Data Studio data source to a single Display & Video 360 partner. You can select multiple advertisers per partner.

To connect to Display & Video 360, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.

  3. Select the **Display & Video 360** connector.

  4. Select the partner and advertisers to which you want to connect.

> You can select multiple partners. If you do this, the data source includes all advertisers for those partners.

  5. In the upper right, click **CONNECT**.

     * The data source fields panel appears.
     * The data source is now connected to your [data set](https://docs.cloud.google.com/data-studio/dataset).



## Configure the data source

The data source fields panel is where you configure the data source by renaming fields and adding descriptions, adding calculated fields, and changing data types and aggregations. Learn more about [working with data source fields](https://docs.cloud.google.com/data-studio/model-your-data).

## Control who sees the data

At the top of the fields panel, you can change the data credentials. Credentials control who can see the data that this data source provides.

**OWNER'S CREDENTIALS** let other people view or create reports that use this data without requiring them to have their own access to the dataset.

**VIEWER'S CREDENTIALS** , on the other hand, require each user of the data source to provide their own credentials to access the dataset.

**SERVICE ACCOUNT CREDENTIALS** rely on a special type of Google Account that represents a non-human user that can authenticate and be authorized to access data.

[Learn more about data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article).

## Create a new report from the data source

To create a new report from the data source, follow these steps:

  1. In the upper right, click **CREATE REPORT**. The report editor appears.
  2. Click **ADD TO REPORT**. 
     1. This action adds the data source to the report.
     2. You can now create charts and controls that get their data from this data source.



### New to Data Studio?

Take the [Create a report tutorial](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report).

## Use a template report

Want to get started quickly? Copy this [template report](https://datastudio.google.com/reporting/1u8yeqgfWIv4iI6eX-vCzNKw0jPN9z8vD/page/pWmV/preview) and add your own Display & Video 360 data source. You'll have a fully functioning and attractive report in under a minute.

The following example report is only available in English.

## Limits of the Display & Video 360 connector

The dimensions and metrics available through Data Studio represent a subset of the fields available in Display & Video 360 Instant Reporting.

Campaign Manager and Display & Video 360 [data freshness and availability limits](https://support.google.com/campaignmanager/answer/6110224) apply to the data you'll see in your Data Studio reports.

## Related resources

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Learn more about Display & Video 360](https://support.google.com/displayvideo).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
