---
url: https://docs.cloud.google.com/looker/docs/viewing-embedded-items/
title: Viewing embedded content \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:33.578383+00:00
---

# Viewing embedded content  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/viewing-embedded-items/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Viewing embedded content Stay organized with collections  Save and categorize content based on your preferences. 

With Looker embedded analytics, Looker developers can display [Looks](https://docs.cloud.google.com/looker/docs/viewing-looks), [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), [query visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations), and [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards) in any HTML-formatted web page, portal, or application. You might encounter this embedded content on a [public website](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls#public_embedding_with_iframe_tags) or [behind a login](https://docs.cloud.google.com/looker/docs/private-embedding).

Depending on the [permissions](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#permissions) that your Looker admin has assigned and the type of content that you are viewing, an embedded Look or dashboard may have options that let you interact with your data in various ways.

## Viewing embedded Looks or Explores

The following options may appear at the top right of an embedded [Look](https://docs.cloud.google.com/looker/docs/viewing-looks) or [Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_page), depending on the permissions and [content access](https://docs.cloud.google.com/looker/docs/access-levels#types_of_access_to_folders) that you have been given:

![](https://docs.cloud.google.com/static/looker/docs/images/embed-look-user-controls-2216.png)

  1. The **Time Zone** drop-down lets you change the time zone in which you view time-based data.
  2. The **Run** button lets you run or re-run the query. This is often useful after you make a change to the Look or Explore, such as selecting a different time zone. In those circumstances, the icon turns blue.
  3. The **Explore actions** gear menu shows options that let you do things such as: 
     * [Send](https://docs.cloud.google.com/looker/docs/send-once) or [schedule](https://docs.cloud.google.com/looker/docs/scheduling) a delivery of your data.
     * [Download](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_a_look_or_an_explore) your data.
     * [Edit the Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks).
     * Further [explore your data](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores).
     * Save the [Explore](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#conclusion) to a dashboard or as a Look.
     * [Merge results](https://docs.cloud.google.com/looker/docs/merged-results) from a different Explore with your current Look to create results that include both data sources.
     * [Force new results to be retrieved from the database](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#forcing_new_results_to_be_generated_from_the_database) and reload the Look or Explore results.
  4. The folder icon lets you view the folders that you have access to, along with the Looks and dashboards that they contain.



## Viewing embedded dashboards

If your Looker administrator has enabled [**Dashboard Embed Content Navigation**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#dashboard_embed_content_navigation), the following icons may appear at the top right of an embedded [dashboard](https://docs.cloud.google.com/looker/docs/viewing-dashboards), depending on the permissions and [content access](https://docs.cloud.google.com/looker/docs/access-levels#types_of_access_to_folders) that you have been given:

![](https://docs.cloud.google.com/static/looker/docs/images/embed-dashboard-user-controls-2106.png)

  1. Clicking the circular **Reload** icon [updates the data](https://docs.cloud.google.com/looker/docs/viewing-dashboards#updating_data_on_dashboards_\(beta\)) on the dashboard. Clicking this icon is often useful after filters have been changed, added, or removed. In those circumstances, the icon is encircled by a blue halo.
  2. The three-dot **Dashboard** actions menu shows availableoptions such as [editing the dashboard](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards), [downloading](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_a_dashboard) your data, [sending or scheduling](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards) a delivery of your data, [temporarily changing the dashboard time zone](https://docs.cloud.google.com/looker/docs/viewing-dashboards#temporarily_changing_the_dashboard_time_zone), or [moving the dashboard to the **Trash** folder](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#deleting_dashboards).
  3. The **Open Folders** icon lets you view the folders and the Looks and dashboards that they contain and that you have permission to view.



Looker may also display icons at the top right of each dashboard tile.

![](https://docs.cloud.google.com/static/looker/docs/images/embed-dashboard-tile-user-controls-2100.png)

  1. The bell-shaped **Alerts** icon lets you create or follow an [alert](https://docs.cloud.google.com/looker/docs/alerts-overview) on the tile. A numeric indicator will show how many alerts you are permitted to view on that tile.
  2. The three-dot **Tile actions** icon lets you interact with the data specific to that tile, so you can further [explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) the tile's data, [download](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_dashboard_tiles) the tile's data, or, in some cases, [view the Look](https://docs.cloud.google.com/looker/docs/viewing-looks) that was the source of the tile.
  3. A globe **Results are in <time zone> time zone** icon appears if the tile has a different time zone than the default dashboard time zone and your default time zone. This can only happen when your Looker admin has enabled [**User Specific Time Zones**](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#user_specific_time_zones) and the [dashboard time zone](https://docs.cloud.google.com/looker/docs/viewing-dashboards#temporarily_changing_the_dashboard_time_zone) is set to **Each tile's timezone**. Hover over the globe icon to see the time zone the tile is using.



If the embedded dashboard is in [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards) see the [Editing user-defined dashboards](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards) documentation page for options. However, some editing options may not be available in the embed environment.

## Viewing embedded query visualizations

When viewing an embedded query visualization, Looker only displays the visualization.

![](https://docs.cloud.google.com/static/looker/docs/images/embed-query-224.png)

You may be able to hover over elements in the visualization to view details, but you won't be able to interact in other ways with your data, such as further exploring or downloading your data.

## Using embedded folders to find Looks and dashboards

In Looker, folders are used to store and organize your Looks and dashboards.

### Viewing folders on embedded Looks, Explores and dashboards

Depending on your permissions and, in the case of embedded dashboards, whether your Looker admin has enabled [**Dashboard Embed Content Navigation**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#dashboard_embed_content_navigation), you may see the folders icon ( ![](https://docs.cloud.google.com/static/looker/docs/images/embed-spaces-menu-2106.png) ). Click the icon to view any folders, along with the Looks and dashboards they contain, that you have permission to view:

![](https://docs.cloud.google.com/static/looker/docs/images/embed-spaces-2314.png)

  * The **Favorites** folder shows a list of Looks or dashboards that you've [marked as favorites](https://docs.cloud.google.com/looker/docs/finding-content#marking_content_as_a_favorite).
  * The **My Folder** folder shows your personal folder, where you can store Looks or dashboards that only you can access.
  * If your Looker admin has added you to an [external group](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#groups) of users, you will see the **Group** folder. Here you can view and store content that your entire group can access.
  * The **Shared** folder shows Looks and dashboards that are available to anyone who has access to the **Shared** folder on your Looker instance.



To view any content, click the name of the Look or dashboard.

In addition to Looks and dashboards, Looker may display subfolders in your folders.

![](https://docs.cloud.google.com/static/looker/docs/images/embed-subspaces-2116.png)

Click a subfolder to navigate to it and view any content or additional subfolders stored there.

#### Copying, moving, and deleting content on embedded dashboards

If your Looker administrator has enabled [**Embed Content Management**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#embed_content_management) and you have been granted the necessary permissions, you can copy or move dashboards and Looks into different folders, or you can delete a dashboard or Look by moving it into the [Trash](https://docs.cloud.google.com/looker/docs/admin-spaces#trash) folder.

**To copy content:**

  1. Navigate to the folder that contains the dashboard or Look you want to copy, and then click the three-dot menu next to the content and select **Make a copy**.

![](https://docs.cloud.google.com/static/looker/docs/images/copy-embed-content-220.png)

Looker displays a message indicating that you are copying the selected content and the option to **Copy Here**.

![](https://docs.cloud.google.com/static/looker/docs/images/copy-here-220.png)

  2. If you want to store the copy of the selected content in the same folder as the original, click **Copy Here**.

If you want to create a copy of the content in a different folder, navigate to the folder where you want to store the copy of the content you selected, and then click **Copy Here**.

You'll see a copy of the selected content appear, using the name of the original content and the text `(copy)` appended to the content name. There is not an option to rename the copied content from within an embedded dashboard.




**To move content:**

  1. Navigate to the folder that contains the dashboard or Look that you want to copy, and then click the three-dot menu next to the content and select **Move to**.

![](https://docs.cloud.google.com/static/looker/docs/images/move-embed-content-220.png)

Looker displays a message indicating that you are moving the selected content.

![](https://docs.cloud.google.com/static/looker/docs/images/move-here-220.png)

  2. Navigate to the new folder where you want to store the content you selected, and then click **Move to**.

You'll see the selected content appear in the new folder.




**To delete content:**

  1. Navigate to the folder that contains the dashboard or Look that you want to delete, and then click the three-dot menu next to the content and select **Move to trash**.

![](https://docs.cloud.google.com/static/looker/docs/images/delete-embed-content-220.png)

You will be asked to confirm whether you want to move this content to the trash.

  2. On the confirmation screen, click **Move to trash**.




## Interacting with an embedded Look, Explore, or dashboard

The Look, Explore, or dashboard menu and the three-dot icon on dashboard tiles give you a number of options for modifying and interacting with your Look, Explore, or dashboard. You might see all, some, or none of these options, depending on the permissions your Looker admin has assigned and your access to the content you are viewing. These options include the following:

  * **Explore from Here** : Use the Look (using the Look's gear menu) or a dashboard tile (using the tile's three-dot icon) as a starting point to further explore your data. See the [Viewing and interacting with Explores in Looker](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores) and [Editing user-defined dashboards](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards) documentation pages for more information.
  * **Edit** : Change the field selections, filters, visualization options, and other attributes of a Look. For more information about editing a Look, see the [Saving and editing Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#editing_looks) documentation page.
  * **Save** > **Save As** : Save a copy of a Look to your personal folder or any other folder to which you have access. For more information, see the [Saving and editing Looks](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#saving_looks_from_an_explore) documentation page.
  * **Save** > **As a Look** : Save an Explore as a Look to your personal folder, or, if you are a member of an external group, to the **Group** folder or any other shared folder to which you have access.
  * **Save** > **To existing dashboard** : Save a Look as a dashboard tile, either on an existing dashboard or on a new dashboard that contains the Look as its initial tile. For more information, see the [Creating user-defined dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_look-linked_tiles_from_a_look) documentation page.
  * **Download** : In the case of a Look, an Explore, or a dashboard tile, download your data in one of a variety of formats. When viewing a dashboard, you are given the option to **Download as PDF** , which downloads the entire dashboard in PDF format, or **Download as CSVs** , which downloads the data in each tile as a separate CSV file. For more information, see the [Downloading content](https://docs.cloud.google.com/looker/docs/downloading) and [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards#downloading_data_from_a_dashboard) documentation pages.
  * **Send** or **Schedule** : Deliver immediate or recurring deliveries of your content to an email address or one of several other destinations in one of several formats. For more information, see the [Using the Looker Scheduler to deliver content](https://docs.cloud.google.com/looker/docs/scheduling) documentation page.
  * **Merge Results** : Combine data from a different Explore with your current Look to create results that include both data sources. For more information, see the [Merging results from different Explores](https://docs.cloud.google.com/looker/docs/merged-results) documentation page.
  * **Clear Cache and Refresh** : Refresh the data in your Look, Explore, dashboard, or dashboard tile to ensure that you are viewing the most current results.
  * **Move to Trash** : Delete the Look or dashboard from your folder. For more information, see the [Organizing and managing access to content](https://docs.cloud.google.com/looker/docs/organizing-spaces#deleting_looks_and_dashboards) documentation page.
  * **Dashboard Time Zone** : View and edit the dashboard time zone. For more information, see the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards#temporarily_changing_the_dashboard_time_zone) documentation page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
