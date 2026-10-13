---
url: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.reportstatus-class
title: Class protos.google.cloud.channel.v1.ReportStatus (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:33.330592+00:00
---

# Class protos.google.cloud.channel.v1.ReportStatus (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.reportstatus-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.channel.v1.ReportStatus (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.2  3.6.0  3.2.1  3.0.0  2.5.1  2.4.1  2.2.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6 

Represents a ReportStatus.

## Implements

[protos.google.cloud.channel.v1.IReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ireportstatus)

## Package

[@google-cloud/channel](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.channel.v1.IReportStatus);

Constructs a new ReportStatus.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ireportstatus)`   
Properties to set  
  
## Properties 

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

ReportStatus endTime.

### startTime
    
    
    public startTime?: (google.protobuf.ITimestamp|null);

ReportStatus startTime.

### state
    
    
    public state: (google.cloud.channel.v1.ReportStatus.State|keyof typeof google.cloud.channel.v1.ReportStatus.State);

ReportStatus state.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.channel.v1.IReportStatus): google.cloud.channel.v1.ReportStatus;

Creates a new ReportStatus instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ireportstatus)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.reportstatus-class)` | ReportStatus instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.channel.v1.ReportStatus;

Decodes a ReportStatus message from the specified reader or buffer.

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
`[ReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.reportstatus-class)` | ReportStatus  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.channel.v1.ReportStatus;

Decodes a ReportStatus message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.reportstatus-class)` | ReportStatus  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.channel.v1.IReportStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ReportStatus message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ireportstatus)`   
ReportStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.channel.v1.IReportStatus, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ReportStatus message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ireportstatus)`   
ReportStatus message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.channel.v1.ReportStatus;

Creates a ReportStatus message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.reportstatus-class)` | ReportStatus  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ReportStatus

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

Converts this ReportStatus to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.channel.v1.ReportStatus, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ReportStatus message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ReportStatus](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.reportstatus-class)`   
ReportStatus  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ReportStatus message.

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
