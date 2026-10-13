---
url: https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.diskinfo
title: Class protos.google.cloud.gdchardwaremanagement.v1alpha.Hardware.DiskInfo (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:36.725030+00:00
---

# Class protos.google.cloud.gdchardwaremanagement.v1alpha.Hardware.DiskInfo (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.diskinfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.gdchardwaremanagement.v1alpha.Hardware.DiskInfo (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.10.0  0.7.0  0.5.1  0.4.0  0.2.0 

Represents a DiskInfo.

## Implements

[protos.google.cloud.gdchardwaremanagement.v1alpha.Hardware.IDiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.idiskinfo)

## Package

[@google-cloud/gdchardwaremanagement](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.gdchardwaremanagement.v1alpha.Hardware.IDiskInfo);

Constructs a new DiskInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.idiskinfo)`   
Properties to set  
  
## Properties 

### manufacturer
    
    
    public manufacturer: string;

DiskInfo manufacturer.

### modelNumber
    
    
    public modelNumber: string;

DiskInfo modelNumber.

### partNumber
    
    
    public partNumber: string;

DiskInfo partNumber.

### psid
    
    
    public psid: string;

DiskInfo psid.

### serialNumber
    
    
    public serialNumber: string;

DiskInfo serialNumber.

### slot
    
    
    public slot: number;

DiskInfo slot.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.gdchardwaremanagement.v1alpha.Hardware.IDiskInfo): google.cloud.gdchardwaremanagement.v1alpha.Hardware.DiskInfo;

Creates a new DiskInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.idiskinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.diskinfo)` | DiskInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.gdchardwaremanagement.v1alpha.Hardware.DiskInfo;

Decodes a DiskInfo message from the specified reader or buffer.

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
`[DiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.diskinfo)` | DiskInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.gdchardwaremanagement.v1alpha.Hardware.DiskInfo;

Decodes a DiskInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.diskinfo)` | DiskInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.gdchardwaremanagement.v1alpha.Hardware.IDiskInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DiskInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.idiskinfo)`   
DiskInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.gdchardwaremanagement.v1alpha.Hardware.IDiskInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DiskInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.idiskinfo)`   
DiskInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.gdchardwaremanagement.v1alpha.Hardware.DiskInfo;

Creates a DiskInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.diskinfo)` | DiskInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DiskInfo

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

Converts this DiskInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.gdchardwaremanagement.v1alpha.Hardware.DiskInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DiskInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DiskInfo](https://docs.cloud.google.com/nodejs/docs/reference/gdchardwaremanagement/latest/gdchardwaremanagement/protos.google.cloud.gdchardwaremanagement.v1alpha.hardware.diskinfo)`   
DiskInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DiskInfo message.

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
