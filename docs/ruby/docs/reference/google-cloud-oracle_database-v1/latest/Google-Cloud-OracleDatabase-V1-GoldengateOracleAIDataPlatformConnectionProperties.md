---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleAIDataPlatformConnectionProperties/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOracleAIDataPlatformConnectionProperties (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:15.658526+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOracleAIDataPlatformConnectionProperties (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOracleAIDataPlatformConnectionProperties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOracleAIDataPlatformConnectionProperties (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::GoldengateOracleAIDataPlatformConnectionProperties.

The properties of GoldengateOracleAIDataPlatformConnection.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #connection_url
    
    
    def connection_url() -> ::String

**Returns**

  * (::String) — Optional. Connection URL. It must start with 'jdbc:spark://' 



### #connection_url=
    
    
    def connection_url=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Connection URL. It must start with 'jdbc:spark://' 



**Returns**

  * (::String) — Optional. Connection URL. It must start with 'jdbc:spark://' 



### #private_key_file
    
    
    def private_key_file() -> ::String

**Returns**

  * (::String) — Optional. The content of the private key file (PEM file) corresponding to the API key of the fingerprint. 



### #private_key_file=
    
    
    def private_key_file=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The content of the private key file (PEM file) corresponding to the API key of the fingerprint. 



**Returns**

  * (::String) — Optional. The content of the private key file (PEM file) corresponding to the API key of the fingerprint. 



### #private_key_passphrase_secret
    
    
    def private_key_passphrase_secret() -> ::String

**Returns**

  * (::String) — Optional. The passphrase of the private key. 



### #private_key_passphrase_secret=
    
    
    def private_key_passphrase_secret=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The passphrase of the private key. 



**Returns**

  * (::String) — Optional. The passphrase of the private key. 



### #public_key_fingerprint
    
    
    def public_key_fingerprint() -> ::String

**Returns**

  * (::String) — Optional. The fingerprint of the API Key of the user specified by the user_id. 



### #public_key_fingerprint=
    
    
    def public_key_fingerprint=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The fingerprint of the API Key of the user specified by the user_id. 



**Returns**

  * (::String) — Optional. The fingerprint of the API Key of the user specified by the user_id. 



### #region
    
    
    def region() -> ::String

**Returns**

  * (::String) — Optional. The name of the region. e.g.: us-ashburn-1 



### #region=
    
    
    def region=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The name of the region. e.g.: us-ashburn-1 



**Returns**

  * (::String) — Optional. The name of the region. e.g.: us-ashburn-1 



### #technology_type
    
    
    def technology_type() -> ::String

**Returns**

  * (::String) — Optional. The technology type of OracleAiDataPlatformConnection. 



### #technology_type=
    
    
    def technology_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The technology type of OracleAiDataPlatformConnection. 



**Returns**

  * (::String) — Optional. The technology type of OracleAiDataPlatformConnection. 



### #tenancy_id
    
    
    def tenancy_id() -> ::String

**Returns**

  * (::String) — Optional. The OCID of the related OCI tenancy. 



### #tenancy_id=
    
    
    def tenancy_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The OCID of the related OCI tenancy. 



**Returns**

  * (::String) — Optional. The OCID of the related OCI tenancy. 



### #use_resource_principal
    
    
    def use_resource_principal() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Specifies that the user intends to authenticate to the instance using a resource principal. 



### #use_resource_principal=
    
    
    def use_resource_principal=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Specifies that the user intends to authenticate to the instance using a resource principal. 



**Returns**

  * (::Boolean) — Optional. Specifies that the user intends to authenticate to the instance using a resource principal. 



### #user_id
    
    
    def user_id() -> ::String

**Returns**

  * (::String) — Optional. The OCID of the OCI user who will access. 



### #user_id=
    
    
    def user_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The OCID of the OCI user who will access. 



**Returns**

  * (::String) — Optional. The OCID of the OCI user who will access. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
