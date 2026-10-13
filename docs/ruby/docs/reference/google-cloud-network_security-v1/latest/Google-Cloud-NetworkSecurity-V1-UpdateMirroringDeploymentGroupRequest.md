---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateMirroringDeploymentGroupRequest/
title: Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::UpdateMirroringDeploymentGroupRequest (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:34.785343+00:00
---

# Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::UpdateMirroringDeploymentGroupRequest (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-UpdateMirroringDeploymentGroupRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Security V1 API - Class Google::Cloud::NetworkSecurity::V1::UpdateMirroringDeploymentGroupRequest (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Network Security V1 API class Google::Cloud::NetworkSecurity::V1::UpdateMirroringDeploymentGroupRequest.

Request message for UpdateMirroringDeploymentGroup.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #mirroring_deployment_group
    
    
    def mirroring_deployment_group() -> ::Google::Cloud::NetworkSecurity::V1::MirroringDeploymentGroup

**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::MirroringDeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-MirroringDeploymentGroup)) — Required. The deployment group to update. 



### #mirroring_deployment_group=
    
    
    def mirroring_deployment_group=(value) -> ::Google::Cloud::NetworkSecurity::V1::MirroringDeploymentGroup

**Parameter**

  * **value** ([::Google::Cloud::NetworkSecurity::V1::MirroringDeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-MirroringDeploymentGroup)) — Required. The deployment group to update. 



**Returns**

  * ([::Google::Cloud::NetworkSecurity::V1::MirroringDeploymentGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Cloud-NetworkSecurity-V1-MirroringDeploymentGroup)) — Required. The deployment group to update. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A unique identifier for this request. Must be a UUID4. This request is only idempotent if a `request_id` is provided. See https://google.aip.dev/155 for more details. 



### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A unique identifier for this request. Must be a UUID4. This request is only idempotent if a `request_id` is provided. See https://google.aip.dev/155 for more details. 



**Returns**

  * (::String) — Optional. A unique identifier for this request. Must be a UUID4. This request is only idempotent if a `request_id` is provided. See https://google.aip.dev/155 for more details. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. Fields are specified relative to the deployment group (e.g. `description`; _not_ `mirroring_deployment_group.description`). See https://google.aip.dev/161 for more details. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. Fields are specified relative to the deployment group (e.g. `description`; _not_ `mirroring_deployment_group.description`). See https://google.aip.dev/161 for more details. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_security-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. Fields are specified relative to the deployment group (e.g. `description`; _not_ `mirroring_deployment_group.description`). See https://google.aip.dev/161 for more details. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
