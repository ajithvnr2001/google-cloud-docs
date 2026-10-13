---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec/
title: Retail V2 API - Class Google::Cloud::Retail::V2::SearchRequest::BoostSpec (v2.10.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:30.323196+00:00
---

# Retail V2 API - Class Google::Cloud::Retail::V2::SearchRequest::BoostSpec (v2.10.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Retail V2 API - Class Google::Cloud::Retail::V2::SearchRequest::BoostSpec (v2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.10.0 (latest)  2.9.0  2.8.1  2.7.0  2.6.1  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.3.0  1.2.0  1.1.0  1.0.1  0.21.0  0.20.0  0.19.0  0.18.2  0.17.0  0.16.1  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Retail V2 API class Google::Cloud::Retail::V2::SearchRequest::BoostSpec.

Boost specification to boost certain items.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #condition_boost_specs
    
    
    def condition_boost_specs() -> ::Array<::Google::Cloud::Retail::V2::SearchRequest::BoostSpec::ConditionBoostSpec>

**Returns**

  * (::Array<[::Google::Cloud::Retail::V2::SearchRequest::BoostSpec::ConditionBoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec-ConditionBoostSpec)>) — Condition boost specifications. If a product matches multiple conditions in the specifications, boost scores from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 20. 



### #condition_boost_specs=
    
    
    def condition_boost_specs=(value) -> ::Array<::Google::Cloud::Retail::V2::SearchRequest::BoostSpec::ConditionBoostSpec>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Retail::V2::SearchRequest::BoostSpec::ConditionBoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec-ConditionBoostSpec)>) — Condition boost specifications. If a product matches multiple conditions in the specifications, boost scores from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 20. 



**Returns**

  * (::Array<[::Google::Cloud::Retail::V2::SearchRequest::BoostSpec::ConditionBoostSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec-ConditionBoostSpec)>) — Condition boost specifications. If a product matches multiple conditions in the specifications, boost scores from these specifications are all applied and combined in a non-linear way. Maximum number of specifications is 20. 



### #skip_boost_spec_validation
    
    
    def skip_boost_spec_validation() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to skip boostspec validation. If this field is set to true, invalid [BoostSpec.condition_boost_specs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec#Google__Cloud__Retail__V2__SearchRequest__BoostSpec_condition_boost_specs_instance_ "Google::Cloud::Retail::V2::SearchRequest::BoostSpec#condition_boost_specs \(method\)") will be ignored and valid [BoostSpec.condition_boost_specs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec#Google__Cloud__Retail__V2__SearchRequest__BoostSpec_condition_boost_specs_instance_ "Google::Cloud::Retail::V2::SearchRequest::BoostSpec#condition_boost_specs \(method\)") will still be applied. 



### #skip_boost_spec_validation=
    
    
    def skip_boost_spec_validation=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to skip boostspec validation. If this field is set to true, invalid [BoostSpec.condition_boost_specs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec#Google__Cloud__Retail__V2__SearchRequest__BoostSpec_condition_boost_specs_instance_ "Google::Cloud::Retail::V2::SearchRequest::BoostSpec#condition_boost_specs \(method\)") will be ignored and valid [BoostSpec.condition_boost_specs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec#Google__Cloud__Retail__V2__SearchRequest__BoostSpec_condition_boost_specs_instance_ "Google::Cloud::Retail::V2::SearchRequest::BoostSpec#condition_boost_specs \(method\)") will still be applied. 



**Returns**

  * (::Boolean) — Whether to skip boostspec validation. If this field is set to true, invalid [BoostSpec.condition_boost_specs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec#Google__Cloud__Retail__V2__SearchRequest__BoostSpec_condition_boost_specs_instance_ "Google::Cloud::Retail::V2::SearchRequest::BoostSpec#condition_boost_specs \(method\)") will be ignored and valid [BoostSpec.condition_boost_specs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-retail-v2/latest/Google-Cloud-Retail-V2-SearchRequest-BoostSpec#Google__Cloud__Retail__V2__SearchRequest__BoostSpec_condition_boost_specs_instance_ "Google::Cloud::Retail::V2::SearchRequest::BoostSpec#condition_boost_specs \(method\)") will still be applied. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
