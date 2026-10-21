---
url: https://docs.cloud.google.com/data-studio/organize-assets-with-folders-in-team-workspaces/
title: Organize assets with folders in team workspaces \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:15.033983+00:00
---

# Organize assets with folders in team workspaces  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/organize-assets-with-folders-in-team-workspaces/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Organize assets with folders in team workspaces Stay organized with collections  Save and categorize content based on your preferences. 

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

Users can use folders and subfolders to organize assets (reports and data sources) in [team workspaces](https://docs.cloud.google.com/data-studio/about-team-workspaces). User roles in folders are inherited from the team workspace level. See the Roles and permissions article to learn more about [team workspace folders roles and permissions](https://docs.cloud.google.com/data-studio/roles-and-permissions).

To use folders in team workspaces, you'll need the following requirements:

  * Your organization must purchase Data Studio Pro.
  * Your organization's Google Cloud administrator must [link Data Studio to a Google Cloud project](https://docs.cloud.google.com/data-studio/link-looker-studio-pro-to-a-google-cloud-project-mau-version).
  * At least one team workspace



Once your organization has purchased Data Studio Pro and linked a Google Cloud project, you will be able to access existing team workspaces and folders from the left navigation. For instructions for creating a new team workspace in a project that you belong to, see the [Create, edit, and delete team workspaces](https://docs.cloud.google.com/data-studio/create-edit-and-delete-team-workspaces) article.

This page provides an overview of folders in team spaces, including how to do the following:

  * View assets in folders
  * Create a folder
  * Manage assets in folders
  * Rename a folder
  * Delete a folder



## View assets in folders

To access an existing team workspace and its folders, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)

![A user selects the Sales workspace in the datastudio-preprod-default project to access a list of folders called Q1 revenue reports, Q2 revenue reports, and Q3 revenue reports.](https://docs.cloud.google.com/static/data-studio/images/access-folders.png)

  2. In the left navigation, expand the listing for your project, or click the project ID to open the content list.

  3. From the list, choose the existing team workspace that you want to access.

  4. Click a folder name from the folder list to open the folder.




Once you are in a folder, you can view assets and navigate to any additional subfolders by clicking the asset or subfolder's name.

You can also edit assets and folders by using the available options in a folder or asset's inline more_vert **More options** menu. The options available depend on your [user role](https://docs.cloud.google.com/data-studio/roles-and-permissions) in a team workspace. Options can include the following:

  * Rename a folder
  * Delete a folder
  * [Share an asset](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports)
  * [Rename an asset](https://docs.cloud.google.com/data-studio/rename-reports-data-sources-and-blends)
  * Move an asset
  * Remove an asset

**Note:** If an asset in a team workspace or folder is shared with a user who is not a member of that team workspace, the asset will be displayed in the **Shared with me** section of the left navigation.

### Navigate in folders

Folders can be nested in team workspaces. The name of the folder that you're in will be displayed in the main page navigation header.

To navigate back to a folder or a team workspace from a subfolder, click the more_horiz breadcrumb icon and choose a folder or root team workspace from the drop-down menu.

![The Sales workspace and Q1 revenue reports folders are displayed in the March revenue navigation drop down menu.](https://docs.cloud.google.com/static/data-studio/images/looker-studio-folders-navigation.png)

You can also click the folder or workspace name in the main page navigation header to access several options. The options available depend on your [user role](https://docs.cloud.google.com/data-studio/roles-and-permissions) in a team workspace. Options can include the following:

  * Create a new team folder
  * [Create a new report](https://docs.cloud.google.com/data-studio/create-a-report)
  * [Create a new data source](https://docs.cloud.google.com/data-studio/create-and-manage-data-sets)
  * Rename the folder
  * View Trash for the folder
  * Delete folder



### Change how subfolders and assets are displayed

By default, folders and assets inside of folders are organized according to when they were last opened by you. You can choose to display assets, folders, and subfolders in the following ways:

  * **Alpha-numerically** : Select the **Name** column heading to sort folders and assets by name.
  * **Temporally:** Select the **Last opened by me** drop-down menu in the main page navigation header to view assets and folders by specific events. Options include when assets or folders were last opened by you, when they were last modified, when they were last modified by you, or when they were created.



You can also choose whether to display the reports or the data sources that are referenced in reports by clicking the **Reports** or **Data sources** tabs in the main page navigation header.

**Note:** Folders and assets will always be grouped separately. Folders will be organized and sorted together at the top of the page. Reports and data sources will be organized and sorted together at the bottom of the page.

## Create a folder

**Important:** Folders can only be nested five levels deep.

To create a folder or a subfolder, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. In the left navigation, expand the listing for your project, or click the project name to open the content list.
  3. From the list, choose the existing team workspace where you want to create a folder.
  4. Select ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** , and then choose **Team folder** from the drop-down menu. Alternatively, select the name of the workspace or folder and select **Create new team folder** from the drop-down menu. 
     * If you would like to create a subfolder in an existing folder, choose the existing folder from the list of folders in the team workspace and click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create**.
     * You can also choose an existing folder by selecting the edit pencil icon in the **Create in** section of the ![](https://data-studio/mages/rainbow-plus-2019-06-26.png)**Create** menu.
     * Alternatively, if you are in an existing folder, you can click the name of the folder in the main page navigation header and select **Create new team folder** from the drop-down menu.
  5. In the **New team folder** window, enter a name for your team folder.
  6. Once you have entered a name for the folder, select **Create**.



## Manage assets in folders

**Important:** Folders cannot be moved.

Once you have created a folder in a team workspace, you can move assets into the folder or remove assets from the folder.

The role a user is assigned In a team workspace determines how they can manage assets in folders. Not all roles can perform all actions. See the Roles and permissions article to learn more about [team workspace folders roles and permissions](https://docs.cloud.google.com/data-studio/roles-and-permissions).

### Move a single asset to a folder

To move an asset to a team workspace or to a folder in a team workspace, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Navigate to the **Data Sources** or **Reports** tab in a team workspace or folder, or on the home page list.
  3. Locate the data source or report that you want to move.
  4. Hold your cursor over the data source name. Then, on the right, click the more_vert **More options** icon.
  5. Click **Move to**.
  6. Select the location where you would like to move the asset.
  7. Review any permission changes in the pop up.

**Important:** If you move an asset from the home page list to a team workspace, or from an existing team workspace to a new team workspace, the user access to the asset may change.
  8. Click **Move.**




The location of the asset will be displayed on the home page list in the **Location** column.

### Move multiple assets to a folder

To move multiple assets to a team workspace or to a folder in a team workspace, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. Navigate to the **Data Sources** or **Reports** tab in a team workspace or folder, or on the home page list.

  3. Locate the data sources or reports that you want to move.

  4. To select multiple adjacent assets, hold down the Shift key and click the data sources or reports.

**Tip:** To select multiple non-adjacent assets, hold down the Ctrl key (PC) or the command key (Mac) and click the data sources or reports.
  5. Underneath the **Search Data Studio** search bar, click the logout **Move selected items** icon.

  6. Select the location where you would like to move the assets.

**Important:** If you move assets from the home page list to a team workspace, or from an existing team workspace to a new team workspace, the user access to the assets may change.
  7. In the **Move items** dialog, click **Confirm** to move the assets to the selected folder.




The location of the assets will be displayed on the home page list in the **Location** column.

### Remove a single asset from a folder to the Trash

To remove an asset in a folder to the Trash, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Navigate to the **Data Sources** or **Reports** tab in a team workspace or a folder in a team workspace.
  3. Locate the asset that you want to remove.
  4. Hold your cursor over the data source name. Then, on the right, click the more_vert **More options** icon.
  5. Click **Remove**.



### Remove multiple assets from a folder to the Trash

To remove multiple assets from a folder to the Trash, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)

  2. Navigate to the **Data Sources** or **Reports** tab in a team workspace or a folder in a team workspace.

  3. Locate the data sources or reports that you want to move.

  4. To select multiple adjacent assets, hold down the Shift key and click the data sources or reports.

**Tip:** To select multiple non-adjacent assets, hold down the Ctrl key (PC) or the command key (Mac) and click the data sources or reports.
  5. Underneath the **Search Data Studio** search bar, click the delete **Remove selected items** icon.

  6. In the **Move items to the trash?** dialog, click **Confirm** to move the data sources to the Trash.




### View removed assets

You can view the specific assets that were removed from a workspace or workspace folder. To view the Trash for a specific folder or workspace, follow these steps:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Navigate to a team workspace or a folder in a team workspace.
  3. Click the name of the folder or workspace in the main page navigation header.
  4. Click **View Trash** from the drop-down menu.



You can restore trashed assets from the Trash, or permanently delete assets from the Trash, if you have the appropriate role.

See the [Delete a data source](https://docs.cloud.google.com/data-studio/delete-a-data-source) page for more information about restoring and permanently deleting data sources.

See the [Delete a report](https://docs.cloud.google.com/data-studio/delete-a-report) page for more information about restoring and permanently deleting reports.

## Rename a folder

Users with the [appropriate role](https://docs.cloud.google.com/data-studio/roles-and-permissions) can rename folders in team workspaces.

If you don't have the appropriate role, you will be unable to select the option to rename a folder.

To rename a folder, follow these steps:

  1. If you are viewing a folder from a list of folders, hold your cursor over the folder name, and click the folder's three dot more_vert **More options** icon.

  2. Choose **Rename.**

Alternatively, if you are in an existing folder, click the name of the folder in the main page navigation header, and click **Rename** from the drop-down menu.

  3. In the **Rename team folder** window, enter a new name for your folder.

  4. Once you have entered a name for the folder, select **Update**.




## Delete a folder

**Important:** Folders must be empty before they can be deleted. Deletion of a folder is permanent and cannot be undone.

Folders can only be permanently deleted.

Users with the [appropriate role](https://docs.cloud.google.com/data-studio/roles-and-permissions) can delete a folder. If you do not have the appropriate role, you will be unable to select the option to delete a folder.

When you delete a folder or subfolder, the folder permanently disappears for everyone. Deletion of a folder cannot be undone.

To delete a folder from a list of folders, follow these steps:

  1. Hold your cursor over the folder name, and click the more_vert **More options** icon.
  2. Choose **Delete**.



To delete a folder from inside the folder, follow these steps:

  1. Click the name of the folder in the main page navigation header, and click **Delete folder** from the drop-down menu.
  2. To confirm that you want to delete the folder, select the **Delete folder** option in the pop up.



## Things to know

  * Folders can only be nested five levels deep.
  * Folders cannot be moved.
  * If you move an asset from the home page list to a team workspace, or from an existing team workspace to a new team workspace, the user access to the asset may change.
  * Folders must be empty before they can be deleted.
  * Deletion of a folder is permanent and cannot be undone.



## Related resources

  * [About team workspaces](https://docs.cloud.google.com/data-studio/about-team-workspaces)
  * [Create, edit, and delete team workspaces](https://docs.cloud.google.com/data-studio/create-edit-and-delete-team-workspaces)
  * [Roles and permissions](https://docs.cloud.google.com/data-studio/roles-and-permissions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
