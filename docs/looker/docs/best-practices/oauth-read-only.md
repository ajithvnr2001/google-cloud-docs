---
url: https://docs.cloud.google.com/looker/docs/best-practices/oauth-read-only/
title: Restricting OAuth scope to read-only for Google BigQuery connections \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:36.926253+00:00
---

# Restricting OAuth scope to read-only for Google BigQuery connections  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/oauth-read-only/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Restricting OAuth scope to read-only for Google BigQuery connections Stay organized with collections  Save and categorize content based on your preferences. 

Prior to Looker 24.20, when [OAuth authentication for Google BigQuery connections were being set up](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery#oauth_for_bigquery_connections), Looker created OAuth credentials that allowed the database user to request read and write scope. Starting in Looker 24.20, Looker instead requests OAuth read-only scopes for any new BigQuery OAuth connections, new OAuth authorizations to existing BigQuery OAuth connections, and re-authorizations to existing BigQuery OAuth connections.

Note the following for Google BigQuery connections with read-only scopes:

  * Users can't [execute write operations in SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db#modifying_database_schema_and_data).
  * Google BigQuery connections that are configured for OAuth authentication do not support [query killing](https://docs.cloud.google.com/looker/docs/admin-panel-database-queries#query_killing).



Starting on March 1, 2025, Looker will sign out any users who have not re-authorized with OAuth read-only scopes from all corresponding BigQuery connections. This will cause any schedules dependent on these connections to fail. Each of these users will need to reauthorize their OAuth connection credentials to ensure uninterrupted schedule delivery. You can also [reassign a schedule](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule#reassign_a_schedule) to a user who has reauthorized their OAuth connection credentials.

To ensure a seamless transition to the updated OAuth credentials, follow the steps in the proceeding sections:

  * Reauthorize your OAuth connection credentials
  * Generate a list of all users with potentially affected schedules
  * (Optional) Force read-only scope usage across your Looker instance



## Reauthorize your OAuth connection credentials

To update your OAuth credentials to use a read-only scope, follow these steps:

  1. Navigate to the [**Account** page](https://docs.cloud.google.com/looker/docs/user-account).
  2. In the **OAuth Connection Credentials** section, click **Reauthorize** next to each set of credentials.
  3. You will be prompted to reauthorize Looker to access BigQuery data. The confirmation screen should list the permission "View your data in Google BigQuery" rather than "View and manage your data in Google BigQuery."



Each user that has OAuth credentials for the BigQuery connection will need to complete these steps.

## Generate a list of all users with potentially affected schedules

To generate a list of all users without read-only OAuth credentials who have created schedules on your BigQuery connections, visit the following System Activity Explore, replacing INSTANCE_NAME with the address of your Looker instance (such as `https://example.cloud.looker.com`).
    
    
    INSTANCE_NAME/explore/system__activity/scheduled_plan_oauth_events?fields=user.name,count,query.model&f[query.model]=-NULL&f[count]=0&sorts=user.name&limit=500&column_limit=50&query_timezone=America%2FLos_Angeles&vis=%7B%22show_view_names%22%3Afalse%2C%22show_row_numbers%22%3Atrue%2C%22transpose%22%3Afalse%2C%22truncate_text%22%3Atrue%2C%22hide_totals%22%3Afalse%2C%22hide_row_totals%22%3Afalse%2C%22size_to_fit%22%3Atrue%2C%22table_theme%22%3A%22white%22%2C%22limit_displayed_rows%22%3Afalse%2C%22enable_conditional_formatting%22%3Afalse%2C%22header_text_alignment%22%3A%22left%22%2C%22header_font_size%22%3A12%2C%22rows_font_size%22%3A12%2C%22conditional_formatting_include_totals%22%3Afalse%2C%22conditional_formatting_include_nulls%22%3Afalse%2C%22x_axis_gridlines%22%3Afalse%2C%22y_axis_gridlines%22%3Atrue%2C%22show_y_axis_labels%22%3Atrue%2C%22show_y_axis_ticks%22%3Atrue%2C%22y_axis_tick_density%22%3A%22default%22%2C%22y_axis_tick_density_custom%22%3A5%2C%22show_x_axis_label%22%3Atrue%2C%22show_x_axis_ticks%22%3Atrue%2C%22y_axis_scale_mode%22%3A%22linear%22%2C%22x_axis_reversed%22%3Afalse%2C%22y_axis_reversed%22%3Afalse%2C%22plot_size_by_field%22%3Afalse%2C%22trellis%22%3A%22%22%2C%22stacking%22%3A%22%22%2C%22legend_position%22%3A%22center%22%2C%22point_style%22%3A%22none%22%2C%22show_value_labels%22%3Afalse%2C%22label_density%22%3A25%2C%22x_axis_scale%22%3A%22auto%22%2C%22y_axis_combined%22%3Atrue%2C%22ordering%22%3A%22none%22%2C%22show_null_labels%22%3Afalse%2C%22show_totals_labels%22%3Afalse%2C%22show_silhouette%22%3Afalse%2C%22totals_color%22%3A%22%23808080%22%2C%22type%22%3A%22looker_grid%22%2C%22defaults_version%22%3A1%2C%22series_types%22%3A%7B%7D%2C%22hidden_fields%22%3A%5B%22count%22%5D%7D&filter_config=%7B%22query.model%22%3A%5B%7B%22type%22%3A%22%21null%22%2C%22values%22%3A%5B%7B%7D%2C%7B%7D%5D%2C%22id%22%3A0%7D%5D%2C%22count%22%3A%5B%7B%22type%22%3A%22%3D%22%2C%22values%22%3A%5B%7B%22constant%22%3A%220%22%7D%2C%7B%7D%5D%2C%22id%22%3A1%7D%5D%2C%22__%21internal%21__%22%3A%5B%22OR%22%2C%5B%5B%22AND%22%2C%5B%5B%22FILTER%22%2C%7B%22field%22%3A%22query.model%22%2C%22value%22%3A%22-NULL%22%2C%22type%22%3A%22%21null%22%7D%5D%2C%5B%22FILTER%22%2C%7B%22field%22%3A%22count%22%2C%22value%22%3A%220%22%7D%5D%5D%5D%5D%5D%7D&dynamic_fields=%5B%7B%22category%22%3A%22measure%22%2C%22expression%22%3Anull%2C%22label%22%3A%22Count%22%2C%22value_format%22%3Anull%2C%22value_format_name%22%3Anull%2C%22based_on%22%3A%22event_attribute.value%22%2C%22_kind_hint%22%3A%22measure%22%2C%22measure%22%3A%22count%22%2C%22type%22%3A%22count_distinct%22%2C%22_type_hint%22%3A%22number%22%2C%22filters%22%3A%7B%22event_attribute.value%22%3A%22%25%2Fauth%2Fbigquery.readonly%25%22%7D%7D%5D&origin=share-expanded
    

Each of these users will need to reauthorize their OAuth connection credentials to ensure uninterrupted schedule delivery.

## (Optional) Force read-only scope usage across your Looker instance

To sign out all your users who have OAuth credentials that allow read and write scope from any of your BigQuery connections, follow these steps:

  1. Navigate to the [Admin settings - General settings ](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings) page.
  2. Toggle the **Force BigQuery Readonly Scope usage** setting to "Enabled" and click **Update**.



This process does not sign your users back in to BigQuery. Your users will be prompted to sign in to BigQuery the next time they run a query that is based on a model with a BigQuery connection. Any schedules that are dependent on these connections will fail until the user signs in. You can also [reassign a schedule](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule#reassign_a_schedule) to yourself or another user who has already reauthorized their OAuth connection credentials.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
