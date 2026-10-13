---
url: https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v2.iinstance
title: Interface protos.google.cloud.notebooks.v2.IInstance (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:46.972029+00:00
---

# Interface protos.google.cloud.notebooks.v2.IInstance (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/notebooks/protos.google.cloud.notebooks.v2.iinstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.notebooks.v2.IInstance (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.1.4  1.3.1  1.2.0  1.1.7 

Properties of an Instance.

## Package

[@google-cloud/notebooks](https://docs.cloud.google.com/nodejs/docs/reference/notebooks/latest/overview.html)

## Properties 

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Instance createTime

### creator
    
    
    creator?: (string|null);

Instance creator

### disableProxyAccess
    
    
    disableProxyAccess?: (boolean|null);

Instance disableProxyAccess

### gceSetup
    
    
    gceSetup?: (google.cloud.notebooks.v2.IGceSetup|null);

Instance gceSetup

### healthInfo
    
    
    healthInfo?: ({ [k: string]: string }|null);

Instance healthInfo

### healthState
    
    
    healthState?: (google.cloud.notebooks.v2.HealthState|keyof typeof google.cloud.notebooks.v2.HealthState|null);

Instance healthState

### id
    
    
    id?: (string|null);

Instance id

### instanceOwners
    
    
    instanceOwners?: (string[]|null);

Instance instanceOwners

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Instance labels

### name
    
    
    name?: (string|null);

Instance name

### proxyUri
    
    
    proxyUri?: (string|null);

Instance proxyUri

### state
    
    
    state?: (google.cloud.notebooks.v2.State|keyof typeof google.cloud.notebooks.v2.State|null);

Instance state

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Instance updateTime

### upgradeHistory
    
    
    upgradeHistory?: (google.cloud.notebooks.v2.IUpgradeHistoryEntry[]|null);

Instance upgradeHistory

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
