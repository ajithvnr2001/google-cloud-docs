---
url: https://docs.cloud.google.com/application-design-center/docs/configure-bigquery/
title: Configure a BigQuery dataset \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:54.481895+00:00
---

# Configure a BigQuery dataset  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a BigQuery dataset Stay organized with collections  Save and categorize content based on your preferences. 

Application Design Center lets you create and configure [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) datasets for enterprise data analytics. The dataset components and parameters are based on the [`terraform-google-bigquery`](https://github.com/terraform-google-modules/terraform-google-bigquery) Terraform module.

## Component connections

The following table includes the components that you can connect to a BigQuery dataset, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can read and write data to the BigQuery dataset.
  * The BigQuery resource metadata is added to the Compute Engine instance template.
  * The `roles/bigquery.dataEditor` role is added to Compute Engine instance template service account.

| [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates)  
[Service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The service account can be used by services, such as Cloud Run, to read and modify data in the BigQuery dataset.
  * The BigQuery `roles/bigquery.dataEditor` role is added to the service account.

| [BigQuery IAM roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can interact with the BigQuery dataset.
  * The BigQuery resource metadata is added to the Cloud Run environment variables.
  * The BigQuery `roles/bigquery.dataEditor` role is added to the Cloud Run service account.

| [What is Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)  
[Pub/Sub](https://docs.cloud.google.com/application-design-center/docs/configure-pubsub) | 

  * The Pub/Sub subscription can write messages to the BigQuery dataset.
  * The BigQuery dataset information is added to the BigQuery subscription fields.

| [BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/bigquery)  
  
## Required configuration parameters

If your template includes a BigQuery component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Dataset ID** | [id](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.id) | [Introduction to datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro)  
**Project ID** | The project where you want to deploy the BigQuery dataset and table. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Subfeature | Parameter name | Description and constraint information | Background information  
---|---|---|---|---  
Tables |  | **Table ID** | [id](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.id) | [Introduction to tables](https://docs.cloud.google.com/bigquery/docs/tables-intro)  
| **Description** | [description](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.description) | [Introduction to tables](https://docs.cloud.google.com/bigquery/docs/tables-intro)  
| **Table Name** | [friendlyName](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.friendly_name) | [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming)  
| **Schema** | [schema](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.schema) | [Specifying a schema](https://docs.cloud.google.com/bigquery/docs/schemas)  
| **Clustering** | [clustering](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.clustering) | [Introduction to clustered tables](https://docs.cloud.google.com/bigquery/docs/clustered-tables#limitations)  
| **Require Partition Filter** | [requirePartitionFilter](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.require_partition_filter) | [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter)  
Time Partitioning | **Expiration MS** | [expirationMs](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#timepartitioning) | [Set the partition expiration](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration)  
**Field** | [field](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#timepartitioning) | [Create a time-unit column-partitioned table](https://docs.cloud.google.com/bigquery/docs/creating-partitioned-tables#create_a_time-unit_column-partitioned_table)  
**Type** | [type](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#timepartitioning) | [Create a time-unit column-partitioned table](https://docs.cloud.google.com/bigquery/docs/creating-partitioned-tables#create_a_time-unit_column-partitioned_table)  
Range Partitioning | **Field** | [field](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#rangepartitioning) | [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter)  
**Range Start** | [range.start](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#rangepartitioning) | [Integer range partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#integer_range)  
**Range End** | [range.end](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#rangepartitioning) | [Integer range partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#integer_range)  
**Range Interval** | [range.interval](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#rangepartitioning) | [Integer range partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#integer_range)  
| **Expiration Time** | [expirationTime](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.expiration_time) | [Update a table's expiration time](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_expiration_time)  
| **Deletion Protection** | Select the checkbox to prevent this table from being deleted by Terraform. If not selected, the component-level Deletion Protection setting is used. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_table.html#deletion_protection-1)  
Labels | **Key** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.labels) | [Add labels to tables and views](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)  
**Value** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.labels) | [Add labels to tables and views](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)  
|  | **Dataset Name** | [friendlyName](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.friendly_name) | [Name datasets](https://docs.cloud.google.com/bigquery/docs/datasets#dataset-naming)  
|  | **Description** | [description](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.description) | [Update dataset description](https://docs.cloud.google.com/bigquery/docs/updating-datasets#update-dataset-description)  
|  | **Region** | [location](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.location) | [BigQuery locations](https://docs.cloud.google.com/bigquery/docs/locations)  
|  | **Delete Contents on Destroy** | Select to delete all tables in the dataset when destroying the resource. If not selected, destroying the resource fails if tables are present. | [delete_contents_on_destroy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset#delete_contents_on_destroy-1)  
|  | **Deletion Protection** | When selected, a terraform apply or terraform destroy that would delete tables will fail. When not selected, tables can be deleted. You can override this setting using the deletion protection setting for each table. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_table.html#deletion_protection-1)  
|  | **Default Table Expiration MS** | [defaultTableExpirationMs](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.default_table_expiration_ms) | [Update default table expiration times](https://docs.cloud.google.com/bigquery/docs/updating-datasets#table-expiration)  
|  | **Default Partition Expiration MS** | [defaultPartitionExpirationMs](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.default_partition_expiration_ms) | [Update default partition expiration times](https://docs.cloud.google.com/bigquery/docs/updating-datasets#partition-expiration)  
|  | **Max Time Travel Hours** | [maxTimeTravelHours](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.max_time_travel_hours) | [Update time travel windows](https://docs.cloud.google.com/bigquery/docs/updating-datasets#update_time_travel_windows)  
|  | **Storage Billing Model** | [StorageBillingModel](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#storagebillingmodel) | [Storage billing models](https://docs.cloud.google.com/bigquery/docs/storage_overview#dataset_storage_billing_models)  
|  | **Encryption Key** | [kmsKeyName](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/EncryptionConfiguration) | [Encryption at rest](https://docs.cloud.google.com/bigquery/docs/encryption-at-rest)  
Dataset Labels |  | **Key** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.labels) | [Add labels to datasets](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_dataset_labels)  
| **Value** | [value](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.value) | [Add labels to datasets](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_dataset_labels)  
Resource Tags |  | **Key** | [resourceTags](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.resource_tags) | [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions)  
| **Value** | [resourceTags](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets#Dataset.FIELDS.resource_tags) | [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions)  
Views |  | **View ID** | [id](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables) | [View naming](https://docs.cloud.google.com/bigquery/docs/views#view_naming)  
| **Description** | [description](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.description) | [Introduction to views](https://docs.cloud.google.com/bigquery/docs/views-intro)  
| **Query** | [query](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#viewdefinition) | [Updating a view's SQL query](https://docs.cloud.google.com/bigquery/docs/managing-views#update-sql)  
| **Use Legacy SQL** | [useLegacySql](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#viewdefinition) | [Migrating to GoogleSQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/migrating-from-legacy-sql)  
Labels | **Key** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.labels) | [Add labels to tables and views](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)  
**Value** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.labels) | [Add labels to tables and views](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)  
Materialized Views |  | **View ID** | [id](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables) | [View naming](https://docs.cloud.google.com/bigquery/docs/views#view_naming)  
| **Description** | [description](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.description) | [Introduction to materialized views](https://docs.cloud.google.com/bigquery/docs/materialized-views-intro)  
| **Query** | [query](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#materializedviewdefinition) | [Materialized view query support](https://docs.cloud.google.com/bigquery/docs/materialized-views-create#supported-mvs)  
| **Enable Refresh** | [enableRefresh](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#materializedviewdefinition) | [Refresh materialized views](https://docs.cloud.google.com/bigquery/docs/materialized-views-manage#refresh)  
| **Refresh Interval MS** | [refreshIntervalMs](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#materializedviewdefinition) | [Set the refresh frequency cap](https://docs.cloud.google.com/bigquery/docs/materialized-views-manage#frequency_cap)  
| **Clustering** | [fields[]](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#clustering) | [Cluster materialized views](https://docs.cloud.google.com/bigquery/docs/materialized-views-create#cluster_materialized_views)  
Time Partitioning | **Expiration MS** | [expirationMs](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#timepartitioning) | [Set the partition expiration](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration)  
**Field** | [field](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#timepartitioning) | [Create a time-unit column-partitioned table](https://docs.cloud.google.com/bigquery/docs/creating-partitioned-tables#create_a_time-unit_column-partitioned_table)  
**Type** | [type](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#timepartitioning) | [Create a time-unit column-partitioned table](https://docs.cloud.google.com/bigquery/docs/creating-partitioned-tables#create_a_time-unit_column-partitioned_table)  
**Require Partition Filter** | [requirePartitionFilter](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#timepartitioning) | [Set partition filter requirements](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter)  
Range Partitioning | **Field** | [field](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#rangepartitioning) | [Partitioned materialized views](https://docs.cloud.google.com/bigquery/docs/materialized-views-create#partitioned_materialized_views)  
**Range Start** | [range.start](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#rangepartitioning) | [Integer range partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#integer_range)  
**Range End** | [range.end](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#rangepartitioning) | [Integer range partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#integer_range)  
**Range Interval** | [range.interval](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#rangepartitioning) | [Integer range partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#integer_range)  
| **Expiration Time** | [expirationTime](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.expiration_time) | [Updating a view's expiration time](https://docs.cloud.google.com/bigquery/docs/managing-views#view-expiration)  
| **Max Staleness** | [maxStaleness](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.max_staleness) | [Use materialized views with max_staleness option](https://docs.cloud.google.com/bigquery/docs/materialized-views-create#max_staleness)  
Labels | **Key** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.labels) | [Add labels to tables and views](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)  
**Value** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.labels) | [Add labels to tables and views](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)  
External Tables |  | **Table ID** | [id](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables) | [Introduction to external tables](https://docs.cloud.google.com/bigquery/docs/external-tables)  
| **Description** | A description of the external table. | [description](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.description)  
| **Autodetect** | [autodetect](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Use the autodetect flag](https://docs.cloud.google.com/bigquery/docs/external-table-definition#use-auto-detect-flag)  
| **Compression** | [compression](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Loading compressed and uncompressed data](https://docs.cloud.google.com/bigquery/docs/batch-loading-data#loading_compressed_and_uncompressed_data)  
| **Ignore Unknown Values** | [ignoreUnknownValues](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Create a table definition file for an external data source](https://docs.cloud.google.com/bigquery/docs/external-table-definition)  
| **Max Bad Records** | [maxBadRecords](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Create a table definition file for an external data source](https://docs.cloud.google.com/bigquery/docs/external-table-definition)  
| **Schema** | [schema](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Create a table definition file for an external data source](https://docs.cloud.google.com/bigquery/docs/external-table-definition)  
| **Source Format** | [sourceFormat](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Create a table definition file for an external data source](https://docs.cloud.google.com/bigquery/docs/external-table-definition)  
| **Source URIs** | [sourceUris](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Create a table definition file for an external data source](https://docs.cloud.google.com/bigquery/docs/external-table-definition)  
CSV Options | **Quote** | [quote](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#csvoptions) | [Loading CSV data from Cloud Storage](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv)  
**Allow Jagged Rows** | [allowJaggedRows](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#csvoptions) | [Loading CSV data from Cloud Storage](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv)  
**Allow Quoted Newlines** | [allowQuotedNewlines](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#csvoptions) | [Loading CSV data from Cloud Storage](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv)  
**Encoding** | [encoding](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Encoding](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#encoding)  
**Field Delimiter** | [FieldDelimiter](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [Field delimiters](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#field_delimiters)  
**Skip Leading Rows** | [skipLeadingRows](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#externaldataconfiguration) | [CSV options](https://docs.cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv#csv-options)  
Google Sheets Options | **Range** | [range](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#googlesheetsoptions) | [Create Google Drive external tables](https://docs.cloud.google.com/bigquery/docs/external-data-drive)  
**Skip Leading Rows** | [skipLeadingRows](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#googlesheetsoptions) | [Create Google Drive external tables](https://docs.cloud.google.com/bigquery/docs/external-data-drive)  
Hive Partitioning Options | **Mode** | [mode](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#hivepartitioningoptions) | [Detection modes](https://docs.cloud.google.com/bigquery/docs/hive-partitioned-queries#detection_modes)  
**Source URI Prefix** | [sourceUriPrefix](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#hivepartitioningoptions) | [Use externally partitioned data](https://docs.cloud.google.com/bigquery/docs/hive-partitioned-queries)  
| **Expiration Time** | [expirationTime](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.expiration_time) | [Update a table's expiration time](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_expiration_time)  
| **Max Staleness** | [maxStaleness](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.max_staleness) | [Manage table staleness](https://docs.cloud.google.com/bigquery/docs/change-data-capture#manage_table_staleness)  
| **Deletion Protection** | Select the checkbox to prevent this table from being deleted by Terraform. If not selected, the component-level Deletion Protection setting is used. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_table.html#deletion_protection-1)  
Labels | **Key** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.labels) | [Add labels to tables and views](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)  
**Value** | [labels](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables#Table.FIELDS.labels) | [Add labels to tables and views](https://docs.cloud.google.com/bigquery/docs/adding-labels#adding_table_and_view_labels)  
Routines |  | **Routine ID** | [routineId](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#routinereference) | [Manage routines](https://docs.cloud.google.com/bigquery/docs/routines)  
| **Routine Type** | [routineType](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#Routine.FIELDS.routine_type) | [RoutineType](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#routinetype)  
| **Language** | [language](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#Routine.FIELDS.language) | [Language](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#language)  
| **Definition Body** | [definitionBody](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#Routine.FIELDS.definition_body) | [View the body of a routine](https://docs.cloud.google.com/bigquery/docs/routines#view_the_body_of_a_routine)  
| **Return Type** | [returnType](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#Routine.FIELDS.return_type) | [StandardSqlDataType](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/StandardSqlDataType)  
| **Description** | A description of the routine. | [description](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#Routine.FIELDS.description)  
Arguments | **Name** | The name of the argument. | [name](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#argument)  
**Data Type** | [dataType](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#argument) | [StandardSqlDataType](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/StandardSqlDataType)  
**Argument Kind** | [argumentKind](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#argument) | [ArgumentKind](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#argumentkind)  
**Mode** | [mode](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#argument) | [Mode](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/routines#mode)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
