---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/verify-migration/
title: Verify a migration \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:28.884036+00:00
---

# Verify a migration  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/verify-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Verify a migration Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/verify-migration "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


## Verifying a migration

In this page, you confirm that the migration job migrated data from your source database instance to the destination AlloyDB database instance correctly. 

At a minimum, verify that the database instance and its tables exist in the AlloyDB instance. You can also verify the tables' row counts or exact contents. 

The following steps show a minimal example:

  1. Go to the [AlloyDB clusters page](https://console.cloud.google.com/alloydb) in the Google Cloud console.
  2. Click the read replica entry of your migration job.
  3. Click the **Activate Cloud Shell** icon that appears in the upper-right region of the page.
  4. At the Cloud Shell prompt, press **Enter**.
  5. Optional: If an **Authorize Cloud Shell** dialog box appears, then click **Authorize**.
  6. At the **Enter password** prompt, enter the password that you either provided or that Database Migration Service generated for you in [Define and create the destination AlloyDB instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job#dest).
  7. Run SQL commands to verify the migration. For example: 
     1. At the **postgres** prompt, enter `\list` to list the databases and verify that you see your source database instance.

     2. At the **postgres** prompt, enter `\connect SOURCE_DB_NAME`, and enter the password when prompted, to connect to the database instance and see the tables associated with the instance. The name of the prompt changes from `postgres` to SOURCE_DB_NAME.

     3. At the SOURCE_DB_NAME prompt, enter `\dt` to see the tables of this instance.

     4. At the SOURCE_DB_NAME prompt, enter `GRANT alloydbexternalsync to USER;` because you want to give this user permission to access the data in the tables of this instance. Also, replace USER with the name of the user you used to connect to the destination database instance.

     5. At the SOURCE_DB_NAME prompt, enter `SELECT * from TABLE_NAME;` to see the information that's replicated from a table in your source database instance.

     6. Verify that you see the correct information in the table.



If everything you check is as you expect, then Database Migration Service has migrated the data correctly.

[ Previous arrow_back  Manage migration jobs  ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions)

[ Next Promote a migration  arrow_forward  ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/promote-migration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


