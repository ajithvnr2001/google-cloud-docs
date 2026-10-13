---
url: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinstance
title: Interface protos.google.cloud.alloydb.v1.IInstance (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:42.851216+00:00
---

# Interface protos.google.cloud.alloydb.v1.IInstance (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.alloydb.v1.IInstance (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  1.10.1  1.9.0  1.6.0  1.4.1  1.3.0  1.2.0  0.1.1 

Properties of an Instance.

## Package

[@google-cloud/alloydb](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)

## Properties 

### activationPolicy
    
    
    activationPolicy?: (google.cloud.alloydb.v1.Instance.ActivationPolicy|keyof typeof google.cloud.alloydb.v1.Instance.ActivationPolicy|null);

Instance activationPolicy

### annotations
    
    
    annotations?: ({ [k: string]: string }|null);

Instance annotations

### availabilityType
    
    
    availabilityType?: (google.cloud.alloydb.v1.Instance.AvailabilityType|keyof typeof google.cloud.alloydb.v1.Instance.AvailabilityType|null);

Instance availabilityType

### clientConnectionConfig
    
    
    clientConnectionConfig?: (google.cloud.alloydb.v1.Instance.IClientConnectionConfig|null);

Instance clientConnectionConfig

### connectionPoolConfig
    
    
    connectionPoolConfig?: (google.cloud.alloydb.v1.Instance.IConnectionPoolConfig|null);

Instance connectionPoolConfig

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Instance createTime

### databaseFlags
    
    
    databaseFlags?: ({ [k: string]: string }|null);

Instance databaseFlags

### deleteTime
    
    
    deleteTime?: (google.protobuf.ITimestamp|null);

Instance deleteTime

### displayName
    
    
    displayName?: (string|null);

Instance displayName

### etag
    
    
    etag?: (string|null);

Instance etag

### gceZone
    
    
    gceZone?: (string|null);

Instance gceZone

### instanceType
    
    
    instanceType?: (google.cloud.alloydb.v1.Instance.InstanceType|keyof typeof google.cloud.alloydb.v1.Instance.InstanceType|null);

Instance instanceType

### ipAddress
    
    
    ipAddress?: (string|null);

Instance ipAddress

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Instance labels

### machineConfig
    
    
    machineConfig?: (google.cloud.alloydb.v1.Instance.IMachineConfig|null);

Instance machineConfig

### name
    
    
    name?: (string|null);

Instance name

### networkConfig
    
    
    networkConfig?: (google.cloud.alloydb.v1.Instance.IInstanceNetworkConfig|null);

Instance networkConfig

### nodes
    
    
    nodes?: (google.cloud.alloydb.v1.Instance.INode[]|null);

Instance nodes

### observabilityConfig
    
    
    observabilityConfig?: (google.cloud.alloydb.v1.Instance.IObservabilityInstanceConfig|null);

Instance observabilityConfig

### outboundPublicIpAddresses
    
    
    outboundPublicIpAddresses?: (string[]|null);

Instance outboundPublicIpAddresses

### pscInstanceConfig
    
    
    pscInstanceConfig?: (google.cloud.alloydb.v1.Instance.IPscInstanceConfig|null);

Instance pscInstanceConfig

### publicIpAddress
    
    
    publicIpAddress?: (string|null);

Instance publicIpAddress

### queryInsightsConfig
    
    
    queryInsightsConfig?: (google.cloud.alloydb.v1.Instance.IQueryInsightsInstanceConfig|null);

Instance queryInsightsConfig

### readPoolConfig
    
    
    readPoolConfig?: (google.cloud.alloydb.v1.Instance.IReadPoolConfig|null);

Instance readPoolConfig

### reconciling
    
    
    reconciling?: (boolean|null);

Instance reconciling

### satisfiesPzs
    
    
    satisfiesPzs?: (boolean|null);

Instance satisfiesPzs

### state
    
    
    state?: (google.cloud.alloydb.v1.Instance.State|keyof typeof google.cloud.alloydb.v1.Instance.State|null);

Instance state

### uid
    
    
    uid?: (string|null);

Instance uid

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Instance updateTime

### writableNode
    
    
    writableNode?: (google.cloud.alloydb.v1.Instance.INode|null);

Instance writableNode

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
