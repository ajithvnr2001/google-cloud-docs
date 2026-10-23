---
url: https://docs.cloud.google.com/datastream/docs/sources-servicenow/
title: Stream data from ServiceNow instances \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:30.511727+00:00
---

# Stream data from ServiceNow instances  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-servicenow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from ServiceNow instances Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Connecting a ServiceNow instance to Datastream lets you replicate historical data and incremental changes for analytics and data integration. ServiceNow is a cloud-based platform that helps organizations manage and automate enterprise operations.

Before you set up a ServiceNow source in Datastream, review the key terms, replication behavior, supported versions, replicated objects, and known limitations.

## Key terms

ServiceNow operates using tables, records, and fields:

  * A **ServiceNow instance** is a dedicated, isolated ServiceNow cloud environment, for example, `company.service-now.com`.
  * A **table** is a primary data structure in ServiceNow, equivalent to a database table.
  * A **record** is an individual entry in a table, equivalent to a row in a database.
  * A **field** is an individual data element within a record, equivalent to a database column.
  * The connector uses the **Table API** as the primary RESTful interface to access data directly from ServiceNow tables.
  * **Offset-based pagination** is a method of navigating through records in a ServiceNow table by passing an offset number to the Table API. This method is sensitive to record deletions during pagination, which can cause the connector to skip data.
  * **Keyset-based pagination** is a method where the connector manages pagination by tracking unique record values, such as identifiers or timestamps, and their order. This method is effective even if there are record deletions during pagination.



## Behavior

The ServiceNow source support in Datastream relies on the ServiceNow REST Table API. Datastream supports two primary replication methods to ensure data integrity and performance.

### Historical backfill

  * When replicating change data from a ServiceNow instance, Datastream performs a full historical synchronization of all existing records in a table.
  * To ensure data consistency and prevent record loss during large extractions, the connector uses keyset-based pagination. The connector manages this process by tracking unique record values and their order, which makes the extraction robust to record deletions and prevents the connector from skipping or duplicating records.
  * Datastream sorts data by `sys_updated_on` and `sys_id` record properties to provide a stable order for the initial load. For the `sys_journal_field` table, which contains immutable records and lacks a `sys_updated_on` field, the connector sorts by `sys_created_on` and `sys_id` properties.



### Incremental synchronization

  * When replicating change data from a ServiceNow instance, Datastream captures changes, such as inserts and updates, that occur after the initial backfill.
  * Server-side incremental synchronization: the connector queries the ServiceNow API for records modified since the last successful synchronization using a filter on the `sys_updated_on` and `sys_id` properties (or `sys_created_on` and `sys_id` for the `sys_journal_field` table).
  * The synchronization process uses a compound cursor consisting of `sys_updated_on` (or `sys_created_on` for the `sys_journal_field` table) and `sys_id` markers. The `sys_updated_on` and `sys_created_on` markers ensure that only records with a timestamp equal to or later than a specified time are synchronized in the next cycle, while the `sys_id` marker ensures consistency for records with equal timestamps.



## Versions

The ServiceNow connector works with the ServiceNow REST [Table API (V2)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0551763). The functionality that Datastream supports is validated against the **Zurich** release.

## Objects replicated

The ServiceNow connector uses a dynamic discovery mechanism to identify the entire set of tables (objects) within an instance. To ensure that you replicate only high-value business data, the connector applies a multi-layered filtering process to exclude internal architecture, technical logs, and system metadata tables.

### Filtering logic

  * **Web service access** : you can only replicate tables that you explicitly configure with Web Services Access enabled (`ws_access=true`). If this configuration is missing, the connector can't retrieve record data from the table.
  * **Excluded superclasses** : the connector excludes tables that inherit from the `sys_metadata` system configuration table or are part of a rotated table hierarchy to prevent replicating technical metadata or inconsistent snapshots.
  * **Internal system prefix** : the connector filters out tables starting with specific technical prefixes representing platform plumbing or legacy features.
  * **The _Golden List_ (system exceptions)**: while the connector excludes most `sys_` tables, it explicitly allowlists critical business entities, such as `sys_user`, `sys_choice`, and `sys_journal_field`.



### System prefixes filtered by default

Category | Prefixes | Description  
---|---|---  
**Core internals** | `v_`, `ts_`, `imp_`, `ecc_`, `wf_`, `sh$`, `bin_`, `var_`, `gs_` | Virtual tables, search indexes, import staging, ECC queues, and workflow contexts.  
**Analytics & AI** | `pa_`, `ua_`, `ml_`, `ais_`, `promin_`, `di_` | Performance Analytics scores, vendor telemetry, ML vectors, and AI search profiles.  
**Technical modules** | `sa_`, `sla_`, `atf_`, `cxs_`, `automation_`, `ids_` | Service Mapping patterns, SLA engine logs, and security audit trails.  
**Legacy & admin** | `pf_`, `clone_`, `upgrade_`, `rollback_`, `expert_`, `dscy_` | Instance patching history, upgrade logs, and obsolete legacy modules.  
  
### Allowed system tables

  * **Users & security**: `sys_user`, `sys_user_group`, `sys_user_grmember`, `sys_user_role`, `sys_user_has_role`.
  * **Core reference** : `sys_choice` (drop-down options), `sys_company`, `sys_domain`, `sys_location`.
  * **Audit trails** : `sys_journal_field` (work notes and comments history).



## Known limitations

Known limitations for using ServiceNow as a source include:

  * Datastream doesn't support capturing deleted records.
  * Datastream excludes many internal platform tables by default, for example, tables starting with `ts_`, `v_`, or `imp_`.
  * You can only replicate tables that you explicitly configure with Web Services Access enabled (`ws_access=true`). This is the default for most tables.
  * The connector replicates field values in the way that they appear in the underlying ServiceNow database instance. These values are referred to as _actual values_. This means that the actual values that Datastream replicates to the destination might differ from the values displayed in the ServiceNow user interface (referred to as _display values_). For more information, see the [ServiceNow knowledge base](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0534905).



## What's next

  * Learn how to [configure a ServiceNow source](https://docs.cloud.google.com/datastream/docs/configure-servicenow) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
