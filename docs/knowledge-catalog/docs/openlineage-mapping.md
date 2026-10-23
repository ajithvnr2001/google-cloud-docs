---
url: https://docs.cloud.google.com/knowledge-catalog/docs/openlineage-mapping/
title: OpenLineage mapping \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:01.505931+00:00
---

# OpenLineage mapping  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/openlineage-mapping/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  OpenLineage mapping Stay organized with collections  Save and categorize content based on your preferences. 

The Data Lineage API can ingest lineage information from systems that integrate with [OpenLineage](https://docs.cloud.google.com/knowledge-catalog/docs/open-lineage), an open standard for lineage collection. When you send OpenLineage-formatted events to the Data Lineage API using the [`ProcessOpenLineageRunEvent`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/processOpenLineageRunEvent) method, the Data Lineage API maps attributes from the OpenLineage message to corresponding attributes in the Data Lineage API.

This document provides reference tables for these mappings.

## Attribute mapping

The [`ProcessOpenLineageRunEvent`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations/processOpenLineageRunEvent) REST API method maps OpenLineage attributes to Data Lineage API attributes as follows:

Data Lineage API attributes | OpenLineage attributes  
---|---  
[Process](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes).name | projects/PROJECT_NUMBER/locations/LOCATION/processes/HASH_OF_NAMESPACE_AND_NAME  
[Process](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes).displayName | Job.namespace + ":" + Job.name  
[Process](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes).attributes | Job.facets (see [Stored data](https://docs.cloud.google.com/knowledge-catalog/docs/open-lineage#stored-data))  
[Run](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs).name | projects/PROJECT_NUMBER/locations/LOCATION/processes/HASH_OF_NAMESPACE_AND_NAME/runs/HASH_OF_RUNID  
[Run](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs).displayName | Run.runId  
[Run](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs).attributes | Run.facets (see [Stored data](https://docs.cloud.google.com/knowledge-catalog/docs/open-lineage#stored-data))  
[Run](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs).startTime | eventTime  
[Run](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs).endTime | eventTime  
[Run](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs).state | eventType  
[LineageEvent](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents).name | projects/PROJECT_NUMBER/locations/LOCATION/processes/HASH_OF_NAMESPACE_AND_NAME/runs/HASH_OF_RUNID/lineageEvents/HASH_OF_JOB_RUN_INPUT_OUTPUTS_OF_EVENT (for example, projects/11111111/locations/us/processes/1234/runs/4321/lineageEvents/111-222-333)  
[LineageEvent](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents).EventLinks.source | inputs ([fqn](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names) is namespace and name concatenation)  
[LineageEvent](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents).EventLinks.target | outputs ([fqn](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names) is namespace and name concatenation)  
[LineageEvent](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents).startTime | eventTime  
[LineageEvent](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest/v1/projects.locations.processes.runs.lineageEvents).endTime | eventTime  
requestId | Defined by the method user  
  
Column-level lineage is supported when automatically generated by Managed Service for Apache Spark, provided it uses the `columnLineage` facet within the `outputs` objects. Custom OpenLineage events that include this facet materialize table-level lineage only and don't render column-level lineage in the Google Cloud console. The following is a sample of the facet generated by Managed Service for Apache Spark:
    
    
    "outputs": [ {
      "namespace": "bigquery",
      "name": "project.dataset.outputtable",
      "columnLineage": {
          "_producer": "https://github.com/OpenLineage/OpenLineage/tree/1.39.0/integration/spark",
          "_schemaURL": "https://openlineage.io/spec/facets/1-2-0/ColumnLineageDatasetFacet.json#/$defs/ColumnLineageDatasetFacet",
          "fields": {
            "output_field": { // This is the name of the output field
              "inputFields": [
                {
                  "namespace": "bigquery",
                  "name": "project.dataset.inputtable",
                  "field": "input_field", // This is the name of the input field
                  "transformations": [
                    {
                      "type": "DIRECT",
                      "subtype": "IDENTITY",
                      "description": "",
                      "masking": false
                    }
                  ]
                }
              ]
            }
          },
      }
    }]
    

In this example, you create a column-level lineage link between `input_field` and `output_field`. You must include the transformations field; without it, column-level lineage won't be ingested. For more information about the Open Lineage definition for this facet, see [Column level dataset facet](https://openlineage.io/docs/spec/facets/dataset-facets/column_lineage_facet/).

## FQN mapping

The following table provides examples of [OpenLineage namespace and name](https://openlineage.io/docs/spec/naming/) pairs for various systems, and their equivalent Knowledge Catalog (formerly Dataplex Universal Catalog) fully qualified names (FQN):

System | OpenLineage namespace | OpenLineage name | Knowledge Catalog FQN  
---|---|---|---  
[Athena](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-aws-athena) | `awsathena://athena.{region_name}.amazonaws.com` | 

  * `{catalog}`
  * `{catalog}.{database}`
  * `{catalog}.{database}.{table}`

| 

  * `athena:{catalogId}.{region}`
  * `athena:{catalogId}.{region}.{databaseId}`
  * `athena:{catalogId}.{region}.{databaseId}.{tableId}`

  
[AWS Glue](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-aws-glue) | `arn:aws:glue:{region}:{account id}` | `table/{database name}/{table name}` | `aws_glue:table:{region}.{account id}.{database name}.{table name}`  
[Azure Cosmos DB](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-azure-cosmos-db) | `azurecosmos://{host}/dbs/{database}` | `colls/{table}` | 

  * `cosmos-db:{host}.{database}`
  * `cosmos-db:{host}.{database}.{table}`

  
[Azure Data Explorer](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-azure-data-explorer) | `azurekusto://{host}.kusto.windows.net` | `{database}/{table}` | 

  * `kusto:{host}.{region}.{database}`
  * `kusto:{host}.{region}.{database}.{table}`

  
Azure Synapse | `sqlserver://{host}:{port}` | 

  * `{database}`
  * `{database}.{schema}`
  * `{database}.{schema}.{table}`

| Not supported  
[BigQuery](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-bigquery) | `bigquery` | 

  * `{project id}.{dataset name}`
  * `{project id}.{dataset name}.{table name}`

| 

  * `bigquery:{projectId}.{datasetId}`
  * `bigquery:{projectId}.{datasetId}.{assetId}`

  
[Cassandra](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-cassandra) | `cassandra://{host}:{port}` | 

  * `{keyspace}`
  * `{keyspace}.{table}`

| 

  * `cassandra:{hostWithPort}.{keyspaceId}`
  * `cassandra:{hostWithPort}.{keyspaceId}.{tableId}`

  
[MySQL](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-mysql) | `mysql://{host}:{port}` | 

  * `{database}`
  * `{database}.{table}`

| 

  * `mysql:{hostWithPort}.{databaseId}`
  * `mysql:{hostWithPort}.{databaseId}.{tableId}`

  
CrateDB | `crate://{host}:{port}` | `{database}.{schema}.{table}` | Not supported  
[DB2](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-db2) | `db2://{host}:{port}` | 

  * `{database}`
  * `{database}.{schema}`
  * `{database}.{schema}.{table}`

| 

  * `db2:{dns}.{databaseId}`
  * `db2:{dns}.{databaseId}.{schemaId}`
  * `db2:{dns}.{databaseId}.{schemaId}.{tableId}`

  
Hive | `hive://{host}:{port}` | `{database}.{table}` | Not supported  
MSSQL | `mssql://{host}:{port}` | `{database}.{schema}.{table}` | Not supported  
OceanBase | `oceanbase://{host}:{port}` | `{database}.{table}` | Not supported  
[Oracle](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-oracle) | `oracle://{host}:{port}` | `{serviceName}.{schema}.{table} or {sid}.{schema}.{table}` | 

  * `oracle:{hostWithPort}.{databaseId}`
  * `oracle:{hostWithPort}.{databaseId}.{schemaId}`
  * `oracle:{hostWithPort}.{databaseId}.{schemaId}.{tableId}`

  
[Postgres](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-postgresql) | `postgres://{host}:{port}` | 

  * `{database}`
  * `{database}.{schema}`
  * `{database}.{schema}.{table}`

| 

  * `postgresql:{hostWithPort}.{databaseId}`
  * `postgresql:{hostWithPort}.{databaseId}.{schemaId}`
  * `postgresql:{hostWithPort}.{databaseId}.{schemaId}.{tableId}`

  
Teradata | `teradata://{host}:{port}` | `{database}.{table}` | Not supported  
[Redshift](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-aws-redshift) | `redshift://{cluster_identifier}.{region_name}:{port}` | 

  * `{database}`
  * `{database}.{schema}`
  * `{database}.{schema}.{table}`

| 

  * `redshift:{clusterId}.{region}.{port}.{databaseId}`
  * `redshift:{clusterId}.{region}.{port}.{databaseId}.{schemaId}`
  * `redshift:{clusterId}.{region}.{port}.{databaseId}.{schemaId}.{tableId}`

  
[Snowflake](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-snowflake) | `snowflake://{organization name}-{account name} or snowflake://{account-locator}(.{compliance})(.{cloud_region_id})(.{cloud})` | 

  * `{database}`
  * `{database}.{schema}`
  * `{database}.{schema}.{table}`

| 

  * `snowflake:{accountName}.{databaseId}`
  * `snowflake:{accountName}.{databaseId}.{schemaId}`
  * `snowflake:{accountName}.{databaseId}.{schemaId}.{tableId}`

  
[Spanner](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-spanner) | `spanner://{projectId}:{instanceId}` | `{database}.{schema}.{table}` | Supported in Knowledge Catalog, but not supported in Data lineage  
[Trino](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-trino) | `trino://{host}:{port}` | 

  * `{catalog}`
  * `{catalog}.{schema}`
  * `{catalog}.{schema}.{table}`

| 

  * `trino:{hostWithPort}.{catalogId}`
  * `trino:{hostWithPort}.{catalogId}.{schemaId}`
  * `trino:{hostWithPort}.{catalogId}.{schemaId}.{tableId}`

  
[ABFSS (Azure Data Lake Gen2)](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-azure-blob-storage) | `abfss://{container name}@{service name}.dfs.core.windows.net` | `{path}` | 

  * `abs:{serviceName}.{containerName}`
  * `abs:{serviceName}.{containerName}.{path}`

  
[DBFS (Databricks File System)](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-dbfs) | `dbfs://{workspace name}` | `{path}` | 

  * `dbfs:{workspace}`
  * `dbfs:{workspace}.{path}`

  
[Cloud Storage](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-storage) | `gs://{bucket name}` | `{object key}` | 

  * `gcs:{bucketName}`
  * `gcs:{bucketName}.{virtualPath}`

  
[HDFS](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-hdfs) | `hdfs://{namenode host}:{namenode port}` | `{path}` | 

  * `hdfs:{namenodeHostWithPort}`
  * `hdfs:{namenodeHostWithPort}.{path}`

  
[Kafka](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-kafka) | `kafka://{bootstrap server host}:{port}` | `{topic}` | `kafka:{serverHostWithPort}.{topicId}`  
[Local file system](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-filesystem) | `file` | `{path}` | `filesystem:localhost.{path}`  
[Remote file system](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-filesystem) | `file://{host}` | `{path}` | `filesystem:{hostWithPort}.{path}`  
[S3](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-aws-s3) | `s3://{bucket name}` | `{object key}` | 

  * `s3:{bucketName}`
  * `s3:{bucketName}.{objectKey}`

  
Namespace prefixes `s3a` and `s3n` are also accepted and converted to `s3`  
[WASBS (Azure Blob Storage)](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-azure-blob-storage) | `wasbs://{container name}@{service name}.dfs.core.windows.net` | `{object key}` | 

  * `abs:{serviceName}.{containerName}`
  * `abs:{serviceName}.{containerName}.{objectKey}`

  
[Pub/Sub Topic](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-pubsub) | `pubsub` | `topic:{projectId}:{topicId}` | `pubsub:topic:{projectId}.{topicId}`  
[Pub/Sub Subscription](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-pubsub) | `pubsub` | `subscription:{projectId}:{subscriptionId}` | `pubsub:subscription:{projectId}.{subscriptionId}`  
  
### Additional accepted formats

While OpenLineage doesn't define standard `namespace`/`name` pairs for the following systems, the Data Lineage API accepts lineage events for them when formatted as described in the following table. Resources that are referenced in OpenLineage messages with the namespace `custom` are interpreted as custom fully qualified names.

System | OpenLineage namespace | OpenLineage name | Knowledge Catalog FQN  
---|---|---|---  
[Custom FQN](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#custom) | `custom` | `{some reference}` | `custom:{someReference}`  
[Dataproc Metastore](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names#predefined-dataproc-metastore) | `dataproc_metastore` | 

  * `dataproc_metastore:{projectId}.{location}.{instanceId}`
  * `dataproc_metastore:{projectId}.{location}.{instanceId}.{databaseId}`
  * `dataproc_metastore:{projectId}.{location}.{instanceId}.{databaseId}.{tableId}`

| 

  * `dataproc_metastore:{projectId}.{location}.{instanceId}`
  * `dataproc_metastore:{projectId}.{location}.{instanceId}.{databaseId}`
  * `dataproc_metastore:{projectId}.{location}.{instanceId}.{databaseId}.{tableId}`

  
  
## What's next

  * Learn how to [integrate with OpenLineage](https://docs.cloud.google.com/knowledge-catalog/docs/open-lineage).
  * See the reference for [fully qualified names](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names).
  * Explore the [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/data-lineage/rest).
  * Learn how to [view lineage information](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
