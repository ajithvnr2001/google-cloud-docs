---
url: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.inventoryloyaltyprogram
title: Class protos.google.shopping.merchant.inventories.v1.InventoryLoyaltyProgram (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:12.048090+00:00
---

# Class protos.google.shopping.merchant.inventories.v1.InventoryLoyaltyProgram (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.inventoryloyaltyprogram

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.inventories.v1.InventoryLoyaltyProgram (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.12.0  0.7.1  0.5.0  0.4.0 

Represents an InventoryLoyaltyProgram.

## Implements

[protos.google.shopping.merchant.inventories.v1.IInventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinventoryloyaltyprogram)

## Package

[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.inventories.v1.IInventoryLoyaltyProgram);

Constructs a new InventoryLoyaltyProgram.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinventoryloyaltyprogram)`   
Properties to set  
  
## Properties 

### cashbackForFutureUse
    
    
    public cashbackForFutureUse?: (google.shopping.type.IPrice|null);

InventoryLoyaltyProgram cashbackForFutureUse.

### loyaltyPoints
    
    
    public loyaltyPoints?: (number|Long|string|null);

InventoryLoyaltyProgram loyaltyPoints.

### memberPriceEffectiveInterval
    
    
    public memberPriceEffectiveInterval?: (google.type.IInterval|null);

InventoryLoyaltyProgram memberPriceEffectiveInterval.

### price
    
    
    public price?: (google.shopping.type.IPrice|null);

InventoryLoyaltyProgram price.

### programLabel
    
    
    public programLabel?: (string|null);

InventoryLoyaltyProgram programLabel.

### shippingLabel
    
    
    public shippingLabel?: (string|null);

InventoryLoyaltyProgram shippingLabel.

### tierLabel
    
    
    public tierLabel?: (string|null);

InventoryLoyaltyProgram tierLabel.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.inventories.v1.IInventoryLoyaltyProgram): google.shopping.merchant.inventories.v1.InventoryLoyaltyProgram;

Creates a new InventoryLoyaltyProgram instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IInventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinventoryloyaltyprogram)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[InventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.inventoryloyaltyprogram)` | InventoryLoyaltyProgram instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.inventories.v1.InventoryLoyaltyProgram;

Decodes an InventoryLoyaltyProgram message from the specified reader or buffer.

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
`[InventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.inventoryloyaltyprogram)` | InventoryLoyaltyProgram  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.inventories.v1.InventoryLoyaltyProgram;

Decodes an InventoryLoyaltyProgram message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[InventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.inventoryloyaltyprogram)` | InventoryLoyaltyProgram  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.inventories.v1.IInventoryLoyaltyProgram, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InventoryLoyaltyProgram message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinventoryloyaltyprogram)`   
InventoryLoyaltyProgram message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.inventories.v1.IInventoryLoyaltyProgram, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified InventoryLoyaltyProgram message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IInventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iinventoryloyaltyprogram)`   
InventoryLoyaltyProgram message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.inventories.v1.InventoryLoyaltyProgram;

Creates an InventoryLoyaltyProgram message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[InventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.inventoryloyaltyprogram)` | InventoryLoyaltyProgram  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for InventoryLoyaltyProgram

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

Converts this InventoryLoyaltyProgram to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.inventories.v1.InventoryLoyaltyProgram, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an InventoryLoyaltyProgram message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[InventoryLoyaltyProgram](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.inventoryloyaltyprogram)`   
InventoryLoyaltyProgram  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an InventoryLoyaltyProgram message.

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
