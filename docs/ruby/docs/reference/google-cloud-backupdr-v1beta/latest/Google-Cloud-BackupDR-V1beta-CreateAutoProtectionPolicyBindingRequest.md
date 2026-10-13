---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-CreateAutoProtectionPolicyBindingRequest/
title: Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::CreateAutoProtectionPolicyBindingRequest (v0.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:15:53.890090+00:00
---

# Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::CreateAutoProtectionPolicyBindingRequest (v0.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-CreateAutoProtectionPolicyBindingRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1BETA API - Class Google::Cloud::BackupDR::V1beta::CreateAutoProtectionPolicyBindingRequest (v0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the Backup and DR Service V1BETA API class Google::Cloud::BackupDR::V1beta::CreateAutoProtectionPolicyBindingRequest.

Request message for creating an AutoProtectionPolicyBinding.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #auto_protection_policy_binding
    
    
    def auto_protection_policy_binding() -> ::Google::Cloud::BackupDR::V1beta::AutoProtectionPolicyBinding

**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::AutoProtectionPolicyBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AutoProtectionPolicyBinding)) — Required. The AutoProtectionPolicyBinding resource to create. 



### #auto_protection_policy_binding=
    
    
    def auto_protection_policy_binding=(value) -> ::Google::Cloud::BackupDR::V1beta::AutoProtectionPolicyBinding

**Parameter**

  * **value** ([::Google::Cloud::BackupDR::V1beta::AutoProtectionPolicyBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AutoProtectionPolicyBinding)) — Required. The AutoProtectionPolicyBinding resource to create. 



**Returns**

  * ([::Google::Cloud::BackupDR::V1beta::AutoProtectionPolicyBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1beta/latest/Google-Cloud-BackupDR-V1beta-AutoProtectionPolicyBinding)) — Required. The AutoProtectionPolicyBinding resource to create. 



### #auto_protection_policy_binding_id
    
    
    def auto_protection_policy_binding_id() -> ::String

**Returns**

  * (::String) — Required. The ID to use for the binding. This will become the final component of the binding's resource name. 



### #auto_protection_policy_binding_id=
    
    
    def auto_protection_policy_binding_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID to use for the binding. This will become the final component of the binding's resource name. 



**Returns**

  * (::String) — Required. The ID to use for the binding. This will become the final component of the binding's resource name. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent resource where this binding will be created. Format: projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent resource where this binding will be created. Format: projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy} 



**Returns**

  * (::String) — Required. The parent resource where this binding will be created. Format: projects/{project}/locations/{location}/autoProtectionPolicies/{auto_protection_policy} 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
