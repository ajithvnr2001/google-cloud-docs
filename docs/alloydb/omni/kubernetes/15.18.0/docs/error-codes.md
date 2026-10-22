---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/error-codes/
title: Diagnose error codes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.18.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:24.519417+00:00
---

# Diagnose error codes  |  AlloyDB Omni using the container orchestrator: 15.18.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/error-codes/

This page documents AlloyDB Omni version **15.18.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/overview)



Send feedback 

#  Diagnose error codes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.18.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/error-codes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/error-codes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/error-codes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/error-codes)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/error-codes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/error-codes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/error-codes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/error-codes)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/error-codes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/error-codes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/error-codes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/error-codes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/error-codes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/error-codes)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/error-codes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/error-codes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/error-codes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/error-codes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/error-codes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/error-codes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/error-codes)

This page describes AlloyDB Omni error codes and recommended fixes. 

## Extract an error

To extract an error code, follow these steps:

  1. To get your database cluster manifest, run:
         
         kubectl get dbclusters.a DB_CLUSTER_NAME -n DB_CLUSTER_NAMESPACE -o yaml

Replace the following:

     * `DB_CLUSTER_NAME`: the name of your database cluster—for example, `my-db-cluster`.
     * `DB_CLUSTER_NAMESPACE`: the name of the namespace of your database cluster.
  2. Check for database cluster status conditions and `criticalincidents` fields that might have some of the following error codes.




## AlloyDB Omni error codes

Error code | Description | Recommended action  
---|---|---  
`DBSE0601.PgBackRest: Failed to backup` | AlloyDB Omni uses [pgBackRest](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/set-up-pgbackrest) for its backup and restore related features.  
This error can occur on a backup resource when pgBackRest failed to take the requested backup. | If it occurs, check the following logs for more information:  
pgBackRest backup logs on the `obs` disk of the database Pod in the `/obs/pgbackrest/db-backup.log directory`  
  
PostgreSQL database logs on the `obs` disk of the database Pod in the `/obs/diagnostic/postgresql.log directory`.  
`DBSE0604.pgBackRest: Failed to restore` | AlloyDB Omni uses [pgBackRest](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/set-up-pgbackrest) for its backup and restore related features.  
This error can occur on a restore resource when pgBackRest failed to restore. | If it occurs, check the following logs for more information:  
* pgBackRest restore logs on the `obs` disk of the database Pod in the `/obs/pgbackrest/db-restore.log` directory.  
  
* PostgreSQL database logs on the `obs` disk of the database Pod in the `/obs/diagnostic/postgresql.log` directory.  
`DBSE1080. HA: Failed to stop primary database` | This error occurs when the primary database fails to stop properly.   
This can be because the database is not responsive, or it might have timed out waiting for the database to finish stopping. | If this occurs during a failover, the failover operation attempts to continue to promote a new primary database.  
If the issue persists, you may need to manually repair or recreate the database.  
`DBSE1081. Failed to promote standby database` | This error can occur during a failover or switchover when attempting to promote a standby database.   
Check the error message for more details. | If this occurs, the failover or switchover operation attempts to roll back to the old primary database.   
If the rollback fails, you may need to manually repair, restart, or recreate this database cluster.  
`DBSE1082. Failed to rewind the database` | This error can occur during an operation that tries to change a primary database into a standby database.   
Check the error message for more details. | If this occurs during a failover or switchover operation, AlloyDB Omni attempts to roll back to the old primary database.   
If the rollback fails, you may need to manually repair, restart, or recreate the database cluster.  
`DBSE2411. PostgreSQL: Failed to create physical replication slot` | This error can occur on an upstream instance when trying to set up downstream replication.   
Check the error message for additional details. | If the error persists, you might need to restart the replication setup process.  
`DBSE2412. PostgreSQL: Failed to query replication slots` | This error can occur on an upstream instance. | Check the error message for additional details on what caused the error.  
`DBSE2413. PostgreSQL: Failed to reload config` | This error can occur when a database parameter has been changed and is unable to reload. | Check the error message for more details.   
If the message indicates that a specific parameter causes the error, then you might need to change the parameter.  
`DBSE2414. PostgreSQL: Failed to run pg_basebackup` | This error occurs during the replication setup for a new downstream instance. | Check the error message for additional details.   
If the error persists, you might need to manually delete this instance and restart the replication process.  
`DBSE2415. PostgreSQL: failed to connect to database` | This error occurs when the operator agent is unable to connect to the database. | The most likely reason is that the database is shut down or has crashed.   
Read the error message for more details.  
`DBSE2416. PostgreSQL: Failed to set synchronous standby names` | This error can occur on an upstream instance when setting up a replication.   
If synchronous standby names have not been set correctly, then standby names are asynchronous. | Check the error message for more details.   
If the issue persists, you might need to disable and then re-enable the replication.  
`DBSE2417. PostgreSQL: Failed to terminate replication` | This error can occur on an upstream instance if a downstream instance has changed, for example, the number of standbys is reduced. | Check the error message for more details.   
If the issue persists, you might need to disable and then re-enable the replication.  
`DBSE2418. PostgreSQL: Failed to drop replication slot` | This error can occur on an upstream instance if a downstream instance has changed, for example, the number of standbys is reduced. | Check the error message for more details.   
If the issue persists, you might need to disable and then re-enable the replication.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
