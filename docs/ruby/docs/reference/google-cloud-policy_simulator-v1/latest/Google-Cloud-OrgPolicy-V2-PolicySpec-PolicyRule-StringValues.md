---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-PolicySpec-PolicyRule-StringValues/
title: Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::PolicySpec::PolicyRule::StringValues (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:06.937361+00:00
---

# Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::PolicySpec::PolicyRule::StringValues (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-PolicySpec-PolicyRule-StringValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::PolicySpec::PolicyRule::StringValues (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.1 

Reference documentation and code samples for the Policy Simulator V1 API class Google::Cloud::OrgPolicy::V2::PolicySpec::PolicyRule::StringValues.

A message that holds specific allowed and denied values. This message can define specific values and subtrees of the Resource Manager resource hierarchy (`Organizations`, `Folders`, `Projects`) that are allowed or denied. This is achieved by using the `under:` and optional `is:` prefixes. The `under:` prefix is used to denote resource subtree values. The `is:` prefix is used to denote specific values, and is required only if the value contains a ":". Values prefixed with "is:" are treated the same as values with no prefix. Ancestry subtrees must be in one of the following formats:

  * `projects/<project-id>` (for example, `projects/tokyo-rain-123`)
  * `folders/<folder-id>` (for example, `folders/1234`)
  * `organizations/<organization-id>` (for example, `organizations/1234`)



The `supports_under` field of the associated `Constraint` defines whether ancestry prefixes can be used.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #allowed_values
    
    
    def allowed_values() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — List of values allowed at this resource. 



### #allowed_values=
    
    
    def allowed_values=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — List of values allowed at this resource. 



**Returns**

  * (::Array<::String>) — List of values allowed at this resource. 



### #denied_values
    
    
    def denied_values() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — List of values denied at this resource. 



### #denied_values=
    
    
    def denied_values=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — List of values denied at this resource. 



**Returns**

  * (::Array<::String>) — List of values denied at this resource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
