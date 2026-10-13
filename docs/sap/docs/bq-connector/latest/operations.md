---
url: https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations/
title: BigQuery Connector for SAP operations guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:25.029517+00:00
---

# BigQuery Connector for SAP operations guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/latest/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  BigQuery Connector for SAP operations guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows SAP LT Replication Server administrators, SAP data engineers, or others how to perform operational tasks, such as performance tuning and version updates, for **version 2.15(latest)** of the BigQuery Connector for SAP.

The operational tasks and tools available to you depend on whether your replication target is BigQuery or Cloud Storage.

## Tuning replication performance

The guidance in this section applies only to replicating SAP data to BigQuery by using the BigQuery Connector for SAP.

For replication to Cloud Storage, the connector offers delivery of JSON files to your Cloud Storage bucket. Because this replication path is decoupled from BigQuery, loading data into BigQuery is a separate step. Consequently, your end-to-end replication performance is driven by the custom ingestion tools and configuration that you use for your post-Cloud Storage pipeline.

In general, replication performance can be affected by multiple factors. The specific factors that apply can be different from installation to installation and can change over time.

For more information about replication performance with the BigQuery Connector for SAP, see [Performance planning](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#performance).

### Set performance options for tables

In SAP LT Replication Server you can specify replication options for each table that affect performance.

In particular, the replication performance for large tables, which require more time and resources to replicate, can benefit from specifying ranges and increasing the maximum number of parallel replication jobs that can be used for the table.

Examples of tables that commonly grow large are `MSEG`, `ACDOCA`, and `MATDOC`, among others.

When you specify parallel replication jobs for large tables, you need to balance the number of parallel jobs that you allow for any given table against the total number of parallel jobs that are allowed in the mass transfer configuration. Your organization might also limit the number of parallel replication jobs that you can specify for a given server.

To set performance options for a table:

  1. In the SAP GUI, enter SAP transaction `LTRS`.

  2. On the **Advanced Replication Settings** screen, specify the ID of the mass transfer settings for the table.

  3. In the **Advanced Replication Settings** folder hierarchy, click the **Performance Options** folder to display the tables that have performance options defined.

  4. If the table you need isn't listed, right-click the **Performance Options** folder, and then select **Add Table**.

  5. Specify a name for the Table.

  6. Specify the following options as needed:

     * Under **General Performance Options** : 
       * **No. of Parallel Jobs** , to set the maximum number of parallel replication jobs that can be used for the table.
       * **Sequence Number** , to prioritize the replication of this table relative to other table replications.
     * Under **Initial Load Options** : 
       * For **Reading Type** , select **Reading Type 1 Range Calculation** , if your table is not too large. For more information, see [Performance and the LTRS Advanced Replication Settings](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#perf-reading-types).
       * For **Package Size** , specify the size in bytes of the portions of records that are sent to SAP LT Replication Server.
       * If you select a Reading Type that uses ranges, then define appropriate ranges.
     * Under **Replication Option** : 
       * For **Ranges for Logging Table** , specify **No Ranges** for the most reliable option.
       * If you select **Specify Ranges for Manually** , then define appropriate ranges.
  7. Click **Save**.




### Baseline performance benchmark

To help you evaluate your replication performance, this section contains baseline performance numbers that were observed in Google Cloud test systems, for both [CDC replication to BigQuery through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#cdc-replication-with-pubsub) and [streaming data replication to BigQuery](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#streaming-api-insert-only).

Due to the [many different factors that affect performance](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#performance-best-practices), your performance numbers are likely to vary.

For example, if your SAP systems are not running on Google Cloud, your load and replication rates might be slower than the baseline rates due to things like network latency and the overhead associated with access tokens. If your source table has fewer columns or you install SAP LT Replication Server on its own server in a standalone architecture, then your rates might be faster because SAP LT Replication Server doesn't have to compete with the source system for resources.

#### CDC replication to BigQuery through Pub/Sub: Observed baseline performance numbers

For [CDC replication to BigQuery through Pub/Sub](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#cdc-replication-with-pubsub), the following performance numbers represent the baseline performance that was observed by Google Cloud for each source system type during testing. In each test system, SAP LT Replication Server was installed on the SAP source system in an embedded architecture on Compute Engine VMs. The SAP source system was running in the same Google Cloud region as the target BigQuery dataset.

For information about the configuration of the test systems, see Baseline performance test system configuration.

To see the performance numbers, click your source system type:

###  S/4HANA 

  * Table: ACDOCA 
    * 343 million records
    * 477 columns
  * Initial load 
    * **Load rate:** 280 million records per hour on average
    * **Load duration:** 73.5 minutes on average
  * Replication 
    * **Source table change rate:** 40 million records per hour on average
    * **Maximum replication rate:** 40 million records per hour on average



###  ECC 

  * Table: MSEG 
    * 300 million records
    * 188 columns
  * Initial load 
    * **Load rate:** 308 million records per hour on average
    * **Load duration:** 58 minutes on average
  * Replication 
    * **Source table change rate:** 40 million records per hour on average
    * **Maximum replication rate:** 55.2 million records per hour on average



The preceding performance numbers are the baselines that the Google Cloud testers observed.

The observed performance was better in test systems that had the following attributes:

  * SAP LT Replication Server was installed on its own VM in a standalone architecture. 
    * For S/4HANA systems, a standalone architecture was observed to have an initial load rate approximately 42% faster than an embedded architecture due to the independent scaling of the SAP LT Replication Server processes.
    * For ECC systems, a standalone architecture was observed to have an initial load rate approximately 10% faster than an embedded architecture due to the independent scaling of the SAP LT Replication Server processes.
  * The source table had fewer columns.
  * The overall byte size of the records was smaller.



For information about the system attributes that you can modify to improve performance, see:

  * Tuning replication performance
  * [Performance planning](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#performance)



#### Streaming data replication to BigQuery: Observed baseline performance numbers

For [streaming data replication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#streaming-api-insert-only), the following performance numbers represent the baseline performance that was observed by Google Cloud for each source system type during testing. In each test system, SAP LT Replication Server was installed on the SAP source system in an embedded architecture on Compute Engine VMs. The SAP source system was running in the same Google Cloud region as the target BigQuery dataset.

For information about the configuration of the test systems, see Baseline performance test system configuration.

To see the performance numbers, click your source system type:

###  S/4HANA 

  * Table: ACDOCA 
    * 343 million records
    * 477 columns
  * Initial load 
    * **Load rate:** 350 million records per hour on average
    * **Load duration:** 59 minutes on average
  * Replication 
    * **Source table change rate:** 50 million records per hour on average
    * **Maximum replication rate:** 50 million records per hour on average



###  ECC 

  * Table: MSEG 
    * 203 million records
    * 188 columns
  * Initial load 
    * **Load rate:** 385 million records per hour on average
    * **Load duration:** 32 minutes on average
  * Replication 
    * **Source table change rate:** 50 million records per hour on average
    * **Maximum replication rate:** 69 million records per hour on average



The preceding performance numbers are the baselines that the Google Cloud testers observed.

The observed performance was better in test systems that had the following attributes:

  * SAP LT Replication Server was installed on its own VM in a standalone architecture. 
    * For S/4HANA systems, a standalone architecture was observed to have an initial load rate approximately 42% faster than an embedded architecture due to the independent scaling of the SAP LT Replication Server processes.
    * For ECC systems, a standalone architecture was observed to have an initial load rate approximately 10% faster than an embedded architecture due to the independent scaling of the SAP LT Replication Server processes.
  * The source table had fewer columns.
  * The overall byte size of the records was smaller.



For information about the system attributes that you can modify to improve performance, see:

  * Tuning replication performance
  * [Performance planning](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#performance)



#### Baseline performance test system configuration

The test systems described in this section produced the baseline performance numbers that are listed in the preceding sections, Baseline performance benchmark.

The test systems, including the SAP source system, the SAP LT Replication Server, and the BigQuery dataset, were all running on Compute Engine VMs in the same Google Cloud region.

In each system, the servers and the workload were designed to simulate a heavier workload and higher replication volume that you are likely to find in many real-world installations.

To see the test system attributes, click your source system type:

###  S/4HANA 

  * **SAP LT Replication Server installation architecture** : 
    * Embedded architecture
  * **Source system servers:**
    * Two application servers, each on an N2-based Compute Engine [custom machine type](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) with the following specifications: 
      * vCPUs: 60
      * Memory: 324 GB
      * CPU platform: Intel Cascade Lake
    * One SAP HANA server on an `m1-ultramem-80` Compute Engine VM with the following specifications: 
      * vCPUs: 80
      * Memory: 1,900 GB
      * CPU platform: Intel Broadwell
  * **Software versions:**
    * S/4HANA 1909
    * SAP LT Replication Server: S/4CORE 104 SP00
  * **Table size:**
    * Table name: ACDOCA, general ledger journal entry line item data
    * Number of records: 343 million
    * Number of columns: 477
  * **Work processes on each application server:**
    * 60 Dialog processes
    * 220 Background processes
  * **Load settings in SAP LT Replication Server:**
    * Jobs: 99
    * Reading type: 1 Range
    * Calculation: Auto-ranges
  * **Replication settings:**
    * Jobs: 99
    * Use Key fields to calculate ranges for logging table
    * 128 ranges



###  ECC 

  * **SAP LT Replication Server installation architecture** : 
    * Embedded architecture
  * **Source system servers:**
    * Two application servers, each on an `n2-highmem-48` Compute Engine VM with the following specifications: 
      * vCPUs: 60
      * Memory: 348 GB
      * CPU platform: Intel Cascade Lake
  * **Software versions:**
    * SAP NetWeaver: 7.0 EHP2
    * SAP LT Replication Server: DMIS 2011_1_700 SP17
  * **Table size:**
    * Table: MSEG, materials inventory management documents
    * Number of records: 203 million
    * Number of columns: 188
  * **Work processes on each application server:**
    * 60 Dialog processes
    * 100 Background processes
  * **Load settings in SAP LT Replication Server:**
    * Jobs: 99
    * Reading type: 5 Sender
    * Queue: Manual ranges
  * **Replication settings:**
    * Jobs: 99
    * Ranges for Logging Table: Use Key fields to calculate ranges
    * Number of ranges: 128



## Dynamic chunk size

If you come across errors because the byte size of the chunks exceeds the maximum byte size for HTTP requests that BigQuery accepts, then you need to reduce the byte size manually by reducing the chunk size. The dynamic chunk size feature lets you automatically reduce the chunk size and retry replication to BigQuery when the byte size of a chunk exceeds the maximum byte size for HTTP requests that BigQuery accepts. Dynamic chunk size helps you prevent most replication failures due to exceeding byte size of a request. You might receive an error only if the chunk size reaches 1, but the byte size remains more than the BigQuery limit on the number of bytes in each HTTP request.

You enable dynamic chunk size in the mass transfer configuration for a table by using transaction `/GOOG/SLT_SETTINGS`. Dynamic chunk size is an optional setting. For information about how to enable dynamic chunk size, see:

  * For CDC replication to BigQuery through Pub/Sub, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#configure-connection).
  * For streaming data replication to BigQuery, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#configure-connection).
  * For file-based replication to Cloud Storage, see [Specify general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-gcs-file-replication#specify-general-attributes-gcs).



When you enable dynamic chunk sizing, the BigQuery Connector for SAP's maximum chunk size aligns with underlying service quota limits:

  * For CDC replication to BigQuery through Pub/Sub: The Pub/Sub quota limits, which is 1,000 records.
  * For streaming data replication to BigQuery: The BigQuery quota limits, which is 50,000 records.
  * For file-based replication to Cloud Storage: The Cloud Storage quota limits, which is 50,000 records.



For more information about chunk size, see [Portion size and chunk size](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#perf-transmission-data-chunk-size).

**How dynamic chunk size works**

With dynamic chunk size, if the HTTP request with initial chunk size exceeds the BigQuery limit on byte size, then BigQuery Connector for SAP reduces the chunk size and retries to send the data. BigQuery Connector for SAP keeps on reducing the chunk size and retries to send the data to BigQuery, until the data is transferred successfully for a particular chunk or until the chunk size reaches 1.

The final reduced chunk size, for which the data transfer was successful, is then used as the chunk size for all the remaining chunks of that portion. You can find the final reduced chunk size that was successful for each portion in the [SAP LT Replication Server application logs](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting#logs-slt) as an information message:

`Dynamic chunking triggered. Chunk size reduced from INITIAL_CHUNK_SIZE_VALUE to FINAL_REDUCED_CHUNK_SIZE_VALUE`.

For the subsequent portions and any subsequent replications, BigQuery Connector for SAP starts sending data to BigQuery with the chunk size configured in transaction `/GOOG/SLT_SETTINGS` and keeps on reducing the chunk size if dynamic chunking is triggered.

By default, the chunk size is reduced by 50% after each retry. If you want to reduce the chunk size by a lower or higher percentage, then modify the advanced settings parameters.

Let us understand with an example how chunk size is determined in the replication process when dynamic chunk size is enabled for a table. For this example, CDC replication to BigQuery through Pub/Sub is used. When the SAP LT Replication Server portion size is larger than BigQuery Connector for SAP chunk size and the chunk size of 1,000 records is defined in transaction `/GOOG/SLT_SETTINGS`. BigQuery Connector for SAP replicates a portion to BigQuery as follows:

  1. When replication starts for a portion that contains 2,000 records, the chunk size for the first chunk is 1,000 records, but if the byte size for HTTP request is greater than 10 MB, then BigQuery Connector for SAP reduces the chunk size by 50%, and the new chunk size becomes 500 records.

  2. BigQuery Connector for SAP retries to send the chunk size of 500 records, but if the byte size for HTTP request is still greater than 10 MB, then BigQuery Connector for SAP reduces the chunk size further by 50%, and the new chunk size becomes 250 records.

  3. BigQuery Connector for SAP retries to send the chunk size of 250 records, now if the byte size for the HTTP request for this chunk is smaller than 10 MB, then the replication succeeds and data is inserted into BigQuery.

  4. The chunk size for all subsequent chunks becomes 250 records as long as the byte size for each HTTP request is less than 10 MB. If the byte size of HTTP request for any subsequent chunk exceeds 10 MB, then BigQuery Connector for SAP again reduces the chunk size and retries to send the data to BigQuery, until the data is transferred successfully for a particular chunk. The reduced chunk size is used only for the current portion of the current replication.




**Performance with dynamic chunk size**

Dynamic chunk size can affect the performance of replication to BigQuery. For every chunk, BigQuery Connector for SAP calculates the number of records in a chunk and checks the byte size of HTTP requests. If the byte size is greater than 10 MB, then BigQuery Connector for SAP reduces the chunk size and retries to send the data to BigQuery that increases the overall replication time.

Use dynamic chunk size only in specific situations, where even after configuring an ideal chunk size for some data records, the request size might exceed the HTTP request limit of BigQuery and you don't want to receive a chunk size error. For example:

  * Source tables that contain large variance in sparsity of the data in the fields, that is, for some records fewer fields are maintained whereas for some records many fields are maintained.
  * Source tables that contain long text fields such as `EDID4-SDATA`, `VARI-CLUSTID`, and `REPOSRC-DATA`.



You can also use dynamic chunk size during your testing phase to identify an ideal chunk size for a table that you can define in your production SAP system.

**Note:** Google Cloud recommends that you manually configure a chunk size that is close to an ideal chunk size depending on the data in your table.

For more information about configuring the chunk size, see:

  * For CDC replication to BigQuery through Pub/Sub, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#configure-connection).
  * For streaming data replication to BigQuery, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#configure-connection).



## Table schema caching

To optimize replication performance and avoid exceeding BigQuery API quota limits, you can enable table schema caching. Enabling this setting reduces the number of `tables.get` calls that the connector makes to the BigQuery API.

When you enable table schema caching, BigQuery Connector for SAP stores table schema details in SAP ABAP Shared Objects memory. The connector then retrieves schema details from memory instead of querying the BigQuery API to verify table existence. If the schema remains unchanged, the connector bypasses the API call.

To enable table schema caching, perform the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. From the **Settings Table** drop-down menu, select **Parameters**.

  3. Click the **Execute** icon.

  4. Click the **Insert Row** icon.

  5. In the displayed row, specify the following settings:

     1. In the **Parameter Name** field, enter `SCH_CACHE_ENABLE`. The parameter description is automatically populated.
     2. In the **Parameter Value** field, specify `X`.
  6. Click **Save**.




## Cache Validations

The Cache Validations feature is available only with the CDC replication to BigQuery through Pub/Sub.

The Cache Validations feature, used particularly during initial data loads, significantly improves the performance of data transfer calls from SAP to Google Cloud by caching pipeline validation results after the first successful check. This eliminates redundant validation steps for subsequent data transfers, saving time and resources.

This is a recommended setting, particularly during the initial data load phase. To enable this feature, you select the **Cache Val (Cache Validations)** checkbox in the `/GOOG/SLT_SETTINGS` transaction. For information about enabling this feature, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#table-attributes).

When this setting is active, the BigQuery Connector for SAP performs an initial check to confirm that the Google Cloud pipeline is correctly set up and consistent with the table schema defined in SAP. This pipeline comprises the Pub/Sub topic, its schema, the BigQuery subscription, and the target BigQuery table. After this initial validation and pipeline creation, the results are stored in SAP shared memory. For all subsequent data transfer calls, this validation step is then skipped, optimizing performance by reducing redundant checks.

### Clear the cached validation

When the Cache Validations feature is enabled and you update the SAP table definition, the structural changes are updated only after the existing cached validation expires. In such situations, you can clear the cached validation results manually. To clear the cached validation results, execute the transaction `SE38`, and then run the program `/GOOG/R_GCP_CLEAR_CACHE` or execute the transaction `/GOOG/BQPS_CLR_CACHE`.

### Clean up Google Cloud artifacts

For development environments, to remove Google Cloud resources linked to a mass transfer ID, you can use the program `/GOOG/R_CLEANUP_CPS_ARTIFACTS`. This program deletes the associated Pub/Sub topic, its Pub/Sub schema, and the BigQuery subscription.

**Caution:** This program is strictly for development environments only. Deleting the Google Cloud pipeline can affect dependent processes. If a Pub/Sub topic has multiple subscriptions, then running this program could orphan those not associated with the specific mass transfer ID, potentially leading to data loss.

## Transport mass transfer settings to production

To transport mass transfer settings to production, you first export the settings from a development system, and then import them into the production system.

You can, optionally, import three separate parts of the settings of a mass transfer into production:

  * The advanced replication settings, which can be accessed by using the `LTRS` transaction.
  * The client key settings from the `/GOOG/CLIENT_KEY` table, which can be accessed by using the `SM30` transaction.
  * The BigQuery Connector for SAP the mass transfer settings, which can be accessed by using the `/GOOG/SLT_SETTINGS` transaction.

**Note:** Before you move mass transfer settings to production, validate the settings in a QA or sandbox environment.

### Export mass transfer settings from a development system

In the SAP LT Replication Server development system, export each part of the mass transfer settings:

  1. Export the advanced replication settings:

     1. Run the `LTRS` transaction.
     2. Select the mass transfer records that you are transporting to production.
     3. From the **File** drop-down menu, select **Export All Settings**.
     4. In the **Export Settings** dialog, select a destination and click **Save**. The settings are saved in a compressed file in CSV format on your local workstation.
  2. Export the BigQuery Connector for SAP mass transfer settings:

     1. Run the `/GOOG/SLT_SETTINGS` transaction:
            
            /n/GOOG/SLT_SETTINGS

     2. In the **Settings Table** field, select **Mass Transfer**.

     3. Select the mass transfer records that you are transporting to production.

     4. Click **Transport Mass Transfer**.

     5. In the **Prompt for Workbench request** , enter the transport request number and click the **Continue** icon. For each selected mass transfer record, the settings from the following custom configuration tables are included in the transport:

        * `/GOOG/BQ_MASTR`
        * `/GOOG/BQ_TABLE`
        * `/GOOG/BQ_FIELD`

The mass transfer settings are saved to a transport request.

  3. Export the client key settings by manually including the contents of the `/GOOG/CLIENT_KEY` table in the transport request.

  4. Save the files to your local workstation.




### Import mass transfer settings into a production system

In the SAP LT Replication Server production system, import each part of the mass transfer settings:

  1. Create an SAP LT Replication Server replication configuration for the mass transfer settings.

  2. Import the advanced replication settings:

     1. Run the `LTRS` transaction.
     2. Select the mass transfer that you created in the first step.
     3. From the **File** drop-down menu, select **Import All Settings**.
     4. In the **Choose File** dialog, select the compressed file from your local workstation and click **Open**. The settings are imported as settings for the mass transfer.
  3. Import the transport request that contains the mass transfer settings.

  4. Run the `SM30` transaction.

  5. Update the client key settings as necessary for the production environment.

  6. Run the `/GOOG/SLT_SETTINGS` transaction:
         
         /n/GOOG/SLT_SETTINGS

  7. Verify that the correct mass transfers are displayed in the **Mass Transfers** screen.

  8. In the **Mass Transfer ID** column, replace the mass transfer ID from the development system with the mass transfer ID from the replication configuration that you created in the first step.

  9. In the subsequent **Tables** and **Fields** settings screens, update other values for the table and field mapping as necessary for the production environment.

  10. Test the configuration by starting an initial load or replication.




## Update BigQuery Connector for SAP

Google Cloud delivers new releases of the BigQuery Connector for SAP as SAP transports.

**Note:** For information about version releases of BigQuery Connector for SAP, see [What's new with BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new).

SAP administrators can update BigQuery Connector for SAP by following these steps:

  1. Deactivate the configuration in SAP LT Replication Server.
  2. Import the new SAP transport request.
  3. After validating the successful import and object activation, activate the configuration in SAP LT Replication Server.



## Update the gcloud CLI

You need to keep the Google Cloud CLI updated on the SAP LT Replication Server host.

For more information about managing the gcloud CLI, see [Managing gcloud CLI components](https://docs.cloud.google.com/sdk/docs/components).

## Monitoring

You can monitor several different points along the data path from the SAP data source to the target BigQuery table, including:

  * Infrastructure - network, hardware and operating system
  * The SAP database layer
  * The SAP application layer
  * BigQuery Connector for SAP
  * BigQuery
  * Pub/Sub
  * Cloud Storage



Your options for monitoring at each of these points are presented in the following subsections.

### Monitoring the infrastructure

On Google Cloud, you can install the Ops Agent on your host VMs for advanced monitoring and logging. The Ops Agent sends the data to Cloud Monitoring in the Google Cloud console.

For more information, see:

  * [Ops Agent overview](https://docs.cloud.google.com/monitoring/agent/ops-agent)
  * [Introduction to Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



For systems that are not running on Google Cloud, you can also get server information by running SAP transactions, such as transaction `ST06`.

### Monitoring the database layer

Use standard SAP transaction codes to monitor the health of the database.

The transaction code `DBACOCKPIT` is the most common transaction for monitoring the database. This transaction also provides detailed logs that you can use for troubleshooting errors.

For SAP HANA, you can use SAP HANA Studio for SAP HANA operations. You can install SAP HANA Studio on any frontend machine.

When troubleshooting performance or other issues, check the following things in the source database:

  * Expensive SQL Statements
  * Locks
  * Load history
  * Indexes
  * Processes



### Monitoring the application layer

You can use SAP application monitoring and troubleshooting tools to monitor and troubleshoot BigQuery Connector for SAP, because it runs in the application layer.

SAP application monitoring and troubleshooting can be further classified into the following:

  * Standard SAP monitoring and troubleshooting
  * BigQuery Connector for SAP monitoring and troubleshooting



For larger landscapes, you can use the [SAP Solution Manager](https://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/b80ac35796fa0e2be10000000a441470.html) as a central monitoring tool.

You can use the SAP transaction codes in the following list to monitor and diagnose issues on individual SAP application systems:

  * SLT configuration status: `LTRC`
  * SLT errors and logs: `LTRO` and `SLG1`
  * Internet Communication Manager (HTTP and HTTPS Calls): `SMICM`
  * Security and certificates: `STRUST`
  * SAP transports: `STMS`
  * RFC connections: `SM59`
  * OS command: `SM69`
  * Package check: `SE80`
  * Authorization checks: `SU53`
  * Background jobs: `SM37`
  * System logs: `SM21`



### Monitoring Pub/Sub

Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring) to view Pub/Sub metrics and to create charts and alerts. Each metric is associated with a resource type, either `pubsub_topic` or `pubsub_subscription`, and also includes a set of labels that provide additional dimensions for filtering and analysis.

While you can still use the [Monitoring Query Language (MQL)](https://docs.cloud.google.com/monitoring/mql) for existing configurations, we recommend that you use the [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql) for building new queries. PromQL provides a powerful and flexible way to analyze your Pub/Sub data, aligning with industry standards for observability.

For more information about Monitoring, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

### Monitoring dead-letter topic for failed messages

A dead-letter topic in Pub/Sub is a dedicated topic where messages that cannot be successfully processed by a subscription are sent after a configured number of delivery attempts. To identify and investigate failed messages, preventing data loss and understanding the health of your message processing, you need to monitor your dead-letter topic.

To effectively monitor your dead-letter topic, you typically set up a subscription to your dead-letter topic that you define in your mass transfer configuration. You then monitor this specific subscription using the same `pubsub_subscription` resource type and its associated metrics.

#### Key dead-letter topic metrics

To understand how to query metrics for your dead-letter topic subscription, explore the following PromQL examples:

  * **Count of messages forwarded to the dead-letter topic** : This is the most crucial metric for understanding if messages are failing. 
        
        sum(rate(pubsub_googleapis_com:subscription_dead_letter_message_count{subscription_id="DEAD_LETTER_TOPIC_SUBSCRIPTION_ID"}[5m]))
        

  * **Number of unacknowledged messages in the dead-letter topic** : This indicates messages sitting in the DLQ awaiting processing or review. A persistently high or increasing number suggests a problem that needs attention. 
        
        pubsub_googleapis_com:subscription_num_unacked_messages{subscription_id="DEAD_LETTER_TOPIC_SUBSCRIPTION_ID"}
        

  * **Age of the oldest unacknowledged message in the dead-letter topic** : A rising value here indicates a growing backlog of failed messages that aren't being addressed. 
        
        pubsub_googleapis_com:subscription_oldest_unacked_message_age{subscription_id="DEAD_LETTER_TOPIC_SUBSCRIPTION_ID"}
        

  * **Backlog size (bytes) in the dead-letter topic** : Provides insight into the volume of data in your dead-letter topic. 
        
        pubsub_googleapis_com:subscription_backlog_bytes{subscription_id="DEAD_LETTER_TOPIC_SUBSCRIPTION_ID"}
        




#### Best practices for dead-letter topic monitoring

For dead-letter topic monitoring, apply the following best practices:

  * **Create dedicated alerts** : Set up alerts for increases in `pubsub_googleapis_com:subscription_num_unacked_messages` or `pubsub_googleapis_com:subscription_oldest_unacked_message_age` on your dead-letter topic subscription.

  * **Dashboard for dead-letter topic** : Create a dedicated dashboard in Monitoring to visualize the health of your dead-letter topic across your project.

  * **Human intervention** : Messages in the dead-letter topic often require manual inspection and intervention to understand the root cause of failure, for example, malformed data, application bugs, and external service outages.

  * **Automated reprocessing (with caution)** : For certain predictable failures, you might implement automated processes, such as Cloud Run functions, Dataflow jobs, to consume messages from the dead-letter topic, attempt to fix them, and re-publish them to the original topic. Handle this with extreme care to avoid infinite loops.




### Monitoring BigQuery

Use Monitoring to view BigQuery metrics and create charts and alerts. Each metric has a resource type, either `bigquery_dataset`, `bigquery_project`, or `global`, as well as a set of labels.

Use the resource types and labels to build queries in the [Monitoring Query Language (MQL)](https://docs.cloud.google.com/monitoring/mql).

You can group or filter each metric by using the labels.

For more information about Monitoring, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

## View the connector settings

To view the mass transfer settings of BigQuery Connector for SAP, in SAP GUI, execute the transaction `/GOOG/SLT_SETT_DISP`.

## View the connector version

To view the version of the BigQuery Connector for SAP installed on your system, in SAP GUI, execute the transaction `/GOOG/BQC_VERSION`.

## Connector utilities

The BigQuery Connector for SAP provides the following utilities that help you streamline data operations and optimize performance through features like data preparation, validation, transformation, and load simulation:

Utilities | Streaming data replication to BigQuery | CDC replication to BigQuery through Pub/Sub | File-based replication to Cloud Storage  
---|---|---|---  
Create Table tool | Supported | Not supported | Not supported  
Mass Field Conversion tool | Supported | Not supported | Not supported  
Load Simulation tool | Supported | Not supported | Not supported  
Replication Validation tool | Supported | Not supported | Not supported  
Stream Records tool | Not supported | Supported | Not supported  
  
### Create Table tool

This tool is not supported for CDC replication to BigQuery through Pub/Sub and file-based replication to Cloud Storage.

For empty source tables in SAP, SAP SLT prevents the creation of target tables in BigQuery. If you need to create the target tables in the BigQuery dataset for empty source tables, then you can use the Create Table tool.

To run the Create Table tool, follow these steps:

  1. In SAP GUI, execute the transaction `/GOOG/CREATE_BQ_TAB` preceded by `/n`:
         
         /n/GOOG/CREATE_BQ_TAB

  2. On the **Create target tables from BQ settings** screen, provide values for the following fields:

     * **Mass transfer key** : the mass transfer key that contains the SAP tables.
     * **SAP table name** : the SAP table names that you need to create.
  3. Click the **Execute** icon. The target tables are created in the BigQuery dataset.

  4. Optionally, verify in the BigQuery dataset if the table has been created with the correct schema.




### Mass Field Conversion tool

This tool is not supported for CDC replication to BigQuery through Pub/Sub and file-based replication to Cloud Storage.

Although BigQuery Connector for SAP automatically suggests the BigQuery data types for most fields, you might need to map the fields manually. Rather than manually assigning the data type to each field, you can use the Mass Field Conversion tool to map the data type assignment for all fields in the field mapping screen of the `/GOOG/SLT_SETTINGS` transaction. The Mass Field Conversion tool converts all field mappings for a table to the `STRING` type on BigQuery.

If a table is already being replicated or is added for initial load in the `LTRC` transaction, then don't use the Mass Field Conversion tool for such tables as it can result in schema mismatch issues. You can only use this tool for the SAP tables for which initial load or replication has not started.

To run the Mass Field Conversion tool, follow these steps:

  1. In SAP GUI, execute the transaction `/GOOG/MASS_CNVT_FMAP` preceded by `/n`:
         
         /n/GOOG/MASS_CNVT_FMAP

  2. On the **Mass field conversion** screen, provide values for the following fields:

     * **Mass transfer key** : the mass transfer key that contains the SAP tables.
     * **SAP table name** : the SAP table names for which you need all the field mappings to be converted to the `STRING` type.
  3. Click the **Execute** icon. For the selected tables, all the field mappings are converted to the `STRING` type.




### Load Simulation tool

This tool is not supported for CDC replication to BigQuery through Pub/Sub and file-based replication to Cloud Storage.

This section provides an overview of the Load Simulation tool and what you can do with it.

The Load Simulation tool is a support tool for BigQuery Connector for SAP that lets you simulate the replication of SAP data into BigQuery. The tool is part of the transport that Google Cloud provides for BigQuery Connector for SAP. You use the Load Simulation tool to replicate source SAP data into BigQuery by directly invoking the [Business Add In (BAdI)](https://help.sap.com/viewer/46a2cfc13d25463b8b9a3d2a3c3ba0d9/LATEST/en-US/8ff2e540f8648431e10000000a1550b0.html) of BigQuery Connector for SAP. Because the Load Simulation tool doesn't use the underlying SLT framework, the SLT triggers are not impacted. Don't use the Load Simulation tool for data replication in production environments.

The Load Simulation tool provides a report that you can analyze to assess replication performance, identify potential problems, understand the root cause of issues, and resolve them prior to actual replication of SAP data into BigQuery by using BigQuery Connector for SAP.

The following are some common use cases where you can use the Load Simulation tool:

  * Reproduce and troubleshoot any network connectivity, authorization, or authentication issues.
  * Generate enhanced logs of the BigQuery API calls for troubleshooting issues.
  * For any troubleshooting assistance from Cloud Customer Care, run the Load Simulation tool and provide logs to the Customer Care team.
  * Measure performance metrics by providing the time taken for each step in the replication process.
  * For SAP LT Replication Server in an embedded architecture, determine an optimal chunk size for the SAP tables.



Use a sample mass transfer configuration with the Load Simulation tool that you create using the custom transaction `/GOOG/SLT_SETTINGS`. Don't use your production dataset and BigQuery tables for running the Load Simulation tool.

When your SAP LT Replication Server is in an embedded architecture, you run the Load Simulation tool with the standard SAP tables such as `MARA` and `T001`.

When your SAP LT Replication Server is in a standalone architecture, you run the Load Simulation tool with the sample table `/GOOG/TEST_REPL` that Google Cloud provides with the BigQuery Connector for SAP. The Load Simulation tool does not support reading source tables from a remote system.

For more information about installation architectures, see [Deployment architectures](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#deployment_architectures).

#### Prerequisites

Before you run the Load Simulation tool, make sure that the following prerequisites are satisfied:

  * BigQuery Connector for SAP is installed and configured. For information about the installation and configuration steps, see [Install BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/install) and [Configure the connector for streaming data replication](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api).

  * The intended users have access to the custom transaction `/GOOG/LOAD_SIMULATE` that is provided by Google Cloud. For more information, see [Create SAP roles and authorizations for BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#bqc4sap-define-authorized-sap-roles).




#### How to run the Load Simulation tool

To run the Load Simulation tool, follow these steps:

  1. In the SAP GUI, enter the `/GOOG/LOAD_SIMULATE` transaction preceded by `/n`:
         
         /n/GOOG/LOAD_SIMULATE

  2. Click the **Execute** icon. The **SLT Load Simulation** screen displays.

  3. In the **Processing Options** , make sure that the **Execute Simulation** option is selected.

  4. In the **Selection Options** section, enter the following specifications:

     * From the drop-down menu in the **Google Cloud Partner** field, select **BigQuery**.
     * In the **Mass Transfer Key** field, enter the mass transfer key for the mass transfer configuration.

Use a sample mass transfer configuration with the Load Simulation tool. Don't use your production dataset and BigQuery tables.

     * In the **Table Name** field, enter the name of the source SAP table that you provided in the sample mass transfer configuration.

     * Optionally, in the **Where Condition** field, enter a condition for data selection from the source table.

You can enter up to 255 characters. For example, if you run the Load Simulation tool for SAP table `MARA`, and you need to select material number from a specific range, then for **Where Condition** , specify a value like `MATNR GE '000000000400000001' AND MATNR LE '000000000600000001'`.

     * In the **Cycle Count** field, enter the number of processing cycles that the Load Simulation tool runs.

This is helpful when you need to compare how the simulation report is coming up in multiple cycles. The value must be greater than 1.

     * In the **Record Count per cycle** field, enter the number of records that you want to send to BigQuery in each processing cycle. The value must be greater than 1.

     * In the **Portion size** field, enter the number of records out of the **Records Count per cycle** that SAP LT Replication Server sends to BAdI of BigQuery Connector for SAP in each portion.

     * Select one or more flags as appropriate:

       * **Exact Records Count** : Indicates that exactly the same number of records provided in the **Record Count per cycle** field are sent to BigQuery in each processing cycle. If the table does not have enough records, then the Load Simulation tool duplicates the existing records to achieve the required count. The records are duplicated only to insert data into BigQuery and not to insert data in the source table.

       * **Use SLT Target Structure** : Uses structure of the SLT logging table to get the source table fields. If this flag is not set, then fields are read directly from the source table to generate the target structure. For more information about SAP LT Replication Server data flow, see [Detailed architectural view of the data flow](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#architecture-slt-data-flow-streaming-api-append-only).

       * **Detailed Log** : Indicates that the log records are created for all defined methods in the BigQuery Connector for SAP. If this flag is not set, then only important methods are logged.

       * **Clear Previous Results** : Clears previously created log records for the same mass transfer and SAP table. If the flag is not set, then the logs are appended to the previous results.

  5. To run the Load Simulation tool, click the **Execute** icon.

  6. After the load simulation is complete, in the **Processing Options** section, select the **Display Report** radio button.

  7. In the **Selection Options** section, enter the following specifications:

     * From the drop-down menu in the **Google Cloud Partner** field, select **BigQuery**.
     * In the **Mass Transfer Key** field, enter the mass transfer key for the sample mass transfer configuration.
     * In the **Table Name** field, enter the name of the source SAP table.
     * Optionally, to view the report by load simulation execution date, specify a date range in the **Report Date** field.
     * Optionally, to view the last executed report along with the current report, select the **Last Execution Only** flag.
  8. To display the report, click the **Execute** icon.




The following table describes the columns displayed in the simulation report: 

Name | Description  
---|---  
Transfer Key | The mass transfer key for the mass transfer configuration.  
SAP Table | The name of the SAP table that is being replicated to BigQuery.  
Execution Start Timestamp | The time when the execution started for a BigQuery Connector for SAP method.  
Completion Timestamp | The time when the execution completed for a BigQuery Connector for SAP method.  
Job Number | Unique job number for each completed execution that is automatically generated every time the Load Simulation tool is run.  
Cycle Numb | The sequence number of the processing cycle in which the report is generated. The **Record Count per cycle** provided in the simulation input is transferred to BigQuery for each cycle.  
Portion Numb | The sequence number of the portion. The **Record Count per cycle** provided in the simulation input is split into portions based on the specified portion size. The BAdI of BigQuery Connector for SAP is called for each portion.  
Class Name | The class name of the BigQuery Connector for SAP method.  
Method Name | The name of the BigQuery Connector for SAP method. The methods that are called by BigQuery Connector for SAP are logged in a sequence. If the **Detailed Log** flag is selected in the simulation input, then all methods are logged, or else only the important methods are logged.  
Invoked by Method | The last method that invoked the current BigQuery Connector for SAP method.  
Duration | The total time taken for the execution of a BigQuery Connector for SAP method.  
Recs Count | The number of records passed to a BigQuery Connector for SAP method. This is shown for only the methods to which the records are passed.  
URI Method | The name of the HTTP method, in case the ABAP method makes a BigQuery API call.  
URI String | The HTTP URL, in case the ABAP method makes a BigQuery API call.  
Token Source | The source of the authentication token that the Load Simulation tool is using. This is applicable only if token caching is activated in the `/GOOG/CLIENT_KEY` table. The possible values are: 

  * `A`: Static attribute value from a specific process.
  * `M`: Shared memory value from the memory that is shared across multiple processes.
  * `L`: New value with memory lock. If there is a memory lock and the cached token cannot be read, then a new token is generated.
  * `N`: New value without memory lock. If a token expires or is not found in the memory, then a new token is generated.

  
Expiration Time | The expiration time of the authentication token.   
This is applicable only when token caching is activated in the `/GOOG/CLIENT_KEY` table.  
Token Value | Value of the authentication token that the Load Simulation tool uses to access BigQuery.  
Return code | The return code of the method execution. The possible values are: 

  * `0`: Indicates a successful execution.
  * An error code. In case of a failure, the corresponding BigQuery Connector for SAP error code is displayed. For information about error codes, see [BigQuery Connector for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting).

  
Error Text | The error title, if any.  
Error Description | Detailed information about the error.  
Payload size | The HTTP payload size to BigQuery Insert API. If there is an error in method execution and payload size is greater than 10 MB, then you can adjust the chunk size to decrease the payload size.  
Information text | Any relevant information message raised by the BAdI of BigQuery Connector for SAP. For example, when dynamic chunking is triggered, the following information message is shown: `Dynamic chunking triggered. Chunk size reduced from INITIAL_CHUNK_SIZE_VALUE to FINAL_REDUCED_CHUNK_SIZE_VALUE`.  
Status | Status of the method execution. In case a method execution fails, see the [BigQuery Connector for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/bq-connector/latest/troubleshooting) to resolve the issue.  
  
#### Schedule Load Simulation tool

You can schedule the Load Simulation tool to run automatically as a background job on the SAP LT Replication Server by using the program name `/GOOG/R_LOAD_SIMULATION`. For more information from SAP about scheduling background jobs, see [Scheduling Background Jobs](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-us/4b/2b2954365474fee10000000a421937/frameset.htm).

### Replication validation

If you select the **Extra Fields Flag** when you create the target BigQuery table with transaction `/GOOG/SLT_SETTINGS`, columns are added to the table schema for storing the type of change to each record that triggered replication and for a timestamp that reflects the time at which SAP LT Replication Server received the portion that contained the record.

You can use the change types and the timestamp to query the following types of record counts:

  * The number of records that are loaded into a BigQuery table during an initial load.
  * The number of records replicated on a specified day into a BigQuery table.
  * The total number of unique records in a BigQuery table.



To get these counts, you can query the BigQuery table directly by submitting SQL queries in the Google Cloud console, or you can run the Replication Validation tool, which generates reports that compare the BigQuery record counts with SAP LT Replication Server statistics or record counts from the source table.

For an overview of the **Extra Fields Flag** , see [Capturing record changes and enabling record counts](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#fields-for-changes-and-counts).

For information about how to specify the **Extra Fields Flag** , see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#configure-connection).

#### SQL queries for record counts

On the BigQuery **SQL Editor** page in the Google Cloud console, you can run SQL queries to check the record counts in your BigQuery tables.

You can then compare the BigQuery record counts with the counts in the source table or in the SAP LT Replication Server statistics.

**Required table setting for record counts** : The SQL queries in this section require that you specify the **Extra Fields Flag** when you specify the BigQuery table options during replication configuration. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#fields-for-changes-and-counts). 

##### Query the count of records inserted in initial load mode

When a BigQuery table schema includes the optional `operation_flag` column, records that are inserted into the table in initial load mode include the `L` operation flag.

To get the count of records that were received by BigQuery during an initial load, execute the following query:
    
    
    SELECT COUNT(*)
      FROM
          `PROJECT.DATASET.TABLE`
      WHERE operation_flag = 'L'

##### Query the number of records inserted in replication mode

When a BigQuery table schema includes the optional `operation_flag` column, records that are inserted into the table in replication mode include one of the following operation flags:

  * **`I`** : the record was inserted into the source table.
  * **`D`** : the record was deleted from the source table.
  * **`U`** : the record was updated in the source table.



To get the count of records that were received by BigQuery in replication mode, run the following query:
    
    
    SELECT COUNT(*)
      FROM
          `PROJECT.DATASET.TABLE`
      WHERE operation_flag = 'I' | 'D' | 'U'

##### Query the total count of records in a BigQuery table

When a BigQuery table schema includes the optional `recordstamp` column, the corresponding `recordstamp` field of each record that is inserted into the table contains a timestamp that indicates when the record was sent by SAP LT Replication Server to BigQuery.

When CDC is not activated, to get a total count of the records in a BigQuery table that you can compare with the total count of records in a source table, you can use the `recordstamp` and `is_deleted` fields to count the unique records in the BigQuery table that have not been deleted from the source table.

If the source table is being actively updated or replication is active when you query the records, the count of records in the source and target tables might not match exactly.

To get the current count of unique records in the BigQuery target table, run the following query:
    
    
    SELECT COUNT(*)
      FROM (
        SELECT
          *,
          ROW_NUMBER() OVER (PARTITION BY KEY_FIELD_1, ..., KEY_FIELD_N ORDER BY recordstamp DESC) row_num
        FROM
          `PROJECT.DATASET.TABLE` )
      WHERE row_num = 1 AND is_deleted = false

When CDC is activated, to get the current count of unique records in the BigQuery target table, run the following query:
    
    
    SELECT COUNT(*) FROM `PROJECT.DATASET.TABLE`;

#### Replication Validation tool

This tool is not supported for CDC replication to BigQuery through Pub/Sub and file-based replication to Cloud Storage.

This section provides an overview of the Replication Validation tool and what you can do with it.

**Required table setting for record counts** : To use the Replication Validation tool, you must specify the **Extra Fields Flag** when you specify the BigQuery table options during replication configuration. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#fields-for-changes-and-counts). 

The Replication Validation tool generates reports that compare the record counts in the BigQuery table with SAP LT Replication Server statistics and the record counts in the source table. If the counts don't match exactly, the tool flags the report with a red circle.

To count the records in BigQuery, the tool uses the SQL queries that are shown in the preceding section, SQL queries for record counts.

Run the Replication Validation tool periodically to validate that SAP LT Replication Server and the BigQuery Connector for SAP are replicating records to BigQuery as expected.

To run the Replication Validation tool, enter the custom transaction `/GOOG/REPLIC_VALID` preceded by `/n` in the SAP GUI. For step-by-step instructions, see [Run the Replication Validation tool](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-streaming-api#validate-rep-tool).

##### Replication validation reports

You can generate the following validation reports with the Replication Validation tool:

  * **Initial Load Counts:** A comparison of the number of records that were sent by SAP LT Replication Server in load mode and the number of records that were loaded into BigQuery.
  * **Replication Counts:** A comparison of the number of records that were sent by SAP LT Replication Server in replication mode and the number of records that were inserted into BigQuery on a specified day.
  * **Current Counts:** A point-in-time comparison of the number of records that are in the source table and the number of unique records in BigQuery. Current count on the source table cannot display a number greater than the 32-bit integer limit (-2,147,483,648 to 2,147,483,647).



You can generate each report individually or, by selecting **All Checks** when you run the tool, you can generate all three reports in a single execution. With the **Table Names** field, you can generate the replication validation reports for specific tables in the mass transfer configuration.

##### Display Replication Validation reports

After you generate a report, you can display the report by selecting the **Display Report** radio button in the **Processing Options** section of the Replication Validation tool interface.

The information that the Replication Validation tool displays in each report differs slightly depending on the type of report.

All of the reports include the following types of information:

  * Source record counts from SAP LT Replication Server statistics and the source table.
  * Target record counts from the target BigQuery table.
  * Any difference between the two counts. The difference is calculated by subtracting the BigQuery counts from the source record counts. A positive value indicates a likely problem, because it suggests that not all source records are making it into BigQuery.
  * The difference in the counts displayed as a percentage of source record count.
  * A visual indicator of whether the source and target counts are equal or different.



##### Unequal record counts

The Replication Validation tool includes a status field with each report it displays.

A green square in the status field means that the source record count is equal to the target record count in BigQuery.

A red circle in the status field means that the record counts are not equal.

An unequal record count does not always indicate a problem. The following indicators suggest a possible problem:

  * For a Current Counts report, an unequal value always indicates a problem.
  * For an Initial Load Counts or Replication Counts report, a positive value indicates a likely problem.

A relatively low negative value is not a problem. The count in a target BigQuery table can sometimes be a little higher than the source record count due to events such as momentary connectivity disruptions that cause SAP LT Replication Server to resend data.




If you see an unequal count, rerun the report to make sure it was not caused by a transitory issue. An unequal record count can occur due to replication processing at the time the tool generated the report.

For a very large source table or a table that has filters set in SAP LT Replication Server for initial load or replication, the Replication Validation tool might not be able to count all of the records that are required for an equal count.

#### Schedule validation checks

You can schedule the Replication Validation tool to run automatically at intervals by using the SAP background job feature.

### Stream Records tool

This tool is not supported for streaming data replication to BigQuery and file-based replication to Cloud Storage.

The Stream Records tool lets you stream records from SAP to Pub/Sub based on specific criteria. By default, it creates a subscription with a filter to stream only deleted records from the source SAP table to BigQuery by using the [Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api) through Pub/Sub. However, you can customize the filter options as needed.

To run the Stream Records tool, follow these steps:

  1. In the SAP GUI, execute the transaction **/GOOG/BQPS_FLTR_SUBS** preceded by `/n`:
         
         /n/GOOG/BQPS_FLTR_SUBS

  2. On the Stream records screen, provide values for the following fields:

     * **Mass transfer key** : The mass transfer key that contains the SAP tables.
     * **SAP table name** : The SAP table names for which you need all the field mappings to be converted to the `STRING` type.
     * **Filter Subscription ID** : The name of the subscription to the existing topic that you need to create.
     * **Filter Condition** : Condition with which the subscription is created. The default filter is set to stream only deleted records. For information about the syntax to create a filter, see [Filtering messages](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter#filtering_syntax).
  3. Click the **Execute** icon. For the selected table, a subscription is created with the specified filter condition.




## Edit field definitions in a CSV file

The following sections describe how to export the default field definitions so that your data engineers or system administrators can edit the target field values without requiring access to SAP LT Replication Server.

When editing the target field values, adhere to the following rules:

  * Don't modify values in the **SAP Table Name** and **SAP Field Name** columns.
  * In the **Send Uncompressed Flag** column, to enable record compression, mark the field with only an `X`. Otherwise, leave the field blank. This field is not applicable for file-based replication to Cloud Storage.



### Create a spreadsheet or text file of the default field definitions

To create a CSV file for editing outside of SAP LT Replication Server, do the following:

  1. Run the `/GOOG/SLT_SETTINGS` transaction.

  2. In the **SLT Settings Maintenance** screen, specify the following values:

     * In the **Google Cloud Partner** field, select your replication option.
     * In the **Settings Table** field, specify **Fields**.
     * In the **Mass Transfer Key** field, specify the ID of the mass transfer that you are updating.
     * In the **Table Name** field, either leave the field blank to work with all fields from all tables or specify a table name to work with a specific table.
     * Leave all other fields blank.
  3. Click the **Execute** icon.

  4. Hide all columns except for those in the following list by right-clicking on the column headings and selecting **Hide** from the drop-down menu:

     * **SAP Table Name**
     * **SAP Field Name**
     * **Avro Type** , applicable for CDC replication to BigQuery through Pub/Sub
     * **External Data Element**
     * **External Field Name**
     * **Field Description** , not applicable for file-based replication to Cloud Storage
     * **Send Uncompressed Flag** , not applicable for file-based replication to Cloud Storage
  5. With the remaining columns displayed, click the **Export** icon.

  6. From the **Export** menu, select one of the following options:

     * **Spreadsheet**
     * **Local file**. For ease of converting the file contents to CSV format, we recommend saving the file in the **Text with tabs** format.
  7. Save the default field definitions by clicking the **Checkmark** icon.




### Convert the spreadsheet or text file to CSV format

To upload edited field definitions by using the custom transaction `/GOOG/SLT_SETTINGS`, the field definitions must be in CSV format.

If you are using a spreadsheet, save the spreadsheet as a CSV file before you upload the file.

If you are using a local file in a tab-separated format or any other format, you need to modify the file to conform to CSV format.

For example:
    
    
    SAP Table,SAP Field Name,AVRO Type,External Data Element,External Field Name,Field Description, Send Uncompressed Flag
    SAP_TABLE_NAME,SAP_FIELD_NAME1,AVRO_TYPE,EXTERNAL_DATA_ELEMENT,EXTERNAL_FIELD_NAME,FIELD_DESCRIPTION, SEND_UNCOMPRESSED_FLAG
    SAP_TABLE_NAME,SAP_FIELD_NAME2,AVRO_TYPE,BIGQUERY_DATA_TYPE,BIGQUERY_FIELD_NAME2,BIGQUERY_FIELD_DESCRIPTION2, SEND_UNCOMPRESSED_FLAG2
    SAP_TABLE_NAME,SAP_FIELD_NAME3,AVRO_TYPE,BIGQUERY_DATA_TYPE,BIGQUERY_FIELD_NAME3,BIGQUERY_FIELD_DESCRIPTION3, SEND_UNCOMPRESSED_FLAG3
    

### Upload the CSV file

To upload an edited CSV file:

  1. Run the `/GOOG/SLT_SETTINGS` transaction.

  2. In the **SLT Settings Maintenance** screen, specify the following values:

     * In the **Settings Table** field, specify **Fields**.
     * In the **Mass Transfer Key** field, specify the ID of the mass transfer that you are updating.
     * Select the **Upload from file** checkbox.
  3. Click the **Execute** icon. The **Select File to Upload** dialog opens.

  4. In the **Select File to Upload** dialog, select the CSV file that contains the edited field values.

  5. Click **Open**.

  6. If you receive a security warning, click **Allow**. The file loads and the modified values in the file appear on the applicable rows on the screen.

  7. Click the **Save** icon.

  8. To confirm the values are applied, compare the values in the CSV file with the values that are displayed by SAP LT Replication Server.




## Error handling in source data

This section describes error handling for replication to BigQuery.

Upon receiving a chunk of records from BigQuery Connector for SAP, the BigQuery streaming API checks for data errors before inserting any records into the BigQuery table.

You can control how the BigQuery API and the BigQuery Connector for SAP respond when data errors are found by specifying the following flags in mass transfer settings:

  * The `Skip Invalid Records` (`SKIP`) flag
  * The `Break at First Error Flag` (`BREAK`) flag



### The `SKIP` flag

If you specify the `SKIP` flag, when the BigQuery API receives a chunk of records and finds a record with a data error, then the BigQuery API discards, or _skips_ , the record with the error and continues inserting all other records from the chunk into the BigQuery table.

If you don't specify the `SKIP` flag, when BigQuery finds a record with a data error, BigQuery discards the entire chunk without inserting any records from it into the BigQuery table. This is the default behavior.

Specifying the `SKIP` flag is best for development and QA environments, and is not recommended for production environments.

You can specify the `SKIP` flag in the `/GOOG/SLT_SETTINGS` transaction when you are configuring replication. The specification is stored in the `/GOOG/BQ_MASTR` configuration table.

To see how `SKIP` specifications interact with `BREAK` specifications, see Matrix table for `SKIP` and `BREAK` interactions.

### The `BREAK` flag

If you specify the `BREAK` flag, when BigQuery Connector for SAP is notified by the BigQuery API that a data error was found in a record, BigQuery Connector for SAP stops sending records to BigQuery and terminates the replication job. This is the default behavior.

If you don't specify the `BREAK` flag, when BigQuery Connector for SAP is notified by BigQuery that a data error was found in a record, BigQuery Connector for SAP continues sending records to BigQuery by sending the next chunk and the replication job continues.

Specifying the `BREAK` flag is recommended in production environments.

You can specify the `BREAK` flag in the `/GOOG/SLT_SETTINGS` transaction when you are configuring replication. When you create a new mass transfer key, the `BREAK` flag is enabled by default.

The specification is stored in the `/GOOG/BQ_MASTR` configuration table.

To see how `BREAK` specifications interact with `SKIP` specifications, see Matrix table for `SKIP` and `BREAK` interactions.

### Matrix table for `SKIP` and `BREAK` interactions

You can configure BigQuery Connector for SAP to handle data errors in the following ways:

`SKIP` flag | `BREAK` flag | Behavior  
---|---|---  
FALSE | TRUE |  BigQuery discards the current chunk of records without inserting any records from the current chunk into the BigQuery table.  BigQuery Connector for SAP sends no more chunks of records from the current portion and tells SAP LT Replication Server to terminate the replication job.  This is the **default** and **recommended setting**.  **Important:** When you set these flags to the recommended setting, the BigQuery Connector for SAP relies on SAP LT Replication Server to handle errors and retry sending failed records. SAP LT Replication Server retains failed records in its logging tables until they are successfully sent to BigQuery. However, if the error originates in the data, such as the presence of non-unicode characters, then you must fix the data in the source system before retrying replication to BigQuery.   
FALSE | FALSE |  BigQuery discards the current chunk of records without inserting any records from the current chunk into the BigQuery table.  BigQuery Connector for SAP sends any remaining chunks of records from the current portion and retrieves the next portion. BigQuery Connector for SAP does not tell SAP LT Replication Server to terminate the replication job.  **Warning:** Setting `SKIP` and `BREAK` to non-recommended values can result in data loss that you cannot recover.   
TRUE | TRUE |  BigQuery discards only the record that contains the error and inserts the rest of the records in the current chunk into the BigQuery table.  BigQuery Connector for SAP sends no more chunks of records from the current portion and tells SAP LT Replication Server to terminate the replication job.  **Warning:** Setting `SKIP` and `BREAK` to non-recommended values can result in data loss that you cannot recover.   
TRUE | FALSE |  BigQuery discards only the record that contains the error and inserts the rest of the records in the current chunk into the BigQuery table.  BigQuery Connector for SAP sends any remaining chunks of records from the current portion and retrieves the next portion. BigQuery Connector for SAP does not tell SAP LT Replication Server to terminate the replication job.  **Warning:** Setting `SKIP` and `BREAK` to non-recommended values can result in data loss that you cannot recover.   
  
## Table structure changes

This section explains how to modify the SAP source table structure, for which an existing `LTRC` replication is in progress.

For CDC replication to BigQuery through Pub/Sub, the intermediate Pub/Sub schema is revised according to the table structure changes. When the Pub/Sub schema is updated, it might take a few minutes for the changes to take effect. However, there's no data loss.

### Add a column to a source table

To add a new column to a source table, follow these steps:

  1. Add a new column to the source table. As a result of this step, the replication status changes to `Load/Replication blocked`.

  2. In your SLT system, reset the replication status using transaction `LTRC`. For more information from SAP about how to reset the replication status, see [SAP Note 2204955 - SLT tables are in status 'Load /Replication blocked'](https://launchpad.support.sap.com/#/notes/2204955).

  3. Add, update, or delete an entry in the source table.

  4. Validate the replication result in BigQuery.




### Delete a column from a source table

To delete an existing column from a source table, follow these steps:

  1. In your SLT system, suspend the replication using transaction `LTRC`.

  2. Delete a column from the source table. As a result of this step, the existing SLT triggers are either deleted or changed to an inconsistent state.

  3. For CDC replication to BigQuery through Pub/Sub, manually delete the column from the target Pub/Sub schema by creating a new revision. For more information about the steps to delete a column from an existing schema, see the [Revise a schema](https://docs.cloud.google.com/pubsub/docs/commit-schema-revision#console) in Pub/Sub documentation.

  4. In BigQuery, delete the column from the target BigQuery table. For more information about the steps to delete a column from an existing table, see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/managing-table-schemas#delete_a_column).

  5. In your SLT system, resume the replication using transaction `LTRC`.

  6. In your SLT system, recreate the SLT triggers. For more information from SAP about how to recreate SLT triggers, see [SAP Note 2254376 - SLT trigger(s) in an inconsistent state](https://launchpad.support.sap.com/#/notes/0002254376).

  7. If the replication status is `Load /Replication blocked`, then reset the replication status using transaction `LTRC`. For more information from SAP about how to reset the replication status, see [SAP Note 2204955 - SLT tables are in status 'Load /Replication blocked'](https://launchpad.support.sap.com/#/notes/2204955).

  8. Clear the logs, if any.

  9. Add, update, or delete an entry in the source table.

  10. Validate the replication result in BigQuery.




### Change the data type of an existing column

When you change the data type of an existing column in SAP source table, you need to follow specific steps depending on whether you are changing the data type to a compatible or non-compatible data type with the target BigQuery table.

A data type is compatible with the data type in the target BigQuery table when the existing data type and new data type of an existing column ultimately map to the same data type in the target BigQuery table and consequently, the Pub/Sub Avro schema.

For example, if the data type of a column is changed from `INT1` to `INT2` in a source table, both these SAP data types are considered compatible because they map to the `INTEGER` data type in BigQuery and would correspond to the `int` type in the Pub/Sub Avro schema.

The BigQuery Connector for SAP handles this mapping internally. Compatibility means the underlying BigQuery and Pub/Sub type does not need to change. For more information, see [Schema compatibility](https://docs.cloud.google.com/pubsub/docs/bigquery#schema_compatibility).

For more information about data type mapping in BigQuery Connector for SAP, see [Data type mapping](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#data-type-mapping).

#### Change the data type to a compatible data type

To change the data type of an existing column to a compatible data type, follow these steps:

  1. Change the data type to a compatible data type in the source system. As a result of this step, the existing SLT triggers are either deleted or changed to an inconsistent state.

  2. In your SLT system, recreate the SLT triggers. For more information from SAP about how to recreate SLT triggers, see [SAP Note 2254376 - SLT trigger(s) in an inconsistent state](https://launchpad.support.sap.com/#/notes/0002254376).

  3. If the replication status is `Load /Replication blocked`, then reset the replication status using transaction `LTRC`. For more information from SAP about how to reset the replication status, see [SAP Note 2204955 - SLT tables are in status 'Load /Replication blocked'](https://launchpad.support.sap.com/#/notes/2204955).

  4. Clear the logs, if any.

  5. Add, update, or delete an entry in the source table.

  6. Validate the replication result in BigQuery.




#### Change the data type to a non-compatible data type

To change the data type of an existing column to a non-compatible data type, follow these steps:

  1. In your SLT system, stop the replication using transaction `LTRC`.
  2. For CDC replication to BigQuery through Pub/Sub, in Pub/Sub, delete the target schema, BigQuery subscription, and Pub/Sub topic.
  3. In BigQuery, delete the target table.
  4. Change the data type in the source system.
  5. In your SLT system, start the replication using transaction `LTRC`.

**Note:** Stop replication and Start replication steps reload the records into BigQuery.

For more information about table structure changes, see [BigQuery Connector for SAP: Handle table structure changes like a pro](https://medium.com/google-cloud/bigquery-connector-for-sap-handle-table-structure-changes-like-a-pro-b17dd151ce69).

### Manage Pub/Sub schema for table structure changes

When your table structure changes, for CDC replication to BigQuery through Pub/Sub, the intermediate Pub/Sub schema is also updated to reflect the table structure changes. This results in a new schema revision.

Pub/Sub maintains a history of these revisions, which it then uses for correctly interpreting messages. Pub/Sub allows a maximum of 20 schema revisions per topic. Exceeding this limit can lead to errors and prevent further schema updates.

When the limit of 20 schema revisions is reached, the SAP SLT system receives error messages indicating that new schema revisions cannot be created. In this case, you receive the following errors:

  * **SAP logs** : Errors in the SLT logs, related to Pub/Sub operations, such as:

    * `/GOOG/MSG : 429 - You have exceeded your revisions per schema quota (schema = SCHEMA_NAME)`
    * `Cannot create more schema revisions`
  * **Replication status** : The replication status for the affected tables might change to "Load/Replication blocked."

  * **Pub/Sub errors** : Errors on the Pub/Sub side, indicating that the schema cannot be updated.




When you notice these errors, you can do the following:

  * **Analyze and delete old schema revisions** : If older schema revisions are no longer needed, delete them using the Google Cloud console or gcloud CLI. For more information, see [Delete a schema revision](https://docs.cloud.google.com/pubsub/docs/delete-schema-revision).
  * **Create a new schema** : When deleting old schema revisions is not an option, you can create a new Pub/Sub schema. To create a new Pub/Sub schema, do the following:

    1. In your SLT system, stop the replication by using the transaction `LTRC`.
    2. In the [table attributes](https://docs.cloud.google.com/sap/docs/bq-connector/latest/config-with-bq-storage-write-api#table-attributes), in the **Pub/Sub Schema** field, update the new schema name.
    3. In your SLT system, start the replication by using the transaction `LTRC`.
    4. The connector automatically creates a new schema based on the source table definition.
    5. Once the replication is verified, you can delete the old schema.
**Note:** When you stop or start replication, it reloads the records into BigQuery.



## Enhancement exits

BigQuery Connector for SAP provides several enhancement points in its code where an ABAP developer can insert code to add custom features.

**Important:** You assume the responsibility for any custom code written within the implementation of these enhancement points. We strongly recommend that you test your custom code thoroughly in a non-production environment before deploying it to production. Google Cloud does not provide support for custom features.

The following table lists the functions that the enhancement points support, the methods, and the class that contains the enhancement point:

Function | Class | Method | Spot | Option  
---|---|---|---|---  
Update the handling of control characters in Pub/Sub and Cloud Storage. | `/GOOG/CL_GCP_JSON_UTIL` | `ESCAPE_CONTROL_CHARS_AND_REPLACE` | `/GOOG/ES_GCP_JSON_UTIL` | `/GOOG/REPLACE_CNTRL_CHARS`  
Update the encoding logic before standard adoption. | `/GOOG/CL_GCP_CLIENT_PUBSUB_SLT` | `SERIALIZE_TABLE_ROWS` | `/GOOG/ES_GCP_CLIENT_BQCPS_SLT` | `/GOOG/PRE_ENCODING_REPLACE`  
Update the encoding logic after standard adoption. | `/GOOG/CL_GCP_CLIENT_PUBSUB_SLT` | `SERIALIZE_TABLE_ROWS` | `/GOOG/ES_GCP_CLIENT_BQCPS_SLT` | `/GOOG/POST_ENCODING_REPLACE`  
Update the mapping for a field, such as the external field name and data type. | `/GOOG/CL_IUUC_REPL_RUNTIME` | `CREATE_FLD_MAPPINGS` | `/GOOG/ES_IUUC_REPL_RUNTIME` | `/GOOG/UPDATE_FIELD_MAPPING`  
Update the mapping for the field table by adding or removing fields. | `/GOOG/CL_IUUC_REPL_RUNTIME` | `CREATE_FLD_MAPPINGS` | `/GOOG/ES_IUUC_REPL_RUNTIME` | `/GOOG/UPDATE_FIELD_MAPPINGS`  
Change the value of a source field before the field is converted to a target field. | `/GOOG/CL_IUUC_REPL_RUNTIME_BQ` | `FILL_TARGET_RECORDS` | `/GOOG/ES_IUUC_REPL_RUNTIME_BQ` | `/GOOG/CHANGE_SOURCE_FIELD`  
After a source field is converted to a target field in the target table, change the value of the target field. | `/GOOG/CL_IUUC_REPL_RUNTIME_BQ` | `FILL_TARGET_RECORDS` | `/GOOG/ES_IUUC_REPL_RUNTIME_BQ` | `/GOOG/FILL_TARGET_FIELD`  
Add a field to the target table that does not exist in the source table during the source-to-target table conversion. | `/GOOG/CL_IUUC_REPL_RUNTIME_BQ` | `FILL_TARGET_RECORDS` | `/GOOG/ES_IUUC_REPL_RUNTIME_BQ` | `/GOOG/FILL_EXTRA_FIELD`  
Prepare a BigQuery schema field before the BigQuery table is created. | `/GOOG/CL_GCP_CLIENT_BQ` | `PREP_BQ_TABLE_SCHEMA` | `/GOOG/ES_GCP_CLIENT_BQ` | `/GOOG/PREPARE_SCHEMA_FIELD`  
In case of HTTP errors originating on the Pub/Sub server side, for troubleshooting the issue, you can collect logging data after the HTTP calls to the Pub/Sub API.  | `/GOOG/CL_GCP_CLIENT_PUBSUB_SLT` | `PUBLISH_DATA_CHUNKS` | `/GOOG/ES_GCP_CLIENT_BQCPS_SLT` | `/GOOG/LOG_INSERT_ERROR`  
In case of HTTP errors originating on the BigQuery server side, for troubleshooting the issue, you can collect logging data after the HTTP calls to the BigQuery API.  | `/GOOG/CL_GCP_CLIENT_BQ_SLT` | `INSERT_TABLEDATA` | `/GOOG/ES_GCP_CLIENT_BQ_SLT` | `/GOOG/LOG_INSERT_ERROR`  
In case of HTTP errors originating on the Cloud Storage, for troubleshooting the issue, you can collect logging data after the HTTP calls to the Cloud Storage API. | `/GOOG/CL_GCP_CLIENT_CS_SLT` | `UPLOAD_TABLE_DATA` | `/GOOG/ES_GCP_CLIENT_BQGCS_SLT` | `/GOOG/LOG_INSERT_ERROR`  
In case of HTTP errors originating on the SAP client side, for troubleshooting the issue, you can collect logging data.  | `/GOOG/CL_GCP_HTTP_CLIENT` | `RECEIVE_HTTP_RESPONSE` | `/GOOG/ES_GCP_HTTP_CLIENT` | `/GOOG/RECEIVE_HTTP_RESPONSE`  
In case of HTTP errors originating on the BigQuery server side, for troubleshooting the issue, you can collect logging data after the HTTP calls to the BigQuery API.  | `/GOOG/CL_GCP_CLIENT_BQ_SLT` | `INSERT_TABLEDATA` | `/GOOG/ES_GCP_CLIENT_BQ_SLT` | `/GOOG/LOG_RETURN_STATUS`  
  
## BAdI enhancements

The BigQuery Connector for SAP provides Business Add-In (BAdI) options that let you enhance the standard replication logic.

### Customizing output format for file-based replication to Cloud Storage

To accommodate enterprise requirements for specific file formats, such as CSV, AVRO, Parquet, or ORC, when replicating data to Cloud Storage, BigQuery Connector for SAP provides the BAdI `/GOOG/BADI_GCS_TRANSFORM_DATA` with the interface `/GOOG/IF_GCS_TRANSFORM_DATA`. This BAdI is included in the enhancement spot `/GOOG/ES_BQGCS_TRANSFORMER`.

By default, BigQuery Connector for SAP serializes SAP change data into Newline Delimited JSON (NDJSON) format. If your downstream architecture requires a different format, then you can use this BAdI to implement custom logic that modifies the output format. The custom transformation logic is invoked during runtime. When you use custom transformations, the default transformation logic to NDJSON is skipped, and the resulting custom-formatted file is uploaded directly to your designated Cloud Storage bucket.

This BAdI is specifically designed for replication to Cloud Storage and is not applicable for streaming data replication to BigQuery or CDC replication to BigQuery through Pub/Sub.

**Important:** You assume the responsibility for any custom code written within the implementation of these BAdIs. We strongly recommend that you test your custom code thoroughly in a non-production environment before deploying it to production. Google Cloud does not provide support for custom features.

To implement custom transformation, follow these steps:

  1. Implement the `SKIP_DEFAULT` method with the following settings: 
     * Set the exporting parameter `EV_CONTENT_TYPE` to the [Content-Type](https://docs.cloud.google.com/storage/docs/metadata#content-type) of the target output format that you're going to implement.
     * Set the exporting parameter `EV_FILE_EXTENSION` to the extension of the file that is uploaded to Cloud Storage.
     * Set the changing parameter `CV_SKIP_DEFAULT` to `'X'` (`abap_true`) to ensure the custom implementation is called.
  2. Implement the `TRANSFORM_DATA` method to hold the custom transformation logic for each data chunk: 
     * Use the importing parameter `IT_DATA` to read the table data for the chunk being processed.
     * Set the exporting parameter `EV_DATA` with the transformed data in a string format.



## Advanced settings

Optionally, you can modify the advanced settings for BigQuery Connector for SAP. Google Cloud recommends that you modify the advanced settings parameters only after a comprehensive analysis and impact of new values on performance. You are responsible for ensuring that the new advanced settings for BigQuery Connector for SAP do not cause failures and performance issues.

**Warning:** Don't modify the advanced settings for BigQuery Connector for SAP when an initial load is in progress.

Advanced settings for BigQuery Connector for SAP are applied at the system level and are common for all mass transfer keys. If the advanced settings parameters are not modified, then BigQuery Connector for SAP works with the default settings.

To modify advanced settings parameters, complete the following steps:

  1. In the SAP GUI, enter the `/GOOG/SLT_SETTINGS` transaction preceded by `/n`:
         
         /n/GOOG/SLT_SETTINGS

  2. From the **Settings Table** drop-down menu in the launch screen for the `/GOOG/SLT_SETTINGS` transaction, select **Parameters**.

  3. Click the **Execute** icon. The **BigQuery Settings Maintenance - Parameters** screen displays.

  4. Click the **Insert Row** icon.

  5. In the displayed row, specify the following settings:

     1. In the **Parameter Name** field, enter the name of the parameter. The parameter description is automatically populated.
     2. In the **Parameter Value** field, enter a value.

To know about the Advanced settings parameters, see Advanced settings parameters.

  6. Click **Save**.

Your advanced settings are stored as a record in the `/GOOG/BQ_PARAM` configuration table and the **Changed By** , **Changed On** , and **Changed At** fields are automatically populated.




### Advanced settings parameters

The following table shows the advanced settings parameters for BigQuery Connector for SAP.

**Parameter name** | **Description** | **Default value** | **Valid value**  
---|---|---|---  
`CHUNK_SIZE_DEF` | This is the default chunk size the BigQuery Connector for SAP supports.  
If a chunk size is not maintained in the settings, the default chunk size is used.  
Use this parameter only with the streaming data replication to BigQuery. | 10,000 | The value must be within the [BigQuery Quota limits](https://docs.cloud.google.com/bigquery/quotas).   
`PERC_REDUC_DEF` | The chunk size percentage reduction.  
If dynamic chunk size is enabled, the chunk size is reduced by this percentage until an ideal chunk size is reached and the data in the chunk is transferred to BigQuery successfully. | 50 | The value must be from 1 to 99.  
`CMD_EXEC_TRIES` | For SAP systems that are not running on Google Cloud, if the operating system command that you created in the transaction `SM69` fails to retrieve an access token from Google Cloud, then this is the number of times that the BigQuery Connector for SAP retries the token retrieval.  | 5 | The minimum value that you can assign to this parameter is `1`. To facilitate at least one retry, set the value `2`. The maximum value for this parameter must be set after analyzing the impact that token retrieval retries can have on replication performance.   
`CMD_SECS_DEFLT` | If you have enabled token caching, then this is the duration in seconds after which the cached token expires. | 3500 | The value must be from 1 to 3599.  
`SCH_CACHE_ENABLE` | For [streaming data replication to BigQuery](https://docs.cloud.google.com/sap/docs/bq-connector/latest/overview#streaming-api-insert-only), enables [schema caching](#table-schema-caching), which reduces the number of `tables.get` calls to the BigQuery API. | `False` | `True` or `False`  
`PROCESS_SP_CHAR` | For Cloud Storage replication target, replaces all control characters in data of type `string` with their UTF-8 encoded values. | `False` | `True` or `False`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
