---
url: https://docs.cloud.google.com/database-migration/docs/postgres/set-up-cascading-replica/
title: Set up cascading read replicas for a Cloud SQL destination instance \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:25.597323+00:00
---

# Set up cascading read replicas for a Cloud SQL destination instance  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/set-up-cascading-replica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Set up cascading read replicas for a Cloud SQL destination instance Stay organized with collections  Save and categorize content based on your preferences. 

After you migrate your data to a Cloud SQL destination instance, with Database Migration Service, you can set up cascading read replicas for your destination instance. [ Cascading read replicas](https://docs.cloud.google.com/sql/docs/postgres/replication#cascading-replicas) let you create a read replica under a Cloud SQL read replica in the same or different region before promoting your instance to primary. You can add up to four levels of cascading read replicas, including the primary instance.

## Set up cascading read replicas

To migrate your data to a Cloud SQL destination that is using cascading read replicas:

  1. Perform the standard migration process, but don't promote the migration job when it reaches the CDC phase. For more information, see [ Get started with homogeneous PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).

  2. Once in the CDC phase, you can set up your cascading read replica. For information about how to create cascading read replicas for a Cloud SQL destination instance, see [ Set up a cascading replica](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-replication-from-external#set_up_a_cascading_replica).

  3. You can promote your Cloud SQL replica to a primary instance using Database Migration Service. For information about promoting a destination instance, see [ Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).




When you promote the Cloud SQL replica to a primary instance, the replica's cascading replica hierarchy is retained.

## What's next

To get a complete, step-by-step migration walkthrough, see [ Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
