---
url: https://docs.cloud.google.com/looker/docs/looker-22-release-highlights/
title: Looker 22 release highlights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:01:32.353800+00:00
---

# Looker 22 release highlights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-22-release-highlights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  Looker 22 release highlights Stay organized with collections  Save and categorize content based on your preferences. 

## **Looker 22.20**

_play_circle_filled_ Expected rollout start: **Monday, November 14th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, December 1st, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * The **Use old dashboard routes** legacy feature has been removed. This means that, in URLs and other dashboard file paths, `/dashboards/` indicates a new dashboard experience dashboard, and `/dashboards-legacy/` indicates a legacy dashboard.
  * The [**Can use Legacy Dashboards** legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#current_legacy_features) has been added.
  * The **Prerender iframes (before data loads) for custom visualizations** Experimental Labs feature has moved to Beta.
  * The **Data Studio** feature has been removed from Labs. Users may link their Google account with their Looker account to access Looker instances with Looker Studio.
  * Stacked chart visualizations for queries that have [**Row Totals**](https://cloud.google.com/looker/docs/exploring-data#displaying_totals) selected now include a series for row totals (previously this was supported for group charts, but not stacked charts). This may cause unexpected behavior in stacked chart visualizations for queries that include row totals, which previously excluded the row totals series from the visualization. To exclude this series from a visualization, either clear **Row Totals** from the **Data** bar, or select [**Hide from visualization**](https://cloud.google.com/looker/docs/creating-visualizations#hiding_fields_from_visualizations) in the **Row totals** column gear menu.
  * Area visualizations with null values that also have the **Unpin Axis From Zero** setting turned on and the **Plot Null Values** setting turned off will now behave as expected and unpin the y-axis from 0. An issue that has since been resolved was causing area charts to plot these visualizations from 0.
  * The **Revert to Legacy Dashboards** legacy feature was removed in Looker 22.20. You can no longer use the new dashboards UI to downgrade a dashboard to a legacy dashboard.
  * The configuration settings for SAML, LDAP, and OIDC authentication types have changed. When mirror LDAP/SAML/OIDC groups configuration is turned off under the **Groups & Roles** section for the respective authentication type, Looker can no longer use an externally managed group as the default group for new users when they first log in to Looker. Admins will need to change the **New User Groups** setting to a non-externally managed group before making any changes to the existing configuration.
  * [**Custom fields**](https://docs.cloud.google.com/looker/docs/custom-fields) is now generally available.



* * *

### New BI visualizations

New ways to visualize your BI data

Looker's new visualizations include the following:

  * **[Data history playback (data change over time animation) for visualization](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#data_history_playback_data_change_over_time_animation_for_visualization)** Labs feature
  * Two new scatterplot chart visualization config options: [**Cluster Points**](https://docs.cloud.google.com/looker/docs/scatter-options#cluster_points) and [**Plot Quadrants**](https://docs.cloud.google.com/looker/docs/scatter-options#plot_quadrants)
  * Ability to [hide individual pivots from visualizations](https://docs.cloud.google.com/looker/docs/exploring-data#hiding_specific_columns_of_data_in_a_pivoted_visualization)
  * Ability to [zoom in on Cartesian charts](https://docs.cloud.google.com/looker/docs/viewing-dashboards#zooming_on_cartesian_charts)
  * Ability to view visualizations in [full screen and expanded views](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#full_screen_visualizations) within a dashboard



* * *

### Connected Sheets

Connected Sheets for Looker generally available as of 22.20

This feature must be enabled using a new **Admin** setting.

**Note:** The [staged rollout of Connected Sheets for Looker began on February 1, 2023](https://workspaceupdates.googleblog.com/2023/02/connected-sheets-looker.html) and will reach 100% of Google Workspace users by February 13. By that date, the **Connect to Looker** menu item in the Sheets **Data** menu, under **Data connectors** , will be available for all users. A Looker admin must also enable the feature on each Looker instance.

  * [Connected Sheets for Looker](https://docs.cloud.google.com/looker/docs/connected-sheets) lets you explore data from your LookML models through the familiar Google Sheets interface.
  * Looker admins must first enable the feature on the new **BI Connectors** admin page, which can be found in the **Platform** section of Looker's **Admin** menu

![](https://docs.cloud.google.com/static/looker/docs/images/bi-connectors-2220.png)

  * Connected Sheets for Looker and the new **BI Connectors** admin page are available only for Looker instances that are hosted on Google Cloud.




* * *

### Looker iOS Mobile App

Drilling support and alerts in Looker iOS mobile app

**Looker iOS** mobile app now includes **drilling support** that users can leverage to drill data similar to Looker Web.

Looker users can now receive data **alerts** via push notifications on their iOS devices that will allow them to get those on the go and take timely action.

* * *

### Legacy dashboards

Legacy dashboards are being removed

The **Revert to Legacy Dashboards** legacy flag has been removed as of Looker 22.20. This means that you can no longer use the new dashboards UI to downgrade a dashboard to a **dashboards-legacy**. The **Can use Legacy Dashboards** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#current_legacy_features) has been added to enable users to view legacy dashboards until it is deprecated in Looker 23.6. For more information, see the [Removing the legacy dashboard experience - a timeline from Looker 21.20 (November 2021) through Looker 23.6 (April 2023)](https://docs.cloud.google.com/looker/docs/best-practices/legacy-dashboard-deprecations) Best Practices page.

* * *

### Cookieless embeds

Modern cookieless embedding authentication preview

[**Cookieless Embed**](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#proper_hosting_for_sso_embedding) is an experimental Labs feature that allows an embed user session to be created without the use of cookies. This features will require some server side configuration. Please see the [Looker JavaScript Embed SDK README](https://github.com/looker-open-source/embed-sdk#cookieless-embed) for setup instructions. The **Cookieless Embed** feature is set to **ON** by default.

## **Looker 22.18**

_play_circle_filled_ Expected rollout start: **Monday, October 17th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, October 27th, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * The **Dashboard Filters Location** Labs feature is now out of Labs and is [generally available](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#filters_location).
  * The **Custom buttons for dashboards** Labs feature is now out of Labs and is [generally available](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_buttons).
  * The [**Custom Fields**](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#custom_fields) Labs feature is enabled by default across Looker instances.
  * [API 4.0](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) was made generally available (stable) in Q1 2022. The majority of the API endpoints were promoted to stable to correctly reflect their status. Endpoints marked as beta are still subject to breaking changes.
  * Dashboard buttons linking to other Looker pages will keep the `/embed` prefix if redirected from an embedded dashboard.



* * *

### New ways to connect Looker and Looker Studio

New Labs options to view Looker data in Looker Studio

The [Looker connector](https://support.google.com/looker-studio/answer/12388266), now available in [Public Preview](https://cloud.google.com/products#section-22), lets you view data from a Looker Explore in a Looker Studio report by connecting Looker as a [data source](https://support.google.com/looker-studio/answer/6302399). If you would like to view Looker data in a Looker Studio report, first enroll in the Public Preview by filling out a [Looker Studio / Looker Integration Public Preview](https://forms.gle/bw7uaNUTcsEQxVRK7) form. Once enrolled, you can:

  * Enable the [**Data Studio**](https://docs.cloud.google.com/admin-panel-general-labs#data_studio) Labs feature
  * Use the Looker connector in Looker Studio to add a Looker instance as a [data source](https://support.google.com/looker-studio/answer/6302399)
  * Leverage another new Labs feature, [**Link to Data Studio from Explore**](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#link_to_data_studio_from_explore), which lets you open an [Explore query](https://docs.cloud.google.com/looker/docs/exploring-data) in a Looker Studio [report](https://support.google.com/looker-studio/answer/6302400) by using the [**Open in Data Studio** Explore gear menu option](https://docs.cloud.google.com/looker/docs/exploring-data#the_explore_actions_gear_menu). This gear menu option is available only for the [Google-based database dialects](https://docs.cloud.google.com/looker/docs/dialects) that are [supported by Looker Studio](https://support.google.com/looker-studio/topic/9281288).



The Looker connector and associated Labs features are available only for Looker instances that are hosted on Google Cloud.

## **Looker 22.16**

_play_circle_filled_ Expected rollout start: **Monday, September 19th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, September 29th, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * Transport Layer Security (TLS) 1.0 and 1.1 will be deprecated. Effective September 19, 2022, this will require customer-hosted users to update their internal database to a version of MySQL (5.6.46 or later) or to a version of an alternate DBMS that supports TLS 1.2 or later. Customers (both those who host their own databases and those for whom Looker hosts their databases) who use MySQL as a data source will also need to ensure that these databases are version 5.6.46 or later.
  * Key frontend dependencies for the Looker application will [end support for IE11 in 22.16](https://docs.cloud.google.com/looker/docs/best-practices/looker-internet-explorer-11-support).
  * Customer-hosted instances using SendGrid. As of Looker 22.16, the SendGrid services on customer-hosted instances is deprecated as the default SMTP service. Customers can still configure their own managed SMTP services for their customer-hosted Looker instances.



* * *

### Content Navigation for Embed

New Labs Option for Embed Content Navigation

![](https://docs.cloud.google.com/static/looker/docs/images/embed-spaces-2200.png)

A new Looker Labs feature **[Embed Content Navigation](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#embed_content_navigation)** controls whether the new embed content navigation is available on an instance. This Labs feature will now default to on, with the option of being disabled. Enhanced content navigation is now available for [embedded Looks and Explores](https://docs.cloud.google.com/looker/docs/viewing-embedded-items#viewing_folders_on_embedded_looks_explores_and_dashboards).

* * *

### Enhanced Query Admin UI

Query Admin UI update and pagination enhancement

![](https://docs.cloud.google.com/static/looker/docs/images/enhanced_query_admin.png)

A [Looker Labs feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#enhanced_query_admin) that migrates the **Query Admin** UI from Angular to React refreshes the look-and-feel with standard Looker components. In addition, pagination is available, as well as a separate tab for recent and complete queries, allowing customers with large history tables to effectively administer their instances.

* * *

### General availability of Query Metrics in System Activity

Performance Recommendations dashboard is now GA

The [**Query Performance Metrics** Explore](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#query_performance_metrics) and [**Performance Recommendations** dashboard](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#performance_recommendations_dashboard) are now generally available.

## **Looker 22.14**

_play_circle_filled_ Expected rollout start: **Monday, August 15th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, August 25th, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * Sorting behavior has been changed for [**bin**](https://docs.cloud.google.com/looker/docs/custom-fields#custom_binning) type custom fields on an Explore, such that they are sorted according to the tier number instead of alphabetically on the **bin** column. 



* * *

### New LookML Runtime is GA

New LookML Runtime is generally available and enabled by default across Looker instances.

![](https://docs.cloud.google.com/static/looker/docs/images/new_lookml_ga_2214.png)

  * The **New LookML Runtime** feature is now GA and enabled by default across Looker instances.
  * **New LookML Runtime** provides faster LookML validation and content validation, more performant loading of Explores and dashboards, and faster SQL query writing, among other performance improvements.
  * You can disable the **New LookML Runtime** feature for a specific project by adding [`new_lookml_runtime: no`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime) to the project's manifest file.
  * You can revert to legacy LookML runtime at the instance level by turning on the **Legacy LookML Runtime** legacy feature.



* * *

### Persistent derived tables (PDTs) for Google BigQuery connections with OAuth

Persistent derived tables (PDTs) are now supported for Google BigQuery connections that use OAuth authentication.

![](https://docs.cloud.google.com/static/looker/docs/images/pdts_bq_oauth_2214.png)

For Google BigQuery connections that use OAuth, Looker can now access your database for PDT processes using a separate BigQuery service account that you specify in Looker's connection settings. See [Enabling PDTs for Looker connections to BigQuery with OAuth](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#bq_pdts_oauth) for more information. 

* * *

### Looker Docs are migrating

Docs will be found at cloud.google.com/looker/docs beginning on August 22, 2022.

  * All documentation pages will be migrated.
  * Redirects will be put in place so that docs.looker.com URLs will arrive at the proper location.



## **Looker 22.12**

_play_circle_filled_ Expected rollout start: **Monday, July 18th, 2022** _check_circle_ Expected final deployment and download available: **Tuesday, August 2nd, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * To improve query performance, the history table has been split. As a result, [query context comments](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#context_comments_for_sql_queries) and [Google BigQuery job labels](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#job_labels_and_context_comments_for_bigquery_connections) will no longer include a `history_id` value. Use `history_slug` instead. If you have a workflow that relies on running query data, this might be a breaking change for you. Please review your workflows for any potential impact. 
  * The Add Looks to dashboards [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) has been removed. You can no longer add tiles based on saved content (also known as "Looks") to dashboards directly from the Add menu. See the [**Adding tiles from a Look** section](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_tiles_from_a_look) on the **Creating user-defined dashboards** documentation page for adding saved content to dashboards.** 



* * *

### Dashboards

Add a dashboard to one or more boards.

![](https://docs.cloud.google.com/static/looker/docs/images/add-to-boards-window.png)

You can now [add a dashboard to one or more boards](https://docs.cloud.google.com/looker/docs/presenting-content#adding_with_the_add_to_boards_icon) by selecting the **Add to boards** button on the dashboard. 

## **Looker 22.10**

_play_circle_filled_ Expected rollout start: **Monday, June 13th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, June 23rd, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * There are no breaking changes with Looker version 22.12



* * *

### Table Column Ordering

Manual column ordering is now respected in downloads for most cases.

[**Manual column ordering**](https://docs.cloud.google.com/looker/docs/table-options#manually_moving_and_pinning_columns) in table visualizations is now respected in most cases for downloaded data when **With visualization options applied** is selected in the download pop-up. Some exceptions apply: see the [Downloading content](https://docs.cloud.google.com/looker/docs/downloading#results) page for more information.

## **Looker 22.8**

_play_circle_filled_ Expected rollout start: **Monday, May 16th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, May 26th, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * Beginning with Looker 22.8, Looker Legacy Encryption is no longer supported. Instances must be [migrated to GCM Encryption](https://docs.cloud.google.com/looker/docs/migrating-to-aes-256-gcm-encryption) prior to upgrade. AES-256 Galois/Counter Mode (GCM) encryption is now the default for customer-hosted installations. Admins of new customer-hosted installations will have to [generate an encryption key](https://docs.cloud.google.com/looker/docs/installing-looker-application#create_an_encryption_key) before installing the Looker application. 



* * *

### Forecasting

A new Labs feature lets users automatically project a forecast on top of their Explore data.

![](https://docs.cloud.google.com/static/looker/docs/images/forecast-data-display-2114.png)

The [**Forecasting**](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#forecasting) Labs feature, which lets users add data projections to new or existing Explore queries to help users predict and monitor specific data points, is now enabled by default in preparation for general availability. 

## **Looker 22.6**

_play_circle_filled_ Expected rollout start: **Monday, April 18th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, April 28th, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * **AES-256 Galois/Counter Mode (GCM) encryption** is now the default for customer-hosted installations. New customer-hosted installations will have to [generate an encryption key](https://docs.cloud.google.com/looker/docs/installing-looker-application#create_an_encryption_key) before installing the Looker application. Looker Legacy Encryption will no longer be supported starting in Looker 22.8. Instances must be migrated to GCM Encryption prior to upgrade. 
  * A new legacy feature, **Legacy LookML Runtime** , disables** New LookML Runtime** by default for all LookML projects. Can be overwritten by adding the [`new_lookml_runtime`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime) LookML parameter to a LookML project's manifest file. 
  * A new legacy feature, **Legacy Hosted Action Hub** , allows all hosted action requests to instead use the Legacy Hosted Action Hub. The [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_feature_schedule) will be removed starting in Looker 22.12. 



* * *

### Enhanced Action Hub is now GA

The Enhanced Action Hub Service offers improved reliability, performance, and scalability.

  * New actions offer integrations for sending data from Looker to Salesforce and Facebook for better targeting. With the Salesforce Campaigns Action, customers can send custom lists of leads or contacts from Looker to populate new or existing campaigns within Salesforce.
  * With the Facebook Custom Audiences Action, customers can use their first-party data within Looker to create, update, or replace customer lists in Facebook Custom Audiences.



* * *

### New LookML Runtime

New LookML Runtime improves speed and performance.

`new_lookml_runtime: yes`

  * Offers faster LookML and content validation, more performant loading of Explores and dashboards, and faster SQL query writing.
  * Enabled by default. Can be disabled at the project level with the [`new_lookml_runtime`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime) LookML parameter, or at the instance level with the [Legacy LookML Runtime](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_feature_schedule) legacy feature.



* * *

### First Time User Experience

We've created an onboarding walkthrough for first-time users.

![](https://docs.cloud.google.com/static/looker/docs/images/ftue_enable.png)

  * Admins logging in to new trial Looker instances for the first time will see guidance in the UI to help set up their instance and to connect to and explore their data.
  * These guides will show up only for new instances whose locale/language is set to English, starting with Looker 22.6.



* * *

### Looker Marketplace

The updated Looker Marketplace offers an improved experience.

![](https://docs.cloud.google.com/static/looker/docs/images/dev-marketplace-2120.png)

Looker Marketplace now offers improved performance and installation reliability. 

* * *

### PDT dependency graphs in a new tab

![](https://docs.cloud.google.com/static/looker/docs/images/pdt-dependency-new-tab.png)

Lets users open PDT dependency graphs in a new tab from the [PDT details modal](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#pdt_details_modal). 

## **Looker 22.4**

_play_circle_filled_ Expected rollout start: **Monday, March 14th, 2022** _check_circle_ Expected final deployment and download available: **Wednesday, March 30th, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * Customers on Looker 22.4 need to update their mobile app version to the latest Looker mobile version (v1.2.3) to continue using Looker on iOS mobile devices. 
  * Filenames in a LookML project can no longer contain a `%` character. Existing files that contain `%` characters will display an error and a tooltip explaining why the files need to be renamed to remove the character. 



* * *

### API 4.0

The new Looker [API 4.0](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest) is now GA.

![](https://docs.cloud.google.com/static/looker/docs/images/api-4.0-ga-22.4.png)

  * This generally available Looker API version has multiple breaking and additive changes that promote multiple endpoints from beta to stable. [Read more about these changes in this document.](https://docs.cloud.google.com/looker/docs/api-4-ga)
  * The Looker API 3.1 and 3.0 versions are unaffected.
  * Looker and community-supported SDKs will be updated to support Looker API 4.0 GA endpoints.



* * *

### Custom fields permission

Looker is introducing a standalone permission for custom fields used in Explores: [`create_custom_fields`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#create_custom_fields).

![](https://docs.cloud.google.com/static/looker/docs/images/custom-fields-perm-22.4.png)

  * Grants users the specific permission to create and use [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) in Explores.
  * Separates a user's ability to create custom fields from the user's ability to create [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations).



## **Looker 22.2**

_play_circle_filled_ Expected rollout start: **Monday, February 15th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, February 24th, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * Errors that occur before any data is streamed will now be injected into XLSX downloads. 
  * When a [table chart](https://docs.cloud.google.com/looker/docs/table-options) column is resized, the content of the header row automatically wraps to multiple lines, if necessary, so the content is clearly readable. This can be configured with the new [**Truncate Column Names**](https://docs.cloud.google.com/looker/docs/table-options#truncate_column_names) table chart option. 



* * *

### Organize LookML dashboards in folders

We've introduced the ability to add LookML dashboards to folders.

![](https://docs.cloud.google.com/static/looker/docs/images/lookml-dashboards-folders-222.png)

  * Lets users [move LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#moving_lookml_dashboards_outside_of_the_lookml_dashboards_folder) into folders other than the [**LookML Dashboards**](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards#lookml_dashboards_folder) folder.
  * Brings parity to how user-defined dashboards can be organized.
  * Lets users place better access controls on LookML dashboards.



## **Looker 22.0**

_play_circle_filled_ Expected rollout start: **Tuesday, January 18th, 2022** _check_circle_ Expected final deployment and download available: **Thursday, January 27th, 2022**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance.

  * PrestoSQL and Trino now default to `set SSLVerification=NONE` (if **Verify SSL** is not set) or `set SSLVerification=FULL` (if **Verify SSL** is set). If you set your own value for `SSLVerification`, that value will be used. 
  * [Support access](https://docs.cloud.google.com/looker/docs/admin-panel-general-support-access) is disabled by default for all instances. Customers must use an allowlist to grant specific people access to their instance. 
  * The following JDBC drivers have been updated: Firebolt (v.1.21), Microsoft SQL Server (v.9.4), Databricks Spark (v.2.6.21.1039), and Amazon Athena (v.2.0.25.1001). 
  * Popular fields are no longer displayed in the [field picker search bar](https://docs.cloud.google.com/looker/docs/exploring-data#search_bar). Admins can enable a legacy feature, [**Popular fields in explore search**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#popular_fields_in_explore_search), to restore the [**Popular Fields**](https://docs.cloud.google.com/looker/docs/exploring-data#selecting_fields_from_the_popular_fields_drop-down) drop-down to Explore searches. The [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_feature_schedule) will be removed starting in Looker 22.20. 
  * A new legacy feature, **Allow double click to select text in textarea in Table Visualizations** , allows users to double-click on table cell values to manually select text. The [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_feature_schedule) will be removed starting in Looker 22.20. 
  * A new legacy feature, [**Save as Look keyboard shortcut**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#save_as_look_keyboard_shortcut), allows users to save as Looks by using a [keyboard shortcut](https://docs.cloud.google.com/looker/docs/keyboard-shortcuts#shortcuts_for_exploring). The [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_feature_schedule) will be removed starting in Looker 22.14. 



* * *

### Dashboards updates

The Looker default dashboard experience has been improved.

![](https://docs.cloud.google.com/static/looker/docs/images/dashboards-adv-filters-220.png)

  * A [new save flow](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#creating_a_dashboard_from_a_look_or_an_explore) that is available from the [Explore page](https://docs.cloud.google.com/looker/docs/exploring-data) lets users include filters that are on the first query they save to a dashboard as dashboard filters. 
  * Dashboard creators can now create dashboard filters on fields from Explores that are not present on the dashboard by turning on the [**Advanced** toggle](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#advanced_filters) in the filter creation flow.



* * *

### PDTs at a glance

The new **At a Glance** section on the PDT Admin page lets you quickly view key PDT monitoring information.

![](https://docs.cloud.google.com/static/looker/docs/images/at-a-glance-pdt-220.png)

A new [**At a Glance**](https://docs.cloud.google.com/looker/docs/admin-panel-database-pdts#at_a_glance) section on the PDT **Admin** page provides key PDT monitoring information in a condensed format. 

* * *

### Labs features updates

We've introduced a new [Labs](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs) feature and updated some existing Labs features.

![](https://docs.cloud.google.com/static/looker/docs/images/actionhub-labs-220.png)

An admin user can enable the **Enhanced Action Hub Service** Labs feature to improve reliability and performance of the Looker Action Hub.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
