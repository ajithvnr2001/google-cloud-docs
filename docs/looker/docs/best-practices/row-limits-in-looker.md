---
url: https://docs.cloud.google.com/looker/docs/best-practices/row-limits-in-looker/
title: What are all the row limits in Looker? \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:35.629180+00:00
---

# What are all the row limits in Looker?  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/row-limits-in-looker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  What are all the row limits in Looker? Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the different row limits that can be found across Looker. The rule of thumb is as follows: 

  * If results are being displayed in the browser, the default row limit is 5,000, or up to 50,000 if [a higher limit is specified by your admin](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits). 
  * If results are being exported from Looker, users can choose to export [all results](https://docs.cloud.google.com/looker/docs/downloading#all_results). However, the **All Results** option is unavailable if the query cannot [stream](https://docs.cloud.google.com/looker/docs/downloading#streaming_query_results). See the [Downloading content](https://docs.cloud.google.com/looker/docs/downloading) documentation page for an explanation of limitations on downloading with **All Results**. 
  * If results are being delivered as a Look or an Explore using the Looker Scheduler, users can choose to deliver [all results](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#limit). Starting in Looker 26.2, for deliveries of Looks and Explores, the **All Results** option is visible only to users who are assigned the [`schedule_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_without_limit) permission for the model that underlies the Look or Explore. See the [Delivering Looks and Explores](https://docs.cloud.google.com/looker/docs/delivering-looks-explores) documentation page for an explanation of limitations on delivering content with **All Results**. 



## Explores, Looks, dashboards, SQL Runner

Queries that are created with the Explore page will have a maximum limit of 5,000 rows. This limit also applies to Looks, dashboards, and queries that are created in SQL Runner. 

## Downloading

**Important** : Starting in Looker 26.4, table charts, scatterplot charts, and Google Maps charts that have [increased row limits](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits) are subject to the following limitations when you download, send, or schedule dashboards in PDF format: 

  * The query results for each table chart on a dashboard will display up to 50,000 rows, to a maximum total limit of 200,000 cells per dashboard. 
  * If the combined total of cells for table charts on a dashboard is greater than 200,000 cells, table chart results may be trimmed. If the maximum is reached, users will see a warning that will also be displayed at the bottom of the rendered PDF. 
  * Table charts on a dashboard PDF will display more rows than are displayed on the dashboard tile thumbnail only when the **Expand tables to show all rows** option is selected. 
  * Scatterplot charts and Google Maps charts support up to 50,000 data points (rows) in PDF downloads. The charts will render as the they appear in the tile thumbnail, [or fail](https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-chromium-renderer) based on standard renderer limitations. 



In most cases, it is possible to download the unlimited result set from an Explore, a Look, or a dashboard. It is only possible to download all results if the result set [streams](https://docs.cloud.google.com/looker/docs/downloading#streaming_query_results) and if the user downloading has the [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) permission.

If these conditions are not met, then a [**custom limit**](https://docs.cloud.google.com/looker/docs/downloading#limits) can be set in the download modal instead. Users with the [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) permission are limited to 5,000 rows (or up to 50,000 rows if a higher limit is configured in [**Visualization limits**](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits)) and 50 columns. This custom limit has a default maximum of 100,000 rows for other users, which has sometimes been misunderstood as a per-user or per-role limit.

Looker does not natively support setting granular, custom row download limits (such as setting a limit of 100,000 rows) on a per-user or per-role basis. Any changes to custom download row limits are applied as an instance-wide setting that affects all users.

As a workaround to enforce a custom row download cap instance-wide, you can modify the `max-unstreamed-limit` startup flag on your Looker instance. Setting this startup flag to 100,000 restricts all users on the instance to a maximum of exactly 100,000 rows.

**Note:** Downloading specifically for dashboards is discussed in greater detail on the **Downloading content** documentation page in the [Downloading data from a dashboard](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_a_dashboard) section. 

## Delivering content

**Important** : Starting in Looker 26.4, table charts, scatterplot charts, and Google Maps charts that have [increased row limits](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#visualization-limits) are subject to the following limitations when you download, send, or schedule dashboards in PDF format: 

  * The query results for each table chart on a dashboard will display up to 50,000 rows, to a maximum total limit of 200,000 cells per dashboard. 
  * If the combined total of cells for table charts on a dashboard is greater than 200,000 cells, table chart results may be trimmed. If the maximum is reached, users will see a warning that will also be displayed at the bottom of the rendered PDF. 
  * Table charts on a dashboard PDF will display more rows than are displayed on the dashboard tile thumbnail only when the **Expand tables to show all rows** option is selected. 
  * Scatterplot charts and Google Maps charts support up to 50,000 data points (rows) in PDF downloads. The charts will render as the they appear in the tile thumbnail, [or fail](https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-chromium-renderer) based on standard renderer limitations. 



[Schedules](https://docs.cloud.google.com/looker/docs/scheduling-email) to email can send up to 20 MB of data (for emails with inline content) or 15 MB of data (for emails with attachments), as long as the results stream. All emails with the **All Results** option applied are subject to the 20 MB or 15 MB size limits. The **All Results** option is visible only to users who are assigned the [`schedule_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_without_limit) permission for the content's underlying model. 

Schedules that are delivered with a webhook or to an Amazon S3 bucket or SFTP server can send an unlimited result set as long as the data can be delivered as it's returned, rather than all at once. The **All Results** option is visible only to users who are assigned the [`schedule_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_without_limit) permission for the content's underlying model. 

## File format matters

When you are downloading or delivering content, PDF and PNG file formats will maintain the browser row limit of 5,000. The **All Results** option is typically only available for Markdown, Text, CSV, JSON - Simple, XLSX, or HTML formats for scheduling, sending, and downloading. The data formats available for sending and scheduling data depend on the destination and type of content. The [Using the Looker Scheduler to deliver content](https://docs.cloud.google.com/looker/docs/scheduling) documentation page provides links to documentation about delivering each type of Looker content. The [Downloading content](https://docs.cloud.google.com/looker/docs/downloading#file_formats) documentation page provides more information about file format options for downloading. 

## API

[API calls](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) are subject to the row limits of the context they are called in. API calls based on an Explore, a Look, or a dashboard are subject to the 5,000 row limit, while certain download and schedule file formats can be unlimited. 

To download unlimited results with the API, use the appropriate Run call (such as [Run Inline Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/run_inline_query) or [Run Look](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Look/run_look)) with the `limit` parameter set to `-1` (negative one). `-1` is the number that Looker uses to represent unlimited results.

Check the limits referenced in these sections as appropriate to the type of API call you're using.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
