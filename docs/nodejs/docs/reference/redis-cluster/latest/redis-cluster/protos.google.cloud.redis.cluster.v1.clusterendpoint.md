---
url: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.clusterendpoint
title: Class protos.google.cloud.redis.cluster.v1.ClusterEndpoint (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:23.144239+00:00
---

# Class protos.google.cloud.redis.cluster.v1.ClusterEndpoint (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.clusterendpoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.redis.cluster.v1.ClusterEndpoint (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.0  0.12.0  0.11.0  0.8.0  0.7.1  0.6.0  0.5.0  0.1.0 

Represents a ClusterEndpoint.

## Implements

[protos.google.cloud.redis.cluster.v1.IClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iclusterendpoint)

## Package

[@google-cloud/redis-cluster](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.redis.cluster.v1.IClusterEndpoint);

Constructs a new ClusterEndpoint.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iclusterendpoint)`   
Properties to set  
  
## Properties 

### connections
    
    
    public connections: google.cloud.redis.cluster.v1.IConnectionDetail[];

ClusterEndpoint connections.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.redis.cluster.v1.IClusterEndpoint): google.cloud.redis.cluster.v1.ClusterEndpoint;

Creates a new ClusterEndpoint instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iclusterendpoint)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.clusterendpoint)` | ClusterEndpoint instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.redis.cluster.v1.ClusterEndpoint;

Decodes a ClusterEndpoint message from the specified reader or buffer.

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
`[ClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.clusterendpoint)` | ClusterEndpoint  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.redis.cluster.v1.ClusterEndpoint;

Decodes a ClusterEndpoint message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.clusterendpoint)` | ClusterEndpoint  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.redis.cluster.v1.IClusterEndpoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClusterEndpoint message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iclusterendpoint)`   
ClusterEndpoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.redis.cluster.v1.IClusterEndpoint, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ClusterEndpoint message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iclusterendpoint)`   
ClusterEndpoint message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.redis.cluster.v1.ClusterEndpoint;

Creates a ClusterEndpoint message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.clusterendpoint)` | ClusterEndpoint  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ClusterEndpoint

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

Converts this ClusterEndpoint to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.redis.cluster.v1.ClusterEndpoint, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ClusterEndpoint message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ClusterEndpoint](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.clusterendpoint)`   
ClusterEndpoint  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ClusterEndpoint message.

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
