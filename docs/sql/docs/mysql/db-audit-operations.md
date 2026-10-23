---
url: https://docs.cloud.google.com/sql/docs/mysql/db-audit-operations/
title: Supported operations \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:55.300281+00:00
---

# Supported operations  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/db-audit-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Supported operations Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page shows all the operations you can use for the `ops` audit log setting.

## Operation groups

The following is a list of operation groups and each operation in the group supported by MySQL database auditing.

Operation groups | Operations included  
---|---  
`call` | `call_procedure`  
`dcl` | `grant`, `revoke`, `revoke_all`  
`ddl` |  `alter_db`, `alter_event`, `alter_function`, `alter_procedure`, `alter_table`, `alter_user`, `create_db`, `create_event`, `create_function`, `create_index`, `create_procedure`, `create_table`, `create_trigger`, `create_udf`, `create_user`, `create_view`, `drop_db`, `drop_event`, `drop_function`, `drop_index`, `drop_procedure`, `drop_table`, `drop_trigger`, `drop_user`, `drop_view`, `rename_table` `rename_user`  
`dml` |  `delete`, `delete_multi`, `insert`, `insert_select`, `load`, `replace`, `replace_select`, `truncate`, `update`, `update_multi`  
`dql` | `select`  
`show` |  `show_binlog_events`, `show_create_event`, `show_create_func`, `show_create_proc`, `show_events`, `show_function_code`, `show_grants`, `show_procedure_code`, `show_relaylog_events`, `show_triggers`  
  
## Operations

The following are the operations supported by MySQL database auditing.

` alter_db ` |  ` create_trigger ` |  ` drop_user ` |  ` show_create_event `  
---|---|---|---  
` alter_event ` |  ` create_udf ` |  ` drop_view ` |  ` show_create_func `  
` alter_function ` |  ` create_user ` |  ` grant ` |  ` show_create_proc `  
` alter_procedure ` |  ` create_view ` |  ` insert ` |  ` show_create_trigger `  
` alter_table ` |  ` delete ` |  ` insert_select ` |  ` show_events `  
` alter_user ` |  ` delete_multi ` |  ` load ` |  ` show_function_code `  
` call_procedure ` |  ` disconnect ` |  ` rename_table ` |  ` show_grants `  
` connect ` |  ` drop_db ` |  ` rename_user ` |  ` show_procedure_code `  
` create_db ` |  ` drop_event ` |  ` replace ` |  ` show_relaylog_events `  
` create_event ` |  ` drop_function ` |  ` replace_select ` |  ` show_triggers `  
` create_function ` |  ` drop_index ` |  ` revoke ` |  ` truncate `  
` create_index ` |  ` drop_procedure ` |  ` revoke_all ` |  ` update `  
` create_procedure ` |  ` drop_table ` |  ` select ` |  ` update_multi `  
` create_table ` |  ` drop_trigger ` |  ` show_binlog_events ` |   
  
## What's next

  * Learn about [MySQL database auditing](https://docs.cloud.google.com/sql/docs/mysql/db-audit).
  * Learn about how to use [Use MySQL database auditing](https://docs.cloud.google.com/sql/docs/mysql/db-audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
