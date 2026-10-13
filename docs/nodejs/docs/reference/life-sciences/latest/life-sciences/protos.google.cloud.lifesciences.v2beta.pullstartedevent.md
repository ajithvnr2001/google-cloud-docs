---
url: https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.pullstartedevent
title: Class protos.google.cloud.lifesciences.v2beta.PullStartedEvent (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:31.621870+00:00
---

# Class protos.google.cloud.lifesciences.v2beta.PullStartedEvent (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.pullstartedevent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.lifesciences.v2beta.PullStartedEvent (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  2.3.2  2.1.2  1.1.1  1.0.3 

Represents a PullStartedEvent.

## Implements

[protos.google.cloud.lifesciences.v2beta.IPullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.ipullstartedevent)

## Package

[@google-cloud/life-sciences](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.lifesciences.v2beta.IPullStartedEvent);

Constructs a new PullStartedEvent.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.ipullstartedevent)`   
Properties to set  
  
## Properties 

### imageUri
    
    
    public imageUri: string;

PullStartedEvent imageUri.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.lifesciences.v2beta.IPullStartedEvent): google.cloud.lifesciences.v2beta.PullStartedEvent;

Creates a new PullStartedEvent instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.ipullstartedevent)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.pullstartedevent)` | PullStartedEvent instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.lifesciences.v2beta.PullStartedEvent;

Decodes a PullStartedEvent message from the specified reader or buffer.

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
`[PullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.pullstartedevent)` | PullStartedEvent  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.lifesciences.v2beta.PullStartedEvent;

Decodes a PullStartedEvent message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.pullstartedevent)` | PullStartedEvent  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.lifesciences.v2beta.IPullStartedEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PullStartedEvent message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.ipullstartedevent)`   
PullStartedEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.lifesciences.v2beta.IPullStartedEvent, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PullStartedEvent message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.ipullstartedevent)`   
PullStartedEvent message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.lifesciences.v2beta.PullStartedEvent;

Creates a PullStartedEvent message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.pullstartedevent)` | PullStartedEvent  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PullStartedEvent

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

Converts this PullStartedEvent to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.lifesciences.v2beta.PullStartedEvent, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PullStartedEvent message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PullStartedEvent](https://docs.cloud.google.com/nodejs/docs/reference/life-sciences/latest/life-sciences/protos.google.cloud.lifesciences.v2beta.pullstartedevent)`   
PullStartedEvent  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PullStartedEvent message.

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
