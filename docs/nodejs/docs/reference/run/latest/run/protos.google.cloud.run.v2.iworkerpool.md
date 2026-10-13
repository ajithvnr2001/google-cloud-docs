---
url: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.iworkerpool
title: Interface protos.google.cloud.run.v2.IWorkerPool (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:51.620408+00:00
---

# Interface protos.google.cloud.run.v2.IWorkerPool (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.iworkerpool

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.run.v2.IWorkerPool (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.3.0  3.2.0  2.1.0  1.5.0  1.0.2  0.5.0  0.4.2  0.2.3 

Properties of a WorkerPool.

## Package

[@google-cloud/run](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/overview.html)

## Properties 

### annotations
    
    
    annotations?: ({ [k: string]: string }|null);

WorkerPool annotations

### binaryAuthorization
    
    
    binaryAuthorization?: (google.cloud.run.v2.IBinaryAuthorization|null);

WorkerPool binaryAuthorization

### client
    
    
    client?: (string|null);

WorkerPool client

### clientVersion
    
    
    clientVersion?: (string|null);

WorkerPool clientVersion

### conditions
    
    
    conditions?: (google.cloud.run.v2.ICondition[]|null);

WorkerPool conditions

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

WorkerPool createTime

### creator
    
    
    creator?: (string|null);

WorkerPool creator

### customAudiences
    
    
    customAudiences?: (string[]|null);

WorkerPool customAudiences

### deleteTime
    
    
    deleteTime?: (google.protobuf.ITimestamp|null);

WorkerPool deleteTime

### description
    
    
    description?: (string|null);

WorkerPool description

### etag
    
    
    etag?: (string|null);

WorkerPool etag

### expireTime
    
    
    expireTime?: (google.protobuf.ITimestamp|null);

WorkerPool expireTime

### generation
    
    
    generation?: (number|Long|string|null);

WorkerPool generation

### instanceSplits
    
    
    instanceSplits?: (google.cloud.run.v2.IInstanceSplit[]|null);

WorkerPool instanceSplits

### instanceSplitStatuses
    
    
    instanceSplitStatuses?: (google.cloud.run.v2.IInstanceSplitStatus[]|null);

WorkerPool instanceSplitStatuses

### labels
    
    
    labels?: ({ [k: string]: string }|null);

WorkerPool labels

### lastModifier
    
    
    lastModifier?: (string|null);

WorkerPool lastModifier

### latestCreatedRevision
    
    
    latestCreatedRevision?: (string|null);

WorkerPool latestCreatedRevision

### latestReadyRevision
    
    
    latestReadyRevision?: (string|null);

WorkerPool latestReadyRevision

### launchStage
    
    
    launchStage?: (google.api.LaunchStage|keyof typeof google.api.LaunchStage|null);

WorkerPool launchStage

### name
    
    
    name?: (string|null);

WorkerPool name

### observedGeneration
    
    
    observedGeneration?: (number|Long|string|null);

WorkerPool observedGeneration

### reconciling
    
    
    reconciling?: (boolean|null);

WorkerPool reconciling

### satisfiesPzs
    
    
    satisfiesPzs?: (boolean|null);

WorkerPool satisfiesPzs

### scaling
    
    
    scaling?: (google.cloud.run.v2.IWorkerPoolScaling|null);

WorkerPool scaling

### template
    
    
    template?: (google.cloud.run.v2.IWorkerPoolRevisionTemplate|null);

WorkerPool template

### terminalCondition
    
    
    terminalCondition?: (google.cloud.run.v2.ICondition|null);

WorkerPool terminalCondition

### threatDetectionEnabled
    
    
    threatDetectionEnabled?: (boolean|null);

WorkerPool threatDetectionEnabled

### uid
    
    
    uid?: (string|null);

WorkerPool uid

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

WorkerPool updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
