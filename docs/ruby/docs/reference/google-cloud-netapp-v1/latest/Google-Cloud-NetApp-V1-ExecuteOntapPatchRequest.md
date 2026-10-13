---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapPatchRequest/
title: NetApp V1 API - Class Google::Cloud::NetApp::V1::ExecuteOntapPatchRequest (v2.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:04.038544+00:00
---

# NetApp V1 API - Class Google::Cloud::NetApp::V1::ExecuteOntapPatchRequest (v2.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Cloud-NetApp-V1-ExecuteOntapPatchRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  NetApp V1 API - Class Google::Cloud::NetApp::V1::ExecuteOntapPatchRequest (v2.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.2 (latest)  2.12.1  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.2  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.6.0  0.5.2  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the NetApp V1 API class Google::Cloud::NetApp::V1::ExecuteOntapPatchRequest.

Request message for `ExecuteOntapPatch` API.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #body
    
    
    def body() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Protobuf-Struct)) — Required. The raw `JSON` body of the request. The body should be in the format of the ONTAP resource. For example: ` { "body": { "field1": "value1", "field2": "value2", } } `



### #body=
    
    
    def body=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Protobuf-Struct)) — Required. The raw `JSON` body of the request. The body should be in the format of the ONTAP resource. For example: ` { "body": { "field1": "value1", "field2": "value2", } } `



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-netapp-v1/latest/Google-Protobuf-Struct)) — Required. The raw `JSON` body of the request. The body should be in the format of the ONTAP resource. For example: ` { "body": { "field1": "value1", "field2": "value2", } } `



### #ontap_path
    
    
    def ontap_path() -> ::String

**Returns**

  * (::String) — Required. The resource path of the ONTAP resource. Format: `projects/{project_number}/locations/{location_id}/storagePools/{storage_pool_id}/ontap/{ontap_resource_path}`. For example: `projects/123456789/locations/us-central1/storagePools/my-storage-pool/ontap/api/storage/volumes`. 



### #ontap_path=
    
    
    def ontap_path=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource path of the ONTAP resource. Format: `projects/{project_number}/locations/{location_id}/storagePools/{storage_pool_id}/ontap/{ontap_resource_path}`. For example: `projects/123456789/locations/us-central1/storagePools/my-storage-pool/ontap/api/storage/volumes`. 



**Returns**

  * (::String) — Required. The resource path of the ONTAP resource. Format: `projects/{project_number}/locations/{location_id}/storagePools/{storage_pool_id}/ontap/{ontap_resource_path}`. For example: `projects/123456789/locations/us-central1/storagePools/my-storage-pool/ontap/api/storage/volumes`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
