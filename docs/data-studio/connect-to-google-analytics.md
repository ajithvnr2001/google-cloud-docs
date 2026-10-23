---
url: https://docs.cloud.google.com/data-studio/connect-to-google-analytics/
title: Connect to Google Analytics \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:37.261461+00:00
---

# Connect to Google Analytics  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-google-analytics/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to Google Analytics Stay organized with collections  Save and categorize content based on your preferences. 

You can connect your Google Analytics 4 properties to Data Studio to analyze data from your website, app, or devices. Use Data Studio to build custom reports and dashboards and then share them with your team or other users.

## How to connect to Google Analytics 4

You must have at least **Read & Analyze** permission to the Google Analytics 4 property or Universal Analytics view to which you connect. To connect to Google Analytics 4, follow these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. On the Data Studio home page, in the top left, click add **Create** , and then select **Data Source**.
  3. Select the **Google Analytics** connector.
  4. If prompted to grant Data Studio access to your account, click **AUTHORIZE**.
  5. Select an account.
  6. Select a property.
  7. In the upper right, click **CONNECT**. 
     1. The data source fields panel appears.
     2. The data source is now connected to your [dataset](https://docs.cloud.google.com/data-studio/dataset).



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

## What data is available from Google Analytics?

You can use Data Studio to visualize any of the fields that are available in the [Google Analytics Data API (GA4)](https://developers.google.com/analytics/devguides/reporting/data/v1), including any custom fields that are defined for the property.

**Note:** Data Studio will match the data, but not the explorations, in Google Analytics reporting. Learn more about [data differences between reports and explorations](https://support.google.com/analytics/answer/9371379) in Google Analytics.

## Limits of the Google Analytics connector

Data Studio reports that connect to Google Analytics 4 data are subject to [Google Analytics Data API (GA4) quotas](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas). Reports that exceed these quotas may display an error message. Refer to the [Troubleshooting guide](https://docs.cloud.google.com/data-studio/troubleshooting-guide) documentation page for more information.

Google Analytics 4 segments and comparisons are not available using the Google Analytics connector.

When a table is filtered by a calculated field, the Google Analytics connector doesn't support the display of totals in the table's **Summary row** , if present. When a table is the target of a filter of any type, and the filter condition is based on a calculated field, a custom group, or a bin, the grand total displays `null`.

### Inflated session counts in Stacked Bar charts

When using Google Analytics 4 (GA4) as a data source, you may encounter inflated or "double-counted" session metrics in Stacked Bar charts under specific configurations.

#### The issue

This occurs when a report includes complex filters or segments in combination with specific date dimensions—most commonly ISO Year ISO Week.

Because of how the GA4 API handles "filter pushdown" (the process of sending report filters to be processed by the GA4 engine), certain dimensions can prevent the API from correctly deduplicating sessions that span across the boundaries of those dimensions. In a Stacked Bar chart, Data Studio may sum these individual session fragments, leading to a total that exceeds the actual session count found in the Google Analytics interface.

#### Recommended workarounds

To ensure accurate session counts, consider the following alternatives:

  * **Use BigQuery as an intermediary** : Recreate your complex query as a standard View or Materialized View directly within BigQuery, then connect Data Studio to that View. This allows BigQuery to handle the deduplication logic before the data reaches the chart.

  * **Use non-ISO date dimensions** : If your reporting requirements allow, switch to standard date dimensions (e.g., Date or Month) which often trigger more reliable deduplication using the native connector.

  * **Avoid complex filter pushdown** : If possible, simplify the filter logic applied to the specific chart or move the filtering logic to a Blended Data source to force re-aggregation within Data Studio.




## Related resources

  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)
  * [User permissions in Google Analytics](https://support.google.com/analytics/answer/2884495)
  * [Dimensions & Metrics Explorer](https://developers.google.com/analytics/devguides/reporting/core/dimsmets)
  * [Measure Data Studio report usage with Google Analytics](https://docs.cloud.google.com/data-studio/measure-report-usage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
