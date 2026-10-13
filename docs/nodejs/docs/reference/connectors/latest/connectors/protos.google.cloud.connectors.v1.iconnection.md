---
url: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iconnection
title: Interface protos.google.cloud.connectors.v1.IConnection (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:44.776390+00:00
---

# Interface protos.google.cloud.connectors.v1.IConnection (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/connectors/protos.google.cloud.connectors.v1.iconnection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.connectors.v1.IConnection (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Properties of a Connection.

## Package

[@google-cloud/connectors](https://docs.cloud.google.com/nodejs/docs/reference/connectors/latest/overview.html)

## Properties 

### authConfig
    
    
    authConfig?: (google.cloud.connectors.v1.IAuthConfig|null);

Connection authConfig

### configVariables
    
    
    configVariables?: (google.cloud.connectors.v1.IConfigVariable[]|null);

Connection configVariables

### connectorVersion
    
    
    connectorVersion?: (string|null);

Connection connectorVersion

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Connection createTime

### description
    
    
    description?: (string|null);

Connection description

### destinationConfigs
    
    
    destinationConfigs?: (google.cloud.connectors.v1.IDestinationConfig[]|null);

Connection destinationConfigs

### envoyImageLocation
    
    
    envoyImageLocation?: (string|null);

Connection envoyImageLocation

### imageLocation
    
    
    imageLocation?: (string|null);

Connection imageLocation

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Connection labels

### lockConfig
    
    
    lockConfig?: (google.cloud.connectors.v1.ILockConfig|null);

Connection lockConfig

### name
    
    
    name?: (string|null);

Connection name

### nodeConfig
    
    
    nodeConfig?: (google.cloud.connectors.v1.INodeConfig|null);

Connection nodeConfig

### serviceAccount
    
    
    serviceAccount?: (string|null);

Connection serviceAccount

### serviceDirectory
    
    
    serviceDirectory?: (string|null);

Connection serviceDirectory

### sslConfig
    
    
    sslConfig?: (google.cloud.connectors.v1.ISslConfig|null);

Connection sslConfig

### status
    
    
    status?: (google.cloud.connectors.v1.IConnectionStatus|null);

Connection status

### suspended
    
    
    suspended?: (boolean|null);

Connection suspended

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Connection updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
