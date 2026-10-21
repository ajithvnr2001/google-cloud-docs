---
url: https://docs.cloud.google.com/looker/docs/looker-23-release-highlights/
title: Looker 23 release highlights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:10.945929+00:00
---

# Looker 23 release highlights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-23-release-highlights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  Looker 23 release highlights Stay organized with collections  Save and categorize content based on your preferences. 

Starting in Looker 23.6, Looker Release notes have been integrated into the [Google Cloud release notes](https://cloud.google.com/release-notes) system. 

To get the latest Looker product updates, check the [Looker Release notes](https://docs.cloud.google.com/looker/docs/release-notes) or subscribe to the following RSS feed: `https://cloud.google.com/feeds/looker-release-notes.xml`

## **Looker 23.10**

_play_circle_filled_ Expected rollout start: **Tuesday, June 20, 2023** _check_circle_ Expected final deployment and download available: **Wednesday, June 28, 2023** _play_circle_filled_ Expected Looker (Google Cloud core) deployment start: **Friday, June 30, 2023** _check_circle_ Expected Looker (Google Cloud core) deployment end: **Friday, July 14, 2023**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * Starting in Looker 23.10, Liquid `value` and `rendered_value` now return YYYY-MM-DD style dates for date references.
  * Starting in Looker 23.10, YAML LookML projects, except for LookML dashboards, will now return an error, and all content that is based on YAML LookML projects will break.
  * Starting in Looker 23.10, the LookML generator will always generate LookML for new projects, derived tables, and aggregate tables.
  * Starting in Looker 23.10, when you are exporting data to, for example, a CSV file, a date field backed by a string column in the backend database will now serialize the same as a date field backed by a date column: YYYY-MM-DD.
  * Starting in Looker 23.10, SSO embed functionality, including SSO embed APIs and other SSO embed-specific features, is disabled on the Standard and Enterprise editions of Looker (Google Cloud core) instances.

  * Until API 3.0 and 3.1 are disabled in Looker 23.12, the new Deny API 3.x requests [Legacy feature toggle](https://cloud.google.com/looker/docs/legacy-feature-schedule) can be used to configure a Looker instance to reject API 3.x requests and log those requests to the Looker system log. This will cause API 3.x requests on that instance to fail, allowing administrators to verify that no remaining calls are made to API 3.0 and 3.1.




### Looker-Power BI Connector is GA

Explore data from your LookML models through the Power BI Desktop interface 

This new API-based connector enables users to build fresh, trusted reporting in Power BI Desktop using metrics and data relationships defined centrally in LookML. This new capability is available on all Looker-hosted instances.

Looker admins must enable the feature on the [BI Connectors admin page](https://cloud.google.com/looker/docs/bi-connectors).

Learn more and download the connector file at <https://cloud.google.com/looker/docs/powerbi-connector>.

### LookML Projects

Data tests to pass before deploying LookML projects to production 

Starting in 23.10, all new LookML projects will be enabled for the [**require data tests to pass before deploying this project to production**](https://cloud.google.com/looker/docs/git-options#require-data-tests) project setting (existing LookML projects will keep their current setting for this option). See the [`test`](https://cloud.google.com/looker/docs/reference/param-model-test) documentation for information on adding data tests to your LookML project.

### Get embed URL

The new Get embed URL feature lets you automatically generate a [private embedding URL](https://cloud.google.com/looker/docs/private-embedding) for a dashboard, a Look, or an Explore. The embed URL can optionally include parameters, such as filter values, and apply an existing [theme](https://cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores).

### Embed Your Data Welcome guide

The new Embed Your Data Welcome Guide steps first-time embedding users through creating a [private embed URL](https://cloud.google.com/looker/docs/private-embedding) for a dashboard, applying a [theme](https://cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) to an embedded dashboard, and links to a new codelab that demonstrates how to create an [SSO embed URL](https://cloud.google.com/looker/docs/single-sign-on-embedding) using one of Looker's publicly available scripts.

## **Looker 23.8**

_play_circle_filled_ Expected rollout start: **Monday, May 15th, 2023** _check_circle_ Expected final deployment and download available: **Tuesday, May 30th, 2023**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * Starting in Looker 23.8, sorting for [custom bin fields](https://cloud.google.com/looker/docs/custom-fields#custom_binning) on the New LookML Runtime sorts by tier number as expected.

  * Starting in Looker 23.8, the Looker IDE will now display an error when incompatible types are compared in Liquid statements.

  * Starting in Looker 23.8, the feature where a row's value could be mapped to different tiers for a custom bin field and the internal sort field generated for it works as expected.

  * Starting in Looker 23.8, the **New Explore Visualizations** Labs feature is now generally available. The Explore page, Looks, embedded Looks or Explores, and dashboard tile edit windows will display the same style of funnel chart, timeline, single value, and table visualizations as those that appear on dashboard tiles. Additionally, the drill overlay that appears when you drill into an Explore will match the style of the drill overlay that appears in dashboards, instead of the style that appears in Looks. 

* * *




### Access to set_smtp_settings API endpoint

Customers who do not have the `oem_jar` license feature enabled can now access the [`set_smtp_settings` API endpoint](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Config/set_smtp_settings).

### Cookieless embed API endpoints

[Cookieless embed API endpoints](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Auth/acquire_embed_cookieless_session) are now marked as stable.

## **Looker 23.6**

_play_circle_filled_ Expected rollout start: **Monday, April 17th, 2023** _check_circle_ Expected final deployment and download available: **Thursday, April 27th, 2023**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * Starting in Looker 23.6, the **Can Access Legacy Dashboards** legacy flag has been removed because legacy dashboards are fully deprecated and removed in this release. Now all legacy dashboards are shown in the new dashboard viewer.

  * Starting in Looker 23.6, you can no longer upgrade dashboards from the Folders page because legacy dashboards have been deprecated.

  * Starting in Looker 23.6, the Liquid [`parameter`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#parameter) tag and [`_parameter_value`](https://docs.cloud.google.com/looker/docs/liquid-variable-reference#parameter_value) variables now return a date string rather than date SQL in non-SQL contexts (for example, the [`html`](https://docs.cloud.google.com/looker/docs/reference/param-field-html) and [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link) LookML parameters) for date parameters.

  * Starting in Looker 23.6, customer-hosted Looker instances require Git 2.39.1 or later on the host image (see the [Installing the Looker application](https://cloud.google.com/looker/docs/installing-looker-application) documentation page for the full list of requirements for customer-hosted Looker instances). Git 2.39.1 supports [Git worktrees](https://git-scm.com/docs/git-worktree) instead of complete Git history clones. Looker uses Git worktrees to provide faster entry into Developer Mode, among other benefits.




* * *

### Improved performance in add filter

The performance of the `add filter to dashboard` modal has been improved. A calculation that took ~4s in earlier Looker versions now takes ~4ms (1,000 times faster).

### Incremental PDTs for Databricks

Looker supports Incremental PDTs for Databricks 

Looker now supports [Incremental PDTs](https://docs.cloud.google.com/looker/docs/incremental-pdts) for Databricks connections when using Databricks version 12.1 or later.

### Popup dialogs in an embedded environment

Customers can now set the position of popup dialogs in an embedded environment

Customers must make changes to their embedded applications to take advantage of this feature. Convenient methods have been added to the Embed SDK, and an updated Embed SDK has been published. The Embed SDK repository has also been updated to provide examples of using this feature with the Embed Javascript (windows postMessage) API.

## **Looker 23.4**

_play_circle_filled_ Expected rollout start: **Monday, March 13th, 2023** _check_circle_ Expected final deployment and download available: **Thursday, March 23rd, 2023**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * Starting in Looker 23.4, the Denodo dialect is now deprecated. Customer-hosted instances are expected to update to [Denodo 8](https://docs.cloud.google.com/looker/docs/db-config-denodo).

  * Starting in Looker 23.4, YAML LookML projects will return a warning upon project validation. All instances of YAML LookML must be translated to New LookML.

  * Starting in Looker 23.4, the **New Users Page** and **New Groups Page** Labs features are now generally available, and admins no longer need to turn the feature flags on. These features add a host of performance improvements to the **Users** and **Groups** pages, which includes improved pagination on the **Groups** page.




* * *

### Looker Studio Connector and Connected Sheets now available for all Looker-hosted instances

These features were previously available only for instances that were Looker-hosted on Google Cloud

We previously announced the availability for Google Cloud-hosted Looker instances of the Looker Studio connector [in Looker 23.0](https://docs.cloud.google.com/looker/docs/looker-23-release-highlights#looker_studio_connector_is_ga) and Connected Sheets in [Looker 22.20](https://docs.cloud.google.com/looker/docs/looker-22-release-highlights#connected_sheets). We are excited to announce that both connectors are now available for all Looker-hosted instances, including Looker-hosted on AWS and Azure. Looker users can access and analyze Looker modeled data in Connected Sheets and Looker Studio through the connectors, opening up new enterprise use cases.

Before users can get started with these features, a Looker admin must enable them in the new [BI Connectors Admin page](https://docs.cloud.google.com/looker/docs/bi-connectors).

To learn more, see the Looker documentation for the [Looker Studio connector](https://docs.cloud.google.com/looker/docs/looker-studio-connector) and for [Connected Sheets](https://docs.cloud.google.com/looker/docs/connected-sheets).

### New Performant Field Picker Labs feature

Search more quickly and efficiently in large Explore field pickers

The [**Performant Field Picker**](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#performant_field_picker) Labs feature offers more refined [search](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#search_bar) options, which let users more quickly and efficiently search for fields in large [Explore field pickers](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#field_picker). 

* * *

## **Looker 23.2**

_play_circle_filled_ Expected rollout start: **Monday, February 13th, 2023** _check_circle_ Expected final deployment and download available: **Thursday, February 23rd, 2023**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * The [**Use Legacy Internal Query API legacy feature**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_feature_schedule) is now disabled by default.
  * Users will no longer be able to view legacy dashboards unless a Looker admin turns on the **Can Use Legacy Dashboards** legacy flag on the instance. This is in preparation for the complete deprecation of legacy dashboards in Looker 23.6. See the [Removing the legacy dashboard experience - a timeline from Looker 21.20 (November 2021) through Looker 23.6 (April 2023)](https://docs.cloud.google.com/looker/docs/best-practices/legacy-dashboard-deprecations) Best Practices page for more information.



* * *

## **Looker 23.0**

_play_circle_filled_ Expected rollout start: **Monday, January 16th, 2023** _check_circle_ Expected final deployment and download available: **Tuesday, January 31st, 2023**

### Potentially breaking changes

Check out these potentially breaking changes! Depending on which features or configurations you have implemented, all, some, or none of these changes may apply to your instance. 

  * The **Legacy Render Card Height** [legacy feature](https://cloud.google.com/looker/docs/legacy-feature-schedule) is now removed.
  * The [**Use Legacy Internal Query API legacy feature**](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule#legacy_feature_schedule) configures [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), [Looks](https://docs.cloud.google.com/looker/docs/viewing-looks), and [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics) to use the legacy API for running queries when enabled. When disabled, Explores, Looks, and SQL Runner use the upgraded internal API for running queries. Upgrading the internal query API does not affect applications using the externally available Looker API. This legacy feature is enabled by default for Looker 23.0 and will be disabled by default starting in Looker 23.2.
  * When the pool_timeout to edit a database connection in an api request is less than the minimum allowed, a `pool_timeout ` error is now thrown.



* * *

### Expanded Dashboard Theming

New Labs option for embedded dashboard theming

This feature is now enabled by default, and it lets admin users [display and hide dashboard header elements on embedded dashboards](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores#dashboard_controls).

![](https://docs.cloud.google.com/static/looker/docs/images/expanded_theme_options.png)

* * *

### BI Engine Optimizations

This feature is now out of Labs and is generally available

The **BI Engine Optimizations** feature is enabled for all BigQuery customers who use the BI Engine. With BI Engine optimizations, Looker will generate experimental SQL patterns for certain types of LookML queries that use a BigQuery database connection. These SQL changes are designed specifically to execute faster on Google BigQuery's BI Engine. This feature affects the query runtime and has no effect on query results.

### Looker Studio Connector is GA

This feature is now out of Labs and is generally available

The [**Looker Studio** connector](https://docs.cloud.google.com/looker/docs/looker-studio-connector) lets you access data from a Looker Explore within Looker Studio by adding the Explore as a [data source](https://support.google.com/looker-studio/answer/6268208) in a Looker Studio report. Enable the **Looker Studio** BI connector on the **BI Connectors** page in the **Platform** section of the **Admin** menu.

![](https://docs.cloud.google.com/static/looker/docs/images/bi-connectors-2300.png)

You can also [monitor information](https://docs.cloud.google.com/looker/docs/looker-studio-connector#looker_studio_system_activity) about the queries that are run by your Looker Studio data sources in the System Activity **History** Explore.

See the [Connect to Looker](https://support.google.com/looker-studio/answer/12388266) article in the Looker Studio help center for more information about how to enable the Looker connector in Looker Studio.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
