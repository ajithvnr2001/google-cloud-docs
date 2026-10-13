---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-DemoteMasterMySqlReplicaConfiguration/
title: Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:08.099136+00:00
---

# Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-DemoteMasterMySqlReplicaConfiguration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API class Google::Cloud::Sql::V1::DemoteMasterMySqlReplicaConfiguration.

Read-replica configuration specific to MySQL databases.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ca_certificate
    
    
    def ca_certificate() -> ::String

**Returns**

  * (::String) — PEM representation of the trusted CA's x509 certificate. 



### #ca_certificate=
    
    
    def ca_certificate=(value) -> ::String

**Parameter**

  * **value** (::String) — PEM representation of the trusted CA's x509 certificate. 



**Returns**

  * (::String) — PEM representation of the trusted CA's x509 certificate. 



### #client_certificate
    
    
    def client_certificate() -> ::String

**Returns**

  * (::String) — PEM representation of the replica's x509 certificate. 



### #client_certificate=
    
    
    def client_certificate=(value) -> ::String

**Parameter**

  * **value** (::String) — PEM representation of the replica's x509 certificate. 



**Returns**

  * (::String) — PEM representation of the replica's x509 certificate. 



### #client_key
    
    
    def client_key() -> ::String

**Returns**

  * (::String) — PEM representation of the replica's private key. The corresponding public key is encoded in the client's certificate. The format of the replica's private key can be either PKCS #1 or PKCS #8. 



### #client_key=
    
    
    def client_key=(value) -> ::String

**Parameter**

  * **value** (::String) — PEM representation of the replica's private key. The corresponding public key is encoded in the client's certificate. The format of the replica's private key can be either PKCS #1 or PKCS #8. 



**Returns**

  * (::String) — PEM representation of the replica's private key. The corresponding public key is encoded in the client's certificate. The format of the replica's private key can be either PKCS #1 or PKCS #8. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — This is always `sql#demoteMasterMysqlReplicaConfiguration`. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — This is always `sql#demoteMasterMysqlReplicaConfiguration`. 



**Returns**

  * (::String) — This is always `sql#demoteMasterMysqlReplicaConfiguration`. 



### #password
    
    
    def password() -> ::String

**Returns**

  * (::String) — The password for the replication connection. 



### #password=
    
    
    def password=(value) -> ::String

**Parameter**

  * **value** (::String) — The password for the replication connection. 



**Returns**

  * (::String) — The password for the replication connection. 



### #username
    
    
    def username() -> ::String

**Returns**

  * (::String) — The username for the replication connection. 



### #username=
    
    
    def username=(value) -> ::String

**Parameter**

  * **value** (::String) — The username for the replication connection. 



**Returns**

  * (::String) — The username for the replication connection. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
