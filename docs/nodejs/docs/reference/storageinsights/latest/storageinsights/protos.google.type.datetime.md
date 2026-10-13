---
url: https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.datetime
title: Class protos.google.type.DateTime (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:47.177294+00:00
---

# Class protos.google.type.DateTime (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.datetime

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.type.DateTime (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.3.0  2.1.0  0.1.1 

Represents a DateTime.

## Implements

[protos.google.type.IDateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.idatetime)

## Package

[@google-cloud/storageinsights](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.type.IDateTime);

Constructs a new DateTime.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.idatetime)`   
Properties to set  
  
## Properties 

### day
    
    
    public day: number;

DateTime day.

### hours
    
    
    public hours: number;

DateTime hours.

### minutes
    
    
    public minutes: number;

DateTime minutes.

### month
    
    
    public month: number;

DateTime month.

### nanos
    
    
    public nanos: number;

DateTime nanos.

### seconds
    
    
    public seconds: number;

DateTime seconds.

### timeOffset
    
    
    public timeOffset?: ("utcOffset"|"timeZone");

DateTime timeOffset.

### timeZone
    
    
    public timeZone?: (google.type.ITimeZone|null);

DateTime timeZone.

### utcOffset
    
    
    public utcOffset?: (google.protobuf.IDuration|null);

DateTime utcOffset.

### year
    
    
    public year: number;

DateTime year.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.type.IDateTime): google.type.DateTime;

Creates a new DateTime instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.idatetime)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.datetime)` | DateTime instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.type.DateTime;

Decodes a DateTime message from the specified reader or buffer.

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
`[DateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.datetime)` | DateTime  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.type.DateTime;

Decodes a DateTime message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.datetime)` | DateTime  
  
### encode(message, writer)
    
    
    public static encode(message: google.type.IDateTime, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DateTime message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.idatetime)`   
DateTime message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.type.IDateTime, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DateTime message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.idatetime)`   
DateTime message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.type.DateTime;

Creates a DateTime message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.datetime)` | DateTime  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DateTime

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

Converts this DateTime to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.type.DateTime, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DateTime message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DateTime](https://docs.cloud.google.com/nodejs/docs/reference/storageinsights/latest/storageinsights/protos.google.type.datetime)`   
DateTime  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DateTime message.

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
