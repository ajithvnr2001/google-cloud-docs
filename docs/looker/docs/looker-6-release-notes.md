---
url: https://docs.cloud.google.com/looker/docs/looker-6-release-notes/
title: 6.x Release Notes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:11.915868+00:00
---

# 6.x Release Notes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-6-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  6.x Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

## Preparing for Releases

We occasionally retire features. You can plan for this with the [Legacy Features End-of-life Schedule](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067).

In the release notes, you may see some special symbols:

  * Items marked with a _flash_on_ indicate changes to existing functionality that may require your attention as you update, such as features being retired.

  * Items marked with a _science_ indicate a [Looker Labs](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#labs_overview) feature that must be enabled by an admin on the Labs page.

  * Items marked with a _build_ indicate changes to system configurations that may impact your ability to run the new release.




## Looker 6.24 2019-11-08

### Platform and Administration

  * _science_ Introduced support for a new Slack integration for Looker-hosted instances. This new integration allows users to send content through DMs and to public and private channels via OAuth. [Learn more.](https://docs.cloud.google.com/looker/docs/scheduling-slack)

![](https://docs.cloud.google.com/static/looker/docs/images/admin-slackapp-624.png)

  * _science_ _flash_on_ Introduced a new beta Labs feature, **Curated Search**. This feature enhances the content search experience. This search will include content from a user's folder, from shared folders, or on boards. [Learn more.](https://docs.cloud.google.com/looker/docs/finding-content#curated_search) **Note:** This Labs feature is enabled by default.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-curated-search-624.png)

  * _science_ Introduced a new Labs feature, **New Dashboard Experience**. This feature gives dashboards a new look, customizable and user-friendly filters, a new creation experience and editing flow, and faster performance. Users can also seamlessly switch a dashboard between the beta and original layout. [Learn more.](https://docs.cloud.google.com/looker/docs/viewing-dashboards)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboards-beta-624.png)

  * _science_ **Table-next.** Has transitioned out of Labs beta. This is now the default table visualization available in the visualization drop-down; **Table (legacy)** is still available. [Learn more.](https://docs.cloud.google.com/looker/docs/table-options)

![](https://docs.cloud.google.com/static/looker/docs/images/vis-table-next-624.png)

  * **Boards.** Users who share a board will have the option to send an email notification to newly added users, encouraging them to add the board to their list. [Learn more.](https://docs.cloud.google.com/looker/docs/presenting-content#sending_an_email_notification)




### Embedded Analytics

  * **Embed Events** Introduced support for developers to build on-the-fly UI controls for embed users to dynamically control dashboards:

    * Visualization configuration settings: chart type, axis labels, etc.
    * Dashboard layout: tile position and visibility
    * Tile settings: titles and visibility
  * Introduced support for a new API endpoint: `create_sso_embed_URL`. [Learn more.](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/create_sso_embed_url)




### Scheduling and Downloads

  * **Action Hub:**

    * **Braze:** Added optional attributes. [Learn more.](https://github.com/looker/actions/tree/master/src/actions/braze#braze)
    * **mParticle:** New supported custom action. [Learn more.](https://github.com/looker/actions/blob/master/src/actions/mparticle/README.md#mparticle)
    * **Auger.ai:** New supported custom action — send data for machine learning evaluation. [Learn more.](https://github.com/looker/actions/tree/master/src/actions/auger#auger)
  * **Alerts.** Out of Labs beta and available by default.

    * Filters are applied to the visualizations of alerts and to the links in an alert email. [Learn more.](https://docs.cloud.google.com/looker/docs/alerts-overview)



### Marketplace Content

  * Introduced a new block for Shopify. [Learn more.](https://marketplace.looker.com/marketplace/detail/shopify-v2)



### Dialects

  * **Clickhouse.** Introducing support for this dialect. [Learn more.](https://docs.cloud.google.com/looker/docs/db-config-clickhouse)
  * **MS SQL DW & Azure SQL.** Introduced time zones support.
  * **Snowflake.** Introduced OAuth support. [Learn more.](https://docs.cloud.google.com/looker/docs/db-config-snowflake#oauth)



### LookML and Development

  * **Localization.** Added support to localize `comparison_label` and `single_value_title` parameters.



### General Tweaks and Bug Fixes

#### Embedded Analytics

  * Fixed an issue where the embed theme overrode conditional formatting in a single value visualization.
  * _flash_on_ **API 3.1.** `create_sql_query` endpoint has been modified to ask for a `connection name (string)` parameter instead of `connection id (integer)`.
  * Queries with SQL errors no longer return a 500 error response on the `/api/3.1/query_tasks/multi_results` endpoint.
  * Linked to detailed requirements in API docs for embed users to schedule to email.
  * _flash_on_ **API 3.0 & 3.1.** Many endpoints incorrectly responded with `image/jpg` format and now they respond with `image/jpeg`.
  * Adjusted how the URI Validator evaluated whether the required parameters of a URI are set.
  * Embed_domain URL parameter is now carried forward in the Explore URL.
  * Updated the documentation for `all_git_connection_tests` endpoint to require the session to be in Development Mode.



#### Platform and Administration

  * The model set list under **Roles** on the Admin page is now updated to show the correct models.
  * Unicode encoding from IdP now correctly converts to expected single unicode character for SAML attribute pairing.
  * Looks with multiple pivots using the `Run Look` endpoint and outputting JSON no longer replace pivot keys with "".
  * Selecting **Update** for the **Default Export Format** from Admin settings no longer returns a 500 error message.
  * Adjusted the `schedule_look_email` permission to be model specific.



#### Scheduling & Downloads

  * Public look links no longer result in a 404 error message when selecting JSON format as the output.
  * The option to download **All Results** on a tile menu is now grayed out to prevent non-streamable results from yielding a "Refuse to run query..." error.
  * Downloading a LookML dashboard as a PDF no longer inserts page breaks over visualizations.
  * LookML dashboards scheduled with the **Fit Page to Dashboard** option are no longer rendering a shrunken and cut-off PDF.



#### LookML and Development

  * Creating a project with a BigQuery connection no longer generates the file in old LookML.
  * Markdown files can now be searched successfully within folders in the IDE.
  * Failed data tests now prohibit the ability to push changes to production, even with **Pull Requests Required** enabled.
  * Renaming a folder in the IDE no longer returns a "The requested file failed to load" error.
  * Removed the host, port, and database fields from populating when enabling "PDT override" on a database connection.
  * Returned the option to **Create View From Table** in the IDE.
  * The option to **Explain in SQL Runner** is now hidden if a SQL dialect does not support the EXPLAIN function.
  * Fixed external configuration errors being cached in the LookML Validator.
  * Removed the `generated _FILE` and `_LINE_NUM` parameters that displayed when copying a dashboard's LookML.
  * An internally created field will not automatically be added to a drill path as a filter.
  * Data tests no longer require a view file to have a unique name.
  * America - Sao Paulo timezones are no longer off by one hour due to daylight saving time.



#### Dialects

  * **Amazon Athena.** Improved the performance for returning the connection's schemas.



## Looker 6.22 2019-10-29

### Platform and Administration

  * _science_ **SQL Runner Visualization.** This Beta feature allows users to visualize data directly within SQL Runner and to share links for collaboration with other users. [Learn more.](https://docs.cloud.google.com/looker/docs/sql-runner-create-queries-and-explores#creating_visualizations_with_sql_runner)

![](https://docs.cloud.google.com/static/looker/docs/images/sql-runner-viz-rn-622.png)

  * **IP whitelisting.** This new feature provides a mechanism for Looker administrators to whitelist certain IP addresses or blocks of IP addresses that can reach their Looker instance. When IP whitelisting is activated, Looker will refuse connection attempts from all other IP addresses. **Note:** This feature is available only for instances hosted by Looker. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist)

![](https://docs.cloud.google.com/static/looker/docs/images/admin-ip-whitelisting-rn-622.png)

  * _flash_on_ Scheduled plans without a destination will now fail to send. Schedules without destinations created prior to 6.22 will be deleted. [Learn more.](https://docs.cloud.google.com/looker/docs/scheduling#choosing_the_delivery_destination)

  * **Localization updates.** Language support added for the following languages: Chinese (Simplified & Traditional), Swedish, Turkish, and Polish. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-general-localization#locale)

  * _science_ **Table-Next (Beta) improvements.**

    * If enabled, Table-Next will be the default table in the visualization list. The previous table will still show up in the visualization dropdown menu as **Table (Legacy)**. [Learn more.](https://docs.cloud.google.com/looker/docs/table-options)
  * _science_ **Alerts (Beta) Improvements:**

    * Dashboard filters now automatically apply to the alert query. [Learn more.](https://docs.cloud.google.com/looker/docs/alerts-overview#alerting_with_dashboard_filters)
    * The alert email will include the tile's visualization and the current value of the data. [Learn more.](https://docs.cloud.google.com/looker/docs/alerts-overview#alert_notifications_to_email)
    * Embed users are now able to create alerts. [Learn more.](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#permissions)

![](https://docs.cloud.google.com/static/looker/docs/images/delivery-alerts-2-rn-622.png)![](https://docs.cloud.google.com/static/looker/docs/images/delivery-alerts-1-rn-622.png)

  * New `send_to_integration` permission allows users without scheduling permissions to send and schedule content to custom actions. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#send_to_integration)

  * Introduced an additional `--log-format` argument with the two options, [text, json]. The default is `text`. `json` produces structured logs for improved/simpler processing. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-server-log#setting_the_log_format_on_customer-hosted_instances)

  * **API 3.1** Introduced a new JSON format type called `json_label`. [Learn more.](https://community.looker.com/lookml-5/change-in-json-render-formatting-6-22-14465)




### Scheduling and Downloads

  * _flash_on_ Download, send, and schedule modals will now default to a new JSON format for field `label`. This only impacts the modal, not existing content. [Learn more.](https://community.looker.com/lookml-5/change-in-json-render-formatting-6-22-14465)
    * **Note:** The original option regarding the `json_label` format option with an admin legacy feature was removed mid-release. This was done in an effort to provide a more stable experience in regards to rendering field labels in a JSON format when downloading, scheduling, and sending content.



### Dialects

  * _flash_on_ **Snowflake.** Upgraded JDBC driver to v3.9.1.
  * _flash_on_ **Microsoft SQL Server 2016+.** Added support of connection time zone settings.
  * **Apache Hive.** Introduced support for v3.1.2 and later.
  * **DB2, Dremio, IBM DB2 Warehouse on Cloud.** Enabled SSL string parameters.
  * **Amazon Aurora MySQL.** Previously known as "Amazon Aurora" when selecting this dialect on a new connection.
  * **Presto, Athena, Qubole Presto, Qubole Quantum.** Changed string comparisons to use LIKE instead of REGEXP_LIKE for more performant SQL filtering.



### LookML and Development

  * **IDE folders improvements.**

    * Collapse all folders button.
    * Jump-to-file/search button.
    * Display the file extension type within the modal when creating/renaming a file.
    * Rename modal populates the old name, highlighted.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-ide-folders-rn-622.png)




### Embedded Analytics

  * **New SDKs available.** This will allow developers to work with Looker's APIs in the language they're more comfortable with. [Learn more.](https://docs.cloud.google.com/looker/docs/api-sdk)
    * [Python](https://pypi.org/project/looker-sdk/)
    * [Javascript/TypeScript](https://www.npmjs.com/package/@looker/sdk)



### General Tweaks and Bug Fixes

#### Platform and Administration

  * Fixed an issue that prevented sending All Results (streaming) in schedules when utilizing a database type of IBM DB2 for AS400 and System i.
  * Fixed an issue that was displaying LookML dashboards to users without the `see_lookml_dashboards` permissions in search.
  * Fixed an issue that prevented totals from being displayed in a generated PDF when utilizing the Table-Next beta Labs feature.

### LookML and Development

  * Fixed an issue where uploading a `.strings.json` type file did not show up in the development IDE with folders disabled.

  * Fixed an issue that resulted in a 500 error message: "There was a problem running the validator" when validating in the IDE if a merge query with an unknown field existed in a LookML dashboard file.

  * _flash_on_ Fixed an issue where snowflake queries would hang before connecting until Looker was restarted. Resolved by updating the snowflake JDBC driver to v3.9.1.

  * Fixed an issue where the Git menu would disappear when switching to another user's branch.

  * Fixed an issue where filter suggestions that never populated and a 404 error message appeared in the JS console when a dimension referenced itself in the `suggest_dimension` parameter.

    * _flash_on_ The LookML Validator will now return an error in the presence of self-referential `suggest_dimension` parameters.
  * Fixed an issue that would break the LookML Validator when joining on fields of `type: location`.

    * Fixed an issue that prevented users with the `see_pdts` permission from populating information in the Admin panel without `develop` permission.
    * Fixed an issue where setting the parameter `bind_all_filters: yes` in an NDT led to a circular reference error.
    * Fixed an issue where the quick help for `sql_where` indicated that this parameter was only available for BigQuery.

### Embedded Analytics

    * Fixed an issue that resulted in absolute links opening in the same tab instead of in a new tab.
    * Fixed an issue where conditional formatting would break the table visualization within an embedded LookML dashboard.
    * Fixed an issue that prevented embed users with the `schedule_look_emails` permission from being able to send or schedule a Look.
    * Fixed an issue that when utilizing the API `scheduled_plan_run_once` endpoint returned a 404 error message in cases where the `id` parameter matches an existing ID.
    * Fixed an issue where the alerts permissions `create_alerts` and `follow_alerts` were not available for embed users.



## Looker 6.20 2019-09-08

### Platform and Administration

  * _flash_on_ **Renamed _Spaces_ to _folders_.**
  * **Improved the Browse drop-down menu.**
    * Simplified the left sidebar found by selecting the **Home** option from this drop-down menu.
  * _flash_on_ **Content curation (boards) is no longer in Labs.**

    * Boards provide a way for people to curate and surface existing content for initiatives and teams. This feature works in tandem with folders. In addition, LookML dashboards can now be pinned to boards. [Learn more](https://docs.cloud.google.com/looker/docs/presenting-content).

![](https://docs.cloud.google.com/static/looker/docs/images/whats-new-620-boards.png)




### Dashboards, Visualizations, and Explore

  * _science_ **Table-Next improvements (Labs Beta).**
    * Users can control per-column text formatting such as font color, background color, text styling, and text alignment.



![](https://docs.cloud.google.com/static/looker/docs/images/whats-new-620-table-next.png)

### LookML and Development

  * **IDE folders.** Project generator creates folders for models with multiple schemas.
  * New LookML parameter for native derived tables (NDTs), `bind_all_filters`, takes all filters from the user query and applies them in the NDT subquery. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source#passing_filters_into_an_ndt).
  * **Localization.** The `default_value` parameter in LookML dashboards accepts the Liquid `_localization`. [Learn more](https://docs.cloud.google.com/looker/docs/model-localization#filter_localization_example).
  * _flash_on_ View-level `drill_fields` parameter now applicable to all measures by default. `drill_fields` applied on a per-measure basis will override the view-level set. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-view-drill-fields).



### Dialects

  * _flash_on_ **Apache Druid.**
    * Druid is now Apache Druid.
    * Updated the JDBC driver to version 0.15.
    * Enabled setting additional JDBC parameters through the JDBC connection string. This enables a connection to use the properties mentioned [here](https://calcite.apache.org/avatica/docs/client_reference.html).



### Embedded Analytics

  * **New Javascript click events.** Now capturing embed iFrame clicks for **drilling** , **Explore from Here** , and **Open original Look**. [Learn more](https://docs.cloud.google.com/looker/docs/embedded-javascript-events).



### General Tweaks and Bug Fixes

#### Platform and Administration

  * Modified when SQL statements are displayed in the logs based on the chosen logging levels.



#### LookML and Development

  * **IDE folders**. Fixed an issue where the menu option to **Revert Changes** on a single file was no longer available.



#### Dashboards, Visualizations, and Explore

  * _science_ Fixed several issues in the Table-Next (Beta) chart: 
    * The visualization editor intermittently failed to display menu options.
    * The text in subtotals column failed to align.
    * The color picker not displaying a specific color collection when selected.



#### API

  * Fixed an issue where the API endpoint `all_user_attributes` failed with a 500 error when given a sort parameter.
  * Updated the response returned when an embed user did not have a user attribute value for a parameterized connection.
  * Fixed an issue that returned a 404 error message when an admin updated a schedule that wasn't their own via the API.
  * Updated the Looker API Docs to explicitly require the `query_id` parameter when utilizing the `create_look` endpoint.



#### Scheduling and Downloads

  * Fixed an issue which cut off merged results tiles when rendering a PDF of a dashboard with the option **Single column layout** selected.
  * Fixed an issue that cut off columns from tables when rendering a single-column PDF.



## Looker 6.18 2019-08-11

### Dashboards, Visualizations, and Explore

  * _science_ **Table-Next Improvements (Labs Beta).**
    * Ability to control global text formatting. For example, row font size, header font size, header text color, header background color, and header alignment.
    * Ability to display visualizations within the cells of a table.
  * _science_ **Alerts Improvements (Labs Beta).**
    * Ability to give an alert a custom title.
    * Ability to use table calculations when creating an alert.
    * Ability to subscribe to another user's alert. Note the alert must be **Public** and the user must have the `follow_alerts` permission.



### Content Management and Discoverability

  * _science_ **Content Curation Improvements (Labs beta).**
    * Ability to view, scroll and sort all boards within a user's organization.
    * User personal folders now appear both in the **Browse** menu and on the left sidebar.
    * Folders previously set as a default folder will continue to appear in the left sidebar.
    * Developers can set LookML dashboards to appear in the **Browse** menu and left sidebar.



### Platform and Administration

  * _build_ **Dependencies JAR.**
    * Certain Java class files are now distributed separately, resulting in two distinct JAR files that will need to be downloaded and installed to update your Looker instances. [Learn more.](https://docs.cloud.google.com/looker/docs/downloading-looker-jar-files#downloading_looker_6.18_or_later)
  * _flash_on_ **Completely removed the "Legacy Rendering" Legacy Feature.**
  * **Embed Events.**
    * Added `look:ready` and `explore:ready` events to indicate when both the Explore and query have loaded. [Learn more.](https://docs.cloud.google.com/looker/docs/embedded-javascript-events#event_type_reference)
    * Added a `status` result to dashboard embed events to indicate whether a tile produces an error.
  * _science_ **Content Curation Improvements (Labs beta).**
    * Ability to view, scroll and sort all boards within a user's organization.
    * User personal folders now appear both in the `Browse` menu and on the left sidebar.
    * Folders previously set as a 'default folder' will continue to appear in the left sidebar.
    * Developers can set LookML dashboards to appear in the `Browse` menu and left sidebar.



### LookML and Development

  * _flash_on_ **Importing remote projects is no longer in Labs.**
    * The generalized "Project Import" feature is no longer in Labs.
    * Importing locally maintained projects is still in Labs under "Local Project Import".



### Dialects

  * **Snowflake:** Added support for External Table database objects to be scanned for database metadata information. This will surface external tables in SQL Runner and in LookML View generation.
  * _flash_on_ **Aster Data.** Partially deprecated Aster Data. It will no longer be selectable as a dialect in the Dialect dropdown in the Connection panel. **Existing Aster Data connections will continue to work.**
  * _flash_on_ **Microsoft SQL Server 2005.** Removed support for MS SQL 2005.
  * _flash_on_ **XtremeData.** Removed support for XtremeData.
  * _flash_on_ **Qubole Presto** and **Qubole Quantum.** Updated the JDBC driver to version 2.0.2 to fix intermittent NullPointerException errors. [Learn more.](https://docs.qubole.com/en/latest/driver-release-notes/jdbc-release/releasenotes-jdbc-v2.0.2.html)
  * _flash_on_ Only **Oracle ADWC.** Changed JDBC connection string format for Oracle ADWC connections to use the TNS alias as the hostname. In addition, the TNS_ADMIN JDBC parameter is used to connect with Oracle Wallets. 
    * Example: `jdbc:oracle:thin:@dbname_high?TNS_ADMIN=/path/to/wallet/directory`
  * **Druid.** Updated the JDBC driver to version 1.15.0.



### General Tweaks and Bug Fixes

#### Security

  * Fixed an issue where a Look or dashboard tile's default filter values could be applied instead of a send or schedule's filter values. This could only occur if the filter values came from a view that has v_ as the first two characters in its name.
  * Fixed an issue that resulted in User Attribute values set to hidden were printed to server logs.



#### Scheduling and Downloads

  * All formatting types in streamed results were being ignored. Formats will now be respected. Note: JSON detail format will continue to ignore formats as it is its expected behavior.
  * Fixed a scheduler issue that prevented users from running a specific look both when in development mode and when that user did not have development permission to the model the content was based on.
  * Fixed an issue where schedules failed when a user was in development mode and did not have developer access to the model, even if data should return outside of development mode.
  * Fixed an issue where the schedule dispatcher would not run on the master node if it had scheduler threads set to zero, even if other nodes had scheduler threads.
  * Fixed an issue where Looker was starting with a default of three unlimited execute scheduler threads even though this should be one.
  * Looker now retries schedules and actions if one fails due to multiple events firing simultaneously.



#### Platform and Administration

  * Added clarifying text to the Sessions admin panel. No behaviors changed.



#### Dialects

  * **Google Cloud Spanner.** Fixed an issue where the JDBC driver hit a Java instantiation exception.
  * **Netezza.** SQL Runner will now populate database objects from INFORMATION_SCHEMA.VIEWS in addition to INFORMATION_SCHEMA.TABLES in the Schema and Tables sidebar.
  * **Snowflake.** Fixed an issue where the SQL Runner Describe command did not scope Snowflake tables to the schema, causing describe to fail for tables outside of the default schema.



#### Embedded Analyitcs

  * Fixed an issue where updating a Look filter via an iFrame message failed with an error response.
  * Fixed an issue where failed schedules mentioned Looker despite settings being set to not reference Looker.
  * Fixed an issue where the whitelabel favicon was displaying the Looker icon when downloading a PNG in the browser.
  * Numeric filters can now be set on Looks via the embed messaging in an iframe.
  * Fixed an issue where clicking "Explore from Here" when editing an embedded dashboard did not open in a new tab.



## Looker 6.16 2019-07-07

### Dashboards, Visualizations, and Explore

  * _science_ **Table-Next Labs Beta Improvement.**
    * Ability to wrap or truncate text. [Learn more.](https://docs.cloud.google.com/looker/docs/table-options#truncate_text)
    * Conditional formatting. [Learn more.](https://docs.cloud.google.com/looker/docs/table-options#formatting_menu_options)



### Platform and Administration

  * _flash_on_ **Timeout session.** The session timeout warning will now be displayed two minutes before timing out.
  * **Inactivity Logout Session Setting.** Session settings can be modified to force users to be logged out of a session after 15 minutes of inactivity. Activity is defined as a user clicking anywhere in Looker or touching the screen in the case of touchscreens, or typing anything into Looker. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-sessions#inactivity_logout)



### LookML and Development

  * Introduced a method to preserve number formatting, regardless of what locale-based settings a user may have. [Learn more.](https://docs.cloud.google.com/looker/docs/supported-user-interface-languages#overriding_the_number_format_user_attribute_with_strict_value_format)



### Dialects

  * _flash_on_ **Updated Snowflake driver (v3.8.4).** Addresses Snowflake issues caused by prior versions of the driver. [Learn more.](https://support.snowflake.net/articles/Product_Update/client-release-history)
  * **Qubole Dialect.** Qubole Quantum. The Qubole Presto dialect _Qubole Presto Service_ has been rebranded and is now available as a separate dialect in the drop-down menu as _Qubole Quantum_.



### General Tweaks and Bug Fixes

#### LookML and Development

  * Addressed an issue where `value_format_name` and `value_format` parameters were not being respected in the field being extended. It was taking the parameter definition of the view the field was extended from.
  * Improved an issue where utilizing non-alphanumeric characters upon configuring a new model led to a 500 error.
  * Modified how the `datatype` parameter of `type: date` interacted with a measure within the project IDE.
  * Addressed the inconsistent alignment of Git metadata displayed in the project settings page.
  * Addressed LookML validation error `Uncaught TypeError: Cannot read property '1' of null`.
  * Addressed an issue in which, when user attributes were used to define the `sql_always_where` parameter in a persisted Explore, incorrect data was being pulled from the cache.



#### Dashboards, Visualizations, and Explore

  * Addressed the ability for the x-axis to respect number localization.
  * Addressed number formats mismatching between different viz types.
  * Addressed an issue that was resulting in drills displaying no results when null values were set to a type of `string`.



#### Scheduling and Downloads

  * Addressed an issue that was causing Look and dashboard rendering to fail.



#### API

  * Addressed an issue where the `all_lookml_models()` and `lookml_model(lookml_model_name)` API endpoints would return an empty array with Explores that required access grants.



#### Platform and Administration

  * Addressed an issue where editing the user attribute for a group did not allow them to enter a string. Instead, it only displayed a drop-down of options.



#### Dialects

  * Addressed a Snowflake JDBC driver version 3.8.3 issue that would return a `NullPointerException` message when a queried result set was larger than could be held in one result chunk. Queries returned a blank error message to Looker.



## Looker 6.14 2019-06-09

### Dashboards, Visualizations, and Explore

  * _science_ **Table-Next chart options:** Ability to transpose tables. [Learn more.](https://docs.cloud.google.com/looker/docs/table-options#transpose)

![](https://docs.cloud.google.com/static/looker/docs/images/rns-transpose-tables-614.png)

Ability to reorder columns in the table visualization into any order. [Learn more.](https://docs.cloud.google.com/looker/docs/table-options#manually_moving_and_pinning_columns)

![](https://docs.cloud.google.com/static/looker/docs/images/rns-reorder-columns-2214.png)




### Platform and Administration

  * **Localization of number formatting.** Ability to implement number formatting by setting a user's `number_format` user attribute to one of the available number formats. The formatting is not respected on the x-axis of some visualizations. [Learn more.](https://docs.cloud.google.com/looker/docs/supported-user-interface-languages#localizing_number_formatting)
  * **New user email configuration option:** Allows admins to customize via HTML the body content of the welcome email new users receive to activate their Looker account. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-users-custom-welcome-email)



### Dialects

  * _flash_on_ **Updated Snowflake driver (v3.8.0).** Addresses Snowflake OCSP issue found in prior versions of the driver. [Learn More.](https://support.snowflake.net/articles/Product_Update/client-release-history)
  * _flash_on_ **Updated Athena driver (v2.0.7).** Allows defining `Workgroup=WorkgroupName` parameter in the **Additional JDBC Parameters** field of a database connection in order to utilize AWS Workgroups.



### Scheduling and Downloads

  * _flash_on_ **Run Schedule as Recipient is out of Labs.** This feature is now fully available on all instances.
  * _flash_on_ **Easy to Read Email Images is out of Labs.** This feature is now fully available on all instances.



### General Tweaks and Bug Fixes

#### Scheduling and Downloads

  * Improved rendering of tables with more than 100 rows.
  * Improved the rendering of inline visualizations in schedules.



#### Platform and Administration

  * Improved the ability to filter out Looker employees from the User Activity dashboard under System Activity.
  * Improved the tracking of user and sudo details in events.
  * Addressed an issue where a user could bypass the account lockout by using a capital letter in the email.



## Looker 6.12 2019-05-12

### Dashboards, Visualizations, and Explore

#### Visualization

  * **Boxplot visualization.** Now shows a shaded range between the max and min when 2 or 3 measures are selected. [Learn more.](https://docs.cloud.google.com/looker/docs/boxplot-options)
  * **Waterfall visualization.** Now supports having 1+ measure selected with no dimensions selected. [Learn more.](https://docs.cloud.google.com/looker/docs/waterfall-options)
  * _flash_on_ **Pie visualization.** Refactored the pie visualization and added options to control the start and end angles. [Learn more.](https://docs.cloud.google.com/looker/docs/pie-options)



### Platform and Administration

  * _flash_on_ **Completely removed the "Show Full Field Name" Legacy feature.** [Learn more.](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067)
  * **System Activity.** Added user role information to System Activity User Explores.
  * **Accessing the API.** Looker-hosted customers can now get to the API on the standard `https` port. Instead of defining the port as `https://customer.region.looker.com:19999`, we can now navigate to `https://customer.api.region.looker.com`. [Learn more.](https://docs.cloud.google.com/looker/docs/api-getting-started#looker_api_path_and_port)



### LookML and Development

  * **LookML Constants.** Constants are a new parameter that can be defined in a LookML manifest file and reused in other parts of LookML. [Learn More.](https://docs.cloud.google.com/looker/docs/reference/param-manifest-constant)



### Dialects

  * **Introduced support for Actian Avalanche.** [Learn more.](https://docs.cloud.google.com/looker/docs/db-config-actian-avalanche-and-vector)
  * **Introduced support for BlinkDB.**
  * _flash_on_ **Removed the Google Cloud Spanner driver.** Customer-hosted instances must implement a custom JDBC driver.
  * _flash_on_ **Removed MSSQL 2005 as an option when creating a new connection.** Existing connections with this dialect will be unaffected.
  * _flash_on_ **Updated Snowflake driver (v3.7.2).**



### General Tweaks and Bug Fixes

#### LookML and Development

  * Addressed an issue that did not allow a project name change to include hyphens by automatically turning them into underscores. The hyphens are now honored.
  * Addressed an issue that was returning LookML validation errors for filter configurations of a LookML dashboard that was converted from a user-defined dashboard.
  * Addressed an issue that wasn't surfacing the expected LookML validator error when using a measure that referenced a field that was not included in the fields parameter of the Explore.
  * Addressed an issue where utilizing the `liquid _view._name` Liquid variable in the SQL parameter of a derived table returned the LookML validator error " _view is not available in this context."
  * Addressed an issue where a field specified in the `order_by_field` parameter was surfaced in the Explore, even though it should be excluded by the `fields` parameter defined in the Explore's LookML.
  * Added the ability to replace model file names with special characters.
  * Returns an error if a field is utilizing `type: time` or `type: duration` and it isn't defined as a dimension group.



#### Platform and Administration

  * Addressed an issue regarding PDT rebuilds returning the error "java.io.IOException: Timed out waiting for copy job to complete."
  * Addressed an issue that was displaying more than two decimal places for data that doesn't have more than two decimal places.
  * Addressed an issue where invalid SQL was being generated due to SQL column names containing capitals.
  * Addressed an issue where updating the underlying field of a dashboard filter that comes from a view that is joined with an alias using the `from` parameter still returns an error via the Content Validator.
  * Addressed an issue where utilizing a median custom measure returned the error "SQL Dialect "redshift" does not support Symmetric Aggregates with percentiles, field ignored."
  * Addressed an issue where the LookML validator was returning the error message "Unknown Access Grant for Model" even though the access grant was properly defined in the model.



## Looker 6.10 2019-04-07

### Dashboards, Visualizations, and Explore

  * **New visualizations!**
    * Box plot. [Learn more.](https://docs.cloud.google.com/looker/docs/boxplot-options)
    * Waterfall. [Learn more.](https://docs.cloud.google.com/looker/docs/waterfall-options)
    * Word cloud. [Learn more.](https://docs.cloud.google.com/looker/docs/word-cloud-options)
    * _science_ Experimental new table visualization. [Learn more.](https://docs.cloud.google.com/looker/docs/table-options)
  * **Reverse the colors.** Added an option to reverse the order of a color palette when multiple series are present in a visualization.



### Platform and Administration

  * **Introduced Oauth for the Action Hub.** New actions may be built with OAuth, allowing users to authenticate as themselves to take action in another application. [Learn more.](https://docs.cloud.google.com/looker/docs/action-hub#configuring_an_action_for_oauth)
  * _flash_on_ **New default password requirements.** New and reset passwords will be subject to the following requirements: minimum length 10 characters, at least one uppercase and one lowercase letter, one numeric character, and one special character. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-authentiation-password)
  * **New language support.** Expanded current language support to include Spanish, Italian, Korean, Dutch, Portuguese, Brazilian Portuguese, and Russian. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#locale_\(beta\))
  * _science_ **System Activity model and dashboard improvements:**
    * Fields used in non-Look tiles are now tracked in the model and dashboards.
    * Added descriptions to the remaining fields in the model.
    * Improved drill fields in the System Activity model and dashboards.
  * _science_ Promoted API 3.1 from "experimental" to "beta".
  * Added the ability to disable Gravatar user account profile pictures. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#use_gravatar)
    * Added Javascript events that track when embedded content begins and completes loading data. [Learn more.](https://docs.cloud.google.com/looker/docs/embedded-javascript-events#event_type_reference)



### LookML and Development

  * **The Content Validator now covers dashboard filters and listeners.**



### Security

  * Addressed a vulnerability that allowed for access to other users' scheduled deliveries.
  * Addressed a vulnerability related to the sanitization of SQL Runner downloads.
  * Newly created instance will default to having "Clickjacking Protection" enabled on the Embed Admin page. Existing instances will retain their selected values.



### General Tweaks and Bug Fixes

#### Dialects

  * Fixed an issue where Looker generated invalid SQL for Dremio.
  * Fixed an issue where Looker generated incorrect SQL for relative date filters on Druid. #### LookML and Development
  * Added a link to the "import credentials" project settings tab when the LookML Validator warns that a dependency lacks credentials.
  * Fixed an issue that resulted in "Document Not Found" messages when selecting "View Document" to see a document outside of the IDE.
  * _science_ Custom fields no longer unnecessarily trigger Symmetric Aggregates.
  * Fixed an issue where developers could not see certain models connected to local Git repositories.
  * Fixed an issue where the Content Validator could group errors by the wrong space.
  * Fixed an issue where the Content Validator did not flag errors produced by fields being excluded using `fields: []` at the join level.
  * Fixed an issue where the LookML Validator failed to detect inaccessible native derived table fields.
  * Added validation to properly protect against duplicative model names issues.
  * _science_ Fixed an issue where project import would include all view files in a project when it should just include the root with `include: "/*.view"`. #### Scheduling and Downloading
  * Improved mailer stability by retrying schedules after a timeout period.



## Looker 6.8 2019-03-10

### LookML and Development

  * _science_ **Remote project import for private repositories.** The experimental Project Import feature now supports references to and extensions of private Git repositories. [Learn more.](https://docs.cloud.google.com/looker/docs/importing-projects#adding_authentication_credentials_for_private_remote_repositories)
  * **Explicit LookML field type references.** Introduced a new syntax for referencing LookML field types other than the default. For example, you can now reference a datetime version of `created_date` with `${created_date::datetime}`. [Learn more.](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#lookml_field_type_references)
    * _flash_on_ As part of this change, field references to list measures are not supported and will produce errors.
  * The Content Validator is now a fully supported feature.
  * "Don't Revalidate Unchanged LookML" has also graduated from Labs. [Learn more.](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_changes)
  * Hyphens are now allowed in string file names.
  * Improved IDE performance for very large LookML projects.



### Dashboards, Visualizations, and Explore

  * **Localized dashboards and visualizations.** Visualizations and dashboards now support French, German, and Japanese. Application menu items, filters, etc. do not yet support translations. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#locale_\(beta\))
  * _flash_on_ _science_ To be consistent with how dashboards are handled, the beta API 3.1 no longer includes soft-deleted Looks in `all_looks()` calls. The call is not changed in API 3.0.



### General Tweaks and Bug Fixes

#### Dialects

  * Fixed an issue where Druid connections on clustered instances would produce `Cannot run simple select querysimple SELECT query tests Java::OrgApacheCalciteAvatica::AvaticaClientRuntimeException: Remote driver error: ISE: Connection8b4d9fb4-2383-4aac-92e0-e2b5231aa0e1 already open` errors. #### LookML and Development
  * Fixed an issue where Looker did not escape commas in parameter field values.
  * Fixed an issue that produced "should be localized but has not been" IDE warnings for LookML dashboards when string files are present.
  * Fixed an issue where the LookML Validator failed to run when `remote_dependency` did not have `url` and `ref` parameters.
  * Informational messages related to localization of LookML dashboards are now grouped in the IDE as "LookML Info Messages". This addresses a previous issue that treated them as warnings even when permissive localization was enabled. #### Content Management and Discoverability
  * Fixed an issue that prevented enabling a closed system in the presence of orphaned Looks and dashboards.
  * Fixed an issue where the Explore picker drop-down could be cut off on small windows.
  * Fixed a closed system issue where non-admin users could lose access to a Space when adding users to it.
  * Addressed issues that could cause broken Look and dashboard thumbnails to appear in Spaces. #### Scheduling and Downloading
  * Fixed an issue that caused jobs to fail when cluster nodes listened on different ports. #### Embedded Analytics
  * Fixed an issue where menu items produced 404 errors in the JavaScript Console. 



## Looker 6.6 2019-02-09

### Dashboards, Visualizations, and Explore

  * **Trellis charts.** The new **Grid Layout** visualization option makes trellis charts available for all Cartesian charts. [Learn more.](https://docs.cloud.google.com/looker/docs/column-options#grid_layout)
  * _science_ **Merged results on LookML dashboards.** Users can now use merged results tiles on LookML dashboards. [Learn more.](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#adding_a_visualization_to_an_existing_lookml_dashboard)
  * _flash_on_ **Completely removed the "Legacy Visualizations" legacy feature.** [Learn more.](https://discourse.looker.com/t/deprecation-notice-change-in-visualization-system-6-0/9240)
  * _flash_on_ **Disabled the "Legacy Rendering" legacy feature.** It may be temporarily reenabled on the Legacy Features page if needed to help your transition. If you have not already, please install Chromium to continue rendering PDF and PNGs. [Learn more.](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#chromium)



### Downloads and Scheduling

  * **Expand tables on PDF downloads.** New option to expand tables on PDF downloads to ensure all rows are visible. [Learn more.](https://docs.cloud.google.com/looker/docs/scheduling-email#expand_tables)



##  Platform and Administration 

  * _flash_on_ _science_ **Changed interactive API doc URLs.** The URLs for interactive API docs now disambiguate between API 3.0 and the beta API 3.1.
  * **Redesigned user activation email.** New email with single call to action designed to make new user activation simpler.
  * **Added support for OpenJDK.** [Learn more.](https://docs.cloud.google.com/looker/docs/installing-looker-application)
  * **Refactored Google Authentication.** In preparation for the deprecation of the Google+ API on March 7, Looker no longer utilizes the Google+ API for Google Authentication. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-google)



### LookML and Development

  * **SQL Runner search out of beta.** All Looker customers can now use the search bar in the SQL Runner to locate specific fields in connected databases.
  * **Localized LookML dashboards.** Developers are now able to use the `.strings` file type to specify localization parameters for LookML dashboards. [Learn more.](https://docs.cloud.google.com/looker/docs/model-localization)
  * _flash_on_ **Completely removed the "Native Derived Tables Convert Dates and Yesnos to Strings" legacy feature.** [Learn more.](https://discourse.looker.com/t/improved-behavior-for-native-derived-tables-in-looker-5-22/8680)
  * **Introduced the`group_item_label` parameter** to allow you to change how a field appears in the field picker when nested under a `group_label`. [Learn more.](https://docs.cloud.google.com/looker/docs/reference/param-field-group-item-label)



### Dialects

  * **Snowflake.** Added support for `List` measure.



### General Tweaks and Bug Fixes

#### Dialects

  * Fixed a bug where the LookML generator did not properly escape hyphens for certain dialects.



#### Administration and Platform

  * Users with the `see_system_activity` permission can now download the System Activity dashboard.
  * Fixed a bug where the HTTPS Git connection option did not correctly support user attributes.



#### Dashboards, Visualizations, and Explore

  * Fixed a bug where the `starts with` string filter incorrectly returned no results when used with quotation marks.
  * Fixed a bug where Single Value visualizations produced the wrong error when no results were returned.
  * Fixed a bug where trend lines on Cartesian charts sometimes appeared behind data.
  * Fixed a bug where values on stacked percentage columns did not always add up to 100.
  * Fixed a bug where visualization labels for fields that contain a `'` did not render correctly.
  * Fixed a bug where scatterplot visualizations did not display on Internet Explorer.
  * Fixed a bug where percent previous visualizations were not available unless the `Legacy Visualizations` legacy feature was turned on.



#### LookML and Development

  * Fixed a bug where switching LookML files triggered a full page refresh.
  * Fixed a bug where queries with totals created using the `create_queries` endpoint sometimes produced and error.
  * Fixed a bug where Liquid HTML in `label` parameter for dimension group did not always render correctly.



#### Scheduling and Downloading

  * Fixed a bug where sending Excel schedules sometimes caused an error message.
  * Fixed a bug where scheduled emails were sometimes blank.



#### Embedded Analytics

  * Fixed a bug where the subtotals visualization was broken in the embed context.



#### Security

  * Added integrity checking to database connection configuration data.



## Looker 6.4 2019-01-13

### Dashboards, Visualizations, and Explore

  * _flash_on_ **Enhanced Rendering out of Beta.** Enhanced Rendering is now out of Beta and turned on by default for all instances. To continue using PhantomJS to render PDFs, please utilize the `Legacy Rendering` legacy feature. [Learn more.](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#phantomjs)
  * **Mixed-type stacked charts.** Cartesian charts using mixed series types can now be stacked. [Learn more.](https://docs.cloud.google.com/looker/docs/creating-visualizations#creating_stacked_charts_with_multiple_visualization_types)
  * **New and custom color collections.** New color palettes and color collections allow for more color customization on visualizations. [Learn more.](https://docs.cloud.google.com/looker/docs/color-collections)
  * **Easier-to-use color palette selector.** Visualization menu improvements make color selection easier and more straightforward. [Learn more.](https://docs.cloud.google.com/looker/docs/line-options#colors)
  * **More powerful conditional formatting.** Finer control over color-value mapping. [Learn more.](https://docs.cloud.google.com/looker/docs/legacy-table-options#enable_conditional_formatting)



### Platform and Administration

  * _science_ **Beta homepage updates.** Updates to default Looker homepage with end-users in mind.
  * **Customizable session length.** Looker admins are now able to customize default session duration for users. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-sessions#session_duration)
  * **Option to disable concurrent sessions.** Looker admins are now able to disable concurrent user sessions. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-sessions#concurrent_sessions)



### LookML and Development

  * _science_ **Content Validator performance improvements.** Significant performance improvements to the Content Validator.
  * _science_ _flash_on_ **Project Import syntax change.** `include` statements for files from imported projects now require the following syntax: `include: "//<INCLUDE_FILE_PATTERN>`. Use of a single-slash will now produce a warning.
  * **New API endpoints:** `deploy_to_production` and _science_`content_validation`.



### Embedded Analytics

  * _science_ **Beta embed theme editor.** Looker admins are now able to set themes for embedded content. [Learn more.](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores)

  * **New embedded JavaScript event:`drillmenu:click`.** Embed developers will now be able to receive JavaScript event notifications of drill menu clicks in iframe embedded contexts. [Learn more.](https://docs.cloud.google.com/looker/docs/embedded-javascript-events#drillmenu:click)




### Dialects

  * **Introduced support for Denodo 7.0**
  * _flash_on_ **Driver updates: MariaDB (2.3.0), PrestoDB (0.214), and PostgreSQL (42.2.5)**
    * **MongoBI** users will need to remove the `maria15x` entry from their custom JDBC YML files in order for Looker to start.



### Security

  * _flash_on_ Resolved an issue where PostgreSQL and Amazon Redshift connections were not verifying SSL certificates. 
    * It's possible that previously silent verification issues may appear upon update.
    * In cases of SSH tunnels, certificate validation is likely not necessary and could produce warnings.



### General Tweaks and Bug Fixes

#### Dialects

  * Fixed a bug where the Week Duration dimensions generated incorrect SQL in BigQuery.



#### Administration and Platform

  * Fixed a bug where connection test for BigQuery hung after uploading new `.p12` file.



#### Dashboards, Visualizations, and Explore

  * Fixed a bug where filter values overflowed the filter input box.
  * Fixed a bug where the table calculations button sometimes did not appear when expected.
  * Fixed a bug where drills did not work in some single value visualization tiles.
  * Fixed a bug where the text area model did not render properly.
  * Fixed a bug where value labels did not appear on stacked column charts.
  * Fixed a bug where the "Explore From Here" page on dashboards did not include filtered custom dimensions.
  * Fixed a bug where funnel visualizations were rendering incorrectly.
  * Fixed a bug where long horizontal axis labels overlapped.
  * Fixed a bug where navigating to PDT Admin panel sometimes produced a 500 error.



#### LookML and Development

  * The IDE now supports uppercase characters in LookML file names.
  * New LookML Validator warnings for invalid characters.
  * Fixed a bug where results downloaded from SQL Runner had arbitrary file names.
  * Fixed a bug where duration fields didn't work as drill fields or when referenced in measures.
  * Fixed a bug where some users were unable to "Explore From" a SQL Runner query.
  * Fixed a bug where some SQL Runner queries could not be cancelled.



#### Scheduling and Downloading

  * Conditional formatting is now retained in XLSX downloads.
  * Fixed a bug where "Send if there are results" did not work with "All Results" selected.
  * Fixed a bug where it was not possible to send visualizations from Explores.
  * Fixed a bug where downloading data from a dashboard did not use correct time zone.
  * Fixed a bug where downloading results from SQL Runner opened results in new browser window instead.
  * Fixed a bug where embedded user-defined dashboards ignored filters when scheduling and sending.



## Looker 6.2 2018-11-25

### Scheduling and Downloading

  * **`run_sql_query` API endpoint.** New endpoint allows Looker developers to run SQL queries against connected databases via the Looker API.
  * **Page breaks in PDF downloads.** Large dashboard PDFs now include page breaks and paper size and orientation options. Please note: this feature requires the Enhanced Rendering Labs feature.



### Dashboards, Visualizations, and Explore

  * **Totals on table calculations.** [Learn more.](https://docs.cloud.google.com/looker/docs/exploring-data#displaying_totals)
  * **Improved color palette editing.** Continuous color palettes are now easier to configure and use. [Learn more about configuring table chart palettes.](https://docs.cloud.google.com/looker/docs/legacy-table-options#formatting_menu_options) [Learn more about configuring funnel chart palettes.](https://docs.cloud.google.com/looker/docs/funnel-options#bars_menu_options) [Learn more about configuring timeline palettes.](https://docs.cloud.google.com/looker/docs/timeline-options#using_colors)
  * **Improved default visualization selection.** Looker now includes improved logic for selecting default visualizations based on data results.



### Platform and Administration

  * _science_ **Beta System Activity model and dashboards.** New model and dashboards give Looker admins better insight into activity on their Looker instance. Enable them on the Labs page. [Learn more about the model.](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores) [Learn more about dashboards.](https://docs.cloud.google.com/looker/docs/system-activity-pages)



### LookML and Development

  * **Beta`label` and `description` parameter localization.** New `locale` user attribute allows Looker developers to localize certain LookML parameters. Please note: this feature does not require a Labs toggle to use, but is still in beta testing. [Learn more.](https://docs.cloud.google.com/looker/docs/model-localization)



### Dialects

  * **Vector.** Added provisional support for Actian Vector.



### General Tweaks and Bug Fixes

#### Dialects

  * Improved "create view from table" performance for Snowflake connections.
  * Date filters on Snowflake now use `CURRENT_DATE()` where possible to take advantage of database-side caching.
  * Updated the Vertica 7.1+ driver to version 9.1.1.



#### Administration and Platform

  * Fixed a bug were OpenID Connect did not work correctly with Amazon Cognito.
  * Fixed a bug where the Look link in the queries tab didn't work.
  * Fixed a bug where long group names with a `-` did not display correctly on the SAML configuration page.



#### Dashboards, Visualizations, and Explore

  * Removed `x` from merged results dialog box and replaced with `cancel` button.
  * Fixed a bug where ordinal X-axis did not display time labels properly.
  * Fixed a bug where string filters containing a `` could sometimes cause a browser crash.
  * Fixed a bug where totals were sometimes displayed on the wrong column with stacked column charts.
  * Fixed a bug where reference lines on horizontal bar charts were labelled vertically.
  * Fixed a bug where some visualizations on dashboards did not re-render after editing.
  * Fixed a bug where hidden series became visible upon update to Looker 6.0.
  * Fixed a bug related to editing embedded Looks.
  * Fixed a bug where table calculations were hidden in the Edit Look modal.
  * Fixed a bug where long legend labels did not wrap to new line.
  * Fixed a bug introduced in Looker 6.0 where some users could no longer re-order series. #### Content Management and Discoverability 
    * Fixed a bug where converting a look from a different space into a dashboard tile failed. #### LookML and Development
  * Fixed a bug where the `access_grants` parameter sometimes caused a LookML error.
  * Fixed a bug where PDTs sometimes did not rebuild after editing SQL.



## Looker 6.0 2018-10-21

### LookML and Development

  * **`access_grant` parameter.** LookML developers can use new LookML parameters to adjust data access at the view, join, Explore, and field levels. [Learn more.](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant)
  * **New`duration` type dimension group.** [Learn more.](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#type_duration)
  * _flash_on_ **Completely removed the "Allow the`access_filter_fields` parameter" Legacy Feature.** User-attribute-based access filters are now the only method for row-level data security. [Learn more.](https://discourse.looker.com/t/deprecation-notice-access-filter-fields-replaced-by-access-filters-4-16/5296)
  * _flash_on_ **Disabled the "Native Derivied Tables Convert Dates and Yesnos to Strings" Legacy Feature.** It may be temporarily reenabled on the Legacy Features page if needed to help your transition. [Learn more.](https://discourse.looker.com/t/improved-behavior-for-native-derived-tables-in-looker-5-22/8680)



### Dashboards and Visualizations

  * **Improved Color Picker.** New color palette selection tool in the Visualizations menu. [Learn more.](https://docs.cloud.google.com/looker/docs/line-options#colors)
  * _flash_on_ **Enhanced Visualizations.** Enhanced Visualizations has moved out of beta and will now be available to all Looker customers. **Legacy Visualizations** is available as a legacy feature in the Admin panel. [Learn more.](https://discourse.looker.com/t/deprecation-notice-change-in-visualization-system-6-0/9240)
  * **New Markdown Toolbar** for dashboard text tile creation. [Learn more.](https://docs.cloud.google.com/looker/docs/creating-legacy-dashboards#adding_dashboard_headers_and_text)



### Dialects

  * **MongoBI.** Looker can now be used with MongoDB using the MongoDB BI connector. PDTs are not supported. [Learn more.](https://docs.cloud.google.com/looker/docs/n/a%20-%20content%20moved)
  * **Google BigQuery.** Added support for BigQuery instances hosted outside the US and PDTs for clustered tables. [Learn more.](https://docs.cloud.google.com/looker/docs/reference/param-view-cluster-keys) ### General Tweaks & Bug Fixes



#### Dashboards, Visualizations, and Explore

  * Looks are now edited in the page instead of in an additional "edit" modal.
  * _science_ Custom visualizations are available to all Looker instances in the Labs panel. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#sandboxed_custom_visualizations)
  * _science_ Continued improvements to custom visualizations.
  * Fixed a bug where reference lines didn't behave as expected with stacked percentage charts.
  * Fixed a bug where log scale y-axes lacked margins.
  * Mixed series types now automatically layer for visibility.
  * Fixed a bug where stacked charts legend order did not match visualizations.
  * _flash_on_ Reference lines now compute standard deviations based on population calculations rather than sample ones. #### Platform and Administration
  * _build_ Looker 6.0 requires Java 1.8 update 161+. [Learn more.](https://docs.cloud.google.com/looker/docs/installing-looker-application)
  * Fixed a bug where the time zone picker did not change in embedded Explores. #### LookML and Development
  * _science_ Continued improvements to experimental custom fields.
  * Improved error messaging around references to unset user attributes. #### Scheduling and Downloading
  * Fixed a bug where scheduling an Excel file sometimes produced an error.
  * Fixed a bug where text visualizations did not render correctly when sent to email as a `.png`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
