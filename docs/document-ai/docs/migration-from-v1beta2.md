---
url: https://docs.cloud.google.com/document-ai/docs/migration-from-v1beta2/
title: Migrating from V1Beta2 \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:45.134099+00:00
---

# Migrating from V1Beta2  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/migration-from-v1beta2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  Migrating from V1Beta2 Stay organized with collections  Save and categorize content based on your preferences. 

Document AI's `v1beta2` API is now deprecated in favor of the [`v1`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors) API.

Unlike `v1beta2`, Document AI [`v1`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors) is a stateful API, meaning you need to create a [`Processor`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#resource:-processor) before you can send requests to [`Process`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/process) and [`BatchProcess`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/batchProcess) documents.

NOTE: This deprecation only affects the version of the API used to call any processor. It does not affect the availability of any processor.

The major areas of v1 API backward incompatibility with v1beta2 API are discussed later in this document.

### Creating a processor

To migrate to `v1` for processor creation, first create a [`Processor`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#resource:-processor). The following table serves as a general guideline for choosing an appropriate [`ProcessorType`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processorTypes#resource:-processortype) to create, but you can consult the full [processor list](https://docs.cloud.google.com/document-ai/docs/processors-list).

`document_type` | `params` | Processor type  
---|---|---  
`invoice` |  | [`INVOICE_PROCESSOR`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor)  
`general` |  | [`OCR_PROCESSOR`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-ocr)  
`general` | `table_extraction_params` | [`FORM_PARSER_PROCESSOR`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_form-parser)  
`general` | `form_extraction_params` | [`FORM_PARSER_PROCESSOR`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_form-parser)  
`general` | `entity_extraction_params` | [`FORM_PARSER_PROCESSOR`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_form-parser)  
`general` | `automl_params` | [`CUSTOM_EXTRACTION_PROCESSOR`](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde)  
  
For a step-by-step guide to creating a processor, view the [guide](https://docs.cloud.google.com/document-ai/docs/create-processor).

### Processing documents

Document AI `v1` has two APIs to accept documents: [`Process`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/process) and [`BatchProcess`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/batchProcess). Each of these methods corresponds to a method from `v1beta2`. The methods and their differences are highlighted:

`v1beta2` Method | `v1` Method | Migration notes  
---|---|---  
`ProcessDocument` | [`Process`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/process) | `InputConfig.Cloud Storage_source` not supported in `v1`, use `BatchProcess` to process documents on Cloud Storage.  
`BatchProcessDocuments` | [`BatchProcess`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/batchProcess) | In addition to accepting individual documents on Cloud Storage, `v1` supports a Cloud Storage prefix to process many documents at once.  
  
### Client libraries

If using the [`Client Libraries`](https://docs.cloud.google.com/document-ai/docs/libraries) to interact with Document AI, switch from using the `DocumentUnderstandingService` to the `DocumentProcessorService`. For a detailed example of using the client libraries for `v1`, see [client libraries](https://docs.cloud.google.com/document-ai/docs/libraries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
