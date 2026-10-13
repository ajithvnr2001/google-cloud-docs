---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-CaseAttachmentService-Rest-ServiceStub/
title: Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::CaseAttachmentService::Rest::ServiceStub (v0.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:39.239108+00:00
---

# Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::CaseAttachmentService::Rest::ServiceStub (v0.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-CaseAttachmentService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Support V2BETA API - Class Google::Cloud::Support::V2beta::CaseAttachmentService::Rest::ServiceStub (v0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud Support V2BETA API class Google::Cloud::Support::V2beta::CaseAttachmentService::Rest::ServiceStub.

REST service stub for the CaseAttachmentService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_attachment
    
    
    def get_attachment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::Attachment

Baseline implementation for the get_attachment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::GetAttachmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-GetAttachmentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::Attachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Attachment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::Attachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-Attachment)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_attachments
    
    
    def list_attachments(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2beta::ListAttachmentsResponse

Baseline implementation for the list_attachments REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2beta::ListAttachmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-ListAttachmentsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2beta::ListAttachmentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-ListAttachmentsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2beta::ListAttachmentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2beta/latest/Google-Cloud-Support-V2beta-ListAttachmentsResponse)) — A result object deserialized from the server's reply 



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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
