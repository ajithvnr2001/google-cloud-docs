---
url: https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/
title: Create and run a MySQL migration job containing metadata with a DEFINER clause \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:15.066101+00:00
---

# Create and run a MySQL migration job containing metadata with a DEFINER clause  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/mysql-definer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Create and run a MySQL migration job containing metadata with a DEFINER clause Stay organized with collections  Save and categorize content based on your preferences. 

A MySQL migration job [ doesn't migrate user accounts and logins](https://docs.cloud.google.com/database-migration/docs/mysql/migration-fidelity). Sources that contain metadata defined by users with the `DEFINER` clause fail when invoked on the new Cloud SQL replica, because the users don't yet exist there.

To identify which `DEFINER` values exist in your metadata, query your MySQL source database. Check the results for entries for either `root%localhost` or for users that don't exist in the destination instance:
    
    
    SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.EVENTS WHERE EVENT_SCHEMA NOT 
    IN ('mysql', 'sys');
    SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_SCHEMA NOT 
    IN ('mysql', 'sys');
    SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.TRIGGERS WHERE TRIGGER_SCHEMA NOT 
    IN ('mysql', 'sys');
    SELECT DISTINCT DEFINER FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA NOT 
    IN ('mysql', 'sys');
    

To run a migration job from a source that includes such metadata, do one of the following:

  1. Create the users on the destination Cloud SQL replica instance before starting your migration job.

     1. To create a draft migration job without starting it, select **Create** instead of **Create & Start**.

     2. On your destination Cloud SQL instance, recreate the users from your source MySQL instance by using the Cloud SQL API or the Google Cloud console.

     3. From the list of migration jobs or the page for the specific job, start the migration job.

  2. Update the `DEFINER` clause to `INVOKER` on your source MySQL instance prior to setting up your migration job.


**Caution:** If `'root'@'localhost'` created your metadata, the migration fails. Change the definer to a different user before starting the migration job.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
