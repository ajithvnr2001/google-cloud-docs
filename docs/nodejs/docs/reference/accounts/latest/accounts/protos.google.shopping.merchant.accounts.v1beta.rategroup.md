---
url: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.rategroup
title: Class protos.google.shopping.merchant.accounts.v1beta.RateGroup (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:03.073886+00:00
---

# Class protos.google.shopping.merchant.accounts.v1beta.RateGroup (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.rategroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.accounts.v1beta.RateGroup (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  3.2.0  2.2.0  1.0.0 

Represents a RateGroup.

## Implements

[protos.google.shopping.merchant.accounts.v1beta.IRateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.irategroup)

## Package

[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.accounts.v1beta.IRateGroup);

Constructs a new RateGroup.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.irategroup)`   
Properties to set  
  
## Properties 

### applicableShippingLabels
    
    
    public applicableShippingLabels: string[];

RateGroup applicableShippingLabels.

### carrierRates
    
    
    public carrierRates: google.shopping.merchant.accounts.v1beta.ICarrierRate[];

RateGroup carrierRates.

### mainTable
    
    
    public mainTable?: (google.shopping.merchant.accounts.v1beta.ITable|null);

RateGroup mainTable.

### name
    
    
    public name?: (string|null);

RateGroup name.

### singleValue
    
    
    public singleValue?: (google.shopping.merchant.accounts.v1beta.IValue|null);

RateGroup singleValue.

### subtables
    
    
    public subtables: google.shopping.merchant.accounts.v1beta.ITable[];

RateGroup subtables.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.accounts.v1beta.IRateGroup): google.shopping.merchant.accounts.v1beta.RateGroup;

Creates a new RateGroup instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.irategroup)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.rategroup)` | RateGroup instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.accounts.v1beta.RateGroup;

Decodes a RateGroup message from the specified reader or buffer.

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
`[RateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.rategroup)` | RateGroup  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.accounts.v1beta.RateGroup;

Decodes a RateGroup message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.rategroup)` | RateGroup  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.accounts.v1beta.IRateGroup, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RateGroup message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.irategroup)`   
RateGroup message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.accounts.v1beta.IRateGroup, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RateGroup message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.irategroup)`   
RateGroup message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.accounts.v1beta.RateGroup;

Creates a RateGroup message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.rategroup)` | RateGroup  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RateGroup

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

Converts this RateGroup to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.accounts.v1beta.RateGroup, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RateGroup message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RateGroup](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1beta.rategroup)`   
RateGroup  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RateGroup message.

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
