---
url: https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations/
title: Version 2.0: BigQuery Connector for SAP operations guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:48.291660+00:00
---

# Version 2.0: BigQuery Connector for SAP operations guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/bq-connector/2.0/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Version 2.0: BigQuery Connector for SAP operations guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows SAP LT Replication Server administrators, SAP data engineers, or others how to perform operational tasks, such as performance tuning and version updates, for **versions 2.0 and 2.1** of the BigQuery Connector for SAP.

## Tuning replication performance

Replication performance can be affected by multiple factors. The specific factors that apply can be different from installation to installation and can change over time.

The following sections provide guidance on how to tune some of the more common factors that can impact performance.

For more information about replication performance with the BigQuery Connector for SAP, see [Performance planning](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#performance).

### Set performance options for tables

In SAP LT Replication Server you can specify replication options for each table that affect performance.

In particular, the replication performance for large tables, which require more time and resources to replicate, can benefit from specifying ranges and increasing the maximum number of parallel replication jobs that can be used for the table.

Examples of tables that commonly grow large are `MSEG`, `ACDOCA`, and `MATDOC`, among others.

When you specify parallel replication jobs for large tables, you need to balance the number of parallel jobs that you allow for any given table against the total number of parallel jobs that are allowed in the mass transfer configuration. Your organization might also limit the number of parallel replication jobs that you can specify for a given server.

To set performance options for a table:

  1. In the SAP GUI, enter SAP transaction `LTRS`.

  2. On the **Advanced Replication Settings** screen, specify the ID of the mass transfer settings for the table.

  3. In the **Advanced Replication Settings** folder hierarchy, click on the **Performance Options** folder to display the tables that have performance options defined.

  4. If the table you need isn't listed, right-click the **Performance Options** folder, and then select **Add Table**.

  5. Specify a name for the Table.

  6. Specify the following options as needed:

     * Under **General Performance Options** : 
       * **No. of Parallel Jobs** , to set the maximum number of parallel replication jobs that can be used for the table.
       * **Sequence Number** , to prioritize the replication of this table relative to other table replications.
     * Under **Initial Load Options** : 
       * For **Reading Type** , select **Reading Type 1 Range Calculation** , if your table is not too large. For more information, see [Performance and the LTRS Advanced Replication Settings](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#perf-reading-types).
       * For **Package Size** , specify the size in bytes of the portions of records that are sent to SAP LT Replication Server.
       * If you select a Reading Type that uses ranges, then define appropriate ranges.
     * Under **Replication Option** : 
       * For **Ranges for Logging Table** , specify **No Ranges** for the most reliable option.
       * If you select **Specify Ranges for Manually** , then define appropriate ranges.
  7. Click **Save**.




### Baseline performance benchmark

To help you evaluate your replication performance, this section contains baseline performance numbers that were observed in Google Cloud test systems.

Due to the [many different factors that affect performance](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#performance-best-practices), your performance numbers are likely to vary.

For example, if your SAP systems are not running on Google Cloud, your load and replication rates might be slower than the baseline rates due to things like network latency and the overhead associated with for access tokens. If your source table has fewer columns or you install SAP LT Replication Server on its own server in a standalone architecture, your rates might be faster because SAP LT Replication Server doesn't have to compete with the source system for resources.

#### Observed baseline performance numbers

The following performance numbers represent the baseline performance that was observed by Google Cloud for each source system type during testing. In each test system, SAP LT Replication Server was installed on the SAP source system in an embedded architecture on Compute Engine VMs. The SAP source system was running in the same Google Cloud region as the target BigQuery dataset.

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
  * [Performance planning](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#performance)



#### Baseline performance test system configuration

The test systems described in this section produced the baseline performance numbers that are listed in the preceding section, Observed baseline performance numbers.

The tests systems, including the SAP source system, the SAP LT Replication Server, and the BigQuery data set, were all running on Compute Engine VMs in the same Google Cloud region.

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

  10. Test the configuration by starting an initial load or replication. For information about starting an initial load or replication, see:

     * If SAP LT Replication Server is running on a Compute Engine VM, [Test replication](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#test_replication).
     * If SAP LT Replication Server is running on a host that is external to Google Cloud, [Test replication](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-off-gc#test_replication).



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

For SAP HANA, you can use SAP HANA Studio for SAP HANA operations. You can install SAP HANA Studio on any front-end machine.

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



### Monitoring BigQuery

Use Cloud Monitoring to view BigQuery metrics and create charts and alerts. Each metric has a resource type, either `bigquery_dataset`, `bigquery_project`, or `global`, as well as a set of labels.

Use the resource types and labels to build queries in the [Monitoring Query Language (MQL)](https://docs.cloud.google.com/monitoring/mql).

You can group or filter each metric by using the labels.

For more information about Monitoring, see the [Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/docs).

## Replication validation

If you select the **Extra Fields Flag** when you create the target BigQuery table with transaction `/GOOG/SLT_SETTINGS`, columns are added to the table schema for storing the type of change to each record that triggered replication and for a timestamp that reflects the time at which SAP LT Replication Server received the portion that contained the record.

You can use the change types and the timestamp to query the following types of record counts:

  * The number of records that are loaded into a BigQuery table during an initial load.
  * The number of records replicated on a specified day into a BigQuery table.
  * The total number of unique records in a BigQuery table.



To get these counts, you can query the BigQuery table directly by submitting SQL queries in the Google Cloud console, or you can run the Replication Validation tool, which generates reports that compare the BigQuery record counts with SAP LT Replication Server statistics or record counts from the source table.

For an overview the **Extra Fields Flag** , see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#add-fields-for-changes-and-counts).

For information about how to specify the **Extra Fields Flag** , see:

  * If SAP LT Replication Server is running on a Compute Engine VM, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#configure-connection).
  * If SAP LT Replication Server is running on a host that is external to Google Cloud, see [Specify table creation and other general attributes](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-off-gc#configure-connection).



### SQL queries for record counts

On the BigQuery **SQL Editor** page in the Google Cloud console, you can run SQL queries to check the record counts in your BigQuery tables.

You can then compare the BigQuery record counts with the counts in the source table or in the SAP LT Replication Server statistics.

**Required table setting for record counts** : The SQL queries in this section require that you specify the **Extra Fields Flag** when you specify the BigQuery table options during replication configuration. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#fields-for-changes-and-counts). 

#### Query the count of records inserted in initial load mode

When a BigQuery table schema includes the optional `operation_flag` column, records that are inserted into the table in initial load mode include the `L` operation flag.

To get the count of records that were received by BigQuery during an initial load, execute the following query:
    
    
    SELECT COUNT(*)
      FROM
          `PROJECT.DATASET.TABLE`
      WHERE operation_flag = 'L'

#### Query the number of records inserted in replication mode

When a BigQuery table schema includes the optional `operation_flag` column, records that are inserted into the table in replication mode include one of the following operation flags:

  * **`I`** : the record was inserted into the source table.
  * **`D`** : the record was deleted from the source table.
  * **`U`** : the record was updated in the source table.



To get the count of records that were received by BigQuery in replication mode, run the following query:
    
    
    SELECT COUNT(*)
      FROM
          `PROJECT.DATASET.TABLE`
      WHERE operation_flag = 'I' | 'D' | 'U'

#### Query the total count of records in a BigQuery table

When a BigQuery table schema includes the optional `recordstamp` column, the corresponding `recordstamp` field of each record that is inserted into the table contains a timestamp that indicates when the record was sent by SAP LT Replication Server to BigQuery.

To get a total count of the records in a BigQuery table that you can compare with the total count of records in a source table, you can use the `recordstamp` and `is_deleted` fields to count the unique records in the BigQuery table that have not been deleted from the source table.

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

### Replication Validation tool

This section provides an overview of the Replication Validation tool and what you can do with it.

**Required table setting for record counts** : To use the Replication Validation tool, you must specify the **Extra Fields Flag** when you specify the BigQuery table options during replication configuration. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#fields-for-changes-and-counts). 

The Replication Validation tool generates reports that compare the record counts in the BigQuery table with SAP LT Replication Server statistics and the record counts in the source table. If the counts don't match exactly, the tool flags the report with a red circle.

To count the records in BigQuery, the tool uses the SQL queries that are shown in the preceding section, SQL queries for record counts.

Run the Replication Validation tool periodically to validate that SAP LT Replication Server and the BigQuery Connector for SAP are replicating records to BigQuery as expected.

To run the Replication Validation tool, enter the custom transaction `/GOOG/REPLIC_VALID` preceded by `/n` in the SAP GUI. For step-by-step instructions, see:

  * If SAP LT Replication Server is running on a Compute Engine VM, [Run the Replication Validation tool](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-on-gc#validate-rep-tool).
  * If SAP LT Replication Server is running on a host that is external to Google Cloud, [Run the Replication Validation tool](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/install-config-off-gc#validate-rep-tool).



#### Replication validation reports

You can generate the following validation reports with the Replication Validation tool:

  * **Initial Load Counts:** A comparison of the number of records that were sent by SAP LT Replication Server in load mode and the number of records that were loaded into BigQuery.
  * **Replication Counts:** A comparison of the number of records that were sent by SAP LT Replication Server in replication mode and the number of records that were inserted into BigQuery on a specified day.
  * **Current Counts:** A point in time comparison of the number of records that are in the source table and the number of unique records in BigQuery.



You can generate each report individually or, by selecting **All Checks** when you run the tool, you can generate all three reports in a single execution.

#### Displaying Replication Validation reports

After you generate a report, you can display the report by selecting the **Display Report** radio button in the **Processing Options** section of the Replication Validation tool interface.

The information that the Replication Validation tool displays in each report differs slightly depending on the type of report.

All of the reports include the following types of information:

  * Source record counts from SAP LT Replication Server statistics and the source table.
  * Target record counts from the target BigQuery table.
  * Any difference between the two counts. The difference is calculated by subtracting the BigQuery counts from the source record counts. A positive value indicates a likely problem, because it suggests that not all source records are making it into BigQuery.
  * The difference in the counts displayed as a percentage of source record count.
  * A visual indicator of whether the source and target counts are equal or different.



#### Unequal record counts

The Replication Validation tool includes a status field with each report it displays.

A green square in the status field means that the source record count is equal to the target record count in BigQuery.

A red circle in the status field means that the record counts are not equal.

An unequal record count does not always indicate a problem. The following indicators suggest a possible problem:

  * For a Current Counts report, an unequal value always indicates a problem.
  * For an Initial Load Counts or Replication Counts report, a positive value indicates a likely problem.

A relatively low negative value is not a problem. The count in a target BigQuery table can sometimes be a little higher than the source record count due to events such as momentary connectivity disruptions that cause SAP LT Replication Server to resend data.




If you see an unequal count, rerun the report to make sure it was not caused by a transitory issue. An unequal record count can occur due to replication processing at the time the tool generated the report.

For a very large source table or a table that has filters set in SAP LT Replication Server for initial load or replication, the Replication Validation tool might not be able to count all of the records that are required for an equal count.

#### Scheduling validation checks

You can schedule the Replication Validation tool to run automatically at intervals by using the SAP background job functionality.

## Edit the BigQuery field map in a CSV file

The following sections describe how to export the default field mapping so that data engineers or BigQuery administrators can edit the target field values without requiring access to SAP LT Replication Server.

### Create a spreadsheet or text file of the default field mappings

To create a CSV file for editing outside of SAP LT Replication Server:

  1. Run the `/GOOG/SLT_SETTINGS` transaction.

  2. In the **SLT Settings Maintenance** screen, specify the following values:

     * In the **Settings Table** field, specify **Fields**.
     * In the **Mass Transfer Key** field, specify the ID of the mass transfer that you are updating.
     * In the **Table Name** field, either leave the field blank to work with all fields from all tables or specify a table name to work with a specific table.
     * Leave all other fields blank.
  3. Click the **Execute** icon. The **BigQuery Settings Maintenance - Fields** screen displays.

  4. On the **BigQuery Settings Maintenance - Fields** screen, hide all columns except for those in the following list by right-clicking on the column headings and selecting **Hide** from the drop-down menu:

     * SAP Table Name
     * SAP Field Name
     * External Data Element
     * External Field Name
     * Field Description
  5. With the five remaining columns displayed, click the **Export** icon.

  6. From the **Export** menu, select one of the following options:

     * **Spreadsheet**
     * **Local file**. For ease of converting the file contents to CSV format, we recommend saving the file in the **Text with tabs** format.
  7. Save the default field mappings by clicking the **Checkmark** icon.




### Convert the spreadsheet or text file to CSV format

To upload edited field mappings by using the custom transaction `/GOOG/SLT_SETTINGS`, the field mappings must be in CSV format.

If you are using a spreadsheet, save the spreadsheet as a CSV file before you upload the file.

If you are using a local file in a tab-separated format or any other format, you need to modify the file to conform to CSV format.

For example:
    
    
    SAP Table,SAP Field Name,External Data Element,External Field Name,Field Description
    SAP_TABLE_NAME,SAP_FIELD_NAME1,BIGQUERY_DATA_TYPE,BIGQUERY_FIELD_NAME1,BIGQUERY_FIELD_DESCRIPTION1
    SAP_TABLE_NAME,SAP_FIELD_NAME2,BIGQUERY_DATA_TYPE,BIGQUERY_FIELD_NAME2,BIGQUERY_FIELD_DESCRIPTION2
    SAP_TABLE_NAME,SAP_FIELD_NAME3,BIGQUERY_DATA_TYPE,BIGQUERY_FIELD_NAME3,BIGQUERY_FIELD_DESCRIPTION3
    

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

  6. If you receive a security warning, click **Allow**. The file loads and the modified values in the file appear on the applicable rows in the **BigQuery Settings Maintenance - Fields** screen.

  7. Click the **Save** icon.

  8. To confirm the values are applied, compare the values in the CSV file with the values that are displayed by SAP LT Replication Server.




## Handling errors in the source data

Upon receiving a chunk of records from BigQuery Connector for SAP, the BigQuery streaming API checks for data errors before inserting any records into the BigQuery table.

You can control how the BigQuery API and the BigQuery Connector for SAP respond when data errors are found by specifying the following flags in mass transfer settings:

  * The `Skip Invalid Records` (`SKIP`) flag
  * The `Break at First Error Flag` (`BREAK`) flag



### The `SKIP` flag

If you specify the `SKIP` flag, when the BigQuery API receives a chunk of records and finds a record with a data error, then the BigQuery API discards, or _skips_ , the record with the error and continues inserting all other records from the chunk into the BigQuery table.

If you do not specify the `SKIP` flag, when BigQuery finds a record with a data error, BigQuery discards the entire chunk without inserting any records from it into the BigQuery table. This is the default behavior.

Specifying the `SKIP` flag is best for development and QA environments, and is not recommended for production environments.

You can specify `SKIP` flag in the `/GOOG/SLT_SETTINGS` transaction when you are configuring replication. The specification is stored in the `/GOOG/BQ_MASTR` configuration table.

To see how `SKIP` specifications interact with `BREAK` specifications, see Matrix table for `SKIP` and `BREAK` interactions.

### The `BREAK` flag

If you specify the `BREAK` flag, when BigQuery Connector for SAP is notified by the BigQuery API that a data error was found in a record, BigQuery Connector for SAP stops sending records to BigQuery and terminates the replication job.

If you do not specify the `BREAK` flag, when BigQuery Connector for SAP is notified by BigQuery that a data error was found in a record, BigQuery Connector for SAP continues sending records to BigQuery by sending the next chunk and the replication job continues. This is the default behavior.

Specifying the `BREAK` flag is recommended in production environments.

You can specify `BREAK` flag in the `//GOOG/SLT_SETTINGS` transaction when you are configuring replication. The specification is stored in the `/GOOG/BQ_MASTR` configuration table.

To see how `BREAK` specifications interact with `SKIP` specifications, see Matrix table for `SKIP` and `BREAK` interactions.

### Matrix table for `SKIP` and `BREAK` interactions

You can configure BigQuery Connector for SAP to handle data errors in the following ways:

`SKIP` flag | `BREAK` flag | Behavior  
---|---|---  
FALSE | TRUE |  BigQuery discards the current chunk of records without inserting any records from the current chunk into the BigQuery table.  BigQuery Connector for SAP sends no more chunks of records from the current portion and tells SAP LT Replication Server to terminate the replication job.  This is the recommended setting.   
FALSE | FALSE |  BigQuery discards the current chunk of records without inserting any records from the current chunk into the BigQuery table.  BigQuery Connector for SAP sends any remaining chunks of records from the current portion of records and then tells SAP LT Replication Server to terminate the replication job.  This is the default.   
TRUE | TRUE |  BigQuery discards only the record that contains the error and inserts the rest of the records in the current chunk into the BigQuery table.  BigQuery Connector for SAP sends no more chunks of records from the current portion and retrieves the next portion. BigQuery Connector for SAP does not tell SAP LT Replication Server to terminate the replication job.   
TRUE | FALSE |  BigQuery discards only the record that contains the error and inserts the rest of the records in the current chunk into the BigQuery table.  BigQuery Connector for SAP sends any remaining chunks of records from the current portion and retrieves the next portion. BigQuery Connector for SAP does not tell SAP LT Replication Server to terminate the replication job.   
  
## Table structure changes

This section explains how to modify the SAP source table structure, for which an existing `LTRC` replication is in progress.

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

  3. In BigQuery, delete the column from the target BigQuery table. For more information about the steps to delete a column from an existing table, see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/managing-table-schemas#delete_a_column).

  4. In your SLT system, resume the replication using transaction `LTRC`.

  5. In your SLT system, recreate the SLT triggers. For more information from SAP about how to recreate SLT triggers, see [SAP Note 2254376 - SLT trigger(s) in an inconsistent state](https://launchpad.support.sap.com/#/notes/0002254376).

  6. If the replication status is `Load /Replication blocked`, then reset the replication status using transaction `LTRC`. For more information from SAP about how to reset the replication status, see [SAP Note 2204955 - SLT tables are in status 'Load /Replication blocked'](https://launchpad.support.sap.com/#/notes/2204955).

  7. Clear the old logs, if any.

  8. Add, update, or delete an entry in the source table.

  9. Validate the replication result in BigQuery.




### Change the data type of an existing column

When you change the data type of an existing column in SAP source table, you need to follow specific steps depending on whether you are changing the data type to a compatible or non-compatible data type with the target BigQuery table.

A data type is compatible with the data type in the target BigQuery table when the existing data type and new data type of an existing column map to the same data type in the target BigQuery table. For example, if the data type of a column is changed from `INT1` to `INT2` in a source table, then both the data types are compatible with the data type `INTEGER` in the target BigQuery table.

For more information about data type mapping in BigQuery Connector for SAP, see [Data type mapping](https://docs.cloud.google.com/sap/docs/bq-connector/2.0/planning#data_type_mapping).

#### Change the data type to a compatible data type

To change the data type of an existing column to a compatible data type, follow these steps:

  1. Change the data type to a compatible data type in the source system. As a result of this step, the existing SLT triggers are either deleted or changed to an inconsistent state.

  2. In your SLT system, recreate the SLT triggers. For more information from SAP about how to recreate SLT triggers, see [SAP Note 2254376 - SLT trigger(s) in an inconsistent state](https://launchpad.support.sap.com/#/notes/0002254376).

  3. If the replication status is `Load /Replication blocked`, then reset the replication status using transaction `LTRC`. For more information from SAP about how to reset the replication status, see [SAP Note 2204955 - SLT tables are in status 'Load /Replication blocked'](https://launchpad.support.sap.com/#/notes/2204955).

  4. Clear the old logs, if any.

  5. Add, update, or delete an entry in the source table.

  6. Validate the replication result in BigQuery.




#### Change the data type to a non-compatible data type

To change the data type of an existing column to a non-compatible data type, follow these steps:

  1. In your SLT system, stop the replication using transaction `LTRC`.
  2. In BigQuery, delete the target table.
  3. Change the data type in the source system.
  4. In your SLT system, start the replication using transaction `LTRC`.

**Note:** Stop replication and Start replication steps reload the records into BigQuery.

## Enhancement exits

BigQuery Connector for SAP provides several enhancement points in its code where an ABAP developer can insert code to add custom functionality.

The following table lists the functions that the enhancement points support, the methods, and the class that contains the enhancement point.

Function | Class | Method | Spot | Option  
---|---|---|---|---  
Update the mapping for a field, such as the external field name, the data type, and so on. | `/GOOG/CL_IUUC_REPL_RUNTIME` | `CREATE_FLD_MAPPINGS` | `/GOOG/ES_IUUC_REPL_RUNTIME` | `/GOOG/UPDATE_FIELD_MAPPING`  
Update the mapping for the field table by adding or removing fields.  | `/GOOG/CL_IUUC_REPL_RUNTIME` | `CREATE_FLD_MAPPINGS` | `/GOOG/ES_IUUC_REPL_RUNTIME` | `/GOOG/UPDATE_FIELD_MAPPINGS`  
Change the value of a source field before the field is converted to a target field. | `/GOOG/CL_IUUC_REPL_RUNTIME_BQ` | `FILL_TARGET_RECORDS` | `/GOOG/ES_IUUC_REPL_RUNTIME_BQ` | `/GOOG/CHANGE_SOURCE_FIELD`  
After a source field is converted to a target field in the target table, change the value of the target field. | `/GOOG/CL_IUUC_REPL_RUNTIME_BQ` | `FILL_TARGET_RECORDS` | `/GOOG/ES_IUUC_REPL_RUNTIME_BQ` | `/GOOG/FILL_TARGET_FIELD`  
Add a field to the target table that does not exist in the source table during the source-to-target table conversion. | `/GOOG/CL_IUUC_REPL_RUNTIME_BQ` | `FILL_TARGET_RECORDS` | `/GOOG/ES_IUUC_REPL_RUNTIME_BQ` | `/GOOG/FILL_EXTRA_FIELD`  
Prepare a BigQuery schema field before the BigQuery table is created. | `/GOOG/CL_GCP_CLIENT_BQ` | `PREP_BQ_TABLE_SCHEMA` | `/GOOG/ES_GCP_CLIENT_BQ` | `/GOOG/PREPARE_SCHEMA_FIELD`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
