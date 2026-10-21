---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/images/
title: Manage preserved backups in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:43:18.598321+00:00
---

# Manage preserved backups in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage preserved backups in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

You can display a list of preserved and discarded snapshot images in the **Images** section of the **Appliance Configuration** page.

From the **Preserved Images** window you can do the following:

  * View **Preserved Images** history to see how many snapshot images were preserved over a period of a week or a month.
  * Select a single snapshot image and access this image in the **Restore** window of the **App Manager**.
  * Expire a single image or multiple preserved images.



From the **Discarded Images** window you can see a summary of images that have been expired without processing over the past day, week, or month.

You can also monitor the **Image Preservation** status for snapshot images:

  * The dashboard in the appliance displays an **Image Preservation** status under the **System Health** widget to inform you of the general status of preserved snapshot images.
  * The **Monitor** displays alerts and warnings specific to image preservation to inform you of different activities that can occur when the backup/recovery appliance attempts to preserve snapshot images.



For details on how to modify or disable the application priority settings for preserved snapshots jobs, see [Configure image preservation priority setting for snapshot images](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#image-preserve).

## View preserved backups history

You can view a graph that shows how many images were in a preserved state on each day over a selected time period (which can be an interval of either **Last Week** or **Last Month**). Data is logged in the **Preserved Images History** graph on an hourly basis.

Use these instructions to view a history of preserved images:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance, click **Configure Appliance** to open the **Appliance Configuration** page.

  3. Go to **Images** then **Preserved/Discarded**.

  4. Click **Preserved Images** and then click the **History** button. The **Preserved Images History** graph appears displaying the number of images preserved over the specified time interval. You can:

     * Modify the time interval to **Last Week** or **Last Month**. The data updates in the history graph based in the interval selection.
     * Hold the pointer over over a date in the graph to see the timestamp and number of images preserved on that date.



## Work with preserved backups

You can choose from the list of preserved snapshot images and perform the following actions on those images from the **Manage** tab:

  * Select from the list of preserved images and navigate to that image in the **App Manager**.
  * Expire one or more selected snapshot images.



When expiring snapshots, the amount of space reclaimed may be less than the amount of space consumed by that snapshot. This is due to the common block reference between snapshots. To ensure maximum space reclamation, expire the oldest snapshot first.

Use these instructions to view a list of all preserved snapshot images and perform an operation on an image:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance, click **Configure Appliance** to open the **Appliance Configuration** page.

  3. Go to **Images** then **Preserved/Discarded**.

  4. All preserved snapshot images are listed.

  5. If you want to navigate to a preserved image in the **App Manager** , select a single preserved image using the appropriate checkbox, then click **Go to Image**. The preserved image appears in the **Restore** window of the **App Manager**.

  6. If you would like to manually expire one or more older preserved images, select a single image or multiple images using the appropriate checkboxes, then click **Expire**.

A confirmation dialog appears instructing you that not all of the space consumed by this image will be reclaimed and that a best practice is to expire the oldest snapshot image first for maximum space reclamation. Click **OK** to proceed with the preserved image expiration.




## View discarded backups

Preserved images will automatically be expired and discarded when pool space or VDisk count reaches the warning threshold levels set. In this case, images are expired based on application priority and age. Images for applications with lower priority will be expired ahead of applications with higher priority. Within a priority level, older images will be expired before newer images.

From the **Discarded Images** list, you can see a summary of images that have been expired over the past day, week (seven-day interval), or month (30-day interval) along with the reason for discarding the image. This list also includes images that have been manually expired prior to processing.

Use these instructions to view the images discarded without processing by the backup/recovery appliance:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.

The **Appliances** page opens.

  2. Select an appliance and click **Configure Appliance** to open the **Appliance Configuration** page.

  3. Go to **Images** then **Preserved/Discarded**.

  4. Click the **Discarded Images** tab.

  5. All expired snapshot images are listed.

  6. Change the time window of discarded images listed by making a selection from the drop-down list in the **Discarded Images** list. You can choose to view discarded images over the past one-day, seven-day, or 30-day interval.




## Alerts and warnings for image preservation

This section outlines the various alerts and warnings related to image preservation.

### Warning level alert: first time the snapshot expiration window is reached

A **Warning** level alert is generated (and posted to the event log) the first time a snapshot that is eligible for expiration is held for pending processing.

This **Warning** level alert is generated for the first snapshot for each application that has its expiration deferred. When the count of deferred expirations for an application goes to zero, the **Warning** alert trigger is reset.

### Warning level alert: snapshot image expired because threshold limit exceeded

When an application has preserved snapshots is expired because the backup/recovery appliance has exceeded the threshold limits (such as VDisk count or pool capacity), a **Warning** level alert indicating this condition is posted. This warning will be logged only for the first snapshot expired due to this situation.

Here is a summary of the **Warning** thresholds for VDisk and storage pools as specified in the **Appliance Configuration** page:

  * The **Warning** threshold for VDisks usage is 90%. The VDisk limit for the backup/recovery appliance is 2048.

  * The **Warning** level is 80% for the snapshot pool. The default value is 90% for the snapshot and primary pools.




### Warning level alert: all preserved images have been processed

When the number of preserved images drops to zero, the following alert is posted in the **Monitor** :

### Weekly error level event: images remotely replicated after seven days

When there are images that have not been remotely replicated for a period of seven days, a weekly error level event of severity **Error** is raised. When the seventh day is reached an alert will be generated to inform you that the appliance has been in **Preserve Image Mode** for seven days.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
