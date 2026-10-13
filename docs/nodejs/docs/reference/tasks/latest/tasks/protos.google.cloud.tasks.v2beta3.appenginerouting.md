---
url: https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginerouting
title: Class protos.google.cloud.tasks.v2beta3.AppEngineRouting (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:26.587795+00:00
---

# Class protos.google.cloud.tasks.v2beta3.AppEngineRouting (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginerouting

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.tasks.v2beta3.AppEngineRouting (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.2.0  7.1.1  5.5.2  3.1.2  3.0.5  2.5.0  2.4.2  2.3.6 

Represents an AppEngineRouting.

## Implements

[protos.google.cloud.tasks.v2beta3.IAppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginerouting)

## Package

[@google-cloud/tasks](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.tasks.v2beta3.IAppEngineRouting);

Constructs a new AppEngineRouting.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginerouting)`   
Properties to set  
  
## Properties 

### host
    
    
    public host: string;

AppEngineRouting host.

### instance
    
    
    public instance: string;

AppEngineRouting instance.

### service
    
    
    public service: string;

AppEngineRouting service.

### version
    
    
    public version: string;

AppEngineRouting version.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.tasks.v2beta3.IAppEngineRouting): google.cloud.tasks.v2beta3.AppEngineRouting;

Creates a new AppEngineRouting instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginerouting)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginerouting)` | AppEngineRouting instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.tasks.v2beta3.AppEngineRouting;

Decodes an AppEngineRouting message from the specified reader or buffer.

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
`[AppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginerouting)` | AppEngineRouting  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.tasks.v2beta3.AppEngineRouting;

Decodes an AppEngineRouting message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginerouting)` | AppEngineRouting  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.tasks.v2beta3.IAppEngineRouting, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppEngineRouting message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginerouting)`   
AppEngineRouting message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.tasks.v2beta3.IAppEngineRouting, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppEngineRouting message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginerouting)`   
AppEngineRouting message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.tasks.v2beta3.AppEngineRouting;

Creates an AppEngineRouting message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginerouting)` | AppEngineRouting  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AppEngineRouting

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

Converts this AppEngineRouting to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.tasks.v2beta3.AppEngineRouting, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AppEngineRouting message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AppEngineRouting](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginerouting)`   
AppEngineRouting  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AppEngineRouting message.

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
