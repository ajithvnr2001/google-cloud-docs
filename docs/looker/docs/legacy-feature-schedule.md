---
url: https://docs.cloud.google.com/looker/docs/legacy-feature-schedule/
title: Admin settings - Legacy features \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:46.249619+00:00
---

# Admin settings - Legacy features  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/legacy-feature-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Legacy features Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances don't include this page.**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

Looker will occasionally make updates to product design and functionality that render an existing feature's functionality obsolete. In some cases, the feature may be designated as a _legacy_ feature — a feature that remains backward compatible for existing workflows. A legacy feature provides the option for existing users to continue to use the feature's functionality. When a legacy feature is enabled, the Looker instance cannot support the old and new functionality simultaneously.

After you learn about a new legacy feature, you should start planning to migrate to the new functionality before you disable the legacy feature.

See the Legacy feature schedule section on this page for version information about when each legacy feature is introduced, disabled, and removed from Looker.

## Learning about new legacy features

Looker announces new legacy features in the release notes. See the [Looker releases](https://docs.cloud.google.com/looker/docs/looker-releases) page for links to the release notes for the latest Looker release.

The Current legacy features section later on this page provides a timeline showing when current legacy features will be disabled and formally removed from the Looker product. See the Previously removed legacy features table on this page for Information about legacy features that have already been removed from Looker.

## Enabling and disabling legacy features

New features that replace legacy features are often simpler, more reliable, more performant, and/or more useful than the features they replace. To take advantage of the improved functionality of a new feature that replaces a legacy feature, migrate away from the legacy feature. Once that transition is complete, a Looker admin can disable the legacy feature on the [Legacy Features](https://docs.cloud.google.com/looker/docs/legacy-features#enabling_and_disabling_legacy_features) page in the **Admin** panel.

The **Legacy Features** page appears in the **Admin** panel only if there are legacy features available for that Looker instance. The number located next to the **Legacy Features** admin menu item indicates the number of legacy features that are enabled.

When Looker is updated, some legacy features are enabled by default, which means that the old feature is still active. When you're ready to move to the new feature, you can turn the legacy feature off.

> If your Looker instance is created after a legacy feature is disallowed, that feature won't appear on the **Legacy Features** page, and admins won't be able to turn it on. The **Legacy Features** page won't appear in the **Admin** panel if there are no legacy features available to your instance for your current Looker version.
> 
> If you update your existing Looker instance to a version in which a legacy feature is disabled by default, your instance will use the new feature behavior automatically.

## Migrating away from legacy features

Eventually, all legacy features are removed from Looker, so Looker strongly recommends moving away from their use. Start planning your migration as early as possible to avoid disruptions to your workflows.

### Planning your migration

Looker announces new legacy features in the [release notes](https://docs.cloud.google.com/looker/docs/looker-22-release-highlights). When needed, Looker provides transition guidelines for migrating away from legacy features. The Legacy feature schedule on this page provides a timeline that shows when current legacy features have been or will be formally removed from the Looker product. The schedule also notes when the features will be disabled by default.

Leave the legacy feature enabled while you implement any necessary transition guidelines. Once these guidelines have been implemented, disable the legacy feature. Be mindful of migrating away from the legacy feature before updating your Looker instance to the version in which the legacy feature is disabled by default. If you have any issues implementing the improved replacement feature, [open a support request](http://console.cloud.google.com/support/cases).

## Legacy feature schedule

  * **Introduced** indicates the version or date in which the feature becomes a legacy feature and appears in the **Legacy Features** page in the **Admin** panel.
  * **Disabled** indicates the version or date in which the legacy feature is turned off for all instances that update to the release. The legacy feature toggle remains available in the **Legacy Features** page for the purposes of remediation, if required.
  * **Disallowed** indicates the version or date in which the legacy feature is removed from the **Legacy Features** page for newly created Looker instances. If you update your existing Looker instance to this version, the legacy feature toggle remains available.
  * **Removed** indicates the version or date in which the legacy feature is removed from the **Legacy Features** page for all Looker instances.



### Current legacy features

**Use Legacy LookML Runtime**  
---  
**Description** | **Introduced** | **Disabled** | **Disallowed** | **Removed** | **Status** | **Resources**  
When this legacy feature is enabled, all LookML projects will use the legacy LookML runtime by default rather than the new LookML runtime. To enable new LookML runtime for a LookML project while this legacy feature is on, add a [`new_lookml_runtime: yes`](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime) LookML statement to the LookML project's manifest file. | 22.6 | 22.14 | 24.2 | TBD | **Active** |   
**Use Legacy Explore and Merge Query Experience**  
**Description** | **Introduced** | **Disabled** | **Disallowed** | **Removed** | **Status** | **Resources**  
When enabled, Explores and Merge Queries open in the legacy experience for all users. Disable this to open them in the new Looker Explore and Merge Query experience by default. Individual users can still switch back to the legacy experience. | 26.20 | 27.2 | 27.6 | 27.6 | **Active** |   
**Use Legacy Explore and Merge Query Experience for Embed**  
**Description** | **Introduced** | **Disabled** | **Disallowed** | **Removed** | **Status** | **Resources**  
When enabled, embedded Explores and Merge Queries open in the legacy experience. Disable this to open them in the new Looker Explore and Merge Query experience for all embedded users, regardless of individual user preferences. The new experience must also be enabled for the instance. | 26.20 | 27.2 | 27.6 | 27.6 | **Active** |   
**Use Legacy Single Value Visualization**  
**Description** | **Introduced** | **Disabled** | **Disallowed** | **Removed** | **Status** | **Resources**  
When enabled, the legacy Single Value visualization is rendered instead of the new KPI visualization. | 26.20 | 27.2 | 27.6 | 27.6 | **Active** |   
  
### Previously removed legacy features

Legacy Feature | Introduced | Disabled | Removed | Status | Resources  
---|---|---|---|---|---  
Old field chooser | 3.18 |  | 3.38 | **Removed in Looker 3.38** |   
Field labels can override view label | 3.16 | 3.44 | 3.46 | **Removed in Looker 3.46** |   
Leading period in field names | 3.16 | 3.44 | 3.46 | **Removed in Looker 3.46** |   
Uppercase labels in download and chart configurations | 3.16 | 3.44 | 3.46 | **Removed in Looker 3.46** |   
Send email from looker@looker.com | 3.32 | 3.44 | 3.46 | **Removed in Looker 3.46** |   
Default Redshift PDT distribution style EVEN | 3.36 | 3.44 | 3.46 | **Removed in Looker 3.46** |   
$$ substitution | 3.46 | 3.48 | 3.50 | **Removed in Looker 3.50** |   
Joins declared in views | 3.46 | 3.48 | 3.50 | **Removed in Looker 3.52** |   
LookML "scoping" parameter | 3.46 | 3.48 | 3.50 | **Removed in Looker 3.52** |   
Legacy drill behavior | 3.42 | 4.8 | 4.22 | **Removed in Looker 4.22** |   
Add unscoped field name alias | 3.52 | 3.54 | 3.56 | **Removed in Looker 4.6** |   
Unsafe Liquid functions | 3.48 | 4.20 | 5.0 | **Removed in Looker 5.0** |   
Non-symmetric aggregates | 3.16 | 4.20 | 5.0 | **Removed in Looker 5.0** |   
Row limit only | 3.16 | 4.20 | 5.0 | **Removed in Looker 5.0** |   
LookML `decimals` parameter and `int` field type | 3.38 | 5.0 | 5.4 | **Removed in Looker 5.4** |   
Deprecated LookML parameters | 3.16 | 5.0 | 5.4 | **Removed in Looker 5.4** |   
Legacy Oracle security settings | 3.50 | 5.0 | 5.4 | **Removed in Looker 5.4** |   
Single row table headers | 3.52 | 5.0 | 5.4 | **Removed in Looker 5.4** |   
JSON numbers as strings | 3.52 | 4.0 & 5.0 | 5.4 | **Removed in Looker 5.4** |   
Coerce dimensions to measures | 3.54 | 5.0 | 5.4 | **Removed in Looker 5.4** |   
Default query result persistence is five minutes | 4.2 | 5.0 | 5.4 | **Removed in Looker 5.4** |   
YAML-based LookML for modeling  | 4.4 | 4.10 & 5.0 | 5.4 | **Removed in Looker 5.4** |   
Implicit dashboard default timezone  | 4.10 | 5.0 | 5.4 | **Removed in Looker 5.4** |   
Allow unlimited downloads that might crash Looker  | 4.14 | 5.0 | 5.4 | **Removed in Looker 5.4** |   
User-based dev mode  | 4.16 | 4.16 & 5.0 | 5.4 | **Removed in Looker 5.4** |   
Allow creating legacy API-only users | 4.0 | 4.0 & 4.20 | 5.12 | **Removed in Looker 5.12** |   
Allow calling legacy query API  | 5.2 | 5.6 | 5.12 | **Removed in Looker 5.12** |   
Allow the `access_filter_fields` parameter  | 4.14 | 5.22 | 6.0 | **Removed in Looker 3.38** |   
Native derived tables convert dates and yesnos to strings  | 5.22 | 6.0 | 6.6 | **Removed in Looker 6.6** |   
Legacy visualizations  | 6.0 | 6.0 | 6.6 | **Removed in Looker 6.6** |   
Show full field name  | 6.8 | 6.8 | 6.12 | **Removed in Looker 6.12** |   
Legacy rendering  | 6.4 | 6.6 | 6.18 | **Removed in Looker 6.18** |   
Legacy .strings files for localization | 7.2 | 7.8 | 7.12 | **Removed in Looker 7.12** | [Transition guidelines ](https://docs.cloud.google.com/looker/docs/best-practices/how-to-convert-strings-files-to-strings-json-files)  
IDE Folders Toggle | 7.0 | 7.10 | 7.12 | **Removed in Looker 7.12** | [Migrating to IDE folders](https://docs.cloud.google.com/looker/docs/ide-folders#migrating_an_existing_project_to_ide_folders)  
Snowflake Unquoted Database Name | 7.8 | 7.12 | 7.16 | **Removed in Looker 7.16** | [Snowflake connection documentation](https://docs.cloud.google.com/looker/docs/db-config-snowflake#adding_the_connection)  
Treat the Datatype Datetime as a Timestamp | 7.14 | 7.20 | 21.4 | **Removed in Looker 21.4** | [`datatype` parameter documentation](https://docs.cloud.google.com/looker/docs/reference/param-field-datatype)  
Unsafe Custom Visualizations | 7.20 | 21.6 | 21.6 | **Removed in Looker 21.6** | [Admin Settings – Visualizations documentation](https://docs.cloud.google.com/looker/docs/admin-panel-platform-visualizations)  
Revert to Legacy Explore Field Picker | 21.12 | 21.12 | 21.16 | **Removed in Looker 21.16** | [Legacy field picker documentation](https://docs.cloud.google.com/looker/docs/legacy-field-picker)  
Legacy Branding | 7.18 | 7.20 | 21.18 | **Removed in Looker 21.18** |   
Syntax Tolerant Liquid | 21.6 | 21.14 | 22.2 | **Removed in Looker 22.2** |   
Use old navigation and legacy routing | 21.20 | 22.0 | 22.2 | **Removed in Looker 22.2** | [New navigation documentation](https://docs.cloud.google.com/looker/docs/finding-content)  
Require authentication to retrieve API specifications | 21.14 | 21.18 | 22.4 | **Removed in Looker 22.4** |   
Save to shared space with `external_group_id` | 21.4 | 21.16 | 22.4 | **Removed in Looker 22.4** |   
Legacy Value Formatting | 21.4 | 21.4 | 22.6 | **Removed in Looker 22.6** |   
Legacy Query Streaming | 21.8 | 21.8 | 22.8 | **Removed in Looker 22.8** |   
Add Looks to dashboards | 21.12 | 21.10 | 22.12 | **Removed in Looker 22.12** | [Adding saved content to dashboards](https://docs.cloud.google.com/looker/docs/adding-saved-content-to-dashboards-legacy-feature)  
Save as look keyboard shortcut | 22.0 | 22.0 | 22.14 | **Removed in Looker 22.14** |   
Allow double-click to select text in textarea in table visualizations | 22.0 | 22.14 | 22.14 | **Removed in Looker 22.14** |   
Popular fields in Explore search | 22.0 | 22.0 | 22.20 | **Removed in Looker 22.20** |   
Allow XHTML-style Empty Tags in Custom Visualizations | 21.20 | 22.20 | 22.20 | **Removed in Looker 22.20** | [Allowing XHTML-style empty tags in custom visualizations](https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-allow-xhtml-style-empty-tags-in-custom-visualizations-legacy-feature)  
Use old dashboard routes | 21.18 | 21.20 | 22.20 | **Removed in Looker 22.20** |   
Revert to Legacy Dashboards | 7.18 | 21.0 | 22.20 | **Removed in Looker 22.20** |   
Legacy Render Card Height | 22.0 | 22.10 | 23.0 | **Removed in Looker 23.0** |   
Can use Legacy Dashboards | 22.20 | 23.2 | 23.6 | **Removed in Looker 23.6** | [Transition guidelines](https://docs.cloud.google.com/looker/docs/best-practices/legacy-dashboard-deprecations)  
Use Legacy Hosted Action Hub | 22.6 | 22.6 | 22.20 | **Removed in Looker 23.12** |   
Use Legacy Internal Query API | 23.0 | 23.2 | 23.8 | **Removed in Looker 23.12** |   
Deny API 3.x Requests | 23.10 | 23.14 | 23.14 | **Removed in Looker 23.14** |   
Use Legacy Homepage Sidebar | 23.8 | 23.12 | 23.16 | **Removed in Looker 23.16** |   
Allow API 3.x requests | 23.14 | 23.14 | 23.18 | **Removed in Looker 23.18** |   
Always hide Row Totals series from stacked charts | 23.0 | 23.0 | 23.20 | **Removed in Looker 23.20** |   
Disallow Numeric Query IDs | 24.2 | 24.10 | 24.10 | **Removed in Looker 24.10** |   
Allow Legacy Maps | 23.10 | 24.8 | 24.18 | **Removed in Looker 24.18** |   
Use Legacy Project Creation Page | 24.20 | 26.4 | 26.18 | **Removed in Looker 26.18** | [Creating a new LookML project](https://docs.cloud.google.com/looker/docs/create-projects)  
Use Legacy Connections Page | 25.4 | 25.8 | 26.20 | **Removed in Looker 26.20** | [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
