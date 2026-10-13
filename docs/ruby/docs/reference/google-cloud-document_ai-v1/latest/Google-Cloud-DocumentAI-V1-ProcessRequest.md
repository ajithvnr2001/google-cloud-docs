---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessRequest/
title: Document AI V1 API - Class Google::Cloud::DocumentAI::V1::ProcessRequest (v1.13.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:14.972659+00:00
---

# Document AI V1 API - Class Google::Cloud::DocumentAI::V1::ProcessRequest (v1.13.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Document AI V1 API - Class Google::Cloud::DocumentAI::V1::ProcessRequest (v1.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.1 (latest)  1.13.0  1.12.1  1.11.0  1.10.2  1.9.0  1.8.0  1.7.0  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.23.1  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.2  0.16.2  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 

Reference documentation and code samples for the Document AI V1 API class Google::Cloud::DocumentAI::V1::ProcessRequest.

Request message for the [ProcessDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-DocumentProcessorService-Client#Google__Cloud__DocumentAI__V1__DocumentProcessorService__Client_process_document_instance_ "Google::Cloud::DocumentAI::V1::DocumentProcessorService::Client#process_document \(method\)") method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #field_mask
    
    
    def field_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Protobuf-FieldMask)) — Specifies which fields to include in the [ProcessResponse.document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessResponse#Google__Cloud__DocumentAI__V1__ProcessResponse_document_instance_ "Google::Cloud::DocumentAI::V1::ProcessResponse#document \(method\)") output. Only supports top-level document and pages field, so it must be in the form of `{document_field_name}` or `pages.{page_field_name}`. 



### #field_mask=
    
    
    def field_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Protobuf-FieldMask)) — Specifies which fields to include in the [ProcessResponse.document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessResponse#Google__Cloud__DocumentAI__V1__ProcessResponse_document_instance_ "Google::Cloud::DocumentAI::V1::ProcessResponse#document \(method\)") output. Only supports top-level document and pages field, so it must be in the form of `{document_field_name}` or `pages.{page_field_name}`. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Protobuf-FieldMask)) — Specifies which fields to include in the [ProcessResponse.document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessResponse#Google__Cloud__DocumentAI__V1__ProcessResponse_document_instance_ "Google::Cloud::DocumentAI::V1::ProcessResponse#document \(method\)") output. Only supports top-level document and pages field, so it must be in the form of `{document_field_name}` or `pages.{page_field_name}`. 



### #gcs_document
    
    
    def gcs_document() -> ::Google::Cloud::DocumentAI::V1::GcsDocument

**Returns**

  * ([::Google::Cloud::DocumentAI::V1::GcsDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-GcsDocument)) — A raw document on Google Cloud Storage.

Note: The following fields are mutually exclusive: `gcs_document`, `inline_document`, `raw_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #gcs_document=
    
    
    def gcs_document=(value) -> ::Google::Cloud::DocumentAI::V1::GcsDocument

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1::GcsDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-GcsDocument)) — A raw document on Google Cloud Storage.

Note: The following fields are mutually exclusive: `gcs_document`, `inline_document`, `raw_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DocumentAI::V1::GcsDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-GcsDocument)) — A raw document on Google Cloud Storage.

Note: The following fields are mutually exclusive: `gcs_document`, `inline_document`, `raw_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #imageless_mode
    
    
    def imageless_mode() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Option to remove images from the document. 



### #imageless_mode=
    
    
    def imageless_mode=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Option to remove images from the document. 



**Returns**

  * (::Boolean) — Optional. Option to remove images from the document. 



### #inline_document
    
    
    def inline_document() -> ::Google::Cloud::DocumentAI::V1::Document

**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document)) — An inline document proto.

Note: The following fields are mutually exclusive: `inline_document`, `raw_document`, `gcs_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #inline_document=
    
    
    def inline_document=(value) -> ::Google::Cloud::DocumentAI::V1::Document

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document)) — An inline document proto.

Note: The following fields are mutually exclusive: `inline_document`, `raw_document`, `gcs_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document)) — An inline document proto.

Note: The following fields are mutually exclusive: `inline_document`, `raw_document`, `gcs_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. 




### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints) and can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. The resource name of the [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Processor "Google::Cloud::DocumentAI::V1::Processor \(class\)") or [ProcessorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessorVersion "Google::Cloud::DocumentAI::V1::ProcessorVersion \(class\)") to use for processing. If a [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Processor "Google::Cloud::DocumentAI::V1::Processor \(class\)") is specified, the server will use its [default version][google.cloud.documentai.v1.Processor.default_processor_version]. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Processor "Google::Cloud::DocumentAI::V1::Processor \(class\)") or [ProcessorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessorVersion "Google::Cloud::DocumentAI::V1::ProcessorVersion \(class\)") to use for processing. If a [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Processor "Google::Cloud::DocumentAI::V1::Processor \(class\)") is specified, the server will use its [default version][google.cloud.documentai.v1.Processor.default_processor_version]. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`



**Returns**

  * (::String) — Required. The resource name of the [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Processor "Google::Cloud::DocumentAI::V1::Processor \(class\)") or [ProcessorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessorVersion "Google::Cloud::DocumentAI::V1::ProcessorVersion \(class\)") to use for processing. If a [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Processor "Google::Cloud::DocumentAI::V1::Processor \(class\)") is specified, the server will use its [default version][google.cloud.documentai.v1.Processor.default_processor_version]. Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`



### #process_options
    
    
    def process_options() -> ::Google::Cloud::DocumentAI::V1::ProcessOptions

**Returns**

  * ([::Google::Cloud::DocumentAI::V1::ProcessOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessOptions)) — Inference-time options for the process API 



### #process_options=
    
    
    def process_options=(value) -> ::Google::Cloud::DocumentAI::V1::ProcessOptions

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1::ProcessOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessOptions)) — Inference-time options for the process API 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1::ProcessOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-ProcessOptions)) — Inference-time options for the process API 



### #raw_document
    
    
    def raw_document() -> ::Google::Cloud::DocumentAI::V1::RawDocument

**Returns**

  * ([::Google::Cloud::DocumentAI::V1::RawDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-RawDocument)) — A raw document content (bytes).

Note: The following fields are mutually exclusive: `raw_document`, `inline_document`, `gcs_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #raw_document=
    
    
    def raw_document=(value) -> ::Google::Cloud::DocumentAI::V1::RawDocument

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1::RawDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-RawDocument)) — A raw document content (bytes).

Note: The following fields are mutually exclusive: `raw_document`, `inline_document`, `gcs_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DocumentAI::V1::RawDocument](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-RawDocument)) — A raw document content (bytes).

Note: The following fields are mutually exclusive: `raw_document`, `inline_document`, `gcs_document`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #skip_human_review
    
    
    def skip_human_review() -> ::Boolean

**Returns**

  * (::Boolean) — Whether human review should be skipped for this request. Default to `false`. 



### #skip_human_review=
    
    
    def skip_human_review=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether human review should be skipped for this request. Default to `false`. 



**Returns**

  * (::Boolean) — Whether human review should be skipped for this request. Default to `false`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
