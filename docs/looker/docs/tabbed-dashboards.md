---
url: https://docs.cloud.google.com/looker/docs/tabbed-dashboards/
title: Adding tabs to dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:35.762708+00:00
---

# Adding tabs to dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/tabbed-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Adding tabs to dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Dashboard tabs let you do the following:

  * **Better organize content:** Group related visualizations and tiles into separate tabs.
  * **Improve data storytelling:** Guide viewers through different aspects of your data in a structured way.
  * **Enhance performance:** Load only the tiles on an active tab, potentially speeding up initial dashboard load times.
  * **Reduce clutter:** Consolidate multiple related analyses into a single dashboard.



![ ](https://docs.cloud.google.com/static/looker/docs/images/looker-tabbed-dashboard-example.png)

This page includes the following sections:

  * User and instance requirements
  * Limitations
  * Tabbed dashboards features for admins
  * Tabbed dashboards features for developers
  * Tabbed dashboards features dashboard creators
  * Tabbed dashboards features for dashboard viewers
  * Related resources



## User and instance requirements

To add tabs to dashboards, you must meet the following requirements:

  * Your Looker instance must be running Looker 26.4 or later.
  * You must have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) to set a **Maximum Dashboard Tabs** limit for your Looker instance.
  * To make permanent changes to dashboards that all users will see, you must have the following access level and permissions:

    * The [**Manage Access, Edit** access level](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) for the dashboard
    * The [`save_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_dashboards) Looker permission to edit the dashboard
  * To view dashboard tab metrics in Looker's **Dashboard** System Activity Explore, you must have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) or the [`see_system_activity`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_system_activity) permission.

**Important:** The **Dashboard** System Activity Explore only displays metrics such as the number of dashboard tabs and the dashboards that they appear on. The **Dashboard** System Activity Explore doesn't display metrics such as tab views.
  * To view dashboards, you must have the following access levels and permissions:

    * The [**View**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access level for the folder in which the dashboard resides
    * The [`see_user_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_user_dashboards) Looker permission

Additionally, to view a specific dashboard tile, you must have [access to the model](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) that the tile is based on.

  * Optionally, users must also have the [appropriate permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) to send, schedule, and download dashboards.

  * Optionally, users must also have [**Manage Access, Edit** access to a board](https://docs.cloud.google.com/looker/docs/presenting-content#board_access_levels) to add tab views to a board (available starting in Looker version 26.8).




## Limitations

Dashboard tabs have the following limitations:

  * The default maximum number of tabs is 5. Admins can set a different maximum number of tabs on the [**Content Guardrails** Admin page](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#maximum-dashboard-tab-limit).

**Note:** For performance speed, downloading speed, and scheduling considerations, we recommend that you use 10 or fewer tabs with a limit of 20 tiles per tab.
  * Tiles on a tab will only start loading if a user clicks on the tab. For example, if a dashboard has 3 tabs and a user clicks the first and second tab, the tiles on those tabs will start loading. No tiles on tab 3 will load. Queries execute and queue in the order of the interaction. The [per-user query limit](https://docs.cloud.google.com/looker/docs/admin-panel-database-queries#query_timeouts_and_queueing) still applies.

  * You cannot control user access to specific tabs.

  * You cannot specify different themes for different tabs.

  * You can download or schedule an individual tab beginning in Looker 26.8.


**Important:** If you encounter the error `This dashboard uses layouts that are not supported for dashboards with tabs. Learn more about updating to a supported layout`, see the [Troubleshooting unsupported layout errors for dashboards](https://docs.cloud.google.com/looker/docs/best-practices/troubleshooting-unsupported-dashboard-layout) page for a step-by-step resolution guide.

## Tabbed dashboard features for admins

Admins can access the following features for managing and monitoring dashboard tabs:

  * Set a **Maximum Dashboard Tabs** limit
  * Monitor dashboard tab usage with System Activity



### Set a Maximum Dashboard Tabs limit

Looker admins can choose to [set a **Maximum Dashboard Tabs** limit](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#maximum-dashboard-tab-limit) instance-wide.

To set a **Maximum Dashboard Tabs** limit for your instance, follow these steps:

  1. In Looker, click the **Admin** option in the [main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu).
  2. Select the **Content Guardrails** option under the **Performance** section to open the [**Content Guardrails** page](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails).
  3. Enter a number into the **Maximum Dashboard Tabs** field to set a number of maximum tabs, or use the up and down arrows to set a number.

**Note:** For performance speed, downloading speed, and scheduling considerations, we recommend that you use 10 or fewer tabs with a limit of 20 tiles per tab.
  4. Click **Save** to save the setting.




### Monitor dashboard tab usage with System Activity

If your Looker instance is running Looker 26.8 or later, and you have the appropriate permissions you can monitor dashboard tab usage with **Dashboard Tabs** metrics on the **Dashboard** System Activity Explore.
    
    
    Important: The **Dashboard** System Activity Explore only displays metrics such as the number of dashboard tabs and the dashboards that they appear on. The **Dashboard** System Activity Explore doesn't display metrics such as tab views.
    

Learn more about using the [**Dashboard** System Activity Explore](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#dashboard) to monitor dashboard usage.

## Tabbed dashboard features for developers

If you have the [`see_lookml_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_lookml_dashboards) and [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) permissions, as well as [access to the LookML models](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) for any data that you want to use, you can use the [`tabs`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#tabs) parameter in conjunction with the [`tab_name`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#tab_name) parameter to add tabs to LookML dashboards. You can also [add buttons](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-button) with navigation to tabs.

**Important:** Tabbed dashboards are supported only for the [`newspaper` dashboard layout method](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#layout).

See the [LookML dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard) page for more information about adding tabs to LookML dashboards.

## Tabbed dashboard features for dashboard creators

Dashboard creators who have appropriate access and permissions have the following option for adding tabs to dashboards:

  * Add tabs
  * Delete tabs
  * Duplicate tabs
  * Edit tabs
  * Apply filters to tiles on different tabs
  * Add buttons with navigation to tabs
  * Move tiles to different tabs
  * Apply a quick layout
  * Apply autorefresh to tiles that are on different tabs

**Note:** Dashboard creators can also [save Explores as query tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore) to specific dashboard tabs directly from an Explore page.

### Add tabs

To add tabs to user-defined dashboards, follow these steps:

  1. Open any user-defined dashboard and [switch to edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select the **\+ Add** button in the top navigation and select the **Tabs** option.
  3. Once a tab is created, click the **Add** button in the tab to add tiles.



You can also [save a query tile to a specific dashboard tab](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore) directly from an Explore.

### Delete tabs

To delete tabs, follow these steps:

  1. Open a tabbed dashboard and [switch to edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select the three-dot menu for a tab, and then select the **Delete** option.
  3. In the **Delete tab?** dialog, click **Delete** to confirm the action, or click **Cancel** to cancel the action.



### Duplicate tabs

**Caution:** Users can't duplicate tabs in the following cases: 

  * When a dashboard has reached the tab limit
  * When duplicating a tab will exceed the [tab query tile limit](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#max-dashboard-tabs)
  * When duplicating a tab will exceed the [maximum query tiles limit](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails#max-query-tiles)



If any of these cases applies, the **Duplicate** option will be inactive, or Looker will display an error message. 

If your Looker instance is running Looker 26.8 or later, you can duplicate tabs. To duplicate a tab, follow these steps:

  1. Open a tabbed dashboard and [switch to edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select the three-dot menu for a tab, and select the **Duplicate** option.



Once you have duplicated a tab, you can edit the tab.

### Edit tabs

You can edit tabs in the following ways:

  * Rename tabs
  * Reorder tabs



#### Rename tabs

To rename a tab, follow these steps:

  1. Open a tabbed dashboard and [switch to edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Double-click the tab name and rename the tab.
  3. Press the Enter key (PC) or Return key (Mac) to save the name.

**Note:** Tab names must be unique. Blank tab names are not accepted. Failed rename attempts will revert back to the default name.



#### Reorder tabs

To change the order of tabs on a user-defined dashboard, follow these steps:

  1. Open the tabbed dashboard and [switch to edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select the three-dot menu for a tab, and select the **> Move right** or **< Move left** option.



### Apply filters to tiles on different tabs

**Important:** You must have one or more tiles on each tab, and more than one tab on a dashboard. If a filter is not applied to _any_ tile on a specific tab, then the filter will be hidden for that tab.

To apply dashboard-level filters to dashboard tiles that are on different tabs, follow these steps:

  1. Open a tabbed dashboard and [switch to edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select the **Filters** button in the top navigation, and then select **Add Filter**.
  3. Configure the filter settings in the [Add Filter window Settings tab](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#adding_dashboard_filters).
  4. Select the [**Tiles To Update** tab](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#customizing_filter_configuration), and then select the tiles that you want to apply the filter to. If you don't want to apply the filter to a tile, select the **Do Not Filter** option from the tile's drop-down menu.

**Tip:** Starting in Looker 26.8, you can use the **All** or **None** options to globally turn a filter on or off for tiles at the dashboard level or, more granularly, at the tab level. Any tiles on a tab that are from a different Explore will be excluded from the **All** or **None** option.



### Add buttons with navigation to tabs

If your Looker instance is running Looker 26.8 or later, you can add buttons to help dashboard viewers quickly navigate to specific tabs. This can be helpful for guiding users to a tab that has additional breakdown data about a metric that is displayed on a dashboard's main tab.

Learn more about [adding buttons to dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_buttons).

### Move tiles to different tabs

To move a tile to a different tab, follow these steps:

  1. Open a tabbed dashboard and [switch to edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select the three-dot menu for a tile, and select the **Move to tab** option.
  3. Select the name of a tab to move the tile.



### Apply a quick layout

Quick layouts let you apply a cohesive tile configuration to tabs on a user-defined dashboard without the need to manually resize tiles. There are a few things to know about applying a quick layout to a dashboard with tabs:

  * You can apply a different quick layout to each tab.
  * Tile sizes change depending on the size of the dashboard.
  * Quick layout affects all tiles including text tiles, visualization tiles, Markdown tiles, and buttons.



Learn more about [quick layouts](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#quick_layout).

### Apply autorefresh to tiles that are on different tabs

To apply [autorefresh](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#autorefresh) for tiles that are on different dashboard tabs, follow these steps:

**Note:** When the **Automatically refresh dashboard** switch is turned on in the **Refresh frequency** menu, select the **Refresh every** option in the **Refresh frequency** menu to set a different refresh interval for individual tiles.

  1. Open a tabbed dashboard and [switch to edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Select the **Settings** button in the top navigation.
  3. On the **General** tab, select the **Refresh every** option from the **Refresh frequency** menu to set a refresh interval for the individual tiles on tabs.



## Tabbed dashboard features for dashboard viewers

In addition to viewing content on tabbed dashboards, dashboard viewers with appropriate permissions can interact with tabbed dashboards in the following ways:

  * Download tabbed dashboards as a PDF
  * Schedule tabbed dashboards as a PDF
  * Add a dashboard tab view to a board
  * Get dashboard links with tab context



### Download tabbed dashboards as a PDF

Starting in Looker 26.8, when you download a tabbed dashboard as a PDF, you can specify a specific tab or set of tabs to download. For earlier Looker versions, all of the tabs will appear in the same PDF. The contents of each tab will be organized under a content header with the name of the tab.

Learn more about [downloading dashboards as PDFs](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_a_pdf).

### Schedule tabbed dashboards as a PDF

Starting in Looker 26.8, when you schedule a tabbed dashboard as a PDF, you can specify a specific tab or set of tabs to schedule.

Learn more about [scheduling and sending dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards).

### Add a dashboard tab view to a board

Starting in Looker 26.8, you can add a dashboard tab view to a board. Content that is curated on boards makes it easier for users to find the information that is most relevant to them.

Learn more about [adding content to boards](https://docs.cloud.google.com/looker/docs/presenting-content#adding_looks_and_dashboards_to_a_board)

### Get dashboard links with tab context

**Note:** You must be out of edit mode to get the link for an individual tab or an entire dashboard.

To get the link for a specific dashboard tab, click a tab and copy the browser URL.

Alternatively, you can [get the entire dashboard link by selecting the **Get link** option](https://docs.cloud.google.com/looker/docs/viewing-dashboards#getting_a_dashboards_link) from the dashboard's three-dot menu.

## Related resources

  * Learn more about [creating user-defined dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards).
  * Learn how to [edit user-defined dashboards](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards).
  * Explore options for [adding and editing dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards).
  * Understand how to [view dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
