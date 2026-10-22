---
url: https://docs.cloud.google.com/data-studio/connect-to-search-console/
title: Connect to Search Console \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:31.648704+00:00
---

# Connect to Search Console  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-search-console/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Search Console Stay organized with collections  Save and categorize content based on your preferences. 

Google Search Console is a free service that helps you monitor and maintain your site's presence in Google Search results. The Data Studio Search Console connector helps you measure and analyze your site's performance on Google Search. You can extend those reports to include data from other sources, such as Google Analytics and Google Ads, to give you a more comprehensive view of your online presence.

## Watch a video

## How to connect to Search Console

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. On the Data Studio home page, in the top left, click add **Create** , and then select **Data Source**.

  3. Select the **Search Console** connector.

  4. If prompted, click **AUTHORIZE** to let Data Studio access your data.

**Tip:** You can [revoke this access](https://support.google.com/accounts/answer/3466521) at any time.
  5. In the _Sites_ panel, choose the site to connect.

**Important:** If you're not seeing a Search Console property that you own, make sure that you are signed in to Data Studio and Search Console with the same Google Account, and that you have at least view permission on the property.
  6. In the _Tables_ panel, choose either **Site Impression** or **URL Impression**.

  7. In the _Search Type_ panel, choose the default search type. See the Notes for more details.

  8. In the upper right, click **CONNECT**.

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

### Tables

Google Search Console uses two different aggregation methods for reporting on search performance: site impressions and URL impressions. The Search Console connector gives you access to both these methods however a single data source can only use one of these.

To see your site impressions and URL impressions side by side, create two data sources and add both to a single report. [Learn more about aggregating data by site versus by page](https://support.google.com/webmasters/answer/6155685#urlorsite).

### Search types

The Search Console connector supports the following search types:

Table  |  Search type   
---|---  
Site Impression  | 

  * web 
  * image 
  * video 
  * news 

  
URL Impression  | 

  * web 
  * image 
  * video 
  * news 
  * discover 
  * googleNews 

  
  
### Search type parameter

Data sources created with the Search Console connector provide you with a _Search type_ parameter. You can use this parameter to let report viewers change the search type. To do this:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the toolbar, click **Add a control** , then select the drop-down list control.
  3. In the **Properties** panel, select the **SETUP** tab.
  4. Click the **Control field** and select the **Search type** parameter.



### Query field

The _Query_ field lists the search terms used by your property's visitors. **To protect user privacy, Search Analytics doesn't show all data.** For example, Google might not show some queries that are made a small number of times, or those that contain personal or sensitive information. In this case, Data Studio may aggregate these queries into a single row with a blank value.

You can remove blank rows from your reports by using a [filter in your report](https://docs.cloud.google.com/data-studio/about-filter-properties) to exclude null values from the Query dimension:

![The Edit Filter dialog for the filter called Query filter with the setting Exclude Is Null values for a field called Query.](https://docs.cloud.google.com/static/data-studio/images/exclude-query-is-null-2018-03-28.png)

## Let viewers select their account

**Tip: Want to use this data source with different accounts?** Try adding a data control. 

Data controls give report viewers a way to select the account that provides the data that they want to see in a report. Data controls can eliminate the need to create separate reports and data sources for your various accounts. [Learn more about data controls](https://docs.cloud.google.com/data-studio/data-control).

## Get started quickly with a report template

Templates let you visualize your data in a finished report. Use these reports "as is" or customize them to fit your unique requirements. To find the latest template for Search Console, visit the [template gallery](https://datastudio.google.com/navigation/templates) and select the Search Console category.

## Related resources

  * [Learn more about Search Console](https://support.google.com/webmasters/answer/4559176).
  * [Learn more about Search Analytics](https://support.google.com/webmasters/answer/6155685).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
