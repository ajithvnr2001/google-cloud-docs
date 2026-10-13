---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-ResourceOptions/
title: GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::ResourceOptions (v2.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:33.105026+00:00
---

# GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::ResourceOptions (v2.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_hub-v1/latest/Google-Cloud-GkeHub-V1-ResourceOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  GKE Hub V1 API - Class Google::Cloud::GkeHub::V1::ResourceOptions (v2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.10.0  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the GKE Hub V1 API class Google::Cloud::GkeHub::V1::ResourceOptions.

ResourceOptions represent options for Kubernetes resource generation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #connect_version
    
    
    def connect_version() -> ::String

**Returns**

  * (::String) — Optional. The Connect agent version to use for connect_resources. Defaults to the latest GKE Connect version. The version must be a currently supported version, obsolete versions will be rejected. 



### #connect_version=
    
    
    def connect_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The Connect agent version to use for connect_resources. Defaults to the latest GKE Connect version. The version must be a currently supported version, obsolete versions will be rejected. 



**Returns**

  * (::String) — Optional. The Connect agent version to use for connect_resources. Defaults to the latest GKE Connect version. The version must be a currently supported version, obsolete versions will be rejected. 



### #k8s_git_version
    
    
    def k8s_git_version() -> ::String

**Returns**

  * (::String) — Optional. Git version of the Kubernetes cluster. This is only used to gate the Connect Agent migration to svc.id.goog on GDC-SO 1.33.100 patch and above. 



### #k8s_git_version=
    
    
    def k8s_git_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Git version of the Kubernetes cluster. This is only used to gate the Connect Agent migration to svc.id.goog on GDC-SO 1.33.100 patch and above. 



**Returns**

  * (::String) — Optional. Git version of the Kubernetes cluster. This is only used to gate the Connect Agent migration to svc.id.goog on GDC-SO 1.33.100 patch and above. 



### #k8s_version
    
    
    def k8s_version() -> ::String

**Returns**

  * (::String) — Optional. Major and minor version of the Kubernetes cluster. This is only used to determine which version to use for the CustomResourceDefinition resources, `apiextensions/v1beta1` or`apiextensions/v1`. 



### #k8s_version=
    
    
    def k8s_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Major and minor version of the Kubernetes cluster. This is only used to determine which version to use for the CustomResourceDefinition resources, `apiextensions/v1beta1` or`apiextensions/v1`. 



**Returns**

  * (::String) — Optional. Major and minor version of the Kubernetes cluster. This is only used to determine which version to use for the CustomResourceDefinition resources, `apiextensions/v1beta1` or`apiextensions/v1`. 



### #v1beta1_crd
    
    
    def v1beta1_crd() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Use `apiextensions/v1beta1` instead of `apiextensions/v1` for CustomResourceDefinition resources. This option should be set for clusters with Kubernetes apiserver versions <1.16. 



### #v1beta1_crd=
    
    
    def v1beta1_crd=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Use `apiextensions/v1beta1` instead of `apiextensions/v1` for CustomResourceDefinition resources. This option should be set for clusters with Kubernetes apiserver versions <1.16. 



**Returns**

  * (::Boolean) — Optional. Use `apiextensions/v1beta1` instead of `apiextensions/v1` for CustomResourceDefinition resources. This option should be set for clusters with Kubernetes apiserver versions <1.16. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
