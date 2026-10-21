---
url: https://docs.cloud.google.com/looker/docs/2612/organizing-spaces/
title: Organizing and managing access to content \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:03.920019+00:00
---

# Organizing and managing access to content  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2612/organizing-spaces/

You are viewing documentation for Looker 26.12. Click this link to see the [most recent documentation](https://docs.cloud.google.com/looker/docs/intro). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/2612/intro)



Send feedback 

#  Organizing and managing access to content Stay organized with collections  Save and categorize content based on your preferences. 

Looker stores [Looks](https://docs.cloud.google.com/looker/docs/2612/saving-and-editing-looks#saving_looks_from_an_explore) (saved visualized query results) and [dashboards](https://docs.cloud.google.com/looker/docs/2612/viewing-dashboards) (collections of tiles that show visualized query results) in folders. Access to these folders is controlled by access levels and user permissions.

**Important:** Be careful when organizing folders. Changes can affect all users who have access to each folder, including your personal folder if other users have access to Looks and dashboards from your folder.

## Folder access levels

A [user](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-users) or a [group of users](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-groups) can have one of two access levels for a folder:

  * **View** : The user or group can see the folder, view the Looks and dashboards inside it, and copy the Looks and dashboards in the folder.

  * **Manage Access, Edit** : The user or group has **View** access and can also manage access to the folder and edit the folder and its content (including renaming folders, moving content, and deleting Looks and dashboards).




For more information about content access and permissions, see [Controlling user content access](https://docs.cloud.google.com/looker/docs/2612/access-control-and-permission-management#controlling_user_content_access) and [How content access and permissions interact](https://docs.cloud.google.com/looker/docs/2612/access-control-and-permission-management#how_content_access_and_permissions_interact).

## Viewing and managing folder access levels

To manage a folder, you need both the appropriate [permissions](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-roles#permissions_list) from your Looker admin and the **Manage Access, Edit** access level for that folder. This lets you edit the name of a folder, create subfolders, and specify which users can view or manage the folder.

  1. Navigate to the folder.

  2. Click the **Toggle Dropdown** gear icon settings.

  3. Select **Manage Access**.

If you are _not_ allowed to change access levels, you cannot manage the folder. The permissions levels won't be selectable, and there won't be an option to add a new group or user.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-folder-manage-access-view-only-2216.png)

  4. If a text field with the placeholder text **Add group or user** appears after the other groups and users, then you can manage the folder.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-folder-add-group-or-user-2216.png)

  5. If the folder is a subfolder, Looker shows whether this folder inherits its access-level settings from its parent.

  6. If you want to customize access-level settings for a particular set of users and groups, you can add those users and groups to a list and manage each of them individually.

     * To change the access level for a user or group, select the current access level and choose the one that you want instead. You cannot change the ability of Looker admins to manage the folder.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-manage-folder-access-718.png)

     * To remove the access level from a group or user, select the X beside the name.

     * To add one or more groups or users, select the **Add group or user** field, choose a group or user, and then select the chosen access level. Select **Add** to select an access level for the group or user.




## Creating a folder

You can create a new folder within the **Shared** folder or your personal folder. By default, a folder inherits the folder access levels of its parent.

  1. [Navigate to the parent folder](https://docs.cloud.google.com/looker/docs/2612/finding-content#navigating_to_content_in_spaces).

  2. Click the **New** button.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-folders-new-button-2220.png)

  3. Select the **Folder** option.

  4. In the **Create folder** window, enter a name for the folder.

  5. Select **Create folder**.




## Setting your default folder

By default, if your admin has enabled the [pre-built Looker homepage](https://docs.cloud.google.com/looker/docs/2612/finding-content#pre-built_homepage) option, Looker displays **Shared folders** in the left navigation. If you set a different default folder, it replaces **Shared folders** in the left navigation.

To set a different folder as your default folder:

  1. Navigate to the folder that you want to set as your default folder.

  2. Click the **Toggle Dropdown** gear icon settings.

  3. Select **Set as your default folder**.




The default folder appears in the **Folders** section of main navigation.

## Renaming, moving, or deleting a folder

You can rename, move, or delete subfolders within **Shared** or your personal folder. However, you cannot change top-level folders, such as **Shared** or your top-level personal folder, in this way.

  1. Navigate to the folder.

  2. Click the **Toggle Dropdown** gear icon settings.

  3. Select **Rename** , **Move** , or **Delete**.


**Important:** Use caution when you delete a folder. In a single action you can delete all folder content, which could include subfolders. A Looker admin _might_ be able to recover the content, but — even if this is possible — the content will be returned to the personal folders of the users who created it and not back to the folder that you deleted.

## Copying or moving Looks and dashboards

If you have the **Manage Access, Edit** access level for a folder, you can copy or move its Looks and [user-defined dashboards](https://docs.cloud.google.com/looker/docs/2612/creating-user-defined-dashboards) to another folder. You can also move a [LookML dashboard](https://docs.cloud.google.com/looker/docs/2612/building-lookml-dashboards) to another folder if you have the [`develop`](https://docs.cloud.google.com/looker/docs/2612/admin-panel-users-roles#develop) permission on the model that includes the LookML dashboard.

If a dashboard has tiles that are based on Looks, then those Looks must be in the same folder as the dashboard. If you try to move a Look that is used in a dashboard, Looker instead makes a _copy_ of the Look in the new location and keeps the Look in its original location. This ensures that your dashboard doesn't have any missing tiles. If you copy or move a dashboard to a new location, then Looker will copy or move its Looks to the new location as well.

  1. Select the checkbox for any items that you want to change. If you have the prebuilt Looker homepage enabled and are in [grid view](https://docs.cloud.google.com/looker/docs/2612/finding-content#grid_view), you can hold your pointer over a thumbnail to see the checkmark and then select it to include the Look or dashboard.

  2. Once a box is checked, select **Copy** or **Move**.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-folders-copy-move-2404.png)

  3. In the **Copy** window or **Move** window, select the name of a top-level folder on the left to navigate to it.

  4. Select a subfolder from the list, or navigate down to a subordinate subfolder. You can also enter the subfolder name into the **Filter by title** field to filter the list.

  5. Select **OK**.




### Preventing `Duplicate Dashboard` errors with LookML dashboards

LookML dashboards are uniquely identified by their model name and filename in the format `MODEL_NAME::FILE_NAME`. 

For example, the LookML dashboard defined in the `sales_overview.dashboard.lkml` file in the model called `thelook` will have the following URL:

`https://INSTANCE_URL/dashboards/thelook::sales_overview`

Because the dashboard is identified with the filename and model name, you cannot have multiple LookML dashboards with the same filename across different folders if they reference the same model file. Attempting to do so results in a `Duplicate Dashboard` error.

To manage separate environments (such as review and production) without duplicating files, use the following best practices:

  * **Use Git branches** : Instead of duplicating files into different folders for testing, use [Git branches](https://docs.cloud.google.com/looker/docs/2612/version-control-and-deploying-changes#creating_a_new_git_branch) to isolate changes. You can test your dashboard in a development branch before merging it into the production branch.
  * **Content access controls** : Use folder access levels to control which users can see or edit specific content. You can maintain a "Production" folder for verified dashboards and a "Sandbox" or "Review" folder for work in progress, but ensure that each LookML dashboard has a unique filename across your project.



## Converting Looks to query tiles

You can create a dashboard tile by linking to a saved Look (also known as a _Look-linked tile_), specifying text, or specifying [a query directly](https://docs.cloud.google.com/looker/docs/2612/creating-user-defined-dashboards#building_query_tiles_within_a_dashboard). Saving many Looks that are only needed for a single dashboard can cause clutter. To avoid this, you can convert all [tiles that are based on saved Looks](https://docs.cloud.google.com/looker/docs/2612/creating-user-defined-dashboards#look-linked_tiles) to query tiles.

Then, you can choose to delete the source Looks, if they meet the following criteria:

  * Not used in another dashboard
  * Not [marked as a favorite](https://docs.cloud.google.com/looker/docs/2612/finding-content#favorites)
  * Not [scheduled for delivery](https://docs.cloud.google.com/looker/docs/2612/scheduling)
  * Not [public](https://docs.cloud.google.com/looker/docs/2612/publishing-looks-with-public-urls#giving_public_access_to_specific_looks)



To convert Looks to query tiles, follow these steps:

  1. From [list view](https://docs.cloud.google.com/looker/docs/2612/finding-content#table_view), select one or more dashboards from your folder.

  2. Select the **Convert Looks to Tiles** button.

  3. In the **Convert All Looks to Tiles** dialog, you can select the checkbox to move Looks to the trash and then hover over the link to see the list of Looks that are identified for deletion.

Looker shows this link _only_ if there are Looks that can be deleted safely, such as those that are not scheduled for data delivery, not used in other dashboards, not favorited, or not public.

  4. To prevent Looker from deleting the source Looks, make sure that the checkbox is not selected. Looker will keep all the Looks for now. You can [delete the Looks manually](https://docs.cloud.google.com/looker/docs/2612/organizing-spaces#deleting_looks_and_dashboards) later to clean up your folders.

  5. Select **Convert** to convert all the dashboard's Look-linked tiles to query tiles.




Looker replaces each Look-linked tile with a new query tile that uses the same query and visualization settings as the original Look. If you opted to move Looks to the trash, those converted Looks no longer appear in folders.

> If you later realize that you need a deleted Look, your Looker admin _might_ be able to recover it for you, if your Looker admin team has not already emptied Looker's trash as part of their maintenance process.

## Deleting Looks and dashboards

If you have the **Manage Access, Edit** access level for a folder, you can delete its Looks and dashboards.

  1. Select the checkbox for each Look or dashboard that you want to delete.
  2. Click **Move to Trash**.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-folders-move-to-trash-2308.png)

  3. In the confirmation window, click **OK**.

If you delete a Look that is the source for a [dashboard](https://docs.cloud.google.com/looker/docs/2612/creating-user-defined-dashboards#adding_look-linked_tiles_from_a_look) tile, the dashboard's Look-linked tile returns an **Element not found** error.

For dashboards, the confirmation window may show an option to **Move an additional X Looks associated with the above Dashboards to the trash**.

When the option is selected, **Move an additional X Looks associated with the above Dashboards to the trash** deletes any Looks that are associated with the dashboard. However, Looker only deletes those Looks they aren't scheduled for data delivery, used in other dashboards, favorited, or public. Hover over the link at the bottom of the confirmation window to see the list of Looks that are identified for deletion.

If you don't see the **Move an additional X Looks associated with the above Dashboards to the trash** option, Looker hasn't identified any Looks that can be deleted safely.


**Note:** If you accidentally delete content, your Looker admin _might_ be able to recover it for you, if your Looker admin team has not already emptied Looker's [trash](https://docs.cloud.google.com/looker/docs/2612/admin-spaces#trash) as part of their maintenance process.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
