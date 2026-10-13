---
url: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3.ipolicybinding
title: Interface protos.google.iam.v3.IPolicyBinding (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:42.077930+00:00
---

# Interface protos.google.iam.v3.IPolicyBinding (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v3.ipolicybinding

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.iam.v3.IPolicyBinding (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.2.0  0.3.2  0.2.2 

Properties of a PolicyBinding.

## Package

[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)

## Properties 

### annotations
    
    
    annotations?: ({ [k: string]: string }|null);

PolicyBinding annotations

### condition
    
    
    condition?: (google.type.IExpr|null);

PolicyBinding condition

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

PolicyBinding createTime

### displayName
    
    
    displayName?: (string|null);

PolicyBinding displayName

### etag
    
    
    etag?: (string|null);

PolicyBinding etag

### name
    
    
    name?: (string|null);

PolicyBinding name

### policy
    
    
    policy?: (string|null);

PolicyBinding policy

### policyKind
    
    
    policyKind?: (google.iam.v3.PolicyBinding.PolicyKind|keyof typeof google.iam.v3.PolicyBinding.PolicyKind|null);

PolicyBinding policyKind

### policyUid
    
    
    policyUid?: (string|null);

PolicyBinding policyUid

### target
    
    
    target?: (google.iam.v3.PolicyBinding.ITarget|null);

PolicyBinding target

### uid
    
    
    uid?: (string|null);

PolicyBinding uid

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

PolicyBinding updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
