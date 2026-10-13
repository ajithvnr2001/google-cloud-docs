---
url: https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.oraclecolumn
title: Class protos.google.cloud.datastream.v1.OracleColumn (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:34.038067+00:00
---

# Class protos.google.cloud.datastream.v1.OracleColumn (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.oraclecolumn

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datastream.v1.OracleColumn (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.0.1  3.4.0  3.3.0  3.1.0  2.2.2  2.1.2  1.1.0  1.0.0  0.2.0 

Represents an OracleColumn.

## Implements

[protos.google.cloud.datastream.v1.IOracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.ioraclecolumn)

## Package

[@google-cloud/datastream](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.datastream.v1.IOracleColumn);

Constructs a new OracleColumn.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.ioraclecolumn)`   
Properties to set  
  
## Properties 

### column
    
    
    public column: string;

OracleColumn column.

### dataType
    
    
    public dataType: string;

OracleColumn dataType.

### encoding
    
    
    public encoding: string;

OracleColumn encoding.

### length
    
    
    public length: number;

OracleColumn length.

### nullable
    
    
    public nullable: boolean;

OracleColumn nullable.

### ordinalPosition
    
    
    public ordinalPosition: number;

OracleColumn ordinalPosition.

### precision
    
    
    public precision: number;

OracleColumn precision.

### primaryKey
    
    
    public primaryKey: boolean;

OracleColumn primaryKey.

### scale
    
    
    public scale: number;

OracleColumn scale.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.datastream.v1.IOracleColumn): google.cloud.datastream.v1.OracleColumn;

Creates a new OracleColumn instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IOracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.ioraclecolumn)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[OracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.oraclecolumn)` | OracleColumn instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.datastream.v1.OracleColumn;

Decodes an OracleColumn message from the specified reader or buffer.

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
`[OracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.oraclecolumn)` | OracleColumn  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.datastream.v1.OracleColumn;

Decodes an OracleColumn message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[OracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.oraclecolumn)` | OracleColumn  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.datastream.v1.IOracleColumn, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OracleColumn message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.ioraclecolumn)`   
OracleColumn message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.datastream.v1.IOracleColumn, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified OracleColumn message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IOracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.ioraclecolumn)`   
OracleColumn message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.datastream.v1.OracleColumn;

Creates an OracleColumn message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[OracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.oraclecolumn)` | OracleColumn  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for OracleColumn

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

Converts this OracleColumn to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.datastream.v1.OracleColumn, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an OracleColumn message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[OracleColumn](https://docs.cloud.google.com/nodejs/docs/reference/datastream/latest/datastream/protos.google.cloud.datastream.v1.oraclecolumn)`   
OracleColumn  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an OracleColumn message.

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
