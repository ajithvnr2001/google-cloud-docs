---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.cartdata
title: Class protos.google.ads.datamanager.v1.CartData (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:21.957180+00:00
---

# Class protos.google.ads.datamanager.v1.CartData (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.cartdata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.CartData (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents a CartData.

## Implements

[protos.google.ads.datamanager.v1.ICartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icartdata)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.ICartData);

Constructs a new CartData.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icartdata)`   
Properties to set  
  
## Properties 

### couponCodes
    
    
    public couponCodes: string[];

CartData couponCodes.

### items
    
    
    public items: google.ads.datamanager.v1.IItem[];

CartData items.

### merchantFeedLabel
    
    
    public merchantFeedLabel: string;

CartData merchantFeedLabel.

### merchantFeedLanguageCode
    
    
    public merchantFeedLanguageCode: string;

CartData merchantFeedLanguageCode.

### merchantId
    
    
    public merchantId: string;

CartData merchantId.

### transactionDiscount
    
    
    public transactionDiscount: number;

CartData transactionDiscount.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.ICartData): google.ads.datamanager.v1.CartData;

Creates a new CartData instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icartdata)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.cartdata)` | CartData instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.CartData;

Decodes a CartData message from the specified reader or buffer.

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
`[CartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.cartdata)` | CartData  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.CartData;

Decodes a CartData message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.cartdata)` | CartData  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.ICartData, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CartData message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icartdata)`   
CartData message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.ICartData, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CartData message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.icartdata)`   
CartData message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.CartData;

Creates a CartData message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.cartdata)` | CartData  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CartData

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

Converts this CartData to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.CartData, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CartData message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CartData](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.cartdata)`   
CartData  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CartData message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
