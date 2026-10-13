---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-CreateTemplateVersionRequest/
title: Parameter Manager V1 API - Class Google::Cloud::ParameterManager::V1::CreateTemplateVersionRequest (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:09.153038+00:00
---

# Parameter Manager V1 API - Class Google::Cloud::ParameterManager::V1::CreateTemplateVersionRequest (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-CreateTemplateVersionRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Parameter Manager V1 API - Class Google::Cloud::ParameterManager::V1::CreateTemplateVersionRequest (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Parameter Manager V1 API class Google::Cloud::ParameterManager::V1::CreateTemplateVersionRequest.

Message for creating a TemplateVersion

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Value for parent in the format `projects/*/locations/*/templates/*`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Value for parent in the format `projects/*/locations/*/templates/*`. 



**Returns**

  * (::String) — Required. Value for parent in the format `projects/*/locations/*/templates/*`. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




### #template_version
    
    
    def template_version() -> ::Google::Cloud::ParameterManager::V1::TemplateVersion

**Returns**

  * ([::Google::Cloud::ParameterManager::V1::TemplateVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-TemplateVersion)) — Required. The TemplateVersion resource being created 



### #template_version=
    
    
    def template_version=(value) -> ::Google::Cloud::ParameterManager::V1::TemplateVersion

**Parameter**

  * **value** ([::Google::Cloud::ParameterManager::V1::TemplateVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-TemplateVersion)) — Required. The TemplateVersion resource being created 



**Returns**

  * ([::Google::Cloud::ParameterManager::V1::TemplateVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-TemplateVersion)) — Required. The TemplateVersion resource being created 



### #template_version_id
    
    
    def template_version_id() -> ::String

**Returns**

  * (::String) — Required. Id of the TemplateVersion resource 



### #template_version_id=
    
    
    def template_version_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Id of the TemplateVersion resource 



**Returns**

  * (::String) — Required. Id of the TemplateVersion resource 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
