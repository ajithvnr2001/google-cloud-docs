---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOggDeployment/
title: Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOggDeployment (v1.1.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:23.133662+00:00
---

# Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOggDeployment (v1.1.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOggDeployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Oracle Database@Google Cloud V1 API - Class Google::Cloud::OracleDatabase::V1::GoldengateOggDeployment (v1.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.1 (latest)  1.1.0  1.0.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Oracle Database@Google Cloud V1 API class Google::Cloud::OracleDatabase::V1::GoldengateOggDeployment.

The Ogg data of the GoldengateDeployment.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #admin_password
    
    
    def admin_password() -> ::String

**Returns**

  * (::String) — Optional. The Goldengate deployment console password in plain text.

Note: The following fields are mutually exclusive: `admin_password`, `admin_password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #admin_password=
    
    
    def admin_password=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Goldengate deployment console password in plain text.

Note: The following fields are mutually exclusive: `admin_password`, `admin_password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. The Goldengate deployment console password in plain text.

Note: The following fields are mutually exclusive: `admin_password`, `admin_password_secret_version`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #admin_password_secret_version
    
    
    def admin_password_secret_version() -> ::String

**Returns**

  * (::String) — Optional. Input only. The Goldengate deployment console password secret version.

Note: The following fields are mutually exclusive: `admin_password_secret_version`, `admin_password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #admin_password_secret_version=
    
    
    def admin_password_secret_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Input only. The Goldengate deployment console password secret version.

Note: The following fields are mutually exclusive: `admin_password_secret_version`, `admin_password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Optional. Input only. The Goldengate deployment console password secret version.

Note: The following fields are mutually exclusive: `admin_password_secret_version`, `admin_password`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #admin_username
    
    
    def admin_username() -> ::String

**Returns**

  * (::String) — Required. The Goldengate deployment console username. 



### #admin_username=
    
    
    def admin_username=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The Goldengate deployment console username. 



**Returns**

  * (::String) — Required. The Goldengate deployment console username. 



### #certificate
    
    
    def certificate() -> ::String

**Returns**

  * (::String) — Output only. The certificate of the GoldengateDeployment. 



### #credential_store
    
    
    def credential_store() -> ::Google::Cloud::OracleDatabase::V1::GoldengateOggDeployment::CredentialStore

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateOggDeployment::CredentialStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateOggDeployment-CredentialStore)) — Output only. The credential store of the GoldengateDeployment. 



### #deployment
    
    
    def deployment() -> ::String

**Returns**

  * (::String) — Required. The name given to the Goldengate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter. 



### #deployment=
    
    
    def deployment=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name given to the Goldengate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter. 



**Returns**

  * (::String) — Required. The name given to the Goldengate service deployment. The name must be 1 to 32 characters long, must contain only alphanumeric characters and must start with a letter. 



### #group_roles_mapping
    
    
    def group_roles_mapping() -> ::Google::Cloud::OracleDatabase::V1::GoldengateGroupToRolesMapping

**Returns**

  * ([::Google::Cloud::OracleDatabase::V1::GoldengateGroupToRolesMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-oracle_database-v1/latest/Google-Cloud-OracleDatabase-V1-GoldengateGroupToRolesMapping)) — Output only. The group to roles mapping of the GoldengateDeployment. 



### #identity_domain_id
    
    
    def identity_domain_id() -> ::String

**Returns**

  * (::String) — Output only. The identity domain id of the GoldengateDeployment. 



### #ogg_version
    
    
    def ogg_version() -> ::String

**Returns**

  * (::String) — Optional. Version of OGG 



### #ogg_version=
    
    
    def ogg_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Version of OGG 



**Returns**

  * (::String) — Optional. Version of OGG 



### #password_secret_id
    
    
    def password_secret_id() -> ::String

**Returns**

  * (::String) — Output only. The password secret id of the GoldengateDeployment. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
