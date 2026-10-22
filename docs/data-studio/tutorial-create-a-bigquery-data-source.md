---
url: https://docs.cloud.google.com/data-studio/tutorial-create-a-bigquery-data-source/
title: Tutorial: Create a BigQuery data source \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:51.483693+00:00
---

# Tutorial: Create a BigQuery data source  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/tutorial-create-a-bigquery-data-source/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Tutorial: Create a BigQuery data source Stay organized with collections  Save and categorize content based on your preferences. 

In this lesson, you'll use the data source tool to build a connection to a BigQuery table. You can use the publicly available table described here, or substitute your own table.

**Important:** BigQuery is a paid product and you will incur BigQuery usage costs when accessing BigQuery through Data Studio. To create a BigQuery data source, you'll need to [set up a billing project](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account?sjid=7792967446974699138-NC), if you don't already have one.

## Step 1: Connect to BigQuery

The first step in creating a data source is to connect to your [dataset](https://docs.cloud.google.com/data-studio/dataset).

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![The Create icon.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. Select the **BigQuery** connector. The _Configuration_ panel appears.
  4. Select **PUBLIC DATASETS.**
  5. For the **Dataset** , select `samples`.
  6. For the **Table,** select `shakespeare`.
  7. Select your **Billing Project.**  
![The Select Connector panel for a BigQuery connection displays options for Projects, Billing Projects, Data Sets, and the available Tables.](https://docs.cloud.google.com/static/data-studio/images/create-datasource-bq-2017-07-14.png)
  8. Click **CONNECT.** The _Fields_ panel appears.  
![The fields panel displays the Index, Field name, ID, Type, Aggregation, and Description settings for data source fields.](https://docs.cloud.google.com/static/data-studio/images/data-source-fields-panel-bq-2015-10-16.png)



The fields panel contains all the dimensions (in green) and metrics (in blue) from the dataset. You can fine-tune the data source by renaming or disabling fields, changing the data type, and more.

## Step 2: Rename your data source

![](https://docs.cloud.google.com/static/data-studio/images/rename-datasource-2015-10-16.png)

Data Studio automatically names your data source the same as your dataset name. If you want to change that, click the name in the upper left and enter a new name.

You can also rename the data source later from the DATA SOURCES home page by clicking the context menu and selecting **Rename**.

## Step 3: Optional — Share the data source

You can let other editors add this data source to reports by sharing it with them.

### To share a data source

  1. In the upper right, click ![Share icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png)**Share**.

  2. Enter the email addresses or Google Groups that you want to share with.

  3. For each person or group, select the access (permissions). Permissions determine what other people can do with the data source. Your choices are as follows:

     * **Can view**. People with this permission can view but not edit the data source.

     * **Can edit**. People with this permission can both view and edit the data source.

![](https://docs.cloud.google.com/static/data-studio/images/share-data-source-2016-05-24.png)




If you want to let other editors use this data source to create reports, you'll need to share it with them.

There are 2 aspects to sharing data sources:

  * **Granting access to the data set (credentials)**. By default, when you create a data source, Data Studio uses your credentials to authorize access to the dataset. These credentials are stored securely and passed through by the data source to the underlying dataset. Other people can then view or create reports that use this data without requiring them to have their own access to the dataset.

You can instead require each user of the data source and any reports built on it to provide their own credentials to the dataset. To do this:

    1. Select the CONFIGURATION tab
    2. Change the **Data source access** to **Viewer's Credentials**
  * Granting access to the data source (permissions). Permissions determine what other people can do with the data source. Your choices are:

    * **Can view**. People with this permission can view but not edit the data source.
    * **Can edit**. People with this permission can both view and edit the data source.



There are some important considerations to keep in mind when sharing data sources and reports. See the **Related resources** section for links to more information.

## Step 4:Use this data source in reports

![The CREATE REPORT button on the edit connection page.](https://docs.cloud.google.com/static/data-studio/images/create-report.png)

Click **Create Report** in the upper right.

You can now create reports that get their data from your BigQuery project.

## Related resources

  * [BigQuery connector](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery)
  * [Share a data source](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports)
  * [Data source credentials](https://docs.cloud.google.com/data-studio/data-credentials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
