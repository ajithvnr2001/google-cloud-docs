---
url: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.shipping
title: Class protos.google.shopping.merchant.products.v1.Shipping (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:23.212886+00:00
---

# Class protos.google.shopping.merchant.products.v1.Shipping (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.shipping

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.products.v1.Shipping (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.1.1 

Represents a Shipping.

## Implements

[protos.google.shopping.merchant.products.v1.IShipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ishipping)

## Package

[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.products.v1.IShipping);

Constructs a new Shipping.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IShipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ishipping)`   
Properties to set  
  
## Properties 

### country
    
    
    public country: string;

Shipping country.

### handlingCutoffTime
    
    
    public handlingCutoffTime?: (string|null);

Shipping handlingCutoffTime.

### handlingCutoffTimezone
    
    
    public handlingCutoffTimezone?: (string|null);

Shipping handlingCutoffTimezone.

### locationGroupName
    
    
    public locationGroupName: string;

Shipping locationGroupName.

### locationId
    
    
    public locationId: (number|Long|string);

Shipping locationId.

### loyaltyProgramLabel
    
    
    public loyaltyProgramLabel: string;

Shipping loyaltyProgramLabel.

### loyaltyTierLabel
    
    
    public loyaltyTierLabel: string;

Shipping loyaltyTierLabel.

### maxHandlingTime
    
    
    public maxHandlingTime?: (number|Long|string|null);

Shipping maxHandlingTime.

### maxTransitTime
    
    
    public maxTransitTime?: (number|Long|string|null);

Shipping maxTransitTime.

### minHandlingTime
    
    
    public minHandlingTime?: (number|Long|string|null);

Shipping minHandlingTime.

### minTransitTime
    
    
    public minTransitTime?: (number|Long|string|null);

Shipping minTransitTime.

### postalCode
    
    
    public postalCode: string;

Shipping postalCode.

### price
    
    
    public price?: (google.shopping.type.IPrice|null);

Shipping price.

### region
    
    
    public region: string;

Shipping region.

### service
    
    
    public service: string;

Shipping service.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.products.v1.IShipping): google.shopping.merchant.products.v1.Shipping;

Creates a new Shipping instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IShipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ishipping)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Shipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.shipping)` | Shipping instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.products.v1.Shipping;

Decodes a Shipping message from the specified reader or buffer.

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
`[Shipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.shipping)` | Shipping  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.products.v1.Shipping;

Decodes a Shipping message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Shipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.shipping)` | Shipping  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.products.v1.IShipping, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Shipping message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IShipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ishipping)`   
Shipping message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.products.v1.IShipping, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Shipping message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IShipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ishipping)`   
Shipping message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.products.v1.Shipping;

Creates a Shipping message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Shipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.shipping)` | Shipping  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Shipping

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

Converts this Shipping to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.products.v1.Shipping, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Shipping message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Shipping](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.shipping)`   
Shipping  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Shipping message.

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
