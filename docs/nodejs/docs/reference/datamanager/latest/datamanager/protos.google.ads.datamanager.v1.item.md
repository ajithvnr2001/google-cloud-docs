---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.item
title: Class protos.google.ads.datamanager.v1.Item (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:08.385912+00:00
---

# Class protos.google.ads.datamanager.v1.Item (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.item

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.Item (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents an Item.

## Implements

[protos.google.ads.datamanager.v1.IItem](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iitem)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.IItem);

Constructs a new Item.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IItem](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iitem)`   
Properties to set  
  
## Properties 

### additionalItemParameters
    
    
    public additionalItemParameters: google.ads.datamanager.v1.IItemParameter[];

Item additionalItemParameters.

### conversionValue
    
    
    public conversionValue?: (number|null);

Item conversionValue.

### customVariables
    
    
    public customVariables: google.ads.datamanager.v1.IItemCustomVariable[];

Item customVariables.

### itemId
    
    
    public itemId: string;

Item itemId.

### merchantFeedLabel
    
    
    public merchantFeedLabel: string;

Item merchantFeedLabel.

### merchantFeedLanguageCode
    
    
    public merchantFeedLanguageCode: string;

Item merchantFeedLanguageCode.

### merchantId
    
    
    public merchantId: string;

Item merchantId.

### merchantProductId
    
    
    public merchantProductId: string;

Item merchantProductId.

### quantity
    
    
    public quantity: (number|Long|string);

Item quantity.

### unitPrice
    
    
    public unitPrice: number;

Item unitPrice.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.IItem): google.ads.datamanager.v1.Item;

Creates a new Item instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IItem](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iitem)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Item](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.item)` | Item instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.Item;

Decodes an Item message from the specified reader or buffer.

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
`[Item](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.item)` | Item  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.Item;

Decodes an Item message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Item](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.item)` | Item  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.IItem, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Item message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IItem](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iitem)`   
Item message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.IItem, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Item message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IItem](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iitem)`   
Item message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.Item;

Creates an Item message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Item](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.item)` | Item  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Item

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

Converts this Item to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.Item, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Item message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Item](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.item)`   
Item  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Item message.

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
