---
url: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory
title: Class protos.google.shopping.merchant.inventories.v1beta.LocalInventory (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:15.718178+00:00
---

# Class protos.google.shopping.merchant.inventories.v1beta.LocalInventory (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.inventories.v1beta.LocalInventory (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.12.0  0.7.1  0.5.0  0.4.0 

Represents a LocalInventory.

## Implements

[protos.google.shopping.merchant.inventories.v1beta.ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)

## Package

[@google-shopping/inventories](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.inventories.v1beta.ILocalInventory);

Constructs a new LocalInventory.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)`   
Properties to set  
  
## Properties 

### account
    
    
    public account: (number|Long|string);

LocalInventory account.

### availability
    
    
    public availability?: (string|null);

LocalInventory availability.

### customAttributes
    
    
    public customAttributes: google.shopping.type.ICustomAttribute[];

LocalInventory customAttributes.

### instoreProductLocation
    
    
    public instoreProductLocation?: (string|null);

LocalInventory instoreProductLocation.

### name
    
    
    public name: string;

LocalInventory name.

### pickupMethod
    
    
    public pickupMethod?: (string|null);

LocalInventory pickupMethod.

### pickupSla
    
    
    public pickupSla?: (string|null);

LocalInventory pickupSla.

### price
    
    
    public price?: (google.shopping.type.IPrice|null);

LocalInventory price.

### quantity
    
    
    public quantity?: (number|Long|string|null);

LocalInventory quantity.

### salePrice
    
    
    public salePrice?: (google.shopping.type.IPrice|null);

LocalInventory salePrice.

### salePriceEffectiveDate
    
    
    public salePriceEffectiveDate?: (google.type.IInterval|null);

LocalInventory salePriceEffectiveDate.

### storeCode
    
    
    public storeCode: string;

LocalInventory storeCode.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.inventories.v1beta.ILocalInventory): google.shopping.merchant.inventories.v1beta.LocalInventory;

Creates a new LocalInventory instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory)` | LocalInventory instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.inventories.v1beta.LocalInventory;

Decodes a LocalInventory message from the specified reader or buffer.

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
`[LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory)` | LocalInventory  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.inventories.v1beta.LocalInventory;

Decodes a LocalInventory message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory)` | LocalInventory  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.inventories.v1beta.ILocalInventory, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LocalInventory message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)`   
LocalInventory message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.inventories.v1beta.ILocalInventory, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified LocalInventory message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ILocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.ilocalinventory)`   
LocalInventory message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.inventories.v1beta.LocalInventory;

Creates a LocalInventory message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory)` | LocalInventory  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for LocalInventory

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

Converts this LocalInventory to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.inventories.v1beta.LocalInventory, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a LocalInventory message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[LocalInventory](https://docs.cloud.google.com/nodejs/docs/reference/inventories/latest/inventories/protos.google.shopping.merchant.inventories.v1beta.localinventory)`   
LocalInventory  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a LocalInventory message.

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
