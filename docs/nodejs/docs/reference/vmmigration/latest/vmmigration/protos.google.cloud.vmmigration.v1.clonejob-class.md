---
url: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.clonejob-class
title: Class protos.google.cloud.vmmigration.v1.CloneJob (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:06.601393+00:00
---

# Class protos.google.cloud.vmmigration.v1.CloneJob (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.clonejob-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.vmmigration.v1.CloneJob (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.2  2.3.2  2.2.1  2.1.0  1.0.0  0.2.0 

Represents a CloneJob.

## Implements

[protos.google.cloud.vmmigration.v1.ICloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iclonejob)

## Package

[@google-cloud/vmmigration](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.vmmigration.v1.ICloneJob);

Constructs a new CloneJob.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iclonejob)`   
Properties to set  
  
## Properties 

### computeEngineDisksTargetDetails
    
    
    public computeEngineDisksTargetDetails?: (google.cloud.vmmigration.v1.IComputeEngineDisksTargetDetails|null);

CloneJob computeEngineDisksTargetDetails.

### computeEngineTargetDetails
    
    
    public computeEngineTargetDetails?: (google.cloud.vmmigration.v1.IComputeEngineTargetDetails|null);

CloneJob computeEngineTargetDetails.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

CloneJob createTime.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

CloneJob endTime.

### error
    
    
    public error?: (google.rpc.IStatus|null);

CloneJob error.

### name
    
    
    public name: string;

CloneJob name.

### state
    
    
    public state: (google.cloud.vmmigration.v1.CloneJob.State|keyof typeof google.cloud.vmmigration.v1.CloneJob.State);

CloneJob state.

### stateTime
    
    
    public stateTime?: (google.protobuf.ITimestamp|null);

CloneJob stateTime.

### steps
    
    
    public steps: google.cloud.vmmigration.v1.ICloneStep[];

CloneJob steps.

### targetVmDetails
    
    
    public targetVmDetails?: ("computeEngineTargetDetails"|"computeEngineDisksTargetDetails");

CloneJob targetVmDetails.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.vmmigration.v1.ICloneJob): google.cloud.vmmigration.v1.CloneJob;

Creates a new CloneJob instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iclonejob)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.clonejob-class)` | CloneJob instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.vmmigration.v1.CloneJob;

Decodes a CloneJob message from the specified reader or buffer.

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
`[CloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.clonejob-class)` | CloneJob  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.vmmigration.v1.CloneJob;

Decodes a CloneJob message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.clonejob-class)` | CloneJob  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.vmmigration.v1.ICloneJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CloneJob message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iclonejob)`   
CloneJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.vmmigration.v1.ICloneJob, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CloneJob message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.iclonejob)`   
CloneJob message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.vmmigration.v1.CloneJob;

Creates a CloneJob message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.clonejob-class)` | CloneJob  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CloneJob

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

Converts this CloneJob to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.vmmigration.v1.CloneJob, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CloneJob message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CloneJob](https://docs.cloud.google.com/nodejs/docs/reference/vmmigration/latest/vmmigration/protos.google.cloud.vmmigration.v1.clonejob-class)`   
CloneJob  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CloneJob message.

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
