---
url: https://docs.cloud.google.com/looker/docs/looker-7-release-notes/
title: Looker 7 release highlights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:15:56.988280+00:00
---

# Looker 7 release highlights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-7-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  Looker 7 release highlights Stay organized with collections  Save and categorize content based on your preferences. 

## **Looker 7.20**

_play_circle_filled_ Expected rollout start: **Wednesday, November 18th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, December 3rd, 2020**

### Potentially breaking changes

Check out these potentially breaking changes introduced in Looker 7.20. Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * Fonts and colors have been updated across the entire Looker application to align with Google branding. This can be enabled or disabled with the **Legacy Branding** toggle under [**Legacy Features**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#current_legacy_features). The toggle is disabled by default in Looker 7.20.
  * For BigQuery Standard SQL connections, the **Treat the Datatype Datetime as a Timestamp** [**legacy feature**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#current_legacy_features) is disabled by default.
  * The [**Upgraded Explore Field Picker**](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#upgraded_explore_field_picker) beta Labs feature is now enabled by default for all instances.
  * When Looker initiates a Snowflake database connection, the `AUTOCOMMIT` parameter is now set to `TRUE` by default.
  * Filter expressions can no longer be added to measures of `type: number`.
  * Looker no longer double-encodes links that contain special characters.
  * The [**Sandboxed Custom Visualizations**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations) Labs feature is now out of Labs and generally available.
  * During startup, Looker now validates the dialect and version of the internal database. If something other than the default in-memory HyperSQL or a MySQLv5.7.x database is used as the internal database, Looker logs an error message before performing any startup migrations.



* * *

### Looker Marketplace Updates

Introducing new Looker Blocks and updates to features in Looker's Marketplace.

![](https://docs.cloud.google.com/static/looker/docs/images/markeplace-block-720.png)

  * Introducing the **BigQuery Information Schema Performance Monitoring Block** that provides holistic analytics to understand BigQuery resource consumption among projects, organizations, or individual users. This block includes the following dashboards: **Performance Summary** , **Job Lookup** , and **Issue Investigation**.
  * Introducing the **Dialogflow Parser Block** that provides visibility and exploration of data that is generated during a user's interactions with a chatbot.
  * Introducing the **Google Cloud's Retail Block** gives users the ability to understand the overall performance, top and bottom stores, and product categories driving each trend.
  * The **Data Dictionary** now offers the ability to add comments to individual fields. Comments exist in the UI, in addition to the LookML.
  * Aggregate awareness has been implemented across the GA360 block.



* * *

### IDE Deployment Manager

The new IDE deployment manager adds a UI for **advanced deploy mode**.

![](https://docs.cloud.google.com/static/looker/docs/images/ide-deploy-manager-720.png)

  * The [deployment manager](https://docs.cloud.google.com/looker/docs/advanced-deploy-mode#deployment_manager) allows developers to deploy any commit to production from any branch.
  * The deployment manager separates deploying from merging: developers who don't have the ability to deploy are now able to merge changes with this feature.
  * This feature also adds Git tags from the UI to mark version numbers or other metadata and allows rolling back to prior versions.



* * *

### IDE Metadata Sidebar Beta Labs Feature

Introducing a new beta Labs feature, IDE Metadata Sidebar.

![](https://docs.cloud.google.com/static/looker/docs/images/ide-metadata-sidebar-720.png)

  * The [**IDE Metadata Sidebar**](https://docs.cloud.google.com/looker/docs/lookml-metadata) Labs feature allows users to see helpful metadata about the object their cursor is on.
  * This feature will help users answer the question _Where else is this object being used?_
  * Examples include which Explores a view is joined into or which objects extend or refine the `explore`.



## **Looker 7.18**

_play_circle_filled_ Expected rollout start: **Sunday, October 18th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, October 29th, 2020**

### Potentially breaking changes

Check out these potentially breaking changes introduced in Looker 7.18. Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance configuration.

  * Looker's [new dashboard experience](https://docs.cloud.google.com/looker/docs/dashboards) is out of Labs and generally available.
  * The [**Cross-filtering** Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#cross-filtering) is enabled by default on dashboards. _Note: This Labs feature is not available on legacy dashboards._
  * Fonts and colors have been updated across the entire Looker application to align with Google branding. This can be enabled or disabled with the **Legacy Branding** toggle under **Legacy Features**. The toggle is enabled by default in Looker 7.18 and will be disabled by default in Looker 7.20.
  * The Aster JDBC driver has been removed from Looker. All Aster connections will require a custom JDBC driver install.
  * The SAP HANA JDBC driver has been upgraded to v2.5.46 to give users the ability to set the default schema, configure SSL, verify SSL connection options, and get additional support for the SAP HANA JDBC parameters.
  * The Postgres Pre-9.1 SQL dialect is being downgraded to a support level of [ **Integration**](https://docs.cloud.google.com/looker/docs/dialects#support_levels). Postgres 9.5+ remains a supported dialect option.
  * Using the [Liquid variable `_filters[]` in a derived table's SQL without the `sql_quote` parameter](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#using__filters\['view_name.field_name'\]_in_pdt_definitions_requires_sql_quote) is now discouraged and will return a deprecation warning when the filter value is rendered in SQL. This warning is expected to be upgraded to an error by 2020.
  * The LookML IDE will now render a warning if two joins without `view_labels` join the same labeled view, which would result in duplicated LookML fields.
  * If the `suggest_dimension` parameter references an invalid or excluded field, the LookML IDE will render a new warning.
  * If localization is used on a project and a dimension group with `type: time` is defined in the LookML, a LookML warning will be rendered. The warning will suggest splitting the dimension group into individual dimensions.



* * *

### New Dashboard Experience

[Looker's new dashboards feature](https://docs.cloud.google.com/looker/docs/dashboards) — formerly known as dashboards (beta) — is now the default dashboard experience in Looker.

![](https://docs.cloud.google.com/static/looker/docs/images/dashboards-collapsible-filters-2-718.png)

  * The new dashboard experience has faster load performance, powerful new [filter controls](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards), a [redesigned scheduler](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards), and a [collapsible filter bar](https://docs.cloud.google.com/looker/docs/viewing-dashboards#filters_icon).
  * [Dashboard creation](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards) now uses the new dashboard experience.
  * Users can [revert to legacy dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards#reverting_dashboards_to_legacy_dashboards) if the **Revert to Legacy Dashboards** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-features) is enabled. For 7.18, the legacy feature is enabled by default.
  * The [**Cross-filtering** Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#cross-filtering) will be enabled by default. _Note: This Labs feature is not available on legacy dashboards._



* * *

### Looker's Google Cloud Rebranding

The Looker platform is in transition to align with Google Cloud branding guidelines.

![](https://docs.cloud.google.com/static/looker/docs/images/gcp-rebrand-718.png)

  * Fonts and colors in the Looker platform have been updated to reflect Google Cloud branding.
  * Users can revert to the Looker branding with the **Legacy Branding** toggle, which is enabled by default in Looker 7.18 and will be disabled by default for all instances in Looker 7.20.



* * *

### Quick Start in Explores

[Quick Start](https://docs.cloud.google.com/looker/docs/exploring-data#quick_start) allows users to load prebuilt queries in their Explores.

![](https://docs.cloud.google.com/static/looker/docs/images/explore-quickstart-718.png)

  * The [**Upgraded Explore Field Picker**](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#upgraded_explore_field_picker) beta Labs feature includes a [**Quick Start**](https://docs.cloud.google.com/looker/docs/exploring-data#quick_start) option that lets users load a [modeled query](https://docs.cloud.google.com/looker/docs/reference/param-explore-query) with a single click.
  * The **Quick Start** option shows up by default on a blank Explore that contains modeled queries and can be accessed once again through the lightning icon next to the Explore title.



* * *

### Looker Mobile App Integration

Introducing the Looker platform in a mobile application as a beta Labs feature.

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-app-718.png)

  * Users will now be able to see data anytime and anywhere through the [Looker mobile app](https://docs.cloud.google.com/looker/docs/mobile-app).
  * The mobile app is available to customers using Looker 7.16+.
  * The app is available through the [Google Play Store](https://play.google.com/store/apps/details?id=com.google.looker) for Android 8+ devices and through the [Apple App Store](https://apps.apple.com/us/app/looker-mobile/id1533498070) for iOS 13+ devices.



## **Looker 7.16**

_play_circle_filled_ Expected rollout start: **Sunday, September 20th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, October 1st, 2020**

### Potentially breaking changes

Check out these potentially breaking changes introduced in Looker 7.16. Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * Users will no longer have the ability to cross-filter on custom dimensions.
  * Filtering by a field that is not a part of an Explore used on dashboards (beta) will display a banner with the message `This filter was created using a filter by field outside of the Explores on this dashboard. You can modify the settings and tiles to update, but will need to create a new filter to change the field.`
  * Referencing a field with the syntax `${field_name}` in a **Custom Filter** will cause the Liquid parameters `&#123;&#123;&nbsp;field_name._is_filtered &#125;&#125;` and `&#123;&#123;&nbsp;field_name._in_query &#125;&#125;` to evaluate as true.
  * Values for hidden user attributes do not have to be re-entered when you update a Marketplace extension configuration or Marketplace extension version.
  * [User attributes referenced by access filters](https://docs.cloud.google.com/looker/docs/reference/param-explore-access-filter#even_admins_must_have_filter_values_set_in_the_ui) that have the values `%, NULL` (for **String Filter [advanced]**) and `<0, >=0, NULL` (for **Number Filter [advanced]**) will no longer automatically generate a `WHERE` clause.
  * Users without the `schedule_external_look_emails` permission will no longer be able to save an alert if they add an email address that is not on the domain allow list.
  * The **Load Assets from CDN** setting has been removed from the **Settings** page in the **General** section of the **Admin** panel for Looker-hosted instances. This setting has not been removed from customer-hosted instances, unless the `--force-cdn` startup flag has been enabled on the instance.
  * **Save and Schedule** menu items will no longer appear on embedded Explores when [**Remove Look Navigation**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-embed#remove_look_navigation) is enabled.
  * The `create_sso_embed_url` API endpoint is no longer metered as an admin call and will be excluded from the admin activity quota.
  * The connections drop-down list on the **Persistent Derived Tables** page in the **Admin** panel will only list connections that have PDTs enabled.
  * Adding the LookML parameter `publish_as_db_view: yes` to a PDT definition in production will now create a view without needing to trigger the table to rebuild or without having to modify the SQL or the LookML of the derived table.



* * *

### Alerts to Action Hub

[Users can now send scheduled alerts to Slack.](https://docs.cloud.google.com/looker/docs/alerts-overview)

  * Slack has been added as a new destination for scheduled alerts.
  * This paves the way for support of more alerts to actions in the future.



* * *

### Aggregate Awareness Enhancements

![](https://docs.cloud.google.com/static/looker/docs/images/aggawareness-716.png)

  * Developers now have the ability to use the following persist parameters inside the [`materialization` block of an aggregate table](https://docs.cloud.google.com/looker/docs/reference/param-explore-aggregate-table#materialization): indexes, cluster_keys, partition_keys, distribution, distribution_style.
  * [Aggregate tables](https://docs.cloud.google.com/looker/docs/aggregate_awareness) no longer need to be an exact timeframe match of the filters in an Explore query. For example, an aggregate table that has a daily timeframe dimension can be used for an Explore query that filters on week or month. As long as the dimension in the aggregate table has a timeframe with a finer (or equal) granularity as the timeframes of the dimensions and filters in the Explore query, the aggregate table can be used for the Explore query.



* * *

### JDK 11 Support for Customer-Hosted Instances

![](https://docs.cloud.google.com/static/looker/docs/images/jdk11-716.png)

  * ~~JDK 11 is now supported for customer-hosted instances.~~
  * Developers now have the opportunity to make performance improvements on front-end rendering and background processes on Looker applications.
  * JDK 11 support has been temporarily suspended.



## **Looker 7.14**

_play_circle_filled_ Expected rollout start: **Sunday, August 16th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, August 27th, 2020**

### Potentially breaking changes

Check out these breaking changes introduced in Looker 7.14. Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * An update to our Markdown rendering library has been made to address security vulnerabilities. This change may render trailing HTML tags if the tags are invalid or unbalanced.
  * Looker now accepts the `pkce` code challenge parameter encoded as either Hex or Base64, per OAuth2 specifications.
  * In an Explore with the **Upgraded Explore Field Picker** Labs feature enabled, the view headers will now be sorted by locale rules (spaces, symbols, letters). Capitalization is not taken into account.
  * The API endpoint `/presentation/query` has been modified to accept either a **path or a query parameter** to prevent query timeouts.
  * The Snowflake JDBC driver has been upgraded to **v3.12.8** to ensure that credentials are not logged in plaintext even when higher tracing levels are enabled.
  * If non-alphanumeric characters are used in LookML dashboard names, the [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) will now render the following warning: `LookML Dashboard name should contain only letters, numbers, dashes, and underscores`.
  * The [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) will now render an error when the `join_fields` parameter has invalid syntax within a merge query tile in a LookML dashboard.
  * Imported projects are now always marked as **read-only** and do not show syntax errors.
  * The [**Looker API CORS**](https://docs.cloud.google.com/looker/docs/api-cors) feature is now out of Labs and generally available. A web application is enabled for OAuth when the application has been registered with the Looker instance. If the application's registration info is deleted from the Looker instance, Looker will no longer accept API OAuth requests from that application.



* * *

### Dashboards (Beta): Cross-Filtering

[Cross-filtering](https://docs.cloud.google.com/looker/docs/cross-filtering-dashboards) allows users to cross-filter any size dataset between dashboards.

  * Cross-filtering is now available through the [**Cross-filtering**](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#cross-filtering) (beta) Labs feature.
  * To further optimize performance, we recommend enabling [ **aggregate awareness**](https://docs.cloud.google.com/looker/docs/aggregate_awareness).
  * Cross-filtering will only be enabled on dashboards where tiles are [created from the same Explore](https://docs.cloud.google.com/looker/docs/cross-filtering-dashboards#enabling_cross-filtering_for_individual_dashboards_\(beta\)).



* * *

### Dashboards (Beta): Drag and Drop Filters

Introducing visual editing of filters with the ability to drag and drop filters in dashboards (beta).

Users now have the ability to [use handlebars to grab, move, and reorder filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#moving_and_repositioning_dashboard_\(beta\)_filters) — and drag them into and out of the filter overflow menu.

* * *

### New Blocks and Visualizations in the Looker Marketplace

Check out Search Ads 360, Google Analytics 360, Google Demand Live Events, Report Visualization.

![](https://docs.cloud.google.com/static/looker/docs/images/marketplace_714.png)

  * **Google Search Ads 360** provides analytics around impressions, clicks, conversions, and revenue for search ads.
  * **DV 360** is another new block that is used for comprehensive analytics for display and video advertising on the Google Marketing Platform. It provides analytics around AD and campaign performance, cost, and reach.
  * The Area 120 **Demand Event Block** combines live event, COVID, and weather data to predict future live event attendance during the coronavirus pandemic.
  * **Report Visualization** , available in the Marketplace, can be used for purpose-built visualizations to create traditional report layouts. This is a great block for financial reporting and other line-item-based statements.



## **Looker 7.12**

_play_circle_filled_ Expected rollout start: **Sunday, July 19th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, July 30th, 2020**

### Potentially breaking changes

Check out these breaking changes introduced in Looker 7.12. Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * A new design for the LookML IDE is available to all users with access to LookML projects. The [object browser](https://docs.cloud.google.com/looker/docs/object-browser) is no longer a [Labs](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs) feature; it is now out of beta and generally available. The **IDE Folders Toggle** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) is now fully removed, and the legacy IDE can no longer be enabled.
  * The **.strings files for localization** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) is now fully removed and unavailable to re-enable.
  * The **SnowFlake Unquoted Database** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) is disabled by default. Snowflake connections that have incorrect capitalization in the database name will break.
  * The [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) will now render a warning if there are multiple entries of the following: `derived_table` parameters within a view file, `query` parameters inside an `aggregate table` within a defined `explore` parameter, or `materialization` parameters within an `aggregate_table` within a defined `explore` parameter.
  * The [LookML Validator](https://docs.cloud.google.com/looker/docs/lookml-validation#validating_your_lookml) will now issue a warning for aggregate table names greater than 255 characters. In addition, the aggregate table LookML generator will no longer generate names longer than the maximum allowed characters.
  * The table visualization setting **Bars** [is now called **Cell Visualization**](https://docs.cloud.google.com/looker/docs/table-options#cell_visualization).
  * CSV downloads now allow non-romanized characters in the filename. This may impact automation that relies on the filename being empty for files named with non-romanized characters.
  * The password reset function will lock after too many failed login attempts. The lockout duration is 5 minutes for most customers after 4 failures and 30 minutes for PCI instances after 6 failures.



* * *

### Redesigned IDE

Check out the new IDE in your LookML projects.

![](https://docs.cloud.google.com/static/looker/docs/images/ide_ga_712.png)

  * The new UI design of the LookML IDE is available to all users with access to LookML projects.
  * You can now navigate projects with the [object browser](https://docs.cloud.google.com/looker/docs/object-browser) without having to enable a [Labs](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs) feature.



* * *

### Upgraded Explore Field Picker

Introducing a redesigned Explore UI through the **Upgraded Explore Field Picker** [Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#upgraded_explore_field_picker).

![](https://docs.cloud.google.com/static/looker/docs/images/explore_beta_2_712.png)

  * Offers a smarter [field search](https://docs.cloud.google.com/looker/docs/exploring-data#search_bar) capability.
  * Fields now provide additional [field context](https://docs.cloud.google.com/looker/docs/exploring-data#field-specific_information_and_actions) (table name, SQL, etc.) and [quickstart options](https://docs.cloud.google.com/looker/docs/exploring-data#three-dot_options_menu) for creating new custom fields.
  * A new [**In Use**](https://docs.cloud.google.com/looker/docs/exploring-data#in_use_tab) tab enables users to view and manage selected fields.



* * *

### The Looker Extension Framework (Beta)

Introducing the [Looker extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework), available with the **Extension Framework** Labs feature, which is enabled by default.

![](https://docs.cloud.google.com/static/looker/docs/images/labs_extension_framework_712.png)

  * This feature allows developers to build custom JavaScript applications and tools on top of Looker without requiring them to set up their own stacks for building.
  * Applications can be used in Looker or embedded in other applications.



## **Looker 7.10**

_play_circle_filled_ Expected rollout start: **Sunday, June 14th, 2020** _check_circle_ Expected final deployment and download available: **Monday, June 29th, 2020**

### Looker API CORS

A new experimental Labs feature that permits browser-based applications to directly call the Looker API without needing a proxy server for the API calls.

![](https://docs.cloud.google.com/static/looker/docs/images/api-cors-labs-710.png)

  * Enabling the **Looker API CORS** [Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#looker_api_cors) allows browser-based web applications to [call the Looker API across domain boundaries using the Cross Origin Resource Sharing (CORS) protocol](https://docs.cloud.google.com/looker/docs/api-cors). Each web application must be registered with the Looker instance and enabled by a Looker admin. Disabling this feature immediately blocks all cross-domain web requests to the Looker API.
  * This feature greatly reduces developer time, infrastructure costs, and operational overhead.



* * *

### Dashboards (Beta): Filter Themes

Introducing the ability to customize embed filter colors.

![](https://docs.cloud.google.com/static/looker/docs/images/embed-filters-theme-710.png)

The [**Themes** page](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) in the **Admin** panel now offers the option to [customize primary buttons and filter controls in dashboards (beta)](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#button_colors) using the **Primary Button Color** setting.

* * *

### Dashboards (Beta): Enhancements

Introducing new menu options on dashboard (beta) tiles and the ability to retrieve dashboard LookML from dashboards (beta).

![](https://docs.cloud.google.com/static/looker/docs/images/dashboards-beta-lookml-710.png)

  * [Tile menus](https://docs.cloud.google.com/looker/docs/viewing-dashboards#dashboard_\(beta\)_tiles) on dashboards (beta) now present the options to **Clear Cache & Refresh** and **View Look**. _**Note:** The **View Look** option is only presented on tiles that are derived from existing Looks._
  * You can now [copy the LookML from a dashboard (beta)](https://docs.cloud.google.com/looker/docs/viewing-dashboards#getting_the_lookml_from_a_dashboard_\(beta\)) by clicking **Get LookML** from the dashboard menu.
  * LookML dashboards can now be configured to use [filter](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards) controls available in dashboards (beta). The LookML for user-defined dashboards with filters configured using dashboards (beta) contain a [`ui_config` parameter](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#ui_config_\(for_dashboards_\(beta\)_only\)) for each filter.



* * *

### Database Connection Pooling

A new beta Labs feature that can improve query performance and support more concurrent users for supported database dialects.

![](https://docs.cloud.google.com/static/looker/docs/images/databases-connection-pooling-labs-710.png)

  * A new beta **Database Connection Pooling** [Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#database_connection_pooling) is now available for Redshift, Postgres, and Snowflake SQL dialects.
  * Enabling this Labs feature optimizes database connection reuse via the JDBC driver.



## **Looker 7.8**

_play_circle_filled_ Expected rollout start: **Sunday, May 17th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, May 28th, 2020**

### Aggregate Awareness

Looker will detect and run a query against the most efficient aggregate table in your database.

![](https://docs.cloud.google.com/static/looker/docs/images/lookml-agg-table-78.png)

  * [Aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness) increases database query performance and decreases costs by allowing you to define aggregate tables in LookML.
  * Aggregate tables are roll-ups of more granular data tables.
  * Looker automatically queries the aggregate tables instead of the larger, more granular tables whenever possible.



* * *

### Parallel Persistent Derived Table Builds

Multiple PDTs can now be built at once.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-connections-parallel-pdt-78.png)

  * Increases the number of PDTs that can be built at one time per connection.
  * The default concurrency is set to 1. The concurrency can be increased in the [**Max PDT Builder Connections**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_pdt_builder_connections) field for a connection's settings.



* * *

### Data Dictionary

The Data Dictionary extension is now available in the Looker Marketplace and can be enabled by switching on the Extension Framework and Marketplace [Labs](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#current_labs_features) features.

![](https://docs.cloud.google.com/static/looker/docs/images/marketplace-data-dictionary-78.png)

  * The [Data Dictionary](https://docs.cloud.google.com/looker/docs/using-looker-data-dictionary) is a centralized source for the field definitions of a selected model and Explore.
  * A field profiler displays information about a specific field and previews its top values.
  * Quick filters help users find the descriptions and field types they need.
  * The Data Dictionary retains Looker's [permissions](https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions) structure — users can see only the models they have access to.



* * *

### New Marketplace Content

New and modified content is now available in the Looker Marketplace.

![](https://docs.cloud.google.com/static/looker/docs/images/marketplace-covid19-78.png)

  * A new data block launched in the [Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) called Covid-19. It has a pre-built data model and dashboards built around public COVID-19 data from the _New York Times_ and Johns Hopkins.
  * A new Radial Gauge visualization offers customizable ranges, target values, and formatting.
  * A new Braintree block by Looker helps you better understand your business' transaction data.



## **Looker 7.6**

_play_circle_filled_ Expected rollout start: **Sunday, April 19th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, April 29th, 2020**

### Persistent Derived Table Admin Page Improvements

Improved searchability, page performance, and monitoring on the **persistent derived tables** page in the **Admin** panel.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-pdt-76.png)

  * Looker admins can use the **Persistent Derived Tables** panel on the Admin page to [view PDTs by connection](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#reading_the_pdt_page) and [search for specific PDTs](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#searching_and_filtering_the_pdt_page).
  * Non-admin users with the [`see_pdts`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_pdts) permission can view information about PDTs from models for which they have data access.



* * *

### LookML Refinements

Introducing [LookML refinements](https://docs.cloud.google.com/looker/docs/lookml-refinements) that allow users to build on the LookML of views and Explores in projects.

![](https://docs.cloud.google.com/static/looker/docs/images/lookml_refinements_76.png)

  * LookML refinements provide users a way to build on the LookML of views and Explores in your projects.
  * LookML refinements are ideal for projects with Looker Blocks, which use pre-built pieces of LookML; projects that import files from other projects; projects where you often need to generate your files from tables in your database; and situations where you want to share LookML between models or projects while making customizations in each place (that is, hub-and-spoke configurations).



* * *

### Removing the Automatic S3 Backup (Customer-Hosted Instances Only)

Automatic S3 backup will no longer be available for customer-hosted instances.

![](https://docs.cloud.google.com/static/looker/docs/images/s3-backups-76-rn.png)

  * Looker highly recommends [hosting your own backup.](https://docs.cloud.google.com/looker/docs/creating-backups)
  * This is recommended as a daily practice to ensure that your Looker content and configurations are continuously saved.



* * *

### Alerts User Management Page

Introduced a new page for users to manage their alerts.

![](https://docs.cloud.google.com/static/looker/docs/images/user-manage-alerts-76-rn.png)

Users can view and manage their alerts through an [alerts user management page](https://docs.cloud.google.com/looker/docs/user-alerts) available from their user profile.

## **Looker 7.4**

_play_circle_filled_ Expected rollout start: **Sunday, March 15th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, March 26th, 2020**

### Dashboards (Beta) Updates

Introducing new functionalities on [dashboards (beta)](https://docs.cloud.google.com/looker/docs/viewing-dashboards).

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-beta-download-options-74.png)

  * Dashboards can now be [downloaded](https://docs.cloud.google.com/looker/docs/viewing-dashboards#downloading_data_from_a_dashboard_\(beta\)) in PDF and CSV formats. _Note: PDF will still render the old dashboard design._
  * A tile's content can be [downloaded](https://docs.cloud.google.com/looker/docs/viewing-dashboards#downloading_data_from_dashboard_\(beta\)\[FIX\]tiles) in these formats: TXT, Excel, CSV, JSON, HTML, Markdown, and PNG.
  * A [grid layout option](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#using_tiles_with_grid_layout) is now supported.
  * Merged results are now [filterable](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_filters) and fully supported.



* * *

### New LookML Syntax

Introducing new `filters` and `order_by_field` syntax.

![](https://docs.cloud.google.com/static/looker/docs/images/lookml-new-syntax-74.png)

  * New [`filters` syntax](https://docs.cloud.google.com/looker/docs/reference/param-field-filters) is more concise and simpler to write. The square brackets denote an array with key-value pairs.
  * Measures can now be [sorted by other measures](https://docs.cloud.google.com/looker/docs/reference/param-field-order-by-field) in the `order_by_field` parameter.



* * *

### Slack Integration Updates

Introducing the ability to add multiple Slack workspaces and Looker homepage in Slack.

![](https://docs.cloud.google.com/static/looker/docs/images/slack-app-beta-74.png)

  * A single Looker instance can now be [connected to multiple Slack workspaces](http://docs.looker.com/sharing-and-publishing/scheduling-and-sharing/scheduling-slack#enabling_the_integration_in_the_looker_action_hub).
  * Users can [authenticate into each workspace](http://docs.looker.com/sharing-and-publishing/scheduling-and-sharing/scheduling-slack#authenticating_into_your_slack_workspace_from_the_account_page) and [choose from connected workspaces](http://docs.looker.com/sharing-and-publishing/scheduling-and-sharing/scheduling-slack#delivering_data_to_slack) when sending or scheduling content.
  * Users can [see their favorite Looker content and folders in Slack](https://docs.cloud.google.com/looker/docs/scheduling-slack#viewing_your_looker_app_home_tab_in_slack).



* * *

### Marketplace Content

More blocks and visualizations are now available in the [Looker Marketplace](https://docs.looker.com/data-modeling/marketplace).

![](https://docs.cloud.google.com/static/looker/docs/images/marketplace-beta-74.png)

Added the following blocks:

  * Salesforce
  * Hubspot
  * Square
  * Time Tracking Essentials
  * Zendesk Analysis



Added the following Visualizations:

  * Aster
  * Spider



* * *

### Action Hub Updates

Introducing two new Google actions - Google Drive & Google Sheets.

![](https://docs.cloud.google.com/static/looker/docs/images/google-actions-74.png)

  * Users now have the ability to use an Oauth-based [Google Drive action](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-google-drive-integration.hmd) to send PDFs, Images, and more straight to Google Drive from Looker.
  * Users now have the ability to use an Oauth-based [Google Sheets action](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-the-google-sheets-integration) to send CSVs from Looker straight to Google Sheets, as well as the ability to maintain live linkages or send static snapshots.



## **Looker 7.2**

_play_circle_filled_ Expected rollout start: **Sunday, February 9th, 2020** _check_circle_ Expected final deployment and download available: **Thursday, February 20th, 2020**

### Dashboards (Beta) Updates

Introducing new functionalities on [dashboards (beta)](https://docs.cloud.google.com/looker/docs/viewing-dashboards).

![](https://docs.cloud.google.com/static/looker/docs/images/dashboards-beta-72-alerts.png)

  * Introducing the ability to create and manage [alerts](https://docs.cloud.google.com/looker/docs/alerts-overview) with a new simplified UI.
  * Introducing support for static maps ([regions](https://docs.cloud.google.com/looker/docs/map-points-options) and [point](https://docs.cloud.google.com/looker/docs/map-regions-options)).
  * The LookML parameter [ `parameter` ](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) is now supported in dashboard (beta) filters, specifically for the following filter types: 
    * Radio buttons
    * Button group
    * Drop-down menu
    * Advanced (is)



* * *

### Team Homepage Settings

[Homepage settings](https://docs.cloud.google.com/looker/docs/admin-panel-general-homepage) are out of Labs (beta) and in the Admin section under General Settings.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-homepage-72.png)

  * Looker admins now have the ability to [set a default homepage for a specific team or individual within the Admin settings](https://docs.cloud.google.com/looker/docs/admin-panel-general-homepage#setting_a_homepage_for_a_specific_user_or_group).
  * This is especially helpful for onboarding new users and for [global organizations with teams who speak different languages](https://docs.cloud.google.com/looker/docs/admin-panel-general-homepage#setting_a_default_homepage_for_your_instance).
  * Any URL can be used as the team homepage, including Markdown files and boards.
  * Suggested content has been removed from the default platform homepage because of performance issues and customer feedback.



* * *

### API 4.0 (Experimental)

Introducing a new experimental version of the Looker API, version 4.0.

![](https://docs.cloud.google.com/static/looker/docs/images/api-40-exp-72.png)

  * Supports "strongly typed" language SDKs such as Kotlin and Swift.
  * All new major API improvements will be made to API 4.0 only — there may be breaking changes until we reach beta version.
  * [Click here to view the Looker API 4.0 reference documentation](https://docs.cloud.google.com/looker/docs/h/looker/docs/reference/looker-api/latest).



## **Looker 7.0**

_play_circle_filled_ Expected rollout start: **Sunday, January 10th, 2020** _check_circle_ Expected final deployment and download available: **Monday, February 3rd, 2020**

### Marketplace

Marketplace (beta) Labs feature is enabled by default.

![](https://docs.cloud.google.com/static/looker/docs/images/marketplace-labs-beta-70.png)

  * Ensures that users can easily discover relevant and helpful [marketplace](https://docs.cloud.google.com/looker/docs/marketplace) choices.
  * Enables Looker users to discover, install, and uninstall content like blocks, applications, and custom visualizations. This initial release of the marketplace is publishing the following: 
    * Sales Application
    * 23 Looker Blocks
    * 12 custom visualizations



* * *

### IDE Improvements

Introducing bulk edits for files and folders in the IDE as well as improvements to the IDE UI.

![](https://docs.cloud.google.com/static/looker/docs/images/ide-folders-bulk-edit-70.png)

  * Ability to perform bulk [move](https://docs.cloud.google.com/looker/docs/ide-folders#moving_files_and_folders_in_bulk) and [delete](https://docs.cloud.google.com/looker/docs/ide-folders#deleting_files_and_folders_in_bulk) actions on folders and files.
  * Ability to use [Shift + click](https://docs.cloud.google.com/looker/docs/ide-folders#bulk_editing_files_and_folders) as a shortcut to select a range of folders or files within the IDE sidebar.
  * Ability to [move a file](https://docs.cloud.google.com/looker/docs/ide-folders#moving_items_in_a_foldered_project) to a collapsed folder.
  * Ability to [expand a folder](https://docs.cloud.google.com/looker/docs/ide-folders#moving_items_in_a_foldered_project) after hovering a file over the folder.
  * Ability to [**Create a View from Table** within a folder](https://docs.cloud.google.com/looker/docs/ide-folders#creating_items_within_a_folder).
  * Ability to [collapse the IDE sidebar](https://docs.cloud.google.com/looker/docs/lookml-project-files#collapse_ide_sidebar).
  * The classic IDE is still available as a legacy feature called **IDE Folders Toggle**. [View the Legacy Features End-of-Life Schedule](http://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067).
  * Ability to [see imported project files natively in the IDE](https://docs.cloud.google.com/looker/docs/importing-projects#viewing_files_from_an_imported_project), organized into a folder called **imported_projects** in the IDE sidebar.



* * *

### Enhanced PDT Rebuilds

Use the power of the LookML model outside of Looker.

![](https://docs.cloud.google.com/static/looker/docs/images/pdt-stable-names-70.png)

  * For every rebuild of a PDT, the given table name will now be unique. This will yield increased stability and faster rebuilds for certain dialects.
  * Stable, statically named view tables can now be generated on top of PDTs. A stable database view will only be published for its underlying PDT when that PDT gets rebuilt. By having a static, friendly name, the view table allows you to consistently access a PDT via SQL on the source database. This feature provides users with the ability to hook up other analytics or data science tools to Looker-governed data. [Learn more about stable view tables](https://docs.cloud.google.com/looker/docs/reference/param-view-publish-as-db-view).



* * *

### System Activity Dashboard Enhancements

System Activity dashboards can be enabled through a beta Looker Labs feature: System Activity Model.

![](https://docs.cloud.google.com/static/looker/docs/images/sys-activity-dashboards-70.png)

  * Improved and reorganized dashboards in a logical and actionable way to provide users with more efficient monitoring of the Looker instance. [Learn more about System Activity dashboards](https://docs.cloud.google.com/looker/docs/system-activity-pages).
  * Use the **Errors and Broken Content** dashboard to stay on top of all the things that need your attention for quick remediation.
  * Visualize potential performance issues via the new scheduler heatmap and avoid bottlenecks.
  * These are the titles of the available dashboards: 
    * **User Activity**
    * **Content Activity**
    * **Performance Audit 1**
    * **Performance Audit 2**
    * **Errors and Broken Content**



* * *

### Boards Section Descriptions

To provide more context to users viewing boards, the feature now includes descriptions for each section.

![](https://docs.cloud.google.com/static/looker/docs/images/boards-section-description-70.png)

[Learn more about how boards can help your organization](https://docs.cloud.google.com/looker/docs/presenting-content).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
