---
url: https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.itransferspec
title: Interface protos.google.storagetransfer.v1.ITransferSpec (5.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:22.401733+00:00
---

# Interface protos.google.storagetransfer.v1.ITransferSpec (5.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.itransferspec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.storagetransfer.v1.ITransferSpec (5.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  4.0.1  3.6.0  3.5.0  3.4.0  3.0.0  2.3.2  2.2.1  2.1.1  1.2.0  1.1.1  1.0.1 

Properties of a TransferSpec.

## Package

[@google-cloud/storage-transfer](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/overview.html)

## Properties 

### awsS3CompatibleDataSource
    
    
    awsS3CompatibleDataSource?: (google.storagetransfer.v1.IAwsS3CompatibleData|null);

TransferSpec awsS3CompatibleDataSource

### awsS3DataSource
    
    
    awsS3DataSource?: (google.storagetransfer.v1.IAwsS3Data|null);

TransferSpec awsS3DataSource

### azureBlobStorageDataSource
    
    
    azureBlobStorageDataSource?: (google.storagetransfer.v1.IAzureBlobStorageData|null);

TransferSpec azureBlobStorageDataSource

### gcsDataSink
    
    
    gcsDataSink?: (google.storagetransfer.v1.IGcsData|null);

TransferSpec gcsDataSink

### gcsDataSource
    
    
    gcsDataSource?: (google.storagetransfer.v1.IGcsData|null);

TransferSpec gcsDataSource

### gcsIntermediateDataLocation
    
    
    gcsIntermediateDataLocation?: (google.storagetransfer.v1.IGcsData|null);

TransferSpec gcsIntermediateDataLocation

### hdfsDataSource
    
    
    hdfsDataSource?: (google.storagetransfer.v1.IHdfsData|null);

TransferSpec hdfsDataSource

### httpDataSource
    
    
    httpDataSource?: (google.storagetransfer.v1.IHttpData|null);

TransferSpec httpDataSource

### objectConditions
    
    
    objectConditions?: (google.storagetransfer.v1.IObjectConditions|null);

TransferSpec objectConditions

### posixDataSink
    
    
    posixDataSink?: (google.storagetransfer.v1.IPosixFilesystem|null);

TransferSpec posixDataSink

### posixDataSource
    
    
    posixDataSource?: (google.storagetransfer.v1.IPosixFilesystem|null);

TransferSpec posixDataSource

### sinkAgentPoolName
    
    
    sinkAgentPoolName?: (string|null);

TransferSpec sinkAgentPoolName

### sourceAgentPoolName
    
    
    sourceAgentPoolName?: (string|null);

TransferSpec sourceAgentPoolName

### transferManifest
    
    
    transferManifest?: (google.storagetransfer.v1.ITransferManifest|null);

TransferSpec transferManifest

### transferOptions
    
    
    transferOptions?: (google.storagetransfer.v1.ITransferOptions|null);

TransferSpec transferOptions

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
