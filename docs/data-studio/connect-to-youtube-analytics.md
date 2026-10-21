---
url: https://docs.cloud.google.com/data-studio/connect-to-youtube-analytics/
title: Connect to YouTube Analytics \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:24.631152+00:00
---

# Connect to YouTube Analytics  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-youtube-analytics/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to YouTube Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Bring your YouTube channel analytics data into Data Studio by using the YouTube Analytics connector. You can create custom reports and dashboards to monitor your channel's performance and share insights with your team.

## How to connect to YouTube Analytics

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click add **Create** , and then select **Data Source**.

  3. Select the **YouTube Analytics** connector.

  4. If prompted to grant Data Studio access to your account, click **AUTHORIZE**.

> You can [revoke this access](https://support.google.com/accounts/answer/3466521) at any time.

  5. Select a connection option and provide your connection details.

  6. In the upper right, click **CONNECT**.

     1. The data source fields panel appears.
     2. The data source is now connected to your [data set](https://docs.cloud.google.com/data-studio/dataset).



### Connection options

When creating a YouTube Analytics data source, you can connect to your YouTube channel data in the following ways:

#### All

The **All** option provides a list of all the accounts and channels to which you have access.

#### My Channel

The **My Channel** option provides a list of the channels associated with your current Google Account.

#### Content Owners

If you use [YouTube's Content ID Matching](https://support.google.com/youtube/answer/2797370) system, you are considered to be a YouTube Content Owner. You can manage multiple channels, and allow other users to access this channel data on your behalf. The Content Owners option provides a list of all the content owner accounts to which you have access. Selecting an account will then show you a list of your channels.

#### Advanced

Use the **Advanced** option to specify either a channel or a content owner ID directly.

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

Only 50 channels are displayed in the **Content Owners** and **Google+ Pages** options. Use the advanced option to access other channels.

To protect viewer privacy, if there are fewer than 10 viewers of a video, country and state data won't appear in the report.

On March 31, 2025, YouTube changed the way views are calculated: the Views metric will count the number of times a Short starts to play or replay, with no minimum watch time requirement. If you created a data source before this date, you don't need to take any action: the changes are automatically applied to your data source.

The existing Shorts view metric, now called "Engaged views," is available in YouTube Analytics. We will add this metric to Data Studio in the coming months.

[Learn more about the change to YouTube Shorts views](http://support.google.com/youtube?p=shorts_viewcount).

**Tip: Want to use this data source with different accounts?** Try adding a data control. 

Data controls give report viewers a way to select the account that provides the data that they want to see in a report. Data controls can eliminate the need to create separate reports and data sources for your various accounts. [Learn more about data controls](https://docs.cloud.google.com/data-studio/data-control).

## Related resources

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [Learn more about YouTube](https://www.youtube.com/yt/about/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
