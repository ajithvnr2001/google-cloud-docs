---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor/
title: Monitor overview \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:06.058153+00:00
---

# Monitor overview  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Monitor overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

From the **Monitor** tab, you can view and manage jobs (cancel, queued, or running jobs or change the job priority of a queued job) from backup/recovery appliances managed by the appliance management console. You can also view events, which are information, warning, and error notifications raised by an appliance.

Jobs are identified in the **Job View** as the following:

  * Canceled
  * Failed
  * Not run
  * Queued
  * Retry
  * Running (where the progress bar indicates the percent completion of the active job)
  * Succeeded
  * Succeeded With Warnings

You can filter jobs by name, status, start or end time, type, host, or application.




You can directly navigate from the **Jobs** list view in **Monitor** to:

  * The **Access** window in **App Manager** by clicking the link on an application listed in the **Application** columns.
  * The **Job Details** view in **Monitor** by clicking a status state link listed in the **Status** columns.
  * By default, the **Monitor** view lists the jobs that are running. You can clear this default filter to show all jobs that are being monitored.



## Monitor alerts in the appliance management console events monitor

You can learn about the context of an event in the **Events Monitor**. Events are information, warning, or error notifications raised by a backup/recovery appliance. You can view events in the **Events Monitor** by doing the following:

  * Viewing events based on date or severity

  * Filtering events based on columns displayed in the **Events** window




Events are identified in the **Events** view as the following:

  * Info
  * Error
  * Warning



Right-click the event to select **View Details** of a selected event. To interpret the information in the event, see the next section.

### Interpret event details in the events monitor

This list has the event items and their meanings.

  * **ID** : Error sequence number.
  * **Event ID** : Event identifier. Events are listed in **Backup and DR Event IDs and Error Codes**.
  * **Appliance Name** : The name of the backup/recovery appliance that processed the job.
  * **Application Name** : The name of the application as it appears in the **App Manager**.
  * **Application Type** : The type of application in the **App Manager**.
  * **Component** : The component that reported the event. If the component type is SKY, this means the event was reported by the backup/recovery appliance named in the **Appliance Name** field.
  * **Job Name** : The job name as it appears in the **System Monitor Jobs** tab.
  * **Error Code** : Event identifier. Error codes are listed in **Backup and DR Event IDs and Error Codes**.
  * **Error Message** : Descriptive text, often with an additional error message appended to it.
  * **Requires Clearing** : Some events are clearable.
  * **Event Date** : A timestamp for the event.
  * **Object Type and Object ID** : The backup/recovery appliance component that encountered the event.
  * **Notification Type** : Severity: information, warning, or error.

**Note:** Not all fields are shown for all events. A field is shown only if it is relevant to the event.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
