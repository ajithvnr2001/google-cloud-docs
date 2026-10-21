---
url: https://docs.cloud.google.com/cortex/docs/v6/operational-sap/
title: Integration with SAP \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:12:22.093318+00:00
---

# Integration with SAP  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/v6/operational-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 6 Guides ](https://docs.cloud.google.com/cortex/docs/v6/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integration with SAP

This page describes the integrating steps for SAP operational workloads (SAP ECC and SAP S/4 HANA) in the Cortex Framework Data Foundation. Cortex Framework can accelerate the integration of SAP data with BigQuery using predefined data processing templates with Dataflow pipelines through to BigQuery, while Managed Service for Apache Airflow schedules and monitors these Dataflow pipelines for getting insights from your SAP operational data.

**Note:** Before configuring the integration for a workload, follow the steps for [Cortex Framework Data Foundation deployment](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).

The [`config.json`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/config/config.json) file in the [Cortex Framework Data Foundation repository](https://github.com/GoogleCloudPlatform/cortex-data-foundation) configures the settings required to transfer data from any data source, including SAP. This file contains the following parameters for operational SAP workloads:
    
    
      "SAP": {
            "deployCDC": true,
            "datasets": {
                "cdc": "",
                "raw": "",
                "reporting": "REPORTING"
            },
            "SQLFlavor": "ecc",
            "mandt": "100"
        }
    

The following table describes the value for each SAP operational parameter:

**Parameter** | **Meaning** | **Default Value** | **Description**  
---|---|---|---  
`SAP.deployCDC` | Deploy CDC  | `true` | Generate CDC processing scripts to run as DAGs in Managed Airflow.   
`SAP.datasets.raw` | Raw landing dataset  | \-  | Used by the CDC process, this is where the replication tool lands the data from SAP. If using test data, create an empty dataset.   
`SAP.datasets.cdc` | CDC Processed Dataset  | \-  | Dataset that works as a source for the reporting views, and target for the records processed DAGs. If using test data, create an empty dataset.   
`SAP.datasets.reporting` | Reporting Dataset SAP  | `"REPORTING"` | Name of the dataset that is accessible to end users for reporting, where views and user-facing tables are deployed.   
`SAP.SQLFlavor` | SQL flavor for source system  | `"ecc"` | `s4` or `ecc`. For testing data, keep the default value (`ecc`).   
`SAP.mandt` | Mandant or Client  | `"100"` | Default mandant or client for SAP. For testing data, keep the default value (`100`).   
`SAP.languages` | Language filter  | `["E","S"]` | SAP language codes (SPRAS) to use for relevant fields (such as names).   
`SAP.currencies` | Currency filter  | `["USD"]` | SAP target currency codes (TCURR) for currency conversion.   
**Note:** If using test data, make sure to use default values for `mandt`, `languages`, and `currencies`.

While there is not a minimum version of SAP that is required, the ECC models have been developed on the current earliest supported version of SAP ECC. Differences in fields between our system and other systems are expected, regardless of the version.

## Data Model

This section describes the SAP (ECC and S/4 HANA) Data Models using the Entity Relationship Diagrams (ERD).

### SAP ECC

[![Entity Relationship Diagram for SAP ECC](https://docs.cloud.google.com/cortex/docs/images/erd_ecc.png)](https://docs.cloud.google.com/static/cortex/docs/images/erd_ecc.png)

**Figure 2**. SAP ECC: Entity Relationship Diagram.

### SAP S/4 HANA

[![Entity Relationship Diagram for SAP S/4 HANA](https://docs.cloud.google.com/cortex/docs/images/erd_s4.png)](https://docs.cloud.google.com/static/cortex/docs/images/erd_s4.png)

**Figure 2**. SAP S/4 HANA: Entity Relationship Diagram.

### Base views

These are the blue objects in the ERD and are views on CDC tables with no transforms other than some column name aliases. See scripts in [`src/SAP/SAP_REPORTING`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SAP/SAP_REPORTING).

### Reporting views

These are the green objects in the ERD and contain the relevant dimensional attributes used by the reporting tables. See scripts in [`src/SAP/SAP_REPORTING`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SAP/SAP_REPORTING).

### Utility or BQML view

These are the yellow objects in the ERD and contain the joined facts and dimensions specific type of view used for data analysis and reporting. See scripts on [`src/SAP/SAP_REPORTING`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SAP/SAP_REPORTING).

### Additional Tags

The color-coded tags on this ERD represent the following features of the reporting tables:

**Tag** | **Color** | **Description**  
---|---|---  
`L` | Yellow  | This tag refers to a data element or attribute that specifies the language in which the data is stored or displayed.   
`S/4` | Red  | This tag indicates that specific attributes are specific for SAP S/4 HANA (this object may not be in SAP ECC).   
`MANDT` | Purple  | This tag indicates that specific attributes contain the MANDT parameter (represents the client or client ID) to determine which client or company instance a specific data record belongs to.   
`EXT` | Red  | This tag indicates that specific objects are populated by DAGs or external datasets. This means that the marked entity or table is not directly stored in the SAP system itself, but it can be extracted and loaded into SAP using a DAG or other mechanism.   
`T` | Purple  | This tag indicates that specific attributes will automatically be materialized using the configured DAG.   
`S` | Red  | This tag indicates that the data within an entity or tables are influenced or affected by multiple currencies.   
  
## Prerequisites for SAP replication

Consider the following prerequisites for SAP replication data with Cortex Framework Data Foundation:

  * **Data Integrity** : Cortex Framework Data Foundation expects SAP tables to be replicated with identical field names, types, and data structures as they exist in SAP. As long as the tables are replicated with the same format, names of fields and granularity as in the source, there is no need to use a specific replication tool.
  * **Table Naming** : BigQuery table names must be created in lowercase.
  * **Table Configuration** : The list of tables used by SAP models is available and configurable in the CDC (Change Data Capture) [`cdc_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-dag-generator/blob/main/cdc_settings.yaml) file. If a table is not listed during deployment, the models depending on it would fail, although other non-dependent models would deploy successfully.
  * **Specific considerations[BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning)**: 
    * **Table Mapping** : About the conversion option, follow the [default table mapping documentation](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#default_data_type_mapping).
    * **Disabling Record Compression** : We **recommend to disable** [record compression](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#record_compression) which could impact both the Cortex CDC layer and the Cortex reporting dataset.
  * **Metadata Replication** : If you aren't deploying test data and generating CDC DAG scripts during deployment, make sure table `DD03L` for SAP metadata is replicated from SAP in the source project. This table contains metadata about tables, such as the list of keys, and is needed for the CDC generator and dependency resolver to work. This table also lets you add tables not covered by the model, for example custom or Z tables, so CDC scripts could be generated.
  * **Handling Minor Table Name Variations** : If there is a minor differences in a table name, some views might fail not finding required fields, because SAP systems might have minor variations due to versions or add-on, or because some replication tools may have slightly different handling of special characters. We recommend to execute the deployment with `turboMode : false` to spot the most failures in one attempt. Some common issues include:

    * Fields starting with `_` (for example, `_DATAAGING`) have their `_` removed.
    * Fields can't start with `/` in BigQuery. Make sure to update the [CDC script generation code](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/SAP/SAP_CDC/src/generate_query.py#L492) to align with your replication settings.

In this situation, you can adjust the failing view to select the field as it is landed by your replication tool of choice.




## Replicating raw data from SAP

The purpose of the Data Foundation is to expose data and analytics models for reporting and applications. The models consume the data replicated from an SAP system using a preferred replication tool, like those listed in the [Data Integration Guides for SAP](https://docs.cloud.google.com/sap/docs/sap-data-integration-guides).

Data from SAP system (either ECC or S/4 HANA) are replicated in raw form. The data is copied directly from SAP to BigQuery without any changes to its structure. It's essentially a mirror image of the tables in your SAP system. BigQuery uses lowercase table names for its data model. So, even though your SAP tables might have uppercase names (like `MANDT`), they are converted to lowercase (like `mandt`) in BigQuery.

## Change Data Capture (CDC) processing

**Note:** For more information about the CDC processing within Cortex Framework, see [Change Data Capture (CDC) processing](https://docs.cloud.google.com/cortex/docs/v6/cdc).

Choose one of the following CDC processing modes that Cortex Framework offers for replication tools to load records from SAP:

  * **Append-always** : Insert every change in a record with a timestamp and an operation flag (Insert, Update, Delete), so the last version can be identified.
  * **Update when landing** (merge or upsert): Create an updated version of a record on landing in the `change data capture processed`. It performs the CDC operation in BigQuery.



Cortex Framework Data Foundation supports both modes, although for append-always, it provides CDC processing templates. Some capabilities need to be commented out for update on landing. For example, [OneTouchOrder.sql](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/SAP/SAP_REPORTING/OneTouchOrder.sql) and all its dependent queries. The capability can be replaced with tables like CDPOS.

![CDC processing](https://docs.cloud.google.com/static/cortex/docs/v6/images/cdc-options.png)

**Figure 1**. CDC processing.

### Configure CDC templates for tools replicating in append-always mode

**We strongly recommend configuring the`cdc_settings.yaml` according to your needs.** Some default frequencies may result in unnecessary cost if the business doesn't require such level of data freshness. If using a tool that runs in append-always mode, Cortex Framework Data Foundation provides CDC templates to automate the updates and create a latest version of the truth or digital twin in the CDC processed dataset.

You can use the configuration in the file `cdc_settings.yaml` if you need to generate CDC processing scripts. See Set up CDC Processing for options. For test data, you can leave this file as a default.

Make all required changes to the [DAG templates](https://github.com/GoogleCloudPlatform/cortex-data-foundation/tree/main/src/SAP/SAP_CDC) according your instance of Airflow or Managed Airflow. For more information, see [Gathering Managed Airflow settings](https://docs.cloud.google.com/cortex/docs/v6/gathering-settings).

**Optional** : If you want to add and process tables individually after deployment, you can modify the [`cdc_settings.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/SAP/SAP_CDC/cdc_settings.yaml) file to process only the tables you need and re-execute the specified module calling [`src/SAP_CDC/cloudbuild.cdc.yaml`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/SAP/SAP_CDC/cloudbuild.cdc.yaml) directly.

### Set up CDC processing

During deployment, you can choose to merge changes in real time using a view in BigQuery or scheduling a merge operation in Managed Airflow (or any other instance of Apache Airflow). Managed Airflow can schedule the scripts to process the merge operations periodically. Data is updated to its latest version every time the merge operations execute, however, more frequent merge operations translate into higher costs. Customize the scheduled frequency according your business needs. For more information, see [scheduling supported by Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dag-run.html).

The following example script shows an extract from the configuration file:
    
    
      data_to_replicate:
        - base_table: adrc
          load_frequency: "@hourly"
        - base_table: adr6
          target_table: adr6_cdc
          load_frequency: "@daily"
    

This configuration sample file does the following:

  1. Create a copy from `SOURCE_PROJECT_ID.REPLICATED_DATASET.adrc` into `TARGET_PROJECT_ID.DATASET_WITH_LATEST_RECORDS.adrc`, if the latter does not exist.
  2. Create a CDC script in the specified bucket.
  3. Create a copy from `SOURCE_PROJECT_ID.REPLICATED_DATASET.adr6` into `TARGET_PROJECT_ID.DATASET_WITH_LATEST_RECORDS.adr6_cdc`, if the latter does not exist.
  4. Create a CDC script in the specified bucket.



If you want to create DAGs or runtime views to process changes for tables that exist in SAP and are not listed in the file, add them to this file before deployment. This works as long as the table `DD03L` is replicated in the source dataset and the schema of the custom table is present in that table. For example, the following configuration creates a CDC script for custom table _`zztable_customer`_ and a runtime view to scan changes in real time for another custom table called _`zzspecial_table`_ :
    
    
        - base_table: zztable_customer
          load_frequency: "@daily"
        - base_table: zzspecial_table
          load_frequency: "RUNTIME"
    

### Sample generated template

The following template generates the processing of changes. Modifications, such as the name of the timestamp field, or additional operations, can be modified at this point:
    
    
      MERGE `${target_table}` T
      USING (
         SELECT *
         FROM `${base_table}`
         WHERE
            recordstamp > (
                SELECT IF(
                    MAX(recordstamp) IS NOT NULL,
                    MAX(recordstamp),
                    TIMESTAMP("1940-12-25 05:30:00+00"))
                FROM `${target_table}` )
      ) S
      ON ${p_key}
      WHEN MATCHED AND S.operation_flag='D' AND S.is_deleted = true THEN
        DELETE
      WHEN NOT MATCHED AND S.operation_flag='I' THEN
        INSERT (${fields})
        VALUES
        (${fields})
      WHEN MATCHED AND S.operation_flag='U' THEN
      UPDATE SET
          ${update_fields}
    

Alternatively, if your business requires near-real time insights and the replication tool supports it, the deployment tool accepts the option `RUNTIME`. This means a CDC script won't be generated. Instead, a view would scan and fetch the latest available record at runtime for [immediate consistency](https://docs.cloud.google.com/bigquery/docs/migration/database-replication-to-bigquery-using-change-data-capture#immediate_consistency_approach).

### Directory structure for CDC DAGs and Scripts

The Cloud Storage bucket structure for SAP CDC DAGs expects the SQL files to be generated in `/data/bq_data_replication`, as the following example. You can modify this path prior to deployment. If you don't have an environment of Managed Service for Apache Airflow available yet, you can create one afterwards and move the files into the DAG bucket.
    
    
    with airflow.DAG("CDC_BigQuery_${base table}",
                    template_searchpath=['/home/airflow/gcs/data/bq_data_replication/'], ##example
                    default_args=default_dag_args,
                    schedule_interval="${load_frequency}") as dag:
        start_task = DummyOperator(task_id="start")
        copy_records = BigQueryOperator(
          task_id='merge_query_records',
            sql="${query_file}",
            create_disposition='CREATE_IF_NEEDED',
            bigquery_conn_id="sap_cdc_bq", ## example
            use_legacy_sql=False)
        stop_task = DummyOperator (task_id="stop")
        start_task >> copy_records >> stop_task
    

The scripts that process data in Airflow or Managed Service for Apache Airflow are purposefully generated separately from the Airflow-specific scripts. This lets you port those scripts to another tool of choice.

### CDC fields required for MERGE operations

Specify the following parameters for the automated generation of CDC batch processes:

  * **Source project + dataset:** Dataset where the SAP data is streamed or replicated. For the CDC scripts to work by default, the tables need to have a timestamp field (called recordstamp) and an operation field with the following values, all set during replication: 
    * **I** : for Insert.
    * **U** : for Update.
    * **D** : for Deletion.
  * **Target project + dataset for the CDC processing** : The script generated by default generates the tables from a copy of the source dataset if they don't exist.
  * **Replicated tables** : Tables for which the scripts need to be generated
  * **Processing frequency** : Following the Cron notation, how frequently the DAGs are expected to run:
  * **Target Cloud Storage bucket** where the CDC output files are copied.
  * **Connection's name** : The name of the connection used by Managed Airflow.
  * **(Optional) Name of the target table:** Available if the result of the CDC processing remains in the same dataset as the target.



### Performance optimization for CDC tables

For certain CDC datasets, you might want to take advantages of BigQuery [table partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables), [table clustering](https://docs.cloud.google.com/bigquery/docs/clustered-tables), or both. This choice depends on the following factors:

  * Size and data of the table.
  * Columns available in the table.
  * Need for real-time data with views.
  * Data materialized as tables.



By default, CDC settings don't apply table partitioning or table clustering. The choice is yours to configure it based on what works best for you. To create tables with partitions or clusters, update the `cdc_settings.yaml` file with relevant configurations. For more information, see [Table Partition](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#table_partition) and [Cluster Settings](https://docs.cloud.google.com/cortex/docs/v6/deployment-step-five#cluster_settings).

  1. This feature only applies when a dataset in `cdc_settings.yaml` is configured for replication as a table (for example, `load_frequency = "@daily"`), and not defined as a view (`load_frequency = "RUNTIME"`).
  2. A table can be both, a partitioned table as well as a clustered table.



If you are using a replication tool that allows partitions in the raw dataset, like the BigQuery Connector for SAP, [setting time-based partitions](https://docs.cloud.google.com/sap/docs/bq-connector/latest/planning#table_partitioning) in the raw tables is recommended. The type of partition works better if it matches the frequency for CDC DAGs in the `cdc_settings.yaml` configuration. For more information, see [Design considerations for SAP data modeling in BigQuery](https://cloud.google.com/blog/products/sap-google-cloud/design-considerations-for-sap-data-modeling-in-bigquery).

## Optional: Configuring the SAP Inventory Module

Cortex Framework SAP Inventory module includes `InventoryKeyMetrics` and `InventoryByPlant` views that provide key insights about your inventory. These views are backed by monthly and weekly snapshots tables using specialized DAGs. Both can be run at the same time and won't interfere with each other.

**Note:** An up-to-date monthly snapshot table is required for the `InventoryKeyMetrics` view, while an up-to-date weekly snapshot table is required for the `InventoryByPlant` view.

To update either or both snapshot tables, follow these steps:

  1. Update `SlowMovingThreshold.sql` and `StockCharacteristicsConfig.sql` to define slow moving threshold and stock characteristics for different material types, based on your requirements.

**Note:** Starting from Cortex Framework v6.0, these scripts are located under the `src/SAP/SAP_REPORTING/{SQL_FLAVOR}` directory, where `{SQL_FLAVOR}` is either `ECC` or `S4`. Make sure to update the correct scripts based on your system.
  2. For initial load or full refresh, run `Stock_Monthly_Snapshots_Initial` and `Stock_Weekly_Snapshots_Initial` DAGs.

  3. For subsequent refreshes, schedule or run the following DAGs:

     * Monthly and weekly updates: 
       * `Stock_Monthly_Snapshots_Periodical_Update`
       * `Stock_Weekly_Snapshots_periodical_Update`
     * Daily Update: 
       * `Stock_Monthly_Snapshots_Daily_Update`
       * `Stock_Weekly_Snapshots_Update_Daily`
**Note:** DAG names here refer to the DAG names after deployment, as displayed in Airflow UI.
  4. Refresh the intermediate `StockMonthlySnapshots` and `StockWeeklySnapshots` views, followed by `InventoryKeyMetrics` and `InventoryByPlants` views, respectively, to expose the refreshed data.




## Optional: Configuring Product Hierarchy Texts view

The Product Hierarchy Texts view flattens materials and their product hierarchies. The resulting table can be used to feed the `Trends` add-on a list of terms to retrieve _Interest Over Time_. Configure this view with the following steps:

  1. Adjust the levels of the hierarchy and the language in file [`prod_hierarchy_texts.sql`](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/src/SAP/SAP_REPORTING/local_k9/prod_hierarchy_texts/prod_hierarchy_texts.sql), under the markers for `## CORTEX-CUSTOMER`.
  2. If your product hierarchy contains more levels, you might need to add an additional SELECT statement similar to the [Common Table Expression](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#with_clause) `h1_h2_h3`.

There might be additional customizations depending on the source systems. We recommend getting the business users or analysts involved early in the process to help spot these.




## Optional: Configuring hierarchy flattening views

Starting with release [v6.0](https://docs.cloud.google.com/cortex/docs/v6/release-notes#release_60), Cortex Framework supports hierarchy flattening as Reporting views. This is a major improvement over the [legacy hierarchy flattener](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/docs/deprecated/README_SAP.md#optional-configuring-the-flattener-for-sap-hierarchies) as it now flattens the entire hierarchy, better optimizes for S/4 by utilizing S/4 specific tables instead of legacy ECC tables, and also significantly improves performance.

**Note:** We recommend to migrate from the legacy hierarchy flattener solution. For more information about how to migrate, see the section migrate from the legacy hierarchy flattener solution.

### Summary of Reporting Views

Find the following views related to hierarchy flattening:

**Type of hierarchy** | **Table containing flattened hierarchy only** | **Views for visualizing flattened hierarchy** | **P &L integration logic using this hierarchy**  
---|---|---|---  
Financial Statement Version (FSV)  | `fsv_glaccounts` | `FSVHierarchyFlattened` | `ProfitAndLossOverview`  
Profit Center  | `profit_centers` | `ProfitCenterHierarchyFlattened` | `ProfitAndLossOverview_ProfitCenterHierarchy`  
Cost Center  | `cost_centers` | `CostCenterHierarchyFlattened` | `ProfitAndLossOverview_CostCenterHierarchy`  
  
Consider the following when using hierarchy flattening views:

  * The **flattened hierarchy only views** are functionally equivalent to the tables generated by the legacy hierarchy flattener solution.
  * The **overview views** are not deployed by default as they are meant to showcase BI logic only. Find their source code under the `src/SAP/SAP_REPORTING` directory.



### Configuring Hierarchy Flattening

Based on the hierarchy you are working with, the following input parameters are required:

**Type of hierarchy** | **Required parameter** | **Source field (ECC)** | **Source field (S4)**  
---|---|---|---  
Financial Statement Version (FSV)  | Chart of account  | `ktopl` | `nodecls`  
Hierarchy name  | `versn` | `hryid`  
Profit center  | Class of the set  | `setclass` | `setclass`  
Organizational Unit: Controlling Area or additional key for the set.  | `subclass` | `subclass`  
Cost Center  | Class of the set  | `setclass` | `setclass`  
Organizational Unit: Controlling Area or additional key for the set.  | `subclass` | `subclass`  
  
If you're unsure about the exact parameters, ask a Finance or Controlling SAP consultant.

After the parameters are collected, update the `## CORTEX-CUSTOMER` comments within each of the corresponding directories, based on your requirements:

**Type of Hierarchy** | **Code location**  
---|---  
Financial Statement Version (FSV)  | `src/SAP/SAP_REPORTING/local_k9/fsv_hierarchy`  
Profit Center  | `src/SAP/SAP_REPORTING/local_k9/profitcenter_hierarchy`  
Cost Center  | `src/SAP/SAP_REPORTING/local_k9/costcenter_hierarchy`  
  
If applicable, make sure to update the `## CORTEX-CUSTOMER` comments within the relevant reporting views under `src/SAP/SAP_REPORTING` directory well.

### Solution Details

The following source tables are used for hierarchy flattening:

**Type of Hierarchy** | **Source Tables (ECC)** | **Source Tables (S4)**  
---|---|---  
Financial Statement Version (FSV)  | 

  * `fagl_011pc`
  * `fagl_011zc`
  * `ska1`

| 

  * `hrrp_node`
  * `hrrp_directory`
  * `ska1`

  
Profit Center  | 

  * `setheader`
  * `setnode`
  * `setleaf`

| 

  * `sethanahier0106`

  
Cost Center  | 

  * `setheader`
  * `setnode`
  * `setleaf`

| 

  * `sethanahier0101`

  
  
### Visualizing the hierarchies

Cortex's SAP hierarchy flattener solution flattens the entire hierarchy. If you would like to create a visual representation of the hierarchy loaded that is comparable to what SAP shows in the UI, query one of the views for visualizing flattened hierarchies with `IsLeafNode=True` condition.

### Migrating from the legacy hierarchy flattener solution

To migrate from the [legacy hierarchy flattening solution prior to Cortex v6.0](https://github.com/GoogleCloudPlatform/cortex-data-foundation/blob/main/docs/deprecated/README_SAP.md#optional-configuring-the-flattener-for-sap-hierarchies), replace the tables as the following table shows. Make sure to check field names for accuracy, as some field names have been slightly modified. For example, `prctr` in `cepc_hier` is now `profitcenter` in `profit_centers` table.

**Type of hierarchy** | **Replace this table:** | **With:**  
---|---|---  
Financial Statement Version (FSV)  | `ska1_hier` | `fsv_glaccounts`  
Profit Center  | `cepc_hier` | `profit_centers`  
Cost Center  | `csks_hier` | `cost_centers`  
**Note:** If a hierarchy node doesn't have any cost center, profit center or general ledger account mapped to it, that node won't be included in the output table views, as these nodes have no functional significance.

## Optional: Configuring the SAP Finance Module

Cortex Framework SAP Finance module includes `FinancialStatement`, `BalanceSheet` and `ProfitAndLoss` views that provide key financial insights.

To update these Finance tables, follow these steps:

### For initial load

  1. After deployment, ensure your CDC dataset is properly populated (run any CDC DAGs as required).
  2. Ensure Hierarchy Flattening Views are properly configured for the types of hierarchies you are using (FSV, Cost Center, and Profit Center).
  3. Run `financial_statement_initial_load` DAG.

**Note:** DAG names here refer to the DAG names after deployment, as displayed in Airflow UI.
  4. If deployed as tables (recommended), refresh the following in order by running their corresponding DAGs:

     1. `Financial_Statements`
     2. `BalanceSheets`
     3. `ProfitAndLoss`



### For periodical refresh

  1. Ensure Hierarchy Flattening Views are properly configured and refreshed up to date for the types of hierarchies you are using (FSV, Cost Center, and Profit Center).
  2. Schedule or run `financial_statement_periodical_load` DAG.

**Note:** Scheduling this DAG based on your business needs to ensure downstream tables get updated correctly as well.
  3. If deployed as tables (recommended), refresh the following in order by running their corresponding DAGs:

     1. `Financial_Statements`
     2. `BalanceSheets`
     3. `ProfitAndLoss`



To visualize the data from these tables, refer to the following Overview views:

  * `ProfitAndLossOverview.sql` if you are using FSV Hierarchy.
  * `ProfitAndLossOverview_CostCenter.sql` if you are using Cost Center Hierarchy.
  * `ProfitAndLossOverview_ProfitCenter.sql` if you are using Profit Center Hierarchy.



## Optional: Enabling task dependent DAGs

Cortex Framework optionally provides recommended dependency settings for most SAP SQL tables (ECC and S/4 HANA), where all dependent tables can be updated by a single DAG. You can customize them further. For more information, see [Task dependent DAGs](https://docs.cloud.google.com/cortex/docs/v6/optional-step-task-dependent-dags).

## What's next?

  * For more information about other data sources and workloads, see [Data sources and workloads](https://docs.cloud.google.com/cortex/docs/v6/data-sources-and-workloads).
  * For more information about the steps for deployment in production environments, see [Cortex Framework Data Foundation deployment prerequisites](https://docs.cloud.google.com/cortex/docs/v6/deployment-prerequisites).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
