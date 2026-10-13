---
url: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ipipelinejob
title: Interface protos.google.cloud.aiplatform.v1beta1.IPipelineJob (7.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:29.471335+00:00
---

# Interface protos.google.cloud.aiplatform.v1beta1.IPipelineJob (7.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/aiplatform/protos.google.cloud.aiplatform.v1beta1.ipipelinejob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.aiplatform.v1beta1.IPipelineJob (7.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.4.1 (latest)  7.3.0  6.10.0  6.9.0  6.8.1  6.6.0  6.4.0  6.3.0  6.2.0  6.1.0  6.0.0  5.14.0  5.13.0  3.15.0  3.13.0  3.11.0  3.10.1  3.9.0  3.7.0  3.6.0  3.4.0  3.3.0  3.0.0  2.12.0  2.11.0  2.10.0  2.7.0  2.6.1  2.5.0  2.3.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.0  1.11.0  1.7.2 

Properties of a PipelineJob.

## Package

[@google-cloud/aiplatform](https://docs.cloud.google.com/nodejs/docs/reference/aiplatform/latest/overview.html)

## Properties 

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

PipelineJob createTime

### displayName
    
    
    displayName?: (string|null);

PipelineJob displayName

### encryptionSpec
    
    
    encryptionSpec?: (google.cloud.aiplatform.v1beta1.IEncryptionSpec|null);

PipelineJob encryptionSpec

### endTime
    
    
    endTime?: (google.protobuf.ITimestamp|null);

PipelineJob endTime

### error
    
    
    error?: (google.rpc.IStatus|null);

PipelineJob error

### jobDetail
    
    
    jobDetail?: (google.cloud.aiplatform.v1beta1.IPipelineJobDetail|null);

PipelineJob jobDetail

### labels
    
    
    labels?: ({ [k: string]: string }|null);

PipelineJob labels

### name
    
    
    name?: (string|null);

PipelineJob name

### network
    
    
    network?: (string|null);

PipelineJob network

### originalPipelineJobId
    
    
    originalPipelineJobId?: (number|Long|string|null);

PipelineJob originalPipelineJobId

### pipelineSpec
    
    
    pipelineSpec?: (google.protobuf.IStruct|null);

PipelineJob pipelineSpec

### pipelineTaskRerunConfigs
    
    
    pipelineTaskRerunConfigs?: (google.cloud.aiplatform.v1beta1.IPipelineTaskRerunConfig[]|null);

PipelineJob pipelineTaskRerunConfigs

### preflightValidations
    
    
    preflightValidations?: (boolean|null);

PipelineJob preflightValidations

### pscInterfaceConfig
    
    
    pscInterfaceConfig?: (google.cloud.aiplatform.v1beta1.IPscInterfaceConfig|null);

PipelineJob pscInterfaceConfig

### reservedIpRanges
    
    
    reservedIpRanges?: (string[]|null);

PipelineJob reservedIpRanges

### runtimeConfig
    
    
    runtimeConfig?: (google.cloud.aiplatform.v1beta1.PipelineJob.IRuntimeConfig|null);

PipelineJob runtimeConfig

### satisfiesPzi
    
    
    satisfiesPzi?: (boolean|null);

PipelineJob satisfiesPzi

### satisfiesPzs
    
    
    satisfiesPzs?: (boolean|null);

PipelineJob satisfiesPzs

### scheduleName
    
    
    scheduleName?: (string|null);

PipelineJob scheduleName

### serviceAccount
    
    
    serviceAccount?: (string|null);

PipelineJob serviceAccount

### startTime
    
    
    startTime?: (google.protobuf.ITimestamp|null);

PipelineJob startTime

### state
    
    
    state?: (google.cloud.aiplatform.v1beta1.PipelineState|keyof typeof google.cloud.aiplatform.v1beta1.PipelineState|null);

PipelineJob state

### templateMetadata
    
    
    templateMetadata?: (google.cloud.aiplatform.v1beta1.IPipelineTemplateMetadata|null);

PipelineJob templateMetadata

### templateUri
    
    
    templateUri?: (string|null);

PipelineJob templateUri

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

PipelineJob updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
