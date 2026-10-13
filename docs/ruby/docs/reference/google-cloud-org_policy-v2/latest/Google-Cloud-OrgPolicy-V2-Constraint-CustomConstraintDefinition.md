---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition/
title: Organization Policy V2 API - Class Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:38.769069+00:00
---

# Organization Policy V2 API - Class Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Organization Policy V2 API - Class Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.6 

Reference documentation and code samples for the Organization Policy V2 API class Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition.

Custom constraint definition. Defines this as a managed constraint.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #action_type
    
    
    def action_type() -> ::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::ActionType

**Returns**

  * ([::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::ActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-ActionType)) — Allow or deny type. 



### #action_type=
    
    
    def action_type=(value) -> ::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::ActionType

**Parameter**

  * **value** ([::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::ActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-ActionType)) — Allow or deny type. 



**Returns**

  * ([::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::ActionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-ActionType)) — Allow or deny type. 



### #condition
    
    
    def condition() -> ::String

**Returns**

  * (::String) — Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true`

The max length of the condition is 1000 characters. 




### #condition=
    
    
    def condition=(value) -> ::String

**Parameter**

  * **value** (::String) — Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true`

The max length of the condition is 1000 characters. 




**Returns**

  * (::String) — Org policy condition/expression. For example: `resource.instanceName.matches("[production|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true`

The max length of the condition is 1000 characters. 




### #method_types
    
    
    def method_types() -> ::Array<::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::MethodType>

**Returns**

  * (::Array<[::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::MethodType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-MethodType)>) — All the operations being applied for this constraint. 



### #method_types=
    
    
    def method_types=(value) -> ::Array<::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::MethodType>

**Parameter**

  * **value** (::Array<[::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::MethodType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-MethodType)>) — All the operations being applied for this constraint. 



**Returns**

  * (::Array<[::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::MethodType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-MethodType)>) — All the operations being applied for this constraint. 



### #parameters
    
    
    def parameters() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::Parameter}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::Parameter}) — Stores the structure of [`Parameters`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-Parameter "Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::Parameter \(class\)") used by the constraint condition. The key of `map` represents the name of the parameter. 



### #parameters=
    
    
    def parameters=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::Parameter}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::Parameter}) — Stores the structure of [`Parameters`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-Parameter "Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::Parameter \(class\)") used by the constraint condition. The key of `map` represents the name of the parameter. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::Parameter}) — Stores the structure of [`Parameters`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-org_policy-v2/latest/Google-Cloud-OrgPolicy-V2-Constraint-CustomConstraintDefinition-Parameter "Google::Cloud::OrgPolicy::V2::Constraint::CustomConstraintDefinition::Parameter \(class\)") used by the constraint condition. The key of `map` represents the name of the parameter. 



### #resource_types
    
    
    def resource_types() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — 

The resource instance type on which this policy applies. Format will be of the form : `<service name>/<type>` Example:

    * `compute.googleapis.com/Instance`.



### #resource_types=
    
    
    def resource_types=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — 

The resource instance type on which this policy applies. Format will be of the form : `<service name>/<type>` Example:

    * `compute.googleapis.com/Instance`.



**Returns**

  * (::Array<::String>) — 

The resource instance type on which this policy applies. Format will be of the form : `<service name>/<type>` Example:

    * `compute.googleapis.com/Instance`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
