---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Paths/
title: Dataproc Metastore V1 API - Module Google::Cloud::Metastore::V1::DataprocMetastore::Paths (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:48.634998+00:00
---

# Dataproc Metastore V1 API - Module Google::Cloud::Metastore::V1::DataprocMetastore::Paths (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1 API - Module Google::Cloud::Metastore::V1::DataprocMetastore::Paths (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Dataproc Metastore V1 API module Google::Cloud::Metastore::V1::DataprocMetastore::Paths.

Path helper methods for the DataprocMetastore API.

## Extended By

  * [Google::Cloud::Metastore::V1::DataprocMetastore::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Paths)



## Included In

  * [Google::Cloud::Metastore::V1::DataprocMetastore::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client)
  * [Google::Cloud::Metastore::V1::DataprocMetastore::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Paths)
  * [Google::Cloud::Metastore::V1::DataprocMetastore::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Rest-Client)



## Methods 

### #backup_path
    
    
    def backup_path(project:, location:, service:, backup:) -> ::String

Create a fully-qualified Backup resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/services/{service}/backups/{backup}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service** (String) 
  * **backup** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #metadata_import_path
    
    
    def metadata_import_path(project:, location:, service:, metadata_import:) -> ::String

Create a fully-qualified MetadataImport resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/services/{service}/metadataImports/{metadata_import}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service** (String) 
  * **metadata_import** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #network_path
    
    
    def network_path(project:, network:) -> ::String

Create a fully-qualified Network resource string.

The resource will be in the following format:

`projects/{project}/global/networks/{network}`

**Parameters**

  * **project** (String) 
  * **network** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #service_path
    
    
    def service_path(project:, location:, service:) -> ::String

Create a fully-qualified Service resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/services/{service}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **service** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #subnetwork_path
    
    
    def subnetwork_path(project:, region:, subnetwork:) -> ::String

Create a fully-qualified Subnetwork resource string.

The resource will be in the following format:

`projects/{project}/regions/{region}/subnetworks/{subnetwork}`

**Parameters**

  * **project** (String) 
  * **region** (String) 
  * **subnetwork** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
