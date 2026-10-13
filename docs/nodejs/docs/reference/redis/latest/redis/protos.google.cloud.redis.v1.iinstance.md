---
url: https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iinstance
title: Interface protos.google.cloud.redis.v1.IInstance (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:53.188499+00:00
---

# Interface protos.google.cloud.redis.v1.IInstance (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/redis/protos.google.cloud.redis.v1.iinstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.redis.v1.IInstance (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.3.0  5.1.0  5.0.1  3.3.0  3.2.2  3.1.5  2.4.0  2.3.1  2.2.6 

Properties of an Instance.

## Package

[@google-cloud/redis](https://docs.cloud.google.com/nodejs/docs/reference/redis/latest/overview.html)

## Properties 

### alternativeLocationId
    
    
    alternativeLocationId?: (string|null);

Instance alternativeLocationId

### authEnabled
    
    
    authEnabled?: (boolean|null);

Instance authEnabled

### authorizedNetwork
    
    
    authorizedNetwork?: (string|null);

Instance authorizedNetwork

### availableMaintenanceVersions
    
    
    availableMaintenanceVersions?: (string[]|null);

Instance availableMaintenanceVersions

### connectMode
    
    
    connectMode?: (google.cloud.redis.v1.Instance.ConnectMode|keyof typeof google.cloud.redis.v1.Instance.ConnectMode|null);

Instance connectMode

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Instance createTime

### currentLocationId
    
    
    currentLocationId?: (string|null);

Instance currentLocationId

### customerManagedKey
    
    
    customerManagedKey?: (string|null);

Instance customerManagedKey

### displayName
    
    
    displayName?: (string|null);

Instance displayName

### host
    
    
    host?: (string|null);

Instance host

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Instance labels

### locationId
    
    
    locationId?: (string|null);

Instance locationId

### maintenancePolicy
    
    
    maintenancePolicy?: (google.cloud.redis.v1.IMaintenancePolicy|null);

Instance maintenancePolicy

### maintenanceSchedule
    
    
    maintenanceSchedule?: (google.cloud.redis.v1.IMaintenanceSchedule|null);

Instance maintenanceSchedule

### maintenanceVersion
    
    
    maintenanceVersion?: (string|null);

Instance maintenanceVersion

### memorySizeGb
    
    
    memorySizeGb?: (number|null);

Instance memorySizeGb

### name
    
    
    name?: (string|null);

Instance name

### nodes
    
    
    nodes?: (google.cloud.redis.v1.INodeInfo[]|null);

Instance nodes

### persistenceConfig
    
    
    persistenceConfig?: (google.cloud.redis.v1.IPersistenceConfig|null);

Instance persistenceConfig

### persistenceIamIdentity
    
    
    persistenceIamIdentity?: (string|null);

Instance persistenceIamIdentity

### port
    
    
    port?: (number|null);

Instance port

### readEndpoint
    
    
    readEndpoint?: (string|null);

Instance readEndpoint

### readEndpointPort
    
    
    readEndpointPort?: (number|null);

Instance readEndpointPort

### readReplicasMode
    
    
    readReplicasMode?: (google.cloud.redis.v1.Instance.ReadReplicasMode|keyof typeof google.cloud.redis.v1.Instance.ReadReplicasMode|null);

Instance readReplicasMode

### redisConfigs
    
    
    redisConfigs?: ({ [k: string]: string }|null);

Instance redisConfigs

### redisVersion
    
    
    redisVersion?: (string|null);

Instance redisVersion

### replicaCount
    
    
    replicaCount?: (number|null);

Instance replicaCount

### reservedIpRange
    
    
    reservedIpRange?: (string|null);

Instance reservedIpRange

### secondaryIpRange
    
    
    secondaryIpRange?: (string|null);

Instance secondaryIpRange

### serverCaCerts
    
    
    serverCaCerts?: (google.cloud.redis.v1.ITlsCertificate[]|null);

Instance serverCaCerts

### state
    
    
    state?: (google.cloud.redis.v1.Instance.State|keyof typeof google.cloud.redis.v1.Instance.State|null);

Instance state

### statusMessage
    
    
    statusMessage?: (string|null);

Instance statusMessage

### suspensionReasons
    
    
    suspensionReasons?: (google.cloud.redis.v1.Instance.SuspensionReason[]|null);

Instance suspensionReasons

### tier
    
    
    tier?: (google.cloud.redis.v1.Instance.Tier|keyof typeof google.cloud.redis.v1.Instance.Tier|null);

Instance tier

### transitEncryptionMode
    
    
    transitEncryptionMode?: (google.cloud.redis.v1.Instance.TransitEncryptionMode|keyof typeof google.cloud.redis.v1.Instance.TransitEncryptionMode|null);

Instance transitEncryptionMode

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
