---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-UpdateClusterRequest/
title: Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::UpdateClusterRequest (v1.5.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:22.643325+00:00
---

# Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::UpdateClusterRequest (v1.5.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-UpdateClusterRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Container V1 API - Class Google::Cloud::EdgeContainer::V1::UpdateClusterRequest (v1.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.2 (latest)  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.4.0  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Distributed Cloud Edge Container V1 API class Google::Cloud::EdgeContainer::V1::UpdateClusterRequest.

Updates a cluster.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cluster
    
    
    def cluster() -> ::Google::Cloud::EdgeContainer::V1::Cluster

**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-Cluster)) — The updated cluster. 



### #cluster=
    
    
    def cluster=(value) -> ::Google::Cloud::EdgeContainer::V1::Cluster

**Parameter**

  * **value** ([::Google::Cloud::EdgeContainer::V1::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-Cluster)) — The updated cluster. 



**Returns**

  * ([::Google::Cloud::EdgeContainer::V1::Cluster](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Cloud-EdgeContainer-V1-Cluster)) — The updated cluster. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided. 



### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided. 



**Returns**

  * (::String) — A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if `request_id` is provided. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_container-v1/latest/Google-Protobuf-FieldMask)) — Field mask is used to specify the fields to be overwritten in the Cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
