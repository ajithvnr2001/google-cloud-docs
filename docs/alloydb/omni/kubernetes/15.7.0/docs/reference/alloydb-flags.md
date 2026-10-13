---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/alloydb-flags/
title: AlloyDB flags \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:41.679258+00:00
---

# AlloyDB flags  |  AlloyDB Omni for Kubernetes: 15.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/alloydb-flags/

This page documents AlloyDB Omni version **15.7.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/choose-compatible-versions)



Send feedback 

#  AlloyDB flags Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.0keyboard_arrow_down

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



This page describes the database flags that AlloyDB for PostgreSQL uses to enable and manage various service features unique to AlloyDB. For a list of all database flags that AlloyDB supports, see [Supported database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/database-flags).

Flags marked with **Instance restarts** mean that AlloyDB restarts an instance whenever you set, remove, or modify this flag on that instance. The flag's value persists for the instance until you modify it again.

### alloydb.enable_pgaudit

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `pgaudit` extension in an AlloyDB instance. Set the parameter to `on` and restart the instance. Then add the `pgaudit` extension to individual databases in the instance by using the `CREATE EXTENSION` command.

The [`pgaudit`](https://www.pgaudit.org/) extension provides detailed session and object audit logging using the standard logging facility provided by PostgreSQL.

**Warning:** In AlloyDB Omni only, enabling this extension and the PostgreSQL `logging_collector` parameter might result in loss of audit logs. To enable the PostgreSQL and audit logs, set `logging_collector` to `off` and `alloydb.enable_pgaudit` to `true`. To enable the PostgreSQL log, set `logging_collector` to `on` and `allobydb.enable_pgaudit` to `false`. 

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
