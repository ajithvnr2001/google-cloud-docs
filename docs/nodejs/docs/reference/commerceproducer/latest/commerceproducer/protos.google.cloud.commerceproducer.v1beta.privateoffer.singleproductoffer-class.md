---
url: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.singleproductoffer-class
title: Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer (0.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:32:08.396846+00:00
---

# Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer (0.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.singleproductoffer-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a SingleProductOffer.

## Implements

[protos.google.cloud.commerceproducer.v1beta.PrivateOffer.ISingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.isingleproductoffer)

## Package

[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.commerceproducer.v1beta.PrivateOffer.ISingleProductOffer);

Constructs a new SingleProductOffer.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.isingleproductoffer)`   
Properties to set  
  
## Properties 

### amendedOffer
    
    
    public amendedOffer?: ("amendedPrivateOffer"|"amendedStandardOffer");

SingleProductOffer amendedOffer.

### amendedPrivateOffer
    
    
    public amendedPrivateOffer?: (string|null);

SingleProductOffer amendedPrivateOffer.

### amendedStandardOffer
    
    
    public amendedStandardOffer?: (string|null);

SingleProductOffer amendedStandardOffer.

### baseStandardOffer
    
    
    public baseStandardOffer: string;

SingleProductOffer baseStandardOffer.

### contractValue
    
    
    public contractValue?: (google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer.IContractValue|null);

SingleProductOffer contractValue.

### customIntervalPrice
    
    
    public customIntervalPrice?: (google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer.ICustomIntervalPrice|null);

SingleProductOffer customIntervalPrice.

### effectiveInstallmentTimeline
    
    
    public effectiveInstallmentTimeline: google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer.IInstallment[];

SingleProductOffer effectiveInstallmentTimeline.

### features
    
    
    public features: google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer.IFeature[];

SingleProductOffer features.

### price
    
    
    public price?: ("standardIntervalPrice"|"customIntervalPrice");

SingleProductOffer price.

### resellerPrivateOfferPlanId
    
    
    public resellerPrivateOfferPlanId: string;

SingleProductOffer resellerPrivateOfferPlanId.

### revenueShare
    
    
    public revenueShare?: (google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer.IRevenueShare|null);

SingleProductOffer revenueShare.

### serviceLevel
    
    
    public serviceLevel: string;

SingleProductOffer serviceLevel.

### standardIntervalPrice
    
    
    public standardIntervalPrice?: (google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer.IStandardIntervalPrice|null);

SingleProductOffer standardIntervalPrice.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.commerceproducer.v1beta.PrivateOffer.ISingleProductOffer): google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer;

Creates a new SingleProductOffer instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.isingleproductoffer)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.singleproductoffer-class)` | SingleProductOffer instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer;

Decodes a SingleProductOffer message from the specified reader or buffer.

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
`[SingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.singleproductoffer-class)` | SingleProductOffer  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer;

Decodes a SingleProductOffer message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.singleproductoffer-class)` | SingleProductOffer  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.commerceproducer.v1beta.PrivateOffer.ISingleProductOffer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SingleProductOffer message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.isingleproductoffer)`   
SingleProductOffer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.commerceproducer.v1beta.PrivateOffer.ISingleProductOffer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SingleProductOffer message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.isingleproductoffer)`   
SingleProductOffer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer;

Creates a SingleProductOffer message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.singleproductoffer-class)` | SingleProductOffer  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SingleProductOffer

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

Converts this SingleProductOffer to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.commerceproducer.v1beta.PrivateOffer.SingleProductOffer, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SingleProductOffer message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SingleProductOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.singleproductoffer-class)`   
SingleProductOffer  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SingleProductOffer message.

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
