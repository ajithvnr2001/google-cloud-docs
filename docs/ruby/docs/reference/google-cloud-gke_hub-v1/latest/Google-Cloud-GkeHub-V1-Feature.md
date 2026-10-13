---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-Feature/
title: GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::Feature (v2.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:53.823245+00:00
---

# GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::Feature (v2.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-Feature/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::Feature (v2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.10.0  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the GKE Hub V1 API class Google::Cloud::GkeHub::V1::Feature.

Feature represents the settings and status of any Fleet Feature.

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

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Protobuf-Timestamp)) — Output only. When the Feature resource was created. 



### #delete_time
    
    
    def delete_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Protobuf-Timestamp)) — Output only. When the Feature resource was deleted. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels for this Feature. 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels for this Feature. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels for this Feature. 



### #membership_specs
    
    
    def membership_specs() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::MembershipFeatureSpec}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::MembershipFeatureSpec}) — Optional. Membership-specific configuration for this Feature. If this Feature does not support any per-Membership configuration, this field may be unused.

The keys indicate which Membership the configuration is for, in the form:

`projects/{p}/locations/{l}/memberships/{m}`

Where {p} is the project, {l} is a valid location and {m} is a valid Membership in this project at that location. {p} WILL match the Feature's project.

{p} will always be returned as the project number, but the project ID is also accepted during input. If the same Membership is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. 




### #membership_specs=
    
    
    def membership_specs=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::MembershipFeatureSpec}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::MembershipFeatureSpec}) — Optional. Membership-specific configuration for this Feature. If this Feature does not support any per-Membership configuration, this field may be unused.

The keys indicate which Membership the configuration is for, in the form:

`projects/{p}/locations/{l}/memberships/{m}`

Where {p} is the project, {l} is a valid location and {m} is a valid Membership in this project at that location. {p} WILL match the Feature's project.

{p} will always be returned as the project number, but the project ID is also accepted during input. If the same Membership is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::MembershipFeatureSpec}) — Optional. Membership-specific configuration for this Feature. If this Feature does not support any per-Membership configuration, this field may be unused.

The keys indicate which Membership the configuration is for, in the form:

`projects/{p}/locations/{l}/memberships/{m}`

Where {p} is the project, {l} is a valid location and {m} is a valid Membership in this project at that location. {p} WILL match the Feature's project.

{p} will always be returned as the project number, but the project ID is also accepted during input. If the same Membership is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. 




### #membership_states
    
    
    def membership_states() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::MembershipFeatureState}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::MembershipFeatureState}) — Output only. Membership-specific Feature status. If this Feature does report any per-Membership status, this field may be unused.

The keys indicate which Membership the state is for, in the form:

`projects/{p}/locations/{l}/memberships/{m}`

Where {p} is the project number, {l} is a valid location and {m} is a valid Membership in this project at that location. {p} MUST match the Feature's project number. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The full, unique name of this Feature resource in the format `projects/*/locations/*/features/*`. 



### #resource_state
    
    
    def resource_state() -> ::Google::Cloud::GkeHub::V1::FeatureResourceState

**Returns**

  * ([::Google::Cloud::GkeHub::V1::FeatureResourceState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-FeatureResourceState)) — Output only. State of the Feature resource itself. 



### #scope_specs
    
    
    def scope_specs() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::ScopeFeatureSpec}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::ScopeFeatureSpec}) — Optional. Scope-specific configuration for this Feature. If this Feature does not support any per-Scope configuration, this field may be unused.

The keys indicate which Scope the configuration is for, in the form:

`projects/{p}/locations/global/scopes/{s}`

Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature's project.

{p} will always be returned as the project number, but the project ID is also accepted during input. If the same Scope is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. 




### #scope_specs=
    
    
    def scope_specs=(value) -> ::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::ScopeFeatureSpec}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::ScopeFeatureSpec}) — Optional. Scope-specific configuration for this Feature. If this Feature does not support any per-Scope configuration, this field may be unused.

The keys indicate which Scope the configuration is for, in the form:

`projects/{p}/locations/global/scopes/{s}`

Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature's project.

{p} will always be returned as the project number, but the project ID is also accepted during input. If the same Scope is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::ScopeFeatureSpec}) — Optional. Scope-specific configuration for this Feature. If this Feature does not support any per-Scope configuration, this field may be unused.

The keys indicate which Scope the configuration is for, in the form:

`projects/{p}/locations/global/scopes/{s}`

Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature's project.

{p} will always be returned as the project number, but the project ID is also accepted during input. If the same Scope is specified in the map twice (using the project ID form, and the project number form), exactly ONE of the entries will be saved, with no guarantees as to which. For this reason, it is recommended the same format be used for all entries when mutating a Feature. 




### #scope_states
    
    
    def scope_states() -> ::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::ScopeFeatureState}

**Returns**

  * (::Google::Protobuf::Map{::String => ::Google::Cloud::GkeHub::V1::ScopeFeatureState}) — Output only. Scope-specific Feature status. If this Feature does report any per-Scope status, this field may be unused.

The keys indicate which Scope the state is for, in the form:

`projects/{p}/locations/global/scopes/{s}`

Where {p} is the project, {s} is a valid Scope in this project. {p} WILL match the Feature's project. 




### #spec
    
    
    def spec() -> ::Google::Cloud::GkeHub::V1::CommonFeatureSpec

**Returns**

  * ([::Google::Cloud::GkeHub::V1::CommonFeatureSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-CommonFeatureSpec)) — Optional. Fleet-wide Feature configuration. If this Feature does not support any Fleet-wide configuration, this field may be unused. 



### #spec=
    
    
    def spec=(value) -> ::Google::Cloud::GkeHub::V1::CommonFeatureSpec

**Parameter**

  * **value** ([::Google::Cloud::GkeHub::V1::CommonFeatureSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-CommonFeatureSpec)) — Optional. Fleet-wide Feature configuration. If this Feature does not support any Fleet-wide configuration, this field may be unused. 



**Returns**

  * ([::Google::Cloud::GkeHub::V1::CommonFeatureSpec](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-CommonFeatureSpec)) — Optional. Fleet-wide Feature configuration. If this Feature does not support any Fleet-wide configuration, this field may be unused. 



### #state
    
    
    def state() -> ::Google::Cloud::GkeHub::V1::CommonFeatureState

**Returns**

  * ([::Google::Cloud::GkeHub::V1::CommonFeatureState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-CommonFeatureState)) — Output only. The Fleet-wide Feature state. 



### #unreachable
    
    
    def unreachable() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. List of locations that could not be reached while fetching this feature. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Protobuf-Timestamp)) — Output only. When the Feature resource was last updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
