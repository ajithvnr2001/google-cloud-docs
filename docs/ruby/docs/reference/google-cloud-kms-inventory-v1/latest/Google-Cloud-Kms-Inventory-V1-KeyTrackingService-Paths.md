---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-Inventory-V1-KeyTrackingService-Paths/
title: KMS Inventory V1 API - Module Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Paths (v0.24.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:50.622714+00:00
---

# KMS Inventory V1 API - Module Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Paths (v0.24.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-Inventory-V1-KeyTrackingService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  KMS Inventory V1 API - Module Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Paths (v0.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.24.0 (latest)  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.2  0.15.1  0.14.1  0.13.0  0.12.2  0.11.3  0.10.0  0.9.1  0.8.3  0.7.0  0.6.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the KMS Inventory V1 API module Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Paths.

Path helper methods for the KeyTrackingService API.

## Extended By

  * [Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-Inventory-V1-KeyTrackingService-Paths)



## Included In

  * [Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-Inventory-V1-KeyTrackingService-Client)
  * [Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-Inventory-V1-KeyTrackingService-Paths)
  * [Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-Inventory-V1-KeyTrackingService-Rest-Client)



## Methods 

### #organization_path
    
    
    def organization_path(organization:) -> ::String

Create a fully-qualified Organization resource string.

The resource will be in the following format:

`organizations/{organization}`

**Parameter**

  * **organization** (String) 



**Returns**

  * (::String) 



### #project_path
    
    
    def project_path(project:) -> ::String

Create a fully-qualified Project resource string.

The resource will be in the following format:

`projects/{project}`

**Parameter**

  * **project** (String) 



**Returns**

  * (::String) 



### #protected_resources_summary_path
    
    
    def protected_resources_summary_path(project:, location:, key_ring:, crypto_key:) -> ::String
    def protected_resources_summary_path(project:, location:, key_ring:, crypto_key:, crypto_key_version:) -> ::String

Create a fully-qualified ProtectedResourcesSummary resource string.

**Overloads**
    
    
    def protected_resources_summary_path(project:, location:, key_ring:, crypto_key:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/protectedResourcesSummary`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **key_ring** (String) 
  * **crypto_key** (String) 


    
    
    def protected_resources_summary_path(project:, location:, key_ring:, crypto_key:, crypto_key_version:) -> ::String

The resource will be in the following format:

`projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}/cryptoKeyVersions/{crypto_key_version}/protectedResourcesSummary`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **key_ring** (String) 
  * **crypto_key** (String) 
  * **crypto_key_version** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
