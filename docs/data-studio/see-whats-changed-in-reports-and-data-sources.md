---
url: https://docs.cloud.google.com/data-studio/see-whats-changed-in-reports-and-data-sources/
title: See what's changed in reports and data sources \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:11:01.561557+00:00
---

# See what's changed in reports and data sources  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/see-whats-changed-in-reports-and-data-sources/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  See what's changed in reports and data sources Stay organized with collections  Save and categorize content based on your preferences. 

As you edit a report or data source, Data Studio keeps a history of your changes. You can also manually save a version at any time. Version history lets you view, restore and delete previous revisions. You can also see when the revision was created, and by whom.

## Restore an earlier version of a report

To restore an earlier versions of a report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the menus on the top left, click **File** ![And then.](https://docs.cloud.google.com/static/data-studio/images/standard--all-hcs--and-then-use-this-for-gup-hcs.png)**Version history** ![And then.](https://docs.cloud.google.com/static/data-studio/images/standard--all-hcs--and-then-use-this-for-gup-hcs.png)**See version history**. The **Version history** panel will display a list of saved versions.
  3. Click a saved version to see that version of the report. The name of the editor who is responsible for that version appears underneath the timestamp or version name.
  4. At the top of the page, click **RESTORE THIS VERSION**. The selected version becomes the current version and appears at the top of the **Version history** panel.



To return to the current version without restoring an older version, on the top left of the page, click ![Back](https://docs.cloud.google.com/static/data-studio/images/standard--tasks--back.png)**Back**.

## Version history and data sources

Reusable data sources maintain their own version history, independent of the reports that use them. Version history for embedded data sources is tied to the version history of their parent report. Restoring a report doesn't affect reusable data sources. Restoring a report with embedded data sources also restores those data sources.

When you restore a report to a previous version, the reusable data sources within the report remain unaffected. However, if the restored version is incompatible with a specific data source, you'll need to either restore that data source to a compatible version or manually adjust it to ensure compatibility.

Restoring a report that contains embedded data sources will also revert those data sources to their state at the time the report version was created. It's not possible to directly restore an embedded data source to a previous version independently. This ensures that the embedded data sources function as intended with any version of the report.

## Restore an earlier version of a reusable data source

**Note:** To see version history for a reusable data source, either you must be the owner of the data credentials, or the data source must use Viewer's Credentials. This helps protect your data from unauthorized access. [Learn more about data credentials](https://docs.cloud.google.com/data-studio/data-credentials).

  1. At the top of the Data Studio home page, click **Data Sources**.
  2. Locate the data source, and then click its name to edit it.
  3. In the top right, click ![Restore.](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--restore-with-clock.png)**See version history**. The **Version history** panel will display a list of saved versions.
  4. Click a saved version to see that version of that data source. The name of the editor responsible for that version appears underneath the timestamp or version name.



To return to the current version without restoring an older version, on the top left of the page, click ![Back.](https://docs.cloud.google.com/static/data-studio/images/standard--tasks--back.png)**Back**.

## Named versions

In the **Version history panel** , you can manually create a version or rename an existing version in the following ways:

![The Version history panel includes the Restore this version button, Only show named and published versions toggle, and three-dot option menus for each version with the options to Rename, Remove name, or Delete.](https://docs.cloud.google.com/static/data-studio/images/named-versions-2021-05-20.png)

  1. With the restore selected version button
  2. With the **Only show named and published versions** toggle.
  3. With the **More options button**



### Create a new named version of a report

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the menus on the top left, click **File** ![And then.](https://docs.cloud.google.com/static/data-studio/images/standard--all-hcs--and-then-use-this-for-gup-hcs.png)**Version history** ![And then.](https://docs.cloud.google.com/static/data-studio/images/standard--all-hcs--and-then-use-this-for-gup-hcs.png)**Name current version**.
  3. Enter the version name, then click **Save**.



### Rename an existing version of a report or data source

  1. Display earlier versions of the report or data source (as described previously).
  2. Select the version that you want to rename, and then click ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)**More options**.
  3. Select **Rename** , and then enter the new name.
  4. To return to the current version, in the upper left, click ![Back.](https://docs.cloud.google.com/static/data-studio/images/standard--tasks--back.png)**Back**.



### Restore the automatically generated version name

  1. Display earlier versions of the report or data source (as described previously).
  2. Select the version that you want to rename, and then click ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)**More options**.
  3. Select **Remove name**.
  4. To return to the current version, in the upper left, click ![Back](https://docs.cloud.google.com/static/data-studio/images/standard--tasks--back.png)**Back**.



## Delete a version

**Caution:** Deleting a version is permanent. You can't undo this action.

  1. Display earlier versions of the report or data source (as described previously).
  2. Select the version you want to delete, and then click ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png)**More options**.
  3. Click **Delete** , and then click **Delete** again to confirm.
  4. To return to the current version, in the upper left, click ![Back](https://docs.cloud.google.com/static/data-studio/images/standard--tasks--back.png)**Back**.



## Undo a version restoration

If you accidentally restore a version of the report and want to return to the previous (most recent) version, click the version immediately following the current version.

## Unable to see a particular version of your file?

The revisions for your reports or data sources may occasionally be merged to save storage space.

## Limits of version history

  * To see version history, you must have edit permission to the report or data source.
  * Version history is not preserved for copies of a report.
  * Changes to data source credentials can't be restored. You must apply credential changes directly to the current version.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
