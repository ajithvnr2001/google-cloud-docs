---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.boolvalue
title: Class protos.google.protobuf.BoolValue (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:15.081395+00:00
---

# Class protos.google.protobuf.BoolValue (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.boolvalue

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.BoolValue (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  0.4.2  0.3.2  0.2.1 

Represents a BoolValue.

## Implements

[protos.google.protobuf.IBoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.iboolvalue)

## Package

[@google-cloud/bigquery-data-exchange](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IBoolValue);

Constructs a new BoolValue.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.iboolvalue)`   
Properties to set  
  
## Properties 

### value
    
    
    public value: boolean;

BoolValue value.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IBoolValue): google.protobuf.BoolValue;

Creates a new BoolValue instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.iboolvalue)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.boolvalue)` | BoolValue instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.BoolValue;

Decodes a BoolValue message from the specified reader or buffer.

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
`[BoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.boolvalue)` | BoolValue  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.BoolValue;

Decodes a BoolValue message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.boolvalue)` | BoolValue  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IBoolValue, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BoolValue message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.iboolvalue)`   
BoolValue message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IBoolValue, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BoolValue message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.iboolvalue)`   
BoolValue message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.BoolValue;

Creates a BoolValue message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.boolvalue)` | BoolValue  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BoolValue

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

Converts this BoolValue to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.BoolValue, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BoolValue message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BoolValue](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-data-exchange/latest/bigquery-data-exchange/protos.google.protobuf.boolvalue)`   
BoolValue  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BoolValue message.

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
