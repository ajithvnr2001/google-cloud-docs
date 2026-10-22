---
url: https://docs.cloud.google.com/data-studio/share-reports-created-with-the-linking-api/
title: Share reports created with the Data Studio Linking API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:37.583654+00:00
---

# Share reports created with the Data Studio Linking API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/share-reports-created-with-the-linking-api/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Share reports created with the Data Studio Linking API Stay organized with collections  Save and categorize content based on your preferences. 

Software developers can use the Data Studio Linking API to provide pre-configured reports that let you view and interact with your data in a seamless "1-click" experience.

When you share a report created using the Linking API, a **Review data access** dialog asks you to review the settings that control access to the report's data.

Learn more about the [Linking API](https://developers.google.com/looker-studio/integrate/linking-api).

## Background

When you connect external data to Data Studio, you manage [connectors](https://docs.cloud.google.com/data-studio/connector), [data sources](https://docs.cloud.google.com/data-studio/data-source), and [credentials](https://docs.cloud.google.com/data-studio/data-credentials). Understanding how these three components work together helps you customize data presentation and securely share reports with your team.

  * **Credentials** determine who can access the data provided by a data source.



Before you share a report that has been generated with the Linking API, you should make sure that the connection details look correct and that the credentials meet your needs for data security. The _Review data access_ dialog box helps you understand where the data in the report is coming from and who will be able to see it.

For each data source added to the report you can review the following:

## Connection details

This section describes the connection configuration. These details will differ depending on which connector was used to create the data source.

### What you should review

Be sure that the [data set](https://docs.cloud.google.com/data-studio/dataset), account details, and custom SQL (if applicable) are appropriate.

[See the connector documentation here](https://docs.cloud.google.com/data-studio/about-connectors-data-sources-and-credentials).

## Used in report

This section tells you how many charts use the data source. If a data source isn't used by any of the charts, you can safely remove it by clicking the "Manage data sources here" link in the dialog.

You can also edit and remove data sources after you save the report by using the **Resource > Manage added data sources** menu option.

## Credentials

The credentials for a data source determine who can access the data provided by that data source:

  * **Owner's credentials** uses the credentials of the data source owner to authorize access to the dataset. This option lets you share reports that use this data source without requiring report viewers to have their own access to the underlying dataset.

**Important:** Before sharing a report or data source that uses Owner's credentials, be sure that you trust the person or persons with whom you share them.
  * **Viewer's credentials** require anyone who attempts to view the data that is provided by this data source to have their own access to the dataset.

  * **Service account credentials** use a special type of Google account that is intended to represent a non-human user that can authenticate and be authorized to access your data.




### What you should review

Sharing a report that includes data sources that use Owner's credentials allows anyone to see your data. If the report you are sharing comes from a trusted source (for example, Google or a developer in your own organization), and the person you are sharing the report with is also known to you and trusted, then you can most likely accept the default configuration.

However, if either the developer of the report or the person you are sharing with is not known to or trusted by you, you may want to use Viewer's credentials for the added data sources. People who view the shared report must be able to provide their own credentials to see the data.

## Take action

To change the data source connection details or credentials, click edit **Edit**.

Learn how to:

  * [Edit the data source connection](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection)
  * [Change the data source credentials](https://docs.cloud.google.com/data-studio/data-credentials)



## Share the report

To share the report with the current data source configuration, go to the bottom of the dialog and then click **Continue**.

## Related resources

  * [Sharing, access permissions, and data credentials](https://docs.cloud.google.com/data-studio/roles-and-permissions)
  * [Data credentials](https://docs.cloud.google.com/data-studio/data-credentials)
  * [About data sources](https://docs.cloud.google.com/data-studio/about-data-sources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
