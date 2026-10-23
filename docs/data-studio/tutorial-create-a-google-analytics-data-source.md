---
url: https://docs.cloud.google.com/data-studio/tutorial-create-a-google-analytics-data-source/
title: Tutorial: Create a Google Analytics data source \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:40.577043+00:00
---

# Tutorial: Create a Google Analytics data source  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/tutorial-create-a-google-analytics-data-source/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Tutorial: Create a Google Analytics data source Stay organized with collections  Save and categorize content based on your preferences. 

A data source provides the data for a Data Studio report. In this tutorial, you'll create a reusable data source that connects to one of your Google Analytics accounts.

## Step 1: Connect to your Google Analytics account

The first step in creating a data source is to connect to your [dataset](https://docs.cloud.google.com/data-studio/dataset).

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. On the Data Studio home page, in the top left, click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then select **Data Source**.
  3. In the list of connectors, select **Google Analytics.**

![The Google Analytics connector chip.](https://docs.cloud.google.com/static/data-studio/images/select-ga-ds-2018-07-27.png)

  4. If you are prompted to, click **AUTHORIZE** to allow Data Studio to access you data.

  5. Select an account and a property. ![The Google Analytics connector configuration page. The Google Analytics Demo account is selected, and three properties belonging to that account are shown in the property list.](https://docs.cloud.google.com/static/data-studio/images/data-source-connector-selection-2016-03-11.png)

  6. In the upper right, click **CONNECT**. The data source configuration page appears.




## Step 2: Configure the data source

The data source configuration page contains all the dimensions (the green chips) and metrics (the blue chips) from the data set. You can fine-tune the data source by renaming or disabling fields, adding calculated fields, and changing the aggregation and data type.

Learn more about [modeling your data](https://docs.cloud.google.com/data-studio/model-your-data).

**Tip:** To create a basic report that uses Google Analytics data, you usually don't need to make any changes to the data source.

![The data source schema page.](https://docs.cloud.google.com/static/data-studio/images/data-source-fields-panel-ga.png)

### Data source settings

For this tutorial, you don't need to change any of the other data source settings.

#### Scope

_Scope_ refers to how a data source can be used in a report.

Data sources can be either _embedded_ or _reusable._ Reports can include both embedded and reusable data sources.

**Data sources that you create while editing a report are embedded** in the report. To edit an embedded data source, you do so within that report. Embedded data sources make collaborating on reports and data sources easier. Anyone who can edit the report can also edit the data source as well as modify its connection. When you share or copy the report, any embedded data sources are shared or copied as well.

**Data sources that you create from the home page are reusable**. You can reuse these data sources in different reports. Reusable data sources let you create and share a consistent data model across your organization. Only people with whom you share the reusable data source can edit it. Only the owner of the data source's credentials can modify the connection.

Learn more about [embedded data sources](https://docs.cloud.google.com/data-studio/embedded-data-sources).

#### Data credentials

Data credentials control access to the data that is provided by this data source:

  * **Owner's credentials** uses the credentials of the data source owner to authorize access to the dataset. This option lets you share reports that use this data source without requiring report viewers to have their own access to the underlying dataset.

**Important:** Before sharing a report or data source that uses Owner's credentials, be sure that you trust the person or persons with whom you share them.
  * **Viewer's credentials** require anyone who attempts to view the data that is provided by this data source to have their own access to the dataset.

  * **Service account credentials** use a special type of Google account that is intended to represent a non-human user that can authenticate and be authorized to access your data.




#### Data freshness

Data freshness refers to how current the data is in a data source. Different types of data sources have different requirements or expectations for data freshness. [Learn more about data freshness](https://docs.cloud.google.com/data-studio/manage-data-freshness).

#### Community visualizations access

Community visualizations are charts that are created by third-party developers who work with your data. These charts can be configured just like Data Studio's default charts. Before you can use a community visualization in your report, you need to turn on community visualization access in the data source. [Learn more about community visualizations](https://docs.cloud.google.com/data-studio/community-visualizations-developer-preview).

#### Field editing in reports

Field editing in reports lets report editors change field definitions at the chart level. Editing field definitions in the report makes customizing your reports faster and easier. If you don't want other editors to make changes to the field definitions, you can turn this option off. [Learn more about field editing in reports](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports). 

## Step 3: Name the data source

![](https://docs.cloud.google.com/static/data-studio/images/rename-datasource-2015-10-16.png)

Data Studio automatically gives your data source the same name as your dataset. If you want to change that, click the name in the upper left and enter a new name.

You can also rename the data source later from the DATA SOURCES home page by clicking the context menu ![](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) and selecting **Rename**.

## Step 4: Share the data source

You can let other editors add this data source to reports by sharing it with them.

### To share a data source

  1. In the upper right, click ![Share icon](https://docs.cloud.google.com/static/data-studio/images/gmpersonaddgrey60048dp-2020-03-12.png)**Share**.

  2. Enter the email addresses or Google Groups that you want to share with.

  3. For each person or group, select the access (permissions). Permissions determine what other people can do with the data source. Your choices are as follows:

     * **Can view**. People with this permission can view but not edit the data source.

     * **Can edit**. People with this permission can both view and edit the data source.




## Step 5: Use the data source in reports

![The CREATE REPORT button on the edit connection page.](https://docs.cloud.google.com/static/data-studio/images/create-report.png)

To create a report that gets its data from your Google Analytics property, Click **CREATE REPORT**.

## Related resources

  * [Google Analytics connector](https://docs.cloud.google.com/data-studio/connect-to-google-analytics)
  * [Report tutorials](https://docs.cloud.google.com/data-studio/tutorial-report-intro)
  * [Share a data source](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports)
  * [Copy a data source](https://docs.cloud.google.com/data-studio/copy-a-data-source)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data source credentials](https://docs.cloud.google.com/data-studio/data-credentials)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
