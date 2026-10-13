---
url: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplan
title: Class protos.google.cloud.capacityplanner.v1beta.CapacityPlan (0.1.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:43.739866+00:00
---

# Class protos.google.cloud.capacityplanner.v1beta.CapacityPlan (0.1.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplan

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.capacityplanner.v1beta.CapacityPlan (0.1.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.2 

Represents a CapacityPlan.

## Package

[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.capacityplanner.v1beta.ICapacityPlan);

Constructs a new CapacityPlan.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.icapacityplan)`   
Properties to set  
  
## Properties 

### capacityDemandMetadata
    
    
    public capacityDemandMetadata?: (google.cloud.capacityplanner.v1beta.IDemandMetadata|null);

CapacityPlan capacityDemandMetadata.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

CapacityPlan createTime.

### description
    
    
    public description: string;

CapacityPlan description.

### name
    
    
    public name: string;

CapacityPlan name.

### reporter
    
    
    public reporter?: (google.cloud.capacityplanner.v1beta.IUser|null);

CapacityPlan reporter.

### serviceDemands
    
    
    public serviceDemands: google.cloud.capacityplanner.v1beta.IServiceDemand[];

CapacityPlan serviceDemands.

### state
    
    
    public state: (google.cloud.capacityplanner.v1beta.State|keyof typeof google.cloud.capacityplanner.v1beta.State);

CapacityPlan state.

### title
    
    
    public title: string;

CapacityPlan title.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

CapacityPlan updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.capacityplanner.v1beta.ICapacityPlan): google.cloud.capacityplanner.v1beta.CapacityPlan;

Creates a new CapacityPlan instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.icapacityplan)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplan)` | CapacityPlan instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.capacityplanner.v1beta.CapacityPlan;

Decodes a CapacityPlan message from the specified reader or buffer.

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
`[CapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplan)` | CapacityPlan  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.capacityplanner.v1beta.CapacityPlan;

Decodes a CapacityPlan message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplan)` | CapacityPlan  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.capacityplanner.v1beta.ICapacityPlan, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CapacityPlan message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.icapacityplan)`   
CapacityPlan message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.capacityplanner.v1beta.ICapacityPlan, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CapacityPlan message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.icapacityplan)`   
CapacityPlan message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.capacityplanner.v1beta.CapacityPlan;

Creates a CapacityPlan message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplan)` | CapacityPlan  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CapacityPlan

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

Converts this CapacityPlan to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.capacityplanner.v1beta.CapacityPlan, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CapacityPlan message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplan)`   
CapacityPlan  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CapacityPlan message.

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
