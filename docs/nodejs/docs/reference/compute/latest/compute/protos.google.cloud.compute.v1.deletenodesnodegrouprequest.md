---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.deletenodesnodegrouprequest
title: Class protos.google.cloud.compute.v1.DeleteNodesNodeGroupRequest (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:02.783386+00:00
---

# Class protos.google.cloud.compute.v1.DeleteNodesNodeGroupRequest (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.deletenodesnodegrouprequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1.DeleteNodesNodeGroupRequest (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a DeleteNodesNodeGroupRequest.

## Implements

[protos.google.cloud.compute.v1.IDeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletenodesnodegrouprequest)

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.compute.v1.IDeleteNodesNodeGroupRequest);

Constructs a new DeleteNodesNodeGroupRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletenodesnodegrouprequest)`   
Properties to set  
  
## Properties 

### nodeGroup
    
    
    public nodeGroup: string;

DeleteNodesNodeGroupRequest nodeGroup.

### nodeGroupsDeleteNodesRequestResource
    
    
    public nodeGroupsDeleteNodesRequestResource?: (google.cloud.compute.v1.INodeGroupsDeleteNodesRequest|null);

DeleteNodesNodeGroupRequest nodeGroupsDeleteNodesRequestResource.

### project
    
    
    public project: string;

DeleteNodesNodeGroupRequest project.

### requestId
    
    
    public requestId?: (string|null);

DeleteNodesNodeGroupRequest requestId.

### zone
    
    
    public zone: string;

DeleteNodesNodeGroupRequest zone.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.compute.v1.IDeleteNodesNodeGroupRequest): google.cloud.compute.v1.DeleteNodesNodeGroupRequest;

Creates a new DeleteNodesNodeGroupRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletenodesnodegrouprequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.deletenodesnodegrouprequest)` | DeleteNodesNodeGroupRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.compute.v1.DeleteNodesNodeGroupRequest;

Decodes a DeleteNodesNodeGroupRequest message from the specified reader or buffer.

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
`[DeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.deletenodesnodegrouprequest)` | DeleteNodesNodeGroupRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.compute.v1.DeleteNodesNodeGroupRequest;

Decodes a DeleteNodesNodeGroupRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.deletenodesnodegrouprequest)` | DeleteNodesNodeGroupRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.compute.v1.IDeleteNodesNodeGroupRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteNodesNodeGroupRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletenodesnodegrouprequest)`   
DeleteNodesNodeGroupRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.compute.v1.IDeleteNodesNodeGroupRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteNodesNodeGroupRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletenodesnodegrouprequest)`   
DeleteNodesNodeGroupRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.compute.v1.DeleteNodesNodeGroupRequest;

Creates a DeleteNodesNodeGroupRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.deletenodesnodegrouprequest)` | DeleteNodesNodeGroupRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteNodesNodeGroupRequest

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

Converts this DeleteNodesNodeGroupRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.compute.v1.DeleteNodesNodeGroupRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteNodesNodeGroupRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteNodesNodeGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.deletenodesnodegrouprequest)`   
DeleteNodesNodeGroupRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteNodesNodeGroupRequest message.

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
