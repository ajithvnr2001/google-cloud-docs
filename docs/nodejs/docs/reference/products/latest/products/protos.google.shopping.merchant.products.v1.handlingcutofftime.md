---
url: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.handlingcutofftime
title: Class protos.google.shopping.merchant.products.v1.HandlingCutoffTime (0.11.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:18.161101+00:00
---

# Class protos.google.shopping.merchant.products.v1.HandlingCutoffTime (0.11.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.handlingcutofftime

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.products.v1.HandlingCutoffTime (0.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.1 (latest)  0.1.1 

Represents a HandlingCutoffTime.

## Implements

[protos.google.shopping.merchant.products.v1.IHandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ihandlingcutofftime)

## Package

[@google-shopping/products](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.shopping.merchant.products.v1.IHandlingCutoffTime);

Constructs a new HandlingCutoffTime.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ihandlingcutofftime)`   
Properties to set  
  
## Properties 

### country
    
    
    public country?: (string|null);

HandlingCutoffTime country.

### cutoffTime
    
    
    public cutoffTime?: (string|null);

HandlingCutoffTime cutoffTime.

### cutoffTimezone
    
    
    public cutoffTimezone?: (string|null);

HandlingCutoffTime cutoffTimezone.

### disableDeliveryAfterCutoff
    
    
    public disableDeliveryAfterCutoff?: (boolean|null);

HandlingCutoffTime disableDeliveryAfterCutoff.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.shopping.merchant.products.v1.IHandlingCutoffTime): google.shopping.merchant.products.v1.HandlingCutoffTime;

Creates a new HandlingCutoffTime instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IHandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ihandlingcutofftime)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[HandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.handlingcutofftime)` | HandlingCutoffTime instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.shopping.merchant.products.v1.HandlingCutoffTime;

Decodes a HandlingCutoffTime message from the specified reader or buffer.

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
`[HandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.handlingcutofftime)` | HandlingCutoffTime  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.shopping.merchant.products.v1.HandlingCutoffTime;

Decodes a HandlingCutoffTime message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[HandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.handlingcutofftime)` | HandlingCutoffTime  
  
### encode(message, writer)
    
    
    public static encode(message: google.shopping.merchant.products.v1.IHandlingCutoffTime, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HandlingCutoffTime message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ihandlingcutofftime)`   
HandlingCutoffTime message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.shopping.merchant.products.v1.IHandlingCutoffTime, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified HandlingCutoffTime message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IHandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.ihandlingcutofftime)`   
HandlingCutoffTime message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.shopping.merchant.products.v1.HandlingCutoffTime;

Creates a HandlingCutoffTime message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[HandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.handlingcutofftime)` | HandlingCutoffTime  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for HandlingCutoffTime

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

Converts this HandlingCutoffTime to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.shopping.merchant.products.v1.HandlingCutoffTime, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a HandlingCutoffTime message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[HandlingCutoffTime](https://docs.cloud.google.com/nodejs/docs/reference/products/latest/products/protos.google.shopping.merchant.products.v1.handlingcutofftime)`   
HandlingCutoffTime  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a HandlingCutoffTime message.

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
