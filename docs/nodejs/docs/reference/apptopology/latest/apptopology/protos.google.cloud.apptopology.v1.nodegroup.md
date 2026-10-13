---
url: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.nodegroup
title: Class protos.google.cloud.apptopology.v1.NodeGroup (0.3.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:54.759206+00:00
---

# Class protos.google.cloud.apptopology.v1.NodeGroup (0.3.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.nodegroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apptopology.v1.NodeGroup (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.0 (latest)  0.1.0 

Represents a NodeGroup.

## Implements

[protos.google.cloud.apptopology.v1.INodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.inodegroup)

## Package

[@google-cloud/apptopology](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apptopology.v1.INodeGroup);

Constructs a new NodeGroup.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.inodegroup)`   
Properties to set  
  
## Properties 

### anyLabels
    
    
    public anyLabels: string[];

NodeGroup anyLabels.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apptopology.v1.INodeGroup): google.cloud.apptopology.v1.NodeGroup;

Creates a new NodeGroup instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[INodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.inodegroup)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.nodegroup)` | NodeGroup instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apptopology.v1.NodeGroup;

Decodes a NodeGroup message from the specified reader or buffer.

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
`[NodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.nodegroup)` | NodeGroup  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apptopology.v1.NodeGroup;

Decodes a NodeGroup message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.nodegroup)` | NodeGroup  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apptopology.v1.INodeGroup, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NodeGroup message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.inodegroup)`   
NodeGroup message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apptopology.v1.INodeGroup, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified NodeGroup message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[INodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.inodegroup)`   
NodeGroup message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apptopology.v1.NodeGroup;

Creates a NodeGroup message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[NodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.nodegroup)` | NodeGroup  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for NodeGroup

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

Converts this NodeGroup to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apptopology.v1.NodeGroup, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a NodeGroup message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[NodeGroup](https://docs.cloud.google.com/nodejs/docs/reference/apptopology/latest/apptopology/protos.google.cloud.apptopology.v1.nodegroup)`   
NodeGroup  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a NodeGroup message.

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
