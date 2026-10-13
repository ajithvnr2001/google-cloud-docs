---
url: https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.deviceinfo-class
title: Class protos.google.cloud.talent.v4beta1.DeviceInfo (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:02.648508+00:00
---

# Class protos.google.cloud.talent.v4beta1.DeviceInfo (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.deviceinfo-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.talent.v4beta1.DeviceInfo (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.2.0  6.4.0  6.3.1  6.0.2  5.1.3  5.0.1  4.1.1  3.5.1  3.4.1  3.3.0  3.2.7 

Represents a DeviceInfo.

## Implements

[protos.google.cloud.talent.v4beta1.IDeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ideviceinfo)

## Package

[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.talent.v4beta1.IDeviceInfo);

Constructs a new DeviceInfo.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ideviceinfo)`   
Properties to set  
  
## Properties 

### deviceType
    
    
    public deviceType: (google.cloud.talent.v4beta1.DeviceInfo.DeviceType|keyof typeof google.cloud.talent.v4beta1.DeviceInfo.DeviceType);

DeviceInfo deviceType.

### id
    
    
    public id: string;

DeviceInfo id.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.talent.v4beta1.IDeviceInfo): google.cloud.talent.v4beta1.DeviceInfo;

Creates a new DeviceInfo instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ideviceinfo)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.deviceinfo-class)` | DeviceInfo instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.talent.v4beta1.DeviceInfo;

Decodes a DeviceInfo message from the specified reader or buffer.

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
`[DeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.deviceinfo-class)` | DeviceInfo  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.talent.v4beta1.DeviceInfo;

Decodes a DeviceInfo message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.deviceinfo-class)` | DeviceInfo  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.talent.v4beta1.IDeviceInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeviceInfo message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ideviceinfo)`   
DeviceInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.talent.v4beta1.IDeviceInfo, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeviceInfo message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ideviceinfo)`   
DeviceInfo message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.talent.v4beta1.DeviceInfo;

Creates a DeviceInfo message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.deviceinfo-class)` | DeviceInfo  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeviceInfo

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

Converts this DeviceInfo to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.talent.v4beta1.DeviceInfo, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeviceInfo message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeviceInfo](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.deviceinfo-class)`   
DeviceInfo  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeviceInfo message.

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
