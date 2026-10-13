---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/alloydb-flags/
title: AlloyDB flags \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:44.796892+00:00
---

# AlloyDB flags  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/alloydb-flags/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  AlloyDB flags Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/reference/alloydb-flags)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/alloydb-flags)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/alloydb-flags)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/alloydb-flags)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/alloydb-flags)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/alloydb-flags)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/alloydb-flags)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/alloydb-flags)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/alloydb-flags)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/alloydb-flags)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/alloydb-flags)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/alloydb-flags)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/alloydb-flags)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/alloydb-flags)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/alloydb-flags)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/alloydb-flags)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/alloydb-flags)



This page describes the database flags that AlloyDB for PostgreSQL uses to enable and manage various service features unique to AlloyDB. For a list of all database flags that AlloyDB supports, see [Supported database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/database-flags).

Flags marked with **Instance restarts** mean that AlloyDB restarts an instance whenever you set, remove, or modify this flag on that instance. The flag's value persists for the instance until you modify it again.

### alloydb.audit_log_line_prefix

Type| `string`  
---|---  
Default| `"%m [%p]: [%l-1] db=%d,user=%u`  
Instance restarts| Yes  
  
Controls information prefixed to each audit log line. If left blank, then no prefix is used.

### alloydb.enable_pgaudit

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `pgaudit` extension in an AlloyDB instance. Set the parameter to `on` and restart the instance. Then add the `pgaudit` extension to individual databases in the instance by using the `CREATE EXTENSION` command.

The [`pgaudit`](https://www.pgaudit.org/) extension provides detailed session and object audit logging using the standard logging facility provided by PostgreSQL.

### alloydb.iam_authentication

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables the use of Identity and Access Management (Identity and Access Management (IAM)) authentication with an AlloyDB instance.

### alloydb.logical_decoding

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables the PostgreSQL logical decoding infrastructure in an AlloyDB instance.

[Logical decoding](https://www.postgresql.org/docs/18/logicaldecoding.html) provides the infrastructure necessary to stream data modifications to external consumers.

**Note:** An automatic restart does not occur when you modify this parameter, and a manual restart of the database cluster is required for the change to take effect.

### alloydb.log_throttling_window

Type| `integer`  
---|---  
Default| `0`  
Instance restarts| No  
  
Controls whether AlloyDB records duplicate log messages received during a specified time window.

If set to a value greater than `0`, then AlloyDB starts a timer that many seconds long whenever it records a log message. If AlloyDB receives the identical log message before the timer expires, it does not record the message. After the timer expires, AlloyDB appends a count of any skipped messages to the next occurrence of the same log message that it records.

If set to `0`, then AlloyDB records all duplicate log messages.

### alloydb.promote_cancel_to_terminate

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
If set to `true`, then any query cancellation requests due to issues such as lock timeouts, statement timeouts, and recovery (replay) conflicts that AlloyDB encounters, are promoted to forced backend termination requests.

By promoting the cancellation requests, AlloyDB helps prevent stuck backends from blocking log replay and other backends.

### alloydb.pg_shadow_select_role

Type| `string`  
---|---  
Default| An empty string  
Instance restarts| No  
  
Name of the PostgreSQL role that is to be used to grant permission to query the `pg_shadow` view.

### alloydb_password

Type| `string`  
---|---  
Default| An empty string  
Instance restarts| No  
  
Provides functions to set and manage password policies for AlloyDB Omni. If your application's database users authenticate with AlloyDB Omni using the built-in, password-based method, then you can make authentication more secure by enforcing strong passwords.

For more information, see [Manage built-in authentication using password policies](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-password-policy).

### alloydb_scann

Type| `string`  
---|---  
Default| An empty string  
Instance restarts| No  
  
Provides functions that enable AlloyDB Omni to handle vector search workloads with high performance and efficiency.

For more information, see [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-index-query-vectors?resource=scann).

### alloydb_ai_nl

Type| `string`  
---|---  
Default| An empty string  
Instance restarts| No  
  
Provides functions that let you securely query AlloyDB using natural language. The extension works together with the parameterized_views` extension that enforces a security layer for your data.

For more information, see [Generate SQL queries using natural language](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/generate-sql-queries-natural-language).

### parameterized_views

Type| `string`  
---|---  
Default| An empty string  
Instance restarts| No  
  
Provides functions that add a security layer when natural language queries are translated to SQL queries. This extension works together with the `alloydb_ai_nl` extension.

For more information, see [Generate SQL queries using natural language](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/generate-sql-queries-natural-language).

### alloydb_ai_nl.enabled

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls whether the AlloyDB AI natural language features are enabled.

### scann.enable_preview_features

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables the use of the following features that are available in [Preview](https://cloud.google.com/products#product-launch-stages):

* [Deferred index creation](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-scann-index#deferred-index-creation-for-empty-or-nearly-empty-tables) defers index creation for empty rows or tables with insufficient rows. * [Four-level tree indexes](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-scann-index#create-scann-index-granular) support tables with more than one billion vector rows. 

### scann.enable_index_with_insufficient_data

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Controls whether deferred index creation is explicitly enabled for empty tables or tables with insufficient rows, without enabling other preview features. For more information, see [Deferred index creation](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-scann-index#deferred-index-creation-for-empty-or-nearly-empty-tables).

### scann.max_allowed_num_levels

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type | `integer`  
---|---  
Default | `2`  
Minimum value | `1`  
Maximum value | `3`  
Instance restarts | No  
  
Determines the highest value you can set for [`max_num_levels`](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/scann-index-reference) when [creating a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/create-scann-index#create-scann-index-granular).

### parameterized_views.enabled

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls whether the parameterized view features are enabled.

The `parameterized_views.enabled` flag setting isn't replicated automatically and must be replicated manually on each instance. You must enable the `parameterized_views.enabled` flag on each replica instance before you query parameterized views on the replica. For more information, see [Manage application data security using AlloyDB Omni parameterized secure views](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-application-data-security-parameterized-secure-views#before-you-begin).

### parameterized_views.json_results_max_rows

Type| `integer`  
---|---  
Default| `1,000,000`  
Instance restarts| No  
  
Sets the maximum number of rows for JSON results from the [`execute_parameterized_query()`](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-application-data-security-parameterized-secure-views#create-parameterized-secure-view) function.

### parameterized_views.json_results_max_size

Type| `integer`  
---|---  
Default| `1,048,576`  
Instance restarts| No  
  
Sets the maximum JSON results size in kilobytes (KB) from the [`execute_parameterized_query()`](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage-application-data-security-parameterized-secure-views#create-parameterized-secure-view) function.

### parameterized_views.max_parallel_workers_per_gather

Type| `integer`  
---|---  
Default| `-1`  
Instance restarts| No  
  
Sets the maximum number of parallel processes per executor node when a query is run using the parameterized views API. `-1` means no limit. This limit applies only if it's more restrictive than `max_parallel_workers_per_gather`.

### parameterized_views.statement_timeout

Type| `integer`  
---|---  
Default| `0`  
Instance restarts| No  
  
Sets the maximum allowed duration in milliseconds of statements run using the parameterized views API. `0` means no limit. This limit applies only if it's more restrictive than `statement_timeout`.

### parameterized_views.temp_file_limit

Type| `integer`  
---|---  
Default| `-1`  
Instance restarts| No  
  
Limits the total size in kB of all temporary files used by each process when run using the parameterized views API. `-1` means no limit. This limit applies only if it's more restrictive than `temp_file_limit`.

### parameterized_views.work_mem

Type| `integer`  
---|---  
Default| `0`  
Instance restarts| No  
  
Sets the maximum memory in kB to be used for query workspaces when it's run using the parameterized views API. `0` means no limit. This limit applies only if it's more restrictive than `work_mem`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
