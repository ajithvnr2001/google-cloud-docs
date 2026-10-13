---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Processor-State/
title: Document AI V1 API - Module Google::Cloud::DocumentAI::V1::Processor::State (v1.13.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:29.236556+00:00
---

# Document AI V1 API - Module Google::Cloud::DocumentAI::V1::Processor::State (v1.13.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Processor-State/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Document AI V1 API - Module Google::Cloud::DocumentAI::V1::Processor::State (v1.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.1 (latest)  1.13.0  1.12.1  1.11.0  1.10.2  1.9.0  1.8.0  1.7.0  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.23.1  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.2  0.16.2  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 

Reference documentation and code samples for the Document AI V1 API module Google::Cloud::DocumentAI::V1::Processor::State.

The possible states of the processor.

## Constants 

### STATE_UNSPECIFIED

**value:** 0  
The processor is in an unspecified state.

### ENABLED

**value:** 1  
The processor is enabled, i.e., has an enabled version which can currently serve processing requests and all the feature dependencies have been successfully initialized.

### DISABLED

**value:** 2  
The processor is disabled.

### ENABLING

**value:** 3  
The processor is being enabled, will become `ENABLED` if successful.

### DISABLING

**value:** 4  
The processor is being disabled, will become `DISABLED` if successful.

### CREATING

**value:** 5  
The processor is being created, will become either `ENABLED` (for successful creation) or `FAILED` (for failed ones). Once a processor is in this state, it can then be used for document processing, but the feature dependencies of the processor might not be fully created yet.

### FAILED

**value:** 6  
The processor failed during creation or initialization of feature dependencies. The user should delete the processor and recreate one as all the functionalities of the processor are disabled.

### DELETING

**value:** 7  
The processor is being deleted, will be removed if successful.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
