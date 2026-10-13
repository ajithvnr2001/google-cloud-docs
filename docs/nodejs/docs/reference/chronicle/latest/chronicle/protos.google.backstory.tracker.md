---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.tracker
title: Class protos.google.backstory.Tracker (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:32.299091+00:00
---

# Class protos.google.backstory.Tracker (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.tracker

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.backstory.Tracker (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a Tracker.

## Implements

[protos.google.backstory.ITracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.itracker)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.backstory.ITracker);

Constructs a new Tracker.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.itracker)`   
Properties to set  
  
## Properties 

### id
    
    
    public id: string;

Tracker id.

### timestamp
    
    
    public timestamp?: (google.protobuf.ITimestamp|null);

Tracker timestamp.

### tracker
    
    
    public tracker: string;

Tracker tracker.

### url
    
    
    public url: string;

Tracker url.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.backstory.ITracker): google.backstory.Tracker;

Creates a new Tracker instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ITracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.itracker)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Tracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.tracker)` | Tracker instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.backstory.Tracker;

Decodes a Tracker message from the specified reader or buffer.

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
`[Tracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.tracker)` | Tracker  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.backstory.Tracker;

Decodes a Tracker message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Tracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.tracker)` | Tracker  
  
### encode(message, writer)
    
    
    public static encode(message: google.backstory.ITracker, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Tracker message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.itracker)`   
Tracker message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.backstory.ITracker, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Tracker message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ITracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.itracker)`   
Tracker message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.backstory.Tracker;

Creates a Tracker message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Tracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.tracker)` | Tracker  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Tracker

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

Converts this Tracker to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.backstory.Tracker, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Tracker message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Tracker](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.tracker)`   
Tracker  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Tracker message.

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
