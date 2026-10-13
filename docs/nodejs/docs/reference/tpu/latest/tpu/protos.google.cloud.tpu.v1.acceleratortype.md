---
url: https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.acceleratortype
title: Class protos.google.cloud.tpu.v1.AcceleratorType (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:55.894096+00:00
---

# Class protos.google.cloud.tpu.v1.AcceleratorType (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.acceleratortype

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.tpu.v1.AcceleratorType (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.8.0  3.7.0  3.6.0  3.2.1  2.6.1  2.4.1  2.2.0  2.1.0  1.2.0  1.1.1  1.0.5 

Represents an AcceleratorType.

## Implements

[protos.google.cloud.tpu.v1.IAcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.iacceleratortype)

## Package

[@google-cloud/tpu](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.tpu.v1.IAcceleratorType);

Constructs a new AcceleratorType.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.iacceleratortype)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

AcceleratorType name.

### type
    
    
    public type: string;

AcceleratorType type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.tpu.v1.IAcceleratorType): google.cloud.tpu.v1.AcceleratorType;

Creates a new AcceleratorType instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.iacceleratortype)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.acceleratortype)` | AcceleratorType instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.tpu.v1.AcceleratorType;

Decodes an AcceleratorType message from the specified reader or buffer.

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
`[AcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.acceleratortype)` | AcceleratorType  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.tpu.v1.AcceleratorType;

Decodes an AcceleratorType message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.acceleratortype)` | AcceleratorType  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.tpu.v1.IAcceleratorType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AcceleratorType message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.iacceleratortype)`   
AcceleratorType message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.tpu.v1.IAcceleratorType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AcceleratorType message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.iacceleratortype)`   
AcceleratorType message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.tpu.v1.AcceleratorType;

Creates an AcceleratorType message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.acceleratortype)` | AcceleratorType  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AcceleratorType

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

Converts this AcceleratorType to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.tpu.v1.AcceleratorType, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AcceleratorType message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AcceleratorType](https://docs.cloud.google.com/nodejs/docs/reference/tpu/latest/tpu/protos.google.cloud.tpu.v1.acceleratortype)`   
AcceleratorType  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AcceleratorType message.

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
