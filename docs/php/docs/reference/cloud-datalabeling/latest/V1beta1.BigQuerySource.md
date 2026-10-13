---
url: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.BigQuerySource
title: Google Cloud Datalabeling V1beta1 Client - Class BigQuerySource (0.8.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:46.389668+00:00
---

# Google Cloud Datalabeling V1beta1 Client - Class BigQuerySource (0.8.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.BigQuerySource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Datalabeling V1beta1 Client - Class BigQuerySource (0.8.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.3 (latest)  0.7.2  0.6.3  0.5.7  0.4.2  0.3.1  0.2.0  0.1.14 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Datalabeling V1beta1 Client class BigQuerySource.

The BigQuery location for input data. If used in an [EvaluationJob](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.EvaluationJob), this is where the service saves the prediction input and output sampled from the model version.

Generated from protobuf message `google.cloud.datalabeling.v1beta1.BigQuerySource`

## Namespace

Google \ Cloud \ DataLabeling \ V1beta1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ input_uri` |  `string`   
Required. BigQuery URI to a table, up to 2,000 characters long. If you specify the URI of a table that does not exist, Data Labeling Service creates a table at the URI with the correct schema when you create your [EvaluationJob](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.EvaluationJob). If you specify the URI of a table that already exists, it must have the [correct schema](https://docs.cloud.google.com/ml-engine/docs/continuous-evaluation/create-job#table-schema). Provide the table URI in the following format: "bq://{your_project_id}/{your_dataset_name}/{your_table_name}" [Learn more](https://docs.cloud.google.com/ml-engine/docs/continuous-evaluation/create-job#table-schema).  
  
### getInputUri

Required. BigQuery URI to a table, up to 2,000 characters long. If you specify the URI of a table that does not exist, Data Labeling Service creates a table at the URI with the correct schema when you create your [EvaluationJob](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.EvaluationJob). If you specify the URI of a table that already exists, it must have the [correct schema](https://docs.cloud.google.com/ml-engine/docs/continuous-evaluation/create-job#table-schema).

Provide the table URI in the following format: "bq://{your_project_id}/{your_dataset_name}/{your_table_name}" [Learn more](https://docs.cloud.google.com/ml-engine/docs/continuous-evaluation/create-job#table-schema).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setInputUri

Required. BigQuery URI to a table, up to 2,000 characters long. If you specify the URI of a table that does not exist, Data Labeling Service creates a table at the URI with the correct schema when you create your [EvaluationJob](https://docs.cloud.google.com/php/docs/reference/cloud-datalabeling/latest/V1beta1.EvaluationJob). If you specify the URI of a table that already exists, it must have the [correct schema](https://docs.cloud.google.com/ml-engine/docs/continuous-evaluation/create-job#table-schema).

Provide the table URI in the following format: "bq://{your_project_id}/{your_dataset_name}/{your_table_name}" [Learn more](https://docs.cloud.google.com/ml-engine/docs/continuous-evaluation/create-job#table-schema).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
