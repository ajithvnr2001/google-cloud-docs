---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-CaseAttachmentService-Rest-ServiceStub/
title: Google Cloud Support V2 API - Class Google::Cloud::Support::V2::CaseAttachmentService::Rest::ServiceStub (v1.11.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:30.463039+00:00
---

# Google Cloud Support V2 API - Class Google::Cloud::Support::V2::CaseAttachmentService::Rest::ServiceStub (v1.11.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-CaseAttachmentService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Support V2 API - Class Google::Cloud::Support::V2::CaseAttachmentService::Rest::ServiceStub (v1.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.3 (latest)  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.1  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Google Cloud Support V2 API class Google::Cloud::Support::V2::CaseAttachmentService::Rest::ServiceStub.

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
    
    
    def get_attachment(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2::Attachment

Baseline implementation for the get_attachment REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2::GetAttachmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-GetAttachmentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2::Attachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-Attachment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2::Attachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-Attachment)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_attachments
    
    
    def list_attachments(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Support::V2::ListAttachmentsResponse

Baseline implementation for the list_attachments REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Support::V2::ListAttachmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-ListAttachmentsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Support::V2::ListAttachmentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-ListAttachmentsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Support::V2::ListAttachmentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-support-v2/latest/Google-Cloud-Support-V2-ListAttachmentsResponse)) — A result object deserialized from the server's reply 



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
