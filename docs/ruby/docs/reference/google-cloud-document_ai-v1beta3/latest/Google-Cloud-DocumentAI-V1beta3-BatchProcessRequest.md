---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchProcessRequest/
title: Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest (v0.49.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:53.505876+00:00
---

# Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest (v0.49.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchProcessRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Document AI V1beta3 API - Class Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest (v0.49.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.49.1 (latest)  0.49.0  0.48.1  0.47.0  0.46.2  0.45.0  0.44.0  0.43.1  0.42.0  0.41.0  0.40.0  0.39.1  0.38.0  0.37.0  0.36.1  0.35.0  0.34.0  0.33.1  0.32.0  0.31.0  0.30.2  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.4 

Reference documentation and code samples for the Document AI V1beta3 API class Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest.

Request message for [BatchProcessDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Client#Google__Cloud__DocumentAI__V1beta3__DocumentProcessorService__Client_batch_process_documents_instance_ "Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Client#batch_process_documents \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #document_output_config
    
    
    def document_output_config() -> ::Google::Cloud::DocumentAI::V1beta3::DocumentOutputConfig

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::DocumentOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentOutputConfig)) — The output configuration for the [BatchProcessDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Client#Google__Cloud__DocumentAI__V1beta3__DocumentProcessorService__Client_batch_process_documents_instance_ "Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Client#batch_process_documents \(method\)") method. 



### #document_output_config=
    
    
    def document_output_config=(value) -> ::Google::Cloud::DocumentAI::V1beta3::DocumentOutputConfig

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::DocumentOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentOutputConfig)) — The output configuration for the [BatchProcessDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Client#Google__Cloud__DocumentAI__V1beta3__DocumentProcessorService__Client_batch_process_documents_instance_ "Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Client#batch_process_documents \(method\)") method. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::DocumentOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentOutputConfig)) — The output configuration for the [BatchProcessDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Client#Google__Cloud__DocumentAI__V1beta3__DocumentProcessorService__Client_batch_process_documents_instance_ "Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Client#batch_process_documents \(method\)") method. 



### #input_configs
    
    
    def input_configs() -> ::Array<::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchInputConfig>

**Returns**

  * (::Array<[::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchProcessRequest-BatchInputConfig)>) — The input config for each single document in the batch process. 



### #input_configs=
    
    
    def input_configs=(value) -> ::Array<::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchInputConfig>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchProcessRequest-BatchInputConfig)>) — The input config for each single document in the batch process. 



**Returns**

  * (::Array<[::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchProcessRequest-BatchInputConfig)>) — The input config for each single document in the batch process. 



### #input_documents
    
    
    def input_documents() -> ::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchDocumentsInputConfig)) — The input documents for the [BatchProcessDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Client#Google__Cloud__DocumentAI__V1beta3__DocumentProcessorService__Client_batch_process_documents_instance_ "Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Client#batch_process_documents \(method\)") method. 



### #input_documents=
    
    
    def input_documents=(value) -> ::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchDocumentsInputConfig)) — The input documents for the [BatchProcessDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Client#Google__Cloud__DocumentAI__V1beta3__DocumentProcessorService__Client_batch_process_documents_instance_ "Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Client#batch_process_documents \(method\)") method. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::BatchDocumentsInputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchDocumentsInputConfig)) — The input documents for the [BatchProcessDocuments](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-DocumentProcessorService-Client#Google__Cloud__DocumentAI__V1beta3__DocumentProcessorService__Client_batch_process_documents_instance_ "Google::Cloud::DocumentAI::V1beta3::DocumentProcessorService::Client#batch_process_documents \(method\)") method. 



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

  * (::String) — Required. The resource name of [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Processor "Google::Cloud::DocumentAI::V1beta3::Processor \(class\)") or [ProcessorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ProcessorVersion "Google::Cloud::DocumentAI::V1beta3::ProcessorVersion \(class\)"). Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Processor "Google::Cloud::DocumentAI::V1beta3::Processor \(class\)") or [ProcessorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ProcessorVersion "Google::Cloud::DocumentAI::V1beta3::ProcessorVersion \(class\)"). Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`



**Returns**

  * (::String) — Required. The resource name of [Processor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-Processor "Google::Cloud::DocumentAI::V1beta3::Processor \(class\)") or [ProcessorVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ProcessorVersion "Google::Cloud::DocumentAI::V1beta3::ProcessorVersion \(class\)"). Format: `projects/{project}/locations/{location}/processors/{processor}`, or `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processorVersion}`



### #output_config
    
    
    def output_config() -> ::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchOutputConfig

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchProcessRequest-BatchOutputConfig)) — The overall output config for batch process. 



### #output_config=
    
    
    def output_config=(value) -> ::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchOutputConfig

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchProcessRequest-BatchOutputConfig)) — The overall output config for batch process. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::BatchProcessRequest::BatchOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-BatchProcessRequest-BatchOutputConfig)) — The overall output config for batch process. 



### #process_options
    
    
    def process_options() -> ::Google::Cloud::DocumentAI::V1beta3::ProcessOptions

**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::ProcessOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ProcessOptions)) — Inference-time options for the process API 



### #process_options=
    
    
    def process_options=(value) -> ::Google::Cloud::DocumentAI::V1beta3::ProcessOptions

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1beta3::ProcessOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ProcessOptions)) — Inference-time options for the process API 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1beta3::ProcessOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1beta3/latest/Google-Cloud-DocumentAI-V1beta3-ProcessOptions)) — Inference-time options for the process API 



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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
