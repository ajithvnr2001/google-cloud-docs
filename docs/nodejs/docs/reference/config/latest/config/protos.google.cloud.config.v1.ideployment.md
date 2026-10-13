---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideployment
title: Interface protos.google.cloud.config.v1.IDeployment (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:20.526041+00:00
---

# Interface protos.google.cloud.config.v1.IDeployment (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideployment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.config.v1.IDeployment (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

Properties of a Deployment.

## Package

[@google-cloud/config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)

## Properties 

### annotations
    
    
    annotations?: ({ [k: string]: string }|null);

Deployment annotations

### artifactsGcsBucket
    
    
    artifactsGcsBucket?: (string|null);

Deployment artifactsGcsBucket

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Deployment createTime

### deleteBuild
    
    
    deleteBuild?: (string|null);

Deployment deleteBuild

### deleteLogs
    
    
    deleteLogs?: (string|null);

Deployment deleteLogs

### deleteResults
    
    
    deleteResults?: (google.cloud.config.v1.IApplyResults|null);

Deployment deleteResults

### errorCode
    
    
    errorCode?: (google.cloud.config.v1.Deployment.ErrorCode|keyof typeof google.cloud.config.v1.Deployment.ErrorCode|null);

Deployment errorCode

### errorLogs
    
    
    errorLogs?: (string|null);

Deployment errorLogs

### importExistingResources
    
    
    importExistingResources?: (boolean|null);

Deployment importExistingResources

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Deployment labels

### latestRevision
    
    
    latestRevision?: (string|null);

Deployment latestRevision

### lockState
    
    
    lockState?: (google.cloud.config.v1.Deployment.LockState|keyof typeof google.cloud.config.v1.Deployment.LockState|null);

Deployment lockState

### name
    
    
    name?: (string|null);

Deployment name

### providerConfig
    
    
    providerConfig?: (google.cloud.config.v1.IProviderConfig|null);

Deployment providerConfig

### quotaValidation
    
    
    quotaValidation?: (google.cloud.config.v1.QuotaValidation|keyof typeof google.cloud.config.v1.QuotaValidation|null);

Deployment quotaValidation

### serviceAccount
    
    
    serviceAccount?: (string|null);

Deployment serviceAccount

### state
    
    
    state?: (google.cloud.config.v1.Deployment.State|keyof typeof google.cloud.config.v1.Deployment.State|null);

Deployment state

### stateDetail
    
    
    stateDetail?: (string|null);

Deployment stateDetail

### terraformBlueprint
    
    
    terraformBlueprint?: (google.cloud.config.v1.ITerraformBlueprint|null);

Deployment terraformBlueprint

### tfErrors
    
    
    tfErrors?: (google.cloud.config.v1.ITerraformError[]|null);

Deployment tfErrors

### tfVersion
    
    
    tfVersion?: (string|null);

Deployment tfVersion

### tfVersionConstraint
    
    
    tfVersionConstraint?: (string|null);

Deployment tfVersionConstraint

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Deployment updateTime

### workerPool
    
    
    workerPool?: (string|null);

Deployment workerPool

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
