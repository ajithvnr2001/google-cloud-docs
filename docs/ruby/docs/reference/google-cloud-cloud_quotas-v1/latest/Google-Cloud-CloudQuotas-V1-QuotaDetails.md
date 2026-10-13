---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaDetails/
title: Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::QuotaDetails (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:02.657006+00:00
---

# Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::QuotaDetails (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-QuotaDetails/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Quotas V1 API - Class Google::Cloud::CloudQuotas::V1::QuotaDetails (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.0  2.2.2  2.1.0  2.0.1  1.3.0  1.2.0  1.1.0  1.0.1  0.3.3  0.2.2  0.1.0 

Reference documentation and code samples for the Cloud Quotas V1 API class Google::Cloud::CloudQuotas::V1::QuotaDetails.

The quota details for a map of dimensions.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #rollout_info
    
    
    def rollout_info() -> ::Google::Cloud::CloudQuotas::V1::RolloutInfo

**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::RolloutInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-RolloutInfo)) — Rollout information of this quota. This field is present only if the effective limit will change due to the ongoing rollout of the service config. 



### #rollout_info=
    
    
    def rollout_info=(value) -> ::Google::Cloud::CloudQuotas::V1::RolloutInfo

**Parameter**

  * **value** ([::Google::Cloud::CloudQuotas::V1::RolloutInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-RolloutInfo)) — Rollout information of this quota. This field is present only if the effective limit will change due to the ongoing rollout of the service config. 



**Returns**

  * ([::Google::Cloud::CloudQuotas::V1::RolloutInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_quotas-v1/latest/Google-Cloud-CloudQuotas-V1-RolloutInfo)) — Rollout information of this quota. This field is present only if the effective limit will change due to the ongoing rollout of the service config. 



### #value
    
    
    def value() -> ::Integer

**Returns**

  * (::Integer) — The value currently in effect and being enforced. 



### #value=
    
    
    def value=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The value currently in effect and being enforced. 



**Returns**

  * (::Integer) — The value currently in effect and being enforced. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
