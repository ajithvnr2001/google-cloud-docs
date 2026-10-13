---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Dialect/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::Dialect (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:02.229778+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::Dialect (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-Dialect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::Dialect (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::Dialect.

The possible dialect options for translation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #azure_synapse_dialect
    
    
    def azure_synapse_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::AzureSynapseDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::AzureSynapseDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-AzureSynapseDialect)) — The Azure Synapse dialect

Note: The following fields are mutually exclusive: `azure_synapse_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #azure_synapse_dialect=
    
    
    def azure_synapse_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::AzureSynapseDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::AzureSynapseDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-AzureSynapseDialect)) — The Azure Synapse dialect

Note: The following fields are mutually exclusive: `azure_synapse_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::AzureSynapseDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-AzureSynapseDialect)) — The Azure Synapse dialect

Note: The following fields are mutually exclusive: `azure_synapse_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bigquery_dialect
    
    
    def bigquery_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::BigQueryDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::BigQueryDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-BigQueryDialect)) — The BigQuery dialect

Note: The following fields are mutually exclusive: `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #bigquery_dialect=
    
    
    def bigquery_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::BigQueryDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::BigQueryDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-BigQueryDialect)) — The BigQuery dialect

Note: The following fields are mutually exclusive: `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::BigQueryDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-BigQueryDialect)) — The BigQuery dialect

Note: The following fields are mutually exclusive: `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #db2_dialect
    
    
    def db2_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::DB2Dialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::DB2Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-DB2Dialect)) — DB2 dialect

Note: The following fields are mutually exclusive: `db2_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #db2_dialect=
    
    
    def db2_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::DB2Dialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::DB2Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-DB2Dialect)) — DB2 dialect

Note: The following fields are mutually exclusive: `db2_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::DB2Dialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-DB2Dialect)) — DB2 dialect

Note: The following fields are mutually exclusive: `db2_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #greenplum_dialect
    
    
    def greenplum_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::GreenplumDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::GreenplumDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GreenplumDialect)) — Greenplum dialect

Note: The following fields are mutually exclusive: `greenplum_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #greenplum_dialect=
    
    
    def greenplum_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::GreenplumDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::GreenplumDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GreenplumDialect)) — Greenplum dialect

Note: The following fields are mutually exclusive: `greenplum_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::GreenplumDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GreenplumDialect)) — Greenplum dialect

Note: The following fields are mutually exclusive: `greenplum_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #hiveql_dialect
    
    
    def hiveql_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::HiveQLDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::HiveQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-HiveQLDialect)) — The HiveQL dialect

Note: The following fields are mutually exclusive: `hiveql_dialect`, `bigquery_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #hiveql_dialect=
    
    
    def hiveql_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::HiveQLDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::HiveQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-HiveQLDialect)) — The HiveQL dialect

Note: The following fields are mutually exclusive: `hiveql_dialect`, `bigquery_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::HiveQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-HiveQLDialect)) — The HiveQL dialect

Note: The following fields are mutually exclusive: `hiveql_dialect`, `bigquery_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mysql_dialect
    
    
    def mysql_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::MySQLDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MySQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MySQLDialect)) — The MySQL dialect

Note: The following fields are mutually exclusive: `mysql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mysql_dialect=
    
    
    def mysql_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::MySQLDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::MySQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MySQLDialect)) — The MySQL dialect

Note: The following fields are mutually exclusive: `mysql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MySQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MySQLDialect)) — The MySQL dialect

Note: The following fields are mutually exclusive: `mysql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #netezza_dialect
    
    
    def netezza_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::NetezzaDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::NetezzaDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-NetezzaDialect)) — The Netezza dialect

Note: The following fields are mutually exclusive: `netezza_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #netezza_dialect=
    
    
    def netezza_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::NetezzaDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::NetezzaDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-NetezzaDialect)) — The Netezza dialect

Note: The following fields are mutually exclusive: `netezza_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::NetezzaDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-NetezzaDialect)) — The Netezza dialect

Note: The following fields are mutually exclusive: `netezza_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #oracle_dialect
    
    
    def oracle_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::OracleDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::OracleDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-OracleDialect)) — The Oracle dialect

Note: The following fields are mutually exclusive: `oracle_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #oracle_dialect=
    
    
    def oracle_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::OracleDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::OracleDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-OracleDialect)) — The Oracle dialect

Note: The following fields are mutually exclusive: `oracle_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::OracleDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-OracleDialect)) — The Oracle dialect

Note: The following fields are mutually exclusive: `oracle_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #postgresql_dialect
    
    
    def postgresql_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::PostgresqlDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::PostgresqlDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-PostgresqlDialect)) — The Postgresql dialect

Note: The following fields are mutually exclusive: `postgresql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #postgresql_dialect=
    
    
    def postgresql_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::PostgresqlDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::PostgresqlDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-PostgresqlDialect)) — The Postgresql dialect

Note: The following fields are mutually exclusive: `postgresql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::PostgresqlDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-PostgresqlDialect)) — The Postgresql dialect

Note: The following fields are mutually exclusive: `postgresql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #presto_dialect
    
    
    def presto_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::PrestoDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::PrestoDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-PrestoDialect)) — The Presto dialect

Note: The following fields are mutually exclusive: `presto_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #presto_dialect=
    
    
    def presto_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::PrestoDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::PrestoDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-PrestoDialect)) — The Presto dialect

Note: The following fields are mutually exclusive: `presto_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::PrestoDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-PrestoDialect)) — The Presto dialect

Note: The following fields are mutually exclusive: `presto_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #redshift_dialect
    
    
    def redshift_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::RedshiftDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::RedshiftDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-RedshiftDialect)) — The Redshift dialect

Note: The following fields are mutually exclusive: `redshift_dialect`, `bigquery_dialect`, `hiveql_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #redshift_dialect=
    
    
    def redshift_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::RedshiftDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::RedshiftDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-RedshiftDialect)) — The Redshift dialect

Note: The following fields are mutually exclusive: `redshift_dialect`, `bigquery_dialect`, `hiveql_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::RedshiftDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-RedshiftDialect)) — The Redshift dialect

Note: The following fields are mutually exclusive: `redshift_dialect`, `bigquery_dialect`, `hiveql_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #snowflake_dialect
    
    
    def snowflake_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::SnowflakeDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SnowflakeDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SnowflakeDialect)) — The Snowflake dialect

Note: The following fields are mutually exclusive: `snowflake_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #snowflake_dialect=
    
    
    def snowflake_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::SnowflakeDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::SnowflakeDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SnowflakeDialect)) — The Snowflake dialect

Note: The following fields are mutually exclusive: `snowflake_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SnowflakeDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SnowflakeDialect)) — The Snowflake dialect

Note: The following fields are mutually exclusive: `snowflake_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sparksql_dialect
    
    
    def sparksql_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::SparkSQLDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SparkSQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SparkSQLDialect)) — The SparkSQL dialect

Note: The following fields are mutually exclusive: `sparksql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sparksql_dialect=
    
    
    def sparksql_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::SparkSQLDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::SparkSQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SparkSQLDialect)) — The SparkSQL dialect

Note: The following fields are mutually exclusive: `sparksql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SparkSQLDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SparkSQLDialect)) — The SparkSQL dialect

Note: The following fields are mutually exclusive: `sparksql_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sql_server_dialect
    
    
    def sql_server_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::SQLServerDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SQLServerDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SQLServerDialect)) — The SQL Server dialect

Note: The following fields are mutually exclusive: `sql_server_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sql_server_dialect=
    
    
    def sql_server_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::SQLServerDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::SQLServerDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SQLServerDialect)) — The SQL Server dialect

Note: The following fields are mutually exclusive: `sql_server_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SQLServerDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SQLServerDialect)) — The SQL Server dialect

Note: The following fields are mutually exclusive: `sql_server_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sqlite_dialect
    
    
    def sqlite_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::SQLiteDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SQLiteDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SQLiteDialect)) — SQLite dialect

Note: The following fields are mutually exclusive: `sqlite_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #sqlite_dialect=
    
    
    def sqlite_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::SQLiteDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::SQLiteDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SQLiteDialect)) — SQLite dialect

Note: The following fields are mutually exclusive: `sqlite_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::SQLiteDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-SQLiteDialect)) — SQLite dialect

Note: The following fields are mutually exclusive: `sqlite_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #teradata_dialect
    
    
    def teradata_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::TeradataDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::TeradataDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TeradataDialect)) — The Teradata dialect

Note: The following fields are mutually exclusive: `teradata_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #teradata_dialect=
    
    
    def teradata_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::TeradataDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::TeradataDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TeradataDialect)) — The Teradata dialect

Note: The following fields are mutually exclusive: `teradata_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::TeradataDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TeradataDialect)) — The Teradata dialect

Note: The following fields are mutually exclusive: `teradata_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `vertica_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vertica_dialect
    
    
    def vertica_dialect() -> ::Google::Cloud::Bigquery::Migration::V2::VerticaDialect

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::VerticaDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-VerticaDialect)) — The Vertica dialect

Note: The following fields are mutually exclusive: `vertica_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #vertica_dialect=
    
    
    def vertica_dialect=(value) -> ::Google::Cloud::Bigquery::Migration::V2::VerticaDialect

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Migration::V2::VerticaDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-VerticaDialect)) — The Vertica dialect

Note: The following fields are mutually exclusive: `vertica_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::VerticaDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-VerticaDialect)) — The Vertica dialect

Note: The following fields are mutually exclusive: `vertica_dialect`, `bigquery_dialect`, `hiveql_dialect`, `redshift_dialect`, `teradata_dialect`, `oracle_dialect`, `sparksql_dialect`, `snowflake_dialect`, `netezza_dialect`, `azure_synapse_dialect`, `sql_server_dialect`, `postgresql_dialect`, `presto_dialect`, `mysql_dialect`, `db2_dialect`, `sqlite_dialect`, `greenplum_dialect`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
