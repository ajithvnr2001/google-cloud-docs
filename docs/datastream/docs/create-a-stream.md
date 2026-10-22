---
url: https://docs.cloud.google.com/datastream/docs/create-a-stream/
title: Create a stream \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:11.265146+00:00
---

# Create a stream  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/create-a-stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Create a stream Stay organized with collections  Save and categorize content based on your preferences. 

A stream in Datastream lets you replicate data and schema changes from a data source into [BigQuery](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4bigquery), Apache Iceberg tables, or a [Cloud Storage](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4cloudstorage) bucket. In the Google Cloud console wizard, you select connection profiles and choose which schemas, tables, or objects to replicate. You also configure historical backfill alongside ongoing replication.

Before starting replication, you can validate the stream to verify your source settings, confirm network connectivity to the destination, and check the end-to-end configuration.

## Before you begin

  * Make sure that you've set up your source database for replication. For information about steps required for each supported source type, see [Configure sources](https://docs.cloud.google.com/datastream/docs/sources).
  * Find out what steps might be required to set up your selected destination. For more information, see [Configure destinations](https://docs.cloud.google.com/datastream/docs/destinations).



## Define settings for the stream

  1. Go to the **Streams** page in the Google Cloud console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click **CREATE STREAM**.

  3. Use the following table to populate the fields of the **Define stream details** section of the **Create stream** page:

Field| Description  
---|---  
Stream name| Enter the display name of the stream.  
Stream ID| Datastream populates this field automatically based on the stream name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the stream is stored. Streams, like all resources, are saved in a region. Region selection doesn't impact whether your stream can connect to the source database or the destination, but can impact availability if the region experiences downtime. We recommend that you keep all resources for the stream in the same region as your source data to optimize cost and performance.  
Source type| Select the profile type that you specified when you created a connection profile for your source. Or, if you haven't created a connection profile for the source database, you can create one now.  
Destination type| Select the profile type that you specified when you created a connection profile for a [BigQuery](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4bigquery) or [Cloud Storage](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4cloudstorage) destination. Or, if you haven't created a connection profile for the destination, you can create one now.  
Encryption| By default, your data is encrypted with a key that's managed by Google Cloud. If you want to manage your encryption, then you can use a customer-managed encryption key (CMEK):
     1. Select the **Cloud KMS key** checkbox.
     2. From the **Key type** drop-down menu, select **Cloud KMS** and then select your CMEK.
If you don't see your key, then click **ENTER KEY RESOURCE NAME** to provide the resource name of the key that you want to use. For example, you can enter `projects/my-project-name/locations/my-location/keyRings/my-keyring/cryptoKeys/my-key` in the **Key resource name** field, and then click **SAVE**.  As part of creating the stream, Datastream will verify that the CMEK exists, and that Datastream has permissions to use the key. For more information about creating a CMEK or giving Datastream permissions for the key, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/datastream/docs/use-cmek).  
  4. Optionally, use labels to organize your Datastream resources.

     1. To create a label, click **ADD LABEL** , and then enter the key-value pair for the label.
     2. To remove the label, click the **trashcan** icon to the right of the row that contains the label.
**Note:** If your source is SQL Server, you can configure your stream to replicate columns added to the source schema after the stream is created by adding the `enable_ddl_support_for_ct` label. For more information, see [How Datastream handles DDL changes to the source schema](https://docs.cloud.google.com/datastream/docs/sources-sqlserver#add-columns).
  5. Optionally, add alerting policies for your stream. Alerting policies define when and how you want to be notified about stream failures.

     1. To create an alerting policy, click **Add alerting policy**.
     2. The **Create alerting policy** page appears in Cloud Monitoring. On this page, you define the alerting policy in case your stream fails.

For more information about alerting policies, see [Managing metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

  6. Review the required prerequisites that are generated automatically to reflect how the environment must be prepared for a stream. These prerequisites can include how to configure the source database and how to connect it to the destination. It's best to complete these prerequisites at this step, but you can complete them at any time before you test the stream or start it. For more information about these prerequisites, see [Sources](https://docs.cloud.google.com/datastream/docs/sources).

  7. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your source database type.

**Note:** If your source database type is Oracle, then the panel name is **Define Oracle connection profile**. If you select a different source database, then that database name appears in the panel name.



## Specify information about the source connection profile

  1. If you have created a source connection profile, then select it from the list of connection profiles.

If you haven't created a source connection profile, then create one by clicking **CREATE CONNECTION PROFILE** at the bottom of the drop-down list, and then perform the same steps as in [Create connection profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles).

  2. Click **RUN TEST** to verify that the source database and Datastream can communicate with each other.

If the test fails, then the issue associated with the connection profile appears. Refer to the [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues) page for troubleshooting steps. Make the necessary changes to correct the issue, and then retest.

  3. Click **CONTINUE**. The **Configure stream source** panel of the **Create stream** page appears.




## Configure information about the source database for the stream

#### Configure a PostgreSQL source database

  1. Define replication properties for your PostgreSQL source database. In the **Replication properties** section, specify the following properties:
     1. In the **Replication slot name** field, enter the name of the slot you created specifically for this stream. The database server uses this slot to send events to Datastream.
     2. In the **Publication name** field, enter the name of the publication you created in the database. A publication is a group of all tables that you want to replicate changes from using this stream.
  2. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the tables and schemas in the source database that Datastream can transfer into the destination.
The menu fails to load the list of tables and schemas if your database has more than 5,000 objects.
     * If you want Datastream to transfer all tables and schemas, then select **All tables from all schemas**.
     * If you want Datastream to transfer only specific tables and schemas, select **Specific schemas and tables** , and then select the checkboxes for the schemas and tables that you want Datastream to pull.

For each schema that you select, there's a **Future tables** checkbox.

       * If this checkbox is selected, then any tables for the schema that you add to the source after the stream is created will be transferred into the destination automatically.
       * If this checkbox isn't selected, then after the stream is created, Datastream won't transfer any new tables for the schema from the source into the destination.

By default, the **Future tables** checkbox is selected for each schema.

For each schema table that you select, there's a **SELECT COLUMNS** button. Click this button to filter any columns of the table that you want to exclude from being streamed from the source into the destination. Any columns that you clear are excluded from the stream.

By default, the checkboxes for all columns of the table are selected.

     * To provide a textual definition of the tables and schemas that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the schemas and tables that you want Datastream to pull. If your database has large numbers of tables and schemas, we recommend using the **Custom** option because some tables and schemas might not be included in the list of objects to pull. 

Enter schemas and tables as a comma-separated list, using the `[schema].[table]` format, where both the schema and the table can be a wildcard (asterisk). You can't use partial wildcards.

  3. If your destination is BigQuery, you can configure partitioning and clustering for your tables: 
     1. For each table that you want to set partitioning or clustering, click **Select columns**.
     2. To configure partitioning, in the **Partitioning** section, select one of the following options: 
        * **No partitioning** : when you select this option, no partitioning is applied to your tables.
        * **Partitioning by ingestion time** : when you select this option, data is organized into time-based partitions. Select a value from the **Partitioning type** list to configure the partitioning granularity with available options being hourly, daily, monthly, or yearly. Daily is the default granularity.
        * **Partitioning by field** : when you select this option, you need to select the source column by which you want to partition your table, and the partitioning type. Only source columns with supported data types can be selected. For information about supported source data types and available partitioning types, see [Configure partitioning and clustering for a BigQuery destination](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

Optionally, select the **Partitioning filter** option. If you select this option, a partition filter is required on all queries for this table. A partition filter can reduce cost and improve performance. For more information, see [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter).

You can use partitioning filters only in the append-only write mode.
     3. To configure clustering, in the **Clustering** section, select the fields by which you want to cluster your table. You can select up to four fields. The order in which you add the clustering fields determines the sort order of the data. If you don't specify clustering settings for a table, Datastream defaults to using up to four primary keys from the source table as the clustering keys in BigQuery.
Partitioning and clustering are only applied to new tables in BigQuery. If you want to configure or modify partitioning and clustering settings for a table that already exists, first delete it from BigQuery, and then configure or modify its settings in Datastream.
     4. Click **Save** to save your settings.

For more information about partitioning and clustering, see [Configure partitioning and clustering](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

  4. Optionally, expand the **Select objects to exclude** node. In the **Objects to exclude** field, enter the tables and schemas in the source database that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream. You define these schemas and tables with the same comma-separated logic that you use if you're specifying schemas and tables that you want Datastream to pull. 
  5. Optionally, expand the **Choose backfill mode for historical data** node, and then make one of the following selections:
     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the tables and schemas in the source database that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to stream only changes to the data into the destination.
  6. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a MySQL source database

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the tables and schemas in the source database that Datastream can transfer into the destination.
The menu fails to load the list of tables and schemas if your database has more than 5,000 objects.
     * If you want Datastream to transfer all tables and schemas, then select **All tables from all schemas**.
     * If you want Datastream to transfer only specific tables and schemas, select **Specific schemas and tables** , and then select the checkboxes for the schemas and tables that you want Datastream to pull.

For each schema that you select, there's a **Future tables** checkbox.

       * If this checkbox is selected, then any tables for the schema that you add to the source after the stream is created will be transferred into the destination automatically.
       * If this checkbox isn't selected, then after the stream is created, Datastream won't transfer any new tables for the schema from the source into the destination.

By default, the **Future tables** checkbox is selected for each schema.

For each schema table that you select, there's a **SELECT COLUMNS** button. Click this button to filter any columns of the table that you want to exclude from being streamed from the source into the destination. Any columns that you clear are excluded from the stream.

By default, the checkboxes for all columns of the table are selected.

     * To provide a textual definition of the tables and schemas that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the schemas and tables that you want Datastream to pull. If your database has large numbers of tables and schemas, we recommend using the **Custom** option because some tables and schemas might not be included in the list of objects to pull. 

Enter schemas and tables as a comma-separated list, using the `[schema].[table]` format, where both the schema and the table can be a wildcard (asterisk). You can't use partial wildcards.

  2. If your destination is BigQuery, you can configure partitioning and clustering for your tables: 
     1. For each table that you want to set partitioning or clustering, click **Select columns**.
     2. To configure partitioning, in the **Partitioning** section, select one of the following options: 
        * **No partitioning** : when you select this option, no partitioning is applied to your tables.
        * **Partitioning by ingestion time** : when you select this option, data is organized into time-based partitions. Select a value from the **Partitioning type** list to configure the partitioning granularity with available options being hourly, daily, monthly, or yearly. Daily is the default granularity.
        * **Partitioning by field** : when you select this option, you need to select the source column by which you want to partition your table, and the partitioning type. Only source columns with supported data types can be selected. For information about supported source data types and available partitioning types, see [Configure partitioning and clustering for a BigQuery destination](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

Optionally, select the **Partitioning filter** option. If you select this option, a partition filter is required on all queries for this table. A partition filter can reduce cost and improve performance. For more information, see [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter).

You can use partitioning filters only in the append-only write mode.
     3. To configure clustering, in the **Clustering** section, select the fields by which you want to cluster your table. You can select up to four fields. The order in which you add the clustering fields determines the sort order of the data. If you don't specify clustering settings for a table, Datastream defaults to using up to four primary keys from the source table as the clustering keys in BigQuery.
Partitioning and clustering are only applied to new tables in BigQuery. If you want to configure or modify partitioning and clustering settings for a table that already exists, first delete it from BigQuery, and then configure or modify its settings in Datastream.
     4. Click **Save** to save your settings.

For more information about partitioning and clustering, see [Configure partitioning and clustering](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

  3. Optionally, expand the **Select objects to exclude** node. In the **Objects to exclude** field, enter the tables and schemas in the source database that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream. You define these schemas and tables with the same comma-separated logic that you use if you're specifying schemas and tables that you want Datastream to pull. 
  4. Specify the CDC method for your stream:
     * **GTID (Global Transaction IDs)-based replication** : select this method if you want Datastream to support failovers and provide seamless replication irrespective of the changes in your database cluster.
     * **Binlog-based replication** : select this method to read and replicate changes directly from the binary log files of a selected database instance. You can't switch a running stream to a different source instance or a replica using this CDC method.
  5. Optionally, expand the **Choose backfill mode for historical data** node, and then make one of the following selections:
     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the tables and schemas in the source database that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to stream only changes to the data into the destination.
  6. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure an Oracle source database

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the tables and schemas in the source database that Datastream can transfer into the destination.
The menu fails to load the list of tables and schemas if your database has more than 5,000 objects.
     * If you want Datastream to transfer all tables and schemas, then select **All tables from all schemas**.
     * If you want Datastream to transfer only specific tables and schemas, select **Specific schemas and tables** , and then select the checkboxes for the schemas and tables that you want Datastream to pull.

For each schema that you select, there's a **Future tables** checkbox.

       * If this checkbox is selected, then any tables for the schema that you add to the source after the stream is created will be transferred into the destination automatically.
       * If this checkbox isn't selected, then after the stream is created, Datastream won't transfer any new tables for the schema from the source into the destination.

By default, the **Future tables** checkbox is selected for each schema.

For each schema table that you select, there's a **SELECT COLUMNS** button. Click this button to filter any columns of the table that you want to exclude from being streamed from the source into the destination. Any columns that you clear are excluded from the stream.

By default, the checkboxes for all columns of the table are selected.

     * To provide a textual definition of the tables and schemas that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the schemas and tables that you want Datastream to pull. If your database has large numbers of tables and schemas, we recommend using the **Custom** option because some tables and schemas might not be included in the list of objects to pull. 

Enter schemas and tables as a comma-separated list, using the `[schema].[table]` format, where both the schema and the table can be a wildcard (asterisk). You can't use partial wildcards. Unless specified explicitly, the Oracle predefined schemas and tables aren't pulled into the destination.

  2. If your destination is BigQuery, you can configure partitioning and clustering for your tables: 
     1. For each table that you want to set partitioning or clustering, click **Select columns**.
     2. To configure partitioning, in the **Partitioning** section, select one of the following options: 
        * **No partitioning** : when you select this option, no partitioning is applied to your tables.
        * **Partitioning by ingestion time** : when you select this option, data is organized into time-based partitions. Select a value from the **Partitioning type** list to configure the partitioning granularity with available options being hourly, daily, monthly, or yearly. Daily is the default granularity.
        * **Partitioning by field** : when you select this option, you need to select the source column by which you want to partition your table, and the partitioning type. Only source columns with supported data types can be selected. For information about supported source data types and available partitioning types, see [Configure partitioning and clustering for a BigQuery destination](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

Optionally, select the **Partitioning filter** option. If you select this option, a partition filter is required on all queries for this table. A partition filter can reduce cost and improve performance. For more information, see [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter).

You can use partitioning filters only in the append-only write mode.
     3. To configure clustering, in the **Clustering** section, select the fields by which you want to cluster your table. You can select up to four fields. The order in which you add the clustering fields determines the sort order of the data. If you don't specify clustering settings for a table, Datastream defaults to using up to four primary keys from the source table as the clustering keys in BigQuery.
Partitioning and clustering are only applied to new tables in BigQuery. If you want to configure or modify partitioning and clustering settings for a table that already exists, first delete it from BigQuery, and then configure or modify its settings in Datastream.
     4. Click **Save** to save your settings.

For more information about partitioning and clustering, see [Configure partitioning and clustering](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

  3. Optionally, expand the **Select objects to exclude** node. In the **Objects to exclude** field, enter the tables and schemas in the source database that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream. You define these schemas and tables with the same comma-separated logic that you use if you're specifying schemas and tables that you want Datastream to pull. 
  4. Specify the CDC method for your stream:
     * **LogMiner** : select this method to query archived redo logs using the LogMiner API. LogMiner supports most options available for Oracle, such as encryption and compression options.
     * **Binary reader** ([Preview](https://cloud.google.com/products/#product-launch-stages)): select this method to extract changes directly from Oracle logs. This allows for faster replication of large Oracle databases and reduced latency and overhead. When you select this option, an additional drop-down is shown. Select the way you want to access your Oracle log files:
       * **Automatic Storage Management (ASM)** : select this option if your database uses ASM. Make sure that you selected the **Enable ASM access for binary reader** checkbox and filled in the details of your ASM instance in your source connection profile.
       * **Database directories** : select this option if you don't use ASM for storing your log files. If you select database directories, you need to provide the redo log and archived log directory names.
  5. Optionally, expand the **Choose backfill mode for historical data** node, and then make one of the following selections:
     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the tables and schemas in the source database that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to stream only changes to the data into the destination.
  6. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a SQL Server source database

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the tables and schemas in the source database that Datastream can transfer into the destination.
The menu fails to load the list of tables and schemas if your database has more than 5,000 objects.
     * If you want Datastream to transfer all tables and schemas, then select **All tables from all schemas**.
     * If you want Datastream to transfer only specific tables and schemas, select **Specific schemas and tables** , and then select the checkboxes for the schemas and tables that you want Datastream to pull.

For each schema that you select, there's a **Future tables** checkbox.

       * If this checkbox is selected, then any tables for the schema that you add to the source after the stream is created will be transferred into the destination automatically.
       * If this checkbox isn't selected, then after the stream is created, Datastream won't transfer any new tables for the schema from the source into the destination.

By default, the **Future tables** checkbox is selected for each schema.

For each schema table that you select, there's a **SELECT COLUMNS** button. Click this button to filter any columns of the table that you want to exclude from being streamed from the source into the destination. Any columns that you clear are excluded from the stream.

By default, the checkboxes for all columns of the table are selected.

     * To provide a textual definition of the tables and schemas that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the schemas and tables that you want Datastream to pull. If your database has large numbers of tables and schemas, we recommend using the **Custom** option because some tables and schemas might not be included in the list of objects to pull. 

Enter schemas and tables as a comma-separated list, using the `[schema].[table]` format, where both the schema and the table can be a wildcard (asterisk). You can't use partial wildcards.

  2. If your destination is BigQuery, you can configure partitioning and clustering for your tables: 
     1. For each table that you want to set partitioning or clustering, click **Select columns**.
     2. To configure partitioning, in the **Partitioning** section, select one of the following options: 
        * **No partitioning** : when you select this option, no partitioning is applied to your tables.
        * **Partitioning by ingestion time** : when you select this option, data is organized into time-based partitions. Select a value from the **Partitioning type** list to configure the partitioning granularity with available options being hourly, daily, monthly, or yearly. Daily is the default granularity.
        * **Partitioning by field** : when you select this option, you need to select the source column by which you want to partition your table, and the partitioning type. Only source columns with supported data types can be selected. For information about supported source data types and available partitioning types, see [Configure partitioning and clustering for a BigQuery destination](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

Optionally, select the **Partitioning filter** option. If you select this option, a partition filter is required on all queries for this table. A partition filter can reduce cost and improve performance. For more information, see [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter).

You can use partitioning filters only in the append-only write mode.
     3. To configure clustering, in the **Clustering** section, select the fields by which you want to cluster your table. You can select up to four fields. The order in which you add the clustering fields determines the sort order of the data. If you don't specify clustering settings for a table, Datastream defaults to using up to four primary keys from the source table as the clustering keys in BigQuery.
Partitioning and clustering are only applied to new tables in BigQuery. If you want to configure or modify partitioning and clustering settings for a table that already exists, first delete it from BigQuery, and then configure or modify its settings in Datastream.
     4. Click **Save** to save your settings.

For more information about partitioning and clustering, see [Configure partitioning and clustering](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

  3. Optionally, expand the **Select objects to exclude** node. In the **Objects to exclude** field, enter the tables and schemas in the source database that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream. You define these schemas and tables with the same comma-separated logic that you use if you're specifying schemas and tables that you want Datastream to pull. 
  4. Specify the CDC method for your stream:
     * **Transaction logs** : select this method to process changes directly from the database logs. This method provides the best performance and is more efficient, but requires additional configuration steps.
     * **Change tables** : select this method to process changes from dedicated change tables. This method is easier to configure and has fewer limitations, but supports lower throughput and produces higher load on your database than the transaction logs method.
  5. Optionally, expand the **Choose backfill mode for historical data** node, and then make one of the following selections:
     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the tables and schemas in the source database that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to stream only changes to the data into the destination.
  6. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a source Salesforce org

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the objects and fields in your org that you want Datastream to transfer into the destination.
The menu fails to load the list if there are more than 5,000 objects.
     * If you want Datastream to transfer all objects, then select **All objects**.
     * If you want Datastream to transfer only specific objects, select **Specific objects** , and then select the checkboxes for the objects that you want Datastream to pull.

For each object that you select, there's a **Select fields** button. Click this button to filter any fields of the object that you want to exclude from being streamed from the source into the destination. Any fields that you clear are excluded from the stream.

By default, the checkboxes for all fields of the object are selected.

     * To provide a textual definition of the objects that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the objects that you want Datastream to pull. Enter the objects as a comma-separated list, using the `[object].[field]` format. If your database has large numbers of objects, we recommend using the **Custom** option because some tables and schemas might not be included in the list of objects to pull. 
  2. Define the polling interval value in minutes. Datastream uses this value to check your Salesforce org for data changes. The higher the value, the lower the cost and load on your org. The lower the value, the more up-to-date the data in the destination.
  3. If your destination is BigQuery, you can configure partitioning and clustering for your objects: 
     1. For each object that you want to set partitioning or clustering, click **Select fields**.
     2. To configure partitioning, in the **Partitioning** section, select one of the following options: 
        * **No partitioning** : when you select this option, no partitioning is applied to your objects.
        * **Partitioning by ingestion time** : when you select this option, data is organized into time-based partitions. Select a value from the **Partitioning type** list to configure the partitioning granularity with available options being hourly, daily, monthly, or yearly. Daily is the default granularity.
        * **Partitioning by field** : when you select this option, you need to select the source field by which you want to partition your object, and the partitioning type. Only fields with supported data types can be selected. For information about supported source data types and available partitioning types, see [Partition and cluster BigQuery tables](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

Optionally, select the **Partitioning filter** option. If you select this option, a partition filter is required on all queries for this object. A partition filter can reduce cost and improve performance. For more information, see [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter).

You can use partitioning filters only in the append-only write mode.
     3. To configure clustering, in the **Clustering** section, select the fields by which you want to cluster your object. You can select up to four fields. The order in which you add the clustering fields determines the sort order of the data. If you don't specify clustering settings for an object, Datastream defaults to using up to four primary keys from the source object as the clustering keys in BigQuery.
Partitioning and clustering are only applied to new tables in BigQuery. If you want to configure or modify partitioning and clustering settings for a table that already exists, first delete it from BigQuery, and then configure or modify its settings in Datastream.
     4. Click **Save** to save your settings.

For more information about partitioning and clustering, see [Partition and cluster BigQuery tables](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

  4. Optionally, expand the **Select objects to exclude** node. In the **Objects to exclude** field, enter the objects and fields in the source org that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream. You define these objects and fields with the same comma-separated logic that you use for including objects.
  5. Optionally, expand the **Choose backfill mode for historical data** node, and then make one of the following selections:
     * Select the **Automatic** option to replicate all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the objects in the source org that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to replicate only changes to the data into the destination.
  6. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a source Salesforce Marketing Cloud instance ([Preview](https://cloud.google.com/products/#product-launch-stages))

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the objects in your instance that you want Datastream to transfer into the destination.
The menu fails to load the list if there are more than 5,000 objects.
     * If you want Datastream to transfer all objects, then select **All objects**.
     * If you want Datastream to transfer only specific objects, select **Specific objects** , and then select the checkboxes for the objects that you want Datastream to pull.
     * If you want to provide a textual definition of the objects that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the objects that you want Datastream to pull. Enter the objects as a comma-separated list. If your database has large numbers of objects, we recommend using the **Custom** option because some objects might not be included in the list of objects to pull. 
  2. Define the polling interval value in minutes. Datastream uses this value to check your Salesforce Marketing Cloud instance for data changes for objects that support incremental sync. You can use a value within the range of `5` to `1440`.
  3. Define the full refresh polling interval value in minutes. Datastream uses this value to perform a periodic full refresh for objects that don't support incremental sync, such as data extensions. You can use a value within the range of `60` to `1440`.
  4. Optionally, expand the **Show advanced options** node.
  5. In the **Objects to exclude** field, enter the objects in the source instance that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream. You define these objects with the same comma-separated logic that you use if you're specifying objects that you want Datastream to pull. 
  6. In the **Choose backfill mode for historical data** section, select the backfill mode:
     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the objects in the source database that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to stream only changes to the data into the destination.
  7. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a source ServiceNow instance ([Preview](https://cloud.google.com/products/#product-launch-stages))

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the tables and fields in your ServiceNow instance that you want Datastream to transfer into the destination.
The menu fails to load the list if there are more than 5,000 objects.
     * If you want Datastream to transfer all tables, then select **All objects**.
     * If you want Datastream to transfer only specific tables, select **Specific objects** , and then select the checkboxes for the tables that you want Datastream to pull.

For each table that you select, there's a **Select fields** button. Click this button to filter any fields of the table that you want to exclude from being streamed from the source into the destination. Datastream excludes any fields that you clear from the stream.

By default, Datastream selects the checkboxes for all fields of the table.

     * If you want to provide a textual definition of the tables that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the tables that you want Datastream to pull. Enter the tables as a comma-separated list, using the `[table].[field]` format. 
  2. Define the polling interval value in minutes. Datastream uses this value to check your ServiceNow instance for data changes. The higher the value, the lower the cost and load on your instance. The lower the value, the more up-to-date the data in the destination.
  3. Optionally, in the **Objects to exclude** field, enter the tables and fields in the source instance that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, Datastream excludes the object from the stream. You define these tables and fields with the same comma-separated logic that you use for including tables.
  4. Optionally, in the **Choose backfill mode for historical data** section, make one of the following selections:
     * Select the **Automatic** option to replicate all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the tables in the source instance that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to replicate only changes to the data into the destination.
  5. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a source MongoDB database

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the databases and collections that you want Datastream to transfer into the destination.
The menu fails to load the list if there are more than 5,000 objects.
     * If you want Datastream to transfer all collections, then select **All databases and collections**.
     * If you want Datastream to transfer only specific collections, select **Specific databases and collections** , and then select the checkboxes for the collections that you want Datastream to pull.

For each collection that you select, there's a **Select fields** button. Click this button to filter any fields of the object that you want to exclude from being streamed from the source into the destination. Any fields that you clear are excluded from the stream.

By default, the checkboxes for all fields of the object are selected.

     * To provide a textual definition of the collections that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the collections that you want Datastream to pull. Enter the objects as a comma-separated list, using the `[collection].[field]` format. If your database has large numbers of objects, we recommend using the **Custom** option because some tables and schemas might not be included in the list of objects to pull. 
  2. If your destination is BigQuery, you can configure partitioning for your collections: 
     1. For each collection that you want to set partitioning, click **Select fields**.
     2. In the **Partitioning** section, select one of the following options: 
        * **No partitioning** : when you select this option, no partitioning is applied to your collections.
        * **Partitioning by ingestion time** : when you select this option, data is organized into time-based partitions. Select a value from the **Partitioning type** list to configure the partitioning granularity with available options being hourly, daily, monthly, or yearly. Daily is the default granularity.

Optionally, select the **Partitioning filter** option. If you select this option, a partition filter is required on all queries for this collection. A partition filter can reduce cost and improve performance. For more information, see [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter).

You can use partitioning filters only in the append-only write mode.
Partitioning is only applied to new tables in BigQuery. If you want to configure or modify partitioning settings for a table that already exists, first delete it from BigQuery, and then configure or modify its settings in Datastream.
     3. Click **Save** to save your settings.

For more information about partitioning and clustering, see [Partition and cluster BigQuery tables](https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering).

  3. Optionally, expand the **Choose backfill mode for historical data** node, and then make one of the following selections:
     * Select the **Automatic** option to replicate all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the objects in the source org that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to replicate only changes to the data into the destination.
  4. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a source Spanner database

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the tables and schemas in the source database that Datastream can transfer into the destination.
The menu fails to load the list of tables and schemas if your database has more than 5,000 objects.
     * If you want Datastream to transfer all tables and schemas, then select **All tables from all schemas**.
     * If you want Datastream to transfer only specific tables and schemas, select **Specific schemas and tables** , and then select the checkboxes for the schemas and tables that you want Datastream to pull.

For each schema that you select, there's a **Future tables** checkbox.

       * If this checkbox is selected, then any tables for the schema that you add to the source after the stream is created will be transferred into the destination automatically.
       * If this checkbox isn't selected, then after the stream is created, Datastream won't transfer any new tables for the schema from the source into the destination.

By default, the **Future tables** checkbox is selected for each schema.

For each schema table that you select, there's a **SELECT COLUMNS** button. Click this button to filter any columns of the table that you want to exclude from being streamed from the source into the destination. Any columns that you clear are excluded from the stream.

By default, the checkboxes for all columns of the table are selected.

     * To provide a textual definition of the tables and schemas that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the schemas and tables that you want Datastream to pull. If your database has large numbers of tables and schemas, we recommend using the **Custom** option because some tables and schemas might not be included in the list of objects to pull. 

Enter schemas and tables as a comma-separated list, using the `[schema].[table]` format, where both the schema and the table can be a wildcard (asterisk). You can't use partial wildcards.

  2. In the **Change stream name** field, enter the name of the Spanner change stream that you created. Datastream reads this change stream to replicate changes from your source database.
  3. Optionally, in the **Objects to exclude** field, enter the tables and schemas in the source database that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream. You define these schemas and tables with the same comma-separated logic that you use if you're specifying schemas and tables that you want Datastream to pull. 
  4. In the **Choose backfill mode for historical data** section, select the backfill mode:
     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the tables and schemas in the source database that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to stream only changes to the data into the destination.
  5. Optionally, specify the maximum number of concurrent CDC and backfill tasks in the respective fields.  Setting the maximum number of concurrent reads for change stream queries (the CDC concurrency limit) might increase streaming latency. This is because change streams are divided into partitions, and limiting concurrency prevents Datastream from reading multiple partitions simultaneously. We recommend setting this value only if you've observed significant CPU usage. 
  6. From the **RPC priority** drop-down, select the [remote procedure call priority](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions#priority) for your Spanner requests: 
     * Low
     * Medium
     * High
  7. In the **FGAC role** field, specify the [fine-grained access control role](https://docs.cloud.google.com/spanner/docs/fgac-about) for your Spanner requests.
  8. Select the **Backfill Data Boost enabled** checkbox if you want to use Data Boost for backfill jobs. To use this option, Data Boost must be enabled for your database. For more information, see [Data Boost overview](https://docs.cloud.google.com/spanner/docs/databoost/databoost-overview).
  9. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a source Dataverse environment ([Preview](https://cloud.google.com/products/#product-launch-stages))

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the objects in your Dataverse environment that Datastream can transfer into the destination.
The menu fails to load the list if there are more than 5,000 objects.
     * If you want Datastream to transfer all standard objects, then select **All objects**.
     * If you want Datastream to transfer only specific standard objects, select **Specific objects** , and then select the checkboxes for the objects that you want Datastream to pull.

For each object that you select, there's a **Future tables** checkbox.

       * If this checkbox is selected, then any objects that you add to the source after the stream is created are transferred into the destination automatically.
       * If this checkbox isn't selected, then after the stream is created, Datastream doesn't transfer any new objects from the source into the destination.

By default, the **Future tables** checkbox is selected for each object.

For each object that you select, there's a **SELECT FIELDS** button. Click this button to filter any fields of the objects that you want to exclude from being streamed from the source into the destination. Any fields that you clear are excluded from the stream.

By default, the checkboxes for all fields of the object are selected.

     * To provide a textual definition of the objects that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the objects that you want Datastream to pull. Enter the objects as a comma-separated list, using the `[OBJECT_NAME]` format. Wildcards aren't supported.
  2. In the **Define polling interval** section, define how often you want Datastream to check for Dataverse data changes. Consider balancing near real-time data needs with efficient API usage to minimize costs and avoid performance issues. The value that you enter must be in the range of `5` to `1440` minutes.
  3. Optionally, expand the **Select objects to exclude** node. In the **Objects to exclude** field, enter the objects in the source Dataverse environment that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream.
  4. Optionally, expand the **Choose backfill mode for historical data** node, and then make one of the following selections:
     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the tables in the source Dataverse environment that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to stream only changes to the data into the destination.
  5. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



#### Configure a source Workday instance ([Preview](https://cloud.google.com/products/#product-launch-stages))

  1. In the **Select objects to include** section, use the **Objects to include** drop-down menu to specify the objects in your instance that you want Datastream to transfer into the destination.
The menu fails to load the list if there are more than 5,000 objects.
     * If you want Datastream to transfer all objects, then select **All objects**.
     * If you want Datastream to transfer only specific objects, select **Specific objects** , and then select the checkboxes for the objects that you want Datastream to pull. If you want to include only specific columns for an object, click **Configure settings** next to the object. Columns for which you clear the checkboxes are excluded from the stream.
     * If you want to provide a textual definition of the objects that you want Datastream to transfer, select **Custom** , and then, in the **Object matching criteria** field, enter the objects that you want Datastream to pull. Enter the objects as a comma-separated list. If your instance has large numbers of objects, we recommend using the **Custom** option because some objects might not be included in the list of objects to pull. 
  2. Define the polling interval value in minutes. Datastream uses this value to check your Workday instance for data changes. You can use a value within the range of `5` to `1440` .
  3. Define the full refresh polling interval value in minutes. Datastream uses this value to perform a periodic full refresh for objects that don't support incremental sync, such as data extensions. You can use a value within the range of `60` to `1440` minutes.
  4. Optionally, expand the **Show advanced options** node.
  5. In the **Objects to exclude** field, enter the objects in the source instance that you want to restrict Datastream from pulling. The **Objects to exclude** list takes precedence over the **Objects to include** list. If an object meets the criteria in both the include and exclude lists, the object is excluded from the stream. You define these objects with the same comma-separated logic that you use if you're specifying objects that you want Datastream to pull. 
  6. In the **Choose backfill mode for historical data** section, select the backfill mode:
     * Select the **Automatic** option to stream all existing data, in addition to changes to the data, from the source into the destination. In the **Objects excluded from automatic backfill** field, enter the objects in the source instance that you want to restrict Datastream from backfilling into the destination.
     * Select the **Manual** option to stream only changes to the data into the destination.
  7. Click **CONTINUE**. The **Define connection profile** panel of the **Create stream** page appears for your destination type.



## Select a destination connection profile

  1. If you have [created a destination connection profile](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4cloudstorage), then select it from the list of connection profiles.

If you haven't created a destination connection profile, then create one by clicking **CREATE CONNECTION PROFILE** at the bottom of the drop-down list, and then perform the same steps as in [Create connection profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles).

**Note:** For Apache Iceberg tables destination, use or create a BigQuery connection profile.
  2. Click **CONTINUE**. The **Configure stream destination** panel of the **Create stream** page appears.




## Configure information about the destination for the stream

This section describes what information you need to provide to configure your BigQuery or Cloud Storage destination.

### BigQuery destination

  1. In the **Specify how Datastream should stream into a BigQuery dataset** section, select one of the following options from the **Schema grouping** drop-down:

     * **Dataset for each schema** : Datastream creates a BigQuery dataset for each source schema, based on the schema name.

If you select this option, then for every schema in the source database, Datastream creates a dataset in the project that contains the stream.

In addition, if you select the **Dataset for each schema** option, you need to provide the following:

       1. In the **Location type** section, specify where you want to store your data in BigQuery. Select **Region** to specify a single geographical location, or **Multi-region** to specify a larger area that contains two or more regions. If your priority is to optimize costs and performance, select **Region** , and keep your datasets alongside other Google Cloud resources that you manage. If you want to achieve higher quota limits, select **Multi-region** to let BigQuery use multiple regions within a group. When you select **Region** , the field defaults to the region that you selected for the stream.
       2. (Optional) In the **Dataset prefix** field, define a prefix for the dataset created by the stream. The string that you specify is added to the source schema name. For example, if the schema is called `<mySchema>`, and you define the dataset prefix as `<myPrefix>`, Datastream creates a dataset called `<myPrefix><mySchema>`.
       3. Expand the **Show advanced encryption options** section.
       4. Specify how you want your data to be encrypted in BigQuery by selecting a Google-managed or customer-managed encryption key.

**Note:** The **Dataset for each schema** option isn't supported for Salesforce sources.
     * **Single dataset for all schemas** : Datastream creates all the tables inside the existing BigQuery dataset that you specify. Each table that Datastream creates is named using a combination of the source schema name and table name, separated by an underscore (for example, ``<mySchemaName>_<myTableName>``). The datasets available are grouped by region. You can also create a new dataset.

  2. Specify the **Stream write mode**. Select your write mode to define how data is written and processed in BigQuery:

     * **Merge** : select this option if you want your data to be synchronised with the source.
     * **Append-only** : select this option if you want to keep all historical data for your change events.
  3. **Specify the limit of data staleness**. Only available when **Merge** mode is selected in the preceding step. Select a limit to balance BigQuery query performance and cost versus data freshness. BigQuery applies the changes in the background on an ongoing basis, or at query run time, according to the staleness limit. Lower staleness (fresher data) may increase BigQuery processing costs. 

If you select **0 minutes** , BigQuery **always** returns the query results based on the freshest data. This results in the highest cost of the query.

  4. Click **CONTINUE**. The **Review stream details and create** panel of the **Create stream** page appears.




### Apache Iceberg tables destination

  1. In the **Specify how Datastream should stream into a BigQuery dataset** section, select how you want Datastream to create new schemas and tables from the **Schema grouping** drop-down:

     * **Dataset for each schema** : Datastream creates a BigQuery dataset for each source schema, based on the schema name.

If you select this option, then for every schema in the source database, Datastream creates a dataset in the project that contains the stream.

In addition, if you select the **Dataset for each schema** option, you need to provide the following:

       1. In the **Location type** section, specify where you want to store your data in BigQuery. Select **Region** to specify a single geographical location, or **Multi-region** to specify a larger area that contains two or more regions. If your priority is to optimize costs and performance, select **Region** , and keep your datasets alongside other Google Cloud resources that you manage. If you want to achieve higher quota limits, select **Multi-region** to let BigQuery use multiple regions within a group. When you select **Region** , the field defaults to the region that you selected for the stream.
       2. (Optional) In the **Dataset prefix** field, define a prefix for the dataset created by the stream. The string that you specify is added to the source schema name. For example, if the schema is called `<mySchema>`, and you define the dataset prefix as `<myPrefix>`, Datastream creates a dataset called `<myPrefix><mySchema>`.
       3. Expand the **Show advanced encryption options** section.
       4. Specify how you want your data to be encrypted in BigQuery by selecting a Google-managed or customer-managed encryption key.

**Note:** The **Dataset for each schema** option isn't supported for Salesforce sources.
     * **Single dataset for all schemas** : Datastream creates all the tables inside the existing BigQuery dataset that you specify. Each table that Datastream creates is named using a combination of the source schema name and table name, separated by an underscore (for example, ``<mySchemaName>_<myTableName>``). The datasets available are grouped by region. You can also create a new dataset.

  2. In the **Define Datastream connection to Apache Iceberg tables** section, provide the following information:

     * From the **Connection ID** drop-down, select the identifier of the BigQuery connection that you created and that you want to use for your stream. For information about creating a Cloud resource connection in BigQuery, see [Configure Apache Iceberg tables in BigQuery](https://docs.cloud.google.com/datastream/docs/destination-blmt#configure-blmt).

**Note:** To prevent your stream from failing, make sure that the connection ID has write permissions to the underlying Cloud Storage bucket.
     * Enter or select the URI address of the bucket that you created in Cloud Storage. For information about creating a Cloud Storage bucket, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  3. Review the **File format** and **Table format**. Datastream supports the **Parquet** file format and the **Iceberg** table format.

  4. Review the **Stream write mode**. Datastream only supports the **Append-only** write mode when streaming to Apache Iceberg tables.

  5. Click **CONTINUE**. The **Review stream details and create** panel of the **Create stream** page appears.




### Cloud Storage destination

  1. Optionally, in the **Stream path prefix** field, enter the folder of the destination bucket into which Datastream will transfer schemas, tables, and data from a source database.

For example, if you want Datastream to transfer data from the source database into the `/root/example` folder in the destination bucket, then enter `/root/example` in the **Stream path prefix** field.

  2. In the **Output format** field, choose the format of files written to Cloud Storage. Datastream supports two output formats: Avro and JSON. 

  3. Optional. If you select the JSON format, then two checkboxes appear:

     1. **Include a Unified Types schema file in the file path** : If you select this checkbox, then Datastream writes two files to Cloud Storage: a JSON data file and an [Avro schema file](https://docs.cloud.google.com/datastream/docs/behavior-overview#features). The schema file has the same name as the data file, with a `.schema` extension. If you don't select this checkbox, then Datastream writes only the JSON data file to Cloud Storage. By default, this checkbox isn't selected.
     2. **Enable gzip compression** : If you select this checkbox, then Datastream uses the `gzip` utility to compress the files that Datastream writes to Cloud Storage. If you don't select this checkbox, then Datastream writes the files to Cloud Storage without compressing them. By default, this checkbox is selected.
  4. Click **CONTINUE**. The **Review stream details and create** panel of the **Create stream** page appears.




## Create the stream

  1. Verify details about the stream as well as the source and destination connection profiles that the stream will use to transfer data from a source database into a destination.
  2. Click **RUN VALIDATION** to validate the stream. By validating a stream, Datastream checks that the source is configured properly, validates that the stream can connect to both the source and the destination, and verifies the end-to-end configuration of the stream.

     1. If your source database is Oracle, then Datastream performs the following checks:

Check| Description  
---|---  
Objects list validity| Datastream verifies that the exclude list doesn't subsume the include list.  
Forward SSH tunnel connectivity| Datastream verifies that it can connect to a bastion host through a Forward SSH tunnel.  
Connectivity to Oracle database| Datastream verifies that it can connect to the source Oracle database.  
Oracle user permissions| Datastream verifies that the user which it uses to connect to the source database has all of the necessary permissions to retrieve schemas, tables, and data from the database so that Datastream can stream this information into the destination.  
Logging mode configuration| Datastream verifies that the logging mode for Oracle database is set to [ARCHIVELOG](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database).  
Supplemental logging configuration| Datastream verifies that supplemental logging is turned on for the database tables that are being streamed from the source into the destination.  
Oracle CDC configuration| Datastream verifies that the CDC method that you selected complies with your database configuration.  
Archive log files configuration| Datastream verifies that archive logging is configured in the source, and that archive log files are present.  
Cloud Storage permissions (for Cloud Storage destinations) | Datastream verifies that it has the necessary permissions to write to the destination bucket in Cloud Storage.  
     2. If your source database is MySQL, then Datastream performs the following checks:

Check| Description  
---|---  
Replication permissions| Datastream verifies that it has permissions to replicate a MySQL database.  
Database version| Datastream verifies that MySQL database version is supported. For information about supported editions, see [Versions](https://docs.cloud.google.com/datastream/docs/sources-mysql#versionsformysqlsourcedb).  
Binary log format configuration| Datastream verifies that the binary log format of the MySQL database is set to `ROW`.  
Binary logging is enabled| Datastream verifies that the binary log files are configured correctly, and that there are log files present.  
Binary log row image configuration| Datastream verifies that the binlog row image is set to `FULL`.  
Binlog compression disabled| Datastream verifies that the binlog compression is disabled.  
Log replica or slave updates enabled| Datastream verifies that the log replica or slave updates are enabled.  
GTID mode configuration (`applies only to GTID-based CDC`)| Datastream verifies that the GTID mode is set to `ON` if GTID based replication is used.  
GtidSet doesn't contain tagged GTIDs (`applies only to GTID-based CDC`)| Datastream verifies that the GTID set doesn't contain any tagged GTIDs.  
Cloud Storage permissions (for Cloud Storage destinations)| Datastream verifies that it has the necessary permissions to write to the destination bucket in Cloud Storage.  
Warnings check| Description  
---|---  
Expire logs days or Expire logs seconds or Binlog retention hours configuration| Datastream verifies that the `expire_logs_days`, `binlog_expire_logs_seconds`, `binlog retention hours` are configured to values greater than `7`, `604800`, and `168`, respectively.  
Max allowed packet configuration| Datastream verifies that the `max_allowed_packet` is set to 1GB.  
Enforce GTID consistency or GTID strict mode (`applies only to GTID-based CDC`)| Datastream verifies that the GTID consistency or GTID strict mode is enabled.  
     3. If your source database is PostgreSQL, then Datastream performs the following checks:

Check| Description  
---|---  
Connectivity to PostgreSQL database| Datastream verifies that it can connect to the source PostgreSQL database.  
Logical decoding is enabled| Datastream verifies that `wal_level` parameter of the PostgreSQL database is set to `logical`.  
Replication slot configuration| Datastream verifies whether the PostgreSQL replication slot exists and is active, whether Datastream has the permissions required to access it, and whether it is configured correctly.  
Publication configuration| Datastream verifies that the publication exists and that the tables to replicate for the stream are included in the publication.  
Backfill permissions| Datastream verifies that tables required to backfill historical data exist and that it has the necessary permissions to read them.  
     4. If your source database is SQL Server, then Datastream performs the following checks:

Check| Description  
---|---  
SQL Server edition| Datastream verifies that the source SQL Server database edition is supported. For information about supported editions, see [Versions](https://docs.cloud.google.com/datastream/docs/sqlserver/sources-sqlserver#sqlserverversions).  
SQL Server user permissions| Datastream verifies that the user has the permissions required to access the source SQL Server database.  
SQL Server CDC is enabled| Datastream verifies whether CDC is enabled for the database and all tables included in the stream.  
SQL Server database validations| Datastream checks whether the source database is configured properly, whether all replication requirements are met and whether there are no unsupported data types in the columns.  
Cloud Storage or BigQuery permissions| Datastream verifies that the user has the necessary permissions to write to the destination.  
     5. If your source database is Salesforce, then Datastream performs the following checks:

Check| Description  
---|---  
Credentials login| Datastream verifies that it can authenticate with the customer's Salesforce org successfully using the provided credentials.   
Bulk API| Datastream verifies that it has the necessary permissions to access the Salesforce Bulk API 2.0. Bulk API 2.0 is required to read large amounts of data.  
Warnings check| Description  
---|---  
API limits| Datastream calculates an estimation of the expected API usage based on the number of objects and polling interval selected. If the expected daily number of requests is higher than your limit enforced by Salesforce, Datastream issues a warning. You can still create and run the stream, even if the validation check doesn't pass.  
     6. If your source database is MongoDB, then Datastream performs the following checks:

Check| Description  
---|---  
User permissions| Datastream verifies that the `readAnyDatabase` role is assigned to the user.  
Connection configurations| Datastream uses the `hello` command to verify that the connection configurations are valid.  
MongoDB version| Datastream verifies that the MongoDB version is 5.0 or later.  
Cloud Storage or BigQuery permissions| Datastream verifies that the user has the necessary permissions to write to the destination.  
     7. If your source database is Spanner, then Datastream performs the following checks:

Check| Description  
---|---  
Spanner API enabled| Datastream verifies that the Spanner API is enabled.  
Database exists| Datastream verifies that the source Spanner database exists.  
IAM permissions| Datastream verifies that its service agent has the necessary IAM permissions on the source database.  
Change stream exists| Datastream verifies that the specified change stream exists in the database.  
Value capture type| Datastream verifies that the change stream is configured with the `NEW_ROW` value capture type.  
     8. If your source is Dataverse, then Datastream performs the following checks:

Check| Description  
---|---  
Connectivity to Dataverse environment| Datastream verifies that it can connect to the source Dataverse environment.  
Dataverse user permissions| Datastream verifies that the application user which it uses to connect to the source environment has all of the necessary read permissions. The read permissions are required to retrieve tables and data from the environment so that Datastream can stream this information into the destination.  
IP restrictions| Datastream verifies that its public IP addresses are allowed to connect to your Dataverse instance endpoint.  
`modifiedon` field presence| Datastream verifies that the `modifiedon` field is present and reliable in the tables being replicated for incremental synchronization.  
Cloud Storage or BigQuery permissions| Datastream verifies that it has the necessary permissions to write to the destination.  
     9. If your source instance is Workday, then Datastream performs the following checks:

Check| Description  
---|---  
Credentials login| Datastream verifies OAuth 2.0 authentication with Workday.  
ISU permissions| Datastream verifies that the Integration System User has the required Domain Security Policy permissions.  
Report validity| Datastream ensures that the selected objects exist and are accessible using the Report as a Service (RaaS) solution.  
  
If a validation check passes, then a check mark icon appears to the left of the validation check. 

If a validation check doesn't pass, then an exclamation point icon appears to the left of the check, and a **SEE ERROR DETAILS** button appears below the check. Click the button, and a dialog window appears, explaining why the check didn't pass and information about what to do to rectify the problem. After making the appropriate corrections, click **REVALIDATE**.

For more information about troubleshooting validation checks that don't pass, see [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues).

  3. After all validation checks pass, click **CREATE & START** to create the stream and start it immediately, or **CREATE** to create the stream without starting it immediately.

If you don't start the stream now, then you can start it from the **Streams** page by clicking **START**.

**Note:** The stream creation process may incur an increased load on the source database. To put off that load, create the stream without starting it, and come back to start the stream when the load can be incurred.



After creating a stream, you can view [high-level and detailed information](https://docs.cloud.google.com/datastream/docs/view-a-stream) about it.

## Create a stream using the automated flow

You can use the automated stream setup to create streams directly from your Cloud SQL overview page in Google Cloud. The automated flow simplifies the stream creation process, and can be used if you're replicating to BigQuery from a Cloud SQL for PostgreSQL, Cloud SQL for MySQL or Cloud SQL for SQL Server instance.

To learn how to use the automated stream setup flow, see [Create a stream using the automated flow](https://docs.cloud.google.com/datastream/docs/create-a-stream-automated).

## What's next

  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to run a stream, see [Run a stream](https://docs.cloud.google.com/datastream/docs/run-a-stream).
  * To learn how to modify your streams, see [Modify a stream](https://docs.cloud.google.com/datastream/docs/modify-a-stream).
  * To learn how to recover a stream, see [Recover a stream](https://docs.cloud.google.com/datastream/docs/recover-a-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
