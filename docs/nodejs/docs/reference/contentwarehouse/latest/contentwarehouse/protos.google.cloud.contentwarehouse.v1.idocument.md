---
url: https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.idocument
title: Interface protos.google.cloud.contentwarehouse.v1.IDocument (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:52.568197+00:00
---

# Interface protos.google.cloud.contentwarehouse.v1.IDocument (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.cloud.contentwarehouse.v1.idocument

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.contentwarehouse.v1.IDocument (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  1.10.0  1.9.0  1.7.0  1.5.0  1.4.0  1.3.0  0.5.1  0.4.0  0.3.1  0.1.2 

Properties of a Document.

## Package

[@google-cloud/contentwarehouse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)

## Properties 

### asyncEnabled
    
    
    asyncEnabled?: (boolean|null);

Document asyncEnabled

### cloudAiDocument
    
    
    cloudAiDocument?: (google.cloud.documentai.v1.IDocument|null);

Document cloudAiDocument

### contentCategory
    
    
    contentCategory?: (google.cloud.contentwarehouse.v1.ContentCategory|keyof typeof google.cloud.contentwarehouse.v1.ContentCategory|null);

Document contentCategory

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Document createTime

### creator
    
    
    creator?: (string|null);

Document creator

### displayName
    
    
    displayName?: (string|null);

Document displayName

### displayUri
    
    
    displayUri?: (string|null);

Document displayUri

### dispositionTime
    
    
    dispositionTime?: (google.protobuf.ITimestamp|null);

Document dispositionTime

### documentSchemaName
    
    
    documentSchemaName?: (string|null);

Document documentSchemaName

### inlineRawDocument
    
    
    inlineRawDocument?: (Uint8Array|Buffer|string|null);

Document inlineRawDocument

### legalHold
    
    
    legalHold?: (boolean|null);

Document legalHold

### name
    
    
    name?: (string|null);

Document name

### plainText
    
    
    plainText?: (string|null);

Document plainText

### properties
    
    
    properties?: (google.cloud.contentwarehouse.v1.IProperty[]|null);

Document properties

### rawDocumentFileType
    
    
    rawDocumentFileType?: (google.cloud.contentwarehouse.v1.RawDocumentFileType|keyof typeof google.cloud.contentwarehouse.v1.RawDocumentFileType|null);

Document rawDocumentFileType

### rawDocumentPath
    
    
    rawDocumentPath?: (string|null);

Document rawDocumentPath

### referenceId
    
    
    referenceId?: (string|null);

Document referenceId

### structuredContentUri
    
    
    structuredContentUri?: (string|null);

Document structuredContentUri

### textExtractionDisabled
    
    
    textExtractionDisabled?: (boolean|null);

Document textExtractionDisabled

### textExtractionEnabled
    
    
    textExtractionEnabled?: (boolean|null);

Document textExtractionEnabled

### title
    
    
    title?: (string|null);

Document title

### updater
    
    
    updater?: (string|null);

Document updater

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Document updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
