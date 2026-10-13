---
url: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1.iasset
title: Interface protos.google.cloud.asset.v1.IAsset (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:48.031034+00:00
---

# Interface protos.google.cloud.asset.v1.IAsset (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.cloud.asset.v1.iasset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.asset.v1.IAsset (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.3.3  5.5.0  5.3.0  5.2.0  5.1.0  5.0.1  4.6.3  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  3.23.1  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.1  3.15.5  3.14.1  3.13.0 

Properties of an Asset.

## Package

[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)

## Properties 

### accessLevel
    
    
    accessLevel?: (google.identity.accesscontextmanager.v1.IAccessLevel|null);

Asset accessLevel

### accessPolicy
    
    
    accessPolicy?: (google.identity.accesscontextmanager.v1.IAccessPolicy|null);

Asset accessPolicy

### ancestors
    
    
    ancestors?: (string[]|null);

Asset ancestors

### assetType
    
    
    assetType?: (string|null);

Asset assetType

### iamPolicy
    
    
    iamPolicy?: (google.iam.v1.IPolicy|null);

Asset iamPolicy

### name
    
    
    name?: (string|null);

Asset name

### orgPolicy
    
    
    orgPolicy?: (google.cloud.orgpolicy.v1.IPolicy[]|null);

Asset orgPolicy

### osInventory
    
    
    osInventory?: (google.cloud.osconfig.v1.IInventory|null);

Asset osInventory

### relatedAsset
    
    
    relatedAsset?: (google.cloud.asset.v1.IRelatedAsset|null);

Asset relatedAsset

### relatedAssets
    
    
    relatedAssets?: (google.cloud.asset.v1.IRelatedAssets|null);

Asset relatedAssets

### resource
    
    
    resource?: (google.cloud.asset.v1.IResource|null);

Asset resource

### servicePerimeter
    
    
    servicePerimeter?: (google.identity.accesscontextmanager.v1.IServicePerimeter|null);

Asset servicePerimeter

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Asset updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
