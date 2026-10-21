---
url: https://docs.cloud.google.com/knowledge-catalog/docs/check-data-quality/
title: Use data quality tasks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:38.599793+00:00
---

# Use data quality tasks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/check-data-quality/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use data quality tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Knowledge Catalog (formerly Dataplex Universal Catalog) data quality tasks is a legacy offering based on open source software. We recommend that you start using the latest built-in [Automatic data quality](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview) offering.

This document shows you how to create Knowledge Catalog data quality tasks that let you schedule and run data quality checks for your built-in and external BigQuery tables.

For more information, see [Data quality tasks overview](https://docs.cloud.google.com/knowledge-catalog/docs/data-quality-tasks-overview).

## Before you begin

This document assumes that you have an existing Knowledge Catalog lake to create the data quality task in.

### Enable Google APIs and services

  1. Enable the Dataproc API.

[Enable the API](https://console.cloud.google.com/apis/library/dataproc.googleapis.com)

  2. [Enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-pga) for your network and subnetwork. Enable Private Google Access on the network that you plan to use with Knowledge Catalog data quality tasks. If you don't specify a network or subnetwork when you create the Knowledge Catalog data quality task, Knowledge Catalog uses the default subnet. In that case, you need to enable Private Google Access on the default subnet.




### Create a specification file

Knowledge Catalog uses [open source CloudDQ](https://github.com/GoogleCloudPlatform/cloud-data-quality) as the driver program. Knowledge Catalog data quality check requirements are defined within CloudDQ YAML specification files.

As input to the data quality task, you can have a single YAML file or a single zip archive containing one or more YAML files. It's recommended that you capture the data quality check requirements in separate YAML specification files, with one file for each section.

To prepare a specification file, do the following:

  1. Create one or more CloudDQ YAML specification files that define your data quality check requirements. For more information about the required syntax, see the About the specification file section of this document.

Save the YAML specification file in `.yml` or `.yaml` format. If you create multiple YAML specification files, save all of the files in a single zip archive.

  2. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  3. [Upload the specification file](https://docs.cloud.google.com/storage/docs/uploading-objects) to the Cloud Storage bucket.



#### About the specification file

Your CloudDQ YAML specification file needs to have the following sections:

  * Rules (defined in the top-level `rules` YAML node): A list of rules to run. You can create these rules from predefined rule types, such as `NOT_NULL` and `REGEX`, or you can extend them with custom SQL statements such as `CUSTOM_SQL_EXPR` and `CUSTOM_SQL_STATEMENT`. The `CUSTOM_SQL_EXPR` statement flags any row that `custom_sql_expr` evaluated to `False` as a failure. The `CUSTOM_SQL_STATEMENT` statement flags any value returned by the whole statement as a failure.

  * Row filters (defined in the top-level `row_filters` YAML node): SQL expressions returning a boolean value that define filters to fetch a subset of data from the underlying entity subject for validation.

  * Rule bindings (defined in the top-level `rule_bindings` YAML node): Defines `rules` and `rule filters` to apply to the tables.

  * Rule dimensions (defined in the `rule_dimensions` YAML node): Defines the allowed list of data quality rule dimensions that a rule can define in the corresponding `dimension` field.

For example:
        
        rule_dimensions:
          - consistency
          - correctness
          - duplication
          - completeness
          - conformance

The `dimension` field is optional for a rule. The rule dimensions section is mandatory if `dimension` is listed on any rule.




For more information, see the [CloudDQ reference guide](https://github.com/GoogleCloudPlatform/cloud-data-quality/blob/main/REFERENCE.md) and the sample specification files.

**Note:** Due to a CloudDQ limitation, you cannot have more than one top node for each section (such as `rules` or `rule_bindings`) in a single YAML file, as CloudDQ only parses the last node of each type within a file.

### Create a dataset to store the results

  * To store the results, [create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets).

The dataset must be in the same region as the tables that you run the data quality task on.

Knowledge Catalog uses this dataset, and it creates or reuses a table of your choice to store the results.




### Create a service account

[Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) that has the following Identity and Access Management (IAM) roles and permissions:

  * Read access to the Cloud Storage path containing the YAML specifications. You can use the [Storage Object Viewer role](https://cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) (`roles/storage.objectViewer`) on the Cloud Storage bucket.
  * Read access to BigQuery datasets with data to be validated. You can use the [BigQuery Data Viewer role](https://cloud.google.com/bigquery/docs/access-control#bigquery) (`roles/bigquery.dataViewer`).
  * Write access to the BigQuery dataset to create a table (if necessary) and write the results to that table. You can use the [BigQuery Data Editor role](https://cloud.google.com/bigquery/docs/access-control#bigquery) (`roles/bigquery.dataEditor`) at the dataset level.
  * [BigQuery Job User role](https://cloud.google.com/bigquery/docs/access-control#bigquery) (`roles/bigquery.jobUser`) at the project level in order to create BigQuery jobs in a project.
  * The Dataplex Metadata Reader role (`roles/dataplex.metadataReader`) at the project or lake level.
  * The [Service Usage Consumer role](https://cloud.google.com/service-usage/docs/access-control#predefined_roles) (`roles/serviceusage.serviceUsageConsumer`) at the project level.
  * The [Dataproc Worker role](https://cloud.google.com/dataproc/docs/concepts/iam/iam#roles) (`roles/dataproc.worker`).
  * The [`iam.serviceAccounts.actAs` permission](https://cloud.google.com/iam/docs/service-account-permissions#user-role) given to the user submitting the job.
  * The [Service account user role](https://cloud.google.com/iam/docs/service-account-permissions#user-role) granted to the Knowledge Catalog lake service account. You can [view the Knowledge Catalog lake service account in the Google Cloud console](https://cloud.google.com/knowledge-catalog/docs/manage-lake#viewing-a-lake).



### Use advanced settings

These steps are optional:

  * BigQuery runs data quality checks in the current project by default. You can choose a different project to run the BigQuery jobs. Use the `--gcp_project_id` `TASK_ARGS` argument for the `--execution-args` property of the task.

  * If the project ID specified to run BigQuery queries is different from the project in which the service account (specified by `--execution-service-account`) is created, ensure that the organization policy that [disables cross-project service account usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_creation) (`iam.disableServiceAccountCreation`) is turned off. Also, ensure that the service account can access the BigQuery job schedule in the project where BigQuery queries are being run.




## Limitations

All the tables specified for a given data quality task must belong to the same Google Cloud region.

## Schedule a data quality task

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Process** page. 

[Go to **Process**](https://console.cloud.google.com/dataplex/process)

  2. Click add_box **Create task**. 
  3. On the **Check Data Quality** card, click **Create task**.
  4. For **Dataplex lake** , choose your lake. 
  5. For **ID** , enter an ID. 
  6. In the **Data quality specification** section, do the following: 
     1. In the **Select GCS file** field, click **Browse**. 
     2. Select your Cloud Storage bucket.

     3. Click **Select**.

  7. In the **Results table** section, do the following:

     1. In the **Select BigQuery dataset** field, click **Browse**.

     2. Select the BigQuery dataset to store validation outcomes.

     3. Click **Select**.

     4. In the **BigQuery table** field, enter the name of the table to store the results. If the table doesn't exist, Knowledge Catalog creates it for you. Don't use the name `dq_summary` because it is reserved for internal processing tasks.

  8. In the **Service account** section, select a service account from the **User service account** menu.

  9. Click **Continue**.

  10. In the **Set schedule** section, configure the schedule for running the data quality task.

  11. Click **Create**.




### gcloud CLI

The following is an example execution of a data quality task that uses the Knowledge Catalog tasks gcloud CLI command:
    
    
    export USER_CLOUDDQ_YAML_CONFIGS_GCS_PATH="USER_CLOUDDQ_YAML_CONFIGS_GCS_PATH"
    
    # Google Cloud project where the Knowledge Catalog task is created.
    export GOOGLE_CLOUD_PROJECT="GOOGLE_CLOUD_PROJECT"
    
    # Google Cloud region for the Knowledge Catalog lake.
    export DATAPLEX_REGION_ID="DATAPLEX_REGION_ID"
    
    # Public Cloud Storage bucket containing the prebuilt data quality executable artifact. There is one bucket for each Google Cloud region.
    export DATAPLEX_PUBLIC_GCS_BUCKET_NAME="dataplex-clouddq-artifacts-${DATAPLEX_REGION_ID}"
    
    # The Knowledge Catalog lake where your task is created.
    export DATAPLEX_LAKE_ID="DATAPLEX_LAKE_ID"
    
    # The service account used for running the task. Ensure that this service account
    has sufficient IAM permissions on your project, including
    BigQuery Data Editor, BigQuery Job User,
    Dataplex Editor, Dataproc Worker, and Service
    Usage Consumer.
    export DATAPLEX_TASK_SERVICE_ACCOUNT="DATAPLEX_TASK_SERVICE_ACCOUNT"
    
    # If you want to use a different dataset for storing the intermediate data quality summary results
    and the BigQuery views associated with each rule binding, use the following:
    export CLOUDDQ_BIGQUERY_DATASET="CLOUDDQ_BIGQUERY_DATASET"
    
    # The BigQuery dataset where the final results of the data quality checks are stored.
    This could be the same as CLOUDDQ_BIGQUERY_DATASET.
    export TARGET_BQ_DATASET="TARGET_BQ_DATASET"
    
    # The BigQuery table where the final results of the data quality checks are stored.
    export TARGET_BQ_TABLE="TARGET_BQ_TABLE"
    
    # The unique identifier for the task.
    export TASK_ID="TASK_ID"
    
    gcloud dataplex tasks create \
        --location="${DATAPLEX_REGION_ID}" \
        --lake="${DATAPLEX_LAKE_ID}" \
        --trigger-type=ON_DEMAND \
        --execution-service-account="$DATAPLEX_TASK_SERVICE_ACCOUNT" \
        --spark-python-script-file="gs://${DATAPLEX_PUBLIC_GCS_BUCKET_NAME}/clouddq_pyspark_driver.py" \
        --spark-file-uris="gs://${DATAPLEX_PUBLIC_GCS_BUCKET_NAME}/clouddq-executable.zip","gs://${DATAPLEX_PUBLIC_GCS_BUCKET_NAME}/clouddq-executable.zip.hashsum","${USER_CLOUDDQ_YAML_CONFIGS_GCS_PATH}" \
        --execution-args=^::^TASK_ARGS="clouddq-executable.zip, ALL, ${USER_CLOUDDQ_YAML_CONFIGS_GCS_PATH}, --gcp_project_id='GOOGLE_CLOUD_PROJECT', --gcp_region_id='${DATAPLEX_REGION_ID}', --gcp_bq_dataset_id='${TARGET_BQ_DATASET}', --target_bigquery_summary_table='${GOOGLE_CLOUD_PROJECT}.${TARGET_BQ_DATASET}.${TARGET_BQ_TABLE}'," \
        "$TASK_ID"

Parameter | Description  
---|---  
`USER_CLOUDDQ_YAML_CONFIGS_GCS_PATH` | The Cloud Storage path to your data quality YAML configurations input for the data quality task. You can have a single YAML file in `.yml` or `.yaml` format or a zip archive containing multiple YAML files.  
`GOOGLE_CLOUD_PROJECT` | The Google Cloud project where the Knowledge Catalog task and BigQuery jobs are created.  
`DATAPLEX_REGION_ID` | The region of the Knowledge Catalog lake where the data quality task is created.  
`SERVICE_ACCOUNT` | The service account used for executing the task. Ensure this service account has sufficient IAM permissions as outlined in the Before you begin section.  
  
For `--execution-args`, the following arguments need to be passed as positioned arguments, and therefore in this order:

Argument | Description  
---|---  
`clouddq-executable.zip` | A precompiled executable that was passed in `spark-file-uris` from a public Cloud Storage bucket.  
`ALL` | Run all the rule bindings. Alternatively, you can provide specific rule bindings as a comma-separated list. For example, `RULE_1,RULE_2`.  
`gcp-project-id` | Project ID that runs the BigQuery queries.  
`gcp-region-id` | Region for running the BigQuery jobs for data quality validation. This region should be the same as the region for `gcp-bq-dataset-id` and `target_bigquery_summary_table`.  
`gcp-bq-dataset-id` | BigQuery dataset that is used to store the `rule_binding` views and intermediate data quality summary results.  
`target-bigquery-summary-table` | Table ID reference of the BigQuery table where the final results of the data quality checks are stored. Don't use the ID value `dq_summary` because it is reserved for internal processing tasks.  
`--summary_to_stdout` | (Optional) When this flag is passed, all the validation result rows created in the `dq_summary` table in the last run are logged as JSON records to Cloud Logging and `stdout`.  
**Note** : By default the Knowledge Catalog data quality task runs in the **Default** network. You could change the network by using one of the arguments: `--vpc-network-name` or `--vpc-sub-network-name`. See how to [set these arguments](https://docs.cloud.google.com/knowledge-catalog/docs/schedule-custom-spark-tasks#schedule_a_spark_java_python_task).

### API

  1. Replace the following:
         
         PROJECT_ID = "Your Knowledge Catalog Project ID"
         REGION = "Your Knowledge Catalog lake region"
         LAKE_ID = "Your Knowledge Catalog lake ID"
         SERVICE_ACC = "Your service account used for reading the data"
         DATAPLEX_TASK_ID = "Unique task ID for the data quality task"
         BUCKET_NAME = "Your Cloud Storage bucket name containing the CloudDQ configs or YAML specification"
         GCP_BQ_BILLING_PROJECT_ID = "Your BigQuery billing project"
         GCP_BQ_REGION_ID = "Your BigQuery dataset region ID" #Optional
         GCP_BQ_DATASET_ID = "Your BigQuery dataset to store the data quality summary results"
         TARGET_TABLE_NAME = "Your target table name to store the results in BigQuery dataset"

  2. Submit an HTTP POST request: 
         
         POST https://dataplex.googleapis.com/v1/projects/${PROJECT_ID}/locations/${REGION}/lakes/${LAKE_ID}/tasks?task_id=${DATAPLEX_TASK_ID}
         {
         "spark": {
             "python_script_file": f"gs://dataplex-clouddq-artifacts-us-central1/clouddq_pyspark_driver.py",
             "file_uris": [  f"gs://dataplex-clouddq-artifacts-us-central1/clouddq-executable.zip",
                             f"gs://dataplex-clouddq-artifacts-us-central1/clouddq-executable.zip.hashsum",
                             f"gs://dataplex-clouddq-artifacts-us-central1/your-clouddq-configs.zip"
                         ]
         },
         "execution_spec": {
             "args": {
                 "TASK_ARGS":f"clouddq-executable.zip, ALL, gs://BUCKET_NAME/your-clouddq-configs.zip, --gcp_project_id=${GCP_BQ_BILLING_PROJECT_ID}, --gcp_region_id=${GCP_BQ_REGION_ID}, --gcp_bq_dataset_id=${GCP_BQ_DATASET_ID}, --target_bigquery_summary_table=${GCP_BQ_BILLING_PROJECT_ID}.${GCP_BQ_DATASET_ID}.${TARGET_TABLE_NAME}"
             },
             "service_account": "SERVICE_ACC"
         },
         "trigger_spec": {
         "type": "ON_DEMAND"
         },
         "description": "${DATAPLEX_TASK_DESCRIPTION}"
         }




See also [Sample Airflow DAG for Knowledge Catalog data quality task](https://github.com/GoogleCloudPlatform/cloud-data-quality/blob/main/scripts/dataproc-workflow-composer/clouddq_composer_dataplex_task_job.py).

## Monitor a scheduled data quality task

See how to [monitor your task](https://docs.cloud.google.com/knowledge-catalog/docs/schedule-custom-spark-tasks#monitor_your_task).

## View the results

The results of the data quality validations are stored in the BigQuery dataset and summary table that you specified, as described in Create a dataset to store the results. The summary table contains the output summary for each combination of rule binding and rule for each validation run. The output in the summary table includes the following information:

Column name | Description  
---|---  
`dataplex_lake` | (string) ID of the Knowledge Catalog lake containing the table being validated.  
`dataplex_zone` | (string) ID of the Knowledge Catalog zone containing the table being validated.  
`dataplex_asset_id` | (string) ID of the Knowledge Catalog asset containing the table being validated.  
`execution_ts` | (timestamp) Timestamp of when the validation query was run.  
`rule_binding_id` | (string) ID of the rule binding for which validation results are reported.  
`rule_id` | (string) ID of the rule under the rule binding for which validation results are reported.  
`dimension` | (string) Data quality dimension of the `rule_id`. This value can only be one of the values specified in the `rule_dimensions` YAML node.  
`table_id` | (string) ID of the entity for which validation results are reported. This ID is specified under the `entity` parameter of the respective rule binding.  
`column_id` | (string) ID of the column for which validation results are reported. This ID is specified under the `column` parameter of the respective rule binding.  
`last_modified` | (timestamp) The last modified timestamp of the `table_id` being validated.  
`metadata_json_string` | (string) Key-value pairs of the metadata parameter content specified under the rule binding or during the data quality run.  
`configs_hashsum` | (string) The hash sum of the JSON document containing the rule binding and all its associated rules, rule bindings, row filters, and entity configurations. `configs_hashsum` allows tracking when the content of a `rule_binding` ID or one of its referenced configurations has changed.  
`dq_run_id` | (string) Unique ID of the record.  
`invocation_id` | (string) ID of the data quality run. All data quality summary records generated within the same data quality execution instance share the same `invocation_id`.  
`progress_watermark` | (boolean) Determines whether this particular record is considered by the data quality check to determine the high watermark for incremental validation. If `FALSE`, the respective record is ignored when establishing the high-watermark value. This information is useful when executing test data quality validations that should not advance the high watermark. Knowledge Catalog populates this field with `TRUE` by default, but the value can be overridden if the `--progress_watermark` argument has a value of `FALSE`.   
`rows_validated` | (integer) Total number of records validated after applying `row_filters` and any high-watermark filters on the `incremental_time_filter_column_id` column, if specified.  
`complex_rule_validation_errors_count` | (float) Number of rows returned by a `CUSTOM_SQL_STATEMENT` rule.  
`complex_rule_validation_success_flag` | (boolean) Success status of `CUSTOM_SQL_STATEMENT` rules.   
`success_count` | (integer) Total number of records that passed validation. This field is set to `NULL` for `CUSTOM_SQL_STATEMENT` rules.   
`success_percentage` | (float) Percentage of the number of records that passed validation within the total number of records validated. This field is set to `NULL` for `CUSTOM_SQL_STATEMENT` rules.  
`failed_count` | (integer) Total number of records that failed validation. This field is set to `NULL` for `CUSTOM_SQL_STATEMENT` rules.   
`failed_percentage` | (float) Percentage of the number of records that failed validation within the total number of records validated. This field is set to `NULL` for `CUSTOM_SQL_STATEMENT` rules.  
`null_count` | (integer) Total number of records that returned null during validation. This field is set to `NULL` for `NOT_NULL` and `CUSTOM_SQL_STATEMENT` rules.  
`null_percentage` | (float) Percentage of the number of records that returned null during validation within the total number of records validated. This field is set to `NULL` for `NOT_NULL` and `CUSTOM_SQL_STATEMENT` rules.  
`failed_records_query` | For every rule that fails, this column stores a query that you can use to get failed records. In this document, see Troubleshoot failed rules with `failed_records_query`.  
  
For BigQuery entities, a view is created for every `rule_binding` containing the SQL validation logic of the latest execution. You can find these views in the BigQuery dataset specified in the argument `--gcp-bq-dataset-id`.

## Cost optimizations

Data quality tasks are executed as BigQuery jobs in your project. To control the cost for running data quality jobs, use BigQuery pricing on the project where your BigQuery jobs run. For more information, see [BigQuery workload management](https://docs.cloud.google.com/bigquery/docs/reservations-intro). 

### Incremental validations

Often, you have tables that are updated routinely with new partitions (new rows). If you don't want to revalidate old partitions in every run, you can use incremental validations.

For incremental validations, you must have a `TIMESTAMP` or `DATETIME` type column in your table where the column value monotonically increases. You can use the columns that your BigQuery table is partitioned on.

To specify incremental validation, specify a value for `incremental_time_filter_column_id=TIMESTAMP/DATETIME type column` as part of a rule binding.

When you specify a column, the data quality task considers only rows with a `TIMESTAMP` value greater than the timestamp of the last data quality task that ran.

## Example specification files

To use these samples, [create a BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets) named `sales`. Then, create a fact table named `sales_orders` and add sample data by [running a query](https://cloud.google.com/bigquery/docs/running-queries#queries) with the following GoogleSQL statements:
    
    
    CREATE OR REPLACE TABLE sales.sales_orders
    (
     id STRING NOT NULL,
     last_modified_timestamp TIMESTAMP,
     customer_id STRING,
     item_id STRING,
     amount NUMERIC,
     transaction_currency STRING
    );
    
    INSERT INTO sales.sales_orders
    (id, last_modified_timestamp, customer_id, item_id, amount, transaction_currency)
    VALUES
    ("order1",CURRENT_TIMESTAMP(),"customer1","ASDWQ123456789012345",100,"USD"),
    ("order1",CURRENT_TIMESTAMP(),"customer2","bad_item_id",-10,"XXX"),
    ("order2",CURRENT_TIMESTAMP(),"customer3","INTNL987654321098765",50,"GBP"),
    ("order3",CURRENT_TIMESTAMP(),"customer4","INTNL932716428593847",50,"GBP")
    

### Sample 1

The following code sample creates data quality checks for validating these values:

  * `amount`: values are zero or positive numbers.
  * `item_id`: an alphanumeric string of 5 alphabetical characters, followed by 15 digits.
  * `transaction_currency`: an allowed currency type, as defined by a static list. The static list of this sample allows GBP and JPY as currency types. This validation only applies to rows marked as international.


    
    
    # The following `NONE` row filter is required.
    row_filters:
     NONE:
       filter_sql_expr: |-
          True
     # This filters for rows marked as international (INTNL).
     INTERNATIONAL_ITEMS:
       filter_sql_expr: |-
          REGEXP_CONTAINS(item_id, 'INTNL')
    
    # Rule dimensions are optional but let you aggregate reporting.
    rule_dimensions:
      - consistency
      - correctness
      - duplication
      - completeness
      - conformance
      - integrity
    
    # Rules can apply to multiple tables or columns.
    rules:
     VALUE_ZERO_OR_POSITIVE:
       rule_type: CUSTOM_SQL_EXPR
       dimension: correctness
       params:
         custom_sql_expr: |-
           $column >= 0
    
     VALID_ITEM_ID:
       rule_type: REGEX
       dimension: conformance
       params:
         pattern: |-
           [A-Z]{5}[0-9]{15}
    
     VALID_CURRENCY_ID:
       rule_type: CUSTOM_SQL_EXPR
       dimension: integrity
       params:
         custom_sql_expr: |-
          $column in ('GBP', 'JPY')
    
    # Rule bindings associate rules to columns within tables.
    rule_bindings:
      TRANSACTION_AMOUNT_VALID:
       entity_uri: bigquery://projects/PROJECT_ID/datasets/DATASET_ID/tables/sales_orders
       column_id: amount
       row_filter_id: NONE
       rule_ids:
         - VALUE_ZERO_OR_POSITIVE
    
      TRANSACTION_VALID_ITEM_ID:
       entity_uri: bigquery://projects/PROJECT_ID/datasets/DATASET_ID/tables/sales_orders
       column_id: item_id
       row_filter_id: NONE
       rule_ids:
         - VALID_ITEM_ID
    
      TRANSACTION_CURRENCY_VALID:
       entity_uri: bigquery://projects/PROJECT_ID/datasets/DATASET_ID/tables/sales_orders
       column_id: transaction_currency
       row_filter_id: INTERNATIONAL_ITEMS
       rule_ids:
         - VALID_CURRENCY_ID
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `DATASET_ID`: the dataset ID.



### Sample 2

If the table to be checked is part of a Knowledge Catalog lake, you can specify the tables using lake or zone notation. This lets you aggregate your results by lake or zone. For example, you can generate a zone level score.

To use this sample, create a Knowledge Catalog lake with the lake ID `operations` and the zone ID `procurement`. Then, add the table `sales_orders` as an [asset](https://docs.cloud.google.com/knowledge-catalog/docs/manage-assets) to the zone.
    
    
    # This is a convenience section that allows you to shorten the entity_uri
    metadata_registry_defaults:
     dataplex:
       projects: PROJECT_ID
       locations: REGION_ID
       lakes: operations
       zones: procurement
    
    # You have to define a NONE row filter
    row_filters:
     NONE:
       filter_sql_expr: |-
          True
     INTERNATIONAL_ITEMS:
       filter_sql_expr: |-
          REGEXP_CONTAINS(item_id, 'INTNL')
    
    # rule dimensions are optional but allow you to aggregate reporting.
    rule_dimensions:
      - consistency
      - correctness
      - duplication
      - completeness
      - conformance
      - integrity
    
    # Rules can be shared across tables or columns.
    rules:
     VALUE_ZERO_OR_POSITIVE:
       rule_type: CUSTOM_SQL_EXPR
       dimension: correctness
       params:
         custom_sql_expr: |-
           $column >= 0
    
     VALID_ITEM_ID:
       rule_type: REGEX
       dimension: conformance
       params:
         pattern: |-
           [A-Z]{5}[0-9]{15}
    
     VALID_CURRENCY_ID:
       rule_type: CUSTOM_SQL_EXPR
       dimension: integrity
       params:
         custom_sql_expr: |-
          $column in ('GBP', 'JPY')
    
    #rule bindings associate rules to {table, column}
    rule_bindings:
     TRANSACTION_AMOUNT_VALID:
       entity_uri: dataplex://projects/PROJECT_ID/locations/REGION_ID/lakes/operations/zones/procurement/entities/sales_orders
       column_id: amount
       row_filter_id: NONE
       rule_ids:
         - VALUE_ZERO_OR_POSITIVE
    
     TRANSACTION_VALID_ITEM_ID:
       entity_uri: dataplex://zones/procurement/entities/sales_orders # omitting projects/locations/lakes from uri path to use the default values specified in metadata_registry_defaults
       column_id: item_id
       row_filter_id: NONE
       rule_ids:
         - VALID_ITEM_ID
    
     TRANSACTION_CURRENCY_VALID:
       entity_uri: dataplex://zones/procurement/entities/sales_orders
       column_id: transaction_currency
       row_filter_id: INTERNATIONAL_ITEMS
       rule_ids:
         - VALID_CURRENCY_ID
    

Replace the following:

  * PROJECT_ID: your project ID.
  * REGION_ID: the region ID of the Knowledge Catalog lake in which the table exists, such as `us-central1`.



### Sample 3

This example enhances Sample 2 by adding a custom SQL check to see if the ID values are unique.
    
    
    # This is a convenience section that allows you to shorten the entity_uri
    metadata_registry_defaults:
     dataplex:
       projects: PROJECT_ID
       locations: REGION_ID
       lakes: operations
       zones: procurement
    
    # You have to define a NONE row filter
    row_filters:
     NONE:
       filter_sql_expr: |-
          True
     INTERNATIONAL_ITEMS:
       filter_sql_expr: |-
          REGEXP_CONTAINS(item_id, 'INTNL')
    
    # rule dimensions are optional but allow you to aggregate reporting.
    rule_dimensions:
      - consistency
      - correctness
      - duplication
      - completeness
      - conformance
      - integrity
    
    # Rules can be shared across tables or columns.
    rules:
    # This rule is parameterized with column_names as parameter
     NO_DUPLICATES_IN_COLUMN_GROUPS:
       rule_type: CUSTOM_SQL_STATEMENT
       dimension: duplication
       params:
         custom_sql_arguments:
           - column_names
         custom_sql_statement: |-
           select a.*
           from data a
           inner join (
             select
               $column_names
             from data
             group by $column_names
             having count(*) > 1
           ) duplicates
           using ($column_names)
    
     VALUE_ZERO_OR_POSITIVE:
       rule_type: CUSTOM_SQL_EXPR
       dimension: correctness
       params:
         custom_sql_expr: |-
           $column >= 0
    
     VALID_ITEM_ID:
       rule_type: REGEX
       dimension: conformance
       params:
         pattern: |-
           [A-Z]{5}[0-9]{15}
    
     VALID_CURRENCY_ID:
       rule_type: CUSTOM_SQL_EXPR
       dimension: integrity
       params:
         custom_sql_expr: |-
          $column in ('GBP', 'JPY')
    
    #rule bindings associate rules to {table, column}
    
    rule_bindings:
     TRANSACTIONS_UNIQUE:
       entity_uri: dataplex://projects/PROJECT_ID/locations/REGION_ID/lakes/operations/zones/procurement/entities/sales_orders
       column_id: id
       row_filter_id: NONE
       rule_ids:
         - NO_DUPLICATES_IN_COLUMN_GROUPS:
             column_names: "id"
    
     TRANSACTION_AMOUNT_VALID:
       entity_uri: dataplex://zones/procurement/entities/sales_orders # omitting projects/locations/lakes from uri path to use the default values specified in metadata_registry_defaults
       column_id: amount
       row_filter_id: NONE
       rule_ids:
         - VALUE_ZERO_OR_POSITIVE
    
     TRANSACTION_VALID_ITEM_ID:
       entity_uri: dataplex://zones/procurement/entities/sales_orders
       column_id: item_id
       row_filter_id: NONE
       rule_ids:
         - VALID_ITEM_ID
    
     TRANSACTION_CURRENCY_VALID:
       entity_uri: dataplex://zones/procurement/entities/sales_orders
       column_id: transaction_currency
       row_filter_id: INTERNATIONAL_ITEMS
       rule_ids:
         - VALID_CURRENCY_ID
    

### Sample 4

This example enhances Sample 3 by adding incremental validations using the `last_modified_timestamp` column. You can add incremental validations for one or more rule bindings.
    
    
    # This is a convenience section that allows you to shorten the entity_uri
    metadata_registry_defaults:
     dataplex:
       projects: PROJECT_ID
       locations: REGION_ID
       lakes: operations
       zones: procurement
    
    # You have to define a NONE row filter
    row_filters:
     NONE:
       filter_sql_expr: |-
          True
     INTERNATIONAL_ITEMS:
       filter_sql_expr: |-
          REGEXP_CONTAINS(item_id, 'INTNL')
    
    # rule dimensions are optional but allow you to aggregate reporting.
    rule_dimensions:
      - consistency
      - correctness
      - duplication
      - completeness
      - conformance
      - integrity
    
    # Rules can be shared across tables or columns.
    rules:
    # This rule is parameterized with column_names as parameter
     NO_DUPLICATES_IN_COLUMN_GROUPS:
       rule_type: CUSTOM_SQL_STATEMENT
       dimension: duplication
       params:
         custom_sql_arguments:
           - column_names
         custom_sql_statement: |-
           select a.*
           from data a
           inner join (
             select
               $column_names
             from data
             group by $column_names
             having count(*) > 1
           ) duplicates
           using ($column_names)
    
     VALUE_ZERO_OR_POSITIVE:
       rule_type: CUSTOM_SQL_EXPR
       dimension: correctness
       params:
         custom_sql_expr: |-
           $column >= 0
    
     VALID_ITEM_ID:
       rule_type: REGEX
       dimension: conformance
       params:
         pattern: |-
           [A-Z]{5}[0-9]{15}
    
     VALID_CURRENCY_ID:
       rule_type: CUSTOM_SQL_EXPR
       dimension: integrity
       params:
         custom_sql_expr: |-
          $column in ('GBP', 'JPY')
    
    #rule bindings associate rules to {table, column}
    
    rule_bindings:
     TRANSACTIONS_UNIQUE:
       entity_uri: dataplex://projects/PROJECT_ID/locations/REGION_ID/lakes/operations/zones/procurement/entities/sales_orders
       column_id: id
       row_filter_id: NONE
       incremental_time_filter_column_id: last_modified_timestamp
       rule_ids:
         - NO_DUPLICATES_IN_COLUMN_GROUPS:
             column_names: "id"
    
     TRANSACTION_AMOUNT_VALID:
       entity_uri: dataplex://zones/procurement/entities/sales_orders # omitting projects/locations/lakes from uri path to use the default values specified in metadata_registry_defaults
       column_id: amount
       row_filter_id: NONE
       incremental_time_filter_column_id: last_modified_timestamp
       rule_ids:
         - VALUE_ZERO_OR_POSITIVE
    
     TRANSACTION_VALID_ITEM_ID:
       entity_uri: dataplex://zones/procurement/entities/sales_orders
       column_id: item_id
       row_filter_id: NONE
       incremental_time_filter_column_id: last_modified_timestamp
       rule_ids:
         - VALID_ITEM_ID
    
     TRANSACTION_CURRENCY_VALID:
       entity_uri: dataplex://zones/procurement/entities/sales_orders
       column_id: transaction_currency
       row_filter_id: INTERNATIONAL_ITEMS
       incremental_time_filter_column_id: last_modified_timestamp
       rule_ids:
         - VALID_CURRENCY_ID
    

## Troubleshoot failed rules with `failed_records_query`

For every rule that fails, the summary table stores a query in the `failed_records_query` column that you can use to get failed records.

To debug, you can also use `reference columns` in your YAML file, which lets you join the output of `failed_records_query` with the original data to get the entire record. For example, you can specify a `primary_key` column or a compound `primary_key` column as a reference column.

**Note:** Failed record queries do not use `reference_columns` for `CUSTOM_SQL_STATEMENT` rules. The output of the failed records query depends on the query in `CUSTOM_SQL_STATEMENT` itself. For example, if you need a reference column in the failed records query for a `CUSTOM_SQL_STATEMENT` rule, you need to include the column in the SQL statement as well. See Use failed records queries for CUSTOM_SQL_STATEMENT rules for more information. 

### Specify reference columns

To generate reference columns, you can add the following to your YAML specification:

  1. The `reference_columns` section. In this section, you can create one or more reference column sets, with each set specifying one or more columns.

  2. The `rule_bindings` section. In this section, you can add a line to a rule binding that specifies a reference column ID (`reference_columns_id`) to use for the rules in that rule binding. It should be one of the reference column sets specified in the `reference_columns` section.




For example, the following YAML file specifies a `reference_columns` section and defines three columns: `id`, `last_modified_timestamp`, and `item_id` as part of the `ORDER_DETAILS_REFERENCE_COLUMNS` set. The following example uses the sample table `sales_orders`.
    
    
    reference_columns:
      ORDER_DETAILS_REFERENCE_COLUMNS:
        include_reference_columns:
          - id
          - last_modified_timestamp
          - item_id
    rules:
      VALUE_ZERO_OR_POSITIVE:
      rule_type: CUSTOM_SQL_EXPR
      params:
        custom_sql_expr: |-
    
    row_filters:
    NONE:
      filter_sql_expr: |-
          True
    
    rule_bindings:
    TRANSACTION_AMOUNT_VALID:
      entity_uri: bigquery://projects/PROJECT_ID/datasets/DATASET_ID/tables/sales_orders
      column_id: amount
      row_filter_id: NONE
      reference_columns_id: ORDER_DETAILS_REFERENCE_COLUMNS
      rule_ids:
        - VALUE_ZERO_OR_POSITIVE

### Using the failed records query

The failed records query generates a row for every record that has a rule that failed. It includes the column name that triggered the failure, the value that triggered the failure, and the values for the reference columns. It also includes metadata that you can use to relate to the execution of the data quality task.

The following is an example of the output from a failed records query for the YAML file described in Specify reference columns. It shows a failure for column `amount` and a failed value of `-10`. It also records the corresponding value for the reference column.

_dq_validation_invocation_id | _dq_validation_rule_binding_id | _dq_validation_rule_id | _dq_validation_column_id | _dq_validation_column_value | _dq_validation_dimension | _dq_validation_simple_rule_row_is_valid | _dq_validation_complex_rule_validation_errors_count | _dq_validation_complex_rule_validation_success_flag | id | last_modified_timestamp | item_id  
---|---|---|---|---|---|---|---|---|---|---|---  
10a25be9-8dfa-446c-a42c-75f6bb4a49d9 | TRANSACTION_AMOUNT_VALID | VALUE_ZERO_OR_POSITIVE | amount | -10 |  | FALSE |  |  | order1 | 2022-01-22T02:30:06.321Z | bad_item_id  
  
####  Use failed records queries for CUSTOM_SQL_STATEMENT rules

For `CUSTOM_SQL_STATEMENT` rules, failed record queries include the `custom_sql_statement_validation_errors` column. The `custom_sql_statement_validation_errors` column is a nested column with fields that match the output of your SQL statement. Reference columns are not included in failed records queries for `CUSTOM_SQL_STATEMENT` rules. 

For example, your `CUSTOM_SQL_STATEMENT` rule might look like this: 
    
    
    rules:
      TEST_RULE:
        rule_type: CUSTOM_SQL_STATEMENT
        custom_sql_arguments:
          - existing_id
          - replacement_id
        params:
         CUSTOM_SQL_STATEMENT: |-
           (SELECT product_name, product_key FROM data
           where $existing_id != $replacement_id)

The results for this example will contain one or more rows for the `custom_sql_statement_validation_errors` column, with a row for every occurrence where `existing_id!=replacement_id`. 

When rendered in JSON, the contents of a cell in this column might look like this: 
    
    
    {
      "custom_sql_statement_valdation_errors" :{
        "product_name"="abc"
        "product_key"="12345678"
        "_rule_binding_id"="your_rule_binding"
      }
    }
    

You can join these results to the original table with a nested reference like `join on custom_sql_statement_valdation_errors.product_key`. 

## What's next

  * Refer to the [CloudDQ YAML specification reference](https://github.com/GoogleCloudPlatform/cloud-data-quality/blob/main/REFERENCE.md).
  * For sample data quality rules, see [Simple rules](https://github.com/GoogleCloudPlatform/cloud-data-quality/blob/main/USERMANUAL.md#example-use-cases) and [Advanced rules](https://github.com/GoogleCloudPlatform/cloud-data-quality/blob/main/docs/examples/advanced_rules/USERMANUAL.md).
  * See [Sample Airflow DAG for Knowledge Catalog data quality task](https://github.com/GoogleCloudPlatform/cloud-data-quality/blob/main/scripts/dataproc-workflow-composer/clouddq_composer_dataplex_task_job.py).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
