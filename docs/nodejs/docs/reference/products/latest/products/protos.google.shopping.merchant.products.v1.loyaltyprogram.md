---
url: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.loyaltyprogram
title: Class protos.google.shopping.merchant.products.v1.LoyaltyProgram (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:19.599789+00:00
---

# Class protos.google.shopping.merchant.products.v1.LoyaltyProgram (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.loyaltyprogram

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.products.v1.LoyaltyProgram (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.1.1 

Represents a LoyaltyProgram.

## Implements

[protos.google.shopping.merchant.products.v1.ILoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iloyaltyprogram)

## Package

[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.products.v1.ILoyaltyProgram);

Constructs a new LoyaltyProgram.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iloyaltyprogram)`   
Properties to set  
  
## Properties 

### cashbackForFutureUse
    
    
    public cashbackForFutureUse?: (google.shopping.type.IPrice|null);

LoyaltyProgram cashbackForFutureUse.

### loyaltyPoints
    
    
    public loyaltyPoints?: (number|Long|string|null);

LoyaltyProgram loyaltyPoints.

### memberPriceEffectiveDate
    
    
    public memberPriceEffectiveDate?: (google.type.IInterval|null);

LoyaltyProgram memberPriceEffectiveDate.

### price
    
    
    public price?: (google.shopping.type.IPrice|null);

LoyaltyProgram price.

### programLabel
    
    
    public programLabel?: (string|null);

LoyaltyProgram programLabel.

### shippingLabel
    
    
    public shippingLabel?: (string|null);

LoyaltyProgram shippingLabel.

### tierLabel
    
    
    public tierLabel?: (string|null);

LoyaltyProgram tierLabel.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.products.v1.ILoyaltyProgram): google.shopping.merchant.products.v1.LoyaltyProgram;

Creates a new LoyaltyProgram instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iloyaltyprogram)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.loyaltyprogram)` | LoyaltyProgram instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.products.v1.LoyaltyProgram;

Decodes a LoyaltyProgram message from the specified reader or buffer.

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
`[LoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.loyaltyprogram)` | LoyaltyProgram  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.products.v1.LoyaltyProgram;

Decodes a LoyaltyProgram message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.loyaltyprogram)` | LoyaltyProgram  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.products.v1.ILoyaltyProgram, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LoyaltyProgram message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iloyaltyprogram)`   
LoyaltyProgram message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.products.v1.ILoyaltyProgram, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LoyaltyProgram message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.iloyaltyprogram)`   
LoyaltyProgram message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.products.v1.LoyaltyProgram;

Creates a LoyaltyProgram message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.loyaltyprogram)` | LoyaltyProgram  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LoyaltyProgram

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

Converts this LoyaltyProgram to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.products.v1.LoyaltyProgram, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LoyaltyProgram message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.loyaltyprogram)`   
LoyaltyProgram  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LoyaltyProgram message.

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
