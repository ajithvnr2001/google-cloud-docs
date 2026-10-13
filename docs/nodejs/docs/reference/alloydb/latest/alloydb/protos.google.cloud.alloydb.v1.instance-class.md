---
url: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.instance-class
title: Class protos.google.cloud.alloydb.v1.Instance (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:53:59.857500+00:00
---

# Class protos.google.cloud.alloydb.v1.Instance (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.instance-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.alloydb.v1.Instance (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  1.10.1  1.9.0  1.6.0  1.4.1  1.3.0  1.2.0  0.1.1 

Represents an Instance.

## Implements

[protos.google.cloud.alloydb.v1.IInstance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinstance)

## Package

[@google-cloud/alloydb](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.alloydb.v1.IInstance);

Constructs a new Instance.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinstance)`   
Properties to set  
  
## Properties 

### activationPolicy
    
    
    public activationPolicy: (google.cloud.alloydb.v1.Instance.ActivationPolicy|keyof typeof google.cloud.alloydb.v1.Instance.ActivationPolicy);

Instance activationPolicy.

### annotations
    
    
    public annotations: { [k: string]: string };

Instance annotations.

### availabilityType
    
    
    public availabilityType: (google.cloud.alloydb.v1.Instance.AvailabilityType|keyof typeof google.cloud.alloydb.v1.Instance.AvailabilityType);

Instance availabilityType.

### clientConnectionConfig
    
    
    public clientConnectionConfig?: (google.cloud.alloydb.v1.Instance.IClientConnectionConfig|null);

Instance clientConnectionConfig.

### connectionPoolConfig
    
    
    public connectionPoolConfig?: (google.cloud.alloydb.v1.Instance.IConnectionPoolConfig|null);

Instance connectionPoolConfig.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Instance createTime.

### databaseFlags
    
    
    public databaseFlags: { [k: string]: string };

Instance databaseFlags.

### deleteTime
    
    
    public deleteTime?: (google.protobuf.ITimestamp|null);

Instance deleteTime.

### displayName
    
    
    public displayName: string;

Instance displayName.

### etag
    
    
    public etag: string;

Instance etag.

### gceZone
    
    
    public gceZone: string;

Instance gceZone.

### instanceType
    
    
    public instanceType: (google.cloud.alloydb.v1.Instance.InstanceType|keyof typeof google.cloud.alloydb.v1.Instance.InstanceType);

Instance instanceType.

### ipAddress
    
    
    public ipAddress: string;

Instance ipAddress.

### labels
    
    
    public labels: { [k: string]: string };

Instance labels.

### machineConfig
    
    
    public machineConfig?: (google.cloud.alloydb.v1.Instance.IMachineConfig|null);

Instance machineConfig.

### name
    
    
    public name: string;

Instance name.

### networkConfig
    
    
    public networkConfig?: (google.cloud.alloydb.v1.Instance.IInstanceNetworkConfig|null);

Instance networkConfig.

### nodes
    
    
    public nodes: google.cloud.alloydb.v1.Instance.INode[];

Instance nodes.

### observabilityConfig
    
    
    public observabilityConfig?: (google.cloud.alloydb.v1.Instance.IObservabilityInstanceConfig|null);

Instance observabilityConfig.

### outboundPublicIpAddresses
    
    
    public outboundPublicIpAddresses: string[];

Instance outboundPublicIpAddresses.

### pscInstanceConfig
    
    
    public pscInstanceConfig?: (google.cloud.alloydb.v1.Instance.IPscInstanceConfig|null);

Instance pscInstanceConfig.

### publicIpAddress
    
    
    public publicIpAddress: string;

Instance publicIpAddress.

### queryInsightsConfig
    
    
    public queryInsightsConfig?: (google.cloud.alloydb.v1.Instance.IQueryInsightsInstanceConfig|null);

Instance queryInsightsConfig.

### readPoolConfig
    
    
    public readPoolConfig?: (google.cloud.alloydb.v1.Instance.IReadPoolConfig|null);

Instance readPoolConfig.

### reconciling
    
    
    public reconciling: boolean;

Instance reconciling.

### satisfiesPzs
    
    
    public satisfiesPzs: boolean;

Instance satisfiesPzs.

### state
    
    
    public state: (google.cloud.alloydb.v1.Instance.State|keyof typeof google.cloud.alloydb.v1.Instance.State);

Instance state.

### uid
    
    
    public uid: string;

Instance uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Instance updateTime.

### writableNode
    
    
    public writableNode?: (google.cloud.alloydb.v1.Instance.INode|null);

Instance writableNode.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.alloydb.v1.IInstance): google.cloud.alloydb.v1.Instance;

Creates a new Instance instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinstance)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.instance-class)` | Instance instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.alloydb.v1.Instance;

Decodes an Instance message from the specified reader or buffer.

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
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.instance-class)` | Instance  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.alloydb.v1.Instance;

Decodes an Instance message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.instance-class)` | Instance  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.alloydb.v1.IInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Instance message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinstance)`   
Instance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.alloydb.v1.IInstance, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Instance message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInstance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.iinstance)`   
Instance message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.alloydb.v1.Instance;

Creates an Instance message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.instance-class)` | Instance  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Instance

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

Converts this Instance to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.alloydb.v1.Instance, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Instance message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Instance](https://docs.cloud.google.com/nodejs/docs/reference/alloydb/latest/alloydb/protos.google.cloud.alloydb.v1.instance-class)`   
Instance  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Instance message.

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
