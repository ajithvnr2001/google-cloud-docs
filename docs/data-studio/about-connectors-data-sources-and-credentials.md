---
url: https://docs.cloud.google.com/data-studio/about-connectors-data-sources-and-credentials/
title: About connectors, data sources, and credentials \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:42.495952+00:00
---

# About connectors, data sources, and credentials  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/about-connectors-data-sources-and-credentials/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  About connectors, data sources, and credentials Stay organized with collections  Save and categorize content based on your preferences. 

When you connect external data to Data Studio, you manage [connectors](https://docs.cloud.google.com/data-studio/connector), [data sources](https://docs.cloud.google.com/data-studio/data-source), and [credentials](https://docs.cloud.google.com/data-studio/data-credentials). Understanding how these three components work together helps you customize data presentation and securely share reports with your team.

## About connectors

Connectors link your underlying data to a Data Studio data source. Connectors are specific to the kind of data that you want to visualize in Data Studio. For example, Google has built connectors to [various Google and non-Google products](https://docs.cloud.google.com/data-studio/available-connectors), including BigQuery, Google Sheets, Google Analytics, and MySQL databases. You can also use [connectors built by 3rd party developers](https://docs.cloud.google.com/data-studio/about-community-connectors) to visualize data from a wide variety of non-Google products, such as Bing, Facebook Ads, and Salesforce.

[Connect to data now in Data Studio](https://datastudio.google.com/data)

## About data sources

Data sources can be either _embedded_ or _reusable._ Reports can include both embedded and reusable data sources.

**Data sources that you create while editing a report are embedded** in the report. To edit an embedded data source, you do so within that report. Embedded data sources make collaborating on reports and data sources easier. Anyone who can edit the report can also edit the data source as well as modify its connection. When you share or copy the report, any embedded data sources are shared or copied as well.

**Data sources that you create from the home page are reusable**. You can reuse these data sources in different reports. Reusable data sources let you create and share a consistent data model across your organization. Only people with whom you share the reusable data source can edit it. Only the owner of the data source's credentials can modify the connection.

[Learn more about the features of embedded vs. reusable data sources](https://docs.cloud.google.com/data-studio/embedded-data-sources).

## About credentials

A data source's credentials determine who can access the data provided by that data source:

  * **Owner's credentials** uses the credentials of the data source owner to authorize access to the dataset. This option lets you share reports that use this data source without requiring report viewers to have their own access to the underlying dataset.

**Important:** Before sharing a report or data source that uses Owner's credentials, be sure that you trust the person or persons with whom you share them.
  * **Viewer's credentials** require anyone who attempts to view the data that is provided by this data source to have their own access to the dataset.

  * **Service account credentials** use a special type of Google account that is intended to represent a non-human user that can authenticate and be authorized to access your data.


**Note:** Cloud Identity and Google Workspace administrators can change the default credentials or disable the Owner's credentials option.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
