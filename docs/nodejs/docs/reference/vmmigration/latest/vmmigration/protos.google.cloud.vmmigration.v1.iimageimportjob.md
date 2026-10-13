---
url: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iimageimportjob
title: Interface protos.google.cloud.vmmigration.v1.IImageImportJob (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:56.368829+00:00
---

# Interface protos.google.cloud.vmmigration.v1.IImageImportJob (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iimageimportjob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.vmmigration.v1.IImageImportJob (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.2  2.3.2  2.2.1  2.1.0  1.0.0  0.2.0 

Properties of an ImageImportJob.

## Package

[@google-cloud/vmmigration](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)

## Properties 

### cloudStorageUri
    
    
    cloudStorageUri?: (string|null);

ImageImportJob cloudStorageUri

### createdResources
    
    
    createdResources?: (string[]|null);

ImageImportJob createdResources

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

ImageImportJob createTime

### diskImageTargetDetails
    
    
    diskImageTargetDetails?: (google.cloud.vmmigration.v1.IDiskImageTargetDetails|null);

ImageImportJob diskImageTargetDetails

### endTime
    
    
    endTime?: (google.protobuf.ITimestamp|null);

ImageImportJob endTime

### errors
    
    
    errors?: (google.rpc.IStatus[]|null);

ImageImportJob errors

### machineImageTargetDetails
    
    
    machineImageTargetDetails?: (google.cloud.vmmigration.v1.IMachineImageTargetDetails|null);

ImageImportJob machineImageTargetDetails

### name
    
    
    name?: (string|null);

ImageImportJob name

### state
    
    
    state?: (google.cloud.vmmigration.v1.ImageImportJob.State|keyof typeof google.cloud.vmmigration.v1.ImageImportJob.State|null);

ImageImportJob state

### steps
    
    
    steps?: (google.cloud.vmmigration.v1.IImageImportStep[]|null);

ImageImportJob steps

### warnings
    
    
    warnings?: (google.cloud.vmmigration.v1.IMigrationWarning[]|null);

ImageImportJob warnings

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
