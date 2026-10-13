---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint/
title: Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::Constraint (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:49.848441+00:00
---

# Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::Constraint (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Simulator V1 API - Class Google::Cloud::OrgPolicy::V2::Constraint (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.1 

Reference documentation and code samples for the Policy Simulator V1 API class Google::Cloud::OrgPolicy::V2::Constraint.

A constraint describes a way to restrict resource's configuration. For example, you could enforce a constraint that controls which Google Cloud services can be activated across an organization, or whether a Compute Engine instance can have serial port connections established. Constraints can be configured by the organization policy administrator to fit the needs of the organization by setting a policy that includes constraints at different locations in the organization's resource hierarchy. Policies are inherited down the resource hierarchy from higher levels, but can also be overridden. For details about the inheritance rules, see [`Policy`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Policy "Google::Cloud::OrgPolicy::V2::Policy \(class\)").

Constraints have a default behavior determined by the `constraint_default` field, which is the enforcement behavior that is used in the absence of a policy being defined or inherited for the resource in question.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #boolean_constraint
    
    
    def boolean_constraint() -> ::Google::Cloud::OrgPolicy::V2::Constraint::BooleanConstraint

**Returns**

  * ([::Google::Cloud::OrgPolicy::V2::Constraint::BooleanConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-BooleanConstraint)) — Defines this constraint as being a boolean constraint.

Note: The following fields are mutually exclusive: `boolean_constraint`, `list_constraint`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #boolean_constraint=
    
    
    def boolean_constraint=(value) -> ::Google::Cloud::OrgPolicy::V2::Constraint::BooleanConstraint

**Parameter**

  * **value** ([::Google::Cloud::OrgPolicy::V2::Constraint::BooleanConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-BooleanConstraint)) — Defines this constraint as being a boolean constraint.

Note: The following fields are mutually exclusive: `boolean_constraint`, `list_constraint`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OrgPolicy::V2::Constraint::BooleanConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-BooleanConstraint)) — Defines this constraint as being a boolean constraint.

Note: The following fields are mutually exclusive: `boolean_constraint`, `list_constraint`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #constraint_default
    
    
    def constraint_default() -> ::Google::Cloud::OrgPolicy::V2::Constraint::ConstraintDefault

**Returns**

  * ([::Google::Cloud::OrgPolicy::V2::Constraint::ConstraintDefault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-ConstraintDefault)) — The evaluation behavior of this constraint in the absence of a policy. 



### #constraint_default=
    
    
    def constraint_default=(value) -> ::Google::Cloud::OrgPolicy::V2::Constraint::ConstraintDefault

**Parameter**

  * **value** ([::Google::Cloud::OrgPolicy::V2::Constraint::ConstraintDefault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-ConstraintDefault)) — The evaluation behavior of this constraint in the absence of a policy. 



**Returns**

  * ([::Google::Cloud::OrgPolicy::V2::Constraint::ConstraintDefault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-ConstraintDefault)) — The evaluation behavior of this constraint in the absence of a policy. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — Detailed description of what this constraint controls as well as how and where it is enforced.

Mutable. 




### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — Detailed description of what this constraint controls as well as how and where it is enforced.

Mutable. 




**Returns**

  * (::String) — Detailed description of what this constraint controls as well as how and where it is enforced.

Mutable. 




### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The human readable name.

Mutable. 




### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The human readable name.

Mutable. 




**Returns**

  * (::String) — The human readable name.

Mutable. 




### #equivalent_constraint
    
    
    def equivalent_constraint() -> ::String

**Returns**

  * (::String) — Managed constraint and canned constraint sometimes can have equivalents. This field is used to store the equivalent constraint name. 



### #equivalent_constraint=
    
    
    def equivalent_constraint=(value) -> ::String

**Parameter**

  * **value** (::String) — Managed constraint and canned constraint sometimes can have equivalents. This field is used to store the equivalent constraint name. 



**Returns**

  * (::String) — Managed constraint and canned constraint sometimes can have equivalents. This field is used to store the equivalent constraint name. 



### #list_constraint
    
    
    def list_constraint() -> ::Google::Cloud::OrgPolicy::V2::Constraint::ListConstraint

**Returns**

  * ([::Google::Cloud::OrgPolicy::V2::Constraint::ListConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-ListConstraint)) — Defines this constraint as being a list constraint.

Note: The following fields are mutually exclusive: `list_constraint`, `boolean_constraint`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #list_constraint=
    
    
    def list_constraint=(value) -> ::Google::Cloud::OrgPolicy::V2::Constraint::ListConstraint

**Parameter**

  * **value** ([::Google::Cloud::OrgPolicy::V2::Constraint::ListConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-ListConstraint)) — Defines this constraint as being a list constraint.

Note: The following fields are mutually exclusive: `list_constraint`, `boolean_constraint`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::OrgPolicy::V2::Constraint::ListConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-OrgPolicy-V2-Constraint-ListConstraint)) — Defines this constraint as being a list constraint.

Note: The following fields are mutually exclusive: `list_constraint`, `boolean_constraint`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Immutable. The resource name of the constraint. Must be in one of the following forms:

    * `projects/{project_number}/constraints/{constraint_name}`
    * `folders/{folder_id}/constraints/{constraint_name}`
    * `organizations/{organization_id}/constraints/{constraint_name}`

For example, "/projects/123/constraints/compute.disableSerialPortAccess". 




### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Immutable. The resource name of the constraint. Must be in one of the following forms:

    * `projects/{project_number}/constraints/{constraint_name}`
    * `folders/{folder_id}/constraints/{constraint_name}`
    * `organizations/{organization_id}/constraints/{constraint_name}`

For example, "/projects/123/constraints/compute.disableSerialPortAccess". 




**Returns**

  * (::String) — Immutable. The resource name of the constraint. Must be in one of the following forms:

    * `projects/{project_number}/constraints/{constraint_name}`
    * `folders/{folder_id}/constraints/{constraint_name}`
    * `organizations/{organization_id}/constraints/{constraint_name}`

For example, "/projects/123/constraints/compute.disableSerialPortAccess". 




### #supports_dry_run
    
    
    def supports_dry_run() -> ::Boolean

**Returns**

  * (::Boolean) — Shows if dry run is supported for this constraint or not. 



### #supports_dry_run=
    
    
    def supports_dry_run=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Shows if dry run is supported for this constraint or not. 



**Returns**

  * (::Boolean) — Shows if dry run is supported for this constraint or not. 



### #supports_simulation
    
    
    def supports_simulation() -> ::Boolean

**Returns**

  * (::Boolean) — Shows if simulation is supported for this constraint or not. 



### #supports_simulation=
    
    
    def supports_simulation=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Shows if simulation is supported for this constraint or not. 



**Returns**

  * (::Boolean) — Shows if simulation is supported for this constraint or not. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
