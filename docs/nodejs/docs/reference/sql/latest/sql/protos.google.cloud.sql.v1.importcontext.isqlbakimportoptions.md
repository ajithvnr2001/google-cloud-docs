---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.importcontext.isqlbakimportoptions
title: Interface protos.google.cloud.sql.v1.ImportContext.ISqlBakImportOptions (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:03.781147+00:00
---

# Interface protos.google.cloud.sql.v1.ImportContext.ISqlBakImportOptions (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1.importcontext.isqlbakimportoptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.sql.v1.ImportContext.ISqlBakImportOptions (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Properties of a SqlBakImportOptions.

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Properties 

### bakType
    
    
    bakType?: (google.cloud.sql.v1.BakType|keyof typeof google.cloud.sql.v1.BakType|null);

SqlBakImportOptions bakType

### encryptionOptions
    
    
    encryptionOptions?: (google.cloud.sql.v1.ImportContext.SqlBakImportOptions.IEncryptionOptions|null);

SqlBakImportOptions encryptionOptions

### noRecovery
    
    
    noRecovery?: (google.protobuf.IBoolValue|null);

SqlBakImportOptions noRecovery

### recoveryOnly
    
    
    recoveryOnly?: (google.protobuf.IBoolValue|null);

SqlBakImportOptions recoveryOnly

### stopAt
    
    
    stopAt?: (google.protobuf.ITimestamp|null);

SqlBakImportOptions stopAt

### stopAtMark
    
    
    stopAtMark?: (string|null);

SqlBakImportOptions stopAtMark

### striped
    
    
    striped?: (google.protobuf.IBoolValue|null);

SqlBakImportOptions striped

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
