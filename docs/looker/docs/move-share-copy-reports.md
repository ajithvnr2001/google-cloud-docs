---
url: https://docs.cloud.google.com/looker/docs/move-share-copy-reports/
title: Move, share, and copy reports \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:51.225595+00:00
---

# Move, share, and copy reports  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/move-share-copy-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Move, share, and copy reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

Looker stores reports, [Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore) (saved visualized query results), and [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards) (collections of tiles that show visualized query results) in folders. When you create a report in Looker, you can share it with other users by clicking **Save and Share** and saving it to a folder to which those users have access. Access to these folders is controlled by [access levels](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) and user permissions. Once a report is saved, you can move or copy the report to a different folder, or you can delete the report.

This page guides you through the components of sharing reports by moving and copying them to folders for other users to access in Looker. Read the following sections to learn about these concepts:

  * Things to know about sharing reports
  * Move reports
  * Copy reports
  * Delete reports



## Things to know about sharing reports

There are several things to know about sharing reports in Looker:

  * Reports can't be stored in folders that are nested more than five folder levels deep, and they also can't be stored in folders with [custom access levels](https://docs.cloud.google.com/looker/docs/access-levels#configure_groups_to_provide_granular_access). This restriction applies to saving, copying, and moving reports, as well as copying or moving folders that _contain_ reports. For example, consider the following use cases:

    * You can't save a report in a subfolder that is nested 10 folder levels away from the parent folder.
    * You can't move a folder that contains reports to a folder that has custom access levels.
    * You can't move a report to a folder that has custom access levels.
    * You _can_ move a folder into another folder that has inherited access levels.
  * Users can share a report with other users by moving it into a folder that those users have access to.

  * Copying reports with embedded data sources that support [Owner credentials](https://docs.cloud.google.com/looker/docs/studio/roles-and-permissions#basic_roles), for example, Sheets and BigQuery, can result in dataset configuration errors. We recommend that you don't copy reports that contain that have embedded data sources that support Owner credentials.




For more information about content access and permissions, see [Controlling user content access](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#controlling_user_content_access) and [How content access and permissions interact](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management#how_content_access_and_permissions_interact).

If you want to change the access level settings for a folder, see [Viewing and managing folder access levels](https://docs.cloud.google.com/looker/docs/organizing-spaces#viewing_and_managing_folder_access_levels).

## Move reports

Once a report is saved, you can move the report to another folder. To move reports, users must have one of the following types of access:

  * [**Admin** access](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) to the Looker instance.
  * [**Manage Access, Edit** access level](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) to the report's folder
  * **Manage Access, Edit** access level to the folder to which the report will be moved

**Caution:** Reports can't be moved to folders that are more than five levels deep, and reports can't be saved in folders that have [custom access levels](https://docs.cloud.google.com/looker/docs/access-levels#configure_groups_to_provide_granular_access).

You can move reports individually, or you can move multiple reports at once.

**Note:** If you want to move an entire folder, see [Renaming, moving, or deleting a folder](https://docs.cloud.google.com/looker/docs/organizing-spaces#renaming_moving_or_deleting_a_folder). See the Things to know about sharing reports section on this page for things to know about moving folders that contain reports.

### Move individual reports

To move an individual report to a new folder, follow these steps:

  1. From a folder, click a report's more_horiz three-dot **Options** menu.

If the folder contents are displayed in [grid view](https://docs.cloud.google.com/looker/docs/finding-content#using_list_view_and_grid_view), hold the pointer over a report thumbnail to access the more_horiz three-dot **Actions** menu.

  2. Select the **Move** option to open the **Move reports** window.

  3. In the **Move reports** window, select the name of a top-level folder on the left to navigate to it.

  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.

  5. Click **OK**.




### Move multiple reports

To move multiple reports to a new folder, follow these steps:

  1. From a folder, click the check_box checkbox for any reports that you want to move.

If the folder contents are displayed in [grid view](https://docs.cloud.google.com/looker/docs/finding-content#using_list_view_and_grid_view), hold the pointer over a report thumbnail to access the check_circle_outline **Select** checkmark, and then select the checkmark to include the report in the bulk move.

  2. Select the **Move** option in the **Reports** section of the folder to open the **Move reports** window.

  3. In the **Move reports** window, select the name of a top-level folder on the left to navigate to it.

  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.

  5. Click **OK**.




## Copy reports

To copy reports, users must have one of the following types of access:

  * [**Admin** access](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) to the Looker instance
  * [**Manage Access, Edit** or **View** access level](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) to the report's folder
  * **Manage Access, Edit** access level to the folder to which the report will be copied, to save it in a folder other than the parent folder

**Caution:** Copied reports can't be saved to folders that are more than five levels deep, and copied reports can't be saved to folders that have [custom access levels](https://docs.cloud.google.com/looker/docs/access-levels#configure_groups_to_provide_granular_access).

You can copy reports individually, or you can copy multiple reports at once.

### Copy individual reports

To copy an individual report, follow these steps:

  1. From a folder, click a report's more_horiz three-dot **Options** menu.

If the folder contents are displayed in [grid view](https://docs.cloud.google.com/looker/docs/finding-content#using_list_view_and_grid_view), hold the pointer over a report thumbnail to access the more_horiz three-dot **Actions** menu.

  2. Select the **Copy** option to open the **Copy reports** window to select a folder to save the copy.

  3. In the **Copy reports** window, select the name of a top-level folder on the left to navigate to it.

  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.

  5. Click **Copy**.




### Copy multiple reports

To copy multiple reports, follow these steps:

  1. From a folder, click the check_box checkbox for any reports that you want to copy.

If the folder contents are displayed in [grid view](https://docs.cloud.google.com/looker/docs/finding-content#using_list_view_and_grid_view), hold the pointer over a report thumbnail to access the check_circle_outline **Select** checkmark, and then select the checkmark to include the report in the bulk copy.

  2. Select the **Copy** option in the **Reports** section of the folder to open the **Copy reports** window. Then, select a folder to save the copy.

  3. In the **Copy reports** window, select the name of a top-level folder on the left to navigate to it.

  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.

  5. Click **Copy**.




## Delete reports

To delete reports, users must have one of the following types of access:

  * [**Admin** access](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) to the Looker instance
  * [**Manage Access, Edit** access level](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) to the report's folder



To _restore_ deleted reports, users must have Admin access. See the [Deleted and unused content for admins](https://docs.cloud.google.com/looker/docs/admin-spaces#trash) documentation page for more information about how to restore deleted content.

You can delete reports individually, or you can delete multiple reports at once.

**Important:** Use caution when you delete a folder. In a single action you can delete all folder content, which could include subfolders. A Looker admin might be able to recover the content, but — even if this is possible — the content will be returned to the personal folders of the users who created it and not back to the folder that you deleted. See the [Deleted and unused content for admins](https://docs.cloud.google.com/looker/docs/admin-spaces#trash) documentation page for more information about how to restore deleted content.

### Delete individual reports

To delete an individual report, follow these steps:

  1. From a folder, click a report's more_horiz three-dot **Options** menu.

If the folder contents are displayed in [grid view](https://docs.cloud.google.com/looker/docs/finding-content#using_list_view_and_grid_view), hold the pointer over a report thumbnail to access the more_horiz three-dot **Actions** menu.

  2. Select the **Move to Trash** option.

  3. Click the **Move to Trash** button to confirm, or click the **Cancel** button to cancel.


**Note:** If you accidentally delete a report, your Looker admin _might_ be able to recover it for you, but only if your Looker admin team has not already emptied Looker's [trash](https://docs.cloud.google.com/looker/docs/admin-spaces#trash) as part of their maintenance process. Reports created with a Looker version prior to Looker 25.4 can't be recovered.

### Delete multiple reports

To delete multiple reports, follow these steps:

  1. From a folder, select the check_box checkbox for any reports that you want to delete.

If the folder contents are displayed in [grid view](https://docs.cloud.google.com/looker/docs/finding-content#using_list_view_and_grid_view), hold the pointer over a report thumbnail to access the check_circle_outline **Select** checkmark, and then select the checkmark to include the report in the bulk delete.

  2. Select the **Move to Trash** option in the **Reports** section of the folder.

  3. Click the **Move to Trash** button to confirm, or click the **Cancel** button to cancel.


**Note:** If you accidentally delete a report, your Looker admin _might_ be able to recover it for you, but only if your Looker admin team has not already emptied Looker's [trash](https://docs.cloud.google.com/looker/docs/admin-spaces#trash) as part of their maintenance process. Reports created with a Looker version prior to Looker 25.4 can't be recovered.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
