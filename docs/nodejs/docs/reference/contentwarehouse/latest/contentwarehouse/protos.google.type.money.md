---
url: https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.money
title: Class protos.google.type.Money (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:44.534694+00:00
---

# Class protos.google.type.Money (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.money

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.type.Money (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.4.0  1.10.0  1.9.0  1.7.0  1.5.0  1.4.0  1.3.0  0.5.1  0.4.0  0.3.1  0.1.2 

Represents a Money.

## Implements

[protos.google.type.IMoney](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.imoney)

## Package

[@google-cloud/contentwarehouse](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.type.IMoney);

Constructs a new Money.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMoney](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.imoney)`   
Properties to set  
  
## Properties 

### currencyCode
    
    
    public currencyCode: string;

Money currencyCode.

### nanos
    
    
    public nanos: number;

Money nanos.

### units
    
    
    public units: (number|Long|string);

Money units.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.type.IMoney): google.type.Money;

Creates a new Money instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMoney](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.imoney)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Money](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.money)` | Money instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.type.Money;

Decodes a Money message from the specified reader or buffer.

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
`[Money](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.money)` | Money  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.type.Money;

Decodes a Money message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Money](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.money)` | Money  
  
### encode(message, writer)
    
    
    public static encode(message: google.type.IMoney, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Money message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMoney](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.imoney)`   
Money message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.type.IMoney, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Money message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMoney](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.imoney)`   
Money message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.type.Money;

Creates a Money message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Money](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.money)` | Money  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Money

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

Converts this Money to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.type.Money, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Money message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Money](https://docs.cloud.google.com/nodejs/docs/reference/contentwarehouse/latest/contentwarehouse/protos.google.type.money)`   
Money  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Money message.

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
