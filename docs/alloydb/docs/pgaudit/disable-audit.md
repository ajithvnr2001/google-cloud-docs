---
url: https://docs.cloud.google.com/alloydb/docs/pgaudit/disable-audit/
title: Disable pgAudit \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:07.034618+00:00
---

# Disable pgAudit  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/pgaudit/disable-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Disable pgAudit Stay organized with collections  Save and categorize content based on your preferences. 

To disable pgAudit on an AlloyDB instance, set the value of the `alloydb.enable_pgaudit` flag to `off`. You can change the value of the `alloydb.enable_pgaudit` flag through the Google Cloud console or the gcloud command.

To disable the `alloydb.enable_pgaudit` flag, use the standard instructions as described in [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

When you disable the `alloydb.enable_pgaudit` flag, audit logging stops immediately. However, it saves the applied pgAudit settings such as the pgaudit.log parameter settings.

**Note:** The instance automatically restarts when you update the `alloydb.enable_pgaudit` flag. 

Additionally, run the `DROP EXTENSION` command by using a compatible `psql` client to remove the extension state.

You disable an extension by reversing the procedure used to enable it.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  1. Connect a `psql` client to the cluster's primary instance, as described in [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql). 
  2. At the `psql` command prompt, connect to the database that has the extension enabled and drop the extension: 
         
         \c DB_NAME
             DROP EXTENSION pgaudit;
             

  3. Repeat the previous two steps to connect to other databases and create the extension in each one of them. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
