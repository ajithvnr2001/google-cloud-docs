---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportEvaluatedExamplesOperationMetadata-ExportEvaluatedExamplesOutputInfo/
title: Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata::ExportEvaluatedExamplesOutputInfo (v0.19.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:13.796140+00:00
---

# Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata::ExportEvaluatedExamplesOutputInfo (v0.19.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportEvaluatedExamplesOperationMetadata-ExportEvaluatedExamplesOutputInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1beta1 API - Class Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata::ExportEvaluatedExamplesOutputInfo (v0.19.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.1  0.13.1  0.12.0  0.11.1  0.10.2  0.9.0  0.8.0  0.7.0  0.6.1  0.5.5 

Reference documentation and code samples for the Cloud AutoML V1beta1 API class Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOperationMetadata::ExportEvaluatedExamplesOutputInfo.

Further describes the output of the evaluated examples export. Supplements

[ExportEvaluatedExamplesOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1beta1/latest/Google-Cloud-AutoML-V1beta1-ExportEvaluatedExamplesOutputConfig "Google::Cloud::AutoML::V1beta1::ExportEvaluatedExamplesOutputConfig \(class\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bigquery_output_dataset
    
    
    def bigquery_output_dataset() -> ::String

**Returns**

  * (::String) — The path of the BigQuery dataset created, in bq://projectId.bqDatasetId format, into which the output of export evaluated examples is written. 



### #bigquery_output_dataset=
    
    
    def bigquery_output_dataset=(value) -> ::String

**Parameter**

  * **value** (::String) — The path of the BigQuery dataset created, in bq://projectId.bqDatasetId format, into which the output of export evaluated examples is written. 



**Returns**

  * (::String) — The path of the BigQuery dataset created, in bq://projectId.bqDatasetId format, into which the output of export evaluated examples is written. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
