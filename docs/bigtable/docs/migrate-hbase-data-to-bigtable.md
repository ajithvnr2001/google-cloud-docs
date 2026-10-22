---
url: https://docs.cloud.google.com/bigtable/docs/migrate-hbase-data-to-bigtable/
title: Migrate data from HBase to Bigtable offline \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:18.326609+00:00
---

# Migrate data from HBase to Bigtable offline  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/migrate-hbase-data-to-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback 

#  Migrate data from HBase to Bigtable offline Stay organized with collections  Save and categorize content based on your preferences. 

This page describes considerations and processes for migrating data from an Apache HBase cluster to a Bigtable instance on Google Cloud.

The process described on this page requires you to take your application offline. If you want to migrate with no downtime, see the guidance for online migration at [Replicate from HBase to Bigtable](https://docs.cloud.google.com/bigtable/docs/hbase-replication).

Before you begin this migration, you should consider performance implications, Bigtable schema design, your approach to authentication and authorization, and the Bigtable feature set.

## Pre-migration considerations

This section suggests a few things to review and think about before you begin your migration.

### Performance

Under a typical workload, Bigtable delivers highly predictable performance. Make sure that you understand the factors that affect [Bigtable performance](https://docs.cloud.google.com/bigtable/docs/performance) before you migrate your data.

### Bigtable schema design

In most cases, you can use the same schema design in Bigtable as you do in HBase. If you want to change your schema or if your use case is changing, review the concepts laid out in [Designing your schema](https://docs.cloud.google.com/bigtable/docs/schema-design) before you migrate your data.

### Authentication and authorization

Before you design access control for Bigtable, review the existing HBase authentication and authorization processes.

Bigtable uses Google Cloud's standard [mechanisms for authentication](https://docs.cloud.google.com/docs/authentication) and Identity and Access Management to provide access control, so you convert your existing authorization on HBase to IAM. You can map the existing Hadoop groups that provide access control mechanisms for HBase to different service accounts.

Bigtable allows you to control access at the project, instance, and table levels. For more information, see [Access Control](https://docs.cloud.google.com/bigtable/docs/access-control).

### Downtime requirement

The migration approach that is described on this page involves taking your application offline for the duration of the migration. If your business can't tolerate downtime while you migrate to Bigtable, see the guidance for online migration at [Replicate from HBase to Bigtable](https://docs.cloud.google.com/bigtable/docs/hbase-replication).

## Migrate HBase to Bigtable

To migrate your data from HBase to Bigtable, you export an HBase snapshot for each table to Cloud Storage and then import the data into Bigtable. These steps are for a single HBase cluster and are described in detail in the next several sections.

  1. Stop sending writes to your HBase cluster.
  2. Take snapshots of the HBase cluster's tables.
  3. Export the snapshot files to Cloud Storage.
  4. Compute hashes and export them to Cloud Storage.
  5. Create destination tables in Bigtable.
  6. Import the HBase data from Cloud Storage into Bigtable.
  7. Validate the imported data.
  8. Route writes to Bigtable.



### Before you begin

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store your snapshots. Create the bucket in the same [location](https://cloud.google.com/about/locations) that you plan to run your Dataflow job in.

  2. [Create a Bigtable instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) to store your new tables.

  3. Identify the Hadoop cluster that you are exporting. You can run the jobs for your migration either directly on the HBase cluster or on a separate Hadoop cluster that has network connectivity to the HBase cluster's Namenode and Datanodes.

  4. Install and configure the Cloud Storage connector on every node in the Hadoop cluster as well as the host where the job is initiated from. For detailed installation steps, see [Installing the Cloud Storage connector](https://github.com/GoogleCloudDataproc/hadoop-connectors/blob/master/gcs/INSTALL.md).

  5. Open a command shell on a host that can connect to your HBase cluster and your Bigtable project. This is where you'll complete the next steps.

  6. Get the Schema Translation tool:
         
         wget BIGTABLE_HBASE_TOOLS_URL
         

Replace `BIGTABLE_HBASE_TOOLS_URL` with the URL of the latest `JAR with dependencies` available in the tool's [Maven repository](https://repo1.maven.org/maven2/com/google/cloud/bigtable/bigtable-hbase-1.x-tools/). The file name is similar to `https://repo1.maven.org/maven2/com/google/cloud/bigtable/bigtable-hbase-1.x-tools/1.24.0/bigtable-hbase-1.x-tools-1.24.0-jar-with-dependencies.jar`.

To find the URL or to manually download the JAR, do the following:

     1. [Go to the repository.](https://search.maven.org/artifact/com.google.cloud.bigtable/bigtable-hbase-1.x-tools)
     2. Click the most recent version number.
     3. Identify the `JAR with dependencies file` (usually at the top).
     4. Either right-click and copy the URL, or click to download the file.
  7. Get the Import tool:
         
         wget BIGTABLE_BEAM_IMPORT_URL
         

Replace `BIGTABLE_BEAM_IMPORT_URL` with the URL of the latest `shaded JAR` available in the tool's [Maven repository](https://search.maven.org/artifact/com.google.cloud.bigtable/bigtable-beam-import). The file name is similar to `https://repo1.maven.org/maven2/com/google/cloud/bigtable/bigtable-beam-import/1.24.0/bigtable-beam-import-1.24.0-shaded.jar`.

To find the URL or to manually download the JAR, do the following:

     1. [Go to the repository.](https://search.maven.org/artifact/com.google.cloud.bigtable/bigtable-beam-import)
     2. Click the most recent version number.
     3. Click **Downloads**.
     4. Mouse over **shaded.jar**.
     5. Either right-click and copy the URL, or click to download the file.
  8. Set the following environment variables:
         
         #Google Cloud
         
         export PROJECT_ID=PROJECT_ID
         export INSTANCE_ID=INSTANCE_ID
         export REGION=REGION
         export CLUSTER_NUM_NODES=CLUSTER_NUM_NODES
         
         #JAR files
         
         export TRANSLATE_JAR=TRANSLATE_JAR
         export IMPORT_JAR=IMPORT_JAR
         
         #Cloud Storage
         
         export BUCKET_NAME="gs://BUCKET_NAME"
         export MIGRATION_DESTINATION_DIRECTORY="$BUCKET_NAME/hbase-migration-snap"
         
         #HBase
         
         export ZOOKEEPER_QUORUM=ZOOKEPER_QUORUM
         export ZOOKEEPER_PORT=2181
         export ZOOKEEPER_QUORUM_AND_PORT="$ZOOKEEPER_QUORUM:$ZOOKEEPER_PORT"
         export MIGRATION_SOURCE_DIRECTORY=MIGRATION_SOURCE_DIRECTORY
         

Replace the following:

     * `PROJECT_ID`: the Google Cloud project that your instance is in
     * `INSTANCE_ID`: the identifier of the Bigtable instance that you are importing your data to
     * `REGION`: a region that contains one of the clusters in your Bigtable instance. Example: `northamerica-northeast2`
     * `CLUSTER_NUM_NODES`: the number of nodes in your Bigtable instance
     * `TRANSLATE_JAR`: the name and version number of the `bigtable hbase tools` JAR file that you downloaded from Maven. The value should look something like `bigtable-hbase-1.x-tools-1.24.0-jar-with-dependencies.jar`.
     * `IMPORT_JAR`: the name and version number of the `bigtable-beam-import` JAR file that you downloaded from Maven. The value should look something like `bigtable-beam-import-1.24.0-shaded.jar`.
     * `BUCKET_NAME`: the name of the Cloud Storage bucket where you are storing your snapshots
     * `ZOOKEEPER_QUORUM`: the zookeeper host that the tool will connect to, in the format `host1.myownpersonaldomain.com`
     * `MIGRATION_SOURCE_DIRECTORY`: the directory on your HBase host that holds the data that you want to migrate, in the format `hdfs://host1.myownpersonaldomain.com:8020/hbase`
  9. (Optional) To confirm that the variables were set correctly, run the `printenv` command to view all environment variables.




### Stop sending writes to HBase

Before you take snapshots of your HBase tables, stop sending writes to your HBase cluster.

### Take HBase table snapshots

When your HBase cluster is no longer ingesting data, take a snapshot of each table that you plan to migrate to Bigtable.

A snapshot has a minimal storage footprint on the HBase cluster at first, but over time it might grow to the same size as the original table. The snapshot does not consume any CPU resources.

Run the following command for each table, using a unique name for each snapshot:
    
    
    echo "snapshot 'TABLE_NAME', 'SNAPSHOT_NAME'" | hbase shell -n
    

Replace the following:

  * `TABLE_NAME`: the name of the HBase table that you are exporting data from.
  * `SNAPSHOT_NAME`: the name for the new snapshot



### Export the HBase snapshots to Cloud Storage

After you create the snapshots, you need to export them. When you're executing export jobs on a production HBase cluster, monitor the cluster and other HBase resources to ensure that the clusters remain in a good state.

For each snapshot that you want to export, run the following:
    
    
    hbase org.apache.hadoop.hbase.snapshot.ExportSnapshot \
    -Dhbase.zookeeper.quorum=$ZOOKEEPER_QUORUM_AND_PORT -snapshot SNAPSHOT_NAME \
        -copy-from $MIGRATION_SOURCE_DIRECTORY \
        -copy-to $MIGRATION_DESTINATION_DIRECTORY/data
    

Replace `SNAPSHOT_NAME` with the name of the snapshot to export.

**Note:** If you need to limit the bandwidth that the export uses, use the `-mappers` parameter with an integer value for specifying how many mappers to run and the `-bandwidth` parameter with an integer value for MB/sec. For example, to limit the concurrency of copy map tasks to 20, set `-mappers 20` and to limit the bandwidth that each copy map task uses to 50 MB/sec, add `-bandwidth 50` to the command. This makes the total bandwidth 1,000 MB/sec (50 MB/sec * 20 mappers = 1,000 MB/sec).

### Compute and export hashes

Next, create hashes to use for validation after the migration is complete. HashTable is a validation tool provided by HBase that computes hashes for row ranges and exports them to files. You can run a `sync-table` job on the destination table to match the hashes and gain confidence in the integrity of migrated data.

Run the following command for each table that you exported:
    
    
    hbase org.apache.hadoop.hbase.mapreduce.HashTable --batchsize=32000 --numhashfiles=20 \
    TABLE_NAME $MIGRATION_DESTINATION_DIRECTORY/hashtable/TABLE_NAME
    

Replace the following:

  * `TABLE_NAME`: the name of the HBase table that you created a snapshot for and exported

**Note:** For bigger migrations where you're migrating multiple tables, you can run `ExportSnapshot` and `HashTable` jobs in parallel. This is possible because the export job is reading from disk, and the HashTable job is busy computing hashes and scanning HBase. This option can reduce the downtime required for the migration.

### Create destination tables

The next step is to create a destination table in your Bigtable instance for each snapshot that you exported. Use an account that has `bigtable.tables.create` permission for the instance.

This guide uses the [Bigtable Schema Translation tool](https://github.com/googleapis/java-bigtable-hbase/tree/master/bigtable-hbase-1.x-parent/bigtable-hbase-1.x-tools), which automatically creates the table for you. However, if you don't want your Bigtable schema to exactly match the HBase schema, you can [create a table](https://docs.cloud.google.com/bigtable/docs/managing-tables#creating_a_table) using the `cbt` command-line tool or the Google Cloud console.

The Bigtable Schema Translation tool captures the schema of the HBase table, including the table name, column families, garbage collection policies, and splits. Then it creates a similar table in Bigtable.

**Note:** If your HBase master is in a virtual private cloud or you can't connect to the internet, you can follow the [alternative instructions](https://github.com/googleapis/java-bigtable-hbase/blob/04768334a033325b490bbaf6f92c9c14a2a6f1f9/bigtable-hbase-1.x-parent/bigtable-hbase-1.x-tools/README.md#alternative-exporting-schema) instead of the instructions in this section. When you use the alternative instructions, you export the HBase schema to a file, and then use that file to create tables in Bigtable.

For each table that you want to import, run the following to copy the schema from HBase to Bigtable.
    
    
    java \
     -Dgoogle.bigtable.project.id=$PROJECT_ID \
     -Dgoogle.bigtable.instance.id=$INSTANCE_ID \
     -Dgoogle.bigtable.table.filter=TABLE_NAME \
     -Dhbase.zookeeper.quorum=$ZOOKEEPER_QUORUM \
     -Dhbase.zookeeper.property.clientPort=$ZOOKEEPER_PORT \
     -jar $TRANSLATE_JAR
    

Replace `TABLE_NAME` with the name of the HBase table that you are importing. The Schema Translation tool uses this name for your new Bigtable table.

You can also optionally replace `TABLE_NAME` with a regular expression, such as ".*", that captures all the tables that you want to create, and then run the command only once.

### Import the HBase data into Bigtable using Dataflow

After you have a table ready to migrate your data to, you are ready to import and validate your data.

#### Uncompressed tables

If your HBase tables are not compressed, run the following command for each table that you want to migrate:
    
    
    java -jar $IMPORT_JAR importsnapshot \
        --runner=DataflowRunner \
        --project=$PROJECT_ID \
        --bigtableInstanceId=$INSTANCE_ID \
        --bigtableTableId=TABLE_NAME \
        --hbaseSnapshotSourceDir=$MIGRATION_DESTINATION_DIRECTORY/data \
        --snapshotName=SNAPSHOT_NAME \
        --stagingLocation=$MIGRATION_DESTINATION_DIRECTORY/staging \
        --tempLocation=$MIGRATION_DESTINATION_DIRECTORY/temp \
        --maxNumWorkers=$(expr 3 \* $CLUSTER_NUM_NODES) \
        --region=$REGION
    

Replace the following:

  * `TABLE_NAME`: the name of the HBase table that you are importing. The Schema Translation tool gives uses this name for your new Bigtable table. New table names are not supported.
  * `SNAPSHOT_NAME`: the name that you assigned to the snapshot of the table that you are importing



After you run the command, the tool restores the HBase snapshot to your Cloud Storage bucket, then starts the import job. It can take several minutes for the process of restoring the snapshot to finish, depending on the size of the snapshot.

Keep the following tips in mind when you import:

  * To improve the performance of data loading, be sure to set `maxNumWorkers`. This value helps to ensure that the import job has enough compute power to complete in a reasonable amount of time, but not so much that it would overwhelm the Bigtable instance. 
    * If you are not also using the Bigtable instance for another workload, multiply the number of nodes in your Bigtable instance by 3, and use that number for `maxNumWorkers`.
    * If you are using the instance for another workload at the same time that you are importing your HBase data, reduce the value of `maxNumWorkers` appropriately.
  * Use the default worker type.
  * During the import, you should monitor the Bigtable instance's [CPU usage](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu). If the CPU utilization across the Bigtable instance is too high, you might need to add additional nodes. It can take up to 20 minutes for the cluster to provide the performance benefit of additional nodes.



For more information about monitoring the Bigtable instance, see [Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

#### Snappy compressed tables

If you are importing Snappy compressed tables, you need to use a [custom container image](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers) in the Dataflow pipeline. The custom container image that you use to import compressed data into Bigtable provides Hadoop native compression library support. You must have the Apache Beam SDK version 2.30.0 or later to use Dataflow Runner v2, and you must have version 2.3.0 or later of the HBase client library for Java.

To import Snappy compressed tables, run the same command that you run for uncompressed tables, but add the following option:
    
    
        --enableSnappy=true
    

### Validate the imported data in Bigtable

To validate the imported data, you need to run the `sync-table` job. The `sync-table` job computes hashes for row ranges in Bigtable, then matches them with the HashTable output that you computed earlier.

To run the `sync-table` job, run the following in the command shell:
    
    
    java -jar $IMPORT_JAR sync-table  \
        --runner=dataflow \
        --project=$PROJECT_ID \
        --bigtableInstanceId=$INSTANCE_ID \
        --bigtableTableId=TABLE_NAME \
        --outputPrefix=$MIGRATION_DESTINATION_DIRECTORY/sync-table/output-TABLE_NAME-$(date +"%s") \
        --stagingLocation=$MIGRATION_DESTINATION_DIRECTORY/sync-table/staging \
        --hashTableOutputDir=$MIGRATION_DESTINATION_DIRECTORY/hashtable/TABLE_NAME \
        --tempLocation=$MIGRATION_DESTINATION_DIRECTORY/sync-table/dataflow-test/temp \
        --region=$REGION
    

Replace `TABLE_NAME` with the name of the HBase table that you are importing.

When the `sync-table` job is complete, open the [Dataflow Job details](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf) page and review the **Custom counters** section for the job. If the import job successfully imports all of the data, the value for **`ranges_matched`** has a value and the value for **`ranges_not_matched`** is 0.

![Dataflow custom counters](https://docs.cloud.google.com/bigtable/img/custom-counters.png)

If **`ranges_not_matched`** shows a value, open the **Logs** page, choose **Worker Logs** , and filter by **Mismatch on range**. The machine-readable output of these logs is stored in Cloud Storage at the output destination that you create in the sync-table `outputPrefix` option.

![Dataflow worker logs](https://docs.cloud.google.com/bigtable/img/worker-logs.png)

You can try the import job again or write a script to read the output files to determine where the mismatches occurred. Each line in the output file is a [serialized JSON record](https://github.com/googleapis/java-bigtable-hbase/blob/6c3b151bc69349ff30deeb7a6c47770157940b58/bigtable-dataflow-parent/bigtable-beam-import/src/main/java/com/google/cloud/bigtable/beam/validation/HadoopHashTableSource.java#L66) of a mismatched range.

### Route writes to Bigtable

After you've validated the data for each table in the cluster, you can [configure your applications](https://docs.cloud.google.com/bigtable/docs/hbase-connecting) to route all their traffic to Bigtable, then deprecate the HBase instance.

When your migration is complete, you can delete the snapshots on your HBase instance.

## What's next

  * Learn more about [Cloud Storage](https://docs.cloud.google.com/storage/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
