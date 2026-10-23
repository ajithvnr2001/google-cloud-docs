---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/database-inplace-major-version-upgrade-errors/
title: Database in-place major version upgrade errors \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:39.274687+00:00
---

# Database in-place major version upgrade errors  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/database-inplace-major-version-upgrade-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Database in-place major version upgrade errors Stay organized with collections  Save and categorize content based on your preferences. 

To resolve pre-upgrade check violations, extension incompatibilities, and resource limit errors when you perform an in-place major version upgrade in AlloyDB for PostgreSQL, apply the recommended fixes for the error messages that your upgrade operation returns. For general upgrade troubleshooting steps, see [Troubleshoot an in-place major version upgrade](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-database-inplace-major-version-upgrade).

## Common major version upgrade errors

The following sections describe the error messages that can occur during a major version upgrade and how to resolve them.

### Error: Database: database_name. extension_violation: DEPRECATED, action_required: DELETE_EXTENSION

**Description:** AlloyDB detects deprecated extension. The error indicates which extensions caused an error:
    
    
    database_name. extension_violation: DEPRECATED_EXTENSION, action_required: DELETE_EXTENSION."+" Query format to delete the extensions: `DROP EXTENSION {extension_name}; Violation list: [extensions]
    

**Recommended fix:** Delete the extension. The query format to delete an extension is `DROP EXTENSION {extension_name};`.

### Error: Database: database_name. extension_violation: INVALID_EXTENSION_VERSION, action_required: UPGRADE_EXTENSION

**Description:** AlloyDB detects invalid extension version.

**Recommended fix:** Upgrade the extension. The query format to upgrade an extension is `ALTER EXTENSION {extension_name} UPDATE TO {target_version};`.

### Error: Database: database_name contains pg_largeobject

**Description:** AlloyDB detects `pg_largeobject`.

**Recommended fix:** Remove `pg_largeobject` before upgrading the AlloyDB cluster.

### ERROR: out of shared memory

**Description:** If the instance has insufficient shared memory, you might see this error message. This error is more likely to occur if you have more than 10,000 tables.

**Recommended fix:** Before you start an upgrade, set the value of the [`max_locks_per_transaction`](https://docs.cloud.google.com/alloydb/docs/reference/database-flags#postgres-m) flag to approximately twice the number of tables in the instance. The instance is restarted when you change the value of this flag.

### ERROR: Insufficient connections

**Description:** If your instance has insufficient connection capacity, you might see this error message.

**Recommended fix:** We recommend that you increase the [`max_connections`](https://docs.cloud.google.com/alloydb/docs/reference/database-flags#postgres-m) flag value by the number of databases in your instance. When you change the value of this flag, the instance is restarted.

### Pre-upgrade checks are failing

**Description:** When you upgrade your AlloyDB cluster, your upgrade might fail due to pre-upgrade checks. Details about the violations are in the API response in the form of `logs_url`. You are directed to the Google Cloud console page where the logs are present.

**Recommended fix:** Based on the error message, see other errors listed earlier in this document to resolve the specific issue.

## What's next

  * [Troubleshoot an in-place major version upgrade](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-database-inplace-major-version-upgrade).
  * Learn how to [perform a database in-place major version upgrade](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
