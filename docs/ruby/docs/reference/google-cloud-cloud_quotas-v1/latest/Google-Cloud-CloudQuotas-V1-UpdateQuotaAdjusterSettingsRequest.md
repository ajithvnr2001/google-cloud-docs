---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-UpdateQuotaAdjusterSettingsRequest/
title: Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::UpdateQuotaAdjusterSettingsRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:25.198472+00:00
---

# Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::UpdateQuotaAdjusterSettingsRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-UpdateQuotaAdjusterSettingsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::UpdateQuotaAdjusterSettingsRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.2  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.3.3  0.2.2  0.1.0 

Reference documentation and code samples for the Cloud Quotas V1 API class Google::Cloud::CloudQuotas::V1::UpdateQuotaAdjusterSettingsRequest.

Request for updating QuotaAdjusterSettings

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #quota_adjuster_settings
    
    
    def quota_adjuster_settings() -> ::Google::Cloud::CloudQuotas::V1::QuotaAdjusterSettings

**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::QuotaAdjusterSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaAdjusterSettings)) — Required. The QuotaAdjusterSettings to update. 



### #quota_adjuster_settings=
    
    
    def quota_adjuster_settings=(value) -> ::Google::Cloud::CloudQuotas::V1::QuotaAdjusterSettings

**Parameter**

  * **value** ([::Google::Cloud::CloudQuotas::V1::QuotaAdjusterSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaAdjusterSettings)) — Required. The QuotaAdjusterSettings to update. 



**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::QuotaAdjusterSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaAdjusterSettings)) — Required. The QuotaAdjusterSettings to update. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Protobuf-FieldMask)) — Optional. The list of fields to update. 



### #validate_only
    
    
    def validate_only() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. If set to true, checks the syntax of the request but doesn't update the quota adjuster settings value. Note that although a request can be valid, that doesn't guarantee that the request will be fulfilled. 



### #validate_only=
    
    
    def validate_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. If set to true, checks the syntax of the request but doesn't update the quota adjuster settings value. Note that although a request can be valid, that doesn't guarantee that the request will be fulfilled. 



**Returns**

  * (::Boolean) — Optional. If set to true, checks the syntax of the request but doesn't update the quota adjuster settings value. Note that although a request can be valid, that doesn't guarantee that the request will be fulfilled. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
