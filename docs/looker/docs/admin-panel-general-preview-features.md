---
url: https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features/
title: Admin settings - Preview Features \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:37:23.180290+00:00
---

# Admin settings - Preview Features  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Preview Features Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

The **Preview Features** page in the **General** section of the **Admin** panel lets you enable and disable features that are in preview.

## Preview features overview

Preview features are new, in-progress features whose details can change over time.

You can choose to use these features or leave them disabled. The **Preview Features** page lists each feature with a short description underneath it explaining the functionality that it adds to or changes in Looker.

Preview features are split into two categories:

  * **Preview features** : Preview features have a planned path to general availability, and we expect to resolve feature issues. However, these features may change in detail, and errors may not be fixed with the same speed as with general availability features. You can see the list of current preview features in the Current preview features section on this page.
  * **Labs features** : Labs features may be removed from the product at any time, without extended notice. Feature issues may or may not be resolved. These experimental features are intended to show you functionality that could be incorporated into Looker in the future and to get your feedback. Labs features are available only in Looker (original). You can see the list of current experimental Labs features in the Labs features (Looker (original) only) section on this page.

**Note:** These features are Preview offerings, subject to the "Pre-GA Offerings Terms" of the [Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). For these features, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-terms), subject to applicable restrictions and obligations in the Agreement (as defined in the Pre-GA Offerings Terms).

## Enabling and disabling preview features

To enable or disable a feature, click the switch next to the feature name.

**Caution:** Use caution when disabling a preview feature. If users or developers have relied on the feature to create a certain behavior, disabling the feature breaks that functionality.

## Current preview features

Looker supports the following preview features.

### Data Apps

This feature is disabled by default.

[Looker Data Apps](https://docs.cloud.google.com/looker/docs/data-apps) are freeform canvas dashboards that are built by local AI coding agents, such as Gemini CLI, Claude Code, or Cursor, from natural-language prompts. Data Apps give you complete visual layout control (including absolute positioning, overlapping elements, and custom web components) while remaining bound to Looker's governed LookML semantic layer and user permissions.

### End User Conversational Analytics (CA) Query Review

This feature is disabled by default.

This feature allows admins to review users' Conversational Analytics queries in a System Activity dashboard. This feature is not for use to score, monitor, or judge worker output or employment status. Instead this usage data can be used to improve system performance, such as supporting troubleshooting and agent building. When time-limited on-demand support is initiated, Conversational Analytics queries are also visible to Google support.

In order for a Looker admin to see a specific user's query data, that user must have [consented to revealing their query data](https://docs.cloud.google.com/looker/docs/user-account#conversational-analytics).

### Filters as Tiles and Tile-Level Filter Context

This preview feature is disabled by default.

When this preview feature is enabled, dashboard editors can [place dashboard filters anywhere on the canvas alongside visualization tiles](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#filters_as_tiles). This also adds filter context to individual visualization tiles, showing viewers exactly which dashboard filters are being applied to that tile.

### Filters on Visualization Tiles

This preview feature is disabled by default.

When this feature is enabled, filters can be placed directly on visualization tiles in dashboards.

For more information, see the [Filters on visualization tiles](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#filters-on-visualization-tiles) documentation.

### Google Maps Enhancements

Enables new Google Maps visualization features, including the following:

  * [Intensity](https://docs.cloud.google.com/looker/docs/google-map-options#intensity) and [threshold](https://docs.cloud.google.com/looker/docs/google-map-options#threshold) options for [Density Heatmap charts](https://docs.cloud.google.com/looker/docs/google-map-options#density_heatmap).
  * A [3D Heatmap](https://docs.cloud.google.com/looker/docs/google-map-options#3d_heatmap) chart option.
  * A [Dual-axis Map](https://docs.cloud.google.com/looker/docs/google-map-options#dual-axis_map) option, which lets you overlay a second measure as a grayscale layer on top of the primary color-coded map regions.
  * Access to several additional [map layers](https://docs.cloud.google.com/looker/docs/google-map-options#layers_menu_options) in the visualization settings:

    * **Transit Layer** : Overlays transit lines and stations.
    * **Bicycling Layer** : Highlights bicycle paths and bike-friendly streets.
    * **Traffic Layer** : Displays real-time traffic conditions.



### Increase SQL Runner Schema and Table Limit

This preview feature is enabled by default.

When this preview feature is enabled, the total number of schemas that can be returned to [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics) increases to 12,000.

**Warning:** Enabling this preview feature will increase the table name display response time if your instance has access to a large number of schemas and tables.

### KPI Visualization

This preview feature is enabled by default.

When enabled, the **KPI Visualization** preview feature replaces the **Single Value** chart option with the **KPI (Single Value)** chart option. The new **KPI (Single Value)** chart option lets users access the following enhanced styling options for single value visualizations:

  * Adding secondary visualizations: Users can add a sparkline or bar chart within a visualization to show trends or distributions that are related to the primary KPI.
  * Showing enhanced comparisons: Users can specify and compare a primary value against any other measure in an Explore query, using data from the first row, second row, last row, or totals row.
  * Accessing improved styling options: Users have more control over the appearance of the visualization, including background color of the tile, and the alignment of the values.



Learn more about the new [KPI (Single Value) Visualization](https://docs.cloud.google.com/looker/docs/kpi-single-value-options).

### Knowledge Catalog Lineage

This preview feature is disabled by default.

Share Looker (Google Cloud core) metadata with Knowledge Catalog to power data lineage. To use lineage, ensure that the following are also enabled:

  * the [Knowledge Catalog integration for Looker](https://docs.cloud.google.com/looker/docs/looker-core-dataplex#enable)
  * the Data Lineage API
  * the [service-level lineage integration](https://docs.cloud.google.com/dataplex/docs/use-lineage#control-ingestion) in your Knowledge Catalog settings.



This feature is available only for Looker (Google Cloud core) instances.

### Modern User Interface

This preview feature is enabled by default.

The **Modern User Interface** feature enables a modernized navigation and page layout, and exposes configuration settings to apply modernized visual themes and enhanced design defaults to dashboards and visualizations.

For more information, see the [Using the modern user interface](https://docs.cloud.google.com/looker/docs/modern-ui) documentation page.

### New/Edit Roles Enhancement

This preview feature is disabled by default on Looker (Google Cloud core) and enabled by default on Looker (Original).

When enabled, the **New/Edit Roles Enhancement** preview feature provides a modernized, step-by-step interface for creating and editing roles on the [**Roles**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#creating-editing-roles-enhancement) page in the **Users** section of the **Admin** panel.

### New Looker Explore and Merge Query Experience

This preview feature is enabled by default.

When enabled, the **New Looker Explore and Merge Query Experience** feature lets individual users have the option to try the redesigned Looker Explore and Merge Query interfaces. The streamlined interfaces let Looker users find connections and gain insights from their data more quickly. For an AI-assisted experience, enable additional options on the [**Gemini in Looker**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) page in the **Platform** section of the **Admin** panel.

[Learn more about the new Explore and Merge Query experience](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview).

### Table Row Grouping

This preview feature is enabled by default.

When this feature is enabled, you can display table chart data hierarchically in groups and customize the appearance with new [**Grouping** menu options](https://docs.cloud.google.com/looker/docs/table-options#grouping-menu-options).

**Note:** **Table Row Grouping** is not supported for [table (legacy) charts](https://docs.cloud.google.com/looker/docs/legacy-table-options).

## Labs features (Looker (original) only)

The following features are available only on **Looker (original)** instances. These features aren't fully developed and may be significantly changed or completely removed in future releases. Don't use them for production workloads.

### Access Studio in Looker

**Important:** Starting on December 4, 2025, new instances or instances that have not already enabled Looker reports cannot enable Looker reports.

This Labs feature enables the [Looker reports feature](https://docs.cloud.google.com/looker/docs/enabling-studio-in-looker), which lets you [create, view, and edit Data Studio reports](https://docs.cloud.google.com/looker/docs/studio-in-looker) in your Looker instance, including both governed and ad hoc data. You can [share and manage your reports](https://docs.cloud.google.com/looker/docs/move-share-copy-reports) in Looker folders and see your recent reports and the reports that you have marked as favorites from the Looker Home page.

### BI Engine Symmetric Aggregates

This Labs feature is disabled by default.

When the **BI Engine Symmetric Aggregates** feature is enabled, for queries that use [symmetric aggregates](https://docs.cloud.google.com/looker/docs/best-practices/understanding-symmetric-aggregates), Looker generates experimental SQL patterns that execute faster on the BigQuery BI Engine. This feature has no effect on query results, only on execution performance.

### Guided analyses in System Activity

This Labs feature is disabled by default.

When enabled, the [**History**](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#history) System Activity Explore displays [guided analysis](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#guided_analyses_in_system_activity_labs_feature) options to provide a question-and-answer format for performing analyses.

### In-database merge queries

This Labs feature is disabled by default.

This feature improves performance and allows for unlimited rows of data being joined for [merged queries](https://docs.cloud.google.com/looker/docs/merged-results) when both queries being merged use the same BigQuery connection. By default, merged queries are processed in Looker memory, and therefore each query is limited to 5,000 rows that can be joined. When the **In-database merge queries** feature is enabled and both queries are from the same BigQuery connection, the join of the queries is run in the BigQuery database itself. See the [Merging results from different Explores](https://docs.cloud.google.com/looker/docs/merged-results#in-database-merge-queries) documentation page for more information.

### New Explore & Look Saving

This Labs feature is enabled by default.

This feature improves the visibility and navigation of **Save** dialogs on the Explore and Look pages. The new experience allows quick navigation of folders, and users can choose to sort existing content by Name, Created Date, or Last Update. It does not change any functionality of these pages.

### Redux DevTools

This Labs feature is disabled by default.

This feature enables Redux DevTools for debugging application state.

### Rigorous Dashboard Download Permission Checking

This Labs feature is disabled by default.

When this feature is enabled, users can download a dashboard only if they have the [`download_with_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit) or [`download_without_limit`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit) permission on every model that the dashboard includes.

### SQL Runner Vis

This Labs feature is disabled by default.

This feature adds the ability to visualize ad hoc queries from SQL Runner.

This feature is not supported for [Looker (Google Cloud core) instances](https://docs.cloud.google.com/looker/docs/looker-core-overview).

### Tiered Support Access

This Labs feature is enabled by default.

Enabling the **Tiered Support Access** feature enables enhanced support access, including updated access duration times and access levels. For more information, see the [Admin settings - Support Access](https://docs.cloud.google.com/looker/docs/admin-panel-general-support-access) documentation page. Disabling this feature enables [legacy support access](https://docs.cloud.google.com/looker/docs/admin-panel-general-support-access#legacy_support_access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
