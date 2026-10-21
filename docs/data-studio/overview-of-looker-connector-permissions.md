---
url: https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions/
title: Overview of Looker connector permissions \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:19.884356+00:00
---

# Overview of Looker connector permissions  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Overview of Looker connector permissions Stay organized with collections  Save and categorize content based on your preferences. 

In addition to the [Data Studio roles](https://docs.cloud.google.com/data-studio/roles-and-permissions) that may be required to perform tasks for a given data source, users need specific [Looker permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) to perform certain tasks that are related to the setup and use of the Looker connector. Because each Looker data source is essentially a Looker Explore, users must be granted these permissions on the Explore's underlying model. If a report contains multiple Looker data sources, users must have permissions for each underlying model to be able to [view or interact](https://docs.cloud.google.com/data-studio/view-and-interact-with-looker-data-on-a-report) with the report, and to perform the following tasks.

The following Looker permissions are granted in the Looker instance by a [Looker admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) but are also respected in Data Studio. Required Data Studio roles are managed in Data Studio.

Task | Minimum Looker permission for the LookML model | Minimum Data Studio role for the data source  
---|---|---  
Enable the Looker connector in the Looker instance | [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) role _The Admin role contains all permissions for all models on the Looker instance._ | Not applicable  
[Monitor Looker connector usage](https://docs.cloud.google.com/looker/docs/looker-studio-connector#monitoring_the_looker_connector_for_looker_studio) in the Looker instance with System Activity | [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) role | Not applicable  
Use the Looker connector to create a Looker data source in Data Studio | [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) | [Editor](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
View and edit the data source configuration in Data Studio | [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) | [Editor](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
View Looker Explore data in Data Studio | [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) | [Viewer](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
Refresh Looker data in Data Studio | [`clear_cache_refresh`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#clear_cache_refresh) | [Viewer](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
Export up to 5,000 rows of data from a [chart](https://docs.cloud.google.com/data-studio/export-data-from-a-chart) or from [blend results](https://docs.cloud.google.com/data-studio/how-blends-work) that are based on a Looker data source as a CSV file or to Microsoft Excel or Google Sheets | [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) _This permission is applicable to Data Studio Pro users who are using a Looker instance that is on Looker 25.4 or later as a data source._ | [Viewer](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
Export up to 15,000 rows of data from a [chart](https://docs.cloud.google.com/data-studio/export-data-from-a-chart) or from [blend results](https://docs.cloud.google.com/data-studio/how-blends-work) that are based on a Looker data source as a CSV file or to Microsoft Excel or Google Sheets | [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) _This permission is applicable to Data Studio Pro users who are using a Looker instance that is on Looker 25.4 or later as a data source._ | [Viewer](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
[Download reports](https://docs.cloud.google.com/data-studio/download-a-report-as-pdf) that use Looker data sources._Data downloads are limited to 5,000 rows._ | [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) or [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) _These permissions are applicable to Data Studio Pro users who are using a Looker instance that is on Looker 25.4 or later as a data source._ | [Viewer](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
[Schedule automated report delivery](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery) | [`schedule_look_emails`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_look_emails) _This permission is applicable to Data Studio Pro users who are using a Looker instance that is on Looker 25.4 or later as a data source._ | [Viewer with scheduling permissions](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
[Create, edit, pause, and delete alerts](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery) on a chart | [`create_alerts`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_alerts) _This permission is applicable to Data Studio Pro users who are using a Looker instance that is on Looker 25.4 or later as a data source._ | [Viewer](https://docs.cloud.google.com/data-studio/roles-and-permissions)  
Make API calls to [fetch a list of models and Explores](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/all_lookml_models) and to [fetch all metadata about a given Explore](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/LookmlModel/lookml_model_explore) for which they have data access — for use with [Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics) |  [`gemini_in_looker`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_in_looker) _This permission is available for Data Studio Pro users who are[Looker viewers](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles)._ | N/A  
[Create calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields) | [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields), [`create_table_calculations`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_table_calculations) | [Viewer](https://docs.cloud.google.com/data-studio/roles-and-permissions#viewer)  
  
## Related resources

  * [Looker permissions management](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles)
  * [Enable the Looker connector from a Looker instance](https://docs.cloud.google.com/looker/docs/bi-connectors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
