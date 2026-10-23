---
url: https://docs.cloud.google.com/looker/docs/system-activity-pages/
title: System Activity pages \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:51.470921+00:00
---

# System Activity pages  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/system-activity-pages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  System Activity pages Stay organized with collections  Save and categorize content based on your preferences. 

System Activity is a [LookML model](https://docs.cloud.google.com/looker/docs/model-and-view-files#model_files) that connects to Looker's underlying application database. System Activity [Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) and [dashboards](https://docs.cloud.google.com/looker/docs/system-activity-dashboards) that are built upon this model show information about your Looker instance, which includes the following:

  * All Looks and dashboards that are saved on your instance
  * User and historical query information
  * Instance performance statistics



Both the granularity and retention of System Activity data are subject to system constraints. System Activity is designed for collecting high-volume data, and aggregating it can be used to supplement your business logs.

> This data can be useful for supplementing monitoring and auditing activities, but is not intended to replace your current compliance strategy.
> 
> The text in filters run by users is accessible in System Activity and can be viewed by any user who has permission to view the System Activity model.
> 
> **Take action** : Modify who has view access to the System Activity models. Looker admins have access to System Activity by default. A Looker admin can grant access to System Activity to a non-admin user by giving the user the `see_system_activity` permission.

System Activity includes the following elements:

  * [System Activity dashboards](https://docs.cloud.google.com/looker/docs/system-activity-dashboards): Looker-created dashboards showing usage and performance information about the Looker instance. You can [download](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards#downloading_your_dashboard), [schedule](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards#scheduling_dashboard_data_delivery), [set alerts on](https://docs.cloud.google.com/looker/docs/alerts-overview), and [drill into](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling_down_into_the_data) metrics and elements just like on any other dashboard. Data in the System Activity dashboards is updated and cached every 12 hours.

  * [System Activity Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores): Using System Activity Explores, you can create your own Looks and dashboards to monitor and analyze your Looker instance. See the [System Activity Explores](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#system_activity_explores) page for a list of Explores and their cache rules.

  * [System Activity for Looker reports](https://docs.cloud.google.com/looker/docs/system-activity-for-looker-reports): If the [Looker reports](https://docs.cloud.google.com/looker/docs/enabling-looker-reports) feature is enabled on your Looker instance, System Activity dashboards and Explores include information about the [Looker reports](https://docs.cloud.google.com/looker/docs/move-share-copy-reports) that are saved on your Looker instance.

  * [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity): An optional analytical store that increases System Activity performance and storage limits. Elite System Activity is a paid feature on Looker (original), and is a standard feature on the [**Enterprise** and **Embed** editions](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences) of Looker (Google Cloud core).

  * [Read replica option](https://docs.cloud.google.com/looker/docs/system-activity-read-replica-db): For customer-hosted instances only, this method increases System Activity performance and provides longer System Activity data retention.

  * [Understanding PDT log actions](https://docs.cloud.google.com/looker/docs/pdt-log-actions): Use the **PDT Event Log** Explore to view and understand PDT log actions and their corresponding action data.

  * [Looker events](https://docs.cloud.google.com/looker/docs/events): The events that Looker generates and how to view them.




## System Activity in embedded environments

In an [embedded environment](https://docs.cloud.google.com/looker/docs/signed-embedding), strict restrictions prevent embedded users from rendering underlying system data, even if you grant the [`see_system_activity`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_system_activity) permission during single sign-on (SSO) authentication. Directly embedding System Activity dashboards for typical embedded users isn't supported.

To share System Activity insights with embedded users, you must extract the data and serve it from a customer-controlled model. You can use the following alternatives:

  * **Looker API scripting** : Use a [Looker API client SDK](https://docs.cloud.google.com/looker/docs/api-sdk), such as the Python SDK, to programmatically run queries against the `system__activity` model. Schedule a script to fetch daily results and write them directly to an external database.
  * **Scheduled deliveries** : Create a Look that's based on System Activity and [schedule a daily delivery](https://docs.cloud.google.com/looker/docs/delivering-looks-explores) as a CSV or JSON file to an [Amazon S3 bucket](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_amazon_s3) or [SFTP server](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_sftp). Then, use an extract, transform, and load (ETL) pipeline to ingest the data.
  * **Custom models and dashboards** : Extract the data by using Looker API scripting, scheduled deliveries, or [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity), and load it into your own database, such as BigQuery. Then, create a standard LookML model on top of that data and embed dashboards that you build from the new model.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
