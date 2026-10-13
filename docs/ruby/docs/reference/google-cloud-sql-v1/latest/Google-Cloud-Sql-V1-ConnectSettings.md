---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ConnectSettings/
title: Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::ConnectSettings (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:10:38.271644+00:00
---

# Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::ConnectSettings (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ConnectSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::ConnectSettings (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API class Google::Cloud::Sql::V1::ConnectSettings.

Connect settings retrieval response.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #backend_type
    
    
    def backend_type() -> ::Google::Cloud::Sql::V1::SqlBackendType

**Returns**

  * ([::Google::Cloud::Sql::V1::SqlBackendType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlBackendType)) — `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google. This property is read-only; use the `tier` property in the `settings` object to determine the database type. 



### #backend_type=
    
    
    def backend_type=(value) -> ::Google::Cloud::Sql::V1::SqlBackendType

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::SqlBackendType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlBackendType)) — `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google. This property is read-only; use the `tier` property in the `settings` object to determine the database type. 



**Returns**

  * ([::Google::Cloud::Sql::V1::SqlBackendType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlBackendType)) — `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google. This property is read-only; use the `tier` property in the `settings` object to determine the database type. 



### #connection_name
    
    
    def connection_name() -> ::String

**Returns**

  * (::String) — Optional. Output only. Connection name of the Cloud SQL instance used in connection strings, in the format project:region:instance. 



### #custom_subject_alternative_names
    
    
    def custom_subject_alternative_names() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Custom subject alternative names for the server certificate. 



### #custom_subject_alternative_names=
    
    
    def custom_subject_alternative_names=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Custom subject alternative names for the server certificate. 



**Returns**

  * (::Array<::String>) — Custom subject alternative names for the server certificate. 



### #database_version
    
    
    def database_version() -> ::Google::Cloud::Sql::V1::SqlDatabaseVersion

**Returns**

  * ([::Google::Cloud::Sql::V1::SqlDatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlDatabaseVersion)) — The database engine type and version. The `databaseVersion` field cannot be changed after instance creation. MySQL instances: `MYSQL_8_0`, `MYSQL_5_7` (default), or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12` (default), `POSTGRES_13`, or `POSTGRES_14`. SQL Server instances: `SQLSERVER_2017_STANDARD` (default), `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. 



### #database_version=
    
    
    def database_version=(value) -> ::Google::Cloud::Sql::V1::SqlDatabaseVersion

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::SqlDatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlDatabaseVersion)) — The database engine type and version. The `databaseVersion` field cannot be changed after instance creation. MySQL instances: `MYSQL_8_0`, `MYSQL_5_7` (default), or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12` (default), `POSTGRES_13`, or `POSTGRES_14`. SQL Server instances: `SQLSERVER_2017_STANDARD` (default), `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. 



**Returns**

  * ([::Google::Cloud::Sql::V1::SqlDatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlDatabaseVersion)) — The database engine type and version. The `databaseVersion` field cannot be changed after instance creation. MySQL instances: `MYSQL_8_0`, `MYSQL_5_7` (default), or `MYSQL_5_6`. PostgreSQL instances: `POSTGRES_9_6`, `POSTGRES_10`, `POSTGRES_11`, `POSTGRES_12` (default), `POSTGRES_13`, or `POSTGRES_14`. SQL Server instances: `SQLSERVER_2017_STANDARD` (default), `SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`, `SQLSERVER_2019_STANDARD`, `SQLSERVER_2019_ENTERPRISE`, `SQLSERVER_2019_EXPRESS`, or `SQLSERVER_2019_WEB`. 



### #dns_name
    
    
    def dns_name() -> ::String

**Returns**

  * (::String) — The dns name of the instance. 



### #dns_name=
    
    
    def dns_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The dns name of the instance. 



**Returns**

  * (::String) — The dns name of the instance. 



### #dns_names
    
    
    def dns_names() -> ::Array<::Google::Cloud::Sql::V1::DnsNameMapping>

**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::DnsNameMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-DnsNameMapping)>) — Output only. The list of DNS names used by this instance. 



### #ip_addresses
    
    
    def ip_addresses() -> ::Array<::Google::Cloud::Sql::V1::IpMapping>

**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::IpMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-IpMapping)>) — The assigned IP addresses for the instance. 



### #ip_addresses=
    
    
    def ip_addresses=(value) -> ::Array<::Google::Cloud::Sql::V1::IpMapping>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Sql::V1::IpMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-IpMapping)>) — The assigned IP addresses for the instance. 



**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::IpMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-IpMapping)>) — The assigned IP addresses for the instance. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — This is always `sql#connectSettings`. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — This is always `sql#connectSettings`. 



**Returns**

  * (::String) — This is always `sql#connectSettings`. 



### #mdx_protocol_support
    
    
    def mdx_protocol_support() -> ::Array<::Google::Cloud::Sql::V1::ConnectSettings::MdxProtocolSupport>

**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::ConnectSettings::MdxProtocolSupport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ConnectSettings-MdxProtocolSupport)>) — Optional. Output only. mdx_protocol_support controls how the client uses metadata exchange when connecting to the instance. The values in the list representing parts of the MDX protocol that are supported by this instance. When the list is empty, the instance does not support MDX, so the client must not send an MDX request. The default is empty. 



### #node_count
    
    
    def node_count() -> ::Integer

**Returns**

  * (::Integer) — The number of read pool nodes in a read pool. 



### #node_count=
    
    
    def node_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The number of read pool nodes in a read pool. 



**Returns**

  * (::Integer) — The number of read pool nodes in a read pool. 



### #nodes
    
    
    def nodes() -> ::Array<::Google::Cloud::Sql::V1::ConnectSettings::ConnectPoolNodeConfig>

**Returns**

  * (::Array<[::Google::Cloud::Sql::V1::ConnectSettings::ConnectPoolNodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ConnectSettings-ConnectPoolNodeConfig)>) — Output only. Entries containing information about each read pool node of the read pool. 



### #psc_enabled
    
    
    def psc_enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Whether PSC connectivity is enabled for this instance. 



### #psc_enabled=
    
    
    def psc_enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether PSC connectivity is enabled for this instance. 



**Returns**

  * (::Boolean) — Whether PSC connectivity is enabled for this instance. 



### #region
    
    
    def region() -> ::String

**Returns**

  * (::String) — The cloud region for the instance. For example, `us-central1`, `europe-west1`. The region cannot be changed after instance creation. 



### #region=
    
    
    def region=(value) -> ::String

**Parameter**

  * **value** (::String) — The cloud region for the instance. For example, `us-central1`, `europe-west1`. The region cannot be changed after instance creation. 



**Returns**

  * (::String) — The cloud region for the instance. For example, `us-central1`, `europe-west1`. The region cannot be changed after instance creation. 



### #server_ca_cert
    
    
    def server_ca_cert() -> ::Google::Cloud::Sql::V1::SslCert

**Returns**

  * ([::Google::Cloud::Sql::V1::SslCert](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SslCert)) — SSL configuration. 



### #server_ca_cert=
    
    
    def server_ca_cert=(value) -> ::Google::Cloud::Sql::V1::SslCert

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::SslCert](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SslCert)) — SSL configuration. 



**Returns**

  * ([::Google::Cloud::Sql::V1::SslCert](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SslCert)) — SSL configuration. 



### #server_ca_mode
    
    
    def server_ca_mode() -> ::Google::Cloud::Sql::V1::ConnectSettings::CaMode

**Returns**

  * ([::Google::Cloud::Sql::V1::ConnectSettings::CaMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ConnectSettings-CaMode)) — Specify what type of CA is used for the server certificate. 



### #server_ca_mode=
    
    
    def server_ca_mode=(value) -> ::Google::Cloud::Sql::V1::ConnectSettings::CaMode

**Parameter**

  * **value** ([::Google::Cloud::Sql::V1::ConnectSettings::CaMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ConnectSettings-CaMode)) — Specify what type of CA is used for the server certificate. 



**Returns**

  * ([::Google::Cloud::Sql::V1::ConnectSettings::CaMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-ConnectSettings-CaMode)) — Specify what type of CA is used for the server certificate. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
