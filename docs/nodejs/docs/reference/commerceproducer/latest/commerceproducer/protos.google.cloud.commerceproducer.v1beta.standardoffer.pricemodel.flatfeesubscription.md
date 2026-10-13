---
url: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.flatfeesubscription
title: Class protos.google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.FlatFeeSubscription (0.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:32:00.512990+00:00
---

# Class protos.google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.FlatFeeSubscription (0.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.flatfeesubscription

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.FlatFeeSubscription (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a FlatFeeSubscription.

## Implements

[protos.google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.IFlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.iflatfeesubscription)

## Package

[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.IFlatFeeSubscription);

Constructs a new FlatFeeSubscription.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.iflatfeesubscription)`   
Properties to set  
  
## Properties 

### sku
    
    
    public sku: string;

FlatFeeSubscription sku.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.IFlatFeeSubscription): google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.FlatFeeSubscription;

Creates a new FlatFeeSubscription instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IFlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.iflatfeesubscription)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[FlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.flatfeesubscription)` | FlatFeeSubscription instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.FlatFeeSubscription;

Decodes a FlatFeeSubscription message from the specified reader or buffer.

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
`[FlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.flatfeesubscription)` | FlatFeeSubscription  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.FlatFeeSubscription;

Decodes a FlatFeeSubscription message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[FlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.flatfeesubscription)` | FlatFeeSubscription  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.IFlatFeeSubscription, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FlatFeeSubscription message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.iflatfeesubscription)`   
FlatFeeSubscription message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.IFlatFeeSubscription, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified FlatFeeSubscription message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IFlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.iflatfeesubscription)`   
FlatFeeSubscription message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.FlatFeeSubscription;

Creates a FlatFeeSubscription message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[FlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.flatfeesubscription)` | FlatFeeSubscription  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for FlatFeeSubscription

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

Converts this FlatFeeSubscription to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.commerceproducer.v1beta.StandardOffer.PriceModel.FlatFeeSubscription, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a FlatFeeSubscription message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[FlatFeeSubscription](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.standardoffer.pricemodel.flatfeesubscription)`   
FlatFeeSubscription  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a FlatFeeSubscription message.

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

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
