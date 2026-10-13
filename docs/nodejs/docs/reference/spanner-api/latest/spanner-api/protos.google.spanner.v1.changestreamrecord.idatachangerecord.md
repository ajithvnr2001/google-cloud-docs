---
url: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.changestreamrecord.idatachangerecord
title: Interface protos.google.spanner.v1.ChangeStreamRecord.IDataChangeRecord (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:18.147734+00:00
---

# Interface protos.google.spanner.v1.ChangeStreamRecord.IDataChangeRecord (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.v1.changestreamrecord.idatachangerecord

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.spanner.v1.ChangeStreamRecord.IDataChangeRecord (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Properties of a DataChangeRecord.

## Package

[@google-cloud/spanner-api](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/overview.html)

## Properties 

### columnMetadata
    
    
    columnMetadata?: (google.spanner.v1.ChangeStreamRecord.DataChangeRecord.IColumnMetadata[]|null);

DataChangeRecord columnMetadata

### commitTimestamp
    
    
    commitTimestamp?: (google.protobuf.ITimestamp|null);

DataChangeRecord commitTimestamp

### isLastRecordInTransactionInPartition
    
    
    isLastRecordInTransactionInPartition?: (boolean|null);

DataChangeRecord isLastRecordInTransactionInPartition

### isSystemTransaction
    
    
    isSystemTransaction?: (boolean|null);

DataChangeRecord isSystemTransaction

### mods
    
    
    mods?: (google.spanner.v1.ChangeStreamRecord.DataChangeRecord.IMod[]|null);

DataChangeRecord mods

### modType
    
    
    modType?: (google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ModType|keyof typeof google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ModType|null);

DataChangeRecord modType

### numberOfPartitionsInTransaction
    
    
    numberOfPartitionsInTransaction?: (number|null);

DataChangeRecord numberOfPartitionsInTransaction

### numberOfRecordsInTransaction
    
    
    numberOfRecordsInTransaction?: (number|null);

DataChangeRecord numberOfRecordsInTransaction

### recordSequence
    
    
    recordSequence?: (string|null);

DataChangeRecord recordSequence

### serverTransactionId
    
    
    serverTransactionId?: (string|null);

DataChangeRecord serverTransactionId

### table
    
    
    table?: (string|null);

DataChangeRecord table

### transactionTag
    
    
    transactionTag?: (string|null);

DataChangeRecord transactionTag

### valueCaptureType
    
    
    valueCaptureType?: (google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ValueCaptureType|keyof typeof google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ValueCaptureType|null);

DataChangeRecord valueCaptureType

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
