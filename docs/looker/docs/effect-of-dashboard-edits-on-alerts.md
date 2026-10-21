---
url: https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts/
title: Effect of dashboard edits on alerts \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:19.724039+00:00
---

# Effect of dashboard edits on alerts  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Effect of dashboard edits on alerts Stay organized with collections  Save and categorize content based on your preferences. 

If you have the appropriate user [permissions](https://docs.cloud.google.com/looker/docs/alerts-for-admins), you can create alerts on [query-based tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#query_tiles) or [Look-linked tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#look-linked_tiles) on [user-defined dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards) or on [LookML dashboards](https://docs.cloud.google.com/looker/docs/reference/lookml-dashboard-overview).

Each alert query captures the dashboard and tile settings at the time an alert is created; however, an alert will sync with many of the common types of changes that you or other users make to its underlying dashboard or tile without the need to recreate the alert. This documentation page discusses how these types of dashboard changes affect alerts:

  * Editing a dashboard or tile
  * Copying a dashboard
  * Deleting a dashboard
  * Checking an alert's synchronization
  * Resolving an unsynced alert



For information about editing an alert query, see the [Modifying alerts](https://docs.cloud.google.com/looker/docs/modifying-alerts) documentation page.

## Editing a dashboard or tile

Many of the changes that you or other users make to an alert's tile or dashboard synchronize to the alert settings without the need to recreate the alert. The alert captures some changes to its dashboard tile or its tile's dashboard filter. The alert may also treat changes differently depending on its tile's dashboard type.

### Editing a dashboard tile

If the tile has at least one alert on it, Looker displays a warning when you hover over the **Edit** option from the dashboard tile's [three-dot menu](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_tiles):

`Editing may affect any alerts on this tile.`

![](https://docs.cloud.google.com/static/looker/docs/images/edit-dashboard-tile-enhanced-alert-2220.png)

Looker also displays a warning inside the **Edit Tile** window:

`At least one alert is set on this dashboard tile. Editing the fields in this tile's visualization may invalidate the conditions for these alerts.`

![Looker displays the warning that editing may affect any alerts on this tile.](https://docs.cloud.google.com/static/looker/docs/images/edit-tile-enhanced-alert-2114.png)

Many of the changes that are made to a dashboard tile will be adopted by the alert on that tile. Some changes, however, may invalidate the intended meaning of the alert query and break the synchronization between the alert and the dashboard tile. See the tables on this page for lists of common dashboard tile changes and how those changes affect any alerts on that tile.

#### Editing a user-defined or LookML dashboard

This table shows whether alerts remain synchronized for each change a user may make to the tile queries on user-defined dashboards (UDD) or LookML dashboards.

**Changes to dashboard tile query** | **Does the alert remain synced to the dashboard?** | **Owner resolution**  
---|---|---  
[Removing](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#removing_fields) a dimension or [custom dimension](https://docs.cloud.google.com/looker/docs/custom-fields#viewing_and_using_custom_fields) that is used in the alert query | No | [Edit existing alert conditions.](https://docs.cloud.google.com/looker/docs/modifying-alerts)  
[Adding](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#adding_more_dimensions_for_more_detail) or [removing](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#removing_fields) a dimension or [custom dimension](https://docs.cloud.google.com/looker/docs/custom-fields#viewing_and_using_custom_fields) that is not used in the alert query | Yes |   
[Removing](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#removing_fields) a dimension of [`type: time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_time) that is used in the alert query | No | [Edit existing alert conditions.](https://docs.cloud.google.com/looker/docs/modifying-alerts)  
[Adding](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#adding_more_dimensions_for_more_detail) a measure or [custom measure](https://docs.cloud.google.com/looker/docs/custom-fields#viewing_and_using_custom_fields) | Yes |   
[Removing](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#removing_fields) a dimension, [custom dimension](https://docs.cloud.google.com/looker/docs/custom-fields#viewing_and_using_custom_fields), measure, [custom measure](https://docs.cloud.google.com/looker/docs/custom-fields#viewing_and_using_custom_fields), or [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) that is not used in the alert query | Yes |   
[Removing](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#removing_fields) a measure or [custom measure](https://docs.cloud.google.com/looker/docs/custom-fields#viewing_and_using_custom_fields) that is used in the alert query | No | [Edit existing alert conditions.](https://docs.cloud.google.com/looker/docs/modifying-alerts)  
[Editing](https://docs.cloud.google.com/looker/docs/table-calculations#editing_table_calculations) an existing table calculation that is not used in the alert query | Yes |   
[Editing](https://docs.cloud.google.com/looker/docs/table-calculations#editing_table_calculations) an existing table calculation that is used in the alert query | Yes |   
Removing a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) that is used in the alert query | No | [Edit existing alert conditions.](https://docs.cloud.google.com/looker/docs/modifying-alerts)  
Adding a [table calculation](https://docs.cloud.google.com/looker/docs/table-calculations) | Yes |   
[Hiding a dimension](https://docs.cloud.google.com/looker/docs/creating-visualizations#hiding_fields_from_visualizations) that is not used in the alert query from a visualization | Yes |   
[Hiding a dimension](https://docs.cloud.google.com/looker/docs/creating-visualizations#hiding_fields_from_visualizations) that is used in the alert query from a visualization | Yes |   
[Hiding a measure](https://docs.cloud.google.com/looker/docs/creating-visualizations#hiding_fields_from_visualizations) that is not used in the alert query from a visualization | Yes |   
[Hiding a measure](https://docs.cloud.google.com/looker/docs/creating-visualizations#hiding_fields_from_visualizations) that is used in the alert query from a visualization | Yes | [Edit existing alert conditions.](https://docs.cloud.google.com/looker/docs/modifying-alerts)  
Changing a [visualization type](https://docs.cloud.google.com/looker/docs/creating-visualizations#choosing_a_visualization_type) | Yes |   
Changing a query [filter](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#filtering_data_overview) | Yes | Although the changes will sync with the alert, the alert may be invalidated if the alert's trigger values are outside of the data values that are dictated by the updated query filters. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
Changing the [sort order](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#sorting_data) | Yes | [Edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
Changing a [pivot](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#pivoting_dimensions) (unpivot, pivot on a different field) | Yes | Although the changes will sync with the alert, the alert may be invalidated if the alert's trigger values are outside of the data values that are dictated by the updated pivots. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
Changing a [column limit](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#column_limits) | Yes | Although the changes will sync with the alert, the alert may be invalidated if the alert's trigger values are outside of the data values that are dictated by the updated column limit. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
Changing a [row limit](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#row_limits) | Yes | Although the changes will sync with the alert, the alert may be invalidated if the alert's trigger values are outside of the data values that are dictated by the updated row limit. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
Adding or removing [subtotals](https://docs.cloud.google.com/looker/docs/table-options#subtotals) | Yes |   
Adding or removing [column](https://docs.cloud.google.com/looker/docs/table-options#totals) or [row totals](https://docs.cloud.google.com/looker/docs/table-options#row_totals) | Yes |   
[Filling in](https://docs.cloud.google.com/looker/docs/creating-visualizations#filling_in_missing_dates_and_values) missing dates and values | Yes | Although the changes will sync with the alert, if the fields with missing values are timeframes, filling in those values may affect the tile query results. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
[Reordering](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#reordering_columns) fields | Yes | Although the changes will sync with the alert, if there is a row or column limit on the query, changing the order of fields in the tile query may affect the query results. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
[Reordering](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#reordering_columns) dimensions of [`type: time`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_time) or [custom dimensions](https://docs.cloud.google.com/looker/docs/custom-fields#viewing_and_using_custom_fields) | Yes | _Exception:_ If the first time dimension is different from the time dimension on which the alert is set, the alert becomes unsynced.  
  
#### Editing LookML dashboards

This table describes how changes made exclusively to LookML dashboards affect any alerts on those tiles.

**Changes to LookML dashboard tile query** | **Does the alert remain synced to the dashboard?** | **Owner resolution**  
---|---|---  
Changing [`explore`](https://docs.cloud.google.com/looker/docs/reference/param-explore) or [`model`](https://docs.cloud.google.com/looker/docs/reference/param-model) parameters (but keeping the same LookML dashboard ID, `model::dashboardname`) | No | 

  * If you want to retain the original alert settings without undoing the LookML changes, recreate the dashboard element with the original `explore` or `model` parameter configuration. Then recreate the alert.
  * [Create a new alert](https://docs.cloud.google.com/looker/docs/creating-alerts) that applies to the new element `model` or `explore` parameter configuration.

  
  
### Editing dashboard filters

For [user-defined dashboards](https://docs.cloud.google.com/looker/docs/dashboards), you can choose whether to sync changes that are made to dashboard filters with all alerts on the dashboard or to sync no dashboard filters changes. You cannot selectively apply changes that are made to dashboard filters to alerts on individual dashboard tiles.

To sync dashboard filter changes with all alerts on the dashboard:

  1. Click the dashboard's [three-dot menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu).
  2. Select **Edit dashboard** to enter [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards_\(beta\)).
  3. Click **Filters** in the top toolbar.
  4. Enable the **Apply filter edits to alerts** toggle.

![](https://docs.cloud.google.com/static/looker/docs/images/enhanced-alerts-apply-filters-2320.png)




> Looker won't attempt to synchronize alerts with changes that are made to LookML dashboard filters.

This table describes how changes that are made exclusively to [user-defined dashboards](https://docs.cloud.google.com/looker/docs/dashboards) affect any alerts on those tiles.

**Changes to UDD permanent filters (with alerts toggle enabled)** | **Does the alert remain synced to the dashboard?** | **User resolution**  
---|---|---  
[Adding](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#adding_dashboard_filters) or [removing](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#deleting_dashboard_filters) a dashboard filter | Yes | Although the changes will sync with the alert, updating dashboard filters may affect the query results. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
[Editing](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#editing_dashboard_filters) a dashboard filter default value | Yes | Although the changes will sync with the alert, updating dashboard filters may affect the query results. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
[Editing](https://docs.cloud.google.com/looker/docs/viewing-dashboards#temporarily_changing_filter_values_on_dashboards) a dashboard filter's temporary value | No | Although the changes will sync with the alert, updating dashboard filters may affect the query results. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
[Editing](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#editing_dashboard_filters) the fields that a dashboard filter applies to | Yes | Although the changes will sync with the alert, updating dashboard filters may affect the query results. You may need to [edit the alert trigger values](https://docs.cloud.google.com/looker/docs/modifying-alerts) to account for a new range of data values.  
  
## Copying a dashboard

Making a copy of a dashboard does not copy any enhanced alerts on that dashboard.

## Deleting a dashboard

Deleting a dashboard immediately disables any alerts on that dashboard. Any followers or recipients will no longer receive notifications when the alert conditions are met.

The alert owner will see immediately that the name of the dashboard has been deleted for the alert on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts). After the next time the alert query runs, the alert status will show as **Disabled**.

## Checking an alert's synchronization status

You can view the synchronization status of your alert on the **Alert Details** page, available from the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts#alert_details_page). If you're a Looker admin, the **Alert Details** page is also available from the [**Alerts** management page](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts#alert_details_page).

The synchronization status is displayed on the bottom left of the page:

  * A green encircled check mark indicates that the alert is still synced to its dashboard.
  * A yellow triangular warning symbol indicates that the alert has become unsynced from its dashboard. The status includes a timestamp of when the synchronization was broken. An unsynced alert displays a **None** value in the **Dashboard** column of the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts) or the [**Alerts** admin management page](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts).



## Resolving an unsynced alert

Even if an alert becomes unsynced from its dashboard, Looker will continue to run alert queries to check the dashboard tile data for the alert conditions. Results of these queries will be displayed in the alert's history, viewable on the **Alert Details** page on the alert management pages for [alert owners](https://docs.cloud.google.com/looker/docs/user-alerts#alert_details_page) and [admins](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alerts#alert_details_page) and on the [**Alerts History**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-alert-history) admin page. However, depending on the reason for the synchronization breakage, it might not be possible for alert conditions to be met.

If an alert that you own has become unsynced from its dashboard, you may need to resolve the behavior by:

  * Editing the original alert conditions
  * Editing the original alert threshold values
  * Recreating the tile's original query and any desired filters



To edit an alert, see the [Modifying alerts](https://docs.cloud.google.com/looker/docs/modifying-alerts) documentation page.

To recreate the tile query:

  1. Click the **Explore from here** option from the visualization three-dot menu on the **Alert Details** page.
  2. Recreate the original query.
  3. Click the Explore gear icon and select **Save** on the gear menu and then **To existing dashboard** on the submenu to [add the query](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore) to the appropriate dashboard.
  4. On the dashboard, [apply dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#adding_dashboard_filters) to the tile as needed.
  5. [Set a new alert](https://docs.cloud.google.com/looker/docs/creating-alerts) on that dashboard tile.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
