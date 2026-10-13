---
url: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideploymentgroup
title: Interface protos.google.cloud.config.v1.IDeploymentGroup (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:20.617200+00:00
---

# Interface protos.google.cloud.config.v1.IDeploymentGroup (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/config/latest/config/protos.google.cloud.config.v1.ideploymentgroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.config.v1.IDeploymentGroup (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.14.0  0.12.0  0.7.0  0.5.0  0.2.0  0.1.1 

Properties of a DeploymentGroup.

## Package

[@google-cloud/config](https://docs.cloud.google.com/nodejs/docs/reference/config/latest/overview.html)

## Properties 

### annotations
    
    
    annotations?: ({ [k: string]: string }|null);

DeploymentGroup annotations

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

DeploymentGroup createTime

### deploymentUnits
    
    
    deploymentUnits?: (google.cloud.config.v1.IDeploymentUnit[]|null);

DeploymentGroup deploymentUnits

### labels
    
    
    labels?: ({ [k: string]: string }|null);

DeploymentGroup labels

### name
    
    
    name?: (string|null);

DeploymentGroup name

### provisioningError
    
    
    provisioningError?: (google.rpc.IStatus|null);

DeploymentGroup provisioningError

### provisioningState
    
    
    provisioningState?: (google.cloud.config.v1.DeploymentGroup.ProvisioningState|keyof typeof google.cloud.config.v1.DeploymentGroup.ProvisioningState|null);

DeploymentGroup provisioningState

### provisioningStateDescription
    
    
    provisioningStateDescription?: (string|null);

DeploymentGroup provisioningStateDescription

### state
    
    
    state?: (google.cloud.config.v1.DeploymentGroup.State|keyof typeof google.cloud.config.v1.DeploymentGroup.State|null);

DeploymentGroup state

### stateDescription
    
    
    stateDescription?: (string|null);

DeploymentGroup stateDescription

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

DeploymentGroup updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
