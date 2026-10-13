---
url: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportjob
title: Interface protos.google.cloud.kms.v1.IImportJob (6.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:01.489170+00:00
---

# Interface protos.google.cloud.kms.v1.IImportJob (6.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/kms/protos.google.cloud.kms.v1.iimportjob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.kms.v1.IImportJob (6.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.2.1 (latest)  5.7.0  5.6.0  5.3.0  4.5.0  4.3.0  3.5.1  3.4.0  3.3.1  3.1.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.0  2.6.0  2.5.0  2.4.4  2.3.3 

Properties of an ImportJob.

## Package

[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)

## Properties 

### attestation
    
    
    attestation?: (google.cloud.kms.v1.IKeyOperationAttestation|null);

ImportJob attestation

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

ImportJob createTime

### cryptoKeyBackend
    
    
    cryptoKeyBackend?: (string|null);

ImportJob cryptoKeyBackend

### expireEventTime
    
    
    expireEventTime?: (google.protobuf.ITimestamp|null);

ImportJob expireEventTime

### expireTime
    
    
    expireTime?: (google.protobuf.ITimestamp|null);

ImportJob expireTime

### generateTime
    
    
    generateTime?: (google.protobuf.ITimestamp|null);

ImportJob generateTime

### importMethod
    
    
    importMethod?: (google.cloud.kms.v1.ImportJob.ImportMethod|keyof typeof google.cloud.kms.v1.ImportJob.ImportMethod|null);

ImportJob importMethod

### name
    
    
    name?: (string|null);

ImportJob name

### protectionLevel
    
    
    protectionLevel?: (google.cloud.kms.v1.ProtectionLevel|keyof typeof google.cloud.kms.v1.ProtectionLevel|null);

ImportJob protectionLevel

### publicKey
    
    
    publicKey?: (google.cloud.kms.v1.ImportJob.IWrappingPublicKey|null);

ImportJob publicKey

### publicKeyFormat
    
    
    publicKeyFormat?: (google.cloud.kms.v1.PublicKey.PublicKeyFormat|keyof typeof google.cloud.kms.v1.PublicKey.PublicKeyFormat|null);

ImportJob publicKeyFormat

### state
    
    
    state?: (google.cloud.kms.v1.ImportJob.ImportJobState|keyof typeof google.cloud.kms.v1.ImportJob.ImportJobState|null);

ImportJob state

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
