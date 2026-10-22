---
url: https://docs.cloud.google.com/looker/docs/looker-3-release-notes/
title: 3.x Release Notes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:50.279123+00:00
---

# 3.x Release Notes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-3-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  3.x Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

> Starting in Looker 3.46, items marked with a _flash_on_ indicate changes to existing functionality that may require your attention as you update.

## Looker 3.56 2016-09-25

### _flash_on_ Looks

  * **Looks are now stand-alone documents**. Looks have been refreshed to focus on content presentation. Some things to look for include: 
    * Increased emphasis on the visualization pane
    * **A collapsable Details panel** , which exposes quick information about the Look including its description, creator, created and last updated times and scheduling and dashboard information
    * **On-Look configuration options** including scheduling, deleting, and access control
    * **An on-Look edit overly** , where the query and Look title can be modified
    * **Reset Look and Explore from Here links** , which allow users to play with the query and dig deeper without affecting others' consumption of saved content.



### Dashboards

  * **On-Dashboard Editing**. When in edit mode, users can now modify tiles directly from the dashboard.
  * Added a message on dashboards over 25 tiles informing users that performance may be impacted.
  * LookML Dashboard notes will transfer to user-defined dashboards after being converted.



### Visualizations and the Explore Page

  * _flash_on_ **Filtering on a dimension** by clicking on a value in the results data table or a table visualization now adds that dimension as a filter on the current page rather than refreshing the entire page. This disables such dimensional filtering on dashboard table visualization elements.
  * **Added an Unpin from Zero option** to allow charts to focus on the area for which data exist rather than showing the full scale starting at zero.



### LookML

  * **Introduced`${EXTENDED}`**, which allows you to refer to refer to both the object being extended and the extension object at the same time. [Learn more](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends).
  * **Renamed`SUPER*` to `EXTENDED*` for lists.** [Learn more.](https://docs.cloud.google.com/looker/docs/reusing-code-with-extends)
  * Persistent derived tables built in Development Mode will now always have a maximum `persist_for` of 24 hours. [Learn more](https://docs.cloud.google.com/looker/docs/derived-tables#persistence-in-dev-mode).
  * The LookML generator will now add a `description` parameter to freshly generated view files.



### Dialects

  * **BigQuery.** Introduced initial support for BigQuery Standard SQL. Includes support for the query size estimator and symmetric aggregates.
  * **Impala.** Added support for persistent derived tables.
  * **DataVirtuality.** Fixed an issue that could cause symmetric aggregates to generate invalid SQL.
  * **MS SQL:**
    * Fixed an issue where a field could not use more than 30 characters.
    * Introduced a static dialect (Microsoft SQL Server 2005) to connect to the deprecated 2005 version of MS SQL.
  * **Snowflake.** Fixed an issue where certain combinations of date filters incorrectly returned no results.



### Admin

  * On the Groups page, added the ability to filter on the list of users within a Group.
  * A user's page will now display the Reset Password link below the send button.
  * Groups on the Groups page are now ordered alphabetically.
  * Users on the Users page are sorted alphabetically, with null user names at the end of the list.



### General Tweaks and Bug Fixes

  * **Updated the 404 page** across Looker to reflect that the page could be a result of missing content or a lack of permissions.
  * **Updated Save, Copy, and Move dialogs** that display Space or Dashboard trees to show the Spaces a user may save to.
  * **Groups may now be set in an SSO Embed URL.**
  * Cursors will now focus on the first field any modal.
  * Fixed an issue where the Look Validator could take longer than normal to return results.
  * Disabled the "Open in Browser" option when the file format is Excel.
  * Fixed an issue where not all subSpaces would load in the Save, Copy, or Move dialog.
  * Fixed an issue where the Get Dashboard LookML explore option did not generate all dimensions and measures.
  * Improved the error message when users cannot move content into Spaces to which they don't have access.
  * Fixed a series of color picker-related issues.
  * Fixed an issue where secondary, tertiary, and further pivot sorts were not respected on the Explore page.
  * Fixed an issue where inputting text into the visualization configuration boxes could be jittery.
  * Fixed an issue where IE11.0 users could not click on the Choose Field drop-down in the dashboard filter modal.
  * Fixed an issue where `start_date` and `end_date` evaluated to null when using the "is on the day" date filter option.



## Looker 3.54 2016-08-28

### Content Management & Spaces

  * **Access Controls for Spaces** : Introduce the ability to manage who can access various Spaces and at what level. [Learn more](https://discourse.looker.com/t/introducing-access-controls-for-spaces-3-54/3243).
  * **Groups for User & Content Management**: A new Groups paradigm governs collections of users. Groups may be given access to Spaces as a unit. Groups can be set up automatically through existing authentication methods like LDAP and SAML. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups).



### Looker Design

_flash_on_ **Updates to Mobile Dashboards** for easier viewing, including:

  * Larger tile size
  * Improved filter usability
  * Updated navigation for improved screen real estate



### LookML

  * **Added new timeframes** including `second`, `millisecond`, and `microsecond`. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#timeframes).
  * Added the ability to filter on the `second` timeframe. [Learn more](https://docs.cloud.google.com/looker/docs/filter-expressions).
  * _flash_on_ The LookML Validator will now correctly warn when `order_by_field` is declared on a non-dimension field or references a measure. [Learn more](https://discourse.looker.com/t/order-by-field-can-only-be-used-with-dimensions/3268).
  * _flash_on_ Introduced a legacy feature to prevent dimensions from referencing measures. [Learn more](https://discourse.looker.com/t/why-looker-warns-when-dimensions-references-measures-and-how-to-fix-it/3259).
  * _flash_on_ The LookML Validator will now correctly warn when filter fields are declared with `type: time`. [Learn more](https://discourse.looker.com/t/type-time-should-be-used-with-dimension-groups-only/3267).



### Explore

  * **Added the ability to copy values in a column of the data table.** The copied values will be accepted into the filter input box if pasted there.
  * **Added the ability to replace field references in table calculations and custom filters with the Look Validator.** [Learn more](https://docs.cloud.google.com/looker/docs/content-validation).
  * **Filters now default to the same interval as the timeframe being filtered on.** For example, when filtering on "created_hour", the filter will default to "hours" instead of "days".
  * Descriptions for dimension groups now appear at the dimension group name level rather than repeated for each dimension. [Learn more about descriptions](https://docs.cloud.google.com/looker/docs/reference/param-field#description). [Learn more about dimension groups](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#time).



### Visualizations

  * **Added a visualization option to reverse the direction of the x- or y-axis**.
  * **Added the ability to hide totals on the table visualization**.
  * Reference lines now leverage a color picker instead of hex value inputs.
  * Charts now use the null symbol (∅) rather than the string "null".
  * Pie charts and the associated legend will now be centered as a unit instead of centering the chart itself.



### Scheduling & Downloading

  * **Resource Manager for Scheduled and Downloaded Tasks**
    * By default, the system will process downloading and rendering tasks in pairs. Instance administrators will see a new source in the query panel called "renderer".
    * These changes should result in fewer timeouts on rendered content and reduce impact on the Looker instance.



### General Tweaks and Bug Fixes

  * **Tweaks to Spaces**
    * Improved the load time of the Spaces page.
    * Improved the loading time of the Space picker in the Save, Copy and Move modals.
    * Ensured that the title of Spaces properly propagate to the browser tab.
    * Updated the styling of the Edit Space modal to match other modals.
    * Cursors now focus in the first editable field in Space modals.
  * _flash_on_ **Retired support for Internet Explorer 10.** [Learn more](https://docs.cloud.google.com/looker/docs/supported-browsers).
  * **Added a new permission to allow users to view drill overlays on dashboards without being able to explore the data.**
  * **Requesting a password reset link from the login page now offers a confirmation when the password has successfully been reset**.
  * Introduced a new keyboard shortcut (ctrl+shift+d) to enter Development Mode.
  * **Standardized the presentation of the closed Filters section on Explores and Dashboards.**
  * In the "Choose Field..." drop-down in the dashboard filter edit modal, values will now respect associated view labels.
  * Added built-in support for creating local version control.
  * **Improved the efficiency of the LookML Validator.**
  * **Improved query killing for Presto versions 0.133 and above.**
  * Added explanatory language for the Temp Database on the edit connections page.
  * Ensured that `datatype: date` fields are filtered properly in certain dialects.
  * Fixed an issue where symmetric aggregates removed newlines on most dialects.
  * Fixed a bug where validating LookML could crash an instance.
  * Fixed an issue where totals could be omitted when pivots are sorted with a column limit.
  * Fixed an issue that could result in mismatched colors between titles and text in single value visualizations.
  * Fixed an issue where default color palettes may not apply everywhere.
  * Fixed an issue where sections of the Field Picker could not be expanded or collapsed when using Firefox.
  * Fixed an issue where timeframes produced a LookML error when using `can_filter: false`.
  * Fixed an issue where LookML dashboards with text objects wouldn't download.
  * Fixed an issue where reassigning ownership of scheduled plans could cause recipients to be removed.
  * Fixed an issue where the `can_filter` parameter could allowing filtering when interacting with drilling.
  * Fixed an issue where a filter could switch to `matches (advanced)` after a query is run.
  * Fixed an issue where timezones could change on drill-down.
  * Fixed an issue where filter values were reliably removed from the filter input boxes on the explore page.
  * Fixed an issue where measure sorts could remain in the query after the measure was removed.
  * Fixed an issue where SQL did not reliably generate on the SQL tab on the Explore page.
  * Fixed an issue where a user's Space could hang if the user lacked access to certain Spaces.
  * Fixed an issue where editing filters on a dashboard copied from a deleted user's space could produce a `Validation Failed` error.



## Looker 3.52 2016-07-31

### Looker Design

#### _flash_on_ Redesigned Navigation Bar

  * **Widened available working canvas** to expand real estate for working with tables and visualizations and accommodate landscape viewing on additional devices.
  * **Simplified navigation** by removing icons and focusing organization on user actions. The navigation includes: 
    * **Browse:** Have a look at existing content; start from existing Looks and dashboards
    * **Explore:** Start a new query
    * **Develop:** Enter the LookML editor, the SQL Runner, and turn Development Mode on/off
  * **Increased the available Help** and reorganized the menu. The help menu includes: 
    * Search for Docs and Discourse
    * Links to official Documentation and Looker Discourse
    * Information about the current Looker release (including release notes and number)
    * Chat support with Looker's Department of Customer Love (only available to developers and instance admins)
  * **Menu cleanup.** Tweaked a number of menus and lists in order to facilitate navigation and unify design. 
    * Alphabetized a number of lists including Roles, Connections, and Explores in the dashboard Filters modal
    * Left aligned gear menu items and appended "..." to options that launch another modal



### Visualizations

#### _flash_on_ Series Tab in Visualization Editor

The Series tab introduces an improved interface for editing the color, name, and type of a series. Everything that had been modified using key-value pairs in the Style tab's free text boxes can be found in the Series tab, which has replaced the Style tab for cartesian charts.

Learn more: [Column charts](https://docs.cloud.google.com/looker/docs/column-options#series_menu_options) / [Bar charts](https://docs.cloud.google.com/looker/docs/bar-options#series_menu_options) / [Scatter charts](https://docs.cloud.google.com/looker/docs/scatter-options#series_menu_options) / [Line charts](https://docs.cloud.google.com/looker/docs/line-options#series_menu_options) / [Area charts](https://docs.cloud.google.com/looker/docs/area-options#series_menu_options)

### Explore

  * Data tables now display column totals when row limit is reached. [Learn more](https://docs.cloud.google.com/looker/docs/exploring-data#displaying_totals).
  * Explore descriptions are now displayed in the Explore drop-down on the top navigation bar.



### Scheduling & Downloading

  * **Stand-alone Permission to View Scheduled Information.** The `see_schedules` permission allows access to the scheduled plan and the scheduler history panels. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_and_dependencies).
  * _flash_on_ **Improved Layout for Pivoted Downloads**. Downloaded `.csv`, `.html`, `.md`, `.txt`, and `.xlsx` files now display one row per pivoted dimension to more closely match the display in Looker. If you have processes that rely on a single header row, please make use of the "Single Row Table Headers" legacy feature. [Learn more](https://discourse.looker.com/t/deprecation-notice-exports-with-pivoted-columns-look-different-3-52/3029).
  * Clarified the error that users receive when Looker is unable to render PDFs due to PhantomJS not being installed.
  * Clarified the error that users receive if they are a recipient of a scheduled plan made by a user who has been deleted or disabled.



### LookML & Development Environment

  * **Autogenerated Context as SQL Comments for PDTs**. When generating PDTs, Looker will issue a comment to indicate the model, view, ID of the user generating the table (if available), whether or not the user is in Developer Mode, and the instance slug. [Learn more](https://docs.cloud.google.com/looker/docs/derived-tables#monitoring_and_troubleshooting_persistent_derived_tables).
  * **Updated the Look Validator** to improve design and include the ability to replace the name of fields, views, explores, and models regardless of the error. [Learn more](https://docs.cloud.google.com/looker/docs/content-validation).
  * **Fast File Switching.** The LookML development IDE now instantly switches between files and does not require a full page reload.
  * _flash_on_ **Truncated SQL Runner Table List.** The SQL Runner limits the table preview list to 500 to limit browser impact.
  * Completely removed the `scoping` parameter. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-model-scoping).



### Dialects

  * **BigQuery** : 
    * Fixed an issue where Symmetric Aggregates could be incorrectly calculated in the presence of negative numbers.
    * Improved the efficiency of the `week` timeframe.
    * Improved the behavior of measures in `fanout_on` fields.
  * **Snowflake** : 
    * Added information about whether PDTs are functioning.
  * _flash_on_ **Hive** : 
    * Hive version 1.2 is the minimum supported version (rather than Hive version 0.13).
    * Hive now uses `LIKE` instead of regular expressions for string filtering.
  * **Spark** : 
    * Looker now uses HiveQL 1.2 instead of HiveQL 0.13 syntax.
  * **Presto** : 
    * Incorporated the standard Presto JDBC driver (version 0.149). [Learn more](https://docs.cloud.google.com/looker/docs/db-config-prestodb-and-trino).
  * **DataVirtuality** : 
    * Added an SSL option in Looker's connection panel.
    * Fixed an issue where DataVirtuality didn't properly load error messages.
  * _flash_on_ **MS SQL** : 
    * Updated the JDBC driver to v4.2. Note that SQL Server 2005 will no longer be supported.



### General Tweaks and Bug Fixes

  * _flash_on_ [**API (beta) Changes**](https://discourse.looker.com/t/api-changes-3-52/3031): 
    * Ensured that JSON format will return the values of `type: number` fields as numbers rather than strings. [Learn more](https://discourse.looker.com/t/deprecation-notice-json-numbers-can-be-returned-as-numbers-instead-of-strings-in-api-3-52/3049).
    * Replaced the `run_async` and `create_query_and_run_async` routes. API users should transition to the `create_query_task` route.
  * **Performance and Stability Tweaks** : 
    * Improved performance when fetching cached results.
    * Reduced memory usage when reading from and writing to the query cache.
    * Changed the way Looker connects to internal MySQL databases to make the connection more robust.
  * **Visualization Bug Fixes:**
    * Fixed an issue where maps did not work with hidden columns when table calculations were present and all measures were hidden.
    * Fixed an issue where right padding on charts could be misaligned.
    * Fixed an issue where the value format of table calculations did not appear on the y-axis of a visualization.
    * Fixed an issue where time label format would only work with a label rotation value.
    * Fixed an issue where visualizations would render empty if a min or max y-axis value was used with a log scale type.
    * Fixed an issue where a chart warning could push the x-axis out of view.
  * Addressed an issue where different Looker systems could process and sort results in different orders across various areas (dashboards, Explores, downloads, etc.).
  * Fixed an issue where the visual indication that a filter input box was looking for suggestions failed to appear or continue to disappeared while running.
  * Fixed an issue where labels were inconsistently truncated on PDF downloads.
  * Text tiles on LookML Dashboards no longer produce "Element must specify an explore" warnings.
  * Fixed an issue where gear menus from fields in tables would overlay empty state messages on the data table.
  * Fixed an issue where the default value for a dashboard filter was not properly integrating with other filters if set up to do so.
  * Fixed an Issue where embedded dashboards could return empty results on the first run.
  * Fixed an issue where custom filters using yesno dimensions could produce incorrect SQL.
  * Fixed a bug where extended explores incorrectly returned the error "ignore unexpected list of fields in explore".



## Looker 3.50 2016-07-05

### _flash_on_ Legacy Feature Updates

The following 3 features are being turned off and will be removed entirely in 3.50:

  * $$ substitution
  * Joins declared in views
  * LookML "scoping" Parameter



Details on how to migrate off these features can be found in [this Community topic](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067).

### Visualizations

#### **Trend Lines** [Labs] and Reference Lines

  * Added the ability to specify the location of reference line text. Options are Left, Right, Center. [Learn more](https://discourse.looker.com/t/creating-reference-lines-for-charts-through-the-visualization-editor-3-18/642).

  * Added the ability to specify trend lines.

    * Options include linear, exponential, logarithmic, and moving average.
    * Moving average type has options for 7, 14 and 28 as it is typically used for days.
    * Any number of trend lines can be added.
    * Each trend line can be set to a specific series.

See documentation: [Area Charts](https://docs.cloud.google.com/looker/docs/area-options#add_trend_line) \- [Bar Charts](https://docs.cloud.google.com/looker/docs/bar-options#add_trend_line) \- [Column Charts](https://docs.cloud.google.com/looker/docs/column-options#add_trend_line) \- [Line Charts](https://docs.cloud.google.com/looker/docs/line-options#add_trend_line) \- [Scatter Charts](https://docs.cloud.google.com/looker/docs/scatter-options#add_trend_line)




#### Plot Region Data on Interactive Maps

  * **U.S. Zipcode Tabulation Areas and U.S. Counties Map Layers.** These new map layers can be used on the interactive map. The `zipcode` field type automatically works with the interactive map. [Learn more](https://discourse.looker.com/t/using-map-layers-for-visualizing-region-data-in-static-region-3-42-and-interactive-3-50-maps/2303).
  * **TopoJSON Map Layers on Interactive Maps.**
  * All existing TopoJSON `map_layers` in LookML now work on interactive maps, including built in maps like Countries, U.S. States, and U.K Postcodes, and the new Zipcode and County layers. [Learn more](https://discourse.looker.com/t/using-map-layers-for-visualizing-region-data-in-static-region-3-42-and-interactive-3-50-maps/2303).
  * Added a heatmap opacity setting and now map labels can show above or below the heatmap. [Learn more](https://discourse.looker.com/t/interactive-map-new-features-for-release-3-50/2895).



### Explore

#### Custom Filters

See documentation: [Custom Filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) & [Looker Expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions)

  * Full control over filter logic via ANDs, ORs, and parentheses
  * Access to same functions available in table calcs
  * Can be used in conjunction with regular filters
  * Contextual help pane



#### Table Calculations Enhancements

See documentation: [Table Calculations](https://docs.cloud.google.com/looker/docs/table-calculations) & [Looker Expressions](https://docs.cloud.google.com/looker/docs/creating-looker-expressions)

  * New `running_product` function. [See documentation.](https://docs.cloud.google.com/looker/docs/functions-and-operators)
  * New `pivot_where` function allowing references to pivot values based on content instead of position. [See documentation.](https://docs.cloud.google.com/looker/docs/pivot_where)
  * New `pivot_offset_list` and `pivot_column` functions. [See documentation.](https://docs.cloud.google.com/looker/docs/functions-and-operators)
  * New `log` function. [See documentation.](https://docs.cloud.google.com/looker/docs/functions-and-operators)
  * `Yes` and `No` have now been added as constants that can be referenced in functions. [See documentation](https://docs.cloud.google.com/looker/docs/functions-and-operators)
  * New editor including type-ahead assistance, in-editor documentation, and links to the relevant documentation website pages. [See documentation.](https://docs.cloud.google.com/looker/docs/creating-looker-expressions)



### Improved Explore URLs

The explore page URL now has a shorter, more stable, format and the URL does not contain filter values or other data. [Learn more](https://discourse.looker.com/t/how-to-access-the-long-url-of-a-look-3-22/885).

### Powered By Looker

  * **Embedded Explore pages now broadcast a JavaScript event whenever the page state changes.** Enables the ability to build a custom saving mechanism for embed users. [Learn more](https://discourse.looker.com/t/broadcasting-embedded-dashboard-events-to-the-parent-page-3-42/2298).
  * **Support for wildcard subdomains in the embed domain whitelist.** This makes it much easier to whitelist groups of embedded domains.
  * Fixed an issue where downloading a PDF from an embedded dashboard did not work.
  * Fixed an issue where filter values on embedded dashboards did not wrap properly.



### Scheduler

  * Improved unsubscribe flow for scheduled content.
  * Text objects on Dashboards will now appear in Dashboard PDFs.
  * When scheduling content, the **To** section now accepts comma-separated lists of email addresses.
  * The schedule reassignment modal (accessed via `admin/scheduled_plans` ) now includes the name of the Look or Dashboard.



### LookML

  * **Added [`date_start` and `date_end` to date filters**](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-date_start-and-date_end-with-date-filters). This allows the beginning and end dates in a date filter to be explicitly referred to in LookML. This is useful for table wildcard functions in BigQuery or partitioned columns in Hadoop.
  * **PDT Trigger Check / Regenerator** can now rebuild tables concurrently. [See documentation](https://docs.cloud.google.com/looker/docs/derived-tables#query_performance_and_persistence).



### Dialects

[See dialect support level definitions.](https://discourse.looker.com/t/looker-dialect-support/2427)

  * _flash_on_ **Changes to Database Connection Credentials.** Looker will no longer pass authentication information through the driver's connection string and will instead pass credentials as part of the connection properties. [Learn more](https://discourse.looker.com/t/connection-credentials-no-longer-passed-through-connection-string-3-50/2882).
  * **Denodo.** Added Level 2 support. [See documentation](https://docs.cloud.google.com/looker/docs/db-config-denodo).
  * _flash_on_ **Oracle.** Changes to database connection configuration. [See documentation](https://docs.cloud.google.com/looker/docs/db-config-oracle).
  * **Snowflake.** Queries now support timezone conversion. This change will enable features like User Specific Timezones on Snowflake. [Learn More](https://discourse.looker.com/t/user-specific-time-zones-3-22/875).
  * **Presto.** Added support for PDTs.
  * _flash_on_ **Vertica.** Updated the Vertica 7 connection to Vertica 7.1 (Vertica 7.0 users should use the Vertica 6 connection; to use all Vertica 7 features, update Vertica to 7.1 and connect with that option)
  * **Teradata Presto.** Added support for version 141t. For more details on connecting, open a support request.
  * **Hive.** Deprecating support for 0.13. This is the last Looker that will support Hive version 0.13. Starting with 3.52, Looker will support Hive version 1.2+.



### Administration & Security

  * **Additional Sub-Admin Permissions.** Permission to view the PDT panel can be given with the `see_pdts` permission. [See documentation](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles).
  * **Usage panel update.** Can now be downloaded as a PDF. [See documentation](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage).
  * **Connections page update.** Offer to configure PDT support exists only if the dialect supports PDTs. [See documentation](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#persistent_derived_tables).
  * Regenerator based PDT builds now appear in query panel.



### General Tweaks and Bug Fixes

  * Restored the ability to color values in Single Value visualizations. [See documentation](https://docs.cloud.google.com/looker/docs/single-value-options).
  * Model sets on the `admin/model_sets/new` page will now appear in alphabetical order.
  * **Updated 404 Message** to let users know that either the page is not found or they do not have access to view it.
  * Fixed an issue that caused filter input boxes to take up unnecessary space.
  * Fixed an issue where scheduled tasks could temporarily be sent from a staging instance.
  * Fixed an issue where text objects caused LookML Dashboards to break.
  * Fixed an issue where scale types didn't update correctly when switching series positions.
  * Fixed an issue on PostgreSQL with slow relative date filters.
  * Fixed an issue where errors due to ${TABLE} deprecation caused broken dashboards.



## Looker 3.48 2016-06-08

### Dashboards

#### _flash_on_ Improved Dashboard PDFs

  * PDF dashboard downloads now look like they do in the browser.
  * Vector-based rendering allows zooming without losing quality.
  * Note the following requirements: 
    * Looker Labs feature must be enabled
    * The default layout for scheduled emails will change to the new format
    * Customer-hosted installations must be running PhantomJS 2.11. [Check your version and update](https://discourse.looker.com/t/installing-phantomjs-for-pdf-download-scheduling-and-scheduled-visualizations/419).



### Explore

  * Table Calculations editor now works properly with special characters or ambiguous calculation names.
  * Single Value Visualizations have improved support for fields that display images via HTML.



### LookML

  * **Faceted Filters enabled at an explore level** when using `access filter fields` or `sql_always_where`: When an explore has `sql_always_where` or `access_filter_fields` set, `full_suggestions` defaults to true for all fields exposed by that explore. Individual fields can still opt out of `full_suggestions` query behavior by setting `full_suggestions = false`, and can opt out of suggestions altogether with `suggestable = false`. [Learn More](https://docs.cloud.google.com/looker/docs/reference/param-field-full-suggestions).
  * **New timeframe`month_name`**. Dates can now be bucketed by name of month. [Learn More](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#time).
  * **New`can_filter` Parameter**: Accepts the inputs `true` or `false`. When set to `false`, the field cannot be used as a filter. This parameter can be applied to measures and dimensions. [Learn More](https://docs.cloud.google.com/looker/docs/reference/param-field-can-filter).
  * Explore and View names can now start with numbers.
  * **Built-In Named Value Formats for British Pounds and Euros** : `gbp_0`, `gbp`, `eur_0`, and `eur`. These are used as inputs to the `value_format_name` parameter. [Learn More](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name).
  * Unsafe Liquid parameters have been deprecated with a Legacy Feature.



### Dialects

  * **MySQL.** Fixed an issue where NULLs would be filtered out of pivoted tables.
  * **Spark.** Fixed an issue that was causing connections to break due to long index name values.
  * **Redshift.** Provides a more useful error when Redshift Admin kill queries.
  * **BigQuery**
    * Added support for User-Defined Functions (UDFs) as part of a PDT definition: [Docs](https://discourse.looker.com/t/defining-and-using-udfs-in-pdts/2748).
    * Streaming downloads are now possible
    * Fixed an issue where wide queries would fail in Looker
    * Updated to a new BigQuery driver that includes Google Drive support
    * Expanded the max field name length to BigQuery's documented 128 character length limit from the previous limit of 24 chars.
  * **Bityota.** Removed support for Bityota
  * **Redshift & MS SQL.** Limited the duration of the long running query statements Looker uses for query killing tests on Redshift and MS SQL.



### Administration

#### User-Specific Database Connections

  * Connections can be configured to use the user's LDAP credentials to connect to the database. [Learn More](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap#pairing_ldap_user_attributes_with_looker_user_attributes).
  * Allows user-specific, database-level permissions to be enforced within Looker, as well as query auditing.
  * NOTE: public URLS and PDTs are not supported for these types of connections



#### [New Sub-Admin Permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles)

  * New permissions for various admin panels can be granted to users without making them full-blown admins.



### Documentation

  * **Added Looker versioning** in documentation. 
    * Use the Looker version selector in the upper right to select your version.
    * Versioning officially starts with 3.48 features but we have preserved some pre-3.48 version-specific content that can be viewed using the selector.
    * The Looker version selector appears on all pages in the "Exploring and Visualizing Data" and "Sharing, Importing, and Embedding Data" section and will gradually appear on all docs.looker.com pages.
  * Added a button to jump back to the top of the page.
  * Added +/- to the side menu to show when a menu item can be expanded.
  * Moved the search bar to the top of the side menu.



### General Tweaks and Bug Fixes

  * _flash_on_ Added a "Scheduled By" note to the bottom of scheduled emails.
  * Fixed a bug causing a parse error in exploring from the SQL Runner.
  * Fixed an issue that prevented suggestions from populating in filters that depended on some PDTs.
  * Fixed an issue that caused LookML Dashboard elements to overlap when using `layout: static`.
  * Fixed a bug causing the group by clause in the SQL related to some pivoted tables to call the wrong field.
  * Properly warn when attempting to filter a measure on a raw timeframe.
  * Fixed a few small table calculation bugs related to pivoted dimension handling.
  * Fixed an issue with connectivity to the internal database (when using MySQL) which could lead to outages.
  * Fixed an issue where instant dashboard would cause a dashboard not to return from cache if the prior run resulted in an error.
  * Fixed a bug where Looker would incorrectly filter "empty" in "is equal to" string filter.
  * Fixed an issue where Looker tried to convert timezone to '' certain generated SQL.
  * Fixed an issue where filters on some date timeframes were generating incorrect SQL.
  * Fixed an issue where scheduled dashboards could send from Dev mode.
  * Removed an unneeded warning for unset database timezones in the Connections panel.
  * Fixed an issue where `field_group_label` was causing an erroneous error.
  * Fixed a few errors related to PDF downloads that reflected 'No Results' incorrectly.



## Looker 3.46 2016-05-08

### Dashboards

#### _flash_on_ New Dashboard Look & Feel

  * More modern aesthetic with font tweaks, better use of whitespace, and removal of clutter.
  * [Single values](https://docs.cloud.google.com/looker/docs/single-value-options) read more naturally with titles on the bottom.



#### _flash_on_ [Dashboard Edit Mode](https://docs.cloud.google.com/looker/docs/editing-legacy-dashboards)

  * Once activated, provides the ability to move and resize tiles, add or edit filters and notes, and add/remove tiles to the Dashboard.
  * This also introduces notices when saving Looks that show which Dashboards will be impacted by the changes.
  * This feature is derived from and replaces the Lock feature that was in Labs.



#### [Headers and Free Text Boxes](https://docs.cloud.google.com/looker/docs/creating-legacy-dashboards#adding_dashboard_headers_and_text)

Allows for title, subtitle, and body text to be inserted into dashboards. Can be resized and arranged just like a regular tile.

#### [Better Tile Dragging and Resizing](https://docs.cloud.google.com/looker/docs/editing-legacy-dashboards#move,_resize,_and_edit_dashboard_tiles)

  * **Improved Dragging Logic** makes it easier to move and resize tiles on dashboards.
  * **More Flexible Sizing for Dashboard Tiles** Tiles now exist on a 24-across grid instead of a 12-across grid.



### Visualizations

#### [Single Value Visualization Enhancements](https://docs.cloud.google.com/looker/docs/single-value-options)

  * Callout Numbers.
  * Progress Bars.
  * _flash_on_ Dashboards auto-adjust text size so tiles all match.



#### Updated Column Truncation Logic for Table Visualizations

  * Added seconds to the Dashboard Refresh function found in the gear menu on Dashboards.
  * Browser tab titles now reflect dashboard names.



### Explore

#### Table Calculations Updates

  * **New date functions**
    * `add_{interval}`: add_seconds, add_minutes, …, add_years.
    * `trunc_{interval}`: trunc_minutes, trunc_hours, …, trunc_years.
  * **Date improvements.** Comparison operators (`>`, `<`, `>=`, `<=`) now support dates.
  * Improved field completions to include labels.
  * _flash_on_ [ANDs now takes precedence over OR](https://docs.cloud.google.com/looker/docs/functions-and-operators#logical_functions,_operators,_and_constants). In the past, these statements evaluated left to right, so existing equations that didn't use parentheses may change.
  * Added the ability to filter on "is not" with day of week index.
  * _flash_on_ Increased checking for type mismatches to avoid errors. However, this change also means that if you need to [modify any expressions where you compare yes/no fields to strings](https://discourse.looker.com/t/error-message-changes-for-boolean-comparisons-in-table-calculations-in-looker-version-3-46/2663).



### Scheduling

#### Webhooks for Scheduled Looks (Labs)

  * New option when scheduling a Look or dashboard to perform an HTTP POST to one or more servers instead of emailing the results. [Learn More](https://discourse.looker.com/t/scheduling-looks-using-webhooks/2593).
  * Use a service like Zapier or a custom web server to upload data from Looker to an S3 bucket, Dropbox, an FTP server, etc. [See example with DropBox](https://discourse.looker.com/t/saving-scheduled-dashboard-pdfs-to-dropbox-3-46/2606).
  * Introduces a [new permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) `send_outgoing_webhook` that is automatically given to all Looker Admins, and is required to use this functionality.



#### [Scheduling Updates](https://docs.cloud.google.com/looker/docs/scheduling)

  * **Added a "Test" Button**. Sends test email to the scheduler but not recipients.
  * **Added a Formatting Option**. New option to use formatted values in CSVs, TXTs, etc. (just like with downloads).
  * _flash_on_ **Timezones**. Always explicitly set the timezone of a scheduled look and thus detach it from the application's timezone. The scheduling modal defaults to the application timezone when creating a new schedule. Changing the application timezone thus effects all newly created plans, but not existing ones.
  * _flash_on_ **Scheduling Modal Changes**. Full control over range of hourly option and improved UI. 
    * Expanded the hourly range available.
    * Support for scheduling on a particular day of the week occurrence in the month was broken and has been removed. Current schedules set to run on a _particular_ day of week and week of month will automatically be reassigned to the first day of the month.



### LookML

  * **Improved reliability of the LookML Generator**. The LookML Generator now only generates for the requested schema instead of always generating for the default schema as well, resolving issues with duplicate field definitions and "exists" errors for view files.
  * **New Value for Timeframes Parameter**. Added `day_of_year` timeframe.
  * **New Filter syntax for filtering on Quarters**. `2015-Q2` will now work in Matches(Advanced).
  * _flash_on_ **LookML Deprecations.** [Learn More](https://discourse.looker.com/t/syntax-deprecations-in-3-46/2594). 
    * $$ substitution is now a legacy feature. It should be replaced with ${TABLE}.
    * Starting in 3.46, joins should only be defined inside an `explore:` definition. Defining a `join:` in any other location is deprecated.
    * The `scoping` parameter has been deprecated. Using `scoping: false` will now produce a LookML Validator error. Models should always use scoped field names.



### Dialects

  * **dashDB** : Now supports PDTs and Query Killing.
  * **Streaming Dialects**. Aster, Data Virtuality, Exasol, Greenplum, Hive, Impala, Microsoft Azure SQL, Microsoft SQL Server, Presto, Spark, and Teradata. See the [What are all the row limits in Looker?](https://cloud.google.com/looker/docs/best-practices/row-limits-in-looker) Best Practices page for more information. 
    * **Spark** : Fixed issue that could cause filter suggestions to generate invalid SQL
    * **Presto** :
    * Now possible to create views from multiple catalogs in PrestoDB, not just the one specified in the connection.
    * Fixed issue where connection tests were remaining in the Presto queue.
  * **PostgreSQL Fixes:**
    * Fixed an issue that caused filtering on a quarter to be incorrect.
    * Fixed an issue with slow queries using relative date filters.
    * Fixed an issue that caused uppercase letters to require quotes.



### General Tweaks and Bug Fixes

  * Added ability to search by models in Spaces.
  * Instant Dashboards (Labs) now takes advantage of improved caching.
  * Added a link to the instance in "Welcome to Looker" emails.
  * Fixed a bug causing a slow resize of embedded pages.
  * Fixed a bug on the LDAP Admin page that caused text values to overflow from form spaces.
  * Fixed a bug for users of Microsoft Edge where visualizations didn't fill space completely.
  * Updated the explanatory tooltip on `see_lookml` permission the permissions page to show that it also allows users to see SQL.
  * Updated the tooltip text on the Generate Project Model page.
  * Fixed a bug where large result sets were being put into cache and causing outages.
  * i__looker updates: 
    * Added `embed_user` as a join to the user explore
    * Added `sql_text` to history explore
    * Added links to admin/queries as well as schedule plan.
  * Fixed a bug where disabled series' labels were remaining on vis.



## Looker 3.44 2016-04-07

### Important Changes

  * **Instant Dashboard** is being removed as a feature. Dashboards will load more quickly from cache.
  * Loading assets from CDN is now enabled for all Looker-hosted customers.
  * Several Legacy Features are going to be turned off by default, but can be re-enabled. [Learn More](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067). 
    * Field Labels Can Override View Label
    * Leading Period in Field Names
    * Upper Case Labels in Downloads and Chart Configurations
    * Send email from looker@looker.com
    * Default Redshift PDT Distribution Style EVEN



### Dashboards

  * **Automagic Heatmaps** : The "Fit to Data" feature is supported when using heatmaps.
  * **Improved Error Messaging on Dashboard Tiles**. Incorrect filter syntax errors are now displayed.
  * Fixed an issue where tiles were loading in a compressed way before properly filling the screen.



### Visualizations

  * **Custom X-Axis Limits**. Introduces a setting to show or hide the first or last X rows as specified by the user.
  * **Logarithmic Y-Axis** is now available for charts.
  * Fixed an issue with misaligned stacking pieces in stacked bar charts.



### Scheduling

  * **New Scheduling Admin Panels**
    * _Scheduled Plans_. Displays all currently scheduled items in your Looker instance with relevant details, including task owners.
    * _Scheduled Job History_. This section shows recently run items on your instance with details, including the query, runtime, and success or failure state with errors (if applicable).
  * **Looks can now have more than one schedule**. Brings Look scheduling into alignment with how Dashboard scheduling works. Now, Look schedules are created per user, so different users can have different schedules for the same Look.
  * **New schedules will start at the first scheduled time**. They will no longer send an email immediately after scheduling.
  * Schedules that belong to a user who no longer exists in the system (i.e., they've been deleted) or have been disabled are automatically reassigned to the first enabled user with the "Admin" role.
  * Fixed issue with dashboard display on the iPhone mail app.



### LookML & the Developer Environment

  * **Custom Field Groups**. Adds the ability to group fields together in the Field Picker using the new `group_label:` parameter. [Learn More](https://discourse.looker.com/t/grouping-fields-within-views-3-44/2448).
  * **Ability to Rename Projects**. Accessible in the "Project Settings" option located under the Sync button.
  * **Updated`Distance` Field**
  * **New In-App Links to Documentation** applies to: 
    * LookML validation errors, where applicable.
    * Applies to deprecated features and the Legacy Feature Panel to help transition off of old features.
  * Multiple conditions in HAVING clauses and filtered measures now are always each wrapped in parentheses.



### Dialects

  * **Spark/Hive Updates** : 
    * Fixed an issue where EXPLAIN was broken for Hadoop-related dialect issues.
    * Fixed an issue where SQL Runner queries were running slowly on Spark SQL.
    * Tests for PDTs are now run at connection time for Spark SQL.
    * Spark SQL now gets schema information from SQL instead of JDBC calls.



### General Tweaks and Bug Fixes

  * **Update to the`create_table_calculation` Permission:** Users now do not need the `create_table_calculation` permission to _see_ table calculations. This permission is still required to _create_ calculations.
  * Fixed an issue where switching into dev mode while looking at a file that only exists in production caused an immediate 404.
  * Made updates to the Explain function in the SQL Runner to apply more dialect-specific functionality and remove forced limits.
  * Fixed a bug where table calculations didn't work when exploring queries from the SQL Runner or i__looker.
  * Fixed a bug in which one failed SAML validation would cause all subsequent checks to fail, even with a valid file.
  * Fixed an issue where a new version of Chrome was causing dashboards to crash the browser.
  * Fixed a bug where dashboard changes were not being reflected due to caching.
  * Fixed a bug where filtering on nulls as strings did not work.
  * Fixed a bug that made navigating LookML files in Developer Mode very slow.
  * Override a chat client setting that caused the chat window to open unnecessarily.



## Looker 3.42 2016-03-13

### Lookerbot

With Looker 3.42, we unveiled the [Lookerbot](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-lookerbot-for-slack), a Slack integration with Looker that allows you to bring Looker data into your chats.

### Labs Features

  * **LookML Extensions** is no longer a Labs features, and will be automatically available for all instances. [Learn More](https://discourse.looker.com/t/code-reusability-extending-explores-and-views/939).
  * **Drill Menus for Visualizations** : See below.



### Drilling Updates

#### Drill Menu

  * Clicking on a drill link now always shows the drill menu. The `...` is used to indicate external links and/or dashboards. Hierarchical and dimensional drills will not display this icon.



#### Drill Preview

  * Drilling loads the results of the drill in a preview overlay. This keeps users in the same context (i.e., on the same Explore page or Dashboard). Users can then choose "Explore From Here" to jump into the full Explore experience. [Learn more](https://discourse.looker.com/t/using-drill-overlays-3-42/2330).
  * Measures with only one drill possibility directly open the Drill Preview.
  * If there is a problem with Drill Preview, it can be disabled by enabling the "Legacy Drill Behavior" on the Legacy Features panel. Read more about [Legacy Features](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067).



#### Drill Menus for Visualizations

  * Enables drilling into visualizations via drill menus. This is now the default behavior and has been removed from the Labs section. [Learn more](https://discourse.looker.com/t/drill-menus-in-visualizations-3-40/2145).
  * Drill menus on visualizations other than tables, single value, and single record no longer show the "Filter on..." drill options.
  * Drill menus work on pivots in both tables and visualizations.



### Visualizations

#### Table Visualization Improvements

  * Columns can be renamed, including the names of pivoted columns. [Learn more](https://discourse.looker.com/t/changing-series-labels-in-table-visualizations-3-42/2328).
  * Styles can be applied to tables, including black & white, transparent, and greyscale. [Learn more](https://discourse.looker.com/t/color-styling-of-table-visualizations-3-42/2326).



#### Totals Labels for Stacked Charts

  * There is a new "Totals Labels" option for stacked column, bar and area charts. [Learn more](https://discourse.looker.com/t/how-to-display-totals-on-stacked-charts-3-42/2324).
  * There is a new "Show Silhouettes" option. When series are deselected in a stacked chart, a gray bar ("silhouette") shows the total of all series behind the subtotal of selected series.
  * _Important note_ : row totals in the data table will no longer display in stacked charts.



#### Map Layers in LookML

  * The relationship between a dimension and a particular set of map regions can now be defined in LookML, rather than requiring each visualization to configure a custom TopoJSON URL. This affects the "Static Map (Regions)" visualization. [Learn More](https://discourse.looker.com/t/using-custom-map-layers-for-visualizing-region-data-3-42/2303).



### Powered by Looker

#### JavaScript API for Events

  * Embedded dashboards can now communicate out to their parent page. [Learn More](https://discourse.looker.com/t/broadcasting-embedded-dashboard-events-to-the-parent-page/2298).



#### New URL Parameters to Customize Embedded Objects

  * Ability to hide the title.
  * Ability to hide the footer.
  * Option to redirect an embedded Look to the explore page version by adding `/explore` to the end of the URL.
  * Option of linking to the explore page with the Field Picker open. [Learn more](https://discourse.looker.com/t/url-parameters-to-customize-embedded-looks-3-42/2329).



### Dialects

  * Raised the default number of database connections from 30 to 75 for Microsoft SQL Server, Redshift, PostgreSQL, and MySQL connections.
  * **Retired Spark 1.3.** Spark customers should use 1.4 or higher.
  * **BigQuery** : 
    * Fixed an issue where counts with filters, on a fanned field, was not working.
    * Fixed an issue that caused a 500 error when generating tables.
    * Fixed an issue where text suggestions sent up "undefined".
  * **Updates to Timeframes**
    * `hour` and `hourX` now return values in the form `YYYY-MM-DD HH`.
    * `minuteX` now returns values in the form `YYYY-MM-DD HH:MM` (matching the minute timeframe).



### General Tweaks and Bug Fixes

  * PDFs and scheduled visualizations will now have darker text for increased readability.
  * Tooltips on charts now reflect custom axis names.
  * Added the ability to set a custom mailer port via Looker command line options (Option is: `--default-mailer-port=[port number goes here]`).
  * Allow the ability to hover over sections of a chart that are mostly composed of tooltips and still get the tooltip to appear.
  * Fixed a bug where items scheduled to send on Sunday were also being sent on Monday.
  * Fixed a bug in which filter values would duplicate and overwrite one another when adding multiple input boxes per filter.
  * **Internet Explorer Fixes** : 
    * X-axis labels will now appear.
    * Fixed an issue in which legends in charts caused errors when charts were too small.
    * Fixed an issue that was causing multiple vertical scrollbars to appear when only one was necessary.
  * Fixed several issues pertaining to Automagic Heatmaps, in which they weren't properly loading or reloading with changes.
  * Fixed a bug where adding and removing a note would mess up alignment on dashboard tiles.
  * Fixed an issue where Time Label Format was inconsistent between Explore and Dashboard.
  * Fixed an issue where publicly embedded tables were not sortable.
  * Fixed an issue where some queries with No Results incorrectly return as "Query Killed" in SQL Runner.



## Looker 3.40 2016-02-25

### Dashboards

  * **Lockable Dashboards [Labs].** Prevent changes to a dashboard without explicitly unlocking it. The feature also surfaces additional information to users about the connections between editing Looks and editing Dashboards for all viewers of those pieces of content. Must be explicitly enabled in the Labs section.
  * **Automatically Link Across Dashboards [Labs].** Provides a drill menu to surface and link to dashboards that have a filter matching the field you are drilling on. The menu will also surface links to external URLs using native drills, although those are available without enabling the drill menu. [Learn More](https://discourse.looker.com/t/dashboards-in-drill-menus-3-40/2151).



### Visualizations

  * **Table Visualization**
    * Truncate column names to reduce width of columns.
  * **Pie Chart Improvements**
    * Cleaned up the presentation and positioning of value labels.
    * Series Labels now function on pie charts.
  * **Drill Menu in Visualizations [Labs]**. Drill into the data directly from a visualization rather than through the table. [Learn More](https://discourse.looker.com/t/labs-drill-menu-in-visualizations-3-40/2145).



### Explore

  * **Table Calculation Updates**
    * Allow the removal of table calculations from the data table instead of forcing user through the table calculations modal.
    * The percent format will now multiply by 100.
  * **Filtering Updates**
    * Queries that produce suggestions for filters now do not time out when users click out of the filter box.
    * Filters on `type: tier` now work even with negative values.
  * **Data Table Updates**
    * Dates in tables now do not wrap. (**Note** : This may widen date columns, changing users' tables).
    * Tables switch to virtual scroll at 10,000 cells instead of 5,000.



### Dialects

  * **Presto is now a fully supported dialect.** Looker 3.40 will support versions up to 0.132 natively. For later versions, contact support.
  * **Spark is now a fully supported dialect.** Looker 3.40 will support versions up to 1.5.2.
  * **Hive** : Auto suggestions are now automatically disabled on filtered fields. To re-instate suggestions for any given view file, comment out the line `suggestions: false`. Additionally, field-specific settings override the view-level default. Also applies to Presto and Spark.
  * **BigQuery** : Symmetric Aggregates are now supported.
  * **BigQuery** : Service account no longer needs read permissions on every dataset in a project.
  * **DataVirtuality** : Fixed issue with query killing.
  * **Vertica** \- The dialect picker on the connections panel now includes "Vertica 6" as an option for those customers with Vertica 6 drivers. The "Vertica" option is for customers with Vertica 7 and above.



### Admin Panel

  * **Query Panel.** PDTs now differentiate between _Building PDT_ and _Waiting for PDT_ , which means that the waiting query needs a PDT which is being built by a different thread. While it is waiting, it is not holding a connection from the DB pool.
  * **Authentication via LDAP.** Configure servers that don't allow paginated results. See full LDAP documentation [here](https://discourse.looker.com/t/setting-up-ldap-with-group-to-role-matching/1565).
  * **Option to Force Two-Factor Authentication on Every Login.** Available as a configuration setting on the Two-Factor Admin page.



### General Tweaks and Bug Fixes

  * **LookML <> SQL Update:** Updated the way multi-item `WHERE` clauses are written from `WHERE A AND B` to `WHERE (A) AND (B)` to ensure proper parentheses in more complex `WHERE` clauses.
  * Fixed a bug where sorts on tables weren't being passed through to the dashboard.
  * Fixed a bug where Explore permissions were being shared across Roles.
  * Fixed a bug where LookML Dashboard embed using `/` rather than `::` does not render correctly.
  * Fixed a bug where sorting on measures in table visualizations was broken.
  * Fixed a bug where relative date filters were breaking with Matches (Advanced).
  * Fixed a bug where PDT builds were locking up all queries on a Looker instance.
  * Fixed a bug where `value_format` was not properly passing through decimal points to display, especially on `percent_of_total` and `percent_of_previous` fields.
  * Fixed a bug where single value visualizations continued to display their previous value if the new value was null.
  * Fixed a bug in the prefetching code that mistakenly produced 200 responses when 404s should have been provided, for example if the prefetch fails due to an error in one of the tiles.
  * Fixed a bug where the trash icon in the color picker wasn't doing anything when clicked.
  * Fixed a bug where drillable single value tiles on dashboards were changing colors sporadically.



### Customer-Hosted Installations

  * Added check to deter downgrade in the startup process. [Learn More](https://discourse.looker.com/t/new-startup-flag-to-allow-booting-with-prior-releases-3-40/2232).



## Looker 3.38 2016-01-12

### Dashboards & Visualizations

  * **Reorderable Filters.** The order in which filters are displayed can now be configured in the Add/Edit Filters options found in the gear menu on Dashboards.
  * **Tiny Charts.** Dashboard visualizations are simplified as they are reduced in size to allow for smaller-than-ever dashboard tiles that still contain readable information. [Learn More](https://discourse.looker.com/t/tiny-charts-3-38/1999).
  * **Column Limit Warnings in Dashboard Tiles.** Since visualizations that reach a column limit can produce inaccurate charts, Looker now surfaces a warning inside the visualization panel, and on dashboard tiles, for improved data interpretation.
  * Charts with pivots, or multiple measures with the same `value_format`, now apply that format to the axis tick marks.



### Powered By Looker

  * **Custom Styling for Embedded Dashboards.** Includes background colors, chart colors, font colors, and more. Applies to both LookML and Drag and Drop Dashboards. [Learn More](https://discourse.looker.com/t/customizable-backgrounds-colors-and-fonts-for-embedded-dashboards-3-38/2013).



### Explore

  * **Table Calculation Updates**
    * Ability to drag and rearrange table calculation columns.
    * Introducing a new `rand()` function. [Learn More](https://discourse.looker.com/t/random-function-via-table-calculations-3-38/1991).
    * Table Calculation names are now required to be unique.
    * A formatting drop-down now surfaces a list of named, common value formats. This eliminates the need to type in formatting strings. 

![](https://docs.cloud.google.com/static/looker/docs/images/value-format-dropdown.png)



### LookML

  * **Select Starting Day for Week Dimensions.** New parameter `week_start_day` allows setting the start of a week (for example, Sunday instead of Monday) for each model. [Learn more](https://discourse.looker.com/t/setting-week-start-day-3-38/2020).
  * **Named Value Formats.** Adds the ability to name and reference specific value formats using `value_format_name`. Looker includes several common, named value formats by default. [Learn More](https://discourse.looker.com/t/named-value-formats-3-38/2010).



### Dialects

  * **Updated Dialect Options**. The dialect picker on the connections configuration now includes specific options for Amazon Aurora, Google Cloud SQL, Microsoft Azure Data Warehouse and Microsoft Azure Database. We recommend updating your connections to reflect the correct dialect so that you can take advantage of future dialect-specific improvements.
  * Basic support for SAP HANA.
  * BigQuery project names that include characters like `:` and `.` now work properly.
  * Fixed an Impala issue preventing queries from being killed in some cases.



### Admin

  * Implemented per-user query throttle to prevent any individual user from overwhelming or locking up the database. [Learn More](https://discourse.looker.com/t/per-user-query-throttle-3-38/2051).



### General Tweaks & Bug Fixes

  * Added a button to refresh schemas and tables in the SQL Runner and view generator.
  * Save Dashboard to Space modal now leverages the Hierarchical Space Picker.
  * Host URL can now be set via provision.yml file.
  * Fixed an issue causing fields to be missing from generated Dashboard LookML.
  * Fixed Source for Dashboard queries to restore prior analytics in the Usage Panel.
  * Fixed an issue with Excel downloads that caused them to use up too much memory.
  * Fixed an issue with Excel downloads that caused excess whitespace to be inserted into downloads.



### Legacy Features

Please note the upcoming changes to Legacy Features to ensure a smooth transition as features are removed. [Learn More](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067).

#### Newly Deprecated Features

  * **LookML`decimals` Parameter and `int` Field Type.** The `decimals` parameter and `int` field type are now deprecated and will display warnings in the LookML validator.

Named value formats now offer a more flexible alternative to `decimals`, including decimal, percent, and financial formats. For example, please use `value_format: decimal_2` or `value_format: '0.##'` in place of `decimals: 2`.

Replace `type: int` dimensions with `type: number`. [Learn More](https://discourse.looker.com/t/deprecate-decimals-parameter-and-int-field-type-3-38/2015).




#### Legacy Features removed in this Looker 3.38

  * Old Field Picker



#### Legacy Features to be removed in Looker 3.40

> Please transition off of these features over the course of the next month prior to your next update.

  * Field Labels Can Override View Label
  * Leading Period in Field Names
  * Upper Case Labels in Downloads and Chart Configurations
  * Send email from looker@looker.com



#### Legacy Features to be removed in Looker 3.42

> Please transition off of these features over the course of the next 2 months.

  * Default Redshift PDT Distribution Style EVEN



## Looker 3.36 2015-12-08

### Labs Features

_As of 3.36, Looker has an expanded definition of Labs features. In addition to those experimental features that exist on the Labs page, select features throughout the application will be presented as part of the Labs program to let users know that they are still being considered for additional functionality._

  * **New & Improved SQL Runner** with an updated interface and the ability to share, download, and explore from SQL queries. This feature will automatically be on for all instances. [Learn more](https://discourse.looker.com/t/new-and-improved-sql-runner-3-36/1893)



### Explore

  * **Table Calculations for Pivot Rows**. Additional functions enabling aggregates across pivot rows, cleaner complex offset computations, and row-level aggregates. Learn more about [pivot rows](https://discourse.looker.com/t/aggregating-across-rows-in-table-calculations-3-36/1894), [offset lists](https://community.looker.com/technical-tips-tricks-1021/calculating-moving-averages-30817), or [lists](https://discourse.looker.com/t/using-lists-in-table-calculations-3-36/1895)
  * **Updated Dashboard Modal.** Shows the type of visualization added to increase clarity while building dashboards.
  * **Share Public Look as Images**. Easily share visualizations as a static image that updates as your data does. [Learn more](https://discourse.looker.com/t/sharing-public-looks-as-static-images-3-36/1897)
  * **Row Limit Warnings for Scheduled Looks.** Items scheduled from the Explore page will include warning in email.
  * Restored the ability to copy/paste table headers from the Explore page.
  * Updated the Make Public Modal to require a user to press Save to enable public links.



### Dashboards & Visualizations

  * **Dashboard Tiles Now Grey Out on Run**. Provides visual clarity on running tiles.
  * **Dashboard Stop Button**. Displayed while queries are running.
  * **Single Value Visualizations Color Setting**. [Learn more](https://discourse.looker.com/t/setting-the-font-color-of-a-single-value-visualization-3-36/1892/1)
  * **API for Prefetching Dashboards**. This will allow Lookers to take advantage of a robust data pre warming system.



### LookML

  * **New Parameter`distribution_style` with possible values `ALL` or `EVEN`**. This allows an explicit choice between all vs. even diststyle in persistent derived tables not distributed by key. Applies only to Redshift. Introduces a legacy feature, which preserves the old default of even distribution. 3.36 forward will default to `ALL` diststyle.
  * **Time Fields Now Generate all Timeframes by Default**. Previously users specified an enumerated list of timeframes that they want. Users can still specify a list to get a subset of timeframes.



### Powered By Looker

  * **Embedded Dashboards with User Timezones**. Instance allows user timezones and connection is configured for timezones. Embedded dashboards will no longer show timezone mismatch warnings.



### Spaces

  * Spaces now show all subspaces instead of limiting to four.



### Admin

  * **Permissions Updates.**
    * Permission Page now reflects Permission Dependencies
    * Users must have the download or download_with_limit permission to download Dashboard PDFs
  * **LDAP configuration changes.** Now allows an admin to say which user attribute to use for searching. This enables mapping LDAP groups to Looker Roles if using the posixGroup style.



### Dialects

  * **Increased DataVirtuality Support**. Added support for Symmetric Aggregates and fixes for day_of_week parameter.
  * **Increased DashDB Support**. Query killing is not yet available.
  * **Increased Exasol Support** , including PDTs
  * **BigQuery**. Update for FLATTENS to allow for multiple fields not on same branch of tree



### General Tweaks & Bug Fixes

  * Looker now supports improved navigation by keyboard keys for greater accessibility.
  * Browser tabs now indicate the part of the app being used on each tab.
  * Fixed an error where Save Look Modal opened with an error.
  * Improved the error messaging when column limit reached for pivots.
  * Fixed a bug causing visualizations to error out inaccurately.
  * Fixed an issue where dashboard tiles gear menus were overflowing the screen and thereby not selectable.
  * Fixed an issue where dashboard element wasn't reflecting sorting done on the Explore page.
  * Fixed a bug where clicking "Add to Table" on a filter removed the Filter from the query.
  * Fixed a bug where Automagic heat map breaks if join does not include xxx_bin_level in fields parameter.
  * Fixed a bug where the Run button occasionally would not show up on an embedded Dashboard.
  * Fixed a bug where an XLS file didn't download properly due to excess whitespace.
  * Fixed the Move Space modal.
  * Fixed an issue where saving over a Look added it to a Dashboard twice instead of updating the Look.
  * Fixed a BigQuery bug in which create view from table can't generate LookML for projects with deprecated project names containing `.` and `:`.
  * Fixed a bug where, in an embedded context, users could use hotkeys to open the edit dashboard modal and chose looks modal.



## Looker 3.34 2015-11-10

### Visualizations

  * **New Visualization: Interactive Maps.** New maps zoom and pan, and are reactive to filter changes. [Learn More](https://discourse.looker.com/t/map-visualization-types-3-34/1656).
  * **Color Improvements for Charts.** [Learn More](https://discourse.looker.com/t/color-palettes-color-picker-3-34/1646). 
    * New series of color palettes that can be used in visualizations.
    * New color picker to assist in selecting new chart colors.
    * Global default color scheme can be applied across the entire instance. [Learn More](https://discourse.looker.com/t/setting-a-global-default-color-palette-3-34/1647).
  * **Ability to Sort by Series in Visualizations.** Sort the row total in the table to see the information in the chart displayed in order of ascending or descending row totals.
  * **Updated Tooltips** for readability.



### Dashboards

  * **Asynchronous Dashboard Loading.** Tiles now load as their data returns from the database, instead of 2 at a time, to aid in faster loading of cached dashboards.
  * **More Informative Error Messaging on Dashboards.** Dashboard tiles will now display the error that has prevented them from rendering, instead of merely showing that an error has occurred.
  * Removed the ability to change Dashboards back to "Drag" layout. "Newspaper" layout is now the preferred layout for all drag & drop dashboards.



### Explore

  * **More Granular Scheduling Options.** Includes multiple hours, different days of the month, and on weekdays only. [Learn More](https://discourse.looker.com/t/more-granular-scheduling-options-3-34/1874).
  * **Ability to Sort by[Row Totals](https://discourse.looker.com/t/sorting-on-row-totals/1738) and [Table Calculations](https://docs.cloud.google.com/exploring-data/using-table-calculations#sorting-table-calcs)**.
  * **In-modal Look Editing.** Keeps users on the page that they accessed the modals from for increased context in the app.
  * **Improved Public Link Workflow.** It is no longer required to refresh the page to see the associated public links after marking a Look as public.
  * **Ability to Issue Queries Without`ORDER BY` Clause.** Looker will not generate an Order By clause if the first field in the table is a `cancel_grouping_field` and there are only dimensions in the query. This can be used to reduce the size and complexity of a query in certain cases.
  * **Improved Suggestions for Filtering**. 
    * Suggestions will now properly populate from a view that is defined using the `sql_table_name` parameter.
    * "Day of Week" and "Day of Week Index" timeframes now suggest days instead of timestamps.
    * See additional changes in the LookML section below, including how to make suggestions work with access filters.
  * **Updates to Filtering for`type: location` Fields**. 
    * Added radius-based filtering.
    * Added support for `null`, `not null` and `-null` in filtering. The location field is considered null if either latitude or longitude (or both) is null.



### LookML

  * **New`quarter` Timeframe.** This timeframe can be created as part of a dimension group or as a standalone dimension. [Learn More](https://discourse.looker.com/t/quarter-and-quarter-of-year-timeframes-3-34/1655).
  * **New`quarter_of_year` Timeframe.** This timeframe returns Q1, Q2, Q3, and Q4 independent of the year and can be created as part of a dimension group or as a standalone dimension. [Learn More](https://discourse.looker.com/t/quarter-and-quarter-of-year-timeframes-3-34/1655).
  * **Suggestions for Access Filters.** Suggestions can be enabled when using access filter fields by utilizing the `full_suggestions: true` parameter. [Learn more](https://discourse.looker.com/t/filtered-suggestions-with-access-filter-fields-3-34/1744).
  * **Configurable Suggestions Caching.** Suggestions can now be cached for the time of your choosing. Set these on a per-field basis using `suggest_persist_for` followed by a timeframe. If no `suggest_persist_for` is set, the default time remains 6 hours.



### Powered By Looker

  * **PDF Downloading for Embedded Dashboards.** Permissions are configured in the same way as for regular Looker Users and Roles.
  * **All Download Types for Embedded Elements.** Permissions are configured in the same way as for regular Looker Users and Roles.
  * **User Timezones for SSO Embedding.** Set the parameter as part of the SSO embed setup process.



### Dialects

  * **Expanded BigQuery Support** ([additional nuance](https://discourse.looker.com/t/lookml-for-bigquery/808)), including: 
    * Query Size Estimator to help manage query usage.
    * Nested and repeated data supported natively in LookML using the `fanout_on` parameter. [Learn More](https://discourse.looker.com/t/lookml-nested-records-in-bigquery/1578).
    * PDTs to optimize querying.
    * Job Canceling for queries.
    * Generator Improvements, especially for nested and repeated data.
    * .p12 Certificates support arbitrary passphrases and are now uploaded via Looker.
  * **Microsoft SQL Data Warehouse Improvements:**
    * Persistent Derived Tables are now supported.
    * Symmetric Aggregates are now supported.
  * **Hive & Spark:** Fixed an error with week truncation.
  * **Vertica:** Fixed query killing.



### Admin

  * PDT Panel on the Admin page now reflects shared PDTs.
  * Added a URL to the modals in the Query panel, so that you can return to the data about those queries.
  * Updates to the i__looker model & Usage panel: 
    * Fixes query most recent run at time.
    * Adds most recent run time.
    * Makes user roles into a list.
    * Fixes dashboard scheduled task email list.



### General Tweaks & Bug Fixes

  * **Scheduled Email Attachments for the iPhone iOS Mail Application.** Fixed a bug that was preventing this functionality.
  * **Added Text Editor Modes.** Set the mode on a per-account basis . Options are "vim" and "emac".
  * Fixed a filtering issue where commas were not properly being escaped.
  * Fixed an issue where some LookML errors were not being caught by the validator.
  * Fixed a bug in which .iqy files were not carrying value format through to the Excel file.
  * Fixed a bug where trying to delete a model with a space in the name caused a 404.
  * HTML Sanitization whitelists are no longer configurable. All HTML specified in LookML is stripped of JavaScript tags and attributes, and all other valid HTML tags are allowed.
  * Looker now supports using an "external" cipher key that is managed in an external file specified to Looker on the command line.
  * Looker 3.34 will also see the introduction of a CDN for our static assets.
  * Improved security for JavaScript files via SRI Integrity matching for browsers that support this new security feature.



### Behavior Changes

  * **LookML Dashboard Changes:** When you copy the LookML that Looker generates for a visualization, keep in mind ... 
    * You cannot set floats or integers to `""` without an error.
    * If a Dashboard's LookML has the `column_limit` set to an empty string (`""`), the `column_limit` is converted to nil.
  * **Liquid Templating Changes for All Customers** : JavaScript in Liquid templates will no longer work as of 3.34. Neither `<script>` tags or event handlers on elements like `onclick` or `onmouseover` will work.



## Looker 3.32 2015-10-13

### Visualizations and Dashboards

  * **Introducing Newspaper style layout for Dashboards** , which allows for some tiles to take up more than one row while others remain on a single row. Also improves ease of dragging and dropping tiles. [Learn More](https://discourse.looker.com/t/using-the-new-newspaper-layout-for-dashboards-3-32/1513).
  * **X-Axis density automatically reduces** based on available space for a visualization.
  * **Updated the Add/Edit Filters modal** for easier application of filters to Dashboard tiles. [Learn more](https://discourse.looker.com/t/adding-and-editing-filters-in-a-newspaper-dashboard-3-32/1550).
  * **Introduced ability to edit filters on a particular tile directly from gear menu.** [Learn More](https://discourse.looker.com/t/how-to-edit-a-dashboard-elements-filters-directly-from-the-element-3-32/1511).
  * Improved responsiveness of filter input boxes on large dashboards.



### LookML & IDE

  * **Introduced a`date_raw` field type and `raw` timeframe**, which excludes timezone conversions and casting. [Learn more](https://discourse.looker.com/t/using-the-raw-timeframe-3-32/1549).
  * **Suggestions now work with`one_to_one` joins.**
  * **Improved the speed of the LookML Validator.**
  * Made the behavior of `type: yyyymmdd` the same as `type: date`, which means that timezone conversions will not be applied to it.
  * To minimize load on customer databases, Looker now truncates the contents of the `pdt_event_log` `action_data` column after 5 days.
  * Fields are now prevented from being both a distinct type _and_ a primary key to avoid errors.



### Administration Panel

  * **Group to Role Mapping for SAML:** SAML Authentication setup now includes the ability to assign groups to roles.
  * **Custom Backups:** Ability to specify a non-standard S3 region.
  * **PDT Panel Improvements:** Ensures there is always a reason for rebuilding tables and sped up loading time in certain situations.
  * Removed Load Balancing settings unless instance is load balanced.
  * SSO URL generator will use hostname instead of port.



### Dialects and Databases

  * **Oracle:** Generated PDT names may be truncated as necessary to prevent errors.
  * **Data Virtuality:** Query killing now works as expected.
  * **Vertica:** Fixed bugs that were causing inaccurate month and year filtering.
  * **MSSQL:** No longer allow tables to lock during long running queries.
  * **Redshift:** Improved pivots in database & improved performance of date predicates.



### General Improvements, Tweaks, and Bug Fixes

  * **Powered By Looker** : Embedded Looks now show totals, row totals and table calculations.
  * Scheduled email tables now include gridlines for easier reading.
  * Improved loading time of Explore pages with large amounts of data.



## Looker 3.30 2015-09-15

### Visualizations and Dashboards

  * **Ability to format reference line labels**. [Learn more](https://discourse.looker.com/t/creating-reference-lines-for-charts-through-the-visualization-editor-3-18/642/7).
  * **Scheduled & downloaded dashboard improvements:**
    * Table elements in a dashboard PDF file display the same number of rows as depicted in the browser. [Learn More](https://discourse.looker.com/t/how-to-optimize-tables-in-dashboard-pdfs/1408).
    * Row and column totals will now be included.
  * **Dashboards & looks now transfer ownership properly after copying**.
  * **Updated the "Add to Dashboard" modal**.



### LookML & IDE

  * PDTs are automatically shared between models, instead of producing duplicate tables.
  * Added `week_of_year` timeframe. [Learn More](https://docs.cloud.google.com/reference/field-reference/dimension-type-reference#time).
  * Generator now writes joins using the `sql_on` convention instead of `foreign_key`.
  * Models that only contain hidden explores now appear in the **Model Set** list on the **Roles & Permission** page.
  * More useful error messaging when git configuration status has issues.
  * Removed `type: composite` and `type: service_level`.
  * ERB templating is permanently removed as a configuration option, and the `template` parameter is deprecated. Liquid templating is enabled for all instances.



### Explore

  * **Table Calculations:**
    * Date operations are added, including the ability to subtract dates, extract parts of dates, return the current date, etc. [Learn More](https://discourse.looker.com/t/using-date-operations-in-table-calculations-3-30/1398).
    * Comments, using the `#` character, can be inserted into table calculation definitions. [Learn More](https://discourse.looker.com/t/comments-in-table-calculations-3-30/1397).
  * **Added Excel Spreadsheet download option**. [Learn More](https://docs.cloud.google.com/sharing-and-publishing/downloading).
  * **Filter suggestions now pull 5000 rows of suggestions**.
  * **Ability to filter on a timestamp field**.
  * **Improved Error Messaging** : 
    * Errors related to fields in an Explore now only appear if relevant to that query.
    * Errors now state whether they are due to a database or LookML model issue.
  * **Performance Improvements** : 
    * Tables now load on scroll. While the entire result set is still returned from every query, only the visible portion of the table will be rendered in the browser at any given time. This should result in performance improvements when dealing with large result sets.



### Dialects and Databases

  * Support for Microsoft SQL Data Warehouse.
  * Support for partitioned tables in BigQuery.
  * Change in configuration for Impala connections using noSasl. [See here](https://discourse.looker.com/t/connecting-to-impala-with-auth-nosasl/1276).



### Administration Panel

  * **`use_sql_runner` permission now does not depend on `develop` permission to function.** [Read more](https://discourse.looker.com/t/why-cant-my-users-see-the-sql-runner-tab/553/2).
  * **Updated the embed panel (/admin/embed) to include a URI validator**.
  * **Usage Panel:**
    * Updated the query "source" to better account for public and private urls and `suggest:` queries.
    * Linked `public_urls` to their relevant `look_id`.
  * **Looker logs now capture`stderr` and `stdout` from both the ruby and java layers**.



### General Improvements, Tweaks, and Bug Fixes

  * Fixed a bug where opening the visualization panel killed a query in progress.
  * Fixed a bug where dates on the x-axis were offset when using the **Time Label Format** input box.
  * Fixed a bug where time zones weren't converted properly when substitution operators were used in field definitions.
  * Fixed two `sql_case` bugs: 
    * Single quotes in bucket names now work correctly.
    * Numbers as bucket names now work correctly.
  * Fixed a bug where a trailing comma in a set of pasted filter values caused the filters to be omitted from the generated SQL.
  * Logging back in after an auto-logout now takes you back to the page you were previously on.
  * If logged out in an embedded context, Looker will now present the login screen instead of a 401 error if the embed URL has `allow_login_screen=true` included as a parameter (e.g. `/embed/dashboards/123?allow_login_screen=true`).



## Looker 3.28 2015-08-18

### Visualizations and Dashboards

  * **New "Table" visualization type**. [Learn More](https://discourse.looker.com/t/table-visualization-type-3-28/1294).
  * **Support for measure-versus-measure scatterplots**. [Learn More](https://discourse.looker.com/t/measure-vs-measure-scatterplots-3-28/1296).
  * **Ability to filter visualizations based on results of yesno table calculations**. [Learn More](https://discourse.looker.com/t/filtering-in-visualizations-using-table-calculations-3-28/1298).
  * **Dashboard PDF filename now includes timestamp**.
  * **Visualization option updates:**
    * Provide more informative field names when "Show Full Field Name" is disabled
    * New single value visualization size option, "Auto Fit"
    * Donut multiple labels are now on by default
    * X-axis defaults to type "time" if stacking isn't "grouped"
    * Default min and max y-axis values are based on values in the chart instead of being symmetric
  * **Performance improvements:**
    * Improved default visualization type for each query
    * Improved performance when rendering cartesian charts
    * Improved efficiency of rendering large result sets



### Explore

  * **NULL values are now treated as 0 for measures of type`sum`**.
  * **Table calculation updates** : 
    * New `pivot_index` function allows referencing pivot columns individually. [Learn More](https://discourse.looker.com/t/using-pivot-index-table-calculation-3-28/1291).
    * Suggestions now appear after space, enter and delete (in addition to after regular text entry)
    * Table calculation columns will be present in the data table while query is running
  * **Updated "Save to dashboard" modal**.
  * **Performance improvements:**
    * Filter suggestions are now cached for 6 hours (instead of 5 minutes)
    * Improved caching for queries accessed via public URLs
    * "No Results" now shown when query returns zero rows



### LookML & Development

  * Support for `datatype: yyyymmdd` time fields in all dialects.
  * `one_to_one` joins can now be specified without `required_joins`.
  * Deprecated `map_point`, `map_line`, and `locations` field types.



### Dialects and Databases

  * **Beta Support for Spark SQL:**
    * Persistent derived tables
    * In-database pivoting and column limits
    * `list` field type
  * **Basic support for EXASOL** , including symmetric aggregates (no support for PDTs or time zones yet)
  * **Improved support for additional JDBC parameters across dialects**
  * **Dialect-specific improvements** : 
    * Oracle field names are now required to be lowercase
    * Microsoft SQL Server now has SSL support
    * Redshift queries are now cancelled in a way that doesn't produce errors in log files



### Administration Panel

  * Users can now be added to the "Admin" role in bulk.
  * Warnings about misconfigured proxies in front of Looker are presented on the "General" admin page.



### Powered By Looker

  * Option to display normal login screen to unauthenticated users (when SSO authentication is not being used).



### Authentication and Security

  * Beta support for group-to-role mappings with SAML.



## Looker 3.26 2015-07-21

### Visualizations and Dashboards

  * **Hide Fields From Visualizations.** [Learn More.](https://discourse.looker.com/t/hide-a-field-from-a-visualization-3-26/1179)
  * **Choose Looks Modal Improvements:** Now supports adding multiple copies of the same Look to a single dashboard. [Learn more](https://discourse.looker.com/t/adding-looks-to-a-dashboard-from-the-dashboard-3-22/883/2).
  * **Chart Specific Improvements:**
    * **Single Value** \- Font size adjusts based on page size when on a dashboard
    * **Pie Chart** \- Value labels now available
    * **Bar & Column Charts** \- Ability to order stacked bar charts by ascending or descending values within each column
    * **Donut Multiples** \- configurable series label font size
  * **Legends for Cartesian Charts Can Be Right or Left Aligned.** [Learn More](https://discourse.looker.com/t/legends-for-cartesian-charts-can-now-be-right-or-left-aligned-3-26/1143).
  * **Reference Lines Remain on Chart When First Series Removed.** Note that series dependent reference lines - like min, max, or mean - will still refer to first-series values. [Learn more](https://discourse.looker.com/t/creating-reference-lines-for-charts-through-the-visualization-editor-3-18/642/3).
  * **X-Axis Setting Improvements:**
    * Force axes to align at zero when negative values are present and no min or max are set.
    * Setting for "Time" on the x-axis now works with only one series.
    * Time label formats are now available for "Ordinal" setting.



### Authentication and Security

  * **Added SAML Support**. [Learn More](https://discourse.looker.com/t/saml-setup-instructions-release-3-26/1317).



### Explore

  * **Improved Suggestions for Filter Drop-Downs:**
    * Suggestions are now available from joined persisted derived tables.
    * Fixed an error preventing the `suggest_explore` parameter from working.
  * **Added Warning When Downloading All Results.** This has been introduced to reduce unintentional user error in downloading overly large result sets.
  * **Improved LookML Button Behavior.** "See LookML" button next to the Explore name in the Field Picker now jumps to the corresponding Explore definition in the development environment.



### LookML & Development

  * Allow `value_format` parameter to be applied to dimensions of `type: tier`.
  * Support custom ports in git URLs. [Learn More](https://discourse.looker.com/t/how-to-configure-git-in-looker-3-18/623/2).



### Administration Panel

  * **Query Management Panel**. View details of recent and running queries with the ability to kill long running queries. [Learn more.](https://discourse.looker.com/t/query-management-panel-3-26/1155)
  * **Usage Panel Updates:**
    * Dashboard schedules are now explorable via a new explore (scheduled_task_dashboard).
    * Derived tables are now available in the i_looker model.
    * Exposed top looks as an element on the Usage Panel.
  * **New Query Management Panel**



### Dialects and Databases

  * Hive support now includes PDTs.
  * Snowflake support now includes Symmetric Aggregates and PDTs.
  * Improved memory usage for downloads on Redshift and MySQL.



### General Improvements, Bug Fixes and Tweaks

  * **Updates to Scheduled Emails:**
    * Links in scheduled emails will now only be available for measures, not dimensions.
    * E-mails with content larger than the allowed size limits (based on e-mail provider) will be converted to html attachments instead of being cut off inline.
    * Link to explore data in Looker has been moved to the top of the e-mail for increased visibility.
  * History now includes Looks.
  * Fixed an issue with the free-text input boxes in the visualization editor clearing unexpectedly.
  * Right justify values for numeric table calculations in the data table.
  * Provide a useful error when limit of 30K rows with pivoted data is reached (error appears in the .csv file, not within Looker).



## Looker 3.24 2015-06-23

### LookML & Derived Tables

  * **LookML Extensions (Labs Feature):** A new parameter `extends` allows developers to add to existing view and explore files in separate, extension files. This allows for more modular, reusable LookML and simplified updates. [Learn more.](https://discourse.looker.com/t/extending-explores-and-views/939)
  * **PDT Event Log Moves to the Internal Looker Database:** The persistent derived table (PDT) event log has been moved out of the scratch schema, and into the Looker database, to speed up performance and reduce load on the analytical database.
  * **Compound Derived Tables:** The SQL definition of any derived table can now refer to any other derived table by using `${view.SQL_TABLE_NAME}`. This works with all types of derived tables (persistent and ephemeral). [See documentation](https://docs.cloud.google.com/data-modeling/learning-lookml/derived-tables#referencing-derived-tables-in-other-derived-tables).



### Explore

  * **Number Formatting in Exported Content:** Value formatting will be applied by default in sharable links or spreadsheet URLs. Toggle formatting by modifying the URL. [Learn More](https://discourse.looker.com/t/number-formats-with-shareable-links-and-spreadsheet-urls-3-24/1042). [See documentation.](https://docs.cloud.google.com/sharing-and-visualization/publishing-looks-with-public-urls)
  * **Table Calculations:** It is now possible to refer to row and column totals in table calculations, when they exist. Use `${field_name: total}` and `${field_name: row_total}`.



### Dashboards & Visualizations

  * Reference lines are now available on bar charts.
  * Elements now reflect filter changes only after re-running the dashboard, instead of showing the changes instantly before they had been applied.



### General Additions & Tweaks

  * Data about SQL Runner queries is now available in the Usage Panel.
  * Symmetric Aggregates are now supported on Snowflake.



## Looker 3.22 2015-05-26

### Spaces

  * **New organizational system for Spaces.** [See documentation](https://docs.cloud.google.com/looker/docs/organizing-spaces). 
    * Spaces can be nested to allow for hierarchy.
    * All existing shared Spaces will start from a new "Home" Space.
    * Location of each Space will be expressed by a breadcrumb above its name.



### Explore

  * **User-Specific Time Zones:** Different users on the same instance can operate in different timezones. [Learn more](https://discourse.looker.com/t/user-specific-time-zones-3-22/875). 
    * **Note:** this feature will affect query results and requires understanding to properly interpret results. The feature should be enabled only when necessary and with proper training for users.
  * **Updated Save Look Modal** makes saving Looks easier and faster.
  * **Ability to access the "long version" of a Look URL**. [Learn more](https://discourse.looker.com/t/how-to-access-the-long-url-of-a-look-3-22/885).
  * **Table Calculation Improvements**
    * Ability to format table calculations using the `value_format` syntax. [See documentation](https://docs.cloud.google.com/reference/field-params/value_format). [Learn more](https://discourse.looker.com/t/formatting-table-calculations-with-value-format-3-22/884).
    * New functions now available: `floor`, `ceiling`, `is_null`, and `mod`.



### Visualizations and Dashboards

  * **New Information bar on Dashboard elements** will show when the query data was returned, if the query was run in another timezone, and a note icon for dashboard notes set to hover.
  * **Ability to add Looks to a Dashboard while on the Dashboard.** Requires that Looks are in the same Space as the dashboard. [Learn more](https://discourse.looker.com/t/adding-looks-to-a-dashboard-from-the-dashboard-3-22/883).
  * **Chart Value Label Improvements**
    * Smarter defaults.
    * New set of customizable settings in the Visualization Configuration tab. [Learn more](https://discourse.looker.com/t/value-label-improvements-for-visualizations-3-22/894). [See documentation](https://docs.cloud.google.com/exploring-data/visualizing-query-results).



### Dialects and Databases

  * Beta support for PDTs in Oracle.
  * Improved support for BigQuery. [Learn more](https://discourse.looker.com/t/lookml-for-bigquery/808).
  * Symmetric Aggregates are now only turned on for dialects that support it, instead of on an instance-wide basis.
  * Ability to turn off PDTs on a per-connection basis.



### LookML & Development Environment

  * **Option to prevent committing with errors.** Configurable on a per-project basis. Default is "on" for new projects. [Learn more](https://discourse.looker.com/t/how-to-prevent-committing-changes-when-there-are-lookml-errors-3-22/886).
  * `bypass_suggest_restrictions: true` can be added to a field, which allows suggestions even when `access_filter_fields` or `sql_always_where` is used. [Learn more](https://discourse.looker.com/t/how-to-override-disabled-suggestions-with-access-filter-fields-and-sql-always-where/887).



### General Tweaks & Bug Fixes

  * Back button now returns to previous state of page on first click.
  * ERB Templating is now deprecated.
  * Fix for PDT-related "Relation Doesn't Exist" or "Table Doesn't Exist" errors.



## Looker 3.20 2015-04-27

### Features Graduating From Labs

These features were in Labs in 3.18, and are now enabled by default:

  * **Table Calculations:** Ability to add new fields directly on the Explore page, based on the results of a query. [Learn more](https://discourse.looker.com/t/table-calculations-3-18-labs-feature/636).
  * **Redesigned Field Picker:** The Field Picker now collapses fields by their view and date group, removes uppercase view names from fields, and changes the color of measures. [Learn more](https://discourse.looker.com/t/redesign-of-field-picker-in-explore-3-18/629).



### Dashboards and Visualizations

**Scheduled Dashboard Improvements** ([learn more](https://discourse.looker.com/t/scheduling-dashboard-pdfs-3-18/681)):

  * Scheduled dashboards can now appear as inline messages or as PDF attachments.
  * All dashboards can be scheduled from their gear icon or from within a Space.
  * A scheduling icon, with scheduling information, now appears for each scheduled dashboard in its Space.



### Development Environment

**Streamlined Developer Workflow** ([learn more](https://discourse.looker.com/t/how-lookml-changes-get-to-production-3-20/838/1)):

  * Simplified Git options from the main Git button.
  * Perform Git actions without losing your place in the editor.
  * Each user's Developer Mode now correlates to a branch, and commits in dev mode are synced with GitHub or your Git service. "Deploy to Production" will update your production environment by merging that branch to master.



### LookML

  * **Liquid Conditions in Joins:** Allows user input to be used in a join condition (often used for performance improvements). [Learn more](https://discourse.looker.com/t/conditions-in-join-clauses/660). [See documentation](https://docs.cloud.google.com/reference/explore-params/sql_on#conditional-joins).
  * **`view_label`:** A new parameter used to rename views in the Explore UI. [Learn more](https://discourse.looker.com/t/labeling-views-to-make-your-models-more-understandable-3-20/664). [See documentation](https://docs.cloud.google.com/reference/explore-params/view_label-for-join).
  * **`sql_distinct_key`** : A new parameter for computing symmetric aggregates based on a specific field. [Learn more](https://discourse.looker.com/t/sql-distinct-key-in-symmetric-aggregates/748). [See documentation](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#sum_distinct).



### Admin

  * Paginate and search users at **/admin/users**.
  * **LDAP Groups** : Instances using LDAP for user authentication can now organize new users according to the groups that already exist in their LDAP configuration.



### General Improvements & Tweaks

  * Support for MariaDB.
  * Symmetric Aggregates and Persistent Derived Tables are now available for Teradata.
  * Maximum number of columns is now 200.
  * Fix for null vs. false values in SQL Runner.
  * Minor updates to PDT Admin panel.



## Looker 3.18 2015-03-30

### Explore

  * **Labs Feature: Redesigned Field Picker** : The Field Picker now collapses fields by their view and date group, removes uppercase view names from fields, and changes the color of measures. Full functionality can be turned on in the Labs panel (**/admin/labs**). [Learn more.](https://discourse.looker.com/t/redesign-of-field-picker-in-explore-3-18/629)
  * **Labs Feature: Table Calculations** : Ability to define calculations on the results of a query from the Explore page. Must be enabled by an admin from the Labs panel. [Learn more.](https://discourse.looker.com/t/table-calculations-3-18-labs-feature/636)
  * **Explore descriptions** : Must be defined in the Model file using the `description:` parameter. Will appear on hover over the **?** icon next to the Explore's name in the Field Picker. [See documentation.](https://docs.cloud.google.com/looker/docs/reference/param-explore-description)
  * **Filtering by 'OR' in Date Fields** : Press the **+** button next to an existing Date filter to add an additional filter on that field, or use commas between dates when using **Matches (Advanced)**. [Learn more.](https://discourse.looker.com/t/filter-on-multiple-date-ranges-or-filters-between-dates/650)
  * The relative time a query ran now appears next to the run button (e.g. 3 minutes ago)
  * When no sort is specified on a query with tiered dimensions, results will be sorted by the default tier order



### Transformations / Persistent Derived Tables

  * **Production and Developer Mode share the same persistent table if the SQL has not changed.** Also, when a user builds a persistent derived table (PDT) in Developer Mode and pushes the updated model to production, production will use the already-built PDT if the SQL has not changed. [See documentation.](https://docs.cloud.google.com/looker/docs/derived-tables#persistence-in-dev-mode)
  * **"Rebuild Derived Tables & Run" will now cause only that user's query to wait for a rebuilt table.** All tables required for this query will rebuild in the background and will be switched out when complete; no other queries will be impacted by the use of this button (i.e., one user pressing this button will no longer block other users) [See documentation.](https://docs.cloud.google.com/looker/docs/derived-tables#users-can-override-persistence)



### IDE & Model Management

  * **Commit history in the IDE** , including links to version control providers for customers who have set those up through Looker. Access history from the drop-down next to the **Push** button. [Learn more.](https://discourse.looker.com/t/commit-history-in-the-ide/638)
  * **Highlighted changes in diffs** to make reading commits easier. [Learn more.](https://discourse.looker.com/t/highlighted-changes-in-diffs-release-3-18/626)
  * **Setup & support for additional version control providers** \- Set up version control for LookML files within Looker using Bitbucket, GitLab, GitHub Enterprise, or any Git server that can use an SSH key for authentication. [Learn more.](https://discourse.looker.com/t/set-up-support-for-additional-version-control-providers-3-18/623)
  * **Project sync upon first push** \- Once git setup is complete, new projects created by one user are automatically added to all users' developer modes without requiring users to rebuild their directory. [Learn more](https://discourse.looker.com/t/project-synchronization-across-developer-environments-upon-push/643).



### Dashboards and Visualizations

  * **Ability to Schedule Dashboards** as PDF attachments to emails (customer-hosted Looker deployments require PhantomJS and must be enabled in the Labs panel.
  * **Ability to mix Cartesian chart types on a single query**. From the visualization configuration tab on the Explore page, indicate the `series_name: <chart_type>`. Any series that does not have an explicit type declared will use the chart type selected. Does not work for stacked charts. [Learn more.](https://discourse.looker.com/t/using-series-types-to-create-mixed-type-visualizations/536)
  * **Reference lines for the Y-Axis can now be defined through the UI.** [Learn more.](https://discourse.looker.com/t/creating-reference-lines-for-charts-through-the-ui-3-18/642)
  * **Y-Axis Maximum can now be set independently of the Y-Axis Minimum.**
  * **Ability to set a custom Y-Axis Tick Density.** [Learn more.](https://discourse.looker.com/t/set-custom-y-axis-density-release-3-18/635)
  * Null points will no long appear on donut charts.



### Spaces

  * **Ability to delete multiple looks at once within a Space.** [See documentation](https://docs.cloud.google.com/looker/docs/organizing-spaces)
  * **Spaces search now includes model name in result set.**
  * **Move / Copy / Delete now available from gear button on each Look in a Space.**



### General Improvements & Tweaks

  * **Dimensions of`type: int` now sort numerically** instead of alphabetically.
  * **Support for Datavirtuality databases.**
  * **Location field types** are now fully supported on Oracle, BigQuery, Redshift, PostgreSQL, MySQL, Greenplum, MS SQL Server, Aster, and Teradata.



## Looker 3.16 2015-03-02

### Dashboards

  * **Adjustable Row Height** \- Ability to change the height of rows of elements in user-defined dashboards. Hover between rows to see an up/down arrow. Drag down to increase the height of the row above your mouse. ([see documentation](https://discourse.looker.com/t/how-to-adjust-the-height-of-dashboard-rows/505))
  * **Notes** \- Each element on a Dashboard can now have an accompanying text note used to convey information specific to that element. Add and edit the note from the gear drop-down in each element. The note can be displayed at the top of the element, bottom of the element, or on hover. ([see documentation](https://discourse.looker.com/t/dashboard-notes-3-16/504))
  * **Collapsible Dashboard Listeners** \- Filters that each element is listening to now collapse if they are longer than 1 line - click them to expand
  * **Improved Dashboard PDF Formatting** \- Includes link to dashboard, footer with time it was downloaded, and Notes
  * **Filter Modal Changes**
    * The "Apply to Field" in the Listener section of the Dashboard filter creation modal defaults to the field that matches or contains the name of the filter it listens to
    * Listeners can each listen to each filter only once



### Visualizations

  * **Improved Mapping** ([see documentation](https://discourse.looker.com/t/improved-mapping-3-16/510)) 
    * New built-in postcode maps: SF Peninsula, NYC, Austin, UK
    * "Map Regions" in the visualization configuration modal on the Explore page now accepts non-geographical TopoJSON for map data that has already been projected
  * **Formats for Single Value Visualizations** \- Use new value_format parameter ([see documentation](https://discourse.looker.com/t/how-to-format-single-value-visualizations/512))
  * **Visualization Editor Updates:**
    * Renamed "Percent Change" to "Percent of Previous
    * Renamed "Show View Names" to "Show Full Field Names"



### Explore

  * **Unknown Field Error Handling** \- Fields with errors do not appear in the Field Picker in Production mode. In Developer Mode, fields with errors will show in the Field Picker as unavailable fields. This should result in a reduction of "Unknown Field Substitution" errors.
  * "Excel File" download has been renamed "Excel Query File Download" to reflect its true action
  * "Make Public" is now an option in the gear button drop-down on the explore page



### Admin Panel

  * **Legacy Features Panel** \- This section shows features that Looker has deprecated and helps users move away from them. Features in this list will vary by a Looker instance's first version (i.e., older users will see more deprecated features than more recent users) ([see documentation](https://discourse.looker.com/t/the-legacy-features-panel/511))
  * **Labs Feature Updates:** Symmetric Aggregates and Column Limits have become full features, and will be on for all new users. More details on each of those features can be found [here](https://discourse.looker.com/t/symmetric-aggregates/261).



### LookML

  * **New Formatting Syntax** ([see documentation](https://docs.cloud.google.com/reference/field-params/value_format)) 
    * Looker now uses Excel-style formatting for number and string fields, written with the parameter `value_format`
    * The new formatting deprecates the following:
    * Printf formatting
    * LookML Field Types: `percentage`, `dollars`, and `cents`
    * Number field parameters: `format` and `units`
  * **Use Existing Derived Table (PDT) while regenerating** \- While a persistent derived table is regenerating, Looker will use the previous table for querying. This applies to derived tables using a SQL trigger.
  * **Integers for Date Fields** \- all dialects now return integers for DateHourOfDay, DateMonthNum, DateDOM, and DateDOWIndex
  * SQL generated by LookML now forces dates to type date when a date is explicitly declared as a date. Allows Redshift to use its sort key.
  * SQL generated by LookML now uses relational operators instead of `BETWEEN` in date equations



### General Improvements and Tweaks

  * **Shortened URLs** \- URLs now present in a shorter format, making them easier to share. Note that this does impact the configurability of the URL which may change behavior for users.
  * Preserving whitespace has been reintroduced to the SQL Runner results table
  * "Create New Space" Button has moved to the top of the Spaces page
  * Space names are now limited to 100 characters
  * Total Runtime is now an available Measure in the History Table (accessed via exploring elements on the Usage Panel)
  * "Open in Looker" link now works in all Scheduled Looks, even those sent to lists
  * Looks are now alphabetical in breadcrumb drop-downs on the Explore page and Dashboards
  * Aster Dialect Syntax Fix: now uses DISTRIBUTE BY (not ON) in persistent_table definition



## Looker 3.14 2015-02-02

### Spaces and Collaboration

  * **Look Validator (Labs feature)** : Check if Looks are broken & find/replace broken or renamed fields in all locations. Use the Look Validator _before_ pushing changes to the model. ([see documentation](https://discourse.looker.com/t/look-validator-3-14-labs-feature/366))
  * **Home Spaces** : Set any Space as your "Home" space by clicking the home icon next to desired Space's name. 

![](https://docs.cloud.google.com/static/looker/docs/images/homespace.png)



### LookML

  * **[Symmetric Aggregates](https://discourse.looker.com/t/symmetric-aggregates/261):** Allows measures to be brought into a joined Explore. [Try it out on individual explores](https://discourse.looker.com/t/turning-on-symmetric-aggregates-in-a-controlled-way/376) and then enable it via Labs for your entire instance.
  * Tiering, SQL Case & Order By Field 
    * **Sort Order Updated:** `sql_case` fields now sort in the order they are listed, rather than alphabetically. _This will change the current sort functionality_ ; to sort alphabetically in the old way use `alpha_sort: true`. ([see documentation](https://discourse.looker.com/t/update-to-sql-case-default-way-of-ordering-looker-3-14/359))
    * **Tier styling now available:** New `style`: parameter updates how the tiers are presented in a data table. Options are `style: relational`, `style: integer`, `style: interval`, and `style: classic` (default) ([see documentation](https://discourse.looker.com/t/new-style-options-for-tier-as-of-3-14/360))
    * **order_by_field added** : A new parameter to allow dimensions to sort by another dimension ([see documentation](https://discourse.looker.com/t/order-by-field-new-as-of-3-14/361))
  * Deprecated `dow` and `dow_number` in favor of `day_of_week` and `day_of_week_index` ([see documentation](https://docs.cloud.google.com/reference/field-reference/dimension-type-reference#timeframes))
  * [New LookML Syntax Highlighting](https://discourse.looker.com/t/new-lookml-syntax-highlighting/429)



### Derived Tables

  * Persistent Derived Table (PDT) admin panel improved to show latest and average PDT build time, table name, and trigger information



### Dashboards and Visualizations

  * Downloading Options 
    * Entire (non-LookML) dashboard can be downloaded as a PDF (Labs feature) (requires [PhantomJS](https://discourse.looker.com/t/installing-phantomjs-for-scheduled-look-visualizations-and-dashboard-pdf-downloads/419) to be installed)
    * Data from a dashboard element can be downloaded directly from dashboard
  * Added ability to hide dashboard titles when embedding, using the URL parameter `hide_title=true` ([see documentation](https://discourse.looker.com/t/embedding-dashboards/189))
  * Looker will only update an element's filter description AFTER query has updated the displayed data
  * Improved messaging in the app: 
    * Refined wording of "unknown substitution error" and other modeling error messages
    * Clarified impacts of copying LookML Dashboards to Spaces
    * Add a warning when listening and filtering on the same element, since filter is ignored



### Enterprise, Platform, and Security

  * Require "explore" permission to open Looks (note: this may affect users who do not have the explore permission but should be able to see looks) ([see documentation](https://discourse.looker.com/t/permission-checks-for-explore-page-3-14/373))
  * Alternate login - ability to add users by email address when LDAP/Google Auth is enabled
  * Custom S3 backups: specify your own S3 bucket and credentials for backups (default is Looker's managed AWS account)
  * Increased max connection pool size to 100 from 30
  * BigQuery and Snowflake generator support
  * New database dialect support for Teradata and Xtremedata



### General Improvements and Tweaks

  * SMTP error handling deletes mail jobs stuck in queue for more than 7 days and backs off following errors
  * (Running) or (Done) text in browser title instead of favicon icons
  * Fixed Safari CSRF cookie issue when embedding Looker in public websites



## Looker 3.12 2015-01-26

### Explore

  * **Additional pivoting functionality:** When pivoting, add `direction: column` to `type: running_total` to calculate down the column instead of across a pivot. The current default is `direction: row`, which calculates across the row instead. See full pivoting instructions [here]/reference/field-reference/measure-type-reference#running_total).
  * **Runtime diagnostics available:** The runtime for every explore query is now available on a user's history page (**/account/history**). This is also logged in the internal Looker database and explorable via the **/admin/usage** panel (see usage panel update below).



### Dashboards and Visualizations

  * **LookML Dashboards Validator** The validator now checks LookML used to create a LookML Dashboard for valid fields and common typos.



### Enterprise, Platform, and Security

  * **Usage Panel Update:** New usage panel at **/admin/usage** now captures the runtime for every explore, dashboard element, embed, and scheduled look.
  * **Improved SMTP Error Handling:** Looker will now recognize SMTP mailer errors and wait progressively longer before the next attempt.
  * **Public Looks without Limits:** Saving a public Look with no limit will allow the public look to return all results (and stream if applicable). See how to save a public look [here](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls).



### LookML and IDE

  * **New sql_table_name use case:** The `sql_table_name` parameter is now available in joins. [See documentation](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-sql-table-name).
  * **PDT Diagnostics Available:** Initial version of a Persistent Derived Table (PDT) admin panel is now available at **/admin/pdts**. This will help manage usage table and will continue to be improved. [See documentation](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts).
  * **Single Table Model Generation:** Generating a model with a single table is now possible. [See documentation](https://docs.cloud.google.com/looker/docs/generating-a-model).



### General Improvements and Tweaks

  * Fixed a memory leak affecting some customers with a large number of model files.
  * Fixed shortcut to run query from SQL Runner (cmd+enter or ctrl+enter). See a list of all keyboard shortcuts [here](https://docs.cloud.google.com/looker/docs/keyboard-shortcuts).
  * Fixed Totals and Row Totals (e.g. `total: true`, `row_total: right`) on LookML dashboards. See [Dashboard LookML document](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard).
  * Updated version of git to ensure we weren't exposed to a potential vulnerability.
  * Added ability to sudo as another user if you are already sudoing as someone else.



## Looker 3.10 2014-12-29

### Dashboards and Visualizations

  * **User-defined dashboards:**
    * LookML to User-Defined Dashboard Import - allows users to move LookML dashboards to shared or personal Spaces
    * User interface to add filters to dashboards ([see documentation](https://docs.cloud.google.com/looker/docs/filters-legacy-dashboards))
    * User-defined dashboards are on by default (no longer a labs feature) ([see documentation](https://docs.cloud.google.com/looker/docs/creating-legacy-dashboards))
  * **Improved dashboard filters:**
    * Dashboards filters match Explore filter UI
    * Ability to hide/show dashboard filters bar
    * Changing a filter now requires "Run" button or hotkey press to refresh dashboard
  * **Redesign of top action bar:** more vertical space, move run button and gear to top right
  * **Quick Navigation in Dashboards:** Breadcrumbs to easily navigate around Spaces from Dashboards

![](https://docs.cloud.google.com/static/looker/docs/images/breadcrumbs.png)

  * **Font size:** Option to change font size for single value elements ("font_size: medium") ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#font_size))

  * **Bar charts:** new visualization type ([see documentation](https://docs.cloud.google.com/looker/docs/bar-options))

  * **Gridlines:** x and y axis gridlines visualization option ("x_axis_gridlines: true") ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#x_axis_gridlines))

  * **Multiple pivoted measures:** now supported in visualizations

  * **Default x axis label:** now automatically fills with field name (This changes the existing default chart behavior)

  * **Show/hide axis labels and ticks:** Ability to turn off x and y axis labels and ticks ("show_x_axis_label: false", "show_x_axis_ticks: false") (see documentation)

  * **Swap axes:** Ability to swap x and y axis, creating a "sideways" graph (see documentation)




### Collaboration and Spaces

  * Welcome note and "how to" for new users in their space
  * Search current space by default with option for searching all



### Enterprise, Platform, and Security

  * Ability to view embed user settings
  * User picker to add users to a role



### Explore

  * Redesign of top action bar: more vertical space, move run button and gear to top right
  * Quick Navigation in Explore: Breadcrumbs to easily navigate around Spaces from Explore
  * Added keyboard shortcuts: for common actions (see gear in top right) ([see documentation](https://docs.cloud.google.com/looker/docs/keyboard-shortcuts))
  * Inclusive date filters: Added a new "in range" date filter that is inclusive on both sides



### LookML and IDE

  * New join syntax:
        
        - join: <view>
            type: left_outer | full_outer | inner | cross   # defaults to left_outer
            relationship: one_to_many | many_to_one | one_to_one | many_to_many
            sql_on: ... # use sql_on, sql, or foreign_key
        

  * Label option for models: Added label: for models

  * Show regex errors in project search

  * Liquid conditions now work in fields




### General Improvements and Tweaks

  * Fixed a bug where filter suggestions did not appear when first focusing on the filter
  * Exclusion filter (not equal to) no longer excludes NULL
  * Disable suggestions when using sql_always_where ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-explore-sql-always-where))
  * Fixed memory leak issue affecting Lookers with a large number of model files
  * Default to Production Mode on embed if user is logged into dev mode in the same browser session



## Looker 3.8 2014-12-01

### Dashboards and Visualizations

  * **User dashboard filters** : User dashboards (non-LookML) now allow filters ([see documentation](https://docs.cloud.google.com/looker/docs/filters-legacy-dashboards))
  * **Dropoff percent** : option for grouped column charts ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#dropoff))
  * **Show view name** : option to show/hide "VIEW NAME" on visualizations and dashboards* ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#view))
  * **Hidden series** : Determines which series will begin hidden in the UI ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#hidden))
  * **Totals** : Totals now display on LookML dashboard elements ("total: on" and "row_total: right") ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#total))
  * **Show values** : Display values above data points on charts ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#value))
  * **Improved null handling** : Discontinuous null option for line and area charts ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#discontinuous))
  * **Series Labels** : Set the label of the series based on the dimension values
  * Cleaner formatting for column charts w/ time dimension on the x-axis ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element#datetime))
  * Series toggle on/off is saved with the visualization
  * **Dashboard embedding** : Add /embed/ to embed a dashboard (requires login)



### Enterprise, Platform, and Security

  * Developer Constraints: Configure a model (and thus a developer) to a specific set of connections
  * New custom permission options ([see documentation](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles)): 
    * download_with_limit: download queries with a limit
    * download_without_limit: download queries that don't have a limit
    * save_content: save and edit looks and dashboards
    * schedule_look_emails: schedule a look to send emails
  * Admin settings for technical email contacts, downtime alerts, and instance update time windows



### General Improvements and Tweaks

  * Clicking dashboard element title will always retain the vis config settings in Explore
  * Dozens of bugs squashed, especially around dashboard and visualizations, huzzah!



## Looker 3.6 2014-11-03

### Organization and Collaboration

  * **Introducing Spaces!** Organize looks and dashboards into shared spaces (e.g. "Marketing", "Q4 Sales Review"). There is still a space for each user in Looker, and you can bulk move and copy items between spaces. ([see documentation](https://docs.cloud.google.com/looker/docs/organizing-spaces))



### Explore

  * Row totals option when pivoting: add a total across a row in addition to down a column
  * Future date shortcuts in advanced filters ("tomorrow", "next week", "next month", "next year")



### LookML

  * **LookML Validator:** Check an entire project for LookML issues all at once, ensuring that everything is working as expected.
  * When pivoting, add `direction: column` to type `percent_of_total` to calculate down the column instead of across a pivot. Use `direction: row` (default) to calculate across the row instead.
  * **LookML Deprecation Warnings (Looker Labs):** The LookML editor will show warnings for LookML options that have been obsoleted by a newer option.



### Enterprise, Platform, and Security

  * **Google Authentication (OAuth):** Looker can authenticate users against your Google-managed domain ([see documentation](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google))
  * Custom permission to disable SQL Runner for specific users



### General Improvements and Tweaks

  * **Looker Labs** : We've added a section in the admin panel where you can get access to experimental features we are cooking up
  * Major app performance improvements. Speedier rendering of large data tables, dashboards, and page loads
  * Responsive LookML dashboard layouts with `layout: grid` ([see documentation](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard))
  * Epoch time fields respect convert_tz: false (disable timezone conversion)
  * Allow percent_of_total and percent_of_previous when a row limit is reached
  * Users only see looks and dashboards if they have model access



## Looker 3.4 2014-10-06

### Visualizations

  * Instant Dashboards (beta): Dashboards will display the previous run's data while new queries are run in the background, allowing information to appear instantly. This feature can be turned on in the admin section of your Looker.



### Explore

  * Explore page and dashboards, the tab icon animates while queries are running, and shows a checkmark when the queries have completed. This makes it easier to leave Looker running in the background while you work on other things.



![](https://docs.cloud.google.com/static/looker/docs/images/field-description.png) \- Field descriptions: Add descriptions to your fields in LookML. Descriptions appear in the Field Picker on the explore page. Descriptions provide a way to explain to users exactly what a dimension or measure means.

#### Field Description Example
    
    
    - dimension: sale_price
      description: 'Customers price'
      type: number
    decimals: 2
      sql: ${TABLE}.sale_price
    

### LookML

  * Adds ability to "alias:" dimension_group fields



### Enterprise, Platform, and Security

  * [Custom Roles Types](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) \- mix and match permissions to create new role types.
  * Added permission option to configure which users can share Looks publicly
  * Added permission option to configure which users can see LookML
  * Support for IBM DB2



## Looker 3.2 2014-09-08

### UI / UX

  * [User-created dashboards](https://docs.cloud.google.com/looker/docs/creating-legacy-dashboards).



### Explore

  * GUI for Filters - drop-downs, calendar picker, and more
  * Keyboard shortcuts for run query, save, and clear query (cmd+enter, cmd+s, cmd+k)
  * Dialog to specify filename for downloads



### LookML / Projects

  * LookML `base_view:` keyword changed to `explore:` (`base_view` is deprecated but backward compatible)
  * LookML `detail:` keyword is now `drill_fields:` (`detail:` is deprecated but backward compatible)
  * Added `suggestable: false` parameter to disable filter suggestions for a field



### Enterprise, Platform, and Security

  * (Beta) Embeddable functionality: SSO, Whitelabel / OEM, Look and Dashboard embedding
  * Roles - Create custom user roles and domains (access levels)



### Bug Fixes and Tweaks

  * Redshift use "terminate" instead of "cancel"
  * Syntax highlighting in SQL Runner
  * Short URL to query also contains last visualization configuration
  * Automatic time zone conversion for Oracle
  * Style updates on 3.0 release (thanks beta testers!)
  * Error messaging improvements
  * Show warnings when fields are not available



## Looker 3.0 2014-08-11

### UI / UX

  * All new style and design!
  * User-configurable charts on the Explore page (not LookML)



### Explore

  * Column (Pivot) Limit - Specify the # of columns to display in addition to rows



### LookML / Projects

  * Providing [suggestions for filters](https://docs.cloud.google.com/looker/docs/reference/param-field) \- New LookML parameters `suggest_base_view`, `suggest_dimension`, and `suggestions` for dimensions.



### Data Visualization

  * Query URLs persist visualization state
  * Embeddable iframe references a saved chart



### Enterprise, Platform, and Security

  * (Beta) Google Authentication (OAuth) - Looker can authenticate users against your Google-managed domain.
  * New User Roles: Developer, Dashboards-Only
  * Session Manager - See and revoke Looker sessions



### Bug Fixes and Tweaks

  * Add/delete projects experience improved
  * "After" date filters work



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
