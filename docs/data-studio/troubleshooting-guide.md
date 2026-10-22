---
url: https://docs.cloud.google.com/data-studio/troubleshooting-guide/
title: Troubleshoot errors in Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:51.868159+00:00
---

# Troubleshoot errors in Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/troubleshooting-guide/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Troubleshoot errors in Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

Data Studio sometimes displays errors during reporting. These errors can occur for many reasons, including broken data sources, improper chart settings, or exceeded platform quotas. Understanding these common errors helps you troubleshoot your reports.

Follow the steps in this guide to investigate and fix issues across your charts, reports, and data sources.

* * *

## Basic hygiene steps

Temporary network issues or server glitches can sometimes cause unexpected problems in Data Studio. Try these quick checks before you spend time troubleshooting complex settings. After trying each step, check whether your issue is resolved.

### Possible symptoms and error messages

Error messages are shown in code font:

  * Unresponsive pages
  * `System error`
  * `Data Studio is not available`



####  Steps to resolve 

  * Refresh your browser window.
  * Clear your browser cache and cookies.
  * Restart your web browser.
  * Try using a different web browser.
  * Restart your computer.
  * Try using a different device if one is available.



If these steps don't solve the issue, wait a few minutes and try again. If the problem persists, check whether other users are experiencing similar issues on the [Data Studio community forum](https://discuss.google.dev/c/data-studio/246).

* * *

## Access issues

If you use Google Workspace or Cloud Identity, your organization administrator must enable Data Studio before you can access it. Similarly, when you share reports with users in another organization, their administrator must enable Data Studio for their accounts.

### Service disabled for your account

`We are sorry, but you do not have access to this service. Please contact your Organization Administrator for access.`

####  Steps to resolve 

Ask your organization administrator to enable Data Studio for your organization ([Learn more about enterprise features](https://docs.cloud.google.com/data-studio/enterprise-administrator-feature-overview)).

### OAuth authorization and consent prompts

When you sign in or use Data Studio features for the first time, you might see an OAuth consent dialog requesting access to your Google Account. Granting this consent authorizes Data Studio to communicate securely with underlying data APIs on your behalf.

####  Steps to resolve 

Click **Continue** (or **Allow**) on the dialog to grant the required permissions. You only need to grant consent once unless you explicitly [revoke access](https://docs.cloud.google.com/data-studio/remove-or-reconnect-access-to-your-google-account).

### Service disabled for a report recipient

When attempting to share a Data Studio report with another user, you might receive the following error message:

`You do not have access to Data Studio. To enable this service, please log in to the Admin console.`

**Cause:** This error message indicates that the recipient does not have the Data Studio service enabled in their Google Workspace or Cloud Identity account. Their organization administrator has disabled or restricted Data Studio for their group.

####  Steps to resolve 

The recipient must contact their organization administrator to request access. You cannot fix this issue as the sender because access depends on the recipient's domain policies.

* * *

## Data source and connection issues

Data connection errors occur for several reasons, including missing [data credentials](https://docs.cloud.google.com/data-studio/data-credentials), broken configurations, deleted data sources, or revoked access permissions. Follow these steps to resolve problems connecting to your data.

### Connector-specific troubleshooting and errors

If you encounter errors on a specific data connector (such as query timeouts, ambiguous join fields, or dataset limits), check the troubleshooting guide for that connector:

  * **BigQuery connector:** See [Troubleshoot BigQuery connector errors and limitations](https://docs.cloud.google.com/data-studio/bigquery-connector-troubleshooting) to fix `Field is ambiguous` joins, `HTTP 504 Gateway timeout` errors, dataset table limits (`>5,000 tables`), `CONDITION_NOT_MET` encryption (CMEK) errors, `TIME` conversions, and VPC Service Controls (`VPC-SC`) off-VPN errors.
  * **Looker connector:** See [Troubleshoot errors from the Looker connector](https://docs.cloud.google.com/data-studio/looker-connector-troubleshooting) to fix Looker-specific connection and Explore failures.



### Possible error messages

Error messages are shown in code font:

  * `Missing data source`
  * `Data set configuration error`
  * `No data set access`
  * `Data source not attached`
  * `Data source needs to be added`
  * `The underlying data has changed`
  * `Database connection error`



####  Steps to resolve 

  * Edit the broken component and [add the correct data source](https://docs.cloud.google.com/data-studio/replace-the-data-source-for-a-component-page-or-report).
  * [Refresh the data source fields](https://docs.cloud.google.com/data-studio/refresh-data-source-fields).
  * [Reconnect the data source](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection).
  * Remove the broken data source from the report, and then add it back.
  * Create a new data source to verify whether a clean connection works.
  * [Revoke and restore](https://docs.cloud.google.com/data-studio/remove-or-reconnect-access-to-your-google-account) Data Studio's access to your Google Account.



### Scheduled email or alert failures behind VPC Service Controls

When your data source is protected by a VPC Service Controls (`VPC-SC`) perimeter using IP-based access levels, automated background features might fail.

Possible symptoms and error messages include:

  * Scheduled email deliveries contain only a report link and miss the report contents or PDF attachments.
  * Chart alerts fail to trigger or stop sending notifications.
  * `Organization VPC Service Controls prohibit access to data set used by this component`
  * `Service Control Failure`



####  Steps to resolve 

Because automated background tasks don't run from an end-user IP address, VPC Service Controls blocks the request. To resolve these errors, configure your data source to use **service account credentials** or create an access level that allows background requests ([Learn more](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery#limitations-of-vpc-sc)).

* * *

## Configuration and chart-level issues

Charts with incomplete settings or incompatible fields display errors. You might also encounter formula syntax errors, such as missing parentheses, incorrect function names, or improper operators. Data Studio highlights the broken section of the formula.

### Possible error messages

Error messages are shown in code font:

  * `System error`
  * `Chart configuration incomplete`
  * `Invalid combination of metrics and dimensions`
  * `Get report failed`



####  Steps to resolve 

  * [Fix or remove invalid calculated fields](https://docs.cloud.google.com/data-studio/add-edit-and-troubleshoot-calculated-fields).
  * Select different dimensions or metrics for the chart.
  * [Refresh the data source fields](https://docs.cloud.google.com/data-studio/refresh-data-source-fields).
  * [Reconnect the data source](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection).
  * [Verify that the report is shared with you](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports), or refresh your browser and reload the report.



**About the`Invalid combination of metrics and dimensions` error**

**Cause:** This error occurs when your chart combines fields in a way that the underlying data source does not support. Backend systems like Google Analytics and Google Ads store data in fixed schemas that allow only specific dimensions and metrics to be queried together.

**Tip:** For Google Analytics, use the [Dimensions and Metrics Explorer](https://ga-dev-tools.web.app/ga4/dimensions-metrics-explorer/) to check compatible combinations before adding fields to your chart.

* * *

## User interface and functionality issues

If Data Studio stops working appropriately or stops responding, browser extensions or add-ons might be causing the conflict.

### Possible symptoms and error messages

Error messages are shown in code font:

  * Features not working
  * Missing UI elements
  * Product stops responding
  * `Sorry! We can't save this report right now.`



####  Steps to resolve 

  * Try the basic hygiene steps described right across the beginning of this page.
  * Try using a different web browser.
  * Turn off third-party browser extensions and add-ons.



If turning off your extensions fixes the problem, turn them back on one at a time to identify the conflicting extension. Consider sharing your finding on the [Looker Forums](https://www.googlecloudcommunity.com/gc/Looker-Forums/ct-p/looker-forums).

* * *

## Blending issues

Most blending errors fall into three categories: misconfigured joins, missing data sources, and unexpected blend results.

### Misconfigured join errors

Error messages are shown in code font:

  * `One or more join configurations is incomplete.`
  * `One or more join configurations is missing a join condition.`
  * `Join key incomplete. Each selected data source must specify a join key field for every join key.`
  * A pink `Missing` field appears inside the join condition.



####  Steps to resolve 

  * [Edit the join configuration](https://docs.cloud.google.com/data-studio/create-edit-and-manage-blends).
  * Verify that every join in your blend has a valid condition and operator. Cross-joins (`CROSS JOIN`) don't use join conditions.
  * For missing fields, either remove the broken field or verify that both joined tables share corresponding key columns.



### Missing or incorrect data source connection

`One or more tables is missing its data source.`

####  Steps to resolve 

[Reconnect any tables](https://docs.cloud.google.com/data-studio/create-edit-and-manage-blends#reconnect_a_table) that are missing their data source inside the blend configuration.

* * *

## Google Analytics 4 quotas exceeded

Reports that connect to Google Analytics 4 (`GA4`) data are subject to [GA4 Data API quotas](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas). You can monitor your report's quota token usage by opening the **Google Analytics Token Usage** dialog.

### View token usage

  1. Edit your Data Studio report.
  2. To check your report's overall token usage, right-click the report canvas and select **Google Analytics token usage**.
  3. To check the token usage for a specific chart, right-click the chart and select **Google Analytics token usage**.



The overall usage summary shows:

![The Google Analytics Token Usage dialog, which shows the number of quota tokens used by the entire report](https://docs.cloud.google.com/static/data-studio/images/ga4tokenusagedialog2022-12-20.png)

  * The quota tokens consumed across the entire report or current page during your session.
  * The quota tokens remaining before you reach your API limit.
  * The quota tokens consumed by each chart, listed from highest to lowest.



The chart-level usage summary shows:

![The Google Analytics Token Usage Details dialog, which shows the number of quota tokens used by each chart](https://docs.cloud.google.com/static/data-studio/images/ga4tokenusagedetailsdialog2022-12-20.png)

  * The quota tokens consumed by each query request.
  * The exact completion timestamp for the query.
  * Whether the chart loaded directly from GA4 or from memory cache. A green checkmark indicates that the chart loaded from memory without consuming tokens. A red X indicates that the chart queried GA4 directly ([Learn more about data freshness](https://docs.cloud.google.com/data-studio/manage-data-freshness)).



### Quota exceeded error messages

Reports that exceed GA4 quotas display one of the following errors:

  * `Exhausted concurrent requests quota. Please send fewer requests concurrently.`
  * `This property has issued too many requests in the last day.`
  * `Too many requests using this Google Analytics property have encountered errors in the last hour.`
  * `This property has issued too many requests in the last hour.`
  * `This property is denied access to Google Analytics.`
  * `This property has issued too many potentially thresholded requests in the last hour.`
  * `This project/property has issued too many requests in the last hour.`



####  Steps to resolve 

If you exceed GA4 quota limits, use the following techniques to query less data from GA4 and rely more on Data Studio's cache:

  * Switch your data source to [owner's credentials](https://docs.cloud.google.com/data-studio/data-credentials). Owner credentials allow multiple report viewers to share the same cached data without consuming new quota tokens.
  * Consolidate duplicate GA4 data sources into a single [reusable data source](https://docs.cloud.google.com/data-studio/embedded-data-sources). Sharing one data source increases memory caching across charts.
  * Reduce visitor traffic by sharing the report with fewer people or removing embedded reports from high-traffic webpages.
  * Reduce the number of charts across your report pages.
  * [Extract your GA4 data](https://docs.cloud.google.com/data-studio/extract-data-for-faster-performance) into a static report snapshot. You must wait up to 24 hours for exceeded quotas to reset before running the extraction.
  * [Export your GA4 data to BigQuery](https://support.google.com/analytics/answer/9823238?sjid=8474625821442068377-NC), and connect to the exported dataset using the [BigQuery connector](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery).
  * [Upgrade to Analytics 360](https://marketingplatform.google.com/about/analytics-360/) for higher API limits.
  * Consider using a [partner connector](https://datastudio.google.com/data).



* * *

## Strategies for troubleshooting complex issues

To diagnose complex issues in Data Studio, first **identify where the problem occurs**. Ask yourself:

  * Is the issue happening across all your reports or only one?
  * Does it affect every chart type or only a specific component?
  * Does it happen in every web browser or only one specific version?



**See also:** [What you need to use Data Studio](https://docs.cloud.google.com/data-studio/what-you-need)

Next, **reduce your variables**. Isolate the problem to the fewest possible factors by simplifying your report or data:

  * **Isolate data issues:** If you suspect bad data, apply a filter to hide half of your rows. If the error disappears, the broken data is in the hidden half. If the error remains, the broken data is in the visible half. Continue dividing the rows until you locate the bad record.
  * **Isolate chart issues:** Create a version of the broken chart containing only one dimension and metric. Gradually add fields and styling options back one by one until the error reappears.



* * *

## Report a problem to Google

If you cannot resolve the problem after trying these steps, [report it to Google](https://docs.cloud.google.com/data-studio/report-a-problem). Be prepared to provide:

  * A complete description of the problem
  * Steps to reproduce the failure
  * Any error messages or error IDs that appear
  * A link to a test report that demonstrates the problem



> **About error IDs**
> 
> If you see an 8-character alphanumeric error ID (`Error ID: a1b2c3d4`), always include it in your bug report. Error IDs help Google engineers locate the exact failure trace in system logs. Error IDs are generated dynamically for every single failure event, so a new ID is created each time the error occurs.

> **About test reports**
> 
> When you share a test report with Google support, keep the report as simple as possible. Make a copy of your original report and delete all unrelated pages, charts, and filters that aren't needed to reproduce the bug.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
