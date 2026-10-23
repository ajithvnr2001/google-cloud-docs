---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-database-inplace-major-version-upgrade/
title: Troubleshoot an in-place major version upgrade \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:38.634441+00:00
---

# Troubleshoot an in-place major version upgrade  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-database-inplace-major-version-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot an in-place major version upgrade Stay organized with collections  Save and categorize content based on your preferences. 

To diagnose and resolve issues that occur during an in-place major version upgrade of your AlloyDB for PostgreSQL cluster, identify the failed upgrade stage in the operation response and address any pre-upgrade check violations. For step-by-step upgrade instructions, see [Upgrade a database in-place major version](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version). For specific error messages and workarounds, see [Database in-place major version upgrade errors](https://docs.cloud.google.com/alloydb/docs/troubleshoot/database-inplace-major-version-upgrade-errors).

AlloyDB validates your request synchronously and returns an error message if any of the following are true:

  * Request is invalid. For example, if the provided target major version isn't supported or is less than or equal to the current major version.
  * The cluster resources are in a state in which the major version upgrade can't be triggered. For example, if the cluster or any of the associated instances aren't in a `READY` state.



If the request is valid, the upgrade might fail due to the following reasons:

  * Pre-upgrade checks performed at various stages can fail, which indicates that violations are detected. You must address these violations before you restart the upgrade.
  * Internal errors mean that you need to retry the upgrade. If retries fail, contact [Google Cloud Support](https://cloud.google.com/support).



## AlloyDB pre-upgrade check failures

Pre-upgrade check failures can happen during any of the following stages:

  * AlloyDB pre-upgrade checks (`ALLOYDB_PRECHECK`)
  * `pg_upgrade` checks (`PG_UPGRADE_CHECK`)
  * Primary cluster upgrades (`PRIMARY_INSTANCE_UPGRADE`)



_Pre-upgrade check failures_ are issues that AlloyDB detects during the pre-upgrade validation phase, which can cause the in-place major version upgrade to fail. For example, AlloyDB checks for extension incompatibilities between the current and target major version.

Error messages are populated in the `logs_url` in the upgrade operation response. You can view these logs by navigating to [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) in the Google Cloud console. For more information, see [View upgrade logs](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version#view-upgrade-logs).

To view the failures and the corresponding error messages that you might see in the logs, see [Database in-place major version upgrade errors](https://docs.cloud.google.com/alloydb/docs/troubleshoot/database-inplace-major-version-upgrade-errors).

The following is an example of the summary that's generated in the logs by AlloyDB pre-upgrade checks:
    
    
    Total number of databases checked for custom checks: 3
    Total number of databases containing pg_largeobject: 0
    Total number of databases containing event triggers permissions issue: 0
    Total number of databases containing extensions compatibility violation: 1
    Total number of databases containing search path violations: 0
    

## pg_upgrade check failures

`PG_UPGRADE_CHECK` checks for violations using the standard `pg_upgrade` utility. This upgrade check includes data inconsistencies that arise from various factors, including differences in version-specific data structures, alterations in encoding and collation, modifications to data types, and adjustments to the system catalog.

Multiple files –like `tables_with_oids.txt` and `tables_using_reg.txt`, which are generated during `pg_upgrade`– are exported to the `postgres_upgrade` log file. You can filter these files using the label `labels.FILE_NAME`.

Filenames that might contain errors to resolve include the following:

**Filename** | **Description**  
---|---  
` tables_with_oids.txt ` | This file contains tables that are listed with object identifiers (OIDs). Delete the tables or modify them so that they don't use OIDs.  
` tables_using_composite.txt ` | This file contains tables that are listed using system-defined composite types. Delete the tables or modify them so that they don't use these composite types.  
` tables_using_unknown.txt ` | This file contains tables that are listed using the `UNKNOWN` data type. Delete the tables or modify them so that they don't use this data type.  
` tables_using_sql_identifier.txt ` | This file contains tables that are listed using the `SQL_IDENTIFIER` data type. Delete the tables or modify them so that they don't use this data type.  
` tables_using_reg.txt ` | This file contains tables that are listed using the `REG*` data type –for example, `REGCOLLATION` or `REGNAMESPACE`. Delete the tables or modify them so that they don't use this data type.  
` postfix_ops.txt ` | This file contains tables that are listed using `postfix` (right-unary) operators. Delete the tables or modify them so that they don't use these operators.  
  
## pg_upgrade failures

The structure of `PG_UPGRADE` logs is similar to the structure of `PG_UPGRADE_CHECK` logs.

The following is an example of a log with the label `labels.FILE_NAME=pg_upgrade_dump*.log:`
    
    
    pg_upgrade_dump: error: query failed: [ERROR: out of shared memory](https://docs.cloud.google.com/alloydb/docs/troubleshoot/database-inplace-major-version-upgrade-errors)
    HINT: You might need to increase max_locks_per_transaction.
    

### What's next

  * Learn about [database in-place major version upgrade errors](https://docs.cloud.google.com/alloydb/docs/troubleshoot/database-inplace-major-version-upgrade-errors).
  * Learn how to [perform a database in-place major version upgrade](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
