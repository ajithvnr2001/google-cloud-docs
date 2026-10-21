---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/promote-migration/
title: Promote a migration \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:29.231043+00:00
---

# Promote a migration  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/promote-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Promote a migration Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/promote-migration "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


  
Promotion means that the destination AlloyDB for PostgreSQL instance is disconnected from the source, and is promoted from a replica instance to a primary instance. 

For continuous migrations, you can initiate the promotion process after it's time to move reads and writes to the destination.

To promote a migration without loss of information, follow these steps:

  1. Go to the [Migration jobs](https://console.cloud.google.com/dbmigration/migrations) page.
  2. Click the migration job that represents the migration that you want to promote. The **Migration job details** page appears.

After the full dump phase has completed and the migration job is in CDC phase, the option for promotion is available.

  3. Immediately after transitioning to the CDC phase, depending on the size of the dump, there may be a long replication delay because the AlloyDB for PostgreSQL destination instance catches up on changes that occurred during the dump and load.

Wait for the replication delay to trend down significantly, ideally on the order of minutes or seconds. The replication delay is available for review on the migration job page.

  4. After the replication delay is at a minimum, you can initiate the promotion. To avoid data loss, make sure to: 
     1. **Stop all writes, running scripts, and client connections to the source database**. The downtime period begins here.
     2. Wait until the replication delay is at zero, which means that the migration job has processed all outstanding changes.
You can promote a migration even if the replication delay isn't at zero. This can reduce the database downtime, but may affect the accuracy of the data in the destination.
  5. In the **Migration job details** page, click **Promote**.
  6. In the **Promote migration job?** window, click **Promote**.
  7. The migration job stops reading from the source and the substatus is `Promote in progress`. At this point, you cannot stop or undo the promotion process. 
  8. The destination instance is promoted to a primary writeable instance. The migration job status is `Completed`.
  9. The application can now be connected to the AlloyDB for PostgreSQL instance and the migration job can be safely deleted. 



When you promote migration jobs that have failed or were manually stopped during CDC phase, data on the source and the destination can be inconsistent.

[ Previous arrow_back  Verify a migration  ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/verify-migration)

[ Next Review connection profiles  arrow_forward  ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/review-connection-profiles)

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


