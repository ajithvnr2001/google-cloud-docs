---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType/
title: Dataplex V1 API - Class Google::Cloud::Dataplex::V1::AspectType (v2.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:54.981649+00:00
---

# Dataplex V1 API - Class Google::Cloud::Dataplex::V1::AspectType (v2.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataplex V1 API - Class Google::Cloud::Dataplex::V1::AspectType (v2.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.1 (latest)  2.10.0  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.2  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.1  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Dataplex V1 API class Google::Cloud::Dataplex::V1::AspectType.

AspectType is a template for creating Aspects, and represents the JSON-schema for a given Entry, for example, BigQuery Table Schema.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #authorization
    
    
    def authorization() -> ::Google::Cloud::Dataplex::V1::AspectType::Authorization

**Returns**

  * ([::Google::Cloud::Dataplex::V1::AspectType::Authorization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-Authorization)) — Immutable. Defines the Authorization for this type. 



### #authorization=
    
    
    def authorization=(value) -> ::Google::Cloud::Dataplex::V1::AspectType::Authorization

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::AspectType::Authorization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-Authorization)) — Immutable. Defines the Authorization for this type. 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::AspectType::Authorization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-Authorization)) — Immutable. Defines the Authorization for this type. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the AspectType was created. 



### #data_classification
    
    
    def data_classification() -> ::Google::Cloud::Dataplex::V1::AspectType::DataClassification

**Returns**

  * ([::Google::Cloud::Dataplex::V1::AspectType::DataClassification](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-DataClassification)) — Optional. Immutable. Stores data classification of the aspect. 



### #data_classification=
    
    
    def data_classification=(value) -> ::Google::Cloud::Dataplex::V1::AspectType::DataClassification

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::AspectType::DataClassification](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-DataClassification)) — Optional. Immutable. Stores data classification of the aspect. 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::AspectType::DataClassification](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-DataClassification)) — Optional. Immutable. Stores data classification of the aspect. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Optional. Description of the AspectType. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Description of the AspectType. 



**Returns**

  * (::String) — Optional. Description of the AspectType. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Optional. User friendly display name. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. User friendly display name. 



**Returns**

  * (::String) — Optional. User friendly display name. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — The service computes this checksum. The client may send it on update and delete requests to ensure it has an up-to-date value before proceeding. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — The service computes this checksum. The client may send it on update and delete requests to ensure it has an up-to-date value before proceeding. 



**Returns**

  * (::String) — The service computes this checksum. The client may send it on update and delete requests to ensure it has an up-to-date value before proceeding. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User-defined labels for the AspectType. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. User-defined labels for the AspectType. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User-defined labels for the AspectType. 



### #metadata_template
    
    
    def metadata_template() -> ::Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate

**Returns**

  * ([::Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-MetadataTemplate)) — Required. MetadataTemplate of the aspect. 



### #metadata_template=
    
    
    def metadata_template=(value) -> ::Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate

**Parameter**

  * **value** ([::Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-MetadataTemplate)) — Required. MetadataTemplate of the aspect. 



**Returns**

  * ([::Google::Cloud::Dataplex::V1::AspectType::MetadataTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-AspectType-MetadataTemplate)) — Required. MetadataTemplate of the aspect. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The relative resource name of the AspectType, of the form: projects/{project_number}/locations/{location_id}/aspectTypes/{aspect_type_id}. 



### #transfer_status
    
    
    def transfer_status() -> ::Google::Cloud::Dataplex::V1::TransferStatus

**Returns**

  * ([::Google::Cloud::Dataplex::V1::TransferStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Cloud-Dataplex-V1-TransferStatus)) — Output only. Denotes the transfer status of the Aspect Type. It is unspecified for Aspect Types created from Dataplex API. 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. System generated globally unique ID for the AspectType. If you delete and recreate the AspectType with the same name, then this ID will be different. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex-v1/latest/Google-Protobuf-Timestamp)) — Output only. The time when the AspectType was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
