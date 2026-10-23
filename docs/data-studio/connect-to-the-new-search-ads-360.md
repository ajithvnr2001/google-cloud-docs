---
url: https://docs.cloud.google.com/data-studio/connect-to-the-new-search-ads-360/
title: Connect to the New Search Ads 360 \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:25.457382+00:00
---

# Connect to the New Search Ads 360  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-the-new-search-ads-360/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to the New Search Ads 360 Stay organized with collections  Save and categorize content based on your preferences. 

New Search Ads 360 is a search management platform that helps agencies and marketers efficiently manage some of the largest search marketing campaigns in the world, across multiple engines and media channels.

The New Search Ads 360 connector gives you access to the data from the new and improved New Search Ads 360 platform. Learn more about what's new in this [blog post](https://blog.google/products/marketingplatform/360/introducing-new-search-ads-360/).

## How to connect to New Search Ads 360

You can connect Data Studio to multiple Agencies, Advertisers, and Accounts in a single data source.

### To connect

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click add **Create** , and then select **Data Source**.

  3. Select the **New Search Ads 360** connector.

  4. Select an **Agency**.

  5. Select the **Advertisers** , and optionally, the **Accounts** to which you want to connect.

> You can connect the data source at the Advertiser or Account level. This determines which fields are available in the data source. For example, to use the _Label_ field, you must connect at the Advertiser level. To connect at the Advertiser level, leave the Account selection blank.

  6. If your account uses multiple currencies, select which currency to use in this data source.

  7. In the upper right, click **CONNECT**.

     1. The data source fields panel appears.
     2. The data source is now connected to your [data set](https://docs.cloud.google.com/data-studio/dataset).



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

## Notes

The dimensions and metrics available through Data Studio represent a subset of the fields available in New Search Ads 360.

The _Label_ dimension is only available in data sources based on the advertiser level (and not the engine level).

You'll get an error connecting to the new Search Ads 360 if your user access to the service is turned off. Google Workspace administrators can change your access in the Google Admin console. Learn more about [turning a service on or off](https://support.google.com/a/answer/182442).

## Related resources

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Learn more about New Search Ads 360](https://support.google.com/sa360/answer/9359572).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
