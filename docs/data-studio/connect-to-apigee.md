---
url: https://docs.cloud.google.com/data-studio/connect-to-apigee/
title: Connect to Apigee \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:24.343928+00:00
---

# Connect to Apigee  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-apigee/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Apigee Stay organized with collections  Save and categorize content based on your preferences. 

Apigee is a platform for developing and managing APIs. The Data Studio Apigee connector lets you create reports and dashboards based on analytics and monetization data and share them with stakeholders and customers.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## How to connect to Apigee

A Data Studio data source can connect to a single Apigee organization.

### Select an individual account

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click ![The Create icon, a plus sign.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.

  3. Select the **Apigee** connector.

  4. If prompted to grant Data Studio access to your account, click **AUTHORIZE**.

> You can [revoke this access](https://support.google.com/accounts/answer/13864929#how-can-i-manage-or-delete-linked-accounts) at any time.

  5. Enter your **Apigee Organization ID**.

  6. In the upper right, click **CONNECT**.

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

## Get started quickly with templates

See your Apigee data in a completed report by using one these pre-built templates:

  * [Apigee API Analytics template](https://datastudio.google.com/reporting/6e5df694-8157-4109-a232-ba99036928b9/preview/)
  * [Apigee Monetization template](https://datastudio.google.com/reporting/8e102cf0-ed07-42d2-a75a-2c56f46e6ecf/preview/)



Learn more about [creating reports from templates](https://docs.cloud.google.com/data-studio/create-a-report-from-a-template).

## Related resources

[What is Apigee?](https://cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
