---
url: https://docs.cloud.google.com/alloydb/docs/pgaudit/about/
title: About pgAudit \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:01.201887+00:00
---

# About pgAudit  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/pgaudit/about/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  About pgAudit Stay organized with collections  Save and categorize content based on your preferences. 

The open-source pgAudit extension in AlloyDB for PostgreSQL lets you selectively record and track SQL operations performed against your databases. Detailed session and object audit logs help you monitor database activity and meet government, financial, and ISO compliance requirements.

## Overview

Database auditing in AlloyDB is available through the pgAudit extension, which monitors and records a configurable subset of executed SQL commands and queries. In contrast, [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) records administrative and maintenance operations performed on an AlloyDB instance, as described in [Monitor access using audit logs](https://docs.cloud.google.com/alloydb/docs/audit-logging).

**Important:** AlloyDB uses an asynchronous managed pipeline to process user generated audit logs. Records are temporarily buffered on the instance's local storage before being securely forwarded to Cloud Logging. This local buffering provides high-performance logging, but it consumes temporary disk space on the instance. For more information, see Limitations.

## Limitations

The following limitations apply to the pgAudit functionality:

  * Creation and processing of audit log records is asynchronous. You might experience a small delay before audit records are available in Cloud Logging. You can monitor the current size of the pending audit data, which can indicate the extent of the delay, using the `alloydb.googleapis.com/node/database/logging/audit/backlog_bytes_count` metric in Cloud Monitoring. For more information, see [Monitor audit log pipeline status](https://docs.cloud.google.com/alloydb/docs/pgaudit/view-audit-log#monitor-audit-log-pipeline-status).

  * When pgAudit is enabled and configured, the creation rate of audit log records depends on your configuration and workload activity.

  * The system is designed to support a maximum log ingestion rate of 90 MiB per second.

  * When log generation rate exceeds the platform's ingestion capacity, logs are buffered locally. Sustained backpressure can result in the following:

    * Higher latency between audit events and records visible in Cloud Logging.
    * Instance restarts or crashes resulting from local disk space exhaustion.
    * Intermittent gaps in processed and persisted audit log trails.
  * The maximum size for a single audit record is 1MB.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
