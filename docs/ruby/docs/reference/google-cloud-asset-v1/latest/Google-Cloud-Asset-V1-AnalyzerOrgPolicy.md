---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy/
title: Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AnalyzerOrgPolicy (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:58.384337+00:00
---

# Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AnalyzerOrgPolicy (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AnalyzerOrgPolicy (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.2  0.32.0  0.31.0  0.30.0  0.29.3  0.28.1  0.27.0  0.26.1  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.1  0.19.0  0.18.0  0.17.3 

Reference documentation and code samples for the Cloud Asset V1 API class Google::Cloud::Asset::V1::AnalyzerOrgPolicy.

This organization policy message is a modified version of the one defined in the Organization Policy system. This message contains several fields defined in the original organization policy with some new fields for analysis purpose.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #applied_resource
    
    
    def applied_resource() -> ::String

**Returns**

  * (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy applies to.

For any user defined org policies, this field has the same value as the [attached_resource] field. Only for default policy, this field has the different value. 




### #applied_resource=
    
    
    def applied_resource=(value) -> ::String

**Parameter**

  * **value** (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy applies to.

For any user defined org policies, this field has the same value as the [attached_resource] field. Only for default policy, this field has the different value. 




**Returns**

  * (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy applies to.

For any user defined org policies, this field has the same value as the [attached_resource] field. Only for default policy, this field has the different value. 




### #attached_resource
    
    
    def attached_resource() -> ::String

**Returns**

  * (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy is set.

Notice that some type of constraints are defined with default policy. This field will be empty for them. 




### #attached_resource=
    
    
    def attached_resource=(value) -> ::String

**Parameter**

  * **value** (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy is set.

Notice that some type of constraints are defined with default policy. This field will be empty for them. 




**Returns**

  * (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource where this organization policy is set.

Notice that some type of constraints are defined with default policy. This field will be empty for them. 




### #inherit_from_parent
    
    
    def inherit_from_parent() -> ::Boolean

**Returns**

  * (::Boolean) — If `inherit_from_parent` is true, Rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the effective root for evaluation. 



### #inherit_from_parent=
    
    
    def inherit_from_parent=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If `inherit_from_parent` is true, Rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the effective root for evaluation. 



**Returns**

  * (::Boolean) — If `inherit_from_parent` is true, Rules set higher up in the hierarchy (up to the closest root) are inherited and present in the effective policy. If it is false, then no rules are inherited, and this policy becomes the effective root for evaluation. 



### #reset
    
    
    def reset() -> ::Boolean

**Returns**

  * (::Boolean) — Ignores policies set above this resource and restores the default behavior of the constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false. 



### #reset=
    
    
    def reset=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Ignores policies set above this resource and restores the default behavior of the constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false. 



**Returns**

  * (::Boolean) — Ignores policies set above this resource and restores the default behavior of the constraint at this resource. This field can be set in policies for either list or boolean constraints. If set, `rules` must be empty and `inherit_from_parent` must be set to false. 



### #rules
    
    
    def rules() -> ::Array<::Google::Cloud::Asset::V1::AnalyzerOrgPolicy::Rule>

**Returns**

  * (::Array<[::Google::Cloud::Asset::V1::AnalyzerOrgPolicy::Rule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy-Rule)>) — List of rules for this organization policy. 



### #rules=
    
    
    def rules=(value) -> ::Array<::Google::Cloud::Asset::V1::AnalyzerOrgPolicy::Rule>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Asset::V1::AnalyzerOrgPolicy::Rule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy-Rule)>) — List of rules for this organization policy. 



**Returns**

  * (::Array<[::Google::Cloud::Asset::V1::AnalyzerOrgPolicy::Rule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy-Rule)>) — List of rules for this organization policy. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
