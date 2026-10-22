---
url: https://docs.cloud.google.com/document-ai/limits/
title: Limits \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:46.675629+00:00
---

# Limits  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Resources ](https://docs.cloud.google.com/document-ai/docs/resources)



Send feedback 

#  Limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the system limits that apply to Document AI. Unlike quotas, system limits can't be changed.

## Content limits

The following content limits apply to all Document AI processors.

**Note:** Document AI also enforces usage limits depending on the processor you are using. See Processor limits for more information.Content limit | Value  
---|---  
Maximum image resolution   
(limit does not apply to PDF files) | 40 megapixels (per page if image contains multiple pages)   
Maximum file size for [online processing](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/process) requests | 40 MB  
Maximum file size for [batch processing](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/batchProcess) requests | 1 GB  
Files per [batch processing](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/batchProcess) request | 5,000 files  
  
## Processor limits

Limits are defined in the current list.

**Note:** To extend the maximum page limit for online and synchronous requests up to 30, enable `imageless_mode` in [`ProcessRequest`](https://docs.cloud.google.com/document-ai/docs/reference/rpc/google.cloud.documentai.v1#processrequest). This extended limit is only applicable when processing pages contiguously starting from page 1.

### Extraction processors

Processor | Limits  
---|---  
[**Custom Extractor**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_cde) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 200  
Maximum pages (imageless mode online/synchronous requests): | 30  
[**Form Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_form-parser) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 100  
Maximum pages (imageless mode online/synchronous requests): | 30  
[**Layout Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_layout-parser) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 500  
Maximum pages (imageless mode online/synchronous requests): | 30  
  
**Note:** For the Custom Document Extractor, documents with checkboxes have a maximum page limit (online and batch) of 10 pages.

### Classification processors

Processor | Limits  
---|---  
[**Custom Classifier**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_CUSTOM_CLASSIFICATION_PROCESSOR) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 200  
Maximum pages (imageless mode online/synchronous requests): | 30  
[**Custom Splitter**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_CUSTOM_SPLITTING_PROCESSOR) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 1000  
Maximum pages (imageless mode online/synchronous requests): | 30  
  
### Digitize processors

Processor | Limits  
---|---  
[**Enterprise Document OCR (Optical Character Recognition)**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_doc-ocr) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 500  
Maximum pages (imageless mode online/synchronous requests): | 30  
  
### Pretrained processors

Processor | Limits  
---|---  
[**Bank Statement Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_bank-statement-parser) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 30  
Maximum pages (imageless mode online/synchronous requests): | 30  
[**W2 Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_w2-parser) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 15  
Maximum pages (imageless mode online/synchronous requests): | 15  
[**Identity Document Proofing Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_id-proofing-parser) |  | Maximum pages (online/synchronous requests): | 2  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 2  
Maximum pages (imageless mode online/synchronous requests): | 2  
[**Pay Slip Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_pay-slip-parser) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 50  
Maximum pages (imageless mode online/synchronous requests): | 30  
[**US Driver License Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_us-driver-license-parser) |  | Maximum pages (online/synchronous requests): | 2  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 2  
Maximum pages (imageless mode online/synchronous requests): | 2  
[**Expense Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_expense-parser) |  | Maximum pages (online/synchronous requests): | 10  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 10  
Maximum pages (imageless mode online/synchronous requests): | 10  
[**Invoice Parser**](https://docs.cloud.google.com/document-ai/docs/processors-list#processor_invoice-processor) |  | Maximum pages (online/synchronous requests): | 15  
---|---  
Maximum pages (batch/offline/asynchronous requests): | 200  
Maximum pages (imageless mode online/synchronous requests): | 30  
  
## Limitations for Document AI

Document AI has the current limitations.

Criteria | Stable release July 2023 | Dataset | 

  * Maximum of 30,000 documents total
  * Maximum of 250,000 pages total

  
---|---  
Processing time | 

Batch jobs are processed asynchronously and are not designed for real-time applications. Most jobs finish within 12 to 24 hours after they start running (not counting the queue time). After 24 hours, incomplete jobs are canceled. You're only charged for completed requests. 
  
Document import | 

  * Maximum of 5,000 documents per import
  * Maximum of 200 pages per document

  
Limits to train a Custom Document Extractor (CDE) | Model-based training [(GA)](https://cloud.google.com/products#product-launch-stages)  


  * Training dataset maximums: 25,000 documents; 100,000 pages
  * Training dataset minimum: each label needs to be present on at least 1 label per 10 documents
  * Test dataset maximums: 2,000 documents; 8,000 pages
  * Test dataset minimum: every label on at least 10 documents
  * Maximum of 200 pages per document

  
Template-based training [(GA)](https://cloud.google.com/products#product-launch-stages)  


  * Training dataset maximums: 300 documents, 300 pages
  * Training dataset minimum: every label on at least on at least 3 documents
  * Test dataset maximums: 2,000 documents; 8,000 pages
  * Test dataset minimum: every label on at least 3 documents
  * Maximum of 20 pages per document

  
Limits to train a Custom Document Classifier (CDC) or a Custom Document Splitter (CDS) | 

  * Training dataset maximums: 30,000 documents; 100,000 pages
  * Training dataset minimum: every label on at least 10 documents
  * Test dataset maximums: 2,000 documents; 8,000 pages
  * Test dataset minimum: every label on at least 2 documents
  * Maximum of 200 pages per document

  
Labeling | 

  * To get started, verify document labels meet defined minimum training and evaluation thresholds.
  * To begin evaluating model performance for documents with layout variation, label at least 100 documents. Specifically, verify that each label exists on 50 documents in training and 50 in evaluation.
  * Maximum allowed labels (fields): 150
  * Label size limits (characters): Long items aren't well supported, but there's no explicit limit. Chunk documents into 800- or 1,000-token pieces, with 100 to 200 tokens overlapping between chunks. (Items longer than the overlapping area might run into quality issues.)
  * Label occurrences in a document: No limit

  
Geographic coverage | 

  * Regions generally supported: US, EU (multiregion)
  * Regions with limited accessibility: Germany, Singapore, UK, Canada, India, Australia

  
  
[ Previous arrow_back  Quotas  ](https://docs.cloud.google.com/document-ai/quotas)

[ Next Capacity reservation  arrow_forward  ](https://docs.cloud.google.com/document-ai/capacity-reservation)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
