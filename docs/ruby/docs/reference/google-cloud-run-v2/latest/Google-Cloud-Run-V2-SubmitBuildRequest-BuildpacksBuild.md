---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-SubmitBuildRequest-BuildpacksBuild/
title: Cloud Run V2 API - Class Google::Cloud::Run::V2::SubmitBuildRequest::BuildpacksBuild (v0.29.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:42.452603+00:00
---

# Cloud Run V2 API - Class Google::Cloud::Run::V2::SubmitBuildRequest::BuildpacksBuild (v0.29.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-SubmitBuildRequest-BuildpacksBuild/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run V2 API - Class Google::Cloud::Run::V2::SubmitBuildRequest::BuildpacksBuild (v0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.1  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run V2 API class Google::Cloud::Run::V2::SubmitBuildRequest::BuildpacksBuild.

Build the source using Buildpacks.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #base_image
    
    
    def base_image() -> ::String

**Returns**

  * (::String) — Optional. The base image to use for the build. 



### #base_image=
    
    
    def base_image=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The base image to use for the build. 



**Returns**

  * (::String) — Optional. The base image to use for the build. 



### #cache_image_uri
    
    
    def cache_image_uri() -> ::String

**Returns**

  * (::String) — Optional. cache_image_uri is the GCR/AR URL where the cache image will be stored. cache_image_uri is optional and omitting it will disable caching. This URL must be stable across builds. It is used to derive a build-specific temporary URL by substituting the tag with the build ID. The build will clean up the temporary image on a best-effort basis. 



### #cache_image_uri=
    
    
    def cache_image_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. cache_image_uri is the GCR/AR URL where the cache image will be stored. cache_image_uri is optional and omitting it will disable caching. This URL must be stable across builds. It is used to derive a build-specific temporary URL by substituting the tag with the build ID. The build will clean up the temporary image on a best-effort basis. 



**Returns**

  * (::String) — Optional. cache_image_uri is the GCR/AR URL where the cache image will be stored. cache_image_uri is optional and omitting it will disable caching. This URL must be stable across builds. It is used to derive a build-specific temporary URL by substituting the tag with the build ID. The build will clean up the temporary image on a best-effort basis. 



### #enable_automatic_updates
    
    
    def enable_automatic_updates() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether or not the application container will be enrolled in automatic base image updates. When true, the application will be built on a scratch base image, so the base layers can be appended at run time. 



### #enable_automatic_updates=
    
    
    def enable_automatic_updates=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether or not the application container will be enrolled in automatic base image updates. When true, the application will be built on a scratch base image, so the base layers can be appended at run time. 



**Returns**

  * (::Boolean) — Optional. Whether or not the application container will be enrolled in automatic base image updates. When true, the application will be built on a scratch base image, so the base layers can be appended at run time. 



### #environment_variables
    
    
    def environment_variables() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User-provided build-time environment variables. 



### #environment_variables=
    
    
    def environment_variables=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. User-provided build-time environment variables. 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. User-provided build-time environment variables. 



### #function_target
    
    
    def function_target() -> ::String

**Returns**

  * (::String) — Optional. Name of the function target if the source is a function source. Required for function builds. 



### #function_target=
    
    
    def function_target=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Name of the function target if the source is a function source. Required for function builds. 



**Returns**

  * (::String) — Optional. Name of the function target if the source is a function source. Required for function builds. 



### #project_descriptor
    
    
    def project_descriptor() -> ::String

**Returns**

  * (::String) — Optional. project_descriptor stores the path to the project descriptor file. When empty, it means that there is no project descriptor file in the source. 



### #project_descriptor=
    
    
    def project_descriptor=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. project_descriptor stores the path to the project descriptor file. When empty, it means that there is no project descriptor file in the source. 



**Returns**

  * (::String) — Optional. project_descriptor stores the path to the project descriptor file. When empty, it means that there is no project descriptor file in the source. 



### #runtime
    
    
    def runtime() -> ::String

**Returns**

  * (::String) — The runtime name, e.g. 'go113'. Leave blank for generic builds. 



### #runtime=
    
    
    def runtime=(value) -> ::String

**Parameter**

  * **value** (::String) — The runtime name, e.g. 'go113'. Leave blank for generic builds. 



**Returns**

  * (::String) — The runtime name, e.g. 'go113'. Leave blank for generic builds. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
