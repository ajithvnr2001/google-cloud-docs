---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.floatvalue
title: Class protos.google.protobuf.FloatValue (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:41.147898+00:00
---

# Class protos.google.protobuf.FloatValue (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.floatvalue

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.FloatValue (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a FloatValue.

## Implements

[protos.google.protobuf.IFloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.ifloatvalue)

## Package

[@google-cloud/bigquery-storage-api](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IFloatValue);

Constructs a new FloatValue.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.ifloatvalue)`   
Properties to set  
  
## Properties 

### value
    
    
    public value: number;

FloatValue value.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IFloatValue): google.protobuf.FloatValue;

Creates a new FloatValue instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.ifloatvalue)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.floatvalue)` | FloatValue instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.FloatValue;

Decodes a FloatValue message from the specified reader or buffer.

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
`[FloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.floatvalue)` | FloatValue  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.FloatValue;

Decodes a FloatValue message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.floatvalue)` | FloatValue  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IFloatValue, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FloatValue message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.ifloatvalue)`   
FloatValue message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IFloatValue, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FloatValue message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.ifloatvalue)`   
FloatValue message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.FloatValue;

Creates a FloatValue message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.floatvalue)` | FloatValue  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FloatValue

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

Converts this FloatValue to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.FloatValue, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FloatValue message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FloatValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-storage-api/latest/bigquery-storage-api/protos.google.protobuf.floatvalue)`   
FloatValue  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FloatValue message.

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

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
