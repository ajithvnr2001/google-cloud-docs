---
url: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.splitpoints-class
title: Class protos.google.spanner.admin.database.v1.SplitPoints (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:00.691592+00:00
---

# Class protos.google.spanner.admin.database.v1.SplitPoints (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.splitpoints-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.spanner.admin.database.v1.SplitPoints (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a SplitPoints.

## Implements

[protos.google.spanner.admin.database.v1.ISplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.isplitpoints)

## Package

[@google-cloud/spanner-api](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.spanner.admin.database.v1.ISplitPoints);

Constructs a new SplitPoints.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.isplitpoints)`   
Properties to set  
  
## Properties 

### expireTime
    
    
    public expireTime?: (google.protobuf.ITimestamp|null);

SplitPoints expireTime.

### index
    
    
    public index: string;

SplitPoints index.

### keys
    
    
    public keys: google.spanner.admin.database.v1.SplitPoints.IKey[];

SplitPoints keys.

### table
    
    
    public table: string;

SplitPoints table.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.spanner.admin.database.v1.ISplitPoints): google.spanner.admin.database.v1.SplitPoints;

Creates a new SplitPoints instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.isplitpoints)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.splitpoints-class)` | SplitPoints instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.spanner.admin.database.v1.SplitPoints;

Decodes a SplitPoints message from the specified reader or buffer.

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
`[SplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.splitpoints-class)` | SplitPoints  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.spanner.admin.database.v1.SplitPoints;

Decodes a SplitPoints message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.splitpoints-class)` | SplitPoints  
  
### encode(message, writer)
    
    
    public static encode(message: google.spanner.admin.database.v1.ISplitPoints, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SplitPoints message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.isplitpoints)`   
SplitPoints message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.spanner.admin.database.v1.ISplitPoints, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SplitPoints message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.isplitpoints)`   
SplitPoints message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.spanner.admin.database.v1.SplitPoints;

Creates a SplitPoints message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.splitpoints-class)` | SplitPoints  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SplitPoints

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

Converts this SplitPoints to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.spanner.admin.database.v1.SplitPoints, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SplitPoints message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SplitPoints](https://docs.cloud.google.com/nodejs/docs/reference/spanner-api/latest/spanner-api/protos.google.spanner.admin.database.v1.splitpoints-class)`   
SplitPoints  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SplitPoints message.

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

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
