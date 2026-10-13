---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-Workflows-Rest-ServiceStub/
title: Workflows V1beta API - Class Google::Cloud::Workflows::V1beta::Workflows::Rest::ServiceStub (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:52.866514+00:00
---

# Workflows V1beta API - Class Google::Cloud::Workflows::V1beta::Workflows::Rest::ServiceStub (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-Workflows-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Workflows V1beta API - Class Google::Cloud::Workflows::V1beta::Workflows::Rest::ServiceStub (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.1  0.15.1  0.14.0  0.13.0  0.12.2  0.11.0  0.10.0  0.9.2  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Workflows V1beta API class Google::Cloud::Workflows::V1beta::Workflows::Rest::ServiceStub.

REST service stub for the Workflows service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_workflow
    
    
    def create_workflow(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_workflow REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workflows::V1beta::CreateWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-CreateWorkflowRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_workflow
    
    
    def delete_workflow(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_workflow REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workflows::V1beta::DeleteWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-DeleteWorkflowRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_workflow
    
    
    def get_workflow(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workflows::V1beta::Workflow

Baseline implementation for the get_workflow REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workflows::V1beta::GetWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-GetWorkflowRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workflows::V1beta::Workflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-Workflow)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workflows::V1beta::Workflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-Workflow)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_workflows
    
    
    def list_workflows(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Workflows::V1beta::ListWorkflowsResponse

Baseline implementation for the list_workflows REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workflows::V1beta::ListWorkflowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-ListWorkflowsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Workflows::V1beta::ListWorkflowsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-ListWorkflowsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Workflows::V1beta::ListWorkflowsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-ListWorkflowsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_workflow
    
    
    def update_workflow(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_workflow REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Workflows::V1beta::UpdateWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Cloud-Workflows-V1beta-UpdateWorkflowRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-workflows-v1beta/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
