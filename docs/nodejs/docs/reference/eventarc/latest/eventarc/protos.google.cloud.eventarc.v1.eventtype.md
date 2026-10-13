---
url: https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventtype
title: Class protos.google.cloud.eventarc.v1.EventType (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:59:49.125998+00:00
---

# Class protos.google.cloud.eventarc.v1.EventType (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventtype

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.eventarc.v1.EventType (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.3.0  4.1.0  4.0.1  3.2.0  2.3.2  2.2.0  2.1.1  1.2.0  1.1.2  1.0.3 

Represents an EventType.

## Implements

[protos.google.cloud.eventarc.v1.IEventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ieventtype)

## Package

[@google-cloud/eventarc](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.eventarc.v1.IEventType);

Constructs a new EventType.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ieventtype)`   
Properties to set  
  
## Properties 

### description
    
    
    public description: string;

EventType description.

### eventSchemaUri
    
    
    public eventSchemaUri: string;

EventType eventSchemaUri.

### filteringAttributes
    
    
    public filteringAttributes: google.cloud.eventarc.v1.IFilteringAttribute[];

EventType filteringAttributes.

### type
    
    
    public type: string;

EventType type.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.eventarc.v1.IEventType): google.cloud.eventarc.v1.EventType;

Creates a new EventType instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ieventtype)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventtype)` | EventType instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.eventarc.v1.EventType;

Decodes an EventType message from the specified reader or buffer.

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
`[EventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventtype)` | EventType  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.eventarc.v1.EventType;

Decodes an EventType message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventtype)` | EventType  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.eventarc.v1.IEventType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EventType message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ieventtype)`   
EventType message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.eventarc.v1.IEventType, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EventType message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ieventtype)`   
EventType message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.eventarc.v1.EventType;

Creates an EventType message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventtype)` | EventType  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EventType

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

Converts this EventType to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.eventarc.v1.EventType, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EventType message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EventType](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.eventtype)`   
EventType  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EventType message.

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
