---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Partner/
title: Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::Partner (v2.4.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:30.102828+00:00
---

# Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::Partner (v2.4.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Partner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Controls Partner V1 API - Class Google::Cloud::CloudControlsPartner::V1::Partner (v2.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.1 (latest)  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.1.1 

Reference documentation and code samples for the Cloud Controls Partner V1 API class Google::Cloud::CloudControlsPartner::V1::Partner.

Message describing Partner resource

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the resource was created 



### #ekm_solutions
    
    
    def ekm_solutions() -> ::Array<::Google::Cloud::CloudControlsPartner::V1::EkmMetadata>

**Returns**

  * (::Array<[::Google::Cloud::CloudControlsPartner::V1::EkmMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-EkmMetadata)>) — List of Google Cloud supported EKM partners supported by the partner 



### #ekm_solutions=
    
    
    def ekm_solutions=(value) -> ::Array<::Google::Cloud::CloudControlsPartner::V1::EkmMetadata>

**Parameter**

  * **value** (::Array<[::Google::Cloud::CloudControlsPartner::V1::EkmMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-EkmMetadata)>) — List of Google Cloud supported EKM partners supported by the partner 



**Returns**

  * (::Array<[::Google::Cloud::CloudControlsPartner::V1::EkmMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-EkmMetadata)>) — List of Google Cloud supported EKM partners supported by the partner 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Identifier. The resource name of the partner. Format: `organizations/{organization}/locations/{location}/partner` Example: "organizations/123456/locations/us-central1/partner" 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier. The resource name of the partner. Format: `organizations/{organization}/locations/{location}/partner` Example: "organizations/123456/locations/us-central1/partner" 



**Returns**

  * (::String) — Identifier. The resource name of the partner. Format: `organizations/{organization}/locations/{location}/partner` Example: "organizations/123456/locations/us-central1/partner" 



### #operated_cloud_regions
    
    
    def operated_cloud_regions() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — List of Google Cloud regions that the partner sells services to customers. Valid Google Cloud regions found here: https://cloud.google.com/compute/docs/regions-zones 



### #operated_cloud_regions=
    
    
    def operated_cloud_regions=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — List of Google Cloud regions that the partner sells services to customers. Valid Google Cloud regions found here: https://cloud.google.com/compute/docs/regions-zones 



**Returns**

  * (::Array<::String>) — List of Google Cloud regions that the partner sells services to customers. Valid Google Cloud regions found here: https://cloud.google.com/compute/docs/regions-zones 



### #partner_project_id
    
    
    def partner_project_id() -> ::String

**Returns**

  * (::String) — Google Cloud project ID in the partner's Google Cloud organization for receiving enhanced Logs for Partners. 



### #partner_project_id=
    
    
    def partner_project_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Google Cloud project ID in the partner's Google Cloud organization for receiving enhanced Logs for Partners. 



**Returns**

  * (::String) — Google Cloud project ID in the partner's Google Cloud organization for receiving enhanced Logs for Partners. 



### #skus
    
    
    def skus() -> ::Array<::Google::Cloud::CloudControlsPartner::V1::Sku>

**Returns**

  * (::Array<[::Google::Cloud::CloudControlsPartner::V1::Sku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Sku)>) — List of SKUs the partner is offering 



### #skus=
    
    
    def skus=(value) -> ::Array<::Google::Cloud::CloudControlsPartner::V1::Sku>

**Parameter**

  * **value** (::Array<[::Google::Cloud::CloudControlsPartner::V1::Sku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Sku)>) — List of SKUs the partner is offering 



**Returns**

  * (::Array<[::Google::Cloud::CloudControlsPartner::V1::Sku](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Cloud-CloudControlsPartner-V1-Sku)>) — List of SKUs the partner is offering 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1/latest/Google-Protobuf-Timestamp)) — Output only. The last time the resource was updated 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
