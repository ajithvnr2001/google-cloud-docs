---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_kafka-v1/latest/Google-Cloud-ManagedKafka-V1-UpdateAclRequest/
title: Managed Service for Apache Kafka V1 API - Class Google::Cloud::ManagedKafka::V1::UpdateAclRequest (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:58.539040+00:00
---

# Managed Service for Apache Kafka V1 API - Class Google::Cloud::ManagedKafka::V1::UpdateAclRequest (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_kafka-v1/latest/Google-Cloud-ManagedKafka-V1-UpdateAclRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka V1 API - Class Google::Cloud::ManagedKafka::V1::UpdateAclRequest (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Managed Service for Apache Kafka V1 API class Google::Cloud::ManagedKafka::V1::UpdateAclRequest.

Request for UpdateAcl.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #acl
    
    
    def acl() -> ::Google::Cloud::ManagedKafka::V1::Acl

**Returns**

  * ([::Google::Cloud::ManagedKafka::V1::Acl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_kafka-v1/latest/Google-Cloud-ManagedKafka-V1-Acl)) — Required. The updated acl. Its `name` and `etag` fields must be populated. `acl_entries` must not be empty in the updated acl; to remove all acl entries for an acl, use DeleteAcl. 



### #acl=
    
    
    def acl=(value) -> ::Google::Cloud::ManagedKafka::V1::Acl

**Parameter**

  * **value** ([::Google::Cloud::ManagedKafka::V1::Acl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_kafka-v1/latest/Google-Cloud-ManagedKafka-V1-Acl)) — Required. The updated acl. Its `name` and `etag` fields must be populated. `acl_entries` must not be empty in the updated acl; to remove all acl entries for an acl, use DeleteAcl. 



**Returns**

  * ([::Google::Cloud::ManagedKafka::V1::Acl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_kafka-v1/latest/Google-Cloud-ManagedKafka-V1-Acl)) — Required. The updated acl. Its `name` and `etag` fields must be populated. `acl_entries` must not be empty in the updated acl; to remove all acl entries for an acl, use DeleteAcl. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_kafka-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the Acl resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_kafka-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the Acl resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-managed_kafka-v1/latest/Google-Protobuf-FieldMask)) — Optional. Field mask is used to specify the fields to be overwritten in the Acl resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
