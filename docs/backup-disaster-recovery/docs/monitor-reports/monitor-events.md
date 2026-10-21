---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-events/
title: Monitor events \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:34:23.939824+00:00
---

# Monitor events  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Monitor events Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Use these instructions to view events:

  1. Click the **Monitor** menu tab and select **Events** from the drop-down menu. The **Events** page opens. A list of events appears in the table.
  2. To modify the display of the fields in the table, you can:

     * **Search By Keyword** : To display a specific subset of data in the **Events** table, use the **Search By Keyword** field to search across the data in the appliance management console database for a specific word or keyword and to display only that subset of data in the table. **Search By Keyword** is case insensitive.

       * Ended filter has single (radio) style buttons to select date range spanning a day, week for month.
     * **Adjust Fields** : To modify the fields that appear in the table, right-click within the table header row and click the checkboxes for the fields you want displayed (or those fields you don't want to view).

     * **Adjust Column Width** : To adjust the width of a table column to show more content in the table, drag the column divider in a column header to the left or right to resize the column width. Column dividers are marked by a pair of thin gray lines.

  3. To modify the number of rows displayed in a table page, you can select from the drop-down list at the bottom of the table. The choices include: 10, 25, 50, 100, or 500 rows per table page.

  4. To export the events list click the export icon. You can export in PDF format.

  5. To filter the list of events to view only a subset, click **Open Filters** to open the filters panel. Make your filtering selections, then click **Update Filters**.

You can search events by:

     * Event ID
     * Event message
     * Time range
     * Event severity (informational, warning, and error notification)
**Note:** To clear a single filter without clearing all filters, click the **x** next to the applied filter (listed next to **Close Filters**). To clear all filtering, click **Clear Filters** in the filters panel.
  6. See View event details for specifics on events in the **Events** window.


**Note:** All events that display in the appliance management console's **Monitor** > **Events** page are logged to Cloud Logging. To display these events see, [Backup and DR event logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events) and to setup notification on these (or specific) events see, [Configure a log-based alert](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).

## Appliance management console dashboard events panel

The **Events** panel on the appliance management console dashboard provides quick access to error and warning events that have occurred over the past 24 hours. It polls for fresh data every two minutes.

  * **Errors number** : Shows errors over the past 24 hours.
  * **Warnings number** : Shows warnings over the past 24 hours.



Click the **Errors** or **Warnings** number area to access the **Events** page. You can also access the events from the **Monitor** > **Events**.

Use these instructions to view events:

  1. Click the **Monitor** > **Events**. A list of generated events are displayed in the **Events** page.
  2. In the **Events** page, you can do the following:

     * View the details of the generated event.

     * In the **Search** box, type a keyword to search across the data in the appliance management console database for a specific word or keyword and to display only that subset of data in the table.

     * Modify the number of rows displayed in a table page, by selecting the required vaule. The choices include: 25, 50, 100, or 500 rows per table page.

     * Click the download icon to export the events list. The list is exported in the PDF format.

     * From the **Filter By** panel, you can filter events by:

       * Event ID
       * Event message
       * Event date
       * Required cleaning
       * Event severity (informational, warning, or error notification)
       * Backup plan violation

To clear a filter, click the **x** beside **Hide Filters**. To clear all filtering, click **Clear Filters** in the filters panel.


**Note:** All events that display in the appliance management console's **Monitor** > **Events** page are logged to Logs Explorer. To display these events see, [Backup and DR event logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events). To setup notification on these (or specific) events see, [Configure a log-based alert](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).

## View event details

Use these instructions to view the details for a specific event:

  1. Click the **Monitor** tab and select **Events** from the drop-down menu.

The **Events** page opens.

  2. Select an item in the **Events** window and then click **View Details** from the bottom right corner of the window. You can also right-click on an event in the list and select **View Details** from the drop-down menu.

  3. The **Event Details** page displays the following.

     * **ID** : The database row ID in the Backup and DR Event data table. This can be ignored.
     * **Event ID** : A unique event identifier.
     * **Appliance Name** : The ID of the backup/recovery appliance where the event occurred.
     * **Component** : The Backup and DR that threw the error.
     * **Application Name** : The user-assigned name of the application, if applicable.
     * **Application Type** : The type of application, if applicable.
     * **Job Name** : A unique job identifier.
     * **Error Code** : If an error code or an event ID or both were generated for the event, it is shown. An error code is generated only for events generating a warning and an error.
     * **Error Message** : A text description of the event. The error message is often supplements by additional information from external components.
     * **Requires Cleaning** : This event continues report until it is cleared. The appliance raises the event periodically until it is cleared.
     * **Event Date** : The time that the event occurred.
     * **Sync Date** : The time at which the events is reported at the appliance management console.
**Note:** Not all events include every detail. For example, event 55468 is about the appliance, so it will have **no application** specific information.
  4. When you are done reviewing event details, click **Return to Events** to return to the **Events** window.




## Review job failures displayed on the appliance management console dashboard

The number of and information about job failures is displayed in the appliance management console dashboard.

Click the number of job failures to display a list of failed jobs in the **Jobs Monitor** service.

Right-click on a job entry to display detailed information about the entry.

Review the details of the entry and:

  * Use the **Search[Knowledge Base](https://docs.cloud.google.com/backup-disaster-recovery/docs/support)** link to learn how to resolve the issue.

  * Ensure the application's host is running.

  * For virtual machines, verify the VM has not been migrated to another vCenter.

  * If applicable, verify that the Backup and DR agent service is running.




## Review errors and warnings displayed on the appliance management console dashboard

The number of errors and warnings encountered by a backup/recovery appliance are displayed in the upper right-hand corner of the dashboard:

  1. Click the number of errors or warnings to display a list of the errors or warning in the **Events Monitor** service. For example:

  2. Right-click on an error entry to display detailed information about the error.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
