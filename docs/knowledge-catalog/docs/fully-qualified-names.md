---
url: https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names/
title: Fully qualified names \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:38:58.086665+00:00
---

# Fully qualified names  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Fully qualified names Stay organized with collections  Save and categorize content based on your preferences. 

Fully qualified names are globally unique, case-sensitive resource identifiers that you can use with Knowledge Catalog (formerly Dataplex Universal Catalog) to refer to Google Cloud and non-Google Cloud resources.

For example, fully qualified names are used for systems that support the [automatic ingestion](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#supported-sources) of metadata from Google Cloud. If you [catalog your non-Google Cloud resources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources) in Knowledge Catalog, you can provide fully qualified names when you create the custom entries that represent those third-party resources.

Fully qualified names are composed of a prefix followed by segments delimited with dots. The maximum length is 4,000 characters. Surround segments that contain reserved characters, such as colons, dots, and whitespace, with backticks. Use double backticks to specify a backtick within a segment.

## Predefined formats for Google Cloud resources

The following tables list the predefined formats for fully qualified names that are supported for Google Cloud resources.

### BigQuery

Resource | Format  
---|---  
Dataset | `bigquery:{projectId}.{datasetId}`  
Table | `bigquery:{projectId}.{datasetId}.{tableId}`  
View | `bigquery:{projectId}.{datasetId}.{viewId}`  
Model | `bigquery:{projectId}.{datasetId}.{modelId}`  
Sharded table | `bigquery:sharded:{projectId}.{datasetId}.{tablePrefix}`  
Routine | `bigquery:routine:{projectId}.{datasetId}.{routineId}`  
Connection | `bigquery:connection:{projectId}.{location}.{connectionId}`  
  
### BigQuery sharing (formerly Analytics Hub)

Resource | Format  
---|---  
Exchange | `analytics_hub:{projectId}.{location}.{exchangeId}`  
Listing | `analytics_hub:{projectId}.{location}.{exchangeId}.{listingId}`  
  
### Bigtable

Resource | Format  
---|---  
Instance | `bigtable:{projectId}.{instanceId}`  
Table | `bigtable:{projectId}.{instanceId}.{tableId}`  
  
### Cloud SQL for MySQL

Resource | Format  
---|---  
Instance | `cloudsql_mysql:{projectId}.{location}.{instanceId}`  
Schema | `cloudsql_mysql:{projectId}.{location}.{instanceId}.{schemaId}`  
Table | `cloudsql_mysql:{projectId}.{location}.{instanceId}.{schemaId}.{tableId}`  
  
### Cloud SQL for PostgreSQL

Resource | Format  
---|---  
Instance | `cloudsql_postgresql:{projectId}.{location}.{instanceId}`  
Database | `cloudsql_postgresql:{projectId}.{location}.{instanceId}.{databaseId}`  
Schema | `cloudsql_postgresql:{projectId}.{location}.{instanceId}.{databaseId}.{schemaId}`  
Table | `cloudsql_postgresql:{projectId}.{location}.{instanceId}.{databaseId}.{schemaId}.{tableId}`  
  
### Cloud Storage

Resource | Format  
---|---  
Bucket | `gcs:{bucketName}`  
Path | `gcs:{bucketName}.{virtualPath}`  
  
### Knowledge Catalog

Resource | Format  
---|---  
Lake | `dataplex:{projectId}.{location}.{lakeId}`  
Zone | `dataplex:{projectId}.{location}.{lakeId}.{zoneId}`  
Table | `dataplex:{projectId}.{location}.{lakeId}.{zoneId}.{tableId}`  
Fileset | `dataplex:{projectId}.{location}.{lakeId}.{zoneId}.{filesetId}`  
  
### Dataproc Metastore

Resource | Format  
---|---  
Service | `dataproc_metastore:{projectId}.{location}.{instanceId}`  
Database | `dataproc_metastore:{projectId}.{location}.{instanceId}.{databaseId}`  
Table | `dataproc_metastore:{projectId}.{location}.{instanceId}.{databaseId}.{tableId}`  
  
### Looker

Resource | Format  
---|---  
Instance | `looker:{instanceId}`  
Dashboard | `looker:dashboard:{instanceId}.{folderId}.{dashboardId}`  
Explore | `looker:explore:{instanceId}.{folderId}.{exploreId}`  
Look | `looker:look:{instanceId}.{folderId}.{lookId}`  
  
### Pub/Sub

Resource | Format  
---|---  
Topic | `pubsub:topic:{projectId}.{topicId}`  
Subscription | `pubsub:subscription:{projectId}.{subscriptionId}`  
  
### Spanner

Resource | Format  
---|---  
Instance | `spanner:{projectId}.{instanceConfigId}.{instanceId}`  
Database | `spanner:{projectId}.{instanceConfigId}.{instanceId}.{databaseId}`  
Table | `spanner:{projectId}.{instanceConfigId}.{instanceId}.{databaseId}.{tableId}`  
View | `spanner:{projectId}.{instanceConfigId}.{instanceId}.{databaseId}.{viewId}`  
  
### Vertex AI

Resource | Format  
---|---  
Model | `vertex_ai:model:{projectId}.{locationId}.{modelId}.{version}`  
Dataset | `vertex_ai:dataset:{projectId}.{locationId}.{datasetId}`  
FeatureGroup | `vertex_ai:featuregroup:{projectId}.{locationId}.{featureGroupId}`  
FeatureOnlineStore | `vertex_ai:featureonlinestore:{projectId}.{locationId}.{featureOnlineStoreId}`  
FeatureView | `vertex_ai:featureonlinestore:{projectId}.{locationId}.{featureOnlineStoreId}.{FeatureViewId}`  
  
## Predefined formats for non-Google Cloud resources

The following tables list the predefined formats for fully qualified names that are supported for third-party resources.

### Apache Cassandra

Resource | Format  
---|---  
Cluster | `cassandra:{dns}`  
Keyspace | `cassandra:{dns}.{keyspaceId}`  
Table | `cassandra:{dns}.{keyspaceId}.{tableId}`  
  
### Apache Hive

Resource | Format  
---|---  
Instance | `hive_metastore:{dns}`  
Database | `hive_metastore:{dns}.{database}`  
Table | `hive_metastore:{dns}.{database}.{table}`  
  
### Apache Kafka

Resource | Format  
---|---  
Cluster | `kafka:{dns}`  
Topic | `kafka:{dns}.{topicId}`  
  
### AWS Athena

Resource | Format  
---|---  
Catalog | `athena:{catalogId}.{region}`  
Database | `athena:{catalogId}.{region}.{databaseId}`  
Table | `athena:{catalogId}.{region}.{databaseId}.{tableId}`  
  
### AWS Redshift

Resource | Format  
---|---  
Instance | `redshift:{clusterId}.{region}.{port}`  
Database | `redshift:{clusterId}.{region}.{port}.{databaseId}`  
Schema | `redshift:{clusterId}.{region}.{port}.{databaseId}.{schemaId}`  
Table | `redshift:{clusterId}.{region}.{port}.{databaseId}.{schemaId}.{tableId}`  
  
### AWS S3

Resource | Format  
---|---  
Bucket | `s3:{bucket}`  
Path | `s3:{bucket}.{virtualPath}`  
  
### AWS Glue

Resource | Format  
---|---  
Table | `aws_glue:table:{region}.{accountId}.{dbName}.{tableName}`  
  
### Azure Blob Storage

Resource | Format  
---|---  
Account | `abs:{account}`  
Container | `abs:{account}.{container}`  
Path | `abs:{account}.{container}.{virtualPath}`  
  
### Azure Cosmos DB

Resource | Format  
---|---  
Account | `cosmos-db:{accountName}`  
Database | `cosmos-db:{accountName}.{databaseId}`  
Container | `cosmos-db:{accountName}.{databaseId}.{containerId}`  
  
### Azure Data Explorer

Resource | Format  
---|---  
Cluster | `kusto:{clusterName}.{region}`  
Database | `kusto:{clusterName}.{region}.{databaseId}`  
Table | `kusto:{clusterName}.{region}.{databaseId}.{tableId}`  
  
### Databricks

Resource | Format  
---|---  
Metastore | `databricks:{metastoreId}`  
Catalog | `databricks:{metastoreId}.{catalogId}`  
Schema | `databricks:{metastoreId}.{catalogId}.{schemaId}`  
Table | `databricks:table:{metastoreId}.{catalogId}.{schemaId}.{tableId}`  
View | `databricks:view:{metastoreId}.{catalogId}.{schemaId}.{viewId}`  
Routine | `databricks:routine:{metastoreId}.{catalogId}.{schemaId}.{routineId}`  
Volume | `databricks:volume:{metastoreId}.{catalogId}.{schemaId}.{volumeId}`  
Model | `databricks:model:{metastoreId}.{catalogId}.{schemaId}.{modelId}`  
  
### Databricks File System

Resource | Format  
---|---  
Instance | `dbfs:{workspace}`  
Path | `dbfs:{workspace}.{path}`  
  
### Generic File System

Resource | Format  
---|---  
Instance | `filesystem:{dns}`  
Path | `filesystem:{dns}.{path}`  
  
### Hadoop Distributed File System

Resource | Format  
---|---  
Instance | `hdfs:{dns}`  
Path | `hdfs:{dns}.{path}`  
  
### IBM DB2

Resource | Format  
---|---  
Instance | `db2:{dns}`  
Database | `db2:{dns}.{databaseId}`  
Schema | `db2:{dns}.{databaseId}.{schemaId}`  
Table | `db2:{dns}.{databaseId}.{schemaId}.{tableId}`  
  
### IBM Informix

Resource | Format  
---|---  
Instance | `informix:{dns}`  
Database | `informix:{dns}.{databaseId}`  
Schema | `informix:{dns}.{databaseId}.{schemaId}`  
Table | `informix:{dns}.{databaseId}.{schemaId}.{tableId}`  
  
### Microsoft SQL Server

Resource | Format  
---|---  
Instance | `sqlserver:{dns}`  
Database | `sqlserver:{dns}.{databaseId}`  
Schema | `sqlserver:{dns}.{databaseId}.{schemaId}`  
Table | `sqlserver:{dns}.{databaseId}.{schemaId}.{tableId}`  
  
### MySQL

Resource | Format  
---|---  
Instance | `mysql:{dns}`  
Schema | `mysql:{dns}.{schemaId}`  
Table | `mysql:{dns}.{schemaId}.{tableId}`  
  
### Oracle Database

Resource | Format  
---|---  
Instance | `oracle:{dns}`  
Database | `oracle:{dns}.{databaseId}`  
Schema | `oracle:{dns}.{databaseId}.{schemaId}`  
Table | `oracle:{dns}.{databaseId}.{schemaId}.{tableId}`  
  
### PostgreSQL

Resource | Format  
---|---  
Instance | `postgresql:{dns}`  
Database | `postgresql:{dns}.{databaseId}`  
Schema | `postgresql:{dns}.{databaseId}.{schemaId}`  
Table | `postgresql:{dns}.{databaseId}.{schemaId}.{tableId}`  
  
### Salesforce

Resource | Format  
---|---  
SObject | `salesforce:{environment}.{orgId}.{sobject}`  
  
### Snowflake

Resource | Format  
---|---  
Account | `snowflake:{accountName}`  
Database | `snowflake:{accountName}.{databaseId}`  
Schema | `snowflake:{accountName}.{databaseId}.{schemaId}`  
Table | `snowflake:{accountName}.{databaseId}.{schemaId}.{tableId}`  
  
### Tableau

Resource | Format  
---|---  
Server | `tableau:{dns}`  
Site | `tableau:{dns}.{site}`  
Project | `tableau:project:{dns}.{site}.{projectId}`  
Data source | `tableau:datasource:{dns}.{site}.{projectId}.{datasourceId}`  
Workbook | `tableau:workbook:{dns}.{site}.{projectId}.{workbookId}`  
Sheet | `tableau:sheet:{dns}.{site}.{projectId}.{workbookId}.{sheetId}`  
Dashboard | `tableau:dashboard:{dns}.{site}.{projectId}.{workbookId}.{dashboardId}`  
  
### Trino

Resource | Format  
---|---  
Instance | `trino:{dns}`  
Catalog | `trino:{dns}.{catalogId}`  
Schema | `trino:{dns}.{catalogId}.{schemaId}`  
Table | `trino:{dns}.{catalogId}.{schemaId}.{tableId}`  
  
## Custom formats

You can create a custom fully qualified name format by using the `custom:` prefix. Custom formats are not validated, and might not be compatible with Knowledge Catalog features. To ease future migration, create custom formats that are similar to predefined formats.

Resources that are referenced in OpenLineage messages with the namespace `custom` are interpreted as custom fully qualified names.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
