---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances/
title: Manage plugin instances \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:47:18.740545+00:00
---

# Manage plugin instances  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage plugin instances Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to edit, sync, and delete plugin instances in API hub. For information about creating a plugin instance, see [Create plugin instances](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances). 

## Edit a plugin instance

You can edit an existing plugin instance to update its display name or modify its curation settings. To edit a plugin instance, perform the following steps: 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Click the **Plugins** tab and go to the **Manage instances** section to view the list of plugin instances in your project.
  4. For the plugin instance that you want to edit, click more_vert (Plugin instance actions) and then select **See details**. 
  5. In the **Plugin details** pane, you can: 
     * Edit the **Instance name** of the instance.
     * Modify the **Curation** logic.
  6. Click **Save** to apply your changes.



## Sync a plugin instance

**Note:** This functionality applies only to [pull-based](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-data-ingestion-methods) Apigee and hybrid plugin instances. For push-based plugins, data ingestion is automatically triggered by changes in the source. 

Pull-based plugin instances automatically ingest data from the connected source at a specified frequency. You can also manually trigger data ingestion for a pull-based plugin instance by performing the following steps: 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Click the **Plugins** tab and go to the **Manage instances** section to view the list of plugin instances in your project.
  4. For the plugin instance that you want to sync, click more_vert (Plugin instance actions) and then select **Run**. 

API hub starts to sync the plugin instance with the data source and the status is updated to **Running**. Once the sync is complete, the status is updated to **Active** as shown in the following image:

![Plugin instance status shown as Active in the Plugins tab.](https://docs.cloud.google.com/static/apigee/docs/apihub/images/plugin-active.png)![Plugin instance status shown as Active in the Plugins tab.](https://docs.cloud.google.com/static/apigee/docs/apihub/images/plugin-active.png)




## Delete a plugin instance

To delete a plugin instance, perform the following steps: **Warning:** Deleting a plugin instance also deletes all the associated data from API hub. 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Click the **Plugins** tab and go to the **Manage instances** section to view the list of plugin instances in your project.
  4. For the plugin instance that you want to delete, click more_vert (Plugin instance actions) and then select **Delete**.
  5. In the confirmation dialog, click **Delete** to confirm the deletion of the plugin instance. **Note:** The deletion operation time depends on the number of API assets associated with the plugin instance. For example, if the plugin instance is associated with 1000 APIs, it might take a litle longer to delete the plugin instance.



## What's next

  * Learn more about [plugins](https://docs.cloud.google.com/apigee/docs/apihub/plugins).
  * Learn more about [curations](https://docs.cloud.google.com/apigee/docs/apihub/curations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
