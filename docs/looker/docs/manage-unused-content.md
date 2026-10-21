---
url: https://docs.cloud.google.com/looker/docs/manage-unused-content/
title: Managing unused content \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:18.267462+00:00
---

# Managing unused content  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/manage-unused-content/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Managing unused content Stay organized with collections  Save and categorize content based on your preferences. 

The **Unused content** folder lets admins and users quickly identify and manage the unused content on a Looker instance. In addition, the **Unused content** folder also provides the following capabilities for managing unused content:

  * Lets admins programmatically schedule content cleanups for an individual piece of content or in bulk, and send automatic notifications to content owners.
  * Lets content owners opt out of automated scheduled cleanups of specific content.
  * Lets admins and users move content to the trash.



This page provides guidance for using the capabilities that are provided by the **Unused content** folder. This page includes the following sections:

  * User and instance requirements
  * Things to know
  * Navigating the Unused content folder
  * Content management for admins
  * Content management for users
  * Related resources



## User and instance requirements

To access and manage unused content in the **Unused content** folder, the following requirements must be met:

  * Your Looker (original) or Looker (Google Cloud core) instance must be running Looker 26.14 or later, and your Looker (original) instance must be [Looker-hosted](https://docs.cloud.google.com/looker/docs/glossary#looker-hosted).
  * To access the **Unused content** folder, you must have the [`save_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_dashboards) or [`save_looks`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_looks) permission.



## Things to know

There are several things to know about the **Unused content** folder.

  * Content is considered "unused" if it meets one of the following criteria: 
    * If there are 0 views within the selected time period
    * If there are no active schedules configured for the piece of content
    * If the piece of content isn't under a temporary exclusion (marked as active) by the content owner
  * The **Unused content** folder only lists content that has few direct views from within the Looker instance. The **Unused content** folder doesn't include content that is public, content that is part of a user's favorites, Looks that are embedded within a dashboard, or content that is used by API sources like [Connected Sheets](https://docs.cloud.google.com/looker/docs/connected-sheets). To more accurately track content usage from API sources, admins should use the [System Activity History explore](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#which_queries_were_initiated_from_within_google_sheets?) and filter for `query_api_client_context.cs_spreadsheet_id isn't null`.
  * Content can still be considered "unused", even if it is [certified](https://docs.cloud.google.com/looker/docs/content-certification).
  * Looks can still be considered "unused", even if they are saved to dashboards that are _not_ "unused".
  * Trashing content from the **Unused content** folder doesn't permanently delete the content, but moves it to the **Trash** folder. Admins can restore or permanently delete the content that has been moved to the trash from the [**Trash** folder](https://docs.cloud.google.com/looker/docs/admin-spaces#trash).
  * Admins can see all of the unused content across the instance on the **Unused content** tab in the **Unused content** folder. Users will only see the content that they own, and the content to which they have [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access.
  * Users will only see the content that they own, and the content to which they have **Manage Access, Edit** access on the **Scheduled for trashing** tab in the **Unused content** folder.
  * The dashboard and Look sections of the **Unused content** and **Scheduled for trashing** tabs will display only 30 pieces of content at a time. If there are more than 30 dashboards or 30 Looks, they will be divided across multiple pages for each section. You'll see the page navigation icons **>** and the text **Dashboards (or Looks) 1-30** at the bottom of each section.
  * Admins can only bulk schedule 30 pieces of content for trashing per schedule, per type of content. For example, one schedule can only include up to 30 dashboards, or 30 Looks. Looks and dashboards must be scheduled for trashing separately in their individual sections.
  * When users opt-out content from scheduled trashing, the content will be ineligible for trash scheduling for 90 days.



## Navigating the Unused content folder

Looker admins and users with appropriate permissions can find the **Unused content** folder in one of two ways:

  * By expanding the [**Folder** section](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu) of the main navigation panel
  * By clicking the [**Folder** option](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu) of the main navigation panel

**Note:** You can't access the **Unused Content** folder from the **All Folders** option of the main navigation panel.

Once you have opened the **Unused content** folder, you will see the following elements:

![ ](https://docs.cloud.google.com/static/looker/docs/images/unused-content-folder-268.png)

  1. The **Time since last use (days)** selector: Filters the **Unused content** folder to display content that is unused for the selected number of days. 90 days is selected by default.
  2. The **% OF TOTAL CONTENT IS UNUSED** tile: Displays the percentage of unused content compared to the total content on the instance for the selected timeframe, with the breakdown numbers of dashboards and Looks.

**Note:** Admins will see the percentage of unused content compared to the total number of pieces of content on the entire instance, while users will see the percentage of unused content compared to the total number of pieces of content to which they have access.
  3. The **SCHEDULED FOR TRASH** tile: Displays the total number of pieces of content that are scheduled for trashing, with the breakdown number of dashboards and Looks.

**Note:** Admins will see the total number of pieces of content that are scheduled for trashing across all content, while users will only see the content that they own, and content to which they have [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access.
  4. The **Unused content** tab: Lists all unused content for the selected timeframe, organized in a section for **Dashboards** and a section for **Looks**.

  5. The **Scheduled for trashing** tab: Lists all unused content that is scheduled for trashing, organized in a section for **Dashboards** and a section for **Looks**.

**Note:** Admins will see the all of the content that is scheduled for trashing, while users will only see the content that they own, and the content to which they have [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access.
  6. Section headers: Specifies the type of content that is listed. Content on both the **Unused content** and **Scheduled for trashing** tabs is organized under separate sections for **Dashboards** and **Looks** , depending on the type of content.

  7. The selection checkboxes: Lets users select or deselect either an individual piece of content by selecting the checkbox inline with the content name, or in bulk by selecting the box inline with the **Name** subheader.

**Note:** The selection checkboxes appear when the content on a tab is displayed in **List view**. This is the default display for the **Unused content** folder.
  8. The content metadata: Displays metadata for each piece of content.

     * The content metadata for the **Unused content** tab include the following: 
       * **Name** : The name of the dashboard or Look, and the name of the user that created the content.
       * **Last Used** : The date that the dashboard or Look was last viewed.
       * **Created Date** : The date that the dashboard or Look was created.
       * **Folder** : The name of and link to the folder in which the dashboard or Look is saved.
       * **Inactive owner** : The status of the user who created the content. If the user has been [disabled on the instance](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#disabling_users), the status will display **Yes**.
     * The content metadata for the **Scheduled for trashing** tab include the following: 
       * **Name** : The name of the dashboard or Look, the name of the user that created the content, and the total number of times that each piece of content has been viewed.
       * **Folder** : The name of and link to the folder in which the dashboard or Look is saved.
       * **Planned Deletion Date** : The number of days from today that the content will be trashed.
  9. The **Sort by** menu: Displays the option for sorting the content.

     * The options for sorting the **Unused content** tab include the following: 
       * **Name**
       * **Last Used Date**
       * **Created Date**
     * The options for sorting the **Scheduled for trashing** tab include the following: 
       * **Name**
       * **Planned Deletion Date**
  10. The **^** **Order** icon: Lets users sort the content in ascending or descending order. The icon will face downward (**v**) or upward (**^**) to indicate the sort direction (ascending or descending).

  11. The grid_view **Show items in a grid** or vertical_split **Show items in a list** icon: Lets you display the content in either grid view (as thumbnails) or as a list. grid_view **Show items in a grid** will display if the content is organized in list view, and vertical_split **Show items in a list** will display if the content is organized in grid view.

**Important:** You can only select items in bulk when viewing the **Unused folder** content in a list.



## Content management for admins

Admins can use the features of the **Unused content** folder to perform the following actions:

  * Scheduling content for trashing
  * Canceling scheduled trashing
  * Trashing content now



### Scheduling content for trashing

To schedule items for trashing, follow these steps:

  1. Navigate to the **Unused content** folder and open the **Unused content** tab.
  2. Choose a timeframe from the **Time since last use (days)** selector. The default selection is 90 days.
  3. If viewing the content as a list, select pieces of content by clicking the checkbox inline with the content name, or select content in bulk by clicking the box inline with the **Name** subheader. Click the inline checkbox again to deselect a piece of content, or deselect all selected content by clicking the box inline with the **Name** subheader.

**Note:** You can only bulk schedule 30 pieces of content for trashing per schedule, per type of content. For example, one schedule can only include up to 30 dashboards, or 30 Looks. Looks and dashboards must be scheduled for trashing separately, in their individual sections.

If you are viewing the content as a grid, you cannot select content in bulk. You can select dashboards or Looks by placing your cursor over the content thumbnail and clicking the **Select** checkbox.

You can click the grid_view **Show items in a grid** or vertical_split **Show items in a list** icon to switch between list view or grid view.

  4. Once the content is selected, click **Schedule for trash** to open the **Schedule for trash** dialog.

  5. Input a number of days, with a minimum of 3 days, into the **Move to trash in (days)** field. 14 days is the default value.

  6. Input any email addresses into the **Notify additional users** field if there are other users in addition to the content owner that you want to notify of the scheduled trashing.

  7. Click **Schedule for trash** to complete the schedule, or click **Cancel** to cancel.




Once a schedule has been set, the content owner of any dashboards or Looks that are impacted will receive the following notifications:

  * **Initial notification** : Sent immediately after the content is scheduled for trashing.
  * **Mid-cycle reminder:** Sent halfway through the scheduled duration.
  * **Final warning** : Sent one day before the scheduled trashing.



For example, if an item is scheduled for trashing in 14 days, the content owner will receive the following notifications:

  * Day 1: Initial notification is sent.
  * Day 7: Mid-cycle reminder is sent.
  * Day 13: Final warning is sent.



If a user chooses to opt out, their content will be removed from the **Unused content** folder and will be ineligible for trash scheduling for 90 days.

The content that is scheduled for trashing will move to the **Scheduled for trashing** tab, where you can cancel the scheduled trashing, or trash the content now.

Trashing content from the **Unused content** folder doesn't permanently delete the content, but moves it to the **Trash** folder. Admins can restore or permanently delete the content that has been moved to the trash from the [**Trash** folder](https://docs.cloud.google.com/looker/docs/admin-spaces#trash).

### Canceling scheduled trashing

Admins can cancel scheduled trashing for content by following these steps:

  1. Navigate to the **Unused content** folder and open the **Scheduled for trashing** tab.
  2. If viewing the content as a list, select pieces of content by clicking the checkbox inline with the content name, or select content in bulk by clicking the box inline with the **Name** subheader. Click the inline checkbox again to deselect a piece of content, or deselect all selected content by clicking the box inline with the **Name** subheader.

**Note:** You can bulk schedule only 30 pieces of content at a time per schedule and per type of content. For example, you can only cancel a scheduled trashing for up to 30 dashboards or 30 Looks. You must opt out from scheduled trashing of Looks and dashboards separately, in their individual sections.

If you are viewing the content as a grid, you cannot select content in bulk. You can select dashboards or Looks by placing your cursor over the content thumbnail and clicking the **Select** checkbox.

You can click the grid_view **Show items in a grid** or vertical_split **Show items in a list** icon to switch between list view or grid view.

  3. Once the content is selected, click **Remove schedule** to opt out the content from a scheduled trashing. Alternatively, click **Restore content**.

The content that is marked as restored will be removed from the **Unused content** folder, and will be ineligible for trash scheduling for 90 days. The content that is unscheduled and moved to the **Unused content** tab will still be eligible for future scheduled trashings. In either case, content owners will no longer see their content on the **Scheduled for trashing** tab.

  4. Confirm the action in the **Restore content?** dialog or **Remove schedule?** dialog. Click **Cancel** to cancel the action.




### Trashing content now

In addition to scheduling trashings to occur in the future, admins can choose to trash content _now_. To trash content now, follow these steps:

  1. Navigate to the **Unused content** folder and open either the **Unused content** tab or the **Scheduled for trashing** tab.
  2. If viewing content on the **Unused content** tab, choose a timeframe from the **Time since last use (days)** selector. The default selection is 90 days.
  3. If viewing the content as a list, select pieces of content by clicking the checkbox inline with the content name, or select content in bulk by clicking the box inline with the **Name** subheader. Click the inline checkbox again to deselect a piece of content, or deselect all selected content by clicking the box inline with the **Name** subheader.

**Note:** You can only bulk trash 30 pieces of content, per type of content, at one time. For example, one trashing can only include up to 30 dashboards, or 30 Looks. Looks and dashboards must be trashed separately, in their individual sections.

If you are viewing the content as a grid, you cannot select content in bulk. You can select dashboards or Looks by placing your cursor over the content thumbnail and clicking the **Select** checkbox.

You can click the grid_view **Show items in a grid** or vertical_split **Show items in a list** icon to switch between list view or grid view.

  4. Once the content is selected, click **Move to trash** to open the **Move selected items to trash** dialog.

  5. Click **Move to trash** to confirm, or **Cancel** to cancel.




Trashing content from the **Unused content** folder doesn't permanently delete the content, but moves it to the **Trash** folder. Admins can restore or permanently delete the content that has been moved to the trash from the [**Trash** folder](https://docs.cloud.google.com/looker/docs/admin-spaces#trash).

## Content management for users

Users that have the required permissions and have either [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access to content, or own content, can use the features of the **Unused content** folder to perform the following actions:

  * Identify and opt-out content from scheduled trashing
  * Trashing content now



### Identify and opt out content from scheduled trashing

Users are automatically alerted by email when a piece of content that they own is scheduled for trashing by an admin.

**Tip:** Users can also identify when content that they own has been scheduled for trashing by viewing the **Scheduled for trashing** tab. In addition to content that they own, users can also view and opt out any content from trashing that they have [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access to.

The email that users receive lists the following criteria in a table:

  * The name of the content, and a link to the content in Looker.
  * The type of content (Look or dashboard).
  * The content owner (admins can send notification emails to more users than just the content owner).
  * The number of days since the content was last used.
  * The number of days until the content will be moved to the trash.
  * The **Review** link to navigate to the **Scheduled for trashing** tab in the **Unused content** folder, where the owner can opt the content out from trashing.



To opt a piece of content out from scheduled trashing, follow these steps:

  1. Navigate to the **Unused content** folder and open the **Scheduled for trashing** tab. Alternatively, click the **Review** link in the notification email to open **Scheduled for trashing** tab.
  2. If viewing the content as a list, select pieces of content by clicking the checkbox inline with the content name, or select content in bulk by clicking the box inline with the **Name** subheader. Click the inline checkbox again to deselect a piece of content, or deselect all selected content by clicking the box inline with the **Name** subheader.

**Note:** You can only bulk select 30 pieces of content at once, per type of content. For example, you can only cancel a scheduled trashing for up to 30 dashboards, or 30 Looks. Looks and dashboards must be opted out from scheduled trashings separately, in their individual sections.

If you are viewing the content as a grid, you cannot select content in bulk. You can select dashboards or Looks by placing your cursor over the content thumbnail and clicking the **Select** checkbox.

You can click the grid_view **Show items in a grid** or vertical_split **Show items in a list** icon to switch between list view or grid view.

  3. Once the content is selected, click **Restore content** to open the **Restore content?** dialog.

  4. Click **Restore content** to confirm, or **Cancel** to cancel.




The content that is restored will be removed from the **Unused content** folder, and will be ineligible for trash scheduling for 90 days.

### Trashing content now

In addition to opting content out of scheduled trashing, users can also choose to immediately trash content that they own, or to trash content to which they have [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access.

To trash content now, follow these steps:

  1. Navigate to the **Unused content** folder and open either the **Unused content** tab or the **Scheduled for trashing** tab.
  2. If viewing content on the **Unused content** tab, choose a timeframe from the **Time since last use (days)** selector. The default selection is 90 days.
  3. If viewing the content as a list, select pieces of content by clicking the checkbox inline with the content name, or select content in bulk by clicking the box inline with the **Name** subheader. Click the inline checkbox again to deselect a piece of content, or deselect all selected content by clicking the box inline with the **Name** subheader.

**Note:** You can only bulk trash 30 pieces of content, per type of content, at one time. For example, one trashing can only include up to 30 dashboards, or 30 Looks. Looks and dashboards must be trashed separately, in their individual sections.

If you are viewing the content as a grid, you cannot select content in bulk. You can select dashboards or Looks by placing your cursor over the content thumbnail and clicking the **Select** checkbox.

You can click the grid_view **Show items in a grid** or vertical_split **Show items in a list** icon to switch between list view or grid view.

  4. Once the content is selected, click **Move to trash** to open the **Move selected items to trash** dialog.

  5. Click **Move to trash** to confirm, or **Cancel** to cancel.




Trashing content from the **Unused content** folder doesn't permanently delete the content, but moves it to the **Trash** folder. Admins can restore or permanently delete the content that has been moved to the trash from the [**Trash** folder](https://docs.cloud.google.com/looker/docs/admin-spaces#trash).

## Related resources

  * Learn more about [finding and viewing content in Looker](https://docs.cloud.google.com/looker/docs/finding-content)
  * Learn more about [organizing and managing access to content](https://docs.cloud.google.com/looker/docs/organizing-spaces)
  * Learn more about [restoring content from the **Trash** folder (for admins)](https://docs.cloud.google.com/looker/docs/admin-spaces)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
