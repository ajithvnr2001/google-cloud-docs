---
url: https://docs.cloud.google.com/looker/docs/data-studio-connector/
title: Connecting to Data Studio \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:22.293962+00:00
---

# Connecting to Data Studio  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/data-studio-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Connecting to Data Studio Stay organized with collections  Save and categorize content based on your preferences. 

With the Looker connector in Data Studio, you can create a [data source](https://docs.cloud.google.com/looker/docs/studio/about-data-sources) that lets you view and analyze data from a Looker Explore within Data Studio.

**Note:** Some [limitations of the Looker connector](https://docs.cloud.google.com/looker/docs/studio/limits-of-the-looker-connector#limits-looker-connector) may determine which Looker instances or models are ideal for connecting to Data Studio.

Looker users who are less familiar with using Data Studio may want to refer to the [Looker and Data Studio shared terms and concepts](https://docs.cloud.google.com/looker/docs/looker-and-studio-shared-terms-glossary) documentation page for more information about the nuances between similar terms and concepts in Looker and Data Studio.

## Before you begin

A Looker data source in Data Studio must be an Explore from a Looker instance that meets the requirements, which are listed on the [Overview of Looker connector requirements, limits, and feature support](https://docs.cloud.google.com/looker/docs/studio/limits-of-the-looker-connector#looker-instance-requirements) documentation page.

Only a Looker [admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) can enable the Looker connector for a Looker instance.

To interact with a Looker data source in Data Studio, users must meet the permissions and roles requirements listed on the [Overview of Looker connector permissions](https://docs.cloud.google.com/looker/docs/studio/overview-of-looker-connector-permissions) documentation page.

## Enabling and using the connector

To enable the connector, follow these steps:

  1. Navigate to the **BI Connectors** page in the **Platform** section of the Looker **Admin** panel.
  2. Either enable the **All Looker BI Connectors** setting or the **Looker Studio** setting. In Looker (Google Cloud core) instances, these settings are enabled by default.



## Disabling the connector

To disable the connector, follow these steps:

  1. Navigate to the **BI Connectors** page in the **Platform** section of the Looker **Admin** panel.
  2. Either disable the **All Looker BI Connectors** setting or the **Looker Studio** setting.



## Monitoring the Looker connector for Data Studio

A Looker admin can view Data Studio usage by using the **Query API Client Properties** group of fields in the [System Activity History Explore](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#history). An entry is created in the **History** Explore every time a new query is run.

In the **Query API Client Properties** dimension group under the **History** view, the following fields are relevant to Data Studio:

  * **API Client Name** — This field uses `Looker Studio` to identify Data Studio entries.
  * **Looker Studio Dashboard ID** — This field shows the ID of the Data Studio report that issued the query.
  * **Looker Studio Datasource ID** — This field shows the ID of the data source in Data Studio that is being queried.



The following example shows a System Activity URL that indicates Data Studio usage. Replace `<instance_name.looker.com>` with your instance URL.
    
    
    https://<instance_name.looker.com>/explore/system__activity/history?fields=query_api_client_context.name,query_api_client_context.ls_dashboard_id,query_api_client_context.ls_datasource_id,user.name,history.created_date,history.created_time_of_day&f[query_api_client_context.name]=looker%20studio&sorts=history.created_time_of_day+desc&limit=5000
    

## What's next

After you have enabled the connector, Explores in the Looker instance are available to use as data sources in Data Studio.

See the [Connect to Looker](https://docs.cloud.google.com/looker/docs/looker-studio-connector) documentation page for information about using the Looker connector to add a Looker Explore as a data source in a Data Studio report.

## Additional resources

  * [Admin settings – BI Connectors](https://docs.cloud.google.com/looker/docs/bi-connectors)
  * [Connect to Looker](https://docs.cloud.google.com/looker/docs/looker-studio-connector)
  * [Understand Looker Explore data on a Data Studio report](https://docs.cloud.google.com/looker/docs/studio/looker-explore-data-on-a-looker-studio-report)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
