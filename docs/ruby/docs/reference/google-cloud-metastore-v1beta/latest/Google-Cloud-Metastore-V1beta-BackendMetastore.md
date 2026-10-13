---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-BackendMetastore/
title: Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::BackendMetastore (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:26.914349+00:00
---

# Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::BackendMetastore (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-BackendMetastore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::BackendMetastore (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Dataproc Metastore V1beta API class Google::Cloud::Metastore::V1beta::BackendMetastore.

Represents a backend metastore for the federation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #metastore_type
    
    
    def metastore_type() -> ::Google::Cloud::Metastore::V1beta::BackendMetastore::MetastoreType

**Returns**

  * ([::Google::Cloud::Metastore::V1beta::BackendMetastore::MetastoreType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-BackendMetastore-MetastoreType)) — The type of the backend metastore. 



### #metastore_type=
    
    
    def metastore_type=(value) -> ::Google::Cloud::Metastore::V1beta::BackendMetastore::MetastoreType

**Parameter**

  * **value** ([::Google::Cloud::Metastore::V1beta::BackendMetastore::MetastoreType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-BackendMetastore-MetastoreType)) — The type of the backend metastore. 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::BackendMetastore::MetastoreType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-BackendMetastore-MetastoreType)) — The type of the backend metastore. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — 

The relative resource name of the metastore that is being federated. The formats of the relative resource names for the currently supported metastores are listed below:

    * BigQuery 
      * `projects/{project_id}`
    * Dataproc Metastore 
      * `projects/{project_id}/locations/{location}/services/{service_id}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The relative resource name of the metastore that is being federated. The formats of the relative resource names for the currently supported metastores are listed below:

    * BigQuery 
      * `projects/{project_id}`
    * Dataproc Metastore 
      * `projects/{project_id}/locations/{location}/services/{service_id}`



**Returns**

  * (::String) — 

The relative resource name of the metastore that is being federated. The formats of the relative resource names for the currently supported metastores are listed below:

    * BigQuery 
      * `projects/{project_id}`
    * Dataproc Metastore 
      * `projects/{project_id}/locations/{location}/services/{service_id}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
