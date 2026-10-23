---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-list-and-yaml/
title: Access backups in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:44.400858+00:00
---

# Access backups in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-list-and-yaml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Access backups in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Use the information on this page to access backups for recovery, restore, and other operations in the appliance management console.

## Access the list of backups

Use these instructions to view captured application data in a table view:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu. 

The **Applications** page opens.

  2. Right-click the application you want to access and select **Access** from the drop-down menu.

The **Access** page opens listing each available image for the application in the timeline ramp view.

  3. Click **Table** on the **Access** page to open the list view for the managed application.

  4. To modify the display of the properties in this view, you can do the following:

     * **Search by keyword** : To display a specific subset of data in the list table, use the **Type to search** field. Enter a word in the field to complete a search across the appliance management console's database for that specific word and display the results in the table.

**Note:** This search is not case sensitive.
     * **Select table fields** : To modify which fields appear in the table, click the three vertical lines in the top-right corner of the table and select the checkboxes for any fields you want displayed.

     * **Sort content** : To sort the content listed in a table column by alphanumeric order, select a column header and then click the up or down arrows to change the order.

     * **Adjust column width** : You can adjust the width of a table column to show more content in the table by dragging the column divider in a column header to the left or right. Column dividers are marked by a pair of thin gray lines.

     * **Filter by** : To filter the list of hosts, click **Show filters**. Click the arrow next to each option to select the filters you want to use.

**Note:** Filters that are of type text, list, or date persist across different appliance management console sessions for the same user.
     * **Adjust rows.** Click the drop-down next to the three vertical lines menu menu to select how many rows display in the table.

     * **Export the list** : You can export the list to PDF by clicking the download button.




You can return to the timeline ramp view by clicking **Timeline**. For more information, see Access the timeline ramp view.

## Access the timeline ramp view

Use these instructions to see an application's timeline ramp view:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Right-click the application you want to access and select **Access** from the drop-down menu options.

The **Access** page opens listing each available image for the application in the timeline ramp view.

**Note:** The shaded area in the snapshot and OnVault pools indicates availability of logs.
  3. Click the specific image and then select how you want to access the image from the drop-down menu.

  4. Click the application icon to open to refine your search results. You can open the application panel by clicking **Applications** > **Consistency Groups** > **Logical Groups**.

  5. To quickly navigate through weeks of captured images you can use the following:

     * The navigation bar to select images from a much wider timeline. Images available for a specific date are represented as color coded dots on the bar:
     * The calendar widget to jump to a specific date.
     * The mouse scroll wheel or the up and down arrows.



## Select an image from the timeline ramp view

The timeline ramp view is a time-based, graphical representation of an application's captured images, where you can see the following:

  * The ramp's y-axis shows seven days of captured images.
  * The ramp's x-axis is divided into lanes for each image type.



Each image is represented by a circle icon on the timeline ramp. Each image icon is color coded to match its corresponding backup plan template policy.

The number of active images—or mounts—associated with an image are displayed at the top of the image icon. When you click an image icon, the image details are listed in the upper right-hand corner of the page. Following the image details is a drop-down menu that lets you to access the image using different access methods. Sensitive images have a lock icon next to their name. An icon in the remote snapshot lane indicates there is a StreamSnap image available.

## Application logs

An application's logs are usually captured separately from the application. If an application is captured along with its logs, the background in the **Snapshot** lane matches the color of the **Snapshot** image, or the OnVault image. You can see the image details by hovering the cursor over an image in either the Snapshot or OnVault lanes.

**Note:** If the snapshot or OnVault lane are not shaded, it indicates that the application's logs are not captured. Logs capture is not available for remote snapshot pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
