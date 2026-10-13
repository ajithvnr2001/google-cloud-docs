---
url: https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.node-class
title: Class protos.google.cloud.tpu.v2.Node (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:49.106004+00:00
---

# Class protos.google.cloud.tpu.v2.Node (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.node-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.tpu.v2.Node (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.8.0  3.7.0  3.6.0  3.2.1  2.6.1  2.4.1  2.2.0  2.1.0  1.2.0  1.1.1  1.0.5 

Represents a Node.

## Implements

[protos.google.cloud.tpu.v2.INode](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.inode)

## Package

[@google-cloud/tpu](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.tpu.v2.INode);

Constructs a new Node.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INode](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.inode)`   
Properties to set  
  
## Properties 

### acceleratorConfig
    
    
    public acceleratorConfig?: (google.cloud.tpu.v2.IAcceleratorConfig|null);

Node acceleratorConfig.

### acceleratorType
    
    
    public acceleratorType: string;

Node acceleratorType.

### apiVersion
    
    
    public apiVersion: (google.cloud.tpu.v2.Node.ApiVersion|keyof typeof google.cloud.tpu.v2.Node.ApiVersion);

Node apiVersion.

### cidrBlock
    
    
    public cidrBlock: string;

Node cidrBlock.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Node createTime.

### dataDisks
    
    
    public dataDisks: google.cloud.tpu.v2.IAttachedDisk[];

Node dataDisks.

### description
    
    
    public description: string;

Node description.

### health
    
    
    public health: (google.cloud.tpu.v2.Node.Health|keyof typeof google.cloud.tpu.v2.Node.Health);

Node health.

### healthDescription
    
    
    public healthDescription: string;

Node healthDescription.

### id
    
    
    public id: (number|Long|string);

Node id.

### labels
    
    
    public labels: { [k: string]: string };

Node labels.

### metadata
    
    
    public metadata: { [k: string]: string };

Node metadata.

### multisliceNode
    
    
    public multisliceNode: boolean;

Node multisliceNode.

### name
    
    
    public name: string;

Node name.

### networkConfig
    
    
    public networkConfig?: (google.cloud.tpu.v2.INetworkConfig|null);

Node networkConfig.

### networkConfigs
    
    
    public networkConfigs: google.cloud.tpu.v2.INetworkConfig[];

Node networkConfigs.

### networkEndpoints
    
    
    public networkEndpoints: google.cloud.tpu.v2.INetworkEndpoint[];

Node networkEndpoints.

### queuedResource
    
    
    public queuedResource: string;

Node queuedResource.

### runtimeVersion
    
    
    public runtimeVersion: string;

Node runtimeVersion.

### schedulingConfig
    
    
    public schedulingConfig?: (google.cloud.tpu.v2.ISchedulingConfig|null);

Node schedulingConfig.

### serviceAccount
    
    
    public serviceAccount?: (google.cloud.tpu.v2.IServiceAccount|null);

Node serviceAccount.

### shieldedInstanceConfig
    
    
    public shieldedInstanceConfig?: (google.cloud.tpu.v2.IShieldedInstanceConfig|null);

Node shieldedInstanceConfig.

### state
    
    
    public state: (google.cloud.tpu.v2.Node.State|keyof typeof google.cloud.tpu.v2.Node.State);

Node state.

### symptoms
    
    
    public symptoms: google.cloud.tpu.v2.ISymptom[];

Node symptoms.

### tags
    
    
    public tags: string[];

Node tags.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.tpu.v2.INode): google.cloud.tpu.v2.Node;

Creates a new Node instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INode](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.inode)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Node](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.node-class)` | Node instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.tpu.v2.Node;

Decodes a Node message from the specified reader or buffer.

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
`[Node](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.node-class)` | Node  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.tpu.v2.Node;

Decodes a Node message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Node](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.node-class)` | Node  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.tpu.v2.INode, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Node message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INode](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.inode)`   
Node message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.tpu.v2.INode, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Node message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INode](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.inode)`   
Node message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.tpu.v2.Node;

Creates a Node message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Node](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.node-class)` | Node  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Node

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

Converts this Node to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.tpu.v2.Node, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Node message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Node](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v2.node-class)`   
Node  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Node message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
