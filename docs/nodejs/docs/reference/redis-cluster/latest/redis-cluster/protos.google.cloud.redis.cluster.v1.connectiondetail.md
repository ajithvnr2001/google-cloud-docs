---
url: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.connectiondetail
title: Class protos.google.cloud.redis.cluster.v1.ConnectionDetail (0.15.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:46.260231+00:00
---

# Class protos.google.cloud.redis.cluster.v1.ConnectionDetail (0.15.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.connectiondetail

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.redis.cluster.v1.ConnectionDetail (0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.13.0  0.12.0  0.11.0  0.8.0  0.7.1  0.6.0  0.5.0  0.1.0 

Represents a ConnectionDetail.

## Implements

[protos.google.cloud.redis.cluster.v1.IConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iconnectiondetail)

## Package

[@google-cloud/redis-cluster](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.redis.cluster.v1.IConnectionDetail);

Constructs a new ConnectionDetail.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iconnectiondetail)`   
Properties to set  
  
## Properties 

### connection
    
    
    public connection?: ("pscAutoConnection"|"pscConnection");

ConnectionDetail connection.

### pscAutoConnection
    
    
    public pscAutoConnection?: (google.cloud.redis.cluster.v1.IPscAutoConnection|null);

ConnectionDetail pscAutoConnection.

### pscConnection
    
    
    public pscConnection?: (google.cloud.redis.cluster.v1.IPscConnection|null);

ConnectionDetail pscConnection.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.redis.cluster.v1.IConnectionDetail): google.cloud.redis.cluster.v1.ConnectionDetail;

Creates a new ConnectionDetail instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iconnectiondetail)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.connectiondetail)` | ConnectionDetail instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.redis.cluster.v1.ConnectionDetail;

Decodes a ConnectionDetail message from the specified reader or buffer.

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
`[ConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.connectiondetail)` | ConnectionDetail  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.redis.cluster.v1.ConnectionDetail;

Decodes a ConnectionDetail message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.connectiondetail)` | ConnectionDetail  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.redis.cluster.v1.IConnectionDetail, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConnectionDetail message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iconnectiondetail)`   
ConnectionDetail message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.redis.cluster.v1.IConnectionDetail, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ConnectionDetail message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.iconnectiondetail)`   
ConnectionDetail message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.redis.cluster.v1.ConnectionDetail;

Creates a ConnectionDetail message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.connectiondetail)` | ConnectionDetail  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ConnectionDetail

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

Converts this ConnectionDetail to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.redis.cluster.v1.ConnectionDetail, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ConnectionDetail message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ConnectionDetail](https://docs.cloud.google.com/nodejs/docs/reference/redis-cluster/latest/redis-cluster/protos.google.cloud.redis.cluster.v1.connectiondetail)`   
ConnectionDetail  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ConnectionDetail message.

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
