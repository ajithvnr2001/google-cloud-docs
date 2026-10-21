---
url: https://docs.cloud.google.com/dataproc-metastore/docs/transactional-tables/
title: Use transactional tables with Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:39:59.053830+00:00
---

# Use transactional tables with Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/transactional-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Use transactional tables with Dataproc Metastore Stay organized with collections  Save and categorize content based on your preferences. 

Transactions with ACID semantics are supported by [Apache Hive](https://hive.apache.org/) metastores in Dataproc Metastore. For more information, see [Hive Transactions](https://cwiki.apache.org/confluence/display/Hive/Hive+Transactions#HiveTransactions-ACIDandTransactionsinHive). These transactions are enabled by default on Hive 3.

**Note:** The `Enterprise` tier supports fully managed asynchronous compaction workflows, which are accessible through the [`Canary` release channel](https://docs.cloud.google.com/dataproc-metastore/docs/release-channel).

## Configurations

You must set server and client side configurations in order to enable transaction support.

**Note:** These configurations are set by default for Dataproc Metastore services created with Hive version 3.1.2.

### Server side configurations

The following server side configurations are set by default during the creation of the service by Dataproc Metastore. You can choose to override these by entering **Key** and **Value** overrides under **Metastore config overrides**.

**Caution:** Changing these configurations while creating a Hive 3 Dataproc Metastore service may result in unexpected errors or cause the service to not work correctly.

  * **`metastore.compactor.initiator.on`** — Whether to run the initiator and cleaner threads on the Dataproc Metastore service.

Set to `true` to enable the initiator.

  * **`metastore.compactor.worker.threads`** — The number of compactor worker threads to run on the Dataproc Metastore.

Set to a positive number to enable the compactor. Setting this to a higher number may affect the performance of the service, especially if you're on Developer tier. If this number needs to be tweaked, we recommend using a lower value, such as 8.

  * **`hive.metastore.event.db.notification.api.auth`** — Whether the Dataproc Metastore service should authorize against database notification related APIs.

Set to `false`. If set to `true`, then only the superusers in proxy settings have permission. See [Metastore notification API security](https://cwiki.apache.org/confluence/display/Hive/HiveReplicationv2Development#HiveReplicationv2Development-MetastorenotificationAPIsecurity) for more information on superuser proxy privilege.




### Client side configurations

Client side configurations are set in the Hive client as described in Validate transactions.

  * **`hive.support.concurrency`** — Set to `true` to support insert, update, and delete transactions.

  * **`hive.exec.dynamic.partition.mode`** — In strict mode, you must specify at least one static partition in case all partitions are accidentally overwritten. In nonstrict mode, all partitions are allowed to be dynamic.

Set to `nonstrict` to support insert, update, and delete transactions.

  * **`hive.txn.manager`** — Set to `org.apache.hadoop.hive.ql.lockmgr.DbTxnManager`.




## Validate transactions

You can validate Hive transactions using a Managed Service for Apache Spark cluster that uses a Dataproc Metastore service on Hive 3.

You must create the Managed Service for Apache Spark cluster in the same project as the Dataproc Metastore service and with Hive 3. The Managed Service for Apache Spark 2.0 images, 2.0-ubuntu18 and 2.0-debian10, support Hive 3 and transactions. You can use the flag `--image-version` to set the 2.0 image. For example:
    
    
    gcloud dataproc clusters create DATAPROC_CLUSTER_ID \
       --dataproc-metastore=projects/PROJECT_ID/locations/LOCATION/services/SERVICE \
       --region=REGION \
       --image-version 2.0-debian10
    

The following instructions demonstrate how to validate transactions in your Dataproc Metastore service that is used by a Managed Service for Apache Spark cluster.

  1. SSH into the Managed Service for Apache Spark cluster. You can do this from either a browser or from the command line.

  2. Run the command `hive` to open the Hive client:
         
         $> hive
         

  3. Set up the client side configurations to enable Hive ACID support for transactions in the hive client session:
         
         SET hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager;
         SET hive.support.concurrency=true;
         SET hive.exec.dynamic.partition.mode=nonstrict;
         

  4. Create a transactional table to insert and update into. The following is an example.

     1. Create a transaction table:
            
            create table student (id int, name string, age int)
            STORED AS ORC TBLPROPERTIES ('transactional' = 'true');
            

     2. Check if the table is transactional:
            
            describe formatted <tableName>;
            

A list of the table properties are printed. A transactional table has `transactional=true` in its table parameters.

     3. Insert data into the table:
            
            INSERT INTO student VALUES
            (1, 'Alice', 10),
            (2, 'Bob', 10),
            (3, 'Charlie', 10);
            

        1. Observe the delta folder created under the `student` directory in the warehouse directory of the service. Multiple delta folders are created if you run multiple insert or update statements.
     4. View which compactions are running and their statuses. Hive metastore runs a thread called initiator every five minutes to check for tables which are due for compaction and requests compaction for those tables.
            
            show compactions;
            

        1. To start a manual compaction (either minor or major):
               
               ALTER TABLE student COMPACT 'minor';
                 ALTER TABLE student COMPACT 'major';
                 ```
               




## What's next

  * [Create a service](https://docs.cloud.google.com/dataproc-metastore/docs/create-service)
  * [Update and delete a service](https://docs.cloud.google.com/dataproc-metastore/docs/manage-service)
  * [Import metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
