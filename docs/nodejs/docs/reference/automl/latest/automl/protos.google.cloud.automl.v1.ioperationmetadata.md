---
url: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ioperationmetadata
title: Interface protos.google.cloud.automl.v1.IOperationMetadata (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:41.406717+00:00
---

# Interface protos.google.cloud.automl.v1.IOperationMetadata (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/automl/protos.google.cloud.automl.v1.ioperationmetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.automl.v1.IOperationMetadata (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.1.3  4.0.1  3.1.2  2.5.2  2.4.5 

Properties of an OperationMetadata.

## Package

[@google-cloud/automl](https://docs.cloud.google.com/nodejs/docs/reference/automl/latest/overview.html)

## Properties 

### batchPredictDetails
    
    
    batchPredictDetails?: (google.cloud.automl.v1.IBatchPredictOperationMetadata|null);

OperationMetadata batchPredictDetails

### createDatasetDetails
    
    
    createDatasetDetails?: (google.cloud.automl.v1.ICreateDatasetOperationMetadata|null);

OperationMetadata createDatasetDetails

### createModelDetails
    
    
    createModelDetails?: (google.cloud.automl.v1.ICreateModelOperationMetadata|null);

OperationMetadata createModelDetails

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

OperationMetadata createTime

### deleteDetails
    
    
    deleteDetails?: (google.cloud.automl.v1.IDeleteOperationMetadata|null);

OperationMetadata deleteDetails

### deployModelDetails
    
    
    deployModelDetails?: (google.cloud.automl.v1.IDeployModelOperationMetadata|null);

OperationMetadata deployModelDetails

### exportDataDetails
    
    
    exportDataDetails?: (google.cloud.automl.v1.IExportDataOperationMetadata|null);

OperationMetadata exportDataDetails

### exportModelDetails
    
    
    exportModelDetails?: (google.cloud.automl.v1.IExportModelOperationMetadata|null);

OperationMetadata exportModelDetails

### importDataDetails
    
    
    importDataDetails?: (google.cloud.automl.v1.IImportDataOperationMetadata|null);

OperationMetadata importDataDetails

### partialFailures
    
    
    partialFailures?: (google.rpc.IStatus[]|null);

OperationMetadata partialFailures

### progressPercent
    
    
    progressPercent?: (number|null);

OperationMetadata progressPercent

### undeployModelDetails
    
    
    undeployModelDetails?: (google.cloud.automl.v1.IUndeployModelOperationMetadata|null);

OperationMetadata undeployModelDetails

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

OperationMetadata updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
