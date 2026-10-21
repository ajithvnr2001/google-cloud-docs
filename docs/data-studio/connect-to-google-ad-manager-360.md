---
url: https://docs.cloud.google.com/data-studio/connect-to-google-ad-manager-360/
title: Connect to Google Ad Manager 360 \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:23.577208+00:00
---

# Connect to Google Ad Manager 360  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-google-ad-manager-360/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Google Ad Manager 360 Stay organized with collections  Save and categorize content based on your preferences. 

You can connect your Google Ad Manager account to Data Studio to access and visualize your ad performance metrics. You can then use Data Studio to build custom reports and securely share them with people in your organization or publicly without granting direct account access.

> This feature is only available to Google Ad Manager 360 customers.

## Get started

#### Enable Data Studio reporting for your Ad Manager network

  1. [Sign in](https://admanager.google.com) to Google Ad Manager.
  2. Click **Admin** arrow_forward_ios **Global settings**.
  3. Scroll to "Report settings" and enable **Reports in Data Studio**. _Only available in Google Ad Manager 360._
  4. Click **Save**.



#### Add a new permission to Ad Manager user roles

  1. [Sign in](https://admanager.google.com) to Google Ad Manager.
  2. Click **Admin** arrow_forward_ios **Access & authorization** arrow_forward_ios **Roles**.
  3. Select the user role associated with users who need to create Data Studio reports.
  4. Next to "Reporting," add the **View and share access to reporting data in Data Studio** permission.
  5. Click **Save**.



The built-in "Administrator" and "Executive" roles already have this permission.

## Add Ad Manager as a data source in Data Studio

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click add **Create** , and then select **Data Source**.

  3. Select the **Ad Manager** connector.

  4. If prompted to grant Data Studio access to your account, click **AUTHORIZE**.

> You can [revoke this access](https://support.google.com/accounts/answer/14012355) at any time.

  5. Click **Available networks.**

  6. Select the Ad Manager network you enabled, then select **Historical** as the report type.

  7. In the upper right, click **Connect**.

     1. The data source fields panel appears.
     2. The data source is now connected to your [data set](https://docs.cloud.google.com/data-studio/dataset).
  8. In the upper right, click **Create report** to [develop your first report](https://docs.cloud.google.com/data-studio/tutorial-create-a-new-report).




> **Unable to connect?** Make sure your Ad Manager network has enabled the "Ad Manager Reporting in Data Studio" network setting and that your Ad Manager user role has the "View and share access to Ad Manager data in Data Studio" permission. All Ad Manager networks associated with your Google account appear here, even if these settings are not enabled.

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

## Tips for creating Ad Manager reports in Data Studio

Your new Ad Manager data source lets you visualize Ad Manager reporting data in Data Studio. The most popular [dimensions](https://support.google.com/admanager/table/7531695) and [metrics](https://support.google.com/admanager/topic/7454305) from the "Historical" report type in Ad Manager are available. Use the [Ad Manager report template](https://datastudio.google.com/c/u/0/org//reporting/1vvYq5_4sI_BE9Dfi8Rf60ytXmSrplE7-/page/nmbK/preview) to get started quickly.

The "Ad Exchange historical" report type and the key-values dimension are not available.

> **How to separate Ad server, AdSense, and Ad Exchange data**  
>  Only the [Total report metrics](https://support.google.com/admanager/table/7568664) are included in Data Studio reports. Use the [Demand channel](https://support.google.com/admanager/table/7531695#demand-channel) dimension field to see Ad server, AdSense, and Ad Exchange subtotals.

[Share reports](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports) with other people with view-only or edit access. When sharing a report, the [data source access credentials you choose](https://docs.cloud.google.com/data-studio/data-credentials) determine what users can see in the report.

**Caution:** **Use caution when sharing** For optimal security, share reports with view-only access and use the viewer's data source credential. The "Viewer's credential" requires each report viewer to have Ad Manager access.

Permission to edit reports can allow any user to gain access to more than you intended to share. For example, if you share a report filtered by a particular advertiser, but grant edit access to users, they could remove that filter and see all of your data.

### Common questions

####  Why is my report loading slowly? 

To ensure a positive Ad Manager reporting experience, each Ad Manager network is allotted a set amount of resources for data requests. Data requests from Data Studio and the Ad Manager API for your network are prioritized after requests from Ad Manager reporting.

If many users in your network are running Ad Manager reports, your Data Studio reports might load more slowly.

####  How can I make my reports faster? 

  * Include fewer dimensions and metrics in your charts. 
  * Reduce the date range of your charts. 
  * Reduce the number of charts on each page of your report, or distribute large groups of charts across multiple pages. Each chart represents a report request to Ad Manager, so many charts compete for your network's allotted Ad Manager reporting resources. 
  * See also: [ Improve Data Studio performance ](https://docs.cloud.google.com/data-studio/improve-performance)

**Tip: Want to use this data source with different accounts?** Try adding a data control. 

Data controls give report viewers a way to select the account that provides the data that they want to see in a report. Data controls can eliminate the need to create separate reports and data sources for your various accounts. [Learn more about data controls](https://docs.cloud.google.com/data-studio/data-control).

## **Related resources**

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Learn more about Ad Manager](https://support.google.com/admanager/topic/7505788).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
