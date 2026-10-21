---
url: https://docs.cloud.google.com/database-migration/docs/postgres/set-up-cascading-replica/
title: Set up cascading read replicas for a Cloud SQL destination instance \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:40.154583+00:00
---

# Set up cascading read replicas for a Cloud SQL destination instance  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/set-up-cascading-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest)



Send feedback 

#  Set up cascading read replicas for a Cloud SQL destination instance Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/set-up-cascading-replica "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | PostgreSQL to AlloyDB

  


## Overview

Database Migration Service lets you migrate data to a Cloud SQL destination instance, and then set up cascading read replicas for that instance.

[Cascading read replicas](https://docs.cloud.google.com/sql/docs/postgres/replication#cascading-replicas) let you create a read replica under a Cloud SQL read replica in the same or different region before promoting your instance to primary. You can add up to four levels of cascading read replicas, including the primary instance.

## Set up cascading read replicas

To migrate your data to a Cloud SQL destination that is using cascading read replicas:

  1. Set up and start your migration job. For more information, see [Create a migration job](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job).

  2. Wait until the full dump phase of the job completes and the migration job enters the change data capture (CDC) phase. Your migration job is in the CDC phase when the **Status** column in the **Migration jobs** page indicates a _CDC_ substatus.

  3. Once in the CDC phase, you can set up your cascading read replica. For information about how to create cascading read replicas for a Cloud SQL destination instance, see [Set up a cascading replica](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#set_up_a_cascading_replica).

  4. You can promote your Cloud SQL replica to primary instance using Database Migration Service. For information about promoting a destination instance, see [Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).




When you promote the Cloud SQL replica to a primary instance, the replica's cascading replica hierarchy is retained.

[ Previous arrow_back  Verify a migration  ](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration)

[ Next Promote a migration  arrow_forward  ](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration)

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


