---
url: https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.product
title: Class protos.google.cloud.privatecatalog.v1beta1.Product (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:55.367057+00:00
---

# Class protos.google.cloud.privatecatalog.v1beta1.Product (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.product

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.privatecatalog.v1beta1.Product (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  2.1.2  2.0.4  1.1.1  1.0.4 

Represents a Product.

## Implements

[protos.google.cloud.privatecatalog.v1beta1.IProduct](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.iproduct)

## Package

[@google-cloud/private-catalog](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.privatecatalog.v1beta1.IProduct);

Constructs a new Product.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IProduct](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.iproduct)`   
Properties to set  
  
## Properties 

### assetReferences
    
    
    public assetReferences: google.cloud.privatecatalog.v1beta1.IAssetReference[];

Product assetReferences.

### assetType
    
    
    public assetType: string;

Product assetType.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Product createTime.

### displayMetadata
    
    
    public displayMetadata?: (google.protobuf.IStruct|null);

Product displayMetadata.

### iconUri
    
    
    public iconUri: string;

Product iconUri.

### name
    
    
    public name: string;

Product name.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Product updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.privatecatalog.v1beta1.IProduct): google.cloud.privatecatalog.v1beta1.Product;

Creates a new Product instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IProduct](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.iproduct)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.product)` | Product instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.privatecatalog.v1beta1.Product;

Decodes a Product message from the specified reader or buffer.

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
`[Product](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.product)` | Product  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.privatecatalog.v1beta1.Product;

Decodes a Product message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.product)` | Product  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.privatecatalog.v1beta1.IProduct, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Product message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IProduct](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.iproduct)`   
Product message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.privatecatalog.v1beta1.IProduct, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Product message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IProduct](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.iproduct)`   
Product message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.privatecatalog.v1beta1.Product;

Creates a Product message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.product)` | Product  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Product

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

Converts this Product to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.privatecatalog.v1beta1.Product, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Product message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Product](https://docs.cloud.google.com/nodejs/docs/reference/private-catalog/latest/private-catalog/protos.google.cloud.privatecatalog.v1beta1.product)`   
Product  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Product message.

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
