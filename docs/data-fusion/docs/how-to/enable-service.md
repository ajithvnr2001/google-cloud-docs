---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/enable-service/
title: Enable or disable Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:55.703742+00:00
---

# Enable or disable Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/enable-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Enable or disable Cloud Data Fusion Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Data Fusion API lets you create and manage instances for building and running data integration pipelines in your Google Cloud project. You can enable the API to provision new resources, or disable it after deleting your instances to deactivate the service and help avoid additional charges. For more information about Service Usage on Google Cloud, see [Enabling and disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable).

## Before you begin

  * Before using Cloud Data Fusion, you must [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) and [enable billing](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account).
  * To enable and disable the Cloud Data Fusion API, you must have the administrator permission. For more information about roles and permissions, see [Access control](https://docs.cloud.google.com/data-fusion/docs/access-control).



## Enable Cloud Data Fusion

You can use an existing project with Cloud Data Fusion or create a new one. If you're using an existing project, you need to enable the Cloud Data Fusion API.

To create a project and enable the Cloud Data Fusion API:

  1. In the Google Cloud console, [select or create a project](https://console.cloud.google.com/cloud-resource-manager).
  2. Make sure that [billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/modify-project) for your project.
  3. Go to the [**Cloud Data Fusion API overview**](https://console.cloud.google.com/apis/library/datafusion.googleapis.com?q=datafusion) page.
  4. Click **Enable**.



## Disable Cloud Data Fusion

To avoid additional charges, complete the following steps for each instance before you disable the Cloud Data Fusion API.

When you disable the Cloud Data Fusion API, instances become unusable within an hour of service deactivation—unless you re-enable the API.  


If you re-enable the API, you're billed for the Service Usage that occurs while the Cloud Data Fusion service is deactivating.

  1. [Delete your instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).
  2. Wait until the following occurs: 
     1. All operations such as creating, updating, or deleting an instance have completed.
     2. All pipelines are no longer running.
  3. To disable the Cloud Data Fusion API: 
     1. In the Google Cloud console, select the project to disable the Cloud Data Fusion API in.
     2. Go to the [**Cloud Data FusionAPI overview**](https://console.cloud.google.com/apis/library/datafusion.googleapis.com?q=datafusion) page.
     3. Click **Manage**.
     4. Click **Disable API**.



## What's next

  * Learn more about [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview).
  * Learn how to [create a Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/create-instance).
  * Work through a [tutorial](https://docs.cloud.google.com/data-fusion/docs/tutorials/targeting-campaign-pipeline).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
