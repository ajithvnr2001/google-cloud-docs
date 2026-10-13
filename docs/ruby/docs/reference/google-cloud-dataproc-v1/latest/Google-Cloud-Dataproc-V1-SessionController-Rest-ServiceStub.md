---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionController-Rest-ServiceStub/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionController::Rest::ServiceStub (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:11.508015+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionController::Rest::ServiceStub (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionController-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionController::Rest::ServiceStub (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::SessionController::Rest::ServiceStub.

REST service stub for the SessionController service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_session
    
    
    def create_session(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_session REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dataproc::V1::CreateSessionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-CreateSessionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_session
    
    
    def delete_session(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_session REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dataproc::V1::DeleteSessionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DeleteSessionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_session
    
    
    def get_session(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Dataproc::V1::Session

Baseline implementation for the get_session REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dataproc::V1::GetSessionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-GetSessionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataproc::V1::Session](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-Session)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::Session](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-Session)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_sessions
    
    
    def list_sessions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Dataproc::V1::ListSessionsResponse

Baseline implementation for the list_sessions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dataproc::V1::ListSessionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListSessionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dataproc::V1::ListSessionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListSessionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::ListSessionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListSessionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #terminate_session
    
    
    def terminate_session(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the terminate_session REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dataproc::V1::TerminateSessionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-TerminateSessionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
