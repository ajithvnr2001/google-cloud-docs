---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-periodic-data-alerts/
title: View data store sync activity and set up alerts \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:12.888608+00:00
---

# View data store sync activity and set up alerts  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-periodic-data-alerts/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  View data store sync activity and set up alerts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view the status, activity logs, and sync activity of a third-party data store, and how to configure alerts for the data store.

## View data store details and status

After connecting your third-party data source to Gemini Enterprise by creating a data store, you can view the status of the data store by going to the **Data stores** page and clicking the data store name.

![The data store console](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/data-store-console/data-store-console.png)The data store console 

### View data store states

The **Connector state** field shows the status of the data store. See the following table for information about possible data store states.

State | Description  
---|---  
**Creating** | The data store is being created.  
**Creating (with errors)** | The data store is being created, but some errors have occurred.  
**Initialization failed** | The data store failed to be created.  
**[Action required]** | User actions that must be completed before the data store can start syncing data.  
**Updating** | The data store is being updated.  
**Failed during setup** | The data store encountered some errors during setup.  
**Failed during sync** | The data store encountered some errors during sync.  
**Authorization issues** | The data store failed with authorization related errors.  
**Quota issues** | The data store failed with quota related errors.  
**Failed** | The data sync run failed.  
**Running** | The data sync run is in progress.  
**Running (with errors)** | The data sync run is in progress, but some errors have occurred (possibly including fatal errors).  
**Warning** | The data store's latest sync run encountered fatal errors.  
**Active** | The data store was successfully created and is awaiting the next sync run. The last sync run encountered no fatal errors.  
**Paused** | The data sync run is paused.  
**Paused (with errors)** | The data sync run is paused, and some errors have occurred.  
  
### View data store sync activity

In the **Data Ingestion Activity** tab, you can see the data store's latest sync activity. Each sync run is listed, with the following fields:

  * **Connector run** : the date and time of the sync run.

  * **Status** : the status of the sync run.

  * **Last update time** : the date and time of the last change in the sync run.

  * **Sync type** : the type of sync (**Full** or **Incremental**).

  * **Items succeeded (%)** : the percentage of entities that were successfully synced.

  * **Items failed** : the number of entities that failed to sync.

  * **Details** : More information about the sync run. If there are more details available, you can click to expand the field and view them.




For information about the possible values of the **Status** field for a sync run, see the following table.

Status | Description  
---|---  
**Running** | The data sync is ongoing. At least one entity is still being synced.  
**Running with errors** | The data sync is ongoing. At least one entity is still being synced. Sync for some entities failed, or encountered nonfatal errors.  
**Succeeded** | The data sync has completed successfully. All of the entities were successfully synced.  
**Succeeded with errors** | The data sync has completed, but some entity sync runs failed or encountered nonfatal errors.  
**Failed** | All entities failed to sync.  
**Cancelled** | The data sync was scheduled, but syncs for all entities have been cancelled.  
**Overrun** | The data sync is ongoing, but has taken longer than expected and continues to run at the time that the next run is scheduled.  
  
For each sync run in the table, you can expand the row by clicking the date and time under **Connector run**. This shows you the details of each specific entity type included in the sync run. For more information, see the following table.

Field | Description  
---|---  
**Status** | 

  * **Succeeded:** The entity sync completed, and at least 99% of the documents are successfully indexed.
  * **Succeeded with errors:** The entity sync completed, but less than 99% of the documents are successfully indexed.
  * **Failed:** The entity sync terminated with fatal failures.

  
**Last update time** | The date and time of the last change in the sync run for this entity.  
**Sync type** | The type of sync (**Full** or **Incremental**).  
**Items Succeeded (%)** | The percentage of items (documents) successfully indexed. This percentage may change over time as the sync run progresses.  
**Items Failed** | The number of items (documents) that failed to index.  
**Details / View Details** | This button opens up a side-panel that shows a link to view logs for this entity sync run, as well as more details about the error.  
  
## View data store activity logs

To view activity logs for the data store, click **View logs** in the data store details page.

![View logs for all data store sync activity](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/data-store-console/activity-logs.png)View logs for all data store sync activity 

This shows you all logs related to this data store, across all sync runs, including all entity sync runs.

## Set up alerts for sync events

After connecting your third-party data source to Gemini Enterprise by creating a data store, you can enable alerts for predefined tasks. Alert notifications can be emailed to selected recipients.

**Note:** You can't configure alerts for a federated search connector.

### Before you begin

To enable alerts for a data store, you need to have the following permissions or role assigned to you:

**Permissions** | 

  * `discoveryengine.googleapis.com/alertPolicies.get`
  * `discoveryengine.googleapis.com/dataConnectors.update`

  
---|---  
**Predefined role** | [`Discovery Engine User`](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.user)  
  
### Enable alerts for a data source

To enable alerts for a specific data source:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. In the navigation menu, click **Data stores**.

  3. Click the name of the data store that you want the alerts configured.

  4. On the data store details page, ensure that you have enabled the **Full sync frequency** and the **Incremental sync frequency**.

  5. Click the **Alerts** tab and then click **Edit**.

  6. In the **Configure alerts** section, click the alert toggle to the on position. The following alerts are supported:

Alert Type | Description  
---|---  
Status: Failed/Cancelled |  The data store failed to connect or retrieve data from your data source, or the sync run was cancelled.   
Status: Succeeded |  The data store successfully connected and retrieved data from your data source.   
  7. In the **Configure recipients** section, add the email addresses that must receive notifications for the enabled alerts.

**Note:** Alert recipients are configured at the Google Cloud project level. If you add an email address to receive alert notifications for one data store, that email address also receives the alert notifications from the other data stores in your project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
