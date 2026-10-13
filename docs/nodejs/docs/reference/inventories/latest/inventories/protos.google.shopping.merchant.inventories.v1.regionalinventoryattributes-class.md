---
url: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryattributes-class
title: Class protos.google.shopping.merchant.inventories.v1.RegionalInventoryAttributes (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:13.620031+00:00
---

# Class protos.google.shopping.merchant.inventories.v1.RegionalInventoryAttributes (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryattributes-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.inventories.v1.RegionalInventoryAttributes (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.12.0  0.7.1  0.5.0  0.4.0 

Represents a RegionalInventoryAttributes.

## Implements

[protos.google.shopping.merchant.inventories.v1.IRegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iregionalinventoryattributes)

## Package

[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.inventories.v1.IRegionalInventoryAttributes);

Constructs a new RegionalInventoryAttributes.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iregionalinventoryattributes)`   
Properties to set  
  
## Properties 

### availability
    
    
    public availability?: (google.shopping.merchant.inventories.v1.RegionalInventoryAttributes.Availability|keyof typeof google.shopping.merchant.inventories.v1.RegionalInventoryAttributes.Availability|null);

RegionalInventoryAttributes availability.

### loyaltyPrograms
    
    
    public loyaltyPrograms: google.shopping.merchant.inventories.v1.IInventoryLoyaltyProgram[];

RegionalInventoryAttributes loyaltyPrograms.

### price
    
    
    public price?: (google.shopping.type.IPrice|null);

RegionalInventoryAttributes price.

### salePrice
    
    
    public salePrice?: (google.shopping.type.IPrice|null);

RegionalInventoryAttributes salePrice.

### salePriceEffectiveDate
    
    
    public salePriceEffectiveDate?: (google.type.IInterval|null);

RegionalInventoryAttributes salePriceEffectiveDate.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.inventories.v1.IRegionalInventoryAttributes): google.shopping.merchant.inventories.v1.RegionalInventoryAttributes;

Creates a new RegionalInventoryAttributes instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iregionalinventoryattributes)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryattributes-class)` | RegionalInventoryAttributes instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.inventories.v1.RegionalInventoryAttributes;

Decodes a RegionalInventoryAttributes message from the specified reader or buffer.

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
`[RegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryattributes-class)` | RegionalInventoryAttributes  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.inventories.v1.RegionalInventoryAttributes;

Decodes a RegionalInventoryAttributes message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryattributes-class)` | RegionalInventoryAttributes  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.inventories.v1.IRegionalInventoryAttributes, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RegionalInventoryAttributes message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iregionalinventoryattributes)`   
RegionalInventoryAttributes message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.inventories.v1.IRegionalInventoryAttributes, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RegionalInventoryAttributes message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.iregionalinventoryattributes)`   
RegionalInventoryAttributes message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.inventories.v1.RegionalInventoryAttributes;

Creates a RegionalInventoryAttributes message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryattributes-class)` | RegionalInventoryAttributes  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RegionalInventoryAttributes

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

Converts this RegionalInventoryAttributes to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.inventories.v1.RegionalInventoryAttributes, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RegionalInventoryAttributes message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RegionalInventoryAttributes](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1.regionalinventoryattributes-class)`   
RegionalInventoryAttributes  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RegionalInventoryAttributes message.

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
