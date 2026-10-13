---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.interval
title: Class protos.google.type.Interval (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:42.482798+00:00
---

# Class protos.google.type.Interval (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.interval

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.type.Interval (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents an Interval.

## Implements

[protos.google.type.IInterval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.iinterval)

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.type.IInterval);

Constructs a new Interval.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInterval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.iinterval)`   
Properties to set  
  
## Properties 

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

Interval endTime.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

Interval startTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.type.IInterval): google.type.Interval;

Creates a new Interval instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInterval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.iinterval)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Interval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.interval)` | Interval instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.type.Interval;

Decodes an Interval message from the specified reader or buffer.

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
`[Interval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.interval)` | Interval  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.type.Interval;

Decodes an Interval message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Interval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.interval)` | Interval  
  
### encode(message, writer)
    
    
    public static encode(message: google.type.IInterval, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Interval message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInterval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.iinterval)`   
Interval message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.type.IInterval, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Interval message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInterval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.iinterval)`   
Interval message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.type.Interval;

Creates an Interval message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Interval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.interval)` | Interval  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Interval

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

Converts this Interval to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.type.Interval, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Interval message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Interval](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.type.interval)`   
Interval  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Interval message.

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
