---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataqualityresult
title: Interface protos.google.cloud.dataplex.v1.IDataQualityResult (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:56.950036+00:00
---

# Interface protos.google.cloud.dataplex.v1.IDataQualityResult (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.idataqualityresult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.dataplex.v1.IDataQualityResult (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Properties of a DataQualityResult.

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Properties 

### anomalyDetectionGeneratedAssets
    
    
    anomalyDetectionGeneratedAssets?: (google.cloud.dataplex.v1.DataQualityResult.IAnomalyDetectionGeneratedAssets|null);

DataQualityResult anomalyDetectionGeneratedAssets

### catalogPublishingStatus
    
    
    catalogPublishingStatus?: (google.cloud.dataplex.v1.IDataScanCatalogPublishingStatus|null);

DataQualityResult catalogPublishingStatus

### columns
    
    
    columns?: (google.cloud.dataplex.v1.IDataQualityColumnResult[]|null);

DataQualityResult columns

### dimensions
    
    
    dimensions?: (google.cloud.dataplex.v1.IDataQualityDimensionResult[]|null);

DataQualityResult dimensions

### passed
    
    
    passed?: (boolean|null);

DataQualityResult passed

### postScanActionsResult
    
    
    postScanActionsResult?: (google.cloud.dataplex.v1.DataQualityResult.IPostScanActionsResult|null);

DataQualityResult postScanActionsResult

### rowCount
    
    
    rowCount?: (number|Long|string|null);

DataQualityResult rowCount

### rules
    
    
    rules?: (google.cloud.dataplex.v1.IDataQualityRuleResult[]|null);

DataQualityResult rules

### scannedData
    
    
    scannedData?: (google.cloud.dataplex.v1.IScannedData|null);

DataQualityResult scannedData

### score
    
    
    score?: (number|null);

DataQualityResult score

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
