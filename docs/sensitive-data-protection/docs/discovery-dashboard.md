---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-dashboard/
title: Visualize data profiles in the discovery dashboard \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:23.989466+00:00
---

# Visualize data profiles in the discovery dashboard  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-dashboard/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Visualize data profiles in the discovery dashboard Stay organized with collections  Save and categorize content based on your preferences. 

This section describes the information displayed in the discovery dashboard in the Google Cloud console.

For more information about the discovery service, see [Overview of sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles).

If you want to query data profiles and perform custom visualizations through Data Studio, see [Analyze data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles).

## Before you begin

Confirm that you have the IAM permissions that are required to work with scan configurations and data profiles at the [organization](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#permissions-to-view-configs-profiles-org) or [project](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#permissions-to-view-configs-profiles-project) level.

## Information in the discovery dashboard

The discovery dashboard provides a visual summary of data assets in the current resource (organization or project) that have been profiled by the Sensitive Data Protection discovery service. This dashboard provides the following information:

  * **Product coverage:** Shows which discovery types are enabled in the resource. For each enabled discovery type, this section shows high-level details, such as profile counts categorized by data sensitivity level. Each [data source that discovery supports](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#supported-resources) has a corresponding discovery type.
  * **Data profiles by geography:** Shows data profile counts in each region and multi-region where you have data that was profiled.
  * **Data profiles map:** Plots the locations of the profiled data on a map. Locations are represented by circles of varying sizes and colors. Locations that have more data profiles are represented by larger circles on the map. Locations with moderate-sensitivity or high-sensitivity data are red. Locations with only low-sensitivity data are green. To see more details about the data in a location, hold the pointer over the circle.
  * **BigQuery profiles with infoType:** If the BigQuery discovery type is enabled, this pie chart shows the infoTypes detected in your BigQuery data.
  * **Cloud SQL profiles with infoType:** If the Cloud SQL discovery type is enabled, this pie chart shows the infoTypes detected in your Cloud SQL data.
  * **Risk over time:** Plots the data risk levels of all profiled data in a time series chart. For more information about how data risk and sensitivity levels are calculated, see [Data risk and sensitivity levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).
  * **Sensitivity over time:** Plots the sensitivity levels of all profiled data in a time series chart.



## View the discovery dashboard

  1. In the Google Cloud console, go to the discovery dashboard.

[Go to Discovery dashboard](https://console.cloud.google.com/security/sensitive-data-protection/dataprofiles/dashboard;source=7)

  2. Select the organization or project that you want to view.




## What's next

  * Learn how to [analyze data profiles and visualize them in Data Studio](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
