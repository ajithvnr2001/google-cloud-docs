---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer/
title: Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:39.000420+00:00
---

# Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.2  0.32.0  0.31.0  0.30.0  0.29.3  0.28.1  0.27.0  0.26.1  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.1  0.19.0  0.18.0  0.17.3 

Reference documentation and code samples for the Cloud Asset V1 API class Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer.

The organization/folder/project resource governed by organization policies of [AnalyzeOrgPolicyGovernedContainersRequest.constraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersRequest#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersRequest_constraint_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersRequest#constraint \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #consolidated_policy
    
    
    def consolidated_policy() -> ::Google::Cloud::Asset::V1::AnalyzerOrgPolicy

**Returns**

  * ([::Google::Cloud::Asset::V1::AnalyzerOrgPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy)) — The consolidated organization policy for the analyzed resource. The consolidated organization policy is computed by merging and evaluating [AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.policy_bundle](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersResponse__GovernedContainer_policy_bundle_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer#policy_bundle \(method\)"). The evaluation will respect the organization policy [hierarchy rules](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy). 



### #consolidated_policy=
    
    
    def consolidated_policy=(value) -> ::Google::Cloud::Asset::V1::AnalyzerOrgPolicy

**Parameter**

  * **value** ([::Google::Cloud::Asset::V1::AnalyzerOrgPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy)) — The consolidated organization policy for the analyzed resource. The consolidated organization policy is computed by merging and evaluating [AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.policy_bundle](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersResponse__GovernedContainer_policy_bundle_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer#policy_bundle \(method\)"). The evaluation will respect the organization policy [hierarchy rules](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy). 



**Returns**

  * ([::Google::Cloud::Asset::V1::AnalyzerOrgPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy)) — The consolidated organization policy for the analyzed resource. The consolidated organization policy is computed by merging and evaluating [AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.policy_bundle](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersResponse__GovernedContainer_policy_bundle_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer#policy_bundle \(method\)"). The evaluation will respect the organization policy [hierarchy rules](https://cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy). 



### #effective_tags
    
    
    def effective_tags() -> ::Array<::Google::Cloud::Asset::V1::EffectiveTagDetails>

**Returns**

  * (::Array<[::Google::Cloud::Asset::V1::EffectiveTagDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-EffectiveTagDetails)>) — The effective tags on this resource. 



### #effective_tags=
    
    
    def effective_tags=(value) -> ::Array<::Google::Cloud::Asset::V1::EffectiveTagDetails>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Asset::V1::EffectiveTagDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-EffectiveTagDetails)>) — The effective tags on this resource. 



**Returns**

  * (::Array<[::Google::Cloud::Asset::V1::EffectiveTagDetails](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-EffectiveTagDetails)>) — The effective tags on this resource. 



### #folders
    
    
    def folders() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The folder(s) that this resource belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to one or more folders. 



### #folders=
    
    
    def folders=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The folder(s) that this resource belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to one or more folders. 



**Returns**

  * (::Array<::String>) — The folder(s) that this resource belongs to, in the format of folders/{FOLDER_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to one or more folders. 



### #full_resource_name
    
    
    def full_resource_name() -> ::String

**Returns**

  * (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource. 



### #full_resource_name=
    
    
    def full_resource_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource. 



**Returns**

  * (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of an organization/folder/project resource. 



### #organization
    
    
    def organization() -> ::String

**Returns**

  * (::String) — The organization that this resource belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to an organization. 



### #organization=
    
    
    def organization=(value) -> ::String

**Parameter**

  * **value** (::String) — The organization that this resource belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to an organization. 



**Returns**

  * (::String) — The organization that this resource belongs to, in the format of organizations/{ORGANIZATION_NUMBER}. This field is available when the resource belongs (directly or cascadingly) to an organization. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the parent of [AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.full_resource_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersResponse__GovernedContainer_full_resource_name_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer#full_resource_name \(method\)"). 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the parent of [AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.full_resource_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersResponse__GovernedContainer_full_resource_name_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer#full_resource_name \(method\)"). 



**Returns**

  * (::String) — The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the parent of [AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer.full_resource_name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersResponse__GovernedContainer_full_resource_name_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer#full_resource_name \(method\)"). 



### #policy_bundle
    
    
    def policy_bundle() -> ::Array<::Google::Cloud::Asset::V1::AnalyzerOrgPolicy>

**Returns**

  * (::Array<[::Google::Cloud::Asset::V1::AnalyzerOrgPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy)>) — The ordered list of all organization policies from the [consolidated_policy.attached_resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy#Google__Cloud__Asset__V1__AnalyzerOrgPolicy_attached_resource_instance_ "Google::Cloud::Asset::V1::AnalyzerOrgPolicy#attached_resource \(method\)"). to the scope specified in the request.

If the constraint is defined with default policy, it will also appear in the list. 




### #policy_bundle=
    
    
    def policy_bundle=(value) -> ::Array<::Google::Cloud::Asset::V1::AnalyzerOrgPolicy>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Asset::V1::AnalyzerOrgPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy)>) — The ordered list of all organization policies from the [consolidated_policy.attached_resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy#Google__Cloud__Asset__V1__AnalyzerOrgPolicy_attached_resource_instance_ "Google::Cloud::Asset::V1::AnalyzerOrgPolicy#attached_resource \(method\)"). to the scope specified in the request.

If the constraint is defined with default policy, it will also appear in the list. 




**Returns**

  * (::Array<[::Google::Cloud::Asset::V1::AnalyzerOrgPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy)>) — The ordered list of all organization policies from the [consolidated_policy.attached_resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzerOrgPolicy#Google__Cloud__Asset__V1__AnalyzerOrgPolicy_attached_resource_instance_ "Google::Cloud::Asset::V1::AnalyzerOrgPolicy#attached_resource \(method\)"). to the scope specified in the request.

If the constraint is defined with default policy, it will also appear in the list. 




### #project
    
    
    def project() -> ::String

**Returns**

  * (::String) — The project that this resource belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project. 



### #project=
    
    
    def project=(value) -> ::String

**Parameter**

  * **value** (::String) — The project that this resource belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project. 



**Returns**

  * (::String) — The project that this resource belongs to, in the format of projects/{PROJECT_NUMBER}. This field is available when the resource belongs to a project. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
