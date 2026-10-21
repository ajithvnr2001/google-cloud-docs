---
url: https://docs.cloud.google.com/data-studio/manage-auto-refresh-for-a-report/
title: Manage auto refresh for a report \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:25.753562+00:00
---

# Manage auto refresh for a report  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/manage-auto-refresh-for-a-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Manage auto refresh for a report Stay organized with collections  Save and categorize content based on your preferences. 

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

You can configure a report to automatically refresh its data while it is open. This feature is useful for reports that may be displayed on a monitor for extended periods of time.

## Prerequisites

To configure auto refresh, the following prerequisites must be met:

  * Your organization must have Data Studio Pro, and the report must be a [Pro report](https://docs.cloud.google.com/data-studio/upgrade-looker-studio-content-to-looker-studio-pro).
  * You must have edit permission on the report. This means that you either need to have created the report or the creator must have [shared the report](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports) with you with the edit [permission](https://docs.cloud.google.com/data-studio/roles-and-permissions).



When auto refresh is enabled, Data Studio periodically attempts to reload the data in your report. If data is older than the freshness setting of your data sources, Data Studio pulls new data from the underlying data connection.

## Set auto refresh for a report

Auto refresh is disabled by default on each report. To change the auto refresh settings for a report, follow these steps:

  1. Edit the report.
  2. In the **Resource** menu, click **Manage auto refresh settings**.
  3. Enable **Automatically refresh report data**.
  4. Select a refresh interval from the following options: 
     * Minutes: Every 5, 10, 15, or 30 minutes
     * Hourly: Every 1, 2, 4, 8, or 12 hours
     * Days: Once a day
  5. Click **Save**.



## How auto refresh works

While a report with auto refresh enabled is open, Data Studio Pro periodically attempts to reload the data. If your report data is older than the freshness setting of your data sources, Data Studio Pro pulls new data from the underlying data connection.

When auto refresh is enabled, Data Studio reloads data regardless of whether the report is in view mode or edit mode.

To see when each tile was last updated, view the report and hover over a tile. If the report's [**Header Visibility**](https://docs.cloud.google.com/data-studio/report-and-page-layout) is set to **Always show** or **Initially hidden** , Data Studio displays a timestamp that indicates when the tile was last updated by the auto refresh feature.

## Auto refresh and data freshness

The auto refresh settings on a report don't affect the [data freshness of a data source](https://docs.cloud.google.com/data-studio/manage-data-freshness). If a report triggers an auto refresh more frequently than the data source triggers a data refresh, the report returns [cached results](https://docs.cloud.google.com/data-studio/manage-data-freshness).

## Auto refresh and cache

An auto refresh does not trigger a cache refresh. However, if there is no cached data available for a query, auto refresh triggers a new query to run.

## Auto refresh and manual queries

If you manually run one or more queries on the report, Data Studio Pro continues to check the auto refresh interval and update the report accordingly.

## Auto refresh and presentation mode

If you are [presenting the report](https://docs.cloud.google.com/data-studio/present-a-report), Data Studio triggers both the presentation refresh and auto refresh according to their respective refresh intervals. Neither triggers a cache refresh.

## Related resources

  * [Manage data freshness](https://docs.cloud.google.com/data-studio/manage-data-freshness)

  * [Present a report](https://docs.cloud.google.com/data-studio/present-a-report)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
