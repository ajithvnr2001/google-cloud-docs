---
url: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.machineshape
title: Class protos.google.cloud.capacityplanner.v1beta.MachineShape (0.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:35.510417+00:00
---

# Class protos.google.cloud.capacityplanner.v1beta.MachineShape (0.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.machineshape

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.capacityplanner.v1beta.MachineShape (0.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.2 

Represents a MachineShape.

## Implements

[protos.google.cloud.capacityplanner.v1beta.IMachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.imachineshape)

## Package

[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.capacityplanner.v1beta.IMachineShape);

Constructs a new MachineShape.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.imachineshape)`   
Properties to set  
  
## Properties 

### cpuCores
    
    
    public cpuCores: number;

MachineShape cpuCores.

### gpuComputeType
    
    
    public gpuComputeType: string;

MachineShape gpuComputeType.

### gpuCores
    
    
    public gpuCores: (number|Long|string);

MachineShape gpuCores.

### gpuType
    
    
    public gpuType: string;

MachineShape gpuType.

### localSsdGb
    
    
    public localSsdGb: number;

MachineShape localSsdGb.

### localSsdInterface
    
    
    public localSsdInterface: string;

MachineShape localSsdInterface.

### localSsdPartitions
    
    
    public localSsdPartitions: (number|Long|string);

MachineShape localSsdPartitions.

### machineFamily
    
    
    public machineFamily: string;

MachineShape machineFamily.

### machineShape
    
    
    public machineShape: string;

MachineShape machineShape.

### machineType
    
    
    public machineType: string;

MachineShape machineType.

### memoryGb
    
    
    public memoryGb: number;

MachineShape memoryGb.

### minCpuPlatform
    
    
    public minCpuPlatform: string;

MachineShape minCpuPlatform.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.capacityplanner.v1beta.IMachineShape): google.cloud.capacityplanner.v1beta.MachineShape;

Creates a new MachineShape instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.imachineshape)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[MachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.machineshape)` | MachineShape instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.capacityplanner.v1beta.MachineShape;

Decodes a MachineShape message from the specified reader or buffer.

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
`[MachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.machineshape)` | MachineShape  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.capacityplanner.v1beta.MachineShape;

Decodes a MachineShape message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[MachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.machineshape)` | MachineShape  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.capacityplanner.v1beta.IMachineShape, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MachineShape message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.imachineshape)`   
MachineShape message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.capacityplanner.v1beta.IMachineShape, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified MachineShape message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.imachineshape)`   
MachineShape message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.capacityplanner.v1beta.MachineShape;

Creates a MachineShape message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[MachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.machineshape)` | MachineShape  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for MachineShape

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

Converts this MachineShape to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.capacityplanner.v1beta.MachineShape, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a MachineShape message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[MachineShape](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.machineshape)`   
MachineShape  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a MachineShape message.

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
