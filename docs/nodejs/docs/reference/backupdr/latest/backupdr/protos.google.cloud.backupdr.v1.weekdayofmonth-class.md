---
url: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.weekdayofmonth-class
title: Class protos.google.cloud.backupdr.v1.WeekDayOfMonth (0.12.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:09.430310+00:00
---

# Class protos.google.cloud.backupdr.v1.WeekDayOfMonth (0.12.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.weekdayofmonth-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.backupdr.v1.WeekDayOfMonth (0.12.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.1 (latest)  0.12.0  0.9.0  0.8.0  0.7.0  0.6.0  0.1.0 

Represents a WeekDayOfMonth.

## Implements

[protos.google.cloud.backupdr.v1.IWeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iweekdayofmonth)

## Package

[@google-cloud/backupdr](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.backupdr.v1.IWeekDayOfMonth);

Constructs a new WeekDayOfMonth.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IWeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iweekdayofmonth)`   
Properties to set  
  
## Properties 

### dayOfWeek
    
    
    public dayOfWeek: (google.type.DayOfWeek|keyof typeof google.type.DayOfWeek);

WeekDayOfMonth dayOfWeek.

### weekOfMonth
    
    
    public weekOfMonth: (google.cloud.backupdr.v1.WeekDayOfMonth.WeekOfMonth|keyof typeof google.cloud.backupdr.v1.WeekDayOfMonth.WeekOfMonth);

WeekDayOfMonth weekOfMonth.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.backupdr.v1.IWeekDayOfMonth): google.cloud.backupdr.v1.WeekDayOfMonth;

Creates a new WeekDayOfMonth instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IWeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iweekdayofmonth)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[WeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.weekdayofmonth-class)` | WeekDayOfMonth instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.backupdr.v1.WeekDayOfMonth;

Decodes a WeekDayOfMonth message from the specified reader or buffer.

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
`[WeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.weekdayofmonth-class)` | WeekDayOfMonth  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.backupdr.v1.WeekDayOfMonth;

Decodes a WeekDayOfMonth message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[WeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.weekdayofmonth-class)` | WeekDayOfMonth  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.backupdr.v1.IWeekDayOfMonth, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified WeekDayOfMonth message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IWeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iweekdayofmonth)`   
WeekDayOfMonth message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.backupdr.v1.IWeekDayOfMonth, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified WeekDayOfMonth message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IWeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.iweekdayofmonth)`   
WeekDayOfMonth message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.backupdr.v1.WeekDayOfMonth;

Creates a WeekDayOfMonth message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[WeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.weekdayofmonth-class)` | WeekDayOfMonth  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for WeekDayOfMonth

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

Converts this WeekDayOfMonth to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.backupdr.v1.WeekDayOfMonth, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a WeekDayOfMonth message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[WeekDayOfMonth](https://docs.cloud.google.com/nodejs/docs/reference/backupdr/latest/backupdr/protos.google.cloud.backupdr.v1.weekdayofmonth-class)`   
WeekDayOfMonth  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a WeekDayOfMonth message.

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
