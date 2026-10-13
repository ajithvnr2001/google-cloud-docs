---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-agent_registry-v1/latest/Google-Cloud-AgentRegistry-V1-CreateServiceRequest/
title: Agent Registry V1 API - Class Google::Cloud::AgentRegistry::V1::CreateServiceRequest (v0.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:26.369195+00:00
---

# Agent Registry V1 API - Class Google::Cloud::AgentRegistry::V1::CreateServiceRequest (v0.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-agent_registry-v1/latest/Google-Cloud-AgentRegistry-V1-CreateServiceRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Agent Registry V1 API - Class Google::Cloud::AgentRegistry::V1::CreateServiceRequest (v0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.1 

Reference documentation and code samples for the Agent Registry V1 API class Google::Cloud::AgentRegistry::V1::CreateServiceRequest.

Message for creating a Service

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

  * (::String) — Required. The project and location to create the Service in. Expected format: `projects/{project}/locations/{location}`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The project and location to create the Service in. Expected format: `projects/{project}/locations/{location}`. 



**Returns**

  * (::String) — Required. The project and location to create the Service in. Expected format: `projects/{project}/locations/{location}`. 



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




### #service
    
    
    def service() -> ::Google::Cloud::AgentRegistry::V1::Service

**Returns**

  * ([::Google::Cloud::AgentRegistry::V1::Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-agent_registry-v1/latest/Google-Cloud-AgentRegistry-V1-Service)) — Required. The Service resource that is being created. Format: `projects/{project}/locations/{location}/services/{service}`. 



### #service=
    
    
    def service=(value) -> ::Google::Cloud::AgentRegistry::V1::Service

**Parameter**

  * **value** ([::Google::Cloud::AgentRegistry::V1::Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-agent_registry-v1/latest/Google-Cloud-AgentRegistry-V1-Service)) — Required. The Service resource that is being created. Format: `projects/{project}/locations/{location}/services/{service}`. 



**Returns**

  * ([::Google::Cloud::AgentRegistry::V1::Service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-agent_registry-v1/latest/Google-Cloud-AgentRegistry-V1-Service)) — Required. The Service resource that is being created. Format: `projects/{project}/locations/{location}/services/{service}`. 



### #service_id
    
    
    def service_id() -> ::String

**Returns**

  * (::String) — Required. The ID to use for the service, which will become the final component of the service's resource name.

This value should be 4-63 characters, and valid characters are `/[a-z][0-9]-/`. 




### #service_id=
    
    
    def service_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID to use for the service, which will become the final component of the service's resource name.

This value should be 4-63 characters, and valid characters are `/[a-z][0-9]-/`. 




**Returns**

  * (::String) — Required. The ID to use for the service, which will become the final component of the service's resource name.

This value should be 4-63 characters, and valid characters are `/[a-z][0-9]-/`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
