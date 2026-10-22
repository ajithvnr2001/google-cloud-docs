---
url: https://docs.cloud.google.com/data-studio/connect-to-campaign-manager-360/
title: Connect to Campaign Manager 360 \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:33.889920+00:00
---

# Connect to Campaign Manager 360  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-campaign-manager-360/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Campaign Manager 360 Stay organized with collections  Save and categorize content based on your preferences. 

Campaign Manager 360 lets you measure digital marketing campaign performance by reporting on metrics like impressions, clicks, conversions, and ad spend, all broken out by dimensions such as campaigns, advertisers, placements, creatives, devices, and geographies.

With the Campaign Manager 360 connector, you can access and transform your Campaign Manager 360 data to generate and share dashboards with your stakeholders.

## How to connect to Campaign Manager 360

A Data Studio data source can connect to either an entire advertising network, or to a single advertiser.

**Note:** At this time, it's not possible to connect to a subset of advertisers.

To connect to Campaign Manager 360, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. Select the **Campaign Manager 360** connector.
  4. Select a network from the **Profiles** column. 
     1. To connect to an entire advertising network, select **All Advertisers** from the **Accounts** column.
     2. To connect to a single advertiser, select that advertiser from the **Accounts** column.
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

**Tip: Want to use this data source with different accounts?** Try adding a data control. 

Data controls give report viewers a way to select the account that provides the data that they want to see in a report. Data controls can eliminate the need to create separate reports and data sources for your various accounts. [Learn more about data controls](https://docs.cloud.google.com/data-studio/data-control).

## Things to know

The dimensions and metrics available through Data Studio represent a subset of the fields available through the Campaign Manager 360 Report Builder tool or the Campaign Manager 360 API. Learn more about Campaign Manager 360 [dimensions](https://support.google.com/campaignmanager/faq/6170528) and [metrics](https://support.google.com/campaignmanager/table/6170532).

The Campaign Manager 360 connector returns a maximum of 2 years' worth of data.

## Related resources

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Learn more about Campaign Manager 360](https://support.google.com/campaignmanager#topic=4387660).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
