---
url: https://docs.cloud.google.com/lakehouse/docs/migrate-delta-lake-cdc/
title: Migrate Delta Lake change data capture (CDC) data into Lakehouse using Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:55.578740+00:00
---

# Migrate Delta Lake change data capture (CDC) data into Lakehouse using Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/migrate-delta-lake-cdc/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Migrate Delta Lake change data capture (CDC) data into Lakehouse using Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Keeping target Lakehouse Apache Iceberg tables synchronized with frequently updated Delta Lake source tables can be difficult. Performing full table reloads to capture dataset changes increases compute costs and processing latency, and building custom pipelines to process transaction logs introduces complex operational overhead.

By using Dataflow scheduled batch change data capture (CDC) pipelines, you can continuously synchronize your Delta Lake source tables with Lakehouse Apache Iceberg tables. Instead of reloading full tables, scheduled batch jobs extract incremental updates directly from your Delta Lake transaction logs and apply them to your target tables on a configurable schedule.

The scheduled batch CDC pipeline provides the following capabilities:

  * **Cost-effective incremental sync** : Periodically processes only changed data (`INSERT`, `UPDATE`, and `DELETE` operations), reducing compute overhead and data latency.
  * **Automatic change mapping** : Parses Delta Lake [Change Data Feed](https://docs.delta.io/delta-change-data-feed/) logs and maps change operations to the target Lakehouse Iceberg table.
  * **Flexible job scheduling** : Executes batch-mode Dataflow jobs on a schedule (for example, 15-minute intervals) that fits your business needs.



## Continuous migration workflow

To set up end-to-end continuous migration from Delta Lake to Lakehouse, complete the following sequence of operations:

  1. Enable the `delta.enableChangeDataFeed` property (`true`) on the input Delta Lake table.
  2. Perform an initial table migration to a commit ID or timestamp after enabling the `delta.enableChangeDataFeed` property. For instructions, see [Import Delta Lake tables into Lakehouse using Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/delta-lake-cdc-df-lakehouse-integration).
  3. Run scheduled batch CDC jobs for subsequent data updates with a frequency (commit ID or timestamp range) chosen for your workload requirements.



## Before you begin

To set up scheduled batch CDC migration, ensure you have the following:

  1. Enable the Dataflow, BigQuery, and Lakehouse APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataflow.googleapis.com,bigquery.googleapis.com,biglake.googleapis.com)

  2. To get the permissions that you need to create the resources, ask your administrator to grant you the required Identity and Access Management (IAM) roles on your project.

  3. A valid Delta Lake table stored in a Cloud Storage bucket. The table directory must contain your data files and the `_delta_log/` transaction log directory. In addition, the table must meet the following requirements:

     * The `delta.enableChangeDataFeed` property must be enabled (`true`) on the Delta Lake table.
     * The start commit ID or timestamp configured for the CDC pipeline must be after the `delta.enableChangeDataFeed` property was enabled.
  4. An existing Lakehouse Iceberg catalog to receive the synced data. If the target namespace doesn't exist, the CDC pipeline automatically creates it. If the target Lakehouse table doesn't exist, the CDC pipeline automatically creates it if you provide a valid list of equality columns.




## Support and limitations

Scheduled batch CDC migration from Delta Lake to Lakehouse has the following considerations:

  * **SDK requirement:** Requires Apache Beam SDK version 2.77.0 or greater.
  * **Destination table creation:** Creating the destination Lakehouse table is supported. If the target table doesn't exist, the CDC pipeline automatically creates it if you supply a valid list of equality columns (`equality_columns`). Only an existing Lakehouse catalog is required; the CDC pipeline automatically creates the namespace if it doesn't exist.
  * **Schema evolution:** Automatic schema changes aren't supported. If the schema of the source Delta Lake table changes, you must manually update the target Lakehouse table schema to match before running the CDC synchronization job.
  * **Batch execution mode:** Delta Lake CDC operates in batch mode. The pipeline pulls transaction logs once per job execution between specified start and end commit bounds (commit ID or timestamp). If an ending commit bound (`end_version` or `end_timestamp`) isn't specified, the pipeline reads up to the latest commit version.
  * **Supported source storage:** The source data must be a valid Delta Lake table stored in Cloud Storage (`gs://`). Amazon S3 isn't supported for Delta Lake table sources.
  * **Catalog-based tables:** Catalog-based Delta Lake tables (for example, Unity Catalog) aren't supported.
  * **Unsupported Delta Lake versions:** Delta Lake version 1.2.1 or earlier isn't supported because Change Data Feed (CDF) isn't supported for these versions.
  * **Automatic Change Data Feed:** Automatic Change Data Feed isn't supported because it doesn't write CDF change log files.



## Create a CDC pipeline programmatically

To programmatically build and run a Delta Lake CDC batch migration pipeline, use the `Managed.read` transform in your Apache Beam pipeline.

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
    
    <dependency>
      <groupId>org.apache.beam</groupId>
      <artifactId>beam-sdks-java-io-delta</artifactId>
      <version>${beam.version}</version>
    </dependency>
    

The following Java snippet demonstrates how to configure and execute a batch CDC pipeline from Delta Lake to Lakehouse. For a full Beam example, see [DeltaLakeCdcToLakehouse.java](https://github.com/apache/beam/blob/master/examples/java/iceberg/src/main/java/org/apache/beam/examples/iceberg/DeltaLakeToLakehouseCdcExample.java). 
    
    
    import java.util.Arrays;
    import java.util.HashMap;
    import java.util.Map;
    import org.apache.beam.sdk.Pipeline;
    import org.apache.beam.sdk.managed.Managed;
    import org.apache.beam.sdk.options.PipelineOptionsFactory;
    import org.apache.beam.sdk.values.PCollection;
    import org.apache.beam.sdk.values.Row;
    
    public class DeltaLakeCdcToLakehouse {
      public static void main(String[] args) {
        Pipeline pipeline = Pipeline.create(PipelineOptionsFactory.fromArgs(args).create());
    
        // 1. Configure Delta Lake CDC reader
        Map<String, Object> readConfig = new HashMap<>();
        readConfig.put("table", "gs://BUCKET_NAME/TABLE_NAME");
        // Starting commit bound (either start_version or start_timestamp must be provided):
        readConfig.put("start_version", START_COMMIT_ID);
        // Optional ending commit bound (end_version or end_timestamp, matching the start bound type):
        // readConfig.put("end_version", END_COMMIT_ID);
        readConfig.put("include_metadata_columns", Arrays.asList("_commit_version", "_change_type"));
    
        // Read CDC events from Delta Lake
        PCollection<Row> cdcRows =
            pipeline.apply(
                "ReadFromDeltaCDC",
                Managed.read(Managed.DELTA_LAKE_CDC).withConfig(readConfig)).getSinglePCollection();
    
        // 2. Configure BigLake REST Catalog properties for Lakehouse Iceberg
        Map<String, String> catalogProps = new HashMap<>();
        catalogProps.put("type", "rest");
        catalogProps.put("uri", "https://biglake.googleapis.com/iceberg/v1/restcatalog");
        catalogProps.put("warehouse", "gs://WAREHOUSE_BUCKET");
        catalogProps.put("header.x-goog-user-project", "PROJECT_ID");
        catalogProps.put("io-impl", "org.apache.iceberg.gcp.gcs.GCSFileIO");
        catalogProps.put("rest.auth.type", "org.apache.iceberg.gcp.auth.GoogleAuthManager");
    
        // 3. Map Delta Lake change types to Iceberg CDC change types
        Map<String, String> changeTypeMap = new HashMap<>();
        changeTypeMap.put("insert", "INSERT");
        changeTypeMap.put("delete", "DELETE");
        changeTypeMap.put("update_preimage", "UPDATE_BEFORE");
        changeTypeMap.put("update_postimage", "UPDATE_AFTER");
    
        // 4. Configure Lakehouse Iceberg CDC writer
        Map<String, Object> writeConfig = new HashMap<>();
        writeConfig.put("table", "TARGET_NAMESPACE.TARGET_TABLE");
        writeConfig.put("catalog_name", "lakehouse");
        writeConfig.put("catalog_properties", catalogProps);
        writeConfig.put("mode", "merge-on-read");
        writeConfig.put("sequence_number_column", "_commit_version");
        writeConfig.put("equality_columns", Arrays.asList("PRIMARY_KEY_COLUMN"));
        // change_type_column and change_type_map are only required for Portable Runner
        writeConfig.put("change_type_column", "_change_type");
        writeConfig.put("change_type_map", changeTypeMap);
    
        // Write CDC rows to target Lakehouse Iceberg table
        cdcRows.apply(
            "WriteToLakehouse",
            Managed.write(Managed.ICEBERG).withConfig(writeConfig));
    
        pipeline.run();
      }
    }
    

Replace the following:

  * `BUCKET_NAME`: the name of the Cloud Storage bucket containing the Delta Lake table.
  * `TABLE_NAME`: the name of the source Delta Lake table directory.
  * `START_COMMIT_ID`: starting commit version number for reading Delta Lake CDC events. Either `start_version` or `start_timestamp` must be provided. The start commit ID or timestamp must be after the `delta.enableChangeDataFeed` property was enabled on the source table.
  * `END_COMMIT_ID`: ending commit version number for reading Delta Lake CDC events. As a best practice, specify an ending bound (`end_version` or `end_timestamp`) that matches the bound type used for start (`start_version` or `start_timestamp`). If an ending bound is omitted, the pipeline reads up to the latest commit version.
  * `WAREHOUSE_BUCKET`: the name of the Cloud Storage bucket used as the Lakehouse catalog warehouse.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `TARGET_NAMESPACE`: the namespace of the target Lakehouse table.
  * `TARGET_TABLE`: the name of the target Lakehouse table.
  * `PRIMARY_KEY_COLUMN`: the primary-key column name used to identify rows for CDC updates and deletes. 
  * Add any additional dependencies needed for Delta Lake and Iceberg based on the [Beam example](https://github.com/apache/beam/blob/master/examples/java/iceberg/build.gradle).

**Note:** The `change_type_column` and `change_type_map` properties are only required when running the pipeline with the [Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner).

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

  * Learn more about [Importing Delta Lake tables into Lakehouse](https://docs.cloud.google.com/lakehouse/docs/import-delta-lake-tables).
  * Learn about [Change data capture ingestion in Lakehouse](https://docs.cloud.google.com/lakehouse/docs/change-data-capture).
  * Learn more about [Managed I/O in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/managed-io).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
