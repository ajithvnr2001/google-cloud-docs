---
url: https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards/
title: Editing user-defined dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:36.455998+00:00
---

# Editing user-defined dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Editing user-defined dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Edit your Looker user-defined dashboards to refine data visualizations and provide clear, relevant information for your operational workflows. You can tailor their content, layout, and display settings to optimize how data is presented and consumed.

To edit a dashboard, you must have the following prerequisites:

  * The [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access level for the folder in which the dashboard resides
  * The appropriate [Looker permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_content) to edit the dashboard



Additionally, to edit a specific dashboard tile, you must have [access to the model](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) that the tile is based on.

If you don't have access to all the models that a particular dashboard's tiles are based on, you can still edit other parts of the dashboard, such as the dashboard title, dashboard settings, [dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#editing_dashboard_filters) (although you won't see filter suggestions for filters based on fields in a model you don't have access to), and tiles for which you do have model access.

When editing a dashboard, keep in mind best practices for dashboard construction. Find information and recommendations about building performant dashboards in the [Considerations when building performant Looker dashboards](https://docs.cloud.google.com/looker/docs/best-practices/considerations-when-building-performant-dashboards) Best Practices page.

## Entering edit mode in dashboards

To enter edit mode, select **Edit dashboard** from the three-dot **Dashboard actions** menu.

In edit mode, you can add, [resize and reposition](https://docs.cloud.google.com/looker/docs/rearranging_and_resizing_tiles), edit, or delete tiles, filters, or [dashboard tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards). You can also edit the dashboard title.

**Important:** If you edit a [dashboard with tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards), every filter will appear on every tab in edit mode. Once you exit edit mode, a filter will only appear on a tab if it is applied to at least one tile on that tab.

When you are in edit mode, Looker displays a blue toolbar at the top of the dashboard that contains the following options:

  * **Add**
  * [**Filters**](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards)
  * **Settings**
  * **Quick layout**
  * **Style** (Available only if your Looker admin has enabled the [**Internal Dashboard Theming** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#internal_dashboard_theming).)
  * **Cancel**
  * **Save**



![](https://docs.cloud.google.com/static/looker/docs/images/dboards-editing-2400.png)

After you make at least one edit, the **Save** button becomes available. Click **Save** to save your edits and exit edit mode.

To discard your edits, click **Cancel**. In the **Discard changes?** dialog, click **Discard** to confirm that you want to cancel and exit edit mode. The **Discard changes?** dialog also appears if you attempt to navigate away from the dashboard by clicking on the [navigation breadcrumb](https://docs.cloud.google.com/looker/docs/viewing-dashboards#navigation_breadcrumb) or the forward or back arrows on your browser.

For more information about moving a dashboard filter, see the [Adding and editing user-defined dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#moving_and_repositioning_dashboard_filters) documentation page.

For information about adding and configuring filters directly on individual visualization tiles, see the [Filters on visualization tiles](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#filters-on-visualization-tiles) documentation.

## Rearranging and resizing tiles

In edit mode, you can move and resize tiles on a dashboard.

To move a tile, drag the six-dot icon in the upper left of a tile. When you drag a tile to a new location on the dashboard, blue grid lines appear to help you position the tile. Looker displays the width and height of each tile, as well as the percentage of the total dashboard width that is occupied by the tile.

You can also use the **Move tile** option in the tile's edit menu to move the tile to the top or the bottom of the dashboard. If your dashboard has tabs, you can also use the [**Move to tab**](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#move-tiles) option in the tile's edit menu to move the tile to a different tab.

To resize a tile, either drag the bottom right corner of the tile or use the **Resize tile** option in the three-dot **Tile actions** menu at the top right of each tile. The available preselected sizes are as follows:

  * **Extra small** — Each tile takes up one-sixth of the dashboard row.
  * **Small** — Each tile takes up one-fourth of the dashboard row.
  * **Medium** — Each tile takes up one-third of the dashboard row.
  * **Large** — Each tile takes up one-half of the dashboard row.
  * **Extra Large** — Each tile takes up the entire width of the dashboard row.



Only the selected tile is resized. Tile sizes are responsive to the size of the dashboard.

If you want to resize a tile to be very short, hiding the tile title can help you make the tile as short as possible.

### Tile size and grid layout

When you add a visualization using [grid layout](https://docs.cloud.google.com/looker/docs/column-options#grid_layout) to a dashboard, the grid arrangement can become responsive to the size of the dashboard tile.

For example, you have a dashboard tile with a visualization that uses a grid layout of four small charts. If you size the tile to be short and wide, the small charts appear as one row of four. If you size the tile as a square, the small charts reposition to two rows of two. If you size the tile to be narrow but tall, the charts reposition to four rows of one.

To ensure that the grid arrangement is responsive, do not enter a number into the visualization's [**Number of Charts per Row**](https://docs.cloud.google.com/looker/docs/column-options#grid_layout) setting. If you enter a value into **Number of Charts per Row** , the dashboard tile respects that setting regardless of the size or shape of the dashboard tile.

## Adding tiles

In edit mode, you can add tiles, tabs, or text to your dashboard. See the [Creating user-defined dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_tiles_and_text_to_a_dashboard) documentation page for information about how to add text and tiles. See the [Adding tabs to dashboards](https://docs.cloud.google.com/looker/docs/tabbed-dashboards) documentation page for information about how to add tabs to dashboards.

## Editing tiles

In edit mode, the three-dot **Tile actions** menu at the top right of each tile shows the available edit options.

These options differ slightly depending on whether or not you are viewing a [query tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#query_tiles) or a [Look-linked tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#look-linked_tiles).

  * In both cases, Looker displays the options **Edit** , **Hide title** , **Add note** , **Add accessibility description**, and **Move tile**. If your dashboard has tabs, the [**Move to tab**](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#move-tiles) option will appear. 
    * For query tiles, Looker also displays the options **Duplicate tile** , **Delete** , and **View**.
    * For Look-linked tiles, Looker also displays the option **Remove Look**.



The three-dot **Tile actions** menu also includes the [**Show Filters**](https://docs.cloud.google.com/looker/docs/viewing-dashboards#show-filters) option, which lets you view filters that are applied to the tile.

### Editing a query tile title

In edit mode, you can edit a [query tile's](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#query_tiles) title by clicking on the title and making your edits. Click **Save** at the upper right of the dashboard to save your changes.

![](https://docs.cloud.google.com/static/looker/docs/images/dboard-beta-edit-tile-title-720.png)

You can also edit tile titles for both query tiles and [Look-linked](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#look-linked_tiles) tiles when editing a tile's underlying query or Look.

### Editing a tile's query or Look

**Note:** Changes to your Look propagate to every dashboard where that Look is used.

In edit mode, you can edit a tile's underlying query or Look — including the title of the tile and the visualization — directly in the dashboard.

Click **Edit** (or **Edit Merged Query** for a [merged query tile](https://docs.cloud.google.com/looker/docs/merge-queries-new-explore)) in the tile's three-dot **Tile actions** menu.

If you're editing a Look, the **Edit Look** toolbar displays the dashboards containing tiles that are linked to that Look. Those dashboards will be affected by your changes. If you're editing a query tile, you won't see a list of dashboards that are affected in the edit pane, because your edits affect only the tile and dashboard that you are in.

![](https://docs.cloud.google.com/static/looker/docs/images/dboard-beta-tile-query-edit-720.png)

**Note:** When you're editing a dashboard tile that contains a funnel chart or a timeline chart, the charts look different on the dashboard tile than they do in the edit window. Additionally, map charts' [tooltips](https://docs.cloud.google.com/looker/docs/viewing-dashboards#drilling_into_data_points) function differently when viewed on dashboard tiles. For more information, visit the [funnel chart](https://docs.cloud.google.com/looker/docs/funnel-options#stepped_funnel_and_funnel_styles), [timeline chart](https://docs.cloud.google.com/looker/docs/timeline-options#viewing_timeline_charts_in_the_new_dashboard_experience), and [map chart](https://docs.cloud.google.com/looker/docs/map-options#viewing_map_charts_in_the_new_dashboard_experience) documentation pages.

### Adding and editing filters on a visualization tile

When the [**Filters on Visualization Tiles**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#filters-on-visualization-tiles) preview feature is enabled, you can add and configure filters directly on an individual visualization tile rather than only in the dashboard filter bar.

In edit mode, you can perform the following tasks:

  * **Add a filter to a tile** : Select the **Add vis filter** icon in the tile header, and then select **Add filter** in the dialog that appears to configure the filter field and settings. For step-by-step instructions, see [Adding a filter to a visualization tile](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#adding-a-filter-to-a-visualization-tile).
  * **Reorder filters** : Click and hold the **Hold and drag to reorder** icon in the tile filter bar, and then drag the filter to a new position in the tile filter bar.
  * **Edit or delete a filter** : Select the three-dot **Filter Menu** icon next to a filter in the tile filter bar, and then select **Edit** or **Delete**.



When you're done editing the dashboard, select **Save** in the edit dashboard toolbar to save your changes and exit edit mode.

For more information on tile-level filter behavior, precedence, and limitations, see the [Filters on visualization tiles](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#filters-on-visualization-tiles) documentation.

### Hiding or showing a tile title

In edit mode, you can hide or show the title of a tile. By default, tile titles are shown. You can hide a title by clicking **Hide title** in the tile's three-dot **Tile actions** menu.

If the title is hidden, Looker instead displays the option **Show title** in the tile's three-dot **Tile actions** menu.

The hide or show option does not appear in the three-dot **Tile actions** menu of [text tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#text_tiles) or tiles that use [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options). To hide or show the title of a single value visualization, [click **Edit**](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_a_tiles_query_or_look) in the tile's three-dot **Tile actions** menu, toggle the [**Show Title**](https://docs.cloud.google.com/looker/docs/single-value-options#show_title) switch in the style menu, and save. To hide or show a title of a text tile, [click **Edit**](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_a_tiles_query_or_look) in the tile's three-dot **Tile actions** menu, remove or reinstate the tile title, and save.

### Adding a tile note

In edit mode, click the **Add note** button in the tile's three-dot **Tile actions** menu.

Enter the note text and configure the following display options:

  1. In the **Note Text** field, enter the note text to show on the tile. You can use plain text or [HTML](https://docs.cloud.google.com/looker/docs/html-sanitization).
  2. In the **Display Location** field, select the location of the note. The options are above the visualization, below the visualization, or as text that appears when users hold their pointers over a circled _i_ icon to the right of the tile title. For tiles containing [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options) that are sized to be 150 pixels tall or shorter, title notes render as text when you hold the pointer over the **Display Location** field.
  3. Check the **Collapse note** box to collapse the note by default. A collapsed note shows only the first line, with an ellipsis at the end of the line. Unchecking this box displays the note's full text by default. If you select **On icon hover** under **Display Location** , you won't see this option.
  4. Click **Add** or **Cancel** to add the note to the tile, or cancel it.



The note appears on the tile with a collapse or an expand arrow to the left of the note. Clicking that arrow or anywhere on the note toggles between collapsed and expanded displays.

![](https://docs.cloud.google.com/static/looker/docs/images/dboard-beta-collapse-expand-note-76-v2.png)

Once you add a note to a tile, the tile's three-dot **Tile actions** menu changes to display **Edit note** instead of **Add note**. Click **Edit note** to edit or delete your note.

### Adding or editing an accessibility description

You can add a text alternative description to a visualization tile for screen readers. Adding an accessibility description makes the data and findings that are depicted in the chart accessible to screen reader users without altering the visual appearance of the dashboard.

To add or edit an accessibility description, follow these steps:

  1. In edit mode, select the tile's three-dot **Tile actions** menu and select **Add accessibility description** (or **Edit accessibility description** if a description already exists).
  2. In the **Accessibility description text** field, enter the text that screen readers should announce when users navigate to the tile.
  3. Select **Add** (or **Save**).



When someone who's using a screen reader navigates to the tile, the screen reader reads the accessibility description aloud after the screen reader reads the tile's title.

To delete an accessibility description, select **Edit accessibility description** from the tile's three-dot **Tile actions** menu, select **Delete** , and then confirm the deletion.

### Duplicating a query tile

In edit mode, you can duplicate [query tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#query_tiles) by clicking the **Duplicate tile** option from the tile's three-dot **Tile actions** menu.

Looker creates a copy of the tile with the same query and visualization settings and adds the new tile to the bottom of the dashboard. From there, you can move or resize the tile, edit the tile title, or edit the new tile to adjust the visualization or the underlying query.

**Note:** If your dashboard has tabs, you can use the [**Move to tab**](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#move-tiles) option in the three-dot **Tile actions** menu to move the duplicate tile to a different dashboard tab.

You cannot duplicate a [Look-linked tile](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#look-linked_tiles) and will not see **Duplicate tile** in the three-dot **Tile actions** menu of Look-linked tiles.

### Editing text

There are two types of text tiles, each of which offers a different editing experience but results in the same kind of tile:

  * **Text** : A dashboard text tile that provides a [visual editing experience](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_text_tiles).
  * **Markdown** : A dashboard text tile that [can be edited](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_markdown_tiles) using [some HTML](https://docs.cloud.google.com/looker/docs/html-sanitization) and [a subset](https://docs.cloud.google.com/looker/docs/using-markdown-in-text-tiles) of the Markdown markup language to format the tile.



To edit a **Text** tile, enter edit mode and click within the tile to make edits.

**Note:** If your dashboard has tabs, you can use the [**Move to tab**](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#move-tiles) option in the three-dot **Tile actions** menu to move the text tile to a different dashboard tab.

To edit a **Markdown** tile, enter edit mode and select **Edit** from the tile's three-dot **Tile actions** menu.

### Move tile options

In edit mode, you can move a tile to the top, bottom, left, or right side of the dashboard. Click the three-dot **Dashboard actions** menu, select **Move tile** , and then select one of the following options:

  * **Move to top**
  * **Move to bottom**
  * **Move to left side**
  * **Move to right side**



The tile will remain in the column or row it's located in. If the tile is already at the top, bottom left, or right side of the column, the option to move it to that spot is disabled.

**Note:** If your dashboard has tabs, you can use the [**Move to tab**](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#move-tiles) option in the three-dot **Tile actions** menu to move the tile to a different dashboard tab.

### Deleting a tile

In edit mode, you can delete a tile from a dashboard. Select **Delete** (for a query tile) or **Remove Look** (for a Look-linked tile) from the tile's three-dot **Tile actions** menu. This deletion cannot be undone.

Deleting a Look-linked tile from a dashboard does not affect the underlying Look.

## Editing dashboard settings

In edit mode, click **Settings** in the upper left of the blue toolbar to edit dashboard settings.

![](https://docs.cloud.google.com/static/looker/docs/images/dboard-beta-settings-2218.png)

From the dashboard settings page, select one of the following tabs:

  * **General**
  * **Filters**
  * **Downloads**



### Dashboard settings: General

On the **General** tab, you can update the following dashboard settings:

  * Time zone
  * Run on load
  * Allow full screen mode for visualizations
  * Preserve desktop layout
  * Automatically refresh dashboard



#### Time zone

This option is only available if your Looker admin has enabled the [**User Specific Time Zone**](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#user_specific_time_zones) setting.

Select the time zone in which your dashboard will be run. Dashboard viewers will be able to [temporarily change the time zone setting](https://docs.cloud.google.com/looker/docs/viewing-dashboards#temporarily_changing_the_dashboard_time_zone) when viewing the dashboard.

You can choose one of the following options:

  * **Each tile's time zone** to run all the tiles in the time zone in which they were saved
  * **Viewer time zone** to run all tiles in each viewer's time zone
  * Select a specific time zone from list in the drop-down menu to run all the tiles in that time zone



#### Run on load

If **Run on load** is enabled, dashboard data automatically loads when the dashboard is first loaded.

If **Run on load** is disabled, the dashboard does not display any data until the [reload data](https://docs.cloud.google.com/looker/docs/viewing-dashboards#reload_data) icon is clicked.

**Important:** For [dashboards with tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards), tiles on a tab will only start loading if a user clicks on the tab. For example, if a dashboard has three tabs and a user clicks the first and second tab, the tiles on those tabs will start loading. No tiles on the third tab will load. Queries execute and queue in the order of the interaction. The [per-user query limit](https://docs.cloud.google.com/looker/docs/admin-panel-database-queries#query_timeouts_and_queueing) still applies.

#### Allow full-screen mode for visualizations

If your Looker admin has enabled the [**Full Screen Visualizations** setting](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#full_screen_visualizations), an option for **Allow full-screen mode for visualizations** appears in the dashboard settings. This option defaults to enabled.

Disabling this option on a dashboard prevents viewers of that dashboard from seeing the [**View**](https://docs.cloud.google.com/looker/docs/viewing-dashboards#view_options) option in each dashboard tile's three-dot **Dashboard actions** menu, and viewers won't be able to see dashboard tiles in full-screen or expanded formats.

#### Preserve desktop layout

When this option is enabled, the full desktop layout of a dashboard will be preserved when users view the dashboard in a smaller browser or on a mobile screen. Users can navigate the dashboard with a zoom slider that enlarges tiles.

Users can switch between desktop and mobile view by clicking the crop_2_3 **Switch to Mobile View** button to revert to viewing the dashboard tiles in a single column, and by clicking the desktop_mac **Switch to Desktop View** button to view the dashboard in desktop layout.

#### Autorefresh

You may want to automatically refresh the data on a regular schedule to ensure that it is up-to-date. You can set autorefresh frequencies for an entire dashboard or for individual tiles. Autorefresh never pulls results from the Looker cache; it always pulls the data from the database.

To set autorefresh for a dashboard and all its tiles, follow these steps:

  1. Enable the **Automatically refresh dashboard** switch.
  2. Select a refresh frequency to automatically update the dashboard and all its tiles.
  3. To adjust the frequency for any individual tiles, do so in the **Tile** section, where each tile in the dashboard is listed. Click the drop-down for that tile in the **Refresh frequency** column, select **Refresh every** , and then set your frequency.
  4. Click **Save** to save your changes.



To set autorefresh for individual tiles but not for the dashboard, follow these steps:

**Note:** If your dashboard has tabs, you can [apply auto refresh to tiles](https://docs.cloud.google.com/looker/docs/tabbed-dashboards#apply-autorefresh) that are on different tabs.

  1. Disable the **Automatically refresh dashboard** switch (if previously enabled).
  2. In the **Refresh frequency** column of the **Tile** section, click the drop-down for a tile to autorefresh.
  3. Select **Refresh every**.
  4. Set your frequency.
  5. For any tiles that you don't want to autorefresh, leave the setting as **Does not refresh**.
  6. Click **Save** to save your changes.



The frequency settings accept whole numbers.

The autorefresh intervals begin at the time of day that you turn on this feature, and the dashboard refreshes on the interval you set as long as the dashboard is open in a browser tab and is not in edit mode. If the dashboard is closed or in edit mode during a scheduled refresh time, it won't refresh. If the dashboard is closed or goes into edit mode, regardless of whether or not it is during a scheduled refresh time, the refresh interval restarts as soon as the dashboard is opened again or leaves edit mode.

For example, if it's 8:33 AM when you set a daily refresh, the dashboard will refresh the next day at 8:33 AM and then refresh again every subsequent day at 8:33 AM. If, however, one day you enter edit mode at 9:02 AM and exit edit mode at 9:45 AM, from then on the daily refresh will occur at 9:45 AM, beginning the following day.

The [**Clear cache and refresh**](https://docs.cloud.google.com/looker/docs/viewing-dashboards#updating_data_on_dashboards_\(beta\)) and [**reload data**](https://docs.cloud.google.com/looker/docs/viewing-dashboards#reload_data) options are independent of the autorefresh interval, meaning that manually refreshing the dashboard does not restart the autorefresh interval. For example, if a dashboard's autorefresh interval is 1 hour, you can use the **Clear cache and refresh** option 40 minutes after an autorefresh and the dashboard will still autorefresh 20 minutes later (1 hour after it was last autorefreshed).

Similarly, autorefresh works regardless of whether **Run on load** is enabled or disabled. If **Run on load** is disabled and you open a dashboard with autorefresh settings, the refresh interval begins upon opening regardless of whether you click the [reload data](https://docs.cloud.google.com/looker/docs/viewing-dashboards#reload_data) icon to load the data initially.

#### Autorefresh and performance

Frequent dashboard updates, especially on large dashboards, can place a significant strain on some database systems. You may want to discuss this consideration with your Looker admin. At a minimum, avoid setting a refresh interval that is shorter than your database update interval, as there would be no new data to refresh and this would trigger unnecessary queries.

Likewise, when multiple users access a dashboard with autorefresh, it may impede performance. To display your dashboard on a shared screen while multiple users simultaneously access it, you can create two identical dashboards and configure only the dashboard on the shared screen to refresh automatically.

Find more information and recommendations about building performant dashboards in the [Considerations when building performant Looker dashboards](https://docs.cloud.google.com/looker/docs/best-practices/considerations-when-building-performant-dashboards) Best Practices page.

### Dashboard settings: Filters

On the **Filters** tab, you can update the following dashboard settings:

  * Default filters view
  * Filters location
  * Display applied filters on tiles



#### Default filters view

**Important:** If you edit a [dashboard with tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards), every filter will appear on every tab in edit mode. Once you exit edit mode, a filter will only appear on a tab if it is applied to at least one tile on that tab.

On the **Filters** tab of the **Settings** window, you can set the **Default filters view** option to one of the following:

  * **Expanded** — The filter bar shows on page load and filters are shown by default.
  * **Collapsed** — The filter bar does not show on page load and filters are hidden by default.



Click **Save** to save the change.

The **Default filters view** option defaults to **Expanded**. If you change the setting to **Collapsed** , you need to exit edit mode and then refresh the dashboard to see your change.

Dashboard viewers can temporarily change the filter bar back and forth between collapsed and expanded by clicking the [filters icon](https://docs.cloud.google.com/looker/docs/viewing-dashboards#filters_icon). However, only the **Default filters view** setting permanently changes the default state of the filter bar.

#### Filters location

**Important:** If you edit a [dashboard with tabs](https://docs.cloud.google.com/looker/docs/tabbed-dashboards), every filter will appear on every tab in edit mode. Once you exit edit mode, a filter will only appear on a tab if it is applied to at least one tile on that tab.

On the **Filters** tab of the **Settings** window, you can set the **Filters location** option to one of the following:

  * **Top** — The filter bar appears at the top of the dashboard.
  * **Right** — The filter bar appears at the right of the dashboard.



Click **Save** to save the change.

The **Filter location** option defaults to **Top**.

#### Display applied filters on tiles

When the [**Filters on Visualization Tiles**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#filters-on-visualization-tiles) or [**Filters as tiles and tile-level filter context**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#filters-as-tiles-and-tile-level-filter-context) preview feature is enabled, the **Filters** tab of the **Settings** window includes the **Tile filter information** setting to configure whether and how filters are displayed on visualization tiles.

You can set the **Tile filter information** option to one of the following:

  * **Show all** : Displays dashboard-level filters, query-level filters (configured in the underlying Explore), and visualization-level filters (if the **Filters on Visualization Tiles** preview feature is enabled).
  * **Hide query filters** (default): Displays dashboard-level filters and visualization-level filters (if the **Filters on Visualization Tiles** preview feature is enabled) only.
  * **Do not show** : Prevents the **Show Filters** option and icon from appearing on visualization tiles.



Click **Save** to save the change.

To learn more about how viewers interact with applied filters on a tile, see [Showing applied filters for a visualization tile](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#showing_applied_filters_for_a_visualization_tile).

### Dashboard settings: Downloads

On the **Downloads** tab, you can update the following dashboard settings:

  * Format
  * Results
  * Values
  * Limit



These settings become the default options when users [download data from the dashboard tiles](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_dashboard_tiles). Users who have a role that contains permissions to download data can edit these options as needed. For more information about downloading dashboards, see the [Downloading content](https://docs.cloud.google.com/looker/docs/downloading#downloading_data_from_a_dashboard) documentation page.

#### Format

In the **Format** section, select the [file format](https://docs.cloud.google.com/looker/docs/downloading#dashboard_tile_file_format) for the downloaded tile data.

You can download data from dashboard tiles in the following file formats:

  * TXT (tab-separated values)
  * Excel spreadsheet (Excel 2007 or later)
  * CSV
  * JSON
  * HTML
  * Markdown
  * PNG (image of visualization)

**Note:** PNG downloads use results from [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode). Other formats show results from whichever mode you are in when you perform the download.

#### Results

**Note:** This option is available only for certain file formats.

In the **Results** section, select how the download [displays the data results](https://docs.cloud.google.com/looker/docs/downloading#dashboard_tile_results). Select **With visualizations options applied** to set the download to include the configuration options that are applied in the tile's visualization, such as conditional formatting or custom labels. Select **As displayed in the data table** to set the download to display the data as it appears in the tile's data table.

#### Values

**Note:** This option is available only for certain file formats.

In the **Values** section, choose how you want the downloaded [data values to be formatted](https://docs.cloud.google.com/looker/docs/downloading#dashboard_tile_data_values).

#### Limit

**Note:** This option is available only for certain file formats.

In the **Limit** section, specify the [number of rows and columns](https://docs.cloud.google.com/looker/docs/downloading#number_of_rows_and_columns_to_include) to include in the data download. You can choose from the following options:

  * **Current result table** : Download only the results that are displayed in the dashboard tile.
  * **All results** : Download the entire query result set. The **All results** option is visible only to users who have a role that contains the [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permission.
  * **Custom** : Specify the default number of rows and columns to include in the data download.



## Quick layout

**Caution:** Using this feature resets the order of the tiles to the order in which they were originally added to the dashboard. Use caution as this can drastically change the layout of your dashboard.

In edit mode, click **Quick layout** in the upper left of the blue toolbar to set all tiles to the same size. The five options for tile size are as follows:

  * **XS** — Six tiles fit in a row on the dashboard.
  * **S** — Four tiles fit in a row on the dashboard.
  * **M** — Three tiles fit in a row on the dashboard.
  * **L** — Two tiles fit in a row on the dashboard.
  * **XL** — One tile fits in a row on the dashboard.



Tile sizes change depending on the size of the dashboard. Quick layout affects all tiles including text tiles, visualization tiles, Markdown tiles, and [buttons](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_buttons).

## Applying a theme to your dashboard

A theme is a set of predefined visual elements, such as background color, text color, and font family, that you can apply to your dashboard.

If your Looker admin has enabled the [**Internal Dashboard Theming** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#internal_dashboard_theming), you will see the **Style** option in the blue toolbar when you are in edit mode.

Click **Style** to open the **Style** panel and select a theme from the **Theme** field, and the theme will be applied to your dashboard. If you select **None** , and your instance has a [default theme](https://docs.cloud.google.com/looker/docs/themes-for-internal-dashboards), the default theme will be applied.

If you are a Looker admin or have the `manage_internal_themes` permission, you will see the **Manage Themes** button, which opens the **Admin > Themes** page, where you can [create and edit dashboard themes](https://docs.cloud.google.com/looker/docs/themes-for-internal-dashboards).

## Editing dashboard details

In edit mode, select **Show dashboard details** from the [three-dot **Dashboard actions** menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu). The **Description** field then becomes editable.

Once you are finished editing the description, click **Save** to save the change.

## Deleting dashboards

If you have the [**Manage Access, Edit**](https://docs.cloud.google.com/looker/docs/organizing-spaces#folder_access_levels) access level for a dashboard, you can delete it in one of two ways:

  * You can delete one or more dashboards at a time from folders, as described on the [Organizing and managing access to content](https://docs.cloud.google.com/looker/docs/organizing-spaces#deleting_looks_and_dashboards) documentation page.
  * You can delete a single dashboard by selecting [**Move to trash**](https://docs.cloud.google.com/looker/docs/viewing-dashboards#anatomy_of_a_dashboard_\(beta\)) from the dashboard's three-dot **Dashboard actions** menu.



Once you delete a dashboard, [only a Looker admin can retrieve it from the trash](https://docs.cloud.google.com/looker/docs/admin-spaces).

## Keyboard shortcuts when dashboards are in edit mode

To see the keyboard shortcuts that you can use when editing dashboards, visit the [Keyboard shortcuts in Looker](https://docs.cloud.google.com/looker/docs/keyboard-shortcuts#shortcuts_when_editing_dashboards) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
