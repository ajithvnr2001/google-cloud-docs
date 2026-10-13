---
url: https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1.iworkstationconfig
title: Interface protos.google.cloud.workstations.v1.IWorkstationConfig (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:36.743039+00:00
---

# Interface protos.google.cloud.workstations.v1.IWorkstationConfig (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/workstations/protos.google.cloud.workstations.v1.iworkstationconfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.workstations.v1.IWorkstationConfig (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.3.0  2.1.0  1.1.1  0.1.1 

Properties of a WorkstationConfig.

## Package

[@google-cloud/workstations](https://docs.cloud.google.com/nodejs/docs/reference/workstations/latest/overview.html)

## Properties 

### allowedPorts
    
    
    allowedPorts?: (google.cloud.workstations.v1.WorkstationConfig.IPortRange[]|null);

WorkstationConfig allowedPorts

### annotations
    
    
    annotations?: ({ [k: string]: string }|null);

WorkstationConfig annotations

### conditions
    
    
    conditions?: (google.rpc.IStatus[]|null);

WorkstationConfig conditions

### container
    
    
    container?: (google.cloud.workstations.v1.WorkstationConfig.IContainer|null);

WorkstationConfig container

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

WorkstationConfig createTime

### degraded
    
    
    degraded?: (boolean|null);

WorkstationConfig degraded

### deleteTime
    
    
    deleteTime?: (google.protobuf.ITimestamp|null);

WorkstationConfig deleteTime

### disableTcpConnections
    
    
    disableTcpConnections?: (boolean|null);

WorkstationConfig disableTcpConnections

### displayName
    
    
    displayName?: (string|null);

WorkstationConfig displayName

### enableAuditAgent
    
    
    enableAuditAgent?: (boolean|null);

WorkstationConfig enableAuditAgent

### encryptionKey
    
    
    encryptionKey?: (google.cloud.workstations.v1.WorkstationConfig.ICustomerEncryptionKey|null);

WorkstationConfig encryptionKey

### ephemeralDirectories
    
    
    ephemeralDirectories?: (google.cloud.workstations.v1.WorkstationConfig.IEphemeralDirectory[]|null);

WorkstationConfig ephemeralDirectories

### etag
    
    
    etag?: (string|null);

WorkstationConfig etag

### grantWorkstationAdminRoleOnCreate
    
    
    grantWorkstationAdminRoleOnCreate?: (boolean|null);

WorkstationConfig grantWorkstationAdminRoleOnCreate

### host
    
    
    host?: (google.cloud.workstations.v1.WorkstationConfig.IHost|null);

WorkstationConfig host

### idleTimeout
    
    
    idleTimeout?: (google.protobuf.IDuration|null);

WorkstationConfig idleTimeout

### labels
    
    
    labels?: ({ [k: string]: string }|null);

WorkstationConfig labels

### maxUsableWorkstations
    
    
    maxUsableWorkstations?: (number|null);

WorkstationConfig maxUsableWorkstations

### name
    
    
    name?: (string|null);

WorkstationConfig name

### persistentDirectories
    
    
    persistentDirectories?: (google.cloud.workstations.v1.WorkstationConfig.IPersistentDirectory[]|null);

WorkstationConfig persistentDirectories

### readinessChecks
    
    
    readinessChecks?: (google.cloud.workstations.v1.WorkstationConfig.IReadinessCheck[]|null);

WorkstationConfig readinessChecks

### reconciling
    
    
    reconciling?: (boolean|null);

WorkstationConfig reconciling

### replicaZones
    
    
    replicaZones?: (string[]|null);

WorkstationConfig replicaZones

### runningTimeout
    
    
    runningTimeout?: (google.protobuf.IDuration|null);

WorkstationConfig runningTimeout

### uid
    
    
    uid?: (string|null);

WorkstationConfig uid

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

WorkstationConfig updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
