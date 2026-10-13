---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-CaseService-Rest-ServiceStub/
title: Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::CaseService::Rest::ServiceStub (v0.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:43.939790+00:00
---

# Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::CaseService::Rest::ServiceStub (v0.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-CaseService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::CaseService::Rest::ServiceStub (v0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud Support V2BETA API class Google::Cloud::Support::V2beta::CaseService::Rest::ServiceStub.

REST service stub for the CaseService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #close_case
    
    
    def close_case(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::Case

Baseline implementation for the close_case REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::CloseCaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-CloseCaseRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_case
    
    
    def create_case(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::Case

Baseline implementation for the create_case REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::CreateCaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-CreateCaseRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #escalate_case
    
    
    def escalate_case(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::Case

Baseline implementation for the escalate_case REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::EscalateCaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-EscalateCaseRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_case
    
    
    def get_case(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::Case

Baseline implementation for the get_case REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::GetCaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-GetCaseRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_cases
    
    
    def list_cases(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::ListCasesResponse

Baseline implementation for the list_cases REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::ListCasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-ListCasesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::ListCasesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-ListCasesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::ListCasesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-ListCasesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #search_case_classifications
    
    
    def search_case_classifications(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::SearchCaseClassificationsResponse

Baseline implementation for the search_case_classifications REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::SearchCaseClassificationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-SearchCaseClassificationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::SearchCaseClassificationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-SearchCaseClassificationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::SearchCaseClassificationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-SearchCaseClassificationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #search_cases
    
    
    def search_cases(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::SearchCasesResponse

Baseline implementation for the search_cases REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::SearchCasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-SearchCasesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::SearchCasesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-SearchCasesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::SearchCasesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-SearchCasesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_case
    
    
    def update_case(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::Case

Baseline implementation for the update_case REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::UpdateCaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-UpdateCaseRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::Case](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Case)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
