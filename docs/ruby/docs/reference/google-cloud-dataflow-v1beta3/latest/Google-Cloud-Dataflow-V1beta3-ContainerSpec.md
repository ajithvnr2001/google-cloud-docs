---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-ContainerSpec/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::ContainerSpec (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:58.105572+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::ContainerSpec (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-ContainerSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::ContainerSpec (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::ContainerSpec.

Container Spec.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #default_environment
    
    
    def default_environment() -> ::Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplateRuntimeEnvironment)) — Default runtime environment for the job. 



### #default_environment=
    
    
    def default_environment=(value) -> ::Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplateRuntimeEnvironment)) — Default runtime environment for the job. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::FlexTemplateRuntimeEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-FlexTemplateRuntimeEnvironment)) — Default runtime environment for the job. 



### #image
    
    
    def image() -> ::String

**Returns**

  * (::String) — Name of the docker container image. E.g., gcr.io/project/some-image 



### #image=
    
    
    def image=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the docker container image. E.g., gcr.io/project/some-image 



**Returns**

  * (::String) — Name of the docker container image. E.g., gcr.io/project/some-image 



### #image_repository_cert_path
    
    
    def image_repository_cert_path() -> ::String

**Returns**

  * (::String) — Cloud Storage path to self-signed certificate of private registry. 



### #image_repository_cert_path=
    
    
    def image_repository_cert_path=(value) -> ::String

**Parameter**

  * **value** (::String) — Cloud Storage path to self-signed certificate of private registry. 



**Returns**

  * (::String) — Cloud Storage path to self-signed certificate of private registry. 



### #image_repository_password_secret_id
    
    
    def image_repository_password_secret_id() -> ::String

**Returns**

  * (::String) — Secret Manager secret id for password to authenticate to private registry. 



### #image_repository_password_secret_id=
    
    
    def image_repository_password_secret_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Secret Manager secret id for password to authenticate to private registry. 



**Returns**

  * (::String) — Secret Manager secret id for password to authenticate to private registry. 



### #image_repository_username_secret_id
    
    
    def image_repository_username_secret_id() -> ::String

**Returns**

  * (::String) — Secret Manager secret id for username to authenticate to private registry. 



### #image_repository_username_secret_id=
    
    
    def image_repository_username_secret_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Secret Manager secret id for username to authenticate to private registry. 



**Returns**

  * (::String) — Secret Manager secret id for username to authenticate to private registry. 



### #metadata
    
    
    def metadata() -> ::Google::Cloud::Dataflow::V1beta3::TemplateMetadata

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::TemplateMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-TemplateMetadata)) — Metadata describing a template including description and validation rules. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Cloud::Dataflow::V1beta3::TemplateMetadata

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::TemplateMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-TemplateMetadata)) — Metadata describing a template including description and validation rules. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::TemplateMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-TemplateMetadata)) — Metadata describing a template including description and validation rules. 



### #sdk_info
    
    
    def sdk_info() -> ::Google::Cloud::Dataflow::V1beta3::SDKInfo

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::SDKInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-SDKInfo)) — Required. SDK info of the Flex Template. 



### #sdk_info=
    
    
    def sdk_info=(value) -> ::Google::Cloud::Dataflow::V1beta3::SDKInfo

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::SDKInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-SDKInfo)) — Required. SDK info of the Flex Template. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::SDKInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-SDKInfo)) — Required. SDK info of the Flex Template. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
