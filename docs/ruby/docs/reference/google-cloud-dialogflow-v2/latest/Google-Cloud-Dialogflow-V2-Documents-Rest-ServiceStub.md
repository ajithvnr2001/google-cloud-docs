---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Documents-Rest-ServiceStub/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Documents::Rest::ServiceStub (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:23.266422+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Documents::Rest::ServiceStub (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Documents-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::Documents::Rest::ServiceStub (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::Documents::Rest::ServiceStub.

REST service stub for the Documents service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_document
    
    
    def create_document(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_document REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::CreateDocumentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CreateDocumentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_document
    
    
    def delete_document(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_document REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::DeleteDocumentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-DeleteDocumentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #export_document
    
    
    def export_document(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the export_document REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::ExportDocumentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ExportDocumentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_document
    
    
    def get_document(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Dialogflow::V2::Document

Baseline implementation for the get_document REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::GetDocumentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-GetDocumentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Document)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Document)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #import_documents
    
    
    def import_documents(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the import_documents REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::ImportDocumentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ImportDocumentsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_documents
    
    
    def list_documents(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Dialogflow::V2::ListDocumentsResponse

Baseline implementation for the list_documents REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::ListDocumentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListDocumentsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Dialogflow::V2::ListDocumentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListDocumentsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::ListDocumentsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ListDocumentsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #reload_document
    
    
    def reload_document(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the reload_document REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::ReloadDocumentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-ReloadDocumentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_document
    
    
    def update_document(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_document REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Dialogflow::V2::UpdateDocumentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-UpdateDocumentRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
