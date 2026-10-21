---
url: https://docs.cloud.google.com/looker/docs/looker-4-release-notes/
title: 4.x Release Notes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:12.466880+00:00
---

# 4.x Release Notes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-4-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  4.x Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

## Preparing for Looker Releases

  * In the Looker release notes, items marked with a _flash_on_ indicate changes to existing functionality that may require your attention as you update.

  * Items marked with a _science_ indicate a [Looker Labs](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#labs_overview) feature that must be enabled by an admin on the Labs page.

  * We occasionally retire features. You can plan for this with the [Legacy Features End-of-life Schedule](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067).




## Looker 4.22 2017-09-10

### Dashboards and Visualizations

  * **Required Filters for Dashboards.** Dashboard filters can now require a filter value input before the dashboard is run. [Learn more](https://docs.cloud.google.com/looker/docs/filters-legacy-dashboards#requiring_a_filter_value).
  * **Timeline Visualization improvements.** Added the ability to plot multiple events on a single line and introduced a legend option. [Learn more](https://docs.cloud.google.com/looker/docs/timeline-options).



### Platform and Administration

#### SQL Runner

  * Added the ability to sort SQL Runner results.
  * You can now execute DDL statements via the SQL Runner. [Learn more](https://docs.cloud.google.com/looker/docs/sql-runner-basics#modifying_database_schema_and_data).



#### Instance Administration

  * **Authentication.** Added support for OpenID Connect, including group-to-role and User Attribute mapping. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-openid-connect).
  * **Access.** Added a Help menu option to manage Looker Support access to your instance. By default, access will remain the same. With the `support_access_toggle` permission, developers can also manage access. If support does not currently have access to your instance, this will not change that. [Learn more](https://docs.cloud.google.com/looker/docs/support-access-customer-hosted-deployment).
  * **Usage.** Added edit links from certain i__looker fields to edit pages in the Administration Panel. [Learn more](https://docs.cloud.google.com/looker/docs/creating-usage-and-metadata-reports-with-i__looker#useful_fields_in_the_user_explore).



#### Legacy Features

  * _flash_on_ Removed the Legacy Drill Behavior feature.



#### API

  * Added a `content_metadata_id` for Look and dashboard lookups.



#### Powered by Looker

  * Added parent-to-iframe JavaScript events for updating Look and dashboard filters.



### LookML and Development

  * **Dynamic grouping, aggregation, and user-inputted variables.** Introducing the `parameter` liquid variable, which allows users to insert a string or number into LookML, providing for more flexible Looks and dashboards. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter).
  * _flash_on_ **Improved the LookML Validator** to better identify when fields have duplicate declarations of the same parameter. This may surface previously ignored errors.
  * **Statistics in Table Calculations. [BETA]** Added 55 new Calculations to allow for statistical analysis. [Learn more](https://docs.cloud.google.com/looker/docs/functions-and-operators).



### Content Management and Discoverability

  * **Browse menu navigation.** The Browse menu now has links to Spaces and the Popular, Favorites, Recently Viewed pages for quicker navigation. [Learn more](https://docs.cloud.google.com/looker/docs/finding-content#navigate).
  * **Lookless Dashboards. [BETA]** Dashboards can now be composed of Tiles, which are not backed by Looks, can be created directly from an exploration without the need to save a Look, and live exclusively on the dashboard. Simplify dashboard creation and content management! [Learn more](https://docs.cloud.google.com/looker/docs/creating-legacy-dashboards).



### Scheduling and Downloading

  * **Just send it.** Added an Explore option to send data or visualizations without having to create a schedule. [Learn more](https://docs.cloud.google.com/looker/docs/send-once).
  * Updated the Scheduler History page to include information about Datagroup triggers.



### Dialects

  * **Exasol.** Added support for medians and percentiles. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median).



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * Fixed an issue where scrolling caused map legends to flip when reverse color scale was enabled.
  * Fixed an issue where the Save button could be obscured when editing the styling of an embedded Dashboard.
  * Fixed an issue where y-axis names didn't appear with pivoted data.
  * Fixed an issue where public Looks containing Conditional Formatting did not load.
  * Fixed an issue editing a Look could result in an error.
  * Fixed an issue where searching for collapsed dimension groups did not properly expand them in the field picker.



#### LookML

  * Fixed an issue where not all timeframes were included by default for dimension groups.
  * Fixed a couple of issues related to LookML generation and database columns that start with `_`.
  * Fixed an issue where an empty action declaration caused a 500 error.
  * Fixed an issue where `value_formats` could display minus signs when they shouldn't have.



#### Scheduling and Downloading

  * Fixed an issue where filtered scheduled emails did not properly link back to a filtered version of the original Look.
  * Fixed an issue where new Google Spreadsheets public URLs led to a 404.
  * Fixed an issue where downloading a PDF could generate an Unexpected Document Error.



#### Administration

  * Fixed issues related to timezone conversions and Oracle SQL.
  * Fixed an issue where users could not connect to a User Attribute-determined host.



## Looker 4.20 2017-08-13

### Scheduling and Downloading

  * **Introduced the ability to schedule Looks and dashboards when an ETL completes.** Scheduled content can now be sent based on a datagroup trigger in addition to the existing time-based options. [Learn more](https://docs.cloud.google.com/looker/docs/scheduling#trigger_options_\(for_developers_and_admins\)).
  * **Remove links to Looker.** Added a scheduling configuration option to include or exclude links back to Looker from emailed content. [Learn more for Looks](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#include_links). [Learn more for dashboards](https://docs.cloud.google.com/looker/docs/delivering-legacy-dashboards#include_links.)
  * _flash_on_ **Downloads will now default to having formatted values.**



### Platform and Administration

  * **Powered by Looker**
    * Added the ability to broadcast iframe height to the parent page.
  * **SQL Runner**
    * Added a Connection panel option to disable schema pre-caching. [Learn more](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#sql_runner_precache).
  * **Legacy Features**
    * _flash_on_ Disabled the following [Legacy Features](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067): 
      * Non-Symmetric Aggregates
      * Row Limit Only
      * Unsafe Liquid Functions
      * Allow creating legacy API-only users



### LookML and Development Environment

  * **New minuteX timeframes.** Added new 4, 20, 6, and 12 minute timeframes. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#minutex).
  * [_science_ Experimental Labs] Added an experimental Labs feature that will speed up LookML validation by not revalidating explores that haven't changed. [Learn more](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_only_updated_lookml).



### Dialects

  * **Amazon Athena.** Introduced support for Symmetric Aggregates. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-explore-symmetric-aggregates).
  * **DataVirtuality.** Added `case_sensitive` support where possible. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-model-case-sensitive#common_challenges).
  * _flash_on_ **Apache Spark 1.5+, Apache Spark 2.0, Apache Hive2, and Cloudera Impala.** Derived tables now use columnar formats and compression.
  * _flash_on_ **Aster Data, Exasol, PostgreSQL, Amazon Redshift, Snowflake, Vertica, and Greenplum.** Sped up queries by no longer using `to_char` in `group by` statements for date timeframes.



### General Tweaks and Bug Fixes

#### Filters

  * The Filters section in explores is now scrollable.
  * Restored the ability to copy filter values.



#### Content Management and Discoverability

  * Added the ability to bulk add LookML Dashboards to Spaces as user-defined dashboards. [Learn more](https://docs.cloud.google.com/looker/docs/converting-lookml-to-user-defined-dashboard#bulk_import).
  * Fixed an issue where the Spaces page would not load if a user did not have access to a Space.
  * Fixed an issue where individual bulk Space actions were not available to users who could not perform copy, move, and delete actions.
  * Fixed an issue where the Save & Add to Dashboard button missed the Add to Dashboard step.
  * Fixed an issue where users could not parameterize Project names using User Attributes.
  * Fixed an issue where Funnel visualizations could fail to render on User Defined Dashboards.
  * Fixed an issue where the LookML Validator incorrectly produced a Redefinition of field error when a dimension group did not have a raw timeframe and another field had the same name.



## Looker 4.18 2017-07-16

### LookML

  * [_science_ Labs] **Native Derived Tables** Derived tables can now be composed with LookML rather than being defined with a simple SQL block. [Learn more](https://discourse.looker.com/t/using-native-derived-tables-labs-feature/5394).
  * **Introduced Liquid parameters to identify a field's presence in a query.** Use `_is_selected`, `_is_filtered`, and `_in_query` to build dynamic behavior based on the fields and filters of a query. [Learn more](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#usage_of__in_query,__is_selected,_and__is_filtered). 
    * _flash_on_ `_in_query` now returns true if a field is in the data table, the filter set, or is being automatically included with `required_fields` or similar parameters.
  * **Introduced the`_filters['view.field']` Liquid parameter.** This allows you to grab a query's current filters, especially useful for cross-dashboard linking as well as hyperlinking to Looks, queries, or other `link` values. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-field-link#passing_a_query%E2%80%99s_filter_values_into_a_link).
  * _flash_on_ **Dashboard, Look, and explore links can now open in the same page or iframe.** `link` values with absolute URLs will continue to open in a new tab while root-relative ones will remain in the current iframe or browser tab.
  * Added the ability to declare a `description` on LookML dashboards. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#description_\(for_dashboard\)).
  * The LookML generator now automatically applies `map_layer_name` to country fields. [Learn more](https://docs.cloud.google.com/looker/docs/generating-a-model).



### Looker Platform and Administration

  * **Segment Integration**. Introduced an integration with Segment that will allow you to schedule data to be connected to third party applications for automating workflows. [Learn more](https://discourse.looker.com/t/looker-integrations-segment/5420).
  * [_science_ Labs] **SQL Runner**. Introduced the ability to search for all of the fields, schemas, and tables on a given connection. [Learn more](https://docs.cloud.google.com/looker/docs/sql-runner-basics#searching_your_database).
  * **Filters** Suggestions to now match partial words and rank suggested filter values based on relevance.
  * **API**
    * **Project management.** Added endpoints to configure a LookML Project's Git settings and generate and fetch public-private SSH key pairs.
    * **Dashboards.** LookML `dashboard_elements` can now be directly associated with a query rather than be routed through a Look.
    * **Dashboards.** `dashboard_elements` now have a `title_text` parameter that will override the Look title or will provide a title if there is no associated Look.
  * **Instance Administration**
    * **Legacy Features.** Updated the Legacy Feature program to provide greater clarity into deprecation timelines and to add deprecation releases for existing Legacy Features. [Learn more](https://docs.cloud.google.com/looker/docs/legacy-features).
    * **Authentication.** Updated the SAML setup page to clarify the IdP Audience field's relationship to the SP Entity ID.
    * _flash_on_ **Permissions.** The **Rebuild Derived Tables & Run** query option will now only be available to those with the Develop permission. [Learn more](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#forcing_new_results_to_be_generated_from_the_database).
    * **Schedule Management.** Updated the Scheduler History Admin panel to include information whether or not the job was a test and the type of scheduled job it was. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule-history).



### Dialects

  * **Amazon Athena.** Query killing is now supported.
  * **Netezza.** Added initial support for Netezza.



### General Tweaks and Bug Fixes

#### Scheduling and Downloading

  * _flash_on_ The **Edit Schedule** gear menu option now says **Add Schedule** if no schedule exists.
  * _flash_on_ Added an identifier to files sent to S3 and SFTP to ensure file names are unique.
  * Users can now download data from the drill modal. [Learn more](https://docs.cloud.google.com/looker/docs/exploring-data#drilling_down_into_the_data).
  * The Scheduled Plan Dialog now closes with the ESC key.
  * Fixed an issue where email addresses removed from a schedule were still listed on the External Emails Admin page.
  * Fixed issues related to zooming on PDF versions of maps.
  * Fixed an issue where scheduling to SFTP could send an empty file.
  * Fixed an issue where Automagic Heatmap Map visualizations could generate empty PNG files.
  * Fixed an issue where empty Totals rows could cause an export to fail.
  * Fixed an issue where "View this data in Looker" links in scheduled emails could lead to an invalid page.
  * Fixed an issue where visualization issues could result in an empty CSV download.



#### Dashboards and Visualizations

  * The vertical order of series in legends now matches their order in stacked Column visualizations.
  * Fixed an issue where stacked Column visualization value labels did not properly hide.
  * Fixed an issue where tooltips did not appear on Area visualizations.
  * Fixed an issue where Timeline visualizations rendered blank due to invalid value format values.
  * Addressed a number of issues related to having multiple maps on a Dashboard.
  * Fixed an issue where clicking "View Access Settings" from a Dashboard's gear menu lead to an endlessly spinning page.



#### Spaces and Content Management

  * When LookML dashboards are imported into a Space, the banner notifications now link to the dashboard and Spaces to which it was moved.
  * Fixed an issue where a user was displayed the Explore From Here link in Spaces despite not having the permissions to do so.
  * Fixed an issue where, after moving a Dashboard, its Looks remained in the departure Space until the page was refreshed.



#### Instance Administration.

  * Fixed a bug where Groups could not be added to an individual user's Space in a closed system.
  * Fixed an issue where SAML users' authentication errors were not appearing on the login page.
  * Fixed an issue where SAML, LDAP, or Google Auth users could be sent password reset emails despite having no password to reset.
  * **Google BigQuery.** Fixed an issue where Max Billing Gigabytes entries could fail to validate.
  * Fixed an issue where grouped Explores did not sort correctly.
  * Fixed an issue where the browse Spaces icon was missing in embedded contexts.
  * Fixed an issue where users could not edit their email preferences.
  * Fixed an issue where Access Filters in Liquid conditions caused erroneous errors.
  * Fixed an issue where certain timeframes produced erroneous to allow_fill warnings.
  * Fixed an issue where the Help menu's search bar was unresponsive.
  * Fixed an issue where markdown tables could render with very narrow columns.
  * Fixed an issue where the `pivot_where` Table Calculation would erroneously error.



## Looker 4.16 2017-06-11

### Scheduling and Downloading

  * **Apply Table visualization configurations to scheduled and exported content.** Table visualization options (including renamed series, hidden columns, and totals) are now available in downloads, schedules, and public Looks. You can still download from the data table if you'd prefer, although the visualization is the default option. [Learn more about downloading](https://docs.cloud.google.com/looker/docs/downloading). [Learn more about scheduling](https://docs.cloud.google.com/looker/docs/scheduling-email#apply_visualization_options). 
    * Conditional formatting and custom colors are currently not applied. Images and HTML applied to table values will not carry through.
    * _flash_on_ If you are exporting to Google Sheets and using the `lookerFetchHtmlTable()` function, you should replace it with `lookerFetchData()`. [Learn more](https://community.looker.com/technical-tips-tricks-1021/exporting-data-to-google-sheets-30229).
  * Scheduled Look and dashboard delivery format choices were reorganized for better clarity.
  * Added the option to select TLS and SSL versions if enabled on the SMTP admin panel.



### Dashboards

  * _flash_on_ **Introduced an on-element toolbar for editing individual dashboard elements.** [Learn more](https://docs.cloud.google.com/looker/docs/editing-legacy-dashboards#editing_tiles).
  * _flash_on_ When loading a dashboard, the **dashboard element rendering order now prioritizes elements in the current viewport.** [Learn more](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards#refreshing_data_in_a_dashboard).



### Explore

  * **Instant Insight.** Introduced the ability to creating an on-the-fly Explore for a SQL query or database table. [Learn more](https://docs.cloud.google.com/looker/docs/sql-runner-basics#getting_insight_into_data_by_creating_an_on-the-fly_explore).
  * **Added a search bar to the Explore menu.** [Learn more](https://docs.cloud.google.com/looker/docs/exploring-data-intro).
  * **Added the ability to drill on null values.**



### Content Management and Discoverability

  * **Reintroduced pagination for Spaces.** Looks and dashboards are now capped at 30 per page, with the option to page forward to see additional content. This does not apply to the LookML dashboards Space.
  * _flash_on_ The model name associated with Looks and dashboards is now displayed only if there is more than one model used in that Space. [Learn more](https://docs.cloud.google.com/looker/docs/finding-content#viewing_lists_of_looks_and_dashboards).



### Looker Platform and Administration

  * **Smarter Query Caching.** `datagroups` will allow you to set LookML triggers and intervals to refresh your query cache, as well as define a maximum potential cache age. [Learn more](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters).
  * **SAML integration improvements.**
    * Added the ability to map user attributes directly to SAML attributes rather than requiring user attributes map to SAML Groups. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml#user_attributes_settings).
    * Introduced the ability to set default Groups for SAML and LDAP integrations. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml#role_settings).
    * Added a Group Finder Strategy to set groups as individual SAML attributes with a membership value. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml#role_settings).
  * _flash_on_ **Beta API changes.**
    * The `scheduled_plans_for_space()` route now returns both disabled and enabled plans.
    * Project file routes now include deleted files.
    * Added an `update_session()` endpoint to switch to and from development mode.
  * _flash_on_ Introduced the "User-based dev mode" Legacy Feature
  * _flash_on_ On the Edit Group page, limited the displayed roles to those related to a given group.
  * License keys are now hidden by default on the Admin panel. Click **Show** to display the full key.



### LookML and Development Environment

  * **Added the`tags` parameter**, which allows you to provide arbitrary metadata to any LookML field. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-field-tags).
  * [_science_ Labs] **Project Importing.** This experimental Labs feature enables extensions across projects. [Learn more](https://discourse.looker.com/t/experimental-lab-feature-importing-files-from-other-lookml-projects/5179).



### Dialects

  * _flash_on_ **Google BigQuery.** Now perform case insensitive filtering by applying `lower()` and performing an equality match.
  * **MemSQL**
    * _flash_on_ Where possible, `date_trunc()` will be used for timeframes rather than `date_format()`.
    * Updated to the new driver to allow for SSL connections.
  * _flash_on_ **DataVirtuality.** Where possible, `cast()` will be used for timeframes rather than `formattimestamp()`
  * **SAP HANA.** added support for Symmetric Aggregates and Persistent Derived Tables.
  * **Athena.** Updated the driver to 1.1.0.
  * **Impala.** Added the ability to authenticate with a user and password when using Cloudera native drivers.



### General Tweaks and Bug Fixes

  * Table Calculations and Custom Filters now autocorrect case sensitivity issues and provide better warnings in the event of improper constant usage (`Yes` vs `yes`, for example).
  * Fixed an issue where Table Calculations were not displayed in a visualization when all other fields were hidden.
  * Fixed an issue where conditional formatting did not color small decimal values.
  * Fixed an issue where the background color of embedded Funnel visualizations was not fully applied.
  * Fixed an issue where text Dashboard Elements did not properly wrap on Internet Explorer.
  * Fixed an issue where `group_labels` did not properly wrap.
  * Fixed an issue where users with no Roles could not load the Spaces page.
  * Addressed an issue where new sub-personal Spaces did not appear until the page was refreshed.
  * Fixed an issue where the LookML Dashboards Space was not visible in certain cases.
  * Fixed an API issue where sql_table_name was not included in the `lookml_model_explore()` output.
  * Fixed an issue where dimension fill would re-enable when dimensions were added or removed.
  * Addressed an issue where dimension fill would warn when no results were returned.
  * Addressed issues related to `datatype: date` on several SQL dialects.



## Looker 4.14 2017-05-14

### Dashboards, Visualizations, and Explores

  * **Introduced the Timeline visualization.** [Learn more](https://docs.cloud.google.com/looker/docs/timeline-options).
  * **A field's`description` will now appear in a tooltip** when hovering over the column header on dashboards, Looks, or explores. [Learn more](https://docs.cloud.google.com/looker/docs/legacy-table-options#tooltips_for_table_columns).
  * **The explores in the Explore menu can now be organized** using the `group_label` LookML parameter. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-explore-group-label).
  * **Dashboard filters can now be configured to accept just a single filter value.** [Learn more](https://docs.cloud.google.com/looker/docs/filters-legacy-dashboards#limit_the_number_of_values).
  * **The`vector_tile_region` map layer now has an option to display outlines of regions without data.** [Learn more](https://docs.cloud.google.com/looker/docs/map-options#gridlines_on_empty_regions).



### Looker Platform and Administration

  * _flash_on_ **Content Access is now entirely governed by Space Access Controls.** [Learn more](https://discourse.looker.com/t/content-access-in-looker-4-10-and-looker-4-14/4582).
  * _flash_on_ **Introduced the "Allow unlimited downloads that might crash Looker" Legacy Feature.** [Learn more](https://discourse.looker.com/t/legacy-feature-allowing-unlimited-downloads-looker-4-14/4987).
  * **Added new API endpoints:**
    * API endpoints for reading project information.
    * API endpoint for LookML validation.
  * You can now filter tables on the Persistent Derived Tables Admin panel. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#filtering_the_pdt_panel).
  * Looker will now pull avatars from Google if you're using Google Auth.
  * Renamed the **Edit Look Settings** gear menu option to **Edit Settings**.



### LookML and Development Environment

  * The LookML generator will now create dimensions of `type: zipcode`.
  * _flash_on_ Replaced the individual Create Model, Create Dashboard, Create Document, etc. options with a single Add Files menu in the LookML development environment. [Learn more](https://docs.cloud.google.com/looker/docs/model-and-view-files#creating_model_files).
  * Removed the striped gradient from the Development Mode banner.



### Dialects

  * **Amazon Spectrum.** Added support for Amazon Spectrum. [Learn more](https://discourse.looker.com/t/using-amazon-redshift-s-new-spectrum-feature/4975).



### General Tweaks and Bug Fixes

  * Fixed a couple of issues related to labels and pie charts.
  * Fixed an issue where selecting Filter from the data table didn't open the filter panel.
  * Fixed an issue where `all_scheduled_plans()` did not return scheduled plans.
  * Fixed some table alignment issues when row totals are present but dimensions and row numbers are not.
  * Fixed an issue where creating a view from a table could overwrite an existing view if it had the same name.
  * Addressed some issues related to manually defining `vector_tile_region` map layers.
  * Tweaked Look and dashboard pages to improve header text alignment.



## Looker 4.12 2017-04-16

### Dashboards and Visualizations

  * **Improved dashboard creation and editing workflow.**
    * You can now create a blank dashboard from the Spaces page.
    * Dashboard titles can be edited directly from the dashboard page.
    * Dashboards can be deleted from the dashboard page.
    * _flash_on_ Edit mode for dashboards now displays the options to add Looks, Text elements, as well as configuration settings and filters in a toolbar rather than in the gear menu.
  * **Dashboard text elements now accept certain Markdown tags for formatting and rendering links.**
  * **Added a dashboard gear menu option to get the dashboard LookML associated with a user-defined dashboard.**
  * **Updated touch options for Visualizations on mobile.**
    * Pressing and releasing will bring up the tooltip for a data point.
    * Pressing and dragging along a chart will display tooltips for whichever datapoint is being touched.
    * Pressing and holding on a single data point will bring up the drill modal.
  * Updated the display for dashboards with elements in multiple timezones.
  * _flash_on_ Collapsed dashboard filters bars now display the filter value for a User Attribute rather than the Attribute name.
  * _flash_on_ Removed text elements from a dashboard's edit settings.
  * _flash_on_ Clicking a dashboard element's title now directly launches an Explore instead of opening the gear menu.
  * _flash_on_ **Changed beta dashboard API routes** , consolidating LookML and user-defined dashboard routes. Impacted APIs include, but are not limited to: 
    * Dashboards
    * Spaces
    * Looks



### Scheduling and Downloading

  * **Introduced the ability to add text to scheduled Looks and dashboards.**
  * **Filterable scheduling is now available on Looks.**
  * **Added a new Inline Image scheduled dashboard type** that mirrors dashboard display in Looker.
  * **Improved Filtered Schedules.**
    * User Attribute-based filter values now display in filtered schedules.
    * If a piece of content is scheduled to more than one user and the schedule fails, the recipient will be displayed in the error email.
    * _flash_on_ "View this data in Looker" links now take users to filtered versions of the Look or dashboard if the email is for a filtered piece of content.
  * Improved the error message produced when scheduling to an email address that is not in a whitelisted domain.



### Dialects

  * **Google BigQuery.** Added the ability to download unlimited results.
  * **Impala.** Added the ability to configure Looker to use Cloudera-provided drivers. [Learn More](https://discourse.looker.com/t/configuring-looker-to-use-impala-jdbc-connector-for-cloudera-enterprise/4772).
  * _flash_on_ **Denodo.** Switched to `LIKE` from `REGEXP_LIKE` for string comparisons.



### LookML

  * **Introduced`percentile` and `percentile_distinct` measure types for certain dialects.** [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#percentile).
  * **Introduced`median` measure type for certain dialects.** [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median).
  * **Introduced`median_distinct` measure type for certain dialects.** [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#median_distinct).



### General Tweaks and Bug Fixes

  * _flash_on_ Addressed an issue where downloading sometimes lead to a `404` or `500` response. Created a new Lookerbot release as a result. [Learn more](https://github.com/looker/looker-slackbot/releases).
  * Updated Data Actions to include the ability to provide a description for form fields, better error messaging, and a beta API endpoint.
  * **Google BigQuery.** Fixed an issue where filtered results were incorrect when using the `case_sensitive` parameter.
  * Clarified definitions of Labs features in the Admin panel.
  * The Content Validator now updates "Explore From Here" Look and dashboard links.
  * Addressed an error message that appeared if a view's primary key was not included in a `fields` list.
  * Addressed a series of incorrect error messages that appeared before a Look or dashboard element ran.
  * Addressed a number of `extends`-related LookML issues.
  * Added more precision to the Funnel visualization for comparing small values.
  * Fixed an issue where drill links were not displayed for Funnel visualizations.
  * Fixed an issue where dashboards with only Text elements would not appear in Spaces.
  * Fixed an issue where deleted content would be included in counts in Spaces.
  * Fixed an issue where the Choose Looks modal did not populate if there was a deleted Look on a dashboard.
  * Fixed an issue where a series's settings were not preserved after moving between axes.
  * Fixed an issue where duplicate browser history events were produced for a single dashboard page load.



## Looker 4.10 2017-03-19

### Dashboards and Visualizations

  * **Selective assignment of series to y-axes.** Create or combine any number of y-axes. [Learn more](https://discourse.looker.com/t/updates-to-the-y-axis-editor/4504).
  * **Introduced a Funnel visualization type.** [Learn more](https://discourse.looker.com/t/funnel-visualization/4503).
  * **Added Visual Drilling to the Labs menu** , allowing it to be disabled if so desired. [Learn more](https://discourse.looker.com/t/visual-drilling/3574).
  * Table Visualizations in PDFs now show their full width.



### Administration

  * **User Attributes as a Access Filter mechanism.** User Attributes can now govern Access Filters, providing for Group-level assignment. [Learn more](https://discourse.looker.com/t/access-filters-with-user-attributes/4596).
  * **Improved User Specific Time Zones.** [Learn more about the enhancement](https://docs.cloud.google.com/looker/docs/using-time-zone-settings). [Learn about the legacy feature](https://discourse.looker.com/t/legacy-feature-implicit-dashboard-default-timezone-looker-4-10/4500).



### Dialects

  * **Google BigQuery.** Introduced a Max Billing Gigabytes connection parameter which can be used to limit the size of any single query. It can also be tied to a User Attribute value.
  * **Introducing support for Google Cloud PosgreSQL.**
  * **Introducing initial support for Google Spanner.**
  * **Snowflake.** Updated to the latest driver.



### General Tweaks and Bug Fixes

  * **LookML and Development Environment.**
    * Added missing quick help docs when the cursor is placed at the start of LookML blocks.
    * Fixed an issue with multi-line pasting in the new IDE.
    * Fixed an issue related to LookML validation when `extension: required` is used.
    * Fixed an issue related to `from` and `view_name` explore inheritance.
    * Fixed an issue where saving could hang.
  * **Dialects.**
    * **Amazon Athena.** Fixed an issue where the LookML generator did not see more than 100 tables across all databases.
    * **Google BigQuery.** Addressed an issue related to casting dimensions with `datatype: date`.
  * _flash_on_ **Addressed inconsistent Look and dashboard presentation in Spaces** for users with `access_data` and `see_user_dashboards` and users with just `see_user_dashboards`. Users' ability to query reports has not changed. [Learn more](https://discourse.looker.com/t/content-access-in-looker-4-10-and-looker-4-12/4582).
  * **Fixed an issue where the edit modal would occasionally not return data.**
  * **Looks & dashboards can now be moved into personal Spaces.**
  * _flash_on_ **The Save button on the Explore page will now return you to the Explore Page** instead of taking you to the Look.
  * _flash_on_ Filter values rather than filter names are now displayed in bold when the filters bar is collapsed.
  * _flash_on_ Deleted Looks will no longer appear in the Content Validator.
  * Hovering over relative timestamps now displays the exact time.
  * Added the ability to copy values from SQL Runner Tables & Drill Overlays.
  * Improved error messages related to malformed tiers and views without `primary_key` dimensions.
  * Addressed an issue where unchecking a default role on a user did not remove that role.
  * Fixed an issue where single value visualizations would be cut off in scheduled inline dashboards.
  * Increased the size of click targets on mobile dashboards and visualizations.
  * Fixed an issue related to MandrillApp and custom SMTP settings that occasionally caused scheduled dashboard elements to render empty.
  * Fixed an issue where downloaded files could not be renamed.
  * Fixed an issue where dashboards could not be renamed.
  * Fixed an issue where Looks and dashboards could be missing from Spaces if a Space was moved into another.
  * Fixed an issue where sorts were not respected in Explores with a single, pivoted dimension.
  * Fixed an issue where Looker-generated SQL incorrectly escaped regex special characters in regex string comparison.
  * Fixed an issue where the Rebuild Derived Tables & Run option was hidden when `persist_for: 0 seconds` was declared.



## Looker 4.8 2017-02-20

### Scheduling and Downloading

  * **Filterable dashboard schedules.** Introduced the ability to change filter values for each schedule associated with a given dashboard.
  * **Inline Tables is now the default email delivery option for new scheduled content.** Existing schedules won't be changed.
  * **Added API support for downloading dashboard PDFs.**



### Dashboards and Visualizations

  * [_science_ Labs] **Conditional Formatting** for Table visualizations. [Learn more about Labs features](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs).
  * **Added drop-down options to the Add/Edit Dashboard Filters interface.**
  * **Trend Line equations and R 2**. Trend Line labels can now display the equation used for the line or the Trend Line's R2 value.



### Looker Platform and Administration

  * **Powered by Looker**
    * **Saving from an Embedded Context.** Introducing the ability for embedded users to save content, including the ability to curate content for embedded users from Spaces.
    * **Scheduling from an Embed Context.** Embedded users now have the ability to schedule Looks and dashboards.
    * Embedded Look URLs can now be modified to override filter values.
    * JavaScript embed events can continue firing across page loads.
    * Exposed embed-related `external_id` fields in already-existing `credentials_embed` and `space` routes.
    * _flash_on_ "Rebuild Derived Tables & Run" option on Explore pages is now hidden for all embedded users.
  * _flash_on_ **Changed the location of deploy keys for newly created projects.** Looker-hosted instances will not need to take any action. _Action is required for customer-hosted clusters creating new projects._ [Learn more about syncing Git SSH keys](https://discourse.looker.com/t/syncing-git-ssh-keys-for-clustered-lookers-looker-4-8/4338). [Learn more about shared storage clusters](https://docs.cloud.google.com/looker/docs/clustering-looker).
  * **Connection tests.** Added an option in the Connections Panel to test all connections or each individually.



### Content Management and Discoverability

  * **Unused Content and Trash.** Introduced two sections that allow instance Admins to, in bulk, clean up all of the unused and unneeded content on an instance. 
    * **The Unused Content page** will pull together all content that hasn't been touched in 90 days. Admins can then delete those items, which will move them to the Trash.
    * **Trash.** Items in Trash can be restored or permanently deleted at the Admin's discretion.
  * **Tables in Spaces are now sortable and are paginated**. This does not apply to the LookML dashboard space.
  * **Move and Copy Modals in Spaces now match the new Save Look modal.**
  * **Run on Load for Looks.** Introduced the ability to set whether Looks run immediately. This setting can be configured in Edit Look Settings.
  * _flash_on_ **Moved Public Access settings for Looks** to the Look Settings modal.
  * **It is now possible to delete a dashboard from the dashboard page.**
  * **Markdown file navigation.** Added the ability to create a navigation menu for Markdown documents.



### LookML and Development Environment

  * **Fiscal years and quarters.** Introduced a `fiscal_month_offset` LookML parameter to allow for custom fiscal years.
  * **Better SQL Runner error highlighting.**
  * **Projects can now include JSON files.**
  * **Updated the syntax for`map_layers`** so that they can now reference JSON files included in the project.
  * Introduced the ability to add files to a project by dragging and dropping them into the LookML IDE.



### Dialects

  * **BigQuery Standard SQL.** Improved the LookML project generator.
  * **BigQuery Legacy SQL.** Removed `EACH` from `GROUP BY`, improving performance for certain queries.
  * **Presto.** Added support for Qubole's Presto as a Service for Presto versions 0.157 and 0.142.



### General Tweaks and Bug Fixes

  * _flash_on_ Disabled the Save button from the Edit Look modal until the query is finished updating. This addresses an issue where Look edits would not persist if saved too quickly.
  * Fixed an issue where menus items that ran off the page could not be reached by scrolling.
  * Removed the Go to LookML link for users who are not able to see LookML.
  * SQL errors are now only exposed to users with the `see_lookml` permission.
  * Fixed an issue where the SQL tab was blank on Safari. Fixed an issue related to escaping the `` character in filter values.
  * Fixed an issue where Reset Look did not reset query results.
  * Fixed an issue where webhook delivery could block scheduled content delivery.
  * Fixed an issue where Single Column PDF dashboard element titles were mixed up.
  * Fixed a issue where the 'Create Schedule' option was not available in the Details pane of the Look page.
  * Fixed an issue related to downloading results from drill overlays.
  * Fixed an issues that resulted in Select 10 SQL Runner functions not working properly.
  * Fixed a SQL Runner issue related to listing tables in on Spark 2.0.
  * Group labels for measures are now the same color as measure names in the Field Picker.



## Looker 4.6 2017-01-22

### Scheduling and Downloading

  * **Multiple schedules.** Added the ability to create multiple schedules via per piece of content from the schedule modal. [Learn more](https://discourse.looker.com/t/multiple-schedules/3974).
  * **Larger scheduled result sets.** The schedule modal now has SFTP and webhook options, to which users may schedule Look results. An "all results" option is available in cases where query results may be streamed. [Learn more](https://docs.cloud.google.com/looker/docs/scheduling-ftp).
  * **Improved inline dashboard emails** to improve legibility and visual consistency.



### Dashboards and Visualizations

  * **User Attributes in Filters.** Added the ability to associate User Attribute values to filter values, allowing for parameterized content. [Learn more](https://discourse.looker.com/t/parameterized-filters-with-user-attributes/4134).
  * **Increased scrolling speed** when dragging dashboard tiles.
  * **Improved rendering of map data** by updating the mapping library.



### Content Management and Discoverability

  * **Redesigned Save Look modals** to improve Space browsing and navigation.
  * **Faceting for Top Content.** Filter and sort Top Content by Group to explore what matters most to you and others.



### Dialects

  * _Amazon Athena._ Introducing support for Amazon Athena. [Learn more](https://docs.cloud.google.com/looker/docs/db-config-amazon-athena).
  * **BigQuery Standard SQL** is now a fully supported dialect.



### General Tweaks & Bug Fixes

  * Fixed an issue where embed users could see explore pages without the `explore` permission. Users could not navigate to the embedded explore page, but could view it if given a URL with embedded explore access or devise one themselves.
  * _flash_on_ Removed Zero Fill for pivoted dimension drills.
  * Fixed a caching issue that could lead to results in browser not matching those scheduled and downloaded.
  * Fixed a broken link from the Content Validator to to Spaces.
  * Fixed an issue where users on BigQuery connections could not Refresh Tables & Tables in the SQL Runner or Create View from Table from the LookML generator.
  * **Sorting issues.**
    * Fixed an issue where a dashboard could ignore measure sort order if declared prior to pivoting.
    * Fixed an issue related to sorting Table Calculations on pivoted results.
    * _flash_on_ Nulls in pivoted measures really sort last regardless of sort order, dialect, and content type.



## Looker 4.4 2017-01-02

### Looker Platform and Administration

  * **User Attributes.** Introducing a new system whereby Users and Groups can be assigned values that can then be referenced throughout Looker. [Learn more](https://discourse.looker.com/t/user-attributes/3979). 
    * **Database connections:** The host, port, database, username, and password of a Connection can be parameterized so that each User will connect with their own credentials rather than through a single Looker user. [Learn more](https://discourse.looker.com/t/parameterizing-connections-with-user-attributes/3986).
    * **Data Actions.** Data Actions now accept User Attributes as part of their payload, allowing you to use a User's credentials to perform an operation against a particular service. [Learn more](https://discourse.looker.com/t/data-actions-with-user-attributes/3988).
  * _flash_on_ **Changes to beta API endpoints** including, but not limited to: 
    * Renamed the `filters` attribute of the `dashboard` response to `dashboard_filters`. Created a new Lookerbot release as a result. [Learn more](https://github.com/looker/looker-slackbot/releases).
    * Added `joins` attribute to the `lookml_model_explore` response class.
    * Better handle LookML field names with a `.`.
    * Added a `is_personal_descendant` flag for sub-personal spaces.
    * Deprecated `is_user_root` and `is_root` properties in the `space` response class. These will still work temporarily, but you should transition to `is_users_root` and `is_shared_root`.
  * _flash_on_ **Admin Panel Reorganization.**
    * **Regrouped items in the left navigation** , bucketing items into smaller, more specific categories.
    * **Reconfigured Labs panel** to indicate which features are beta (under development) and which are experimental (and may be discontinued).



### Scheduling and Downloading

  * **Larger scheduled result sets to SFTP via the API.** Added the ability to schedule queries with no limit to SFTP via the API.
  * **Scheduled tables now include totals and table calculations.** Improved inline table and HTML attachment scheduled Look formats to include table calculations as well as row and column totals.
  * **Improved Single Value visualization downloads.** Scheduled inline visualizations and Look downloads are captured as images rather than text, allowing comparisons, text, and generally making them more closely resemble how they appear in the web browser.



### Content Management and Discoverability

  * **Recently Viewed Content.** A list of the dashboards and Looks you have been visiting lately. [Learn more](https://discourse.looker.com/t/getting-to-what-matters-favorites-top-content-global-search/3745).
  * **Bulk delete dashboards in Spaces.**
  * **Sortable and paginated content browser.** Top Content, Favorites and Recently Viewed Content are now sortable and pages currently contain ten Looks or dashboards.



### Dialects

  * **IBM DB2.** Added support for persistent derived tables.
  * _flash_on_ **Google Cloud SQL.** Temporarily removed support for persistent derived tables. This only impacts Google Cloud SQL, not Google BigQuery Legacy SQL or Google BigQuery Standard SQL.
  * **Presto.** Added support for symmetric aggregates. Requires Presto version 0.153 or above.



### LookML

  * _flash_on_ New projects cannot be created using YAML-based LookML without the legacy feature. [Learn more](https://discourse.looker.com/t/deprecation-notice-old-style-yaml-lookml-looker-4-4/4025).
  * **`order_by_field` on measures.** Measures now accept the `order_by_field` parameter, allowing you to order query results based on another measure. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-field-order-by-field).



### General Tweaks & Bug Fixes

  * **i__looker.**
    * Added average and total runtime measures.
    * _flash_on_ Removed the total query count measure, allowing for pivoting by source.
  * _flash_on_ Reduced the number of filter suggestions from 5,000 to 1,000.
  * _flash_on_ Nulls now sort last in most pivot cases.
  * Fixed an issue where the looker.log file associated with HyperSQL application databases did not properly checkpoint.
  * Fixed an issue where downloads would fail if they included totals.
  * Fixed an issue where the Explore page could go blank after removing a table calculation.
  * Fixed an issue where columns were displayed as dimensions (blue) rather than properly displayed as table calculations (green).
  * Fixed an issue where values entered in to filters did not always make it to the SQL generated for an Explore.
  * Fixed an issue related to filtering on month or year in BigQuery Standard SQL.
  * Fixed two pivot SQL syntax issues, one related to MSSQL and one to Redshift.
  * Fixed an issue where the sort indicator on results tables did not always match the sort direction.
  * Fixed an issue where dashboards and their associated Looks could sort results differently.
  * Fixed an issue where custom Spaces Access Controls were not being displayed in the modal.
  * Fixed an issue where copying a LookML dashboard to Spaces would fail if you did not have the `see_lookml` permission.
  * Fixed an issue where users with the `see_lookml` could not see an Explore page's SQL when in an embed context.
  * Fixed an issue where gears were not clickable on mobile browsers.
  * Fixed an issue where the IDE displayed the Save button when users were not in Development Mode.



## Looker 4.2 2016-10-27

### Content Management and Discoverability

  * **Favorites.** A system for selecting and quickly navigating to the Looks & dashboards you care about most. Clicking the :heart: icon will put a link to the content piece in a list that's easy to access straight from Spaces. [Learn more](https://discourse.looker.com/t/getting-to-what-matters-favorites-top-content-global-search/3745).
  * **Top Content.** A list of the most popular Looks & dashboards on your Looker instance. This section is a great way to learn about new reports you haven't taken a look at yet. [Learn more](https://discourse.looker.com/t/getting-to-what-matters-favorites-top-content-global-search/3745).
  * **Global Search.** A search function in the navigation bar that searches across Looks, dashboards, LookML dashboards, LookML files, Explores, your Favorites, Top Content, and pages like Browse and your Account Settings. [Learn more](https://discourse.looker.com/t/global-search/3784).



### Scheduling & Downloading

  * **Added the Ability to Schedule Unlimited Results to Amazon S3.** The schedule modal now has an S3 option, to which users may schedule Look results. An "all results" option is available in cases where query results may be streamed. [Learn more about scheduling to S3](https://discourse.looker.com/t/scheduling-unlimited-results-to-s3/3785). [Learn more about streaming in Looker](https://docs.cloud.google.com/looker/docs/best-practices/row-limits-in-looker).



### Explore

  * **Streamable In-database Pivots.** Implemented streamable pivots for the majority of SQL dialects for which Looker supports query streaming (exceptions in the second link below). Baring other restrictions, query results are no longer limited to 30,000 cells and users may download results without fearing undue harm to their Looker instance. [Learn more about streaming pivots](https://discourse.looker.com/t/introducing-streaming-pivots/3768). [Learn more about streaming in Looker](https://docs.cloud.google.com/looker/docs/best-practices/row-limits-in-looker).



### Visualizations

  * Added the ability to fade one of the series on a chart when hovering. [Learn more](https://docs.cloud.google.com/looker/docs/line-options#focus-lines-on-hover).
  * Implemented logic to reduce the chances of value label collisions.



### LookML and Derived Tables

  * **Introduced the`sql_always_having` parameter**, which conceptually behaves like the `sql_always where` parameter but instead affects the `HAVING` clause of a query. The parameter can be used to limit the granularity of results an end user may see. [Learn more](https://discourse.looker.com/t/query-restrictions-on-aggregates-with-sql-always-having-looker-4-2/3736).
  * **Introduced the`allow_fill` dimension parameter**, which prevents the filling when relevant dimensions are included in a query. [Learn more about dimension filling](https://discourse.looker.com/t/introducing-dimension-fill-for-query-results/3557).
  * **Scheduled Persistent Derived Table Maintenance.** Admins can enter a cron string to govern when maintenance operations such as the trigger checker and derived table table reaper run. [Learn more](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_and_datagroup_maintenance_schedule).



### Looker Design

#### Validation

  * _flash_on_ **Renamed the Look Validator the Content Validator.** When enabled, it's still found under the Develop tab and functionality remains the same.



#### IDE Improvements

  * Added syntax highlighting to SQL blocks and LookML objects referenced in the `sql` parameter.
  * Improved readability by deemphasizing LookML punctuation such as `{` and `;;`.
  * Surfaced IDE keyboard shortcuts.
  * A personal Space will now appear at the top of the Space list in the Spaces sidebar when it is set as a default space.



### General Tweaks & Bug Fixes

#### Persistence

  * _flash_on_ **Introduced the Default query result persistence is 5 minutes legacy feature.** New instances and those with the legacy feature unchecked will default to a 60 minute query result cache. It is still possible to adjust query cache timing with model- and explore-level `persist_for` parameters. [Learn more](https://discourse.looker.com/t/change-notice-default-cache-length-4-2/3830).



#### Dimension Fill Improvements

  * No longer apply fill when filters are applied to measures.
  * Dimension filling is disabled when a non-default `order_by_field` is used.
  * Filtering on an enumeration dimension disables filling.
  * In the event that dimension filling is not possible, queries and downloads will warn and not apply filling rather than fail.



#### `i__looker` Updates

  * Usage panel dashboard tables no longer scroll. Users may still access more data by clicking Explore from here on each element.
  * Added tracking for dashboard usage to the Usage panel and the history explore.



#### LookML, Converter, and IDE Fixes

  * Fixed an issue where links didn't work on measures.
  * Addressed reference checking for `value_format_name` and `map_layer_name`.
  * Fixed an issue where new LookML did not recognize `day_of_year`.
  * The LookML conversion now automatically translates `date_date` to `date`.
  * The LookML converter will no longer fail when there are ambiguous names.
  * Fixed an issue related to pasting into the IDE.
  * The IDE no longer autosuggests immediately upon return.



#### Visualization Fixes

  * Fixed an issue related to drilling from pie charts.
  * Fixed an issue related to axis label rotation on bar charts.
  * Fixed several trend line related issues.



#### Rendering Fixes

  * Fixed an issue where text elements could break LookML dashboard downloads.
  * Fixed an issue where automagic heatmaps could not plot data.



#### Dialect-specific Fixes

  * Fixed an issue with MSSQL related to using a relative date filter with a non-US server default date format.
  * Fixed an issue related to using Custom Filters in Vertica.
  * Fixed an issue related to Symmetric Aggregates on BigQuery Standard SQL.
  * Fixed an issue where LookML dashboards could not be copied into a Space.
  * Fixed an issue where the LookML Validator errored if the `raw` timeframe is used in a set of filters.
  * Fixed an issue where the save modal would not load for certain users.
  * Fixed an issue where the chat window duplicated on the Look page and the Edit modal.



## Looker 4.0 2016-10-23

### LookML & Development Environment

  * **LookML.** Introduced a newer LookML syntax that borrows from the existing "YAML-style" LookML syntax, but brings three key improvements to the table. [Learn more](https://discourse.looker.com/t/new-lookml-why/3531). 
    * **Indentation no longer defines hierarchy.** Tab as you please (or don't) without fear of parse errors or applying a parameter to the wrong object.
    * **It is more consistent.** No more debating the "proper" way to define a list or when to quote something.
    * **LookML has meaning.** YAML provides syntax, but has no concept of relationships or rules. LookML now knows that a dimension can't be of `type: sum`.
  * **Development environment.** The improvements to the LookML syntax allow for a revamped IDE development environment. [Learn more](https://discourse.looker.com/t/new-lookml-deep-dive-into-the-new-syntax-and-the-new-ide/3539). The new IDE includes: 
    * **Autosuggest and autocompletion.** Only valid parameters and values are proposed, helping you compose new LookML quickly and accurately.
    * **On-the-fly error checking.** Just like your spell checker, the IDE will let you know that you've declared a `dimesnion` rather than a `dimension` without having to run the full LookML Validator.
    * **A context-sensitive help pane.** Dynamically updates to show you documentation relevant to what you're working on.
    * **Automatic formatting** to keep things looking good.
    * **Folding** to help you focus on what you're working on rather than getting lost in the entire file.
    * **A LookML converter** to help you transition from YAML-style LookML to the new refreshed syntax. [Learn more](https://docs.cloud.google.com/looker/docs/best-practices/how-to-convert-yaml-to-new-lookml).



> **Note** that because of LookML's more defined meaning, the LookML Validator may expose errors that were not previously surfaced. Even error-free YAML-style LookML model conversion requires developer coordination and should be viewed as a short project rather than a flip of a switch. Additionally, upon conversion all persistent derived tables will rebuild, so **please set aside some time for conversion to ensure the process is as seamless as possible.** [Learn more](https://docs.cloud.google.com/looker/docs/best-practices/how-to-convert-yaml-to-new-lookml).

### Looker Platform

  * **API**
    * **Public API documentation.** The API now has public documentation. [Learn more](https://docs.cloud.google.com/looker/docs/api-getting-started).
    * **Stable endpoints.**
  * **Data actions.** Introducing the ability to create custom tasks directly inside of Looker using query results. [Learn more](https://discourse.looker.com/t/looker-data-actions/3573).



### Explore

  * **Dimension fill.** The results table now populates with missing date, yesno, and many other dimensional values. Associated measures are given values of null. [Learn more](https://discourse.looker.com/t/introducing-dimension-fill-for-query-results/3557).
  * **Added "Save & Schedule" option.** Users will be prompted to save their query as a Look and then be taken directly to the Schedule modal.



### Looker Design

  * **Updated Colors** to use white backgrounds and new button styles and colors.
  * **Added "Explore From Here" link in Spaces.** This shortcut takes users directly to a Look's Explore page equivalent for faster exploration.



### Visualizations

  * **Series tab for pie charts, donut multiples, and table visualizations.** Implemented the Series tab, previously only available on Cartesian charts, for pie charts, donut multiples, and table visualizations, which replaces the Style tab's key-value pair method for changing colors and column labels.
  * **Visual Drilling.** Added a visualization option to the drill overlay, selectable when drilling from a visualization. [Learn more](https://discourse.looker.com/t/visual-drilling/3574).
  * **Pivots no longer require a second dimension.**
  * **Introduced labels for Trend Lines.**



### Scheduling & Downloading

> _flash_on_ **[Looker 4.0 requires PhantomJS 2.1.1.](https://discourse.looker.com/t/installing-phantomjs-for-pdf-download-scheduling-and-scheduled-visualizations/419)**

  * **Image Rendering.** Added the ability to download an image of the visualization from a Look, Explore, or a dashboard.
  * **Added a progress page for downloading tasks.**
  * **Access filters on scheduled dashboards.** Added an Admin option to run scheduled tasks as the recipient, applying access filters to the dashboard's queries. [Learn more](https://discourse.looker.com/t/run-schedule-as-recipient/3578).
  * **Multiple schedules.** Added the ability to create multiple, differently filtered schedules via the API.
  * **Larger scheduled result sets.** Added the ability to schedule queries with no limit to S3 via the API.



### Dialects

  * _flash_on_ **Spark.**
    * **Added support for Spark 2.0** including symmetric aggregates and PDTs.
    * **Spark 1.6.** Added support for symmetric aggregates.
    * _flash_on_ **Removed support for Spark 1.4.**
  * **Hive.** Added full support for `datatype: date`.



### General Tweaks & Bug Fixes

  * **Added Admin panel option to disable backups.**
  * **Admins can now make any Space their default Space.**
  * **Other Issues**
    * Fixed an issue where the instant dashboards could not pull correctly from cache.
    * Fixed an issue where Liquid templating constants did not work properly.
    * Fixed an issue where not all values pasted into a filter would appear.
    * Fixed an issue where visualizations containing Trend Lines did not properly render with data containing zeros.
    * Fixed an issue where Admins were unable to view users who do not use email authentication.
    * Fixed an issue where users would be removed from their personal Space after switching to a Closed System.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
