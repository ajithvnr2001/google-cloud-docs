---
url: https://docs.cloud.google.com/dataflow/docs/guides/managed-io-databases/
title: Dataflow managed I/O for databases \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:42.939678+00:00
---

# Dataflow managed I/O for databases  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/managed-io-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow managed I/O for databases Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow supports reading from and writing to databases using Java Database Connectivity (JDBC). Dataflow uses the Apache Beam `JdbcIO` connector to connect to JDBC data sources and sinks. Managed I/O for Databases supports standard JDBC drivers for various databases, including PostgreSQL, MySQL, and Microsoft SQL Server.

## Requirements

The following SDKs support managed I/O for databases:

  * Apache Beam SDK for Java version 2.69.0 or later
  * Apache Beam SDK for Python version 2.69.0 or later



## Configuration

Managed I/O for Databases supports the following configuration parameters:

### `POSTGRES` Read

Configuration | Type | Description  
---|---|---  
**jdbc_url** |  `str` |  Connection URL for the JDBC source.   
connection_properties  |  `str` |  Used to set connection properties passed to the JDBC driver not already defined as standalone parameter (e.g. username and password can be set using parameters above accordingly). Format of the string must be "key1=value1;key2=value2;".   
fetch_size  |  `int32` |  This method is used to override the size of the data that is going to be fetched and loaded in memory per every database call. It should ONLY be used if the default value throws memory errors.   
location  |  `str` |  Name of the table to read from.   
num_partitions  |  `int32` |  The number of partitions   
output_parallelization  |  `boolean` |  Whether to reshuffle the resulting PCollection so results are distributed to all workers.   
partition_column  |  `str` |  Name of a column of numeric type that will be used for partitioning.   
password  |  `str` |  Password for the JDBC source. Can be specified as a plain password, or as a secret specification in JSON format if used with a secret manager.   
read_query  |  `str` |  SQL query used to query the JDBC source.   
secret_manager  |  `str` |  Secret Manager to use for fetching secret values. Available options: 'GoogleCloudSecretManager', 'GoogleCloudHsmGeneratedSecretManager'. If not set, no secret manager is used and the password is treated as a plain password.   
username  |  `str` |  Username for the JDBC source.   
  
### `POSTGRES` Write

Configuration | Type | Description  
---|---|---  
**jdbc_url** |  `str` |  Connection URL for the JDBC sink.   
autosharding  |  `boolean` |  If true, enables using a dynamically determined number of shards to write.   
batch_size  |  `int64` |  n/a   
connection_properties  |  `str` |  Used to set connection properties passed to the JDBC driver not already defined as standalone parameter (e.g. username and password can be set using parameters above accordingly). Format of the string must be "key1=value1;key2=value2;".   
location  |  `str` |  Name of the table to write to.   
password  |  `str` |  Password for the JDBC source. Can be specified as a plain password, or as a secret specification in JSON format if used with a secret manager.   
secret_manager  |  `str` |  Secret Manager to use for fetching secret values. Available options: 'GoogleCloudSecretManager', 'GoogleCloudHsmGeneratedSecretManager'. If not set, no secret manager is used and the password is treated as a plain password.   
username  |  `str` |  Username for the JDBC source.   
write_statement  |  `str` |  SQL query used to insert records into the JDBC sink.   
  
### `MYSQL` Read

Configuration | Type | Description  
---|---|---  
**jdbc_url** |  `str` |  Connection URL for the JDBC source.   
connection_init_sql  |  `list[str]` |  Sets the connection init sql statements used by the Driver. Only MySQL and MariaDB support this.   
connection_properties  |  `str` |  Used to set connection properties passed to the JDBC driver not already defined as standalone parameter (e.g. username and password can be set using parameters above accordingly). Format of the string must be "key1=value1;key2=value2;".   
disable_auto_commit  |  `boolean` |  Whether to disable auto commit on read. Defaults to true if not provided. The need for this config varies depending on the database platform. Informix requires this to be set to false while Postgres requires this to be set to true.   
fetch_size  |  `int32` |  This method is used to override the size of the data that is going to be fetched and loaded in memory per every database call. It should ONLY be used if the default value throws memory errors.   
location  |  `str` |  Name of the table to read from.   
num_partitions  |  `int32` |  The number of partitions   
output_parallelization  |  `boolean` |  Whether to reshuffle the resulting PCollection so results are distributed to all workers.   
partition_column  |  `str` |  Name of a column of numeric type that will be used for partitioning.   
password  |  `str` |  Password for the JDBC source. Can be specified as a plain password, or as a secret specification in JSON format if used with a secret manager.   
read_query  |  `str` |  SQL query used to query the JDBC source.   
secret_manager  |  `str` |  Secret Manager to use for fetching secret values. Available options: 'GoogleCloudSecretManager', 'GoogleCloudHsmGeneratedSecretManager'. If not set, no secret manager is used and the password is treated as a plain password.   
username  |  `str` |  Username for the JDBC source.   
  
### `MYSQL` Write

Configuration | Type | Description  
---|---|---  
**jdbc_url** |  `str` |  Connection URL for the JDBC sink.   
autosharding  |  `boolean` |  If true, enables using a dynamically determined number of shards to write.   
batch_size  |  `int64` |  n/a   
connection_init_sql  |  `list[str]` |  Sets the connection init sql statements used by the Driver. Only MySQL and MariaDB support this.   
connection_properties  |  `str` |  Used to set connection properties passed to the JDBC driver not already defined as standalone parameter (e.g. username and password can be set using parameters above accordingly). Format of the string must be "key1=value1;key2=value2;".   
location  |  `str` |  Name of the table to write to.   
password  |  `str` |  Password for the JDBC source. Can be specified as a plain password, or as a secret specification in JSON format if used with a secret manager.   
secret_manager  |  `str` |  Secret Manager to use for fetching secret values. Available options: 'GoogleCloudSecretManager', 'GoogleCloudHsmGeneratedSecretManager'. If not set, no secret manager is used and the password is treated as a plain password.   
username  |  `str` |  Username for the JDBC source.   
write_statement  |  `str` |  SQL query used to insert records into the JDBC sink.   
  
### `SQLSERVER` Read

Configuration | Type | Description  
---|---|---  
**jdbc_url** |  `str` |  Connection URL for the JDBC source.   
connection_properties  |  `str` |  Used to set connection properties passed to the JDBC driver not already defined as standalone parameter (e.g. username and password can be set using parameters above accordingly). Format of the string must be "key1=value1;key2=value2;".   
disable_auto_commit  |  `boolean` |  Whether to disable auto commit on read. Defaults to true if not provided. The need for this config varies depending on the database platform. Informix requires this to be set to false while Postgres requires this to be set to true.   
fetch_size  |  `int32` |  This method is used to override the size of the data that is going to be fetched and loaded in memory per every database call. It should ONLY be used if the default value throws memory errors.   
location  |  `str` |  Name of the table to read from.   
num_partitions  |  `int32` |  The number of partitions   
output_parallelization  |  `boolean` |  Whether to reshuffle the resulting PCollection so results are distributed to all workers.   
partition_column  |  `str` |  Name of a column of numeric type that will be used for partitioning.   
password  |  `str` |  Password for the JDBC source. Can be specified as a plain password, or as a secret specification in JSON format if used with a secret manager.   
read_query  |  `str` |  SQL query used to query the JDBC source.   
secret_manager  |  `str` |  Secret Manager to use for fetching secret values. Available options: 'GoogleCloudSecretManager', 'GoogleCloudHsmGeneratedSecretManager'. If not set, no secret manager is used and the password is treated as a plain password.   
username  |  `str` |  Username for the JDBC source.   
  
### `SQLSERVER` Write

Configuration | Type | Description  
---|---|---  
**jdbc_url** |  `str` |  Connection URL for the JDBC sink.   
autosharding  |  `boolean` |  If true, enables using a dynamically determined number of shards to write.   
batch_size  |  `int64` |  n/a   
connection_properties  |  `str` |  Used to set connection properties passed to the JDBC driver not already defined as standalone parameter (e.g. username and password can be set using parameters above accordingly). Format of the string must be "key1=value1;key2=value2;".   
location  |  `str` |  Name of the table to write to.   
password  |  `str` |  Password for the JDBC source. Can be specified as a plain password, or as a secret specification in JSON format if used with a secret manager.   
secret_manager  |  `str` |  Secret Manager to use for fetching secret values. Available options: 'GoogleCloudSecretManager', 'GoogleCloudHsmGeneratedSecretManager'. If not set, no secret manager is used and the password is treated as a plain password.   
username  |  `str` |  Username for the JDBC source.   
write_statement  |  `str` |  SQL query used to insert records into the JDBC sink.   
  
## What's next

For more information and code examples, see the following documents:

  * [Read from Databases](https://docs.cloud.google.com/dataflow/docs/guides/read-from-databases)
  * [Write to Databases](https://docs.cloud.google.com/dataflow/docs/guides/write-to-databases)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
