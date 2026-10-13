---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta
title: Package com.google.cloud.biglake.hive.v1beta (0.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:34:23.622799+00:00
---

# Package com.google.cloud.biglake.hive.v1beta (0.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.biglake.hive.v1beta (0.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.87.0 (latest)  0.83.0  0.82.0  0.81.1  0.79.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.58.0  0.56.0  0.55.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-biglake/google-cloud-biglake/src/main/java/com/google/cloud/biglake/hive/v1beta)  
---  
  
## This package is not the recommended entry point to using this client library!

For this library, we recommend using [com.google.cloud.biglake.v1](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.v1) for new applications.

## Prerelease Implications

This package is a prerelease version! Use with caution.

Prerelease versions are considered unstable as they may be shut down and/or subject to breaking changes when upgrading. Use them only for testing or if you specifically need their experimental features.

## Client Classes

Client classes are the main entry point to using a package. They contain several variations of Java methods for each of the API's methods. 

Client |  Description  
---|---  
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient) |  Service Description: Hive Metastore Service is a biglake service that allows users to manage their external Hive catalogs. Full API compatibility with OSS Hive Metastore APIs is not supported. The methods match the Hive Metastore API spec mostly except for a few exceptions. These include listing resources with pattern, environment context which are combined in a single  
  
## Settings Classes

Settings classes can be used to configure credentials, endpoints, and retry settings for a Client. 

Settings |  Description  
---|---  
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceSettings](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceSettings) |  Settings class to configure an instance of HiveMetastoreServiceClient. The default instance has everything set to sensible defaults:   
  
## Classes

Class |  Description  
---|---  
[com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest) |  Request message for the BatchCreatePartitions method.   
[com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequest.Builder) |  Request message for the BatchCreatePartitions method.   
[com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse) |  Response message for BatchCreatePartitions.   
[com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponse.Builder) |  Response message for BatchCreatePartitions.   
[com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest) |  Request message for BatchDeletePartitions. The Partition is uniquely identified by values, which is an ordered list. Hence, there is no separate name or partition id field.  
[com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequest.Builder) |  Request message for BatchDeletePartitions. The Partition is uniquely identified by values, which is an ordered list. Hence, there is no separate name or partition id field.  
[com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest) |  Request message for BatchUpdatePartitions.   
[com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequest.Builder) |  Request message for BatchUpdatePartitions.   
[com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse) |  Response message for BatchUpdatePartitions.   
[com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponse.Builder) |  Response message for BatchUpdatePartitions.   
[com.google.cloud.biglake.hive.v1beta.CatalogName](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CatalogName) |   
[com.google.cloud.biglake.hive.v1beta.CatalogName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CatalogName.Builder) |  Builder for projects/{project}/catalogs/{catalog}.  
[com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest) |  Request message for the CreateHiveCatalog method.   
[com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequest.Builder) |  Request message for the CreateHiveCatalog method.   
[com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest) |  Request message for the CreateHiveDatabase method.   
[com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequest.Builder) |  Request message for the CreateHiveDatabase method.   
[com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest) |  Request message for the CreateHiveTable method.   
[com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequest.Builder) |  Request message for the CreateHiveTable method.   
[com.google.cloud.biglake.hive.v1beta.CreatePartitionRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreatePartitionRequest) |  Request message for CreatePartition. The Partition is uniquely identified by values, which is an ordered list. Hence, there is no separate name or partition id field.  
[com.google.cloud.biglake.hive.v1beta.CreatePartitionRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreatePartitionRequest.Builder) |  Request message for CreatePartition. The Partition is uniquely identified by values, which is an ordered list. Hence, there is no separate name or partition id field.  
[com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest) |  Request message for the DeleteHiveCatalog method.   
[com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequest.Builder) |  Request message for the DeleteHiveCatalog method.   
[com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest) |  Request message for the DeleteHiveDatabase method.   
[com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequest.Builder) |  Request message for the DeleteHiveDatabase method.   
[com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest) |  Request message for the DeleteHiveTable method.   
[com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequest.Builder) |  Request message for the DeleteHiveTable method.   
[com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest) |  Request message for FailoverHiveCatalog.   
[com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequest.Builder) |  Request message for FailoverHiveCatalog.   
[com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse) |  Response message for FailoverHiveCatalog.   
[com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponse.Builder) |  Response message for FailoverHiveCatalog.   
[com.google.cloud.biglake.hive.v1beta.FieldSchema](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchema) |  Field schema information.   
[com.google.cloud.biglake.hive.v1beta.FieldSchema.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchema.Builder) |  Field schema information.   
[com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest) |  Request message for the GetHiveCatalog method.   
[com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequest.Builder) |  Request message for the GetHiveCatalog method.   
[com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest) |  Request message for the GetHiveDatabase method.   
[com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequest.Builder) |  Request message for the GetHiveDatabase method.   
[com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest) |  Request message for the GetHiveTable method.   
[com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveTableRequest.Builder) |  Request message for the GetHiveTable method.   
[com.google.cloud.biglake.hive.v1beta.HiveCatalog](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog) |  The HiveCatalog contains spark/hive databases and tables in the BigLake Metastore. While creating resources under a catalog, ideally ensure that the storage bucket location, spark / hive engine location or any other compute  
[com.google.cloud.biglake.hive.v1beta.HiveCatalog.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog.Builder) |  The HiveCatalog contains spark/hive databases and tables in the BigLake Metastore. While creating resources under a catalog, ideally ensure that the storage bucket location, spark / hive engine location or any other compute  
[com.google.cloud.biglake.hive.v1beta.HiveCatalog.Replica](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog.Replica) |  The replica of the Catalog.   
[com.google.cloud.biglake.hive.v1beta.HiveCatalog.Replica.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog.Replica.Builder) |  The replica of the Catalog.   
[com.google.cloud.biglake.hive.v1beta.HiveDatabase](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase) |  Stores the hive database information. It includes the database name, description, location and properties associated with the database.   
[com.google.cloud.biglake.hive.v1beta.HiveDatabase.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabase.Builder) |  Stores the hive database information. It includes the database name, description, location and properties associated with the database.   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreProto](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreProto) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsFixedSizeCollection) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsPage](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsPage) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveCatalogsPagedResponse) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesFixedSizeCollection) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesPage](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesPage) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveDatabasesPagedResponse) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesFixedSizeCollection](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesFixedSizeCollection) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesPage](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesPage) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesPagedResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceClient.ListHiveTablesPagedResponse) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc) |  Hive Metastore Service is a biglake service that allows users to manage their external Hive catalogs. Full API compatibility with OSS Hive Metastore APIs is not supported. The methods match the Hive Metastore API spec mostly  
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceImplBase](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.HiveMetastoreServiceImplBase) |  Base class for the server implementation of the service HiveMetastoreService. Hive Metastore Service is a biglake service that allows users to manage  
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceSettings.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceSettings.Builder) |  Builder for HiveMetastoreServiceSettings.  
[com.google.cloud.biglake.hive.v1beta.HiveTable](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable) |  Stores the hive table information. It includes the table name, schema (column names and types), data location, storage format, serde info, etc. This message closely matches the Table object in the IMetastoreClient  
[com.google.cloud.biglake.hive.v1beta.HiveTable.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTable.Builder) |  Stores the hive table information. It includes the table name, schema (column names and types), data location, storage format, serde info, etc. This message closely matches the Table object in the IMetastoreClient  
[com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest) |  Request message for the ListHiveCatalogs method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequest.Builder) |  Request message for the ListHiveCatalogs method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponse) |  Response message for the ListHiveCatalogs method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponse.Builder) |  Response message for the ListHiveCatalogs method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest) |  Request message for the ListHiveDatabases method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequest.Builder) |  Request message for the ListHiveDatabases method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponse) |  Response message for the ListHiveDatabases method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponse.Builder) |  Response message for the ListHiveDatabases method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest) |  Request message for the ListHiveTables method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequest.Builder) |  Request message for the ListHiveTables method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponse) |  Response message for the ListHiveTables method.   
[com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponse.Builder) |  Response message for the ListHiveTables method.   
[com.google.cloud.biglake.hive.v1beta.ListPartitionsRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsRequest) |  Request message for ListPartitions.   
[com.google.cloud.biglake.hive.v1beta.ListPartitionsRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsRequest.Builder) |  Request message for ListPartitions.   
[com.google.cloud.biglake.hive.v1beta.ListPartitionsResponse](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsResponse) |  Response message for ListPartitions.   
[com.google.cloud.biglake.hive.v1beta.ListPartitionsResponse.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsResponse.Builder) |  Response message for ListPartitions.   
[com.google.cloud.biglake.hive.v1beta.NamespaceName](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.NamespaceName) |   
[com.google.cloud.biglake.hive.v1beta.NamespaceName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.NamespaceName.Builder) |  Builder for projects/{project}/catalogs/{catalog}/databases/{database}.  
[com.google.cloud.biglake.hive.v1beta.Partition](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.Partition) |  Information about a Hive partition.   
[com.google.cloud.biglake.hive.v1beta.Partition.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.Partition.Builder) |  Information about a Hive partition.   
[com.google.cloud.biglake.hive.v1beta.PartitionValues](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.PartitionValues) |  Represents the values of a partition.   
[com.google.cloud.biglake.hive.v1beta.PartitionValues.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.PartitionValues.Builder) |  Represents the values of a partition.   
[com.google.cloud.biglake.hive.v1beta.ProjectName](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ProjectName) |   
[com.google.cloud.biglake.hive.v1beta.ProjectName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ProjectName.Builder) |  Builder for projects/{project}.  
[com.google.cloud.biglake.hive.v1beta.SerdeInfo](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.SerdeInfo) |  Serialization and deserialization information.   
[com.google.cloud.biglake.hive.v1beta.SerdeInfo.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.SerdeInfo.Builder) |  Serialization and deserialization information.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor) |  Contains information about the physical storage of the table data.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.Builder) |  Contains information about the physical storage of the table data.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.Order](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.Order) |  Sort order of the stored data per column.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.Order.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.Order.Builder) |  Sort order of the stored data per column.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo) |  Stores all the information about skewed table.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.Builder) |  Stores all the information about skewed table.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedColumnValue](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedColumnValue) |  The skewed column values.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedColumnValue.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedColumnValue.Builder) |  The skewed column values.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedKeyValuesLocation](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedKeyValuesLocation) |  The skewed key values and their corresponding location.   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedKeyValuesLocation.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedKeyValuesLocation.Builder) |  The skewed key values and their corresponding location.   
[com.google.cloud.biglake.hive.v1beta.TableName](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.TableName) |   
[com.google.cloud.biglake.hive.v1beta.TableName.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.TableName.Builder) |  Builder for projects/{project}/catalogs/{catalog}/databases/{database}/tables/{table}.  
[com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest) |  Request message for the UpdateHiveCatalog method.   
[com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequest.Builder) |  Request message for the UpdateHiveCatalog method.   
[com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest) |  Request message for the UpdateHiveDatabase method.   
[com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequest.Builder) |  Request message for the UpdateHiveDatabase method.   
[com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest) |  Request message for the UpdateHiveTable method.   
[com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequest.Builder) |  Request message for the UpdateHiveTable method.   
[com.google.cloud.biglake.hive.v1beta.UpdatePartitionRequest](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdatePartitionRequest) |  Request message for UpdatePartition.   
[com.google.cloud.biglake.hive.v1beta.UpdatePartitionRequest.Builder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdatePartitionRequest.Builder) |  Request message for UpdatePartition.   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchCreatePartitionsResponseOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchDeletePartitionsRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.BatchUpdatePartitionsResponseOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveCatalogRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveDatabaseRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreateHiveTableRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.CreatePartitionRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.CreatePartitionRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveCatalogRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveDatabaseRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.DeleteHiveTableRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FailoverHiveCatalogResponseOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.FieldSchemaOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.FieldSchemaOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveCatalogRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveDatabaseRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.GetHiveTableRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.GetHiveTableRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.HiveCatalog.ReplicaOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog.ReplicaOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.HiveCatalogOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalogOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.HiveDatabaseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveDatabaseOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.AsyncService](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveMetastoreServiceGrpc.AsyncService) |  Hive Metastore Service is a biglake service that allows users to manage their external Hive catalogs. Full API compatibility with OSS Hive Metastore APIs is not supported. The methods match the Hive Metastore API spec mostly  
[com.google.cloud.biglake.hive.v1beta.HiveTableOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveTableOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveCatalogsResponseOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveDatabasesResponseOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListHiveTablesResponseOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.ListPartitionsRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.ListPartitionsResponseOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.ListPartitionsResponseOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.PartitionOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.PartitionOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.PartitionValuesOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.PartitionValuesOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.SerdeInfoOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.SerdeInfoOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.OrderOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.OrderOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedColumnValueOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedColumnValueOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedKeyValuesLocationOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfo.SkewedKeyValuesLocationOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfoOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptor.SkewedInfoOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.StorageDescriptorOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.StorageDescriptorOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveCatalogRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveDatabaseRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdateHiveTableRequestOrBuilder) |   
[com.google.cloud.biglake.hive.v1beta.UpdatePartitionRequestOrBuilder](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.UpdatePartitionRequestOrBuilder) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.cloud.biglake.hive.v1beta.HiveCatalog.Replica.State](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.HiveCatalog.Replica.State) |  If the catalog is replicated to multiple regions, this enum describes the current state of the replica.   
[com.google.cloud.biglake.hive.v1beta.SerdeInfo.SerdeType](https://cloud.google.com/java/docs/reference/google-cloud-biglake/latest/com.google.cloud.biglake.hive.v1beta.SerdeInfo.SerdeType) |  The serde types.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
