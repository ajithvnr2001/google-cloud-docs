---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-InstanceOSPoliciesCompliance-OSPolicyCompliance/
title: Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::InstanceOSPoliciesCompliance::OSPolicyCompliance (v0.17.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:49.938831+00:00
---

# Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::InstanceOSPoliciesCompliance::OSPolicyCompliance (v0.17.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-InstanceOSPoliciesCompliance-OSPolicyCompliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::InstanceOSPoliciesCompliance::OSPolicyCompliance (v0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.1  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Cloud OS Config V1alpha API class Google::Cloud::OsConfig::V1alpha::InstanceOSPoliciesCompliance::OSPolicyCompliance.

Compliance data for an OS policy

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #os_policy_assignment
    
    
    def os_policy_assignment() -> ::String

**Returns**

  * (::String) — Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to.

Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}`




### #os_policy_assignment=
    
    
    def os_policy_assignment=(value) -> ::String

**Parameter**

  * **value** (::String) — Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to.

Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}`




**Returns**

  * (::String) — Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to.

Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}`




### #os_policy_id
    
    
    def os_policy_id() -> ::String

**Returns**

  * (::String) — The OS policy id 



### #os_policy_id=
    
    
    def os_policy_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The OS policy id 



**Returns**

  * (::String) — The OS policy id 



### #os_policy_resource_compliances
    
    
    def os_policy_resource_compliances() -> ::Array<::Google::Cloud::OsConfig::V1alpha::OSPolicyResourceCompliance>

**Returns**

  * (::Array<[::Google::Cloud::OsConfig::V1alpha::OSPolicyResourceCompliance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicyResourceCompliance)>) — Compliance data for each `OSPolicyResource` that is applied to the VM. 



### #os_policy_resource_compliances=
    
    
    def os_policy_resource_compliances=(value) -> ::Array<::Google::Cloud::OsConfig::V1alpha::OSPolicyResourceCompliance>

**Parameter**

  * **value** (::Array<[::Google::Cloud::OsConfig::V1alpha::OSPolicyResourceCompliance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicyResourceCompliance)>) — Compliance data for each `OSPolicyResource` that is applied to the VM. 



**Returns**

  * (::Array<[::Google::Cloud::OsConfig::V1alpha::OSPolicyResourceCompliance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicyResourceCompliance)>) — Compliance data for each `OSPolicyResource` that is applied to the VM. 



### #state
    
    
    def state() -> ::Google::Cloud::OsConfig::V1alpha::OSPolicyComplianceState

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::OSPolicyComplianceState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicyComplianceState)) — Compliance state of the OS policy. 



### #state=
    
    
    def state=(value) -> ::Google::Cloud::OsConfig::V1alpha::OSPolicyComplianceState

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::OSPolicyComplianceState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicyComplianceState)) — Compliance state of the OS policy. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::OSPolicyComplianceState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-OSPolicyComplianceState)) — Compliance state of the OS policy. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
