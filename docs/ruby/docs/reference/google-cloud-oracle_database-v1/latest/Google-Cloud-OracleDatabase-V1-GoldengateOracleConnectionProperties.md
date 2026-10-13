---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleConnectionProperties/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:22.505700+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleConnectionProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties.

The properties of Goldengate Oracle Database Connection.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #authentication_mode
    
    
    def authentication_mode() -> ::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::OracleAuthenticationMode

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::OracleAuthenticationMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleConnectionProperties-OracleAuthenticationMode)) — Optional. Authentication mode. 



### #authentication_mode=
    
    
    def authentication_mode=(value) -> ::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::OracleAuthenticationMode

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::OracleAuthenticationMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleConnectionProperties-OracleAuthenticationMode)) — Optional. Authentication mode. 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::OracleAuthenticationMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleConnectionProperties-OracleAuthenticationMode)) — Optional. Authentication mode. 



### #connection_string
    
    
    def connection_string() -> ::String

**Returns**

  * (::String) — Optional. Connect descriptor or Easy Connect Naming method used to connect to a database. 



### #connection_string=
    
    
    def connection_string=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Connect descriptor or Easy Connect Naming method used to connect to a database. 



**Returns**

  * (::String) — Optional. Connect descriptor or Easy Connect Naming method used to connect to a database. 



### #gcp_oracle_database_id
    
    
    def gcp_oracle_database_id() -> ::String

**Returns**

  * (::String) — Optional. Autonomous AI Database instance id of database in Oracle Database @ Google Cloud. If gcp_oracle_database_id is provided, connection_string must be empty. Format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database} 



### #gcp_oracle_database_id=
    
    
    def gcp_oracle_database_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Autonomous AI Database instance id of database in Oracle Database @ Google Cloud. If gcp_oracle_database_id is provided, connection_string must be empty. Format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database} 



**Returns**

  * (::String) — Optional. Autonomous AI Database instance id of database in Oracle Database @ Google Cloud. If gcp_oracle_database_id is provided, connection_string must be empty. Format: projects/{project}/locations/{location}/autonomousDatabases/{autonomous_database} 



### #password
    
    
    def password() -> ::String

**Returns**

  * (::String) — Optional. Input only. The password Oracle Goldengate uses in plain text.

Note: The following fields are mutually exclusive: `password`, `password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #password=
    
    
    def password=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Input only. The password Oracle Goldengate uses in plain text.

Note: The following fields are mutually exclusive: `password`, `password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. Input only. The password Oracle Goldengate uses in plain text.

Note: The following fields are mutually exclusive: `password`, `password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #password_secret_version
    
    
    def password_secret_version() -> ::String

**Returns**

  * (::String) — Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses. Format: projects/{project}/secrets/{secret}/versions/{version}.

Note: The following fields are mutually exclusive: `password_secret_version`, `password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #password_secret_version=
    
    
    def password_secret_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses. Format: projects/{project}/secrets/{secret}/versions/{version}.

Note: The following fields are mutually exclusive: `password_secret_version`, `password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses. Format: projects/{project}/secrets/{secret}/versions/{version}.

Note: The following fields are mutually exclusive: `password_secret_version`, `password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #session_mode
    
    
    def session_mode() -> ::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::SessionMode

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::SessionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleConnectionProperties-SessionMode)) — Optional. The mode of the database connection session to be established by the data client. 



### #session_mode=
    
    
    def session_mode=(value) -> ::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::SessionMode

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::SessionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleConnectionProperties-SessionMode)) — Optional. The mode of the database connection session to be established by the data client. 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateOracleConnectionProperties::SessionMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleConnectionProperties-SessionMode)) — Optional. The mode of the database connection session to be established by the data client. 



### #technology_type
    
    
    def technology_type() -> ::String

**Returns**

  * (::String) — Optional. The technology type. 



### #technology_type=
    
    
    def technology_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The technology type. 



**Returns**

  * (::String) — Optional. The technology type. 



### #username
    
    
    def username() -> ::String

**Returns**

  * (::String) — Optional. The username Oracle Goldengate uses to connect. 



### #username=
    
    
    def username=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The username Oracle Goldengate uses to connect. 



**Returns**

  * (::String) — Optional. The username Oracle Goldengate uses to connect. 



### #wallet_file
    
    
    def wallet_file() -> ::String

**Returns**

  * (::String) — Optional. The wallet contents Oracle Goldengate uses to make connections to a database. This attribute is expected to be base64 encoded. 



### #wallet_file=
    
    
    def wallet_file=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The wallet contents Oracle Goldengate uses to make connections to a database. This attribute is expected to be base64 encoded. 



**Returns**

  * (::String) — Optional. The wallet contents Oracle Goldengate uses to make connections to a database. This attribute is expected to be base64 encoded. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
