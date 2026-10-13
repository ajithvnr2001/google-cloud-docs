---
url: https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeter/
title: Access Context Manager V1 API - Class Google::Identity::AccessContextManager::V1::ServicePerimeter (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:05.978832+00:00
---

# Access Context Manager V1 API - Class Google::Identity::AccessContextManager::V1::ServicePerimeter (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Access Context Manager V1 API - Class Google::Identity::AccessContextManager::V1::ServicePerimeter (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.1  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.2  0.7.2  0.6.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Access Context Manager V1 API class Google::Identity::AccessContextManager::V1::ServicePerimeter.

`ServicePerimeter` describes a set of Google Cloud resources which can freely import and export data amongst themselves, but not export outside of the `ServicePerimeter`. If a request with a source within this `ServicePerimeter` has a target outside of the `ServicePerimeter`, the request will be blocked. Otherwise the request is allowed. There are two types of Service Perimeter - Regular and Bridge. Regular Service Perimeters cannot overlap, a single Google Cloud project can only belong to a single regular Service Perimeter. Service Perimeter Bridges can contain only Google Cloud projects as members, a single Google Cloud project may belong to multiple Service Perimeter Bridges.

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

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the `ServicePerimeter` was created in UTC. 



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the `ServicePerimeter` was created in UTC. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the `ServicePerimeter` was created in UTC. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Description of the `ServicePerimeter` and its use. Does not affect behavior. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Description of the `ServicePerimeter` and its use. Does not affect behavior. 



**Returns**

  * (::String) — Description of the `ServicePerimeter` and its use. Does not affect behavior. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Resource name for the ServicePerimeter. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Resource name for the ServicePerimeter. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}`



**Returns**

  * (::String) — Required. Resource name for the ServicePerimeter. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}`



### #perimeter_type
    
    
    def perimeter_type() -> ::Google::Identity::AccessContextManager::V1::ServicePerimeter::PerimeterType

**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeter::PerimeterType](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeter-PerimeterType)) — Perimeter type indicator. A single project is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty. 



### #perimeter_type=
    
    
    def perimeter_type=(value) -> ::Google::Identity::AccessContextManager::V1::ServicePerimeter::PerimeterType

**Parameter**

  * **value** ([::Google::Identity::AccessContextManager::V1::ServicePerimeter::PerimeterType](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeter-PerimeterType)) — Perimeter type indicator. A single project is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty. 



**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeter::PerimeterType](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeter-PerimeterType)) — Perimeter type indicator. A single project is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty. 



### #spec
    
    
    def spec() -> ::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig

**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig)) — Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "use_explicit_dry_run_spec" flag is set. 



### #spec=
    
    
    def spec=(value) -> ::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig

**Parameter**

  * **value** ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig)) — Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "use_explicit_dry_run_spec" flag is set. 



**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig)) — Proposed (or dry run) ServicePerimeter configuration. This configuration allows to specify and test ServicePerimeter configuration without enforcing actual access restrictions. Only allowed to be set when the "use_explicit_dry_run_spec" flag is set. 



### #status
    
    
    def status() -> ::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig

**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig)) — Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries. 



### #status=
    
    
    def status=(value) -> ::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig

**Parameter**

  * **value** ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig)) — Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries. 



**Returns**

  * ([::Google::Identity::AccessContextManager::V1::ServicePerimeterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Identity-AccessContextManager-V1-ServicePerimeterConfig)) — Current ServicePerimeter configuration. Specifies sets of resources, restricted services and access levels that determine perimeter content and boundaries. 



### #title
    
    
    def title() -> ::String

**Returns**

  * (::String) — Human readable title. Must be unique within the Policy. 



### #title=
    
    
    def title=(value) -> ::String

**Parameter**

  * **value** (::String) — Human readable title. Must be unique within the Policy. 



**Returns**

  * (::String) — Human readable title. Must be unique within the Policy. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the `ServicePerimeter` was updated in UTC. 



### #update_time=
    
    
    def update_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the `ServicePerimeter` was updated in UTC. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-identity-access_context_manager-v1/latest/Google-Protobuf-Timestamp)) — Output only. Time the `ServicePerimeter` was updated in UTC. 



### #use_explicit_dry_run_spec
    
    
    def use_explicit_dry_run_spec() -> ::Boolean

**Returns**

  * (::Boolean) — Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values. 



### #use_explicit_dry_run_spec=
    
    
    def use_explicit_dry_run_spec=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values. 



**Returns**

  * (::Boolean) — Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration ("spec") to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config ("status") without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
