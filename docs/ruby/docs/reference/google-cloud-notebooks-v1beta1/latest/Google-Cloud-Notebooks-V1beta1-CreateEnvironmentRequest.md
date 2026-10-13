---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1beta1/latest/Google-Cloud-Notebooks-V1beta1-CreateEnvironmentRequest/
title: AI Platform Notebooks V1beta1 API - Class Google::Cloud::Notebooks::V1beta1::CreateEnvironmentRequest (v0.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:47.762624+00:00
---

# AI Platform Notebooks V1beta1 API - Class Google::Cloud::Notebooks::V1beta1::CreateEnvironmentRequest (v0.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1beta1/latest/Google-Cloud-Notebooks-V1beta1-CreateEnvironmentRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Notebooks V1beta1 API - Class Google::Cloud::Notebooks::V1beta1::CreateEnvironmentRequest (v0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.1  0.11.0  0.10.1  0.9.2  0.8.0  0.7.1  0.6.1  0.5.0  0.4.5 

Reference documentation and code samples for the AI Platform Notebooks V1beta1 API class Google::Cloud::Notebooks::V1beta1::CreateEnvironmentRequest.

Request for creating a notebook environment.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #environment
    
    
    def environment() -> ::Google::Cloud::Notebooks::V1beta1::Environment

**Returns**

  * ([::Google::Cloud::Notebooks::V1beta1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1beta1/latest/Google-Cloud-Notebooks-V1beta1-Environment)) — Required. The environment to be created. 



### #environment=
    
    
    def environment=(value) -> ::Google::Cloud::Notebooks::V1beta1::Environment

**Parameter**

  * **value** ([::Google::Cloud::Notebooks::V1beta1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1beta1/latest/Google-Cloud-Notebooks-V1beta1-Environment)) — Required. The environment to be created. 



**Returns**

  * ([::Google::Cloud::Notebooks::V1beta1::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1beta1/latest/Google-Cloud-Notebooks-V1beta1-Environment)) — Required. The environment to be created. 



### #environment_id
    
    
    def environment_id() -> ::String

**Returns**

  * (::String) — Required. User-defined unique ID of this environment. The `environment_id` must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercase letter and the last character cannot be a dash. 



### #environment_id=
    
    
    def environment_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. User-defined unique ID of this environment. The `environment_id` must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercase letter and the last character cannot be a dash. 



**Returns**

  * (::String) — Required. User-defined unique ID of this environment. The `environment_id` must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercase letter and the last character cannot be a dash. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Format: `projects/{project_id}/locations/{location}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Format: `projects/{project_id}/locations/{location}`



**Returns**

  * (::String) — Required. Format: `projects/{project_id}/locations/{location}`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
