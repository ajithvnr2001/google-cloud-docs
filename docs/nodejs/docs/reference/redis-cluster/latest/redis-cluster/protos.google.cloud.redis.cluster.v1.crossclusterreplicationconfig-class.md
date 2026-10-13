---
url: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.crossclusterreplicationconfig-class
title: Class protos.google.cloud.redis.cluster.v1.CrossClusterReplicationConfig (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:16.561261+00:00
---

# Class protos.google.cloud.redis.cluster.v1.CrossClusterReplicationConfig (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.crossclusterreplicationconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.redis.cluster.v1.CrossClusterReplicationConfig (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.0  0.12.0  0.11.0  0.8.0  0.7.1  0.6.0  0.5.0  0.1.0 

Represents a CrossClusterReplicationConfig.

## Implements

[protos.google.cloud.redis.cluster.v1.ICrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.icrossclusterreplicationconfig)

## Package

[@google-cloud/redis-cluster](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.redis.cluster.v1.ICrossClusterReplicationConfig);

Constructs a new CrossClusterReplicationConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.icrossclusterreplicationconfig)`   
Properties to set  
  
## Properties 

### clusterRole
    
    
    public clusterRole: (google.cloud.redis.cluster.v1.CrossClusterReplicationConfig.ClusterRole|keyof typeof google.cloud.redis.cluster.v1.CrossClusterReplicationConfig.ClusterRole);

CrossClusterReplicationConfig clusterRole.

### membership
    
    
    public membership?: (google.cloud.redis.cluster.v1.CrossClusterReplicationConfig.IMembership|null);

CrossClusterReplicationConfig membership.

### primaryCluster
    
    
    public primaryCluster?: (google.cloud.redis.cluster.v1.CrossClusterReplicationConfig.IRemoteCluster|null);

CrossClusterReplicationConfig primaryCluster.

### secondaryClusters
    
    
    public secondaryClusters: google.cloud.redis.cluster.v1.CrossClusterReplicationConfig.IRemoteCluster[];

CrossClusterReplicationConfig secondaryClusters.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

CrossClusterReplicationConfig updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.redis.cluster.v1.ICrossClusterReplicationConfig): google.cloud.redis.cluster.v1.CrossClusterReplicationConfig;

Creates a new CrossClusterReplicationConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.icrossclusterreplicationconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.crossclusterreplicationconfig-class)` | CrossClusterReplicationConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.redis.cluster.v1.CrossClusterReplicationConfig;

Decodes a CrossClusterReplicationConfig message from the specified reader or buffer.

**Parameters**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
`length` |  `number`   
Message length if known beforehand  
**Returns**  
---  
**Type** | **Description**  
`[CrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.crossclusterreplicationconfig-class)` | CrossClusterReplicationConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.redis.cluster.v1.CrossClusterReplicationConfig;

Decodes a CrossClusterReplicationConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.crossclusterreplicationconfig-class)` | CrossClusterReplicationConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.redis.cluster.v1.ICrossClusterReplicationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CrossClusterReplicationConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.icrossclusterreplicationconfig)`   
CrossClusterReplicationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.redis.cluster.v1.ICrossClusterReplicationConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CrossClusterReplicationConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.icrossclusterreplicationconfig)`   
CrossClusterReplicationConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.redis.cluster.v1.CrossClusterReplicationConfig;

Creates a CrossClusterReplicationConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.crossclusterreplicationconfig-class)` | CrossClusterReplicationConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CrossClusterReplicationConfig

**Parameter**  
---  
**Name** | **Description**  
`typeUrlPrefix` |  `string`   
your custom typeUrlPrefix(default "type.googleapis.com")  
**Returns**  
---  
**Type** | **Description**  
`string` | The default type url  
  
### toJSON()
    
    
    public toJSON(): { [k: string]: any };

Converts this CrossClusterReplicationConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.redis.cluster.v1.CrossClusterReplicationConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CrossClusterReplicationConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CrossClusterReplicationConfig](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.crossclusterreplicationconfig-class)`   
CrossClusterReplicationConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CrossClusterReplicationConfig message.

**Parameter**  
---  
**Name** | **Description**  
`message` |  `{ [k: string]: any }`   
Plain object to verify  
**Returns**  
---  
**Type** | **Description**  
`(string|null)` | `null` if valid, otherwise the reason why it is not  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
