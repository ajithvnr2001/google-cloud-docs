---
url: https://docs.cloud.google.com/looker/docs/looker-5-release-notes/
title: 5.x Release Notes \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:15:20.348192+00:00
---

# 5.x Release Notes  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-5-release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  5.x Release Notes Stay organized with collections  Save and categorize content based on your preferences. 

## Preparing for Releases

We occasionally retire features. You can plan for this with the [Legacy Features End-of-life Schedule](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067).

In the release notes, you may see some special symbols:

  * Items marked with a _flash_on_ indicate changes to existing functionality that may require your attention as you update, such as features being retired.

  * Items marked with a _science_ indicate a [Looker Labs](https://docs.cloud.google.com/looker/docs/admin-panel-general-labs#labs_overview) feature that must be enabled by an admin on the Labs page.

  * Items marked with a _build_ indicate changes to system configurations that may impact your ability to run the new release.




## Looker 5.24 2018-09-23

### LookML and Development

  * _science_ **New API endpoints for Git management.** The experimental API 3.1 now contains the following endpoints: `all_git_branches`, `git_branch`, `create_git`, `update_git`, `find_git_branch`, `delete_git_branch`.



### Scheduling and Downloading

  * **Download Merged Results as CSVs.** It is now possible to download dashboards containing merged results queries as CSVs.



### Dialects

  * **BigQuery Standard SQL.** Added support for `DATETIME` and `NUMERIC` data types.
  * **Amazon Athena.** Updated the driver to version 2.0.5.



### General Tweaks & Bug Fixes

#### Security

  * Fixed a security issue where users could potentially change ownership of other users' dashboards. #### Dashboards, Visualizations, and Explore
  * _flash_on_ Series layering order is now determined automatically, rather than going right to left when the Enhanced Visualizations Labs feature is enabled and multiple series types are selected.
  * Fixed a bug where long-running queries prevented dashboards from loading.
  * Fixed a bug where using custom fields on Merged Results queries hid the **Explore From Here** button.
  * Fixed a bug where some dashboard tiles showed the following error: `Unexpected token � in JSON at position 14`.
  * _science_ Continued improvements to beta Enhanced Visualizations and Enhanced Renderer Labs features. #### Content Management and Discoverability
  * Fixed a bug where embed users could not navigate backward when saving a Look.
  * Fixed a bug where restoring a dashboard from the trash did not also restore Looks. #### Platform and Administration
  * Fixed a bug causing some general instance performance issues for Powered by Looker instances. #### Scheduling and Downloading
  * Fixed a bug where dashboards were rendered wrong in emails due to Gmail UI redesign.
  * Fixed a bug where user-specific time zones were not applied to exported query results. #### LookML and Development
  * Stopped generating superfluous joins for empty filters.
  * _science_ Continued improvements to the experimental Custom Fields Labs feature. #### Action Hub
  * _flash_on_ Made some small UI changes to the **Admin** menu for the Looker Action Hub.



## Looker 5.22 2018-08-26

### Dashboards and Visualizations

  * **Merged Results Improvements** : 
    * _science_ Experimental Custom Fields can now be used in Merged Results.
    * Merged Results are now available in embedded dashboards.
  * _science_ **Beta Enhanced Renderer**. Introduced Enhanced Rendering designed to be used in conjunction with the beta Enhanced Visualizations feature. [Learn more about customer-hosted setup.](https://docs.cloud.google.com/looker/docs/installation-of-rendering-software#enhanced-rendering)



### LookML and Development

  * **Code quality options.** Added a third level of code quality requirements. Looker admins can now allow developers to commit LookML code with warnings, but not with unfixed errors, in the LookML validator. [Learn more.](https://docs.cloud.google.com/looker/docs/git-options#project_settings)
  * **Git setup performance enhancements.** Back-end enhancements to the Git setup process make Git integration faster and more performant.
  * _flash_on_ **Disabled Legacy feature:** The **Allow the`access_filter_fields` parameter** Legacy feature has been disabled, but will remain available until Looker 6.0 if needed. Please use user-attribute-based access filters for controls going forward. [Learn more.](https://discourse.looker.com/t/deprecation-notice-access-filter-fields-replaced-by-access-filters-4-16/5296)
  * _flash_on_ **Introduced a new Legacy feature:** Native derived tables convert dates and `yesno` values to strings by default. [Learn more.](https://discourse.looker.com/t/improved-behavior-for-native-derived-tables-in-looker-5-22/8680)



### Dialects

  * **Athena.** Updated to Athena driver 2.0.5 and introduced support for arrays in Athena.



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * _science_ Continued improvements to the Enhanced Visualizations Labs feature.
  * Fixed a bug where pivots occasionally caused blank visualizations on the Explore.
  * Fixed a bug where some Looks were unable to load more than 10,000 rows. #### Scheduling and Downloading
  * Fixed a bug where schedules occasionally failed due to node communication errors.
  * Fixed a bug where filters on fields that had been removed caused the scheduler UI to break.
  * Fixed a bug where some schedules to S3 buckets were failing. #### Platform and Administration
  * _flash_on_ Fixed a bug where string type user attributes did not properly escape `-`. #### LookML and Development
  * Addressed an issue where switching between files in the IDE was sluggish.
  * Fixed a bug where some `distance` dimensions incorrectly calculated a distance of `0.00`.
  * Unnecessary `include` statements are now generated commented in view files.
  * _science_ Fixed a bug where the Content Validator sometimes reloads with boxes checked.
  * _science_ Continued improvements to experimental Custom Fields.
  * _flash_on_ Fixed a bug where custom dimensions could be used to query filter-only fields. Looks and dashboards with these fields may cause an error message.
  * Fixed a bug where `always_join` was not used in suggestions query. #### Content Management and Discoverability
  * Fixed a bug where the Spaces sidebar was not scrolling properly.
  * Fixed a bug where restoring a dashboard from the Trash did not restore associated Looks.
  * Added breadcrumbs to the Spaces page. #### Dialects
  * Fixed a bug where `number` type dimensions did not recognize the decimal data type in Athena.
  * The LookML generator now double quotes column references in IBM Db2. #### Security
  * Removed stack trace exposure in the event of low-level errors.



## Looker 5.20 2018-07-29

### General Tweaks and Bug Fixes

#### Action Hub

  * Added clearer error messaging in the Action Hub section of the scheduler modal.



#### LookML and Development

  * Added the ability to revert uncommitted changes in the event of a merge conflict.
  * Improved performance when switching between LookML files in the IDE.
  * Fixed a bug where null values in the milliseconds timeframe produced errors.
  * Fixed a bug where the LookML validator showed errors and warnings from previous run.
  * Fixed a bug where direct links to SQL Runner queries occasionally did not load SQL.
  * Fixed a bug where using `suggest_dimension` without `suggest_explore` caused an error.



#### Platform and Administration

  * Added the option to require authentication on the project deploy webhook. [Learn more.](https://docs.cloud.google.com/looker/docs/webhook-deploy-secret)
  * Added the `see_system_activity` permission to allow non-admin users to access the Usage Panel. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage)
  * Added the ability to specify a domain whitelist on hidden user attribute fields.
  * Improved error messaging when hitting git authentication issues.



#### Dialects

  * Added support for querying array type fields in Athena.
  * Added PDT support for MemSQL and IBM Netezza.
  * Enhanced the LookML generator for Dremio to wrap table and schema referenced in double quotes.



#### Dashboards and Visualizations

  * _science_ Continued improvements to experimental Enhanced Visualizations.
  * Improved performance for moving tiles on dashboards.
  * _science_ Continued improvements to experimental Custom Visualizations. 
    * Added asynchronous loading to visualizations for improved performance.
    * Fixed a bug where color palettes were not exported as hex values.
    * Fixed a bug where some visualizations did not render correctly in an iframe.
  * Fixed a bug where the reference line label text box in the visualization settings menu only accepted a single character.
  * Fixed a bug where toggling the visualization configuration menu in the UI created whitespace in the visualization.



#### Scheduling and Downloading

  * Fixed a bug where embed users needed the `save_content` permissions in order to create a schedule.
  * Fixed a bug where email schedules rendered incorrectly in Outlook 2013.



#### Content Management and Discoverability

  * Made the grid or table selection in user spaces persistent across sessions.
  * Fixed a bug where merged results did not work correctly in homepage thumbnails.




## Looker 5.18 2018-06-28

### Platform and Administration

  * **New`Passwords` page in Admin Panel.** New Admin menu allows for additional control over password requirements for Looker users. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-authentiation-password).
  * _flash_on_ **New default password requirements.** New and reset passwords will be subject to the following requirements: minimum length 7 characters, at least one uppercase and one lowercase letter, one numeric character, and one special character.
  * **Looker now adds contextual information as a SQL comment to every query.**
  * **Looker now uses Java to manage certificate verification** rather than maintaining its own distinct CA bundle. [Learn more](https://docs.cloud.google.com/looker/docs/ssl-certificate-for-proper-https#validating_a_sites_certificate_against_the_ca_bundle). ### Dashboards and Visualizations
  * _science_ **Improvements to Merged Results.**
    * Merged Results no longer requires a special user group or Labs setting.
    * Dashboard-level filters can now be applied to Merged Results tiles.
    * It is now possible to validate Merged Results in the Content Validator.
  * _science_ **Enhanced Visualizations in Labs.** The Labs toggle enables a new visualization architecture. Cartesian charts may look a little cleaner with this beta Labs feature enabled.
  * _flash_on_ **Beta API changes.**
    * The `dashboard` route has been updated to allow for filtering on Merged Results tiles. The `dashboard_elements` object now has a `listen` array rather than key-value pairs. [Learn more.](https://discourse.looker.com/t/beta-api-changes-to-filter-listeners-in-dashboards-in-looker-5-18/8213) ### LookML and Development
  * **Git HTTPS configuration.** Git connections can now be configured over HTTPS with a username and password. [Learn more.](https://docs.cloud.google.com/looker/docs/setting-up-git-connection#git_https)
  * **New PDT DDL customization.** Developers can now customize PDT DDL statements with LookML parameters `create_process` and `sql_create`. [Learn more about `create_process`.](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) [Learn more about `sql_create`.](https://docs.cloud.google.com/looker/docs/reference/param-view-sql-create)
  * _science_ **Project Import public remote repositories.** Looker Blocks and other public projects can now be imported and kept up to date as the public repository is updated. [Learn more.](https://docs.cloud.google.com/looker/docs/importing-projects#specifying_remote_projects)
  * _flash_on_ **New LookML warnings.** Introduced two new warnings to alert developers about problematic states that the LookML Validator did not previously recognize. 
    * Added a warning when model-level parameters are overridden by an `include` statement with different model-level parameters.
    * Added a warning when the `include` statement requests a LookML dashboard that can't be found. Most likely triggered by `include: *.dashboard` when no LookML dashboards are present. ### Dialects
  * **Google Cloud SQL.** Enabled support for Persistent Derived Tables. ### General Tweaks and Bug Fixes ####Dashboards, Visualizations, and Explore
  * Fixed a bug where some queries returned `No Results` in the Explore, when they should have returned a SQL error.
  * Fixed a bug where updating to Looker 5.16 caused some visualization settings to change.
  * Fixed a bug where conditional formatting could not be applied to some fields.
  * Fixed a bug where dashboard tiles remained blank instead of displaying an error when the backing explore had been deleted.
  * Fixed a bug where the series editor in the visualization panel did not listen to `hide in visualization`.
  * Fixed a bug where `Explore from Here` was not available on LookML dashboards. ####Security
  * Added encryption to account setup and reset tokens.
  * Fixed a bug where some dashboard filters defaulted to default values from other dashboards. ####Scheduling and Downloading
  * Fixed a bug where dates rendered as `#####` in some `.xls` downloads.
  * Fixed a bug where downloading CSV data from an embed preview showed a 500 error. ####Platform and Administration
  * Fixed a bug where adding LDAP user with incorrectly mapped attributes never fully created Looker user. ####LookML and Development
  * Fixed a bug where a warning was generated by LookML generated by Looker.
  * Fixed a bug where symmetric aggregates were not recomputing with the addition of a custom field.
  * `Non-Unique Primary Key` error now cached with the query that produced it.
  * Fixed a bug where Liquid was unrenderable in a Postgres `list_agg`.
  * Fixed a bug where a git branch with `/` in its name could not be deleted from the Looker UI.
  * Fixed a bug where LookML generator occasionally created self-joins.
  * Fixed a bug that showed a `ViewNotFound` error when using `suggest_dimension`.
  * Improved error handling for fields named `yes` and `no`. ####Dialects
  * Fixed a bug where Presto tables with `-` in the name were not escaped correctly in generated SQL.

## Looker 5.16 2018-06-03




### Action Hub

  * **Introduced Actions for Marketo.** [Learn more](https://discourse.looker.com/t/looker-actions-marketo/7796).
  * **Introduced Actions for Google Cloud Storage.** [Learn more](https://discourse.looker.com/t/looker-actions-google-cloud-storage/7119).
  * **Introduced new Segment, Amazon S3, and Digital Ocean Storage functionality.** [Learn more](https://discourse.looker.com/tags/actionhub).



### Scheduling and Downloading

  * **Added JSON Detail Streaming Support.** It is now possible to stream content as JSON, allowing for delivery of larger result sets.



### LookML and Development

  * Refreshed the Manage Projects page to make it easier to add and configure LookML projects. 
    * _flash_on_ The Delete Project button is now accessible through the LookML Project Settings menu rather than through Manage Projects.
  * _flash_on_ Introduced a LookML validator warning when a field name and an alias name have the potential to cause a collision.
  * Added the ability to create a read-only clone of a project from a public repository.



### Security

  * Fixed an issue that could result in unencrypted files written to a tmp directory in cases of very large Excel exports. Access to these files required system-level access to the Looker host, which is logged and monitored, and is limited to specific Looker personnel.
  * _flash_on_ Users are no longer able to edit Looks and dashboard tiles that are based on models they do not have the Explore permissions for.
  * Fixed potential HTML injection vulnerabilities in experimental Login Page Message, group name as rendered in Recent Activity page, and certain User Attributes fields in the admin panel.
  * Fixed Reverse Tabnapping Vulnerability with anchor tags in fields where markdown is permitted.



### Dialects

  * **Microsoft Azure PostgreSQL.** Introduced support for Microsoft Azure PostgreSQL.
  * **Google BigQuery Standard SQL.** Improved performance and ability to scale queries using Symmetric Aggregates.
  * **Snowflake.** Enhanced the LookML generator to better preserve character casing and properly identify all timestamp types.
  * _flash_on_ **Teradata.** The Looker .jar no longer includes the Teradata driver. Admins of customer-hosted Looker deployments will have to add a driver to their Looker machine. [Learn more](https://discourse.looker.com/t/configuring-looker-to-use-a-teradata-driver-looker-5-16/8070).
  * Improved month name SQL implementation for Hive and Spark to be less verbose and more performant.



### Content Management and Discoverability

  * **Improvements to the way content is displayed in Spaces.**
    * _flash_on_ Looks and dashboards display as thumbnails in Spaces.
    * Copy, edit, delete, and rename content from thumbnails.
    * View content metadata in Spaces.



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * _science_ Added measure `type: sum` to experimental custom fields.
  * _science_ Fixed a bug with autocomplete functionality in custom fields.
  * Fixed a bug where the `run` button was hidden in iframes where filter values contained too many characters.
  * Fixed an issue where `all_dashboards` API call returned deleted dashboards.
  * Fixed a bug where Table Calculations and Custom Fields did not work with aliased fields.



#### Scheduling and Downloading

  * _science_ Added additional endpoints to API 3.1.



#### Platform and Administration

  * Improved Log diagnostic info in cases where Google Auth fails.
  * Fixed a bug where the `run` button was missing from the admin usage page.
  * Fixed a bug where incompatible text lengths in internal databases sometimes resulted in data truncation.




## Looker 5.14 2018-05-06

### Platform and Administration

  * **Cookies Notification Banner.** Added a toggle in the Admin menu to include a cookies notification banner to all users on a Looker instance.
  * _flash_on_ **Email Subscription Changes.** Removed all email subscription options from user menus. Users will now be able to manage their subscription preferences in the [Preference Center](https://discover.looker.com/Preference-Center-Customer.html) linked in their Account page.
  * **Edit Disabled LDAP and SSO users.** Introduced functionality allowing administrators to edit disabled LDAP and SSO users.
  * **Updated Cached Data Retention Policy.** Looker has significantly reduced the time to clean up cached encrypted query results when the Instant Dashboards Labs feature is not enabled.



### Dashboards, Visualizations, and Exploration

  * _science_ **Experimental Custom Fields.** New experimental feature allows for on-the-fly field creation without additional LookML modeling. [Try it on Next](https://discourse.looker.com/t/looker-next-experimental-custom-fields/7799). [Learn more about setting up the experimental group](https://docs.cloud.google.com/looker/docs/managing-business-user-features#enabling_custom_fields).

  * **Improved Mapping Functionality and Added New Maps.** Including a satellite map, a traffic map, label visibility control, and more.

    * _flash_on_ If you're running your instance behind a firewall, you may need to whitelist `mapbox.com`, as the maps are no longer pointing to `lookecdn.com`.



### Scheduling and Downloading

  * **New Scheduler Modal.**
  * **Increased Email Size Limit.** Email size limit has been increased to 15mb.
  * _science_ **Looker API 3.1** API 3.1 endpoints and functionality are now available for experimentation in the interactive Looker API docs. [Learn more](https://docs.cloud.google.com/looker/docs/api-getting-started#interactive_api_documentation_and_explorer).



### LookML and Development

  * _flash_on_ The LookML Validator will now correctly include a warning when `${}` field references are included in SQL-based derived tables. Note that it is _not_ currently possible to reference LookML fields from a derived table; previously, Looker had silently ignored the `${}` characters if they referred to fields.
  * **Git Garbage Collection.** Looker will now periodically perform garbage collection on all project repositories via `git gc`. This will speed up most Git operations done within Looker, especially in larger projects.



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * Fixed a bug where disabled series in certain visualizations were not saved to dashboard tiles.
  * Fixed a bug where the order of visualization options was wrong in Explore toolbar.
  * Fixed a bug where some visualizations with table calculations were showing null values.
  * Fixed a bug where series label changes did not save to non-Cartesian graphs.
  * Fixed a bug with swapping between `time` and `ordinal` data on the X-axis.
  * Fixed a bug where `index()` table calc function was broken.
  * Fixed a bug where Explore field menus were cut off at bottom of page.



#### LookML and Development

  * Fixed a bug where importing any LookML dashboards into a Space would import all LookML dashboards into that Space.
  * Fixed a bug where some PDTs were failing to build in the correct order.
  * Fixed a bug with datagroups lacking a `max_cache_age`.
  * Fixed a bug where incorrect LookML was being generated from a dashboard.



#### Content Management and Discoverability

  * Fixed a bug where `add to dashboard` button had disappeared.



#### Scheduling and Downloading

  * Fixed a bug where editing scheduled plan filters did not save.



#### Dialects

  * _flash_on_ Data Virtuality drivers are no longer bundled with the Looker `.jar`. Admins of customer-hosted Looker deployments will have to add a driver to their Looker machine. [Learn more](https://docs.cloud.google.com/looker/docs/db-config-datavirtuality).



#### Platform and Administration

  * Fixed a bug where it was not possible to delete users that were no longer editable.
  * Fixed a bug where connection test was resulting in a false negative.



#### Security

  * Introduced the ability to escape values in CSV files that might be interpreted as formulas or macros in common spreadsheet applications.
  * Added clickjacking protections for Looker login pages.




## Looker 5.12 2018-04-08

### LookML and Development

  * **Improved Content Validator.** `replace` and `remove` functions are now more clearly distinct and Content Validator now replaces field names in visualization config settings.
  * **Bulk delete from Content Validator.** It is now possible to dispose of many Looks at once when grouping validator errors by Look.
  * **Git branch deletion.** Introduced the ability to delete shared Git branches.
  * **Reference LookML Objects in SQL Runner.** `${view_name.field_name}` and `{view_name.SQL_TABLE_NAME}` can now be referenced from SQL Runner.



### Platform and Administration

  * **PDT-specific database credentials.** You can now assign PDT processes credentials, allowing you to prioritize builds, send builds to different Snowflake warehouses, and reduce users' write access. [Learn more](https://discourse.looker.com/t/using-a-different-database-connection-for-pdt-jobs/7587).



### Scheduling and Downloading

  * _flash_on_ **The Legacy API has been completely removed.** It is no longer possible to create API-only users or to use the Legacy API.



### General Tweaks and Bug Fixes

#### Security

  * Fixed an issue with the password reset process.



#### Administration

  * Added a tooltip to explain the **Suggested For You** section of the home page.
  * _flash_on_ Fixed a bug where User Attributes needed to be explicitly removed when generating SSO embed URLs. Parameter declarations will now overwrite existing ones, as originally intended.



#### LookML and Development

  * Fixed a bug where some datagroup-triggered PDTs were stuck in the build process.
  * Fixed a bug where YAML LookML was being generated for some new LookML projects.
  * Fixed a bug where generated dashboard LookML was wrong if warnings were present.
  * Fixed a bug with generated SQL in cases where `yesno` dimensions are nested inside conditional liquid statements.
  * Fixed a bug where liquid in `label` parameters was not evaluated and rendered correctly.
  * Fixed a bug where `COUNT(*)` was generated instead of `COUNT(field_name)` in some views.
  * Fixed a bug where percentile measures were being cast as numeric instead of decimal.
  * Fixed a bug where nulls were being sorted to the top if the row limit was hit and dimension fill was turned on.



#### Scheduling and Downloading

  * _flash_on_ Fixed a bug where `.xlsx` schedules were sending empty files if results had not changed since last run. Scheduled content will be sent upon update to Looker 5.12, regardless of attachment format or whether "and results changed since last run" is checked.



## Looker 5.10 2018-03-11

### Content Management and Discoverability

  * **Content Validator for Lookless dashboards.** The Content Validator is now able to detect and solve issues in saved tiles on Lookless dashboards.
  * _science_ **Save Merged Results to dashboards.** Users can now save Merged Results queries to dashboards. Please note: these elements do not currently interact with dashboard-level filters. [Learn more about configuring Merged Results](https://discourse.looker.com/t/experimental-feature-setting-up-merged-results/6225).



### LookML and Development

  * **Added the ability to create a new Project via the API.** The new `create_project` call allows API users to create a new LookML Project for development in the UI.
  * **`${view_name.SQL_TABLE_NAME}` is now usable in most `sql:` parameters.** [Learn more.](https://docs.cloud.google.com/looker/docs/sql-and-referring-to-lookml#substitution_operator_\($\))
  * **Added ability to include custom filters in Native Derived Table definition.** New `expression_custom_filter` parameter allows developers to define custom filters on NDTs in LookML. [Learn more.](https://docs.cloud.google.com/looker/docs/reference/param-view-explore-source#defining_a_native_derived_table)
  * _flash_on_ **The`partition_keys` parameter now requires quotes around list items.** [Learn more.](https://docs.cloud.google.com/looker/docs/reference/param-view-partition-keys)



### Platform and Administration

  * **Introducing schedule list by user.** Users are now able to see and navigate their saved schedules all in one place.
  * **Added`allowed_clock_drift` support for SAML configurations.** [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-saml#saml_auth_settings)



### Scheduling and Downloading

  * **Added support for number formatting in Excel.** Downloads with number fields no longer appear as strings in Excel.
  * **_build_ `Dashboard PDFs and Scheduled Visualizations` is now enabled by default.** To have access to rendering options on a customer-hosted instance, the administrator must download the PhantomJS version 2.1.1 on the server hosting the Looker application.



### Dialects

  * **Added Dremio support.**
  * **Updated Snowflake support to include`IN` statements where appropriate.**



### Security

  * Restricted the ability to use a user-editable user attribute towards parameterized database connections.
  * Tightened access to application database.
  * Removed an XSS vulnerability on the `admin/connections/.../edit` page.
  * Addressed a SAML authentication bypass vulnerability.



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * _flash_on_ Added error checking to prevent one field from having two or more filters on a dashboard.
  * Fixed a family of bugs caused by over-row-limit Looks.
  * Fixed a bug where maps were not responding to filter changes.
  * Fixed a bug with scrolling and rendering many dashboards on the Move Dashboard modal.
  * Fixed a bug where values containing commas could not be set as filter defaults on dashboards.
  * Fixed a bug where dashboard filters do not listen to user attribute default values when `Allow Multiple Filter Values` is off.
  * Fixed a bug where option + click did not restore all values in an explore when `Show Silhouette of Disabled Series` was enabled.
  * Fixed a bug where filters of type "1, not 0" would fail.
  * Fixed a bug where deleting a Look that was connected to a dashboard would break the dashboard.



#### LookML and Development

  * Added warning checks before generating dashboard LookML.
  * Fixed a bug where the IDE could not handle git branches with periods in the name.
  * Fixed a bug where counts in one-to-many joins generated the wrong SQL if the count was filtered but not selected.
  * Fixed a bug with user attributes tied to parameters.
  * Fixed a bug where date-type parameters were blank when referenced in `always_filter` parameters.



#### Content Management and Discoverability

  * Added a tooltip explaining that absolute URL paths (as opposed to relative paths) are needed for external links on dashboards.



#### Scheduling and Downloading

  * Added sanitization of reserved characters in file names of downloaded dashboard `CSV`s.
  * Fixed a bug on the Scheduler modal where toggling between datagroup and schedule toggled all schedules, instead of the selected schedule.
  * Fixed a bug where table calc formats were still coming through unformatted Excel downloads.
  * Fixed a bug with the "Send Attachment" Slack integration for non-ZIP attachments.



#### Dialects

  * Fixed a bug where prepended comments for Snowflake queries were not visible.



#### Platform and Administration

  * Added custom filtering on LDAP queries.
  * Fixed a bug where disabling users returned an "undefined" error.
  * Fixed a bug causing persistent persistent sessions for some users.



## Looker 5.8 2018-02-11

### Dialects

  * **Turn off`ORDER BY` in API Queries.** Introduced the option to turn off sorts for downloaded and API queries for users on Hive-based databases.



### Platform and Administration

  * _flash_on_ **Replaced the`Delete` button with the `Disable` button on User Management page to reduce the risk of accidental user deletion.** [Learn more](https://discourse.looker.com/t/what-does-it-mean-to-disable-a-user/1091).
  * _flash_on_ **Fixed a bug with the`see_user` permission in closed system configurations.** Non-admin users on closed systems with the `see_user` permission are now able to see _all_ Looker users rather than those in their same user group.



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * Fixed a bug where Merged Results negatively affected the Filter-Listener modal.
  * Fixed a bug where resizing dashboard tiles changed layouts.
  * Fixed a bug with monotone line charts.
  * Fixed a bug where URLs were not updating when merging results.
  * Fixed a bug where dashboard tiles were not reliably updating after being edited.
  * Fixed a bug with table calculations on Merged Results.
  * Fixed a bug with sorting by `Day of the Week` in Explore.
  * Fixed a bug that resulted in lost progress in Custom Filters upon hitting Enter.
  * Fixed a bug where dashboard LookML was generating with filters out of order.
  * Fixed a bug where dashboards could be saved with no title.
  * Fixed a visual bug with the Delete Dashboard modal.
  * Fixed a bug with stacked series visualizations on merged results.
  * Fixed a bug where filter suggestions remained blank after typing.
  * Fixed a bug where the map visualization did not move upon filtering.



#### LookML and development

  * Fixed an issue with High Sierra that interfered with smooth scrolling in the IDE for users on Safari.
  * Fixed a bug where the LookML validator could not be run on the View Uncommitted Changes page.
  * Fixed a bug where Liquid variables caused incorrect URL encoding.
  * Fixed a bug where user attributes were not correctly populating in `sql_always_where`.
  * Fixed a bug with `filter_expression` and Liquid rendering.
  * Added git validation for branch names upon creation.



#### Content Management and Discoverability

  * Fixed a visual bug on the homepage with clipped heart icons.



#### Scheduling and Downloading

  * Improved error messaging around SMTP issues for admins. [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-platform-smtp#smtp_error_messages)
  * Fixed a bug where certain characters in CSV titles were incorrectly escaped.
  * Edited the API documentation for `user_for_credential` to include `oidc`.
  * Fixed a bug where the dashboard Scheduler modal was inaccessible to the owner of the dashboard.
  * Fixed a bug with the `set_role_groups` API endpoint.
  * Fixed a bug where Scheduler modal was visible to embed users without the `save_content` permission.
  * Fixed a bug where embed users were unable to download PDF and PNG files.
  * Fixed a bug that caused some schedules to fail.
  * Fixed a bug that resulted in an error when running asynchronous queries via the API.
  * Added a quick navigation option for embed users to access the Shared space when saving Looks and dashboards.



#### Dialects

  * Fixed a bug where SQL did not display available tables in SAP Hana.



#### Platform and Administration

  * Fixed a bug where certain user groups could not be edited.
  * Fixed a bug with incompatible text types in MySQL and HyperSQL.
  * Fixed a bug with embed user `external_group_id` generation.
  * Fixed a bug with the Edit Role menu.
  * Fixed a bug with the Add Accounts drop-down menu.
  * Fixed a bug with the Show Tables button in the connection menu.
  * Fixed a bug where user groups could be mistakenly created without a name.
  * Added the ability to scroll through curated admin sidebar.
  * Added jgit logging capability for admins.



#### Content Management

  * Fixed a bug where admin sidebar helper text was incorrect.
  * Added an informational tooltip to admin content sidebar.



## Looker 5.6 2018-01-14

### Action Hub

  * **Introduced the Looker Action Hub.** And some great integrations (Airtable, AWS, Azure Storage, Digital Ocean, Hipchat, JIRA, SendGrid, Slack, Tray, Twilio, Zapier joining Segment). [Learn More.](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions)
    * _flash_on_ **Changes to Segment integration.** Users who have previously used Segment integration will need to accept new terms of service before continuing to use this feature.



### Content Management and Discoverability

  * **Curatable Content Sidebar for Admins.** Admins are now able to create and curate a sidebar on the Looker homepage that allows them to communicate with Looker users in their organization. [Learn More.](https://docs.cloud.google.com/looker/docs/making-announcements-to-your-users)
  * **"Recently Viewed" Content on Homepage.** "Recently Viewed" content can be organized by user group, allowing admins to track content use.



### LookML and Development

  * _flash_on_ **Renamed`Push` and `Pull`.** In Developer Branch Git options menu in IDE to `Push` and `Pull Remote Changes` for clarity.



### Scheduling and Downloading

  * **Dashboard CSV ZIPs.** It is now possible to deliver zipped .csv files from Dashboards via schedule and Send Now.
  * _flash_on_ Public Looks no longer support row limits of more than 5,000. Larger result sets will be truncated at the lesser of the saved row limit or 5,000 rows.
  * _flash_on_ **Increased the size of images in scheduled emails.** Look and Dashboard images embedded in scheduled emails no longer have a fixed width.



### Dialects

  * **Added Qubole Presto streaming capability.**
  * **Introduced support for Date/Time partitioned columns in Google BigQuery.** [Learn more](https://discourse.looker.com/t/announcing-date-time-partitioned-pdts-for-google-bigquery/7132).
  * **Database views in Vertica now appear in SQL Runner.**



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * Added animated scrolling for the filter pane.
  * Fixed a bug where ashboards with "newspaper" layout didn't re-render when window was resized.
  * Fixed a bunch of issues around a mistaken ability to add a Look with an invalidly high limit to a Dashboard.
  * Fixed a bug where Dashboard Refresh Intervals were not properly updating the Dashboard.
  * Fixed a bug where filters bar takes up space in embedded Dashboard when there aren't any filters.
  * Fixed a harmless error that would appear in the console when editing Dashboard filters.
  * Fixed a bug where Dashboard suggestions drop-down not closed when Dashboard is run.
  * Fixed a couple issues with filter suggestions not appearing when they should.
  * Fixed a bug where Saving changes from Edit Settings on a look with a schedule in space gear menu doesn't work.
  * Fixed a bug where toolbar buttons didn't work after resizing and deleting last tile on Dashboard.
  * Fixed a bug where the Dashboard edit toolbar did not follow embed Dashboard styling.
  * Fixed an issue on mobile Dashboards where filters would not wrap, thereby causing whitespace.
  * Shortened the time it takes for a tooltip to disappear on mobile Dashboards in the hopes of leaving fewer phantom tooltips.
  * Fixed a bug where Dashboard banners had poorly escaped titles.
  * Fixed a bug where the ability to option+click a legend series name no longer selected that item/reselected all other items.
  * Fixed a bug where, when collapsed, the filters bar showed a parameter's value instead of its label.
  * Fixed a bug where Map doesn't move on filter update.
  * Provide the ability to delete all Looks no longer on a Dashboard when deleting a Dashboard.
  * Allow horizontal scrolling in the filter suggestion field to enable ability to see full value names.



#### LookML and Development

  * _flash_on_ The LookML Validator now correctly warns when Dashboard `filters` have empty, unnecessary, or unknown parameter declarations. Until addressed, these warnings may prevent committing new LookML changes if the Code Quality feature is enabled.
  * Fixed a bug where `access_filter_fields` usage, though deprecated, was passing through the LookML Validator.
  * Fixed a bug where `_in_query` not working as expected for `sql_on` in row totals.
  * Fixed a couple of bugs with conditional formatting and table calculations.
  * Fixed a bug where the timezone tooltip was activating even when the mouse was not hovering over it.
  * Fixed a bug where typo in join relationship would cause the validator to 500.
  * Fixed a bug where Drill on totals passes {} into filter leading to no results.



#### Content Management and Discoverability

  * Fixed a bug where `page:properties:changed` event broadcast static height incorrectly for embedded iframes.
  * Fixed a bug where **Top Content** wouldn't load when faceted to another group.
  * Updated the logic behind the **Suggested For You** section to more heavily weight users like you and the recency of views.



#### Scheduling and Downloading

  * Wrap filters instead of cutting them off on PDF download.
  * Ensure Heatmap legend appears on PDF download.
  * Fixed a bug where Embedded users were unable to download Dashboards as .csv.
  * Fixed a bug where downloaded png images from Dashboard tile did not have filter applied.
  * Fixed a bug where .xlsx files didn't open in Excel due to a `value_format` issue.
  * Fixed a bug where sending explore results errored.
  * Fixed a bug where Custom SMTP password not updated to null when blank password is saved in SMTP settings
  * Fixed a bug where PDF downloads didn't work on Dashboards that contained blank table calculations.
  * Remove the Download option from drill menus if users do not have the permission to download.



#### Dialects

  * Fixed a vulnerable dependency from Qubole Presto.



#### Platform and Administration

  * Provide an error for customers who try to start Looker with Java 9, which is not supported.
  * Updated the S3 SDK.



#### Content Management

  * Fixed a bug where the Content Access Admin panel didn't show all subspaces of a given space.



#### Authentication

  * Provide the ability to use alternate login (email/password) when using OpenID Connect as authentication scheme.



## Looker 5.4 2017-12-03

### LookML and Development

  * **Jump to file.** It is now possible to search for LookML files by name from within the IDE. [Learn more](https://docs.cloud.google.com/looker/docs/manage-projects#searching_for_project_files).
  * **Example datagroups.** Added example datagroup parameters to newly-generated projects. [Learn more](https://docs.cloud.google.com/looker/docs/generating-a-model).
  * _flash_on_ **Completely removed legacy features.**
    * [LookML `decimals` parameter and `int` field](https://discourse.looker.com/t/deprecation-notice-decimals-parameter-and-int-field-type-3-38/2015)
    * [Deprecated LookML parameters](https://discourse.looker.com/t/deprecation-notice-old-lookml-parameters-3-16/5446)
    * [Coerce dimensions to measures](https://discourse.looker.com/t/why-looker-warns-when-a-dimension-references-a-measure-and-how-to-fix-it/3259)
    * [YAML-based LookML for modeling](https://discourse.looker.com/t/deprecation-notice-old-style-yaml-lookml-4-4/4025) (only applies for newly-created projects, existing projects will continue to function)
    * [User-based development mode](https://discourse.looker.com/t/deprecation-notice-change-in-dev-mode-api-behavior-4-16/5297)



### Content Management and Discoverability

  * **Content Validator performance.** Decreased time for complete validation in Content Validator.
  * The **LookML Dashboards** Space is no longer displayed in the **Browse** drop-down when there are no dashboards in the Space.



### Dashboards and Visualizations

  * _flash_on_ **Dashboard tile defaults.** Changed default size and placement of new dashboard elements to make editing multi-element dashboards easier. [Learn more](https://docs.cloud.google.com/looker/docs/creating-legacy-dashboards#configure).
  * **Lookless dashboard conversion.** Improved usability of dashboard conversion modal.
  * _flash_on_ **Completely removed legacy features.**
    * [Implicit dashboard default timezone](https://discourse.looker.com/t/legacy-feature-implicit-dashboard-default-timezone-looker-4-10/4500)



### Platform and Administration

  * **Clarified Connections page.** Updated the **Connections** page to make it more apparent that the maintenance schedule applies to both Persistent Derived Tables and Datagroups.
  * Added option for administrators to disable "Persistent Sessions." [Learn more.](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-sessions)
  * _flash_on_ **Completely removed legacy features.**
    * [Default Query Result Persistence is 5 Minutes](https://discourse.looker.com/t/change-notice-default-cache-length-4-2/3830)
    * [Legacy Oracle Security Settings](https://discourse.looker.com/t/deprecation-notice-old-oracle-db-configuration-3-50/5448)
  * _science_ **SQL Context Comments.** Added an experimental labs feature that prepends a comment to outgoing SQL queries for tracking. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-server-usage#sql_comments).



### Security

  * Fixed issues where MySQL, Snowflake, and MariaDB drivers had elevated file system access.



### Scheduling and Downloading

  * _flash_on_ **Completely removed legacy features.**
    * [Single Row Table Headers](https://discourse.looker.com/t/deprecation-notice-exports-with-pivoted-columns-look-different-in-3-52/3029)
    * [JSON Numbers as Strings](https://discourse.looker.com/t/deprecation-notice-numbers-can-be-returned-as-numbers-instead-of-strings-in-api-3-52/3049)
    * [Allow Unlimited Downloads the Might Crash Looker](https://discourse.looker.com/t/legacy-feature-allowing-unlimited-downloads/4987)



### General Tweaks and Bug Fixes

#### Dashboards and Visualizations

  * Added a more informative error when a Dashboard Tile's Explore changes.
  * Fixed an issue where the Reset Look link on a Look was broken.
  * Fixed an issue where Scatterplot X Axis Values could be wrong although the tooltip was correct.
  * Fixed a bug where tile legends were showing in the wrong place with timeline visualizations
  * Fixed a bug where editing a Look and saving didn't return the proper filter value
  * Returned the Run button to the filters bar in Embed.
  * Fixed a Dashboard bug that could occur with null date filter values.
  * Fixed a charting bug where a donut multiples would work in the edit modal and then break on the dashboard.
  * Fix an issue where tiles without titles on Dashboards obscured the gear menu on the tile.
  * Fixed an issue where a tile would not update after changing the title.
  * Fixed an issue where option+click on a legend item didn't restore the rest of the legend items to the chart.
  * Fixed an issue where tiles without titles on Dashboards obscured the gear menu on the tile.
  * Fixed an issue where white spacing on bar and map visualizations expanded on dashboard tiles.
  * Fixed an issue where pivots weren't showing in the correct order in the table viz.



#### Explore

  * Fixed an issue where filters bar won't open when clicking on "filter" in the field picker or the filter drop-down when the dimension is included in the query.
  * Fixed a bug where contains() Looker function did not work for '
  * Fixed a bug where the back button didn't work in embedded Explore
  * Fixed an issue where pivoting single tier dimension created an infinite loop error that rendered browser unusable.



#### Downloads and Scheduling

  * Fixed an issue with downloading Dashboard as CSV that caused a 400 error.
  * Fixed an issue where you could create, but not execute, a schedule even without model access to the Look.
  * Fixed a bug where users could not schedule or download a dashboard that contained a single record visualization.
  * Ensured that All Results download option is not available on Dashboard Tile menu for unstreamable results to avoid download errors.
  * Can download csv from dashboard even without PDF Dashboard Labs feature enabled.



#### LookML and Model Development

  * Fixed an issue where users can't use "create model" if they've already clicked it and navigated away.
  * Fixed a bug where Native Derived Tables would not generate the full SQL for a query and break Looks.



#### Platform and Administration

  * Fixed an issue where homepage tiles weren't loading if default color scheme.
  * Renamed the Integration Hub the Action Hub.
  * Ensured that changing a user attribute breaks the cache.



#### Content Management and Discoverability

  * Fixed a bug where the Favorites heart appeared on LookML Dashboards, even though they cannot be favorited.



#### Dialects

  * Ensured that BigQuery cost estimation remains when relevant and disappears when not.
  * Fixed a bug where Druid Query fails if hyphen exists in data store name.



## Looker 5.2 2017-11-05

### Dashboards and Visualizations

  * **Field-by-field conditional formatting.** Added the ability to color table visualizations' series individually. [Learn more](https://docs.cloud.google.com/looker/docs/legacy-table-options#enable_conditional_formatting).
  * **Dashboard tile improvements.**
    * **Duplicate tiles** on a dashboard. [Learn more](https://docs.cloud.google.com/looker/docs/editing-legacy-dashboards#duplicating_tiles).
    * **Convert Looks to tiles** on a given dashboard. [Learn more](https://docs.cloud.google.com/looker/docs/editing-legacy-dashboards#convert_tiles).
    * _flash_on_ Reduced the default new tile width.
  * **Added the ability to hide the title of a Look or tile on a dashboard.** [Learn more](https://docs.cloud.google.com/looker/docs/editing-legacy-dashboards#hiding_the_title_of_a_tile).



### Content Management and Discoverability

  * **Convert entire Look-based dashboards to tile-based ones.** Added the ability to replace a dashboard's Looks with tiles, optionally deleting the previously associated Looks. [Learn more](https://docs.cloud.google.com/looker/docs/organizing-spaces#converting_dashboards_from_look-linked_to_query_tiles).
  * _flash_on_ Removed the Browse navigation sidebar from the home page to allow for more suggested content. You can still use the top Browse menu for all navigation.



### Scheduling and Downloading

  * **Just send it.** Added the option to send data or visualizations from Looks and Dashboards without having to create a schedule. [Learn more](https://docs.cloud.google.com/looker/docs/scheduling).
  * **Dashboard data downloads.** Added the ability to download a zip of CSVs for each Dashboard element. [Learn more](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards#downloading_your_dashboard_as_csv_files).
  * _flash_on_ Improved memory and disk space consumption. Older schedule and render cache entries will removed more rapidly, with results being available to the RenderTask API for one hour.



### LookML and Development

  * **Dynamic field labels.** Added the ability to dynamically change `label` rendering using Liquid variables. Supports user attribute based rendering. [Learn more](https://docs.cloud.google.com/looker/docs/liquid-variable-reference).
  * **Lists in Redshift.** Added support for the `list` measure type on Amazon Redshift connections. [Learn more](https://docs.cloud.google.com/looker/docs/reference/param-measure-types#list).
  * **Improved LookML Validator speed** , especially when using the experimental Labs feature **Only Validate Changed LookML** and when validating Native Derived Tables.
  * _flash_on_ **LookML Collaboration.** Switching to a new branch is no longer possible in cases where there are uncommitted changes or a branch is in a merging state.



### Platform and Administration

  * **LDAP user attributes.** Added the ability to map user attributes to LDAP users. This does not introduce the ability to map to LDAP groups. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-authentication-ldap#pairing_ldap_user_attributes_with_looker_user_attributes).
  * **Support access Data.** The Support Access page now includes information about who has changed Looker support access settings and who from Looker support has accessed your instance and why. [Learn more](https://docs.cloud.google.com/looker/docs/admin-panel-general-support-access).
  * _flash_on_ **Introduced the "Allow calling legacy query API" Legacy Feature.** [Learn more](https://discourse.looker.com/t/legacy-feature-notice-allow-calling-legacy-query-api/6366).



### Dialects

  * **Oracle DWCS (now called ADW).** Introduced initial support for Oracle ADW.
  * **Qubole Presto.** Updated the driver from 1.1.0 to 1.1.6.



### Security

  * Addressed a SQL injection vulnerability.



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * Fixed an issue where Public Looks filtered on User Attributes produced an error page.
  * Fixed an issue where previously saved Looks couldn't be edited in some circumstances.
  * Fixed an issue where visualizations could display two y-axes for a single pivoted series.
  * Fixed an issue where Dashboard Filter changes didn't reliably save.
  * Fixed an issue where adding a Text element could cause a Dashboard to ignore its Filters.
  * Fixed an issue where diff_days produced broken SQL in Custom Filters.
  * Fixed an issue where an errant error about color palettes could prevent Dashboard elements from loading.



#### LookML and development

  * No longer unnecessarily apply Symmetric Aggregates when aggregating from the right side of a one to many join.
  * Fixed an issue where `_is_selected` and `_in_query` could produce broken SQL in the presence of Totals and Row Totals.



#### Content Management and Discoverability

  * Fixed an issue where you couldn't use the Content Validator to replace colons.



#### Scheduling and Downloading

  * Fixed an issue where Datagroups did not populate in the Schedule modal.



#### Dialects

  * Fixed an issue where pivots only worked on IBM Netezza connections in simple cases.



#### Platform and Administration

  * Fixed an issue where the Datagroups Admin page could display incorrect check times.
  * Added a progress bar to page loads.



## Looker 5.0 2017-10-08

### LookML and Development

  * **LookML Collaboration.** Added the ability to create development branches that are not specifically tied to any individual's development mode. Use these branches to work with others on a project or to separate discrete pieces of work you have in progress. [Learn more](https://docs.cloud.google.com/looker/docs/version-control-and-deploying-changes#working_with_git_branches).
  * **Reference pivot values in Liquid.** You can now reference the {{ `value` }} of a pivot value without it being the one you're actively clicking on.
  * **Timezone support for Native Derived Tables.** Use the `timezone` `explore_source` parameter to convert to a consistent timezone or, for ephemeral derived tables, to the timezone your query is in.
  * **Native Derived Tables are no longer a Labs feature.**



### Content Management and Discoverability

  * **Lookless dashboards are out of beta**. Add tiles to your dashboards either by creating the query directly on a dashboard or saving from an exploration.
  * _science_ **Landing Pages.** Introduced a new, experimental home page that will surface Favorite and Suggested content as soon as you log in. [Learn more](https://docs.cloud.google.com/looker/docs/finding-content#personalized_home_page_with_visual_thumbnails).



### Scheduling and Downloading

  * **Increased allowable schedule size.** Attachment-only formats (currently txt, csv, html, md, and json) support scheduling without any row limit applied. Keep in mind, though, that emails of more than 7.5mb may be returned to the sender.



### Dialects

  * **Druid.** Introduced initial support for Druid. [Learn more](https://docs.cloud.google.com/looker/docs/db-config-apache-druid).
  * _flash_on_ **Google BigQuery Legacy SQL.** Updated the name from "Google BigQuery" to "Google BigQuery Legacy SQL" in the connection panel, SQL Runner, and other locations where the dialect name is displayed.



### Platform and Administration

  * _flash_on_ **Disabled and removed a number of Legacy Features.** [Learn more.](https://discourse.looker.com/t/legacy-features-end-of-life-schedule/2067)



### Security

  * Better protected against certain authentication replay attacks.
  * Addressed a file disclosure vulnerability.
  * Addressed a file system vulnerability.
  * Identified and addressed a logging issue.



### Dashboards and Visualizations

  * _science_ **Data Merge.** Introduced the experimental [Merged Results](https://docs.cloud.google.com/looker/docs/merged-results) Labs feature, which allows users to visualize results from multiple datasets without modeling. The ability to save as well as add to Dashboards and Looks is currently in development.
  * _flash_on_ Pie chart's labels will no longer display for every value if there is not enough room. However, labels will no longer get cut off.



### General Tweaks and Bug Fixes

#### Dashboards, Visualizations, and Explore

  * Fixed an issue where filter values would not apply on a Dashboard unless the user hits enter or exits the input box before running the query.
  * Addressed an issue where users could Clear Cache & Refresh even when Required Filters were not entered.
  * Fixed an issue where explores were not displayed using their label.
  * Fixed an issue where a blank page was displayed when a user did not have access to a Look.
  * Fixed an issue where errors would occur when results have arrived but Table Calculations haven't been performed.
  * Fixed an issue where adding a Look to a Dashboard resulted in an ineditable, incorrect title on your Dashboard.



#### LookML and development

  * Fixed an issue where Looker incorrectly errored on parameters that carried through includes.
  * Fixed an issue where a view file with a parameter declaration could not be extended.
  * Fixed an issue related to parameter and Liquid joins.
  * Looker now properly errors when percentiles are used on dialects that don't support them.
  * Fixed an issue where the IDE could display false error messages.
  * Fixed an issue where the Development Mode toggle did not display on Admin pages.
  * Improved the error message when Liquid references were not properly scoped in Derived Tables.
  * Fixed a few issues with the Don't Revalidate Unchanged LookML Labs feature.



#### Content Management and Discoverability

  * Fixed an issue where Dashboard and Look lists did not load at the same time, making it appear as though the page had not finished loading.
  * Fixed an issue where the Model column was not displayed in the LookML Dashboards space.
  * Fixed an issue where you couldn't use the Content Validator to replace spaces ().
  * Fixed an issue where LookML Dashboards with numeric titles broke search.



#### Dialects

  * Google BigQuery Standard SQL. Fixed an issue that produced a SQL error when Symmetric Aggregates where applied to filtered measures.
  * Google BigQuery. Fixed an issue where canceled queries displayed a status of "error" in the Query panel. This applies to both Google BigQuery Standard SQL and - Google BigQuery Legacy SQL.
  * Addressed some issues with query killing on Presto, Spark, DB2, Qubole, Redshift, and Teradata.



#### Platform and Administration

  * Fixed an issue where the API did not properly report errors for duplicates in query.slug to callers.
  * Fixed an issue where new user emails did not send out.
  * Fixed an issue where the Query panel could still display orphaned queries.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
