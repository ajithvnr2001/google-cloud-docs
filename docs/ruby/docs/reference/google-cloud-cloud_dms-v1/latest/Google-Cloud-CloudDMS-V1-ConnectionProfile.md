---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConnectionProfile (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:21.857045+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConnectionProfile (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::ConnectionProfile (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::ConnectionProfile.

A connection profile definition.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #alloydb
    
    
    def alloydb() -> ::Google::Cloud::CloudDMS::V1::AlloyDbConnectionProfile

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbConnectionProfile)) — An AlloyDB cluster connection profile.

Note: The following fields are mutually exclusive: `alloydb`, `mysql`, `postgresql`, `oracle`, `cloudsql`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #alloydb=
    
    
    def alloydb=(value) -> ::Google::Cloud::CloudDMS::V1::AlloyDbConnectionProfile

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::AlloyDbConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbConnectionProfile)) — An AlloyDB cluster connection profile.

Note: The following fields are mutually exclusive: `alloydb`, `mysql`, `postgresql`, `oracle`, `cloudsql`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::AlloyDbConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-AlloyDbConnectionProfile)) — An AlloyDB cluster connection profile.

Note: The following fields are mutually exclusive: `alloydb`, `mysql`, `postgresql`, `oracle`, `cloudsql`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloudsql
    
    
    def cloudsql() -> ::Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlConnectionProfile)) — A CloudSQL database connection profile.

Note: The following fields are mutually exclusive: `cloudsql`, `mysql`, `postgresql`, `oracle`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloudsql=
    
    
    def cloudsql=(value) -> ::Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlConnectionProfile)) — A CloudSQL database connection profile.

Note: The following fields are mutually exclusive: `cloudsql`, `mysql`, `postgresql`, `oracle`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::CloudSqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CloudSqlConnectionProfile)) — A CloudSQL database connection profile.

Note: The following fields are mutually exclusive: `cloudsql`, `mysql`, `postgresql`, `oracle`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The connection profile display name. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The connection profile display name. 



**Returns**

  * (::String) — The connection profile display name. 



### #error
    
    
    def error() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Rpc-Status)) — Output only. The error details in case of state FAILED. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.

Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.

Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — The resource labels for connection profile to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.

Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. 




### #mysql
    
    
    def mysql() -> ::Google::Cloud::CloudDMS::V1::MySqlConnectionProfile

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MySqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MySqlConnectionProfile)) — A MySQL database connection profile.

Note: The following fields are mutually exclusive: `mysql`, `postgresql`, `oracle`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #mysql=
    
    
    def mysql=(value) -> ::Google::Cloud::CloudDMS::V1::MySqlConnectionProfile

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::MySqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MySqlConnectionProfile)) — A MySQL database connection profile.

Note: The following fields are mutually exclusive: `mysql`, `postgresql`, `oracle`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MySqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MySqlConnectionProfile)) — A MySQL database connection profile.

Note: The following fields are mutually exclusive: `mysql`, `postgresql`, `oracle`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}. 



**Returns**

  * (::String) — The name of this connection profile resource in the form of projects/{project}/locations/{location}/connectionProfiles/{connectionProfile}. 



### #oracle
    
    
    def oracle() -> ::Google::Cloud::CloudDMS::V1::OracleConnectionProfile

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::OracleConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-OracleConnectionProfile)) — An Oracle database connection profile.

Note: The following fields are mutually exclusive: `oracle`, `mysql`, `postgresql`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #oracle=
    
    
    def oracle=(value) -> ::Google::Cloud::CloudDMS::V1::OracleConnectionProfile

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::OracleConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-OracleConnectionProfile)) — An Oracle database connection profile.

Note: The following fields are mutually exclusive: `oracle`, `mysql`, `postgresql`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::OracleConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-OracleConnectionProfile)) — An Oracle database connection profile.

Note: The following fields are mutually exclusive: `oracle`, `mysql`, `postgresql`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #postgresql
    
    
    def postgresql() -> ::Google::Cloud::CloudDMS::V1::PostgreSqlConnectionProfile

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::PostgreSqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PostgreSqlConnectionProfile)) — A PostgreSQL database connection profile.

Note: The following fields are mutually exclusive: `postgresql`, `mysql`, `oracle`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #postgresql=
    
    
    def postgresql=(value) -> ::Google::Cloud::CloudDMS::V1::PostgreSqlConnectionProfile

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::PostgreSqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PostgreSqlConnectionProfile)) — A PostgreSQL database connection profile.

Note: The following fields are mutually exclusive: `postgresql`, `mysql`, `oracle`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::CloudDMS::V1::PostgreSqlConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PostgreSqlConnectionProfile)) — A PostgreSQL database connection profile.

Note: The following fields are mutually exclusive: `postgresql`, `mysql`, `oracle`, `cloudsql`, `alloydb`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #provider
    
    
    def provider() -> ::Google::Cloud::CloudDMS::V1::DatabaseProvider

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseProvider)) — The database provider. 



### #provider=
    
    
    def provider=(value) -> ::Google::Cloud::CloudDMS::V1::DatabaseProvider

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::DatabaseProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseProvider)) — The database provider. 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DatabaseProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseProvider)) — The database provider. 



### #state
    
    
    def state() -> ::Google::Cloud::CloudDMS::V1::ConnectionProfile::State

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConnectionProfile::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile-State)) — The current connection profile state (e.g. DRAFT, READY, or FAILED). 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::CloudDMS::V1::ConnectionProfile::State

**Parameter**

  * **value** ([::Google::Cloud::CloudDMS::V1::ConnectionProfile::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile-State)) — The current connection profile state (e.g. DRAFT, READY, or FAILED). 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConnectionProfile::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile-State)) — The current connection profile state (e.g. DRAFT, READY, or FAILED). 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp)) — Output only. The timestamp when the resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
