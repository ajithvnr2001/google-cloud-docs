---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMysqlConnectionProperties/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:44.770641+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMysqlConnectionProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties.

Properties of GoldengateMysqlConnection.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #additional_attributes
    
    
    def additional_attributes() -> ::Array<::Google::Cloud::OracleDatabase::V1::NameValuePair>

**Returns**

  * (::Array<[::Google::Cloud::OracleDatabase::V1::NameValuePair](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-NameValuePair)>) — Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string. 



### #additional_attributes=
    
    
    def additional_attributes=(value) -> ::Array<::Google::Cloud::OracleDatabase::V1::NameValuePair>

**Parameter**

  * **value** (::Array<[::Google::Cloud::OracleDatabase::V1::NameValuePair](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-NameValuePair)>) — Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string. 



**Returns**

  * (::Array<[::Google::Cloud::OracleDatabase::V1::NameValuePair](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-NameValuePair)>) — Optional. An array of name-value pair attribute entries. Used as additional parameters in connection string. 



### #database
    
    
    def database() -> ::String

**Returns**

  * (::String) — Optional. The name of the database. 



### #database=
    
    
    def database=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The name of the database. 



**Returns**

  * (::String) — Optional. The name of the database. 



### #db_system_id
    
    
    def db_system_id() -> ::String

**Returns**

  * (::String) — Optional. The OCID of the database system being referenced. 



### #db_system_id=
    
    
    def db_system_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The OCID of the database system being referenced. 



**Returns**

  * (::String) — Optional. The OCID of the database system being referenced. 



### #host
    
    
    def host() -> ::String

**Returns**

  * (::String) — Optional. The name or address of a host. 



### #host=
    
    
    def host=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The name or address of a host. 



**Returns**

  * (::String) — Optional. The name or address of a host. 



### #password
    
    
    def password() -> ::String

**Returns**

  * (::String) — Optional. Input only. The password Oracle Goldengate uses to connect to MySQL in plain text.

Note: The following fields are mutually exclusive: `password`, `password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #password=
    
    
    def password=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Input only. The password Oracle Goldengate uses to connect to MySQL in plain text.

Note: The following fields are mutually exclusive: `password`, `password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. Input only. The password Oracle Goldengate uses to connect to MySQL in plain text.

Note: The following fields are mutually exclusive: `password`, `password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #password_secret_version
    
    
    def password_secret_version() -> ::String

**Returns**

  * (::String) — Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect to MySQL. Format: projects/{project}/secrets/{secret}/versions/{version}.

Note: The following fields are mutually exclusive: `password_secret_version`, `password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #password_secret_version=
    
    
    def password_secret_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect to MySQL. Format: projects/{project}/secrets/{secret}/versions/{version}.

Note: The following fields are mutually exclusive: `password_secret_version`, `password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. Input only. The resource name of a secret version in Secret Manager which contains the password Oracle Goldengate uses to connect to MySQL. Format: projects/{project}/secrets/{secret}/versions/{version}.

Note: The following fields are mutually exclusive: `password_secret_version`, `password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #port
    
    
    def port() -> ::Integer

**Returns**

  * (::Integer) — Optional. The port of an endpoint usually specified for a connection. 



### #port=
    
    
    def port=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The port of an endpoint usually specified for a connection. 



**Returns**

  * (::Integer) — Optional. The port of an endpoint usually specified for a connection. 



### #security_protocol
    
    
    def security_protocol() -> ::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::MysqlSecurityProtocol

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::MysqlSecurityProtocol](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMysqlConnectionProperties-MysqlSecurityProtocol)) — Optional. Security Type for MySQL. 



### #security_protocol=
    
    
    def security_protocol=(value) -> ::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::MysqlSecurityProtocol

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::MysqlSecurityProtocol](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMysqlConnectionProperties-MysqlSecurityProtocol)) — Optional. Security Type for MySQL. 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::MysqlSecurityProtocol](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMysqlConnectionProperties-MysqlSecurityProtocol)) — Optional. Security Type for MySQL. 



### #ssl_ca_file
    
    
    def ssl_ca_file() -> ::String

**Returns**

  * (::String) — Optional. Database Certificate - The base64 encoded content of a .pem or .crt file containing the server public key (for 1 and 2-way SSL). 



### #ssl_ca_file=
    
    
    def ssl_ca_file=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Database Certificate - The base64 encoded content of a .pem or .crt file containing the server public key (for 1 and 2-way SSL). 



**Returns**

  * (::String) — Optional. Database Certificate - The base64 encoded content of a .pem or .crt file containing the server public key (for 1 and 2-way SSL). 



### #ssl_cert_file
    
    
    def ssl_cert_file() -> ::String

**Returns**

  * (::String) — Optional. Client Certificate - The base64 encoded content of a .pem or .crt file containing the client public key (for 2-way SSL). 



### #ssl_cert_file=
    
    
    def ssl_cert_file=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Client Certificate - The base64 encoded content of a .pem or .crt file containing the client public key (for 2-way SSL). 



**Returns**

  * (::String) — Optional. Client Certificate - The base64 encoded content of a .pem or .crt file containing the client public key (for 2-way SSL). 



### #ssl_crl_file
    
    
    def ssl_crl_file() -> ::String

**Returns**

  * (::String) — Optional. The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA). 



### #ssl_crl_file=
    
    
    def ssl_crl_file=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA). 



**Returns**

  * (::String) — Optional. The base64 encoded list of certificates revoked by the trusted certificate authorities (Trusted CA). 



### #ssl_key_file
    
    
    def ssl_key_file() -> ::String

**Returns**

  * (::String) — Optional. Client Key - The base64 encoded content of a .pem or .crt file containing the client private key (for 2-way SSL). 



### #ssl_key_file=
    
    
    def ssl_key_file=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Client Key - The base64 encoded content of a .pem or .crt file containing the client private key (for 2-way SSL). 



**Returns**

  * (::String) — Optional. Client Key - The base64 encoded content of a .pem or .crt file containing the client private key (for 2-way SSL). 



### #ssl_mode
    
    
    def ssl_mode() -> ::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::SSLMode

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::SSLMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMysqlConnectionProperties-SSLMode)) — Optional. SSL modes for MySQL. 



### #ssl_mode=
    
    
    def ssl_mode=(value) -> ::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::SSLMode

**Parameter**

  * **value** ([::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::SSLMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMysqlConnectionProperties-SSLMode)) — Optional. SSL modes for MySQL. 



**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateMysqlConnectionProperties::SSLMode](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateMysqlConnectionProperties-SSLMode)) — Optional. SSL modes for MySQL. 



### #technology_type
    
    
    def technology_type() -> ::String

**Returns**

  * (::String) — Optional. The technology type of MysqlConnection. 



### #technology_type=
    
    
    def technology_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The technology type of MysqlConnection. 



**Returns**

  * (::String) — Optional. The technology type of MysqlConnection. 



### #username
    
    
    def username() -> ::String

**Returns**

  * (::String) — Optional. The username Oracle Goldengate uses to connect the associated system of the given technology. 



### #username=
    
    
    def username=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The username Oracle Goldengate uses to connect the associated system of the given technology. 



**Returns**

  * (::String) — Optional. The username Oracle Goldengate uses to connect the associated system of the given technology. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
