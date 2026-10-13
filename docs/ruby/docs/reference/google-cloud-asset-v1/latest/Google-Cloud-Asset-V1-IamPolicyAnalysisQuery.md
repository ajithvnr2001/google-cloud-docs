---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery/
title: Cloud Asset V1 API - Class Google::Cloud::Asset::V1::IamPolicyAnalysisQuery (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:28.402313+00:00
---

# Cloud Asset V1 API - Class Google::Cloud::Asset::V1::IamPolicyAnalysisQuery (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Asset V1 API - Class Google::Cloud::Asset::V1::IamPolicyAnalysisQuery (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.2  0.32.0  0.31.0  0.30.0  0.29.3  0.28.1  0.27.0  0.26.1  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.1  0.19.0  0.18.0  0.17.3 

Reference documentation and code samples for the Cloud Asset V1 API class Google::Cloud::Asset::V1::IamPolicyAnalysisQuery.

IAM policy analysis query message.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #access_selector
    
    
    def access_selector() -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::AccessSelector

**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::AccessSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-AccessSelector)) — Optional. Specifies roles or permissions for analysis. This is optional. 



### #access_selector=
    
    
    def access_selector=(value) -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::AccessSelector

**Parameter**

  * **value** ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::AccessSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-AccessSelector)) — Optional. Specifies roles or permissions for analysis. This is optional. 



**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::AccessSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-AccessSelector)) — Optional. Specifies roles or permissions for analysis. This is optional. 



### #condition_context
    
    
    def condition_context() -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ConditionContext

**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ConditionContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-ConditionContext)) — Optional. The hypothetical context for IAM conditions evaluation. 



### #condition_context=
    
    
    def condition_context=(value) -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ConditionContext

**Parameter**

  * **value** ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ConditionContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-ConditionContext)) — Optional. The hypothetical context for IAM conditions evaluation. 



**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ConditionContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-ConditionContext)) — Optional. The hypothetical context for IAM conditions evaluation. 



### #identity_selector
    
    
    def identity_selector() -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::IdentitySelector

**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::IdentitySelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-IdentitySelector)) — Optional. Specifies an identity for analysis. 



### #identity_selector=
    
    
    def identity_selector=(value) -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::IdentitySelector

**Parameter**

  * **value** ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::IdentitySelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-IdentitySelector)) — Optional. Specifies an identity for analysis. 



**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::IdentitySelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-IdentitySelector)) — Optional. Specifies an identity for analysis. 



### #options
    
    
    def options() -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::Options

**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::Options](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-Options)) — Optional. The query options. 



### #options=
    
    
    def options=(value) -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::Options

**Parameter**

  * **value** ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::Options](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-Options)) — Optional. The query options. 



**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::Options](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-Options)) — Optional. The query options. 



### #resource_selector
    
    
    def resource_selector() -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ResourceSelector

**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ResourceSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-ResourceSelector)) — Optional. Specifies a resource for analysis. 



### #resource_selector=
    
    
    def resource_selector=(value) -> ::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ResourceSelector

**Parameter**

  * **value** ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ResourceSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-ResourceSelector)) — Optional. Specifies a resource for analysis. 



**Returns**

  * ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery::ResourceSelector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery-ResourceSelector)) — Optional. Specifies a resource for analysis. 



### #scope
    
    
    def scope() -> ::String

**Returns**

  * (::String) — Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.

This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").

To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). 




### #scope=
    
    
    def scope=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.

This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").

To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). 




**Returns**

  * (::String) — Required. The relative name of the root asset. Only resources and IAM policies within the scope will be analyzed.

This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").

To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
