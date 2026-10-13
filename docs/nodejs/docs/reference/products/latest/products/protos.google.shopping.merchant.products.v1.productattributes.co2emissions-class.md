---
url: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.co2emissions-class
title: Class protos.google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:16.469002+00:00
---

# Class protos.google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.co2emissions-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.1.1 

Represents a Co2Emissions.

## Implements

[protos.google.shopping.merchant.products.v1.ProductAttributes.ICo2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.ico2emissions)

## Package

[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.products.v1.ProductAttributes.ICo2Emissions);

Constructs a new Co2Emissions.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICo2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.ico2emissions)`   
Properties to set  
  
## Properties 

### unit
    
    
    public unit: (google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions.Unit|keyof typeof google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions.Unit);

Co2Emissions unit.

### value
    
    
    public value?: (number|Long|string|null);

Co2Emissions value.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.products.v1.ProductAttributes.ICo2Emissions): google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions;

Creates a new Co2Emissions instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICo2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.ico2emissions)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Co2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.co2emissions-class)` | Co2Emissions instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions;

Decodes a Co2Emissions message from the specified reader or buffer.

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
`[Co2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.co2emissions-class)` | Co2Emissions  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions;

Decodes a Co2Emissions message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Co2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.co2emissions-class)` | Co2Emissions  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.products.v1.ProductAttributes.ICo2Emissions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Co2Emissions message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICo2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.ico2emissions)`   
Co2Emissions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.products.v1.ProductAttributes.ICo2Emissions, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Co2Emissions message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICo2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.ico2emissions)`   
Co2Emissions message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions;

Creates a Co2Emissions message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Co2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.co2emissions-class)` | Co2Emissions  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Co2Emissions

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

Converts this Co2Emissions to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.products.v1.ProductAttributes.Co2Emissions, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Co2Emissions message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Co2Emissions](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.productattributes.co2emissions-class)`   
Co2Emissions  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Co2Emissions message.

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
