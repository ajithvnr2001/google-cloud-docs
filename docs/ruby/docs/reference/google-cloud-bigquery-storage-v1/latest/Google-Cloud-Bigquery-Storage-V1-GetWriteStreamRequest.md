---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-GetWriteStreamRequest/
title: BigQuery Storage V1 API - Class Google::Cloud::Bigquery::Storage::V1::GetWriteStreamRequest (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:51.939898+00:00
---

# BigQuery Storage V1 API - Class Google::Cloud::Bigquery::Storage::V1::GetWriteStreamRequest (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-GetWriteStreamRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Storage V1 API - Class Google::Cloud::Bigquery::Storage::V1::GetWriteStreamRequest (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.27.0  0.26.0  0.25.2  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.1  0.9.2 

Reference documentation and code samples for the BigQuery Storage V1 API class Google::Cloud::Bigquery::Storage::V1::GetWriteStreamRequest.

Request message for `GetWriteStreamRequest`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Name of the stream to get, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the stream to get, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`. 



**Returns**

  * (::String) — Required. Name of the stream to get, in the form of `projects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}`. 



### #view
    
    
    def view() -> ::Google::Cloud::Bigquery::Storage::V1::WriteStreamView

**Returns**

  * ([::Google::Cloud::Bigquery::Storage::V1::WriteStreamView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStreamView)) — Indicates whether to get full or partial view of the WriteStream. If not set, view returned will be basic. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::Bigquery::Storage::V1::WriteStreamView

**Parameter**

  * **value** ([::Google::Cloud::Bigquery::Storage::V1::WriteStreamView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStreamView)) — Indicates whether to get full or partial view of the WriteStream. If not set, view returned will be basic. 



**Returns**

  * ([::Google::Cloud::Bigquery::Storage::V1::WriteStreamView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-storage-v1/latest/Google-Cloud-Bigquery-Storage-V1-WriteStreamView)) — Indicates whether to get full or partial view of the WriteStream. If not set, view returned will be basic. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
