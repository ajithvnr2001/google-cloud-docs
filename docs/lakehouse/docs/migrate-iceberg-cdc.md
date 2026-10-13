---
url: https://docs.cloud.google.com/lakehouse/docs/migrate-iceberg-cdc/
title: Migrate Apache Iceberg change data capture (CDC) data into Lakehouse using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:47.940368+00:00
---

# Migrate Apache Iceberg change data capture (CDC) data into Lakehouse using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/migrate-iceberg-cdc/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Migrate Apache Iceberg change data capture (CDC) data into Lakehouse using Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Keeping target Lakehouse Apache Iceberg tables synchronized with frequently updated Apache Iceberg source tables can be difficult. Performing full table reloads to capture dataset changes increases compute costs and processing latency, and building custom pipelines to process change data capture (CDC) logs introduces complex operational overhead.

By using Dataflow batch or streaming CDC pipelines, you can continuously or periodically synchronize your Apache Iceberg source tables with Lakehouse Apache Iceberg tables. Instead of reloading full tables, CDC pipelines extract incremental updates directly from your source Apache Iceberg change logs and apply them to your target tables.

The CDC pipeline provides the following capabilities:

  * **Cost-effective incremental sync** : Processes only changed data (`INSERT`, `UPDATE`, and `DELETE` operations), reducing compute overhead and data latency.
  * **Flexible execution modes** : Supports both batch and streaming modes to fit your business requirements.



The CDC pipeline supports two execution modes:

  * **Batch CDC mode:** Periodically reads incremental updates from your source Apache Iceberg table between specified start and end snapshot bounds.
  * **Streaming CDC mode:** Continuously polls your source Apache Iceberg table for new change commits on a configurable frequency (defaulting to 1 minute, minimum 1 second) and applies them to your Lakehouse table in near-real-time.



## Before you begin

To set up CDC migration from Apache Iceberg to Lakehouse, ensure you have the following:

  1. Enable the Dataflow, BigQuery, and Lakehouse APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow.googleapis.com,bigquery.googleapis.com,biglake.googleapis.com)

  2. To get the permissions that you need to create the resources, ask your administrator to grant you the required Identity and Access Management (IAM) roles on your project.

  3. A valid source Apache Iceberg table stored in Cloud Storage or registered in an Iceberg REST catalog or metastore.

  4. An existing Lakehouse Iceberg catalog to receive the synced data.

If the target namespace doesn't exist, the CDC pipeline automatically creates it. If the target Lakehouse table doesn't exist, the CDC pipeline automatically creates it if you provide a valid list of equality columns.




## Support and limitations

CDC migration from Apache Iceberg to Lakehouse has the following considerations:

  * **SDK requirement:** Requires Apache Beam SDK version 2.77.0 or greater.
  * **Destination table creation:** Creating the destination Lakehouse table is supported. If the target table doesn't exist, the CDC pipeline automatically creates it, provided you supply a valid list of equality columns (`equality_columns`). Only an existing Lakehouse catalog is required; the CDC pipeline automatically creates the namespace if it doesn't exist.
  * **Schema evolution:** Automatic schema changes aren't supported. If the schema of the source Apache Iceberg table changes, you must manually update the target Lakehouse table schema to match before running the CDC synchronization job.
  * **Execution modes:**
    * **Batch CDC:** Pulls transaction log changes once per job execution between specified start and end snapshot bounds (snapshot ID or timestamp).
    * **Streaming CDC:** Continuously polls the source Apache Iceberg table for new commit logs. The polling frequency is configurable (defaulting to 1 minute, minimum 1 second).



## Create a CDC pipeline using Java

To programmatically build and run an Apache Iceberg CDC batch or streaming migration pipeline using the Apache Beam Java SDK, use the `Managed.read` transform with `Managed.ICEBERG_CDC`.

The following Java examples demonstrate how to configure and execute Apache Iceberg CDC pipelines for batch and streaming workloads.

### Batch CDC pipeline

The following Java example configures a batch pipeline that reads Apache Iceberg CDC events within specified start and end snapshot bounds:

### Java

Add the following dependencies to your `pom.xml` file:
    
    
    <dependency>
      <groupId>org.apache.beam</groupId>
      <artifactId>beam-sdks-java-managed</artifactId>
      <version>${beam.version}</version>
    </dependency>
    <dependency>
      <groupId>org.apache.beam</groupId>
      <artifactId>beam-sdks-java-io-iceberg</artifactId>
      <version>${beam.version}</version>
    </dependency>
    

The following Java snippet demonstrates how to configure and execute a batch CDC pipeline from an Iceberg table to Lakehouse: 
    
    
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.iceberg.cdc.IcebergCdcMetadataColumns;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.Row;
    
    public class IcebergBatchCdcToLakehouse {
      public static void main(String[] args) {
        Pipeline pipeline = Pipeline.create(PipelineOptionsFactory.fromArgs(args).create());
    
        // Configure source catalog properties
        Map<String, String> sourceCatalogProps = new HashMap<>();
        sourceCatalogProps.put("type", "SOURCE_CATALOG_TYPE");
        sourceCatalogProps.put("warehouse", "SOURCE_WAREHOUSE_LOCATION");
        // Add additional properties if required by your catalog type (for example, uri)
    
        // Configure batch Iceberg CDC reader with snapshot bounds
        Map<String, Object> readConfig = new HashMap<>();
        readConfig.put("table", "SOURCE_NAMESPACE.SOURCE_TABLE");
        readConfig.put("catalog_properties", sourceCatalogProps);
        readConfig.put("start_snapshot_id", START_SNAPSHOT_ID);
        readConfig.put("end_snapshot_id", END_SNAPSHOT_ID);
        readConfig.put(
            "include_metadata_columns",
            Arrays.asList(
                IcebergCdcMetadataColumns.CHANGE_TYPE,
                IcebergCdcMetadataColumns.COMMIT_SNAPSHOT_SEQUENCE_NUMBER));
    
        // Read batch CDC events from source Iceberg table
        PCollection<Row> cdcRows =
            pipeline.apply(
                "ReadFromIcebergCDC",
                Managed.read(Managed.ICEBERG_CDC).withConfig(readConfig)).getSinglePCollection();
    
        // Configure destination Lakehouse REST Catalog properties for Lakehouse Iceberg
        Map<String, String> destinationCatalogProps = new HashMap<>();
        destinationCatalogProps.put("type", "rest");
        destinationCatalogProps.put("uri", "https://biglake.googleapis.com/iceberg/v1/restcatalog");
        destinationCatalogProps.put("warehouse", "gs://WAREHOUSE_BUCKET");
        destinationCatalogProps.put("header.x-goog-user-project", "PROJECT_ID");
        destinationCatalogProps.put("io-impl", "org.apache.iceberg.gcp.gcs.GCSFileIO");
        destinationCatalogProps.put("rest.auth.type", "google");
    
        // Configure Lakehouse Iceberg writer
        Map<String, Object> writeConfig = new HashMap<>();
        writeConfig.put("table", "TARGET_NAMESPACE.TARGET_TABLE");
        writeConfig.put("catalog_properties", destinationCatalogProps);
        writeConfig.put("mode", "merge-on-read");
        writeConfig.put("change_type_column", IcebergCdcMetadataColumns.CHANGE_TYPE);
    
        // Write CDC rows to target Lakehouse Iceberg table
        cdcRows.apply(
            "WriteToLakehouse",
            Managed.write(Managed.ICEBERG).withConfig(writeConfig));
    
        pipeline.run();
      }
    }
    

Replace the following:

  * `SOURCE_CATALOG_TYPE`: the type of the source Iceberg catalog (for example, `hadoop` or `hive`).
  * `SOURCE_WAREHOUSE_LOCATION`: the warehouse location of the source Iceberg catalog (for example, `s3://source-warehouse` or `gs://source-warehouse`).
  * `SOURCE_NAMESPACE`: the namespace of the source Iceberg table.
  * `SOURCE_TABLE`: the name of the source Iceberg table.
  * `START_SNAPSHOT_ID`: the starting snapshot ID for the batch CDC read.
  * `END_SNAPSHOT_ID`: the ending snapshot ID for the batch CDC read.
  * `WAREHOUSE_BUCKET`: the name of the Cloud Storage bucket used as the Lakehouse catalog warehouse.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `TARGET_NAMESPACE`: the namespace of the target Lakehouse table.
  * `TARGET_TABLE`: the name of the target Lakehouse table.



### Streaming CDC pipeline

The following Java example configures a streaming pipeline that continuously polls the source Apache Iceberg table for new CDC changes:

### Java

Add the following dependencies to your `pom.xml` file:
    
    
    <dependency>
      <groupId>org.apache.beam</groupId>
      <artifactId>beam-sdks-java-managed</artifactId>
      <version>${beam.version}</version>
    </dependency>
    <dependency>
      <groupId>org.apache.beam</groupId>
      <artifactId>beam-sdks-java-io-iceberg</artifactId>
      <version>${beam.version}</version>
    </dependency>
    

The following Java snippet demonstrates how to configure and execute a streaming CDC pipeline from an Iceberg table to Lakehouse: 
    
    
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.io.iceberg.cdc.IcebergCdcMetadataColumns;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.Row;
    
    public class IcebergStreamingCdcToLakehouse {
      public static void main(String[] args) {
        Pipeline pipeline = Pipeline.create(PipelineOptionsFactory.fromArgs(args).create());
    
        // Configure source catalog properties
        Map<String, String> sourceCatalogProps = new HashMap<>();
        sourceCatalogProps.put("type", "SOURCE_CATALOG_TYPE");
        sourceCatalogProps.put("warehouse", "SOURCE_WAREHOUSE_LOCATION");
        // Add additional properties if required by your catalog type (for example, uri)
    
        // Configure streaming Iceberg CDC reader with continuous polling
        Map<String, Object> readConfig = new HashMap<>();
        readConfig.put("table", "SOURCE_NAMESPACE.SOURCE_TABLE");
        readConfig.put("catalog_properties", sourceCatalogProps);
        readConfig.put("streaming", true);
        readConfig.put("poll_interval_seconds", POLL_INTERVAL_SECONDS);
        readConfig.put(
            "include_metadata_columns",
            Arrays.asList(
                IcebergCdcMetadataColumns.CHANGE_TYPE,
                IcebergCdcMetadataColumns.COMMIT_SNAPSHOT_SEQUENCE_NUMBER));
    
        // Read streaming CDC events from source Iceberg table
        PCollection<Row> cdcRows =
            pipeline.apply(
                "ReadFromIcebergCDC",
                Managed.read(Managed.ICEBERG_CDC).withConfig(readConfig)).getSinglePCollection();
    
        // Configure destination BigLake REST Catalog properties for Lakehouse Iceberg
        Map<String, String> destinationCatalogProps = new HashMap<>();
        destinationCatalogProps.put("type", "rest");
        destinationCatalogProps.put("uri", "https://biglake.googleapis.com/iceberg/v1/restcatalog");
        destinationCatalogProps.put("warehouse", "gs://WAREHOUSE_BUCKET");
        destinationCatalogProps.put("header.x-goog-user-project", "PROJECT_ID");
        destinationCatalogProps.put("io-impl", "org.apache.iceberg.gcp.gcs.GCSFileIO");
        destinationCatalogProps.put("rest.auth.type", "google");
    
        // Configure Lakehouse Iceberg writer
        Map<String, Object> writeConfig = new HashMap<>();
        writeConfig.put("table", "TARGET_NAMESPACE.TARGET_TABLE");
        writeConfig.put("catalog_properties", destinationCatalogProps);
        writeConfig.put("mode", "merge-on-read");
        writeConfig.put("change_type_column", IcebergCdcMetadataColumns.CHANGE_TYPE);
    
        // Write CDC rows to target Lakehouse Iceberg table
        cdcRows.apply(
            "WriteToLakehouse",
            Managed.write(Managed.ICEBERG).withConfig(writeConfig));
    
        pipeline.run();
      }
    }
    

Replace the following:

  * `SOURCE_CATALOG_TYPE`: the type of the source Iceberg catalog (for example, `hadoop` or `hive`).
  * `SOURCE_WAREHOUSE_LOCATION`: the warehouse location of the source Iceberg catalog (for example, `s3://source-warehouse` or `gs://source-warehouse`).
  * `SOURCE_NAMESPACE`: the namespace of the source Iceberg table.
  * `SOURCE_TABLE`: the name of the source Iceberg table.
  * `POLL_INTERVAL_SECONDS`: the continuous polling frequency in seconds (default `60`, minimum `1`).
  * `WAREHOUSE_BUCKET`: the name of the Cloud Storage bucket used as the Lakehouse catalog warehouse.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `TARGET_NAMESPACE`: the namespace of the target Lakehouse table.
  * `TARGET_TABLE`: the name of the target Lakehouse table.



## Examine the job output

Verify that the CDC data was successfully merged into your Lakehouse table:

  1. In the Google Cloud console, go to the BigQuery **Studio** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, execute a SQL query to verify the synchronized data:
         
         SELECT * FROM `PROJECT_ID`.`CATALOG`.`NAMESPACE`.`TABLE_NAME` LIMIT 10;
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `CATALOG`: the name of your Lakehouse catalog.
     * `NAMESPACE`: the namespace of your Lakehouse table.
     * `TABLE_NAME`: the name of your target Lakehouse table.
  3. Click play_arrow**Run** and verify the results.




## What's next

  * Learn more about [Importing Iceberg tables into Lakehouse](https://docs.cloud.google.com/lakehouse/docs/import-iceberg-tables).
  * Learn about [Change data capture ingestion in Lakehouse](https://docs.cloud.google.com/lakehouse/docs/change-data-capture).
  * Learn more about [Managed I/O in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
