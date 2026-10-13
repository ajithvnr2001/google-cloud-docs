---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaIncreaseEligibility/
title: Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:01.664916+00:00
---

# Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaIncreaseEligibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.2  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.3.3  0.2.2  0.1.0 

Reference documentation and code samples for the Cloud Quotas V1 API class Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility.

Eligibility information regarding requesting increase adjustment of a quota.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ineligibility_reason
    
    
    def ineligibility_reason() -> ::Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility::IneligibilityReason

**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility::IneligibilityReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaIncreaseEligibility-IneligibilityReason)) — The reason of why it is ineligible to request increased value of the quota. If the is_eligible field is true, it defaults to INELIGIBILITY_REASON_UNSPECIFIED. 



### #ineligibility_reason=
    
    
    def ineligibility_reason=(value) -> ::Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility::IneligibilityReason

**Parameter**

  * **value** ([::Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility::IneligibilityReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaIncreaseEligibility-IneligibilityReason)) — The reason of why it is ineligible to request increased value of the quota. If the is_eligible field is true, it defaults to INELIGIBILITY_REASON_UNSPECIFIED. 



**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::QuotaIncreaseEligibility::IneligibilityReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaIncreaseEligibility-IneligibilityReason)) — The reason of why it is ineligible to request increased value of the quota. If the is_eligible field is true, it defaults to INELIGIBILITY_REASON_UNSPECIFIED. 



### #is_eligible
    
    
    def is_eligible() -> ::Boolean

**Returns**

  * (::Boolean) — Whether a higher quota value can be requested for the quota. 



### #is_eligible=
    
    
    def is_eligible=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether a higher quota value can be requested for the quota. 



**Returns**

  * (::Boolean) — Whether a higher quota value can be requested for the quota. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
