---
url: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableoffersrequest-class
title: Class protos.google.cloud.channel.v1.ListPurchasableOffersRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:26.943264+00:00
---

# Class protos.google.cloud.channel.v1.ListPurchasableOffersRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableoffersrequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.channel.v1.ListPurchasableOffersRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.2  3.6.0  3.2.1  3.0.0  2.5.1  2.4.1  2.2.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6 

Represents a ListPurchasableOffersRequest.

## Implements

[protos.google.cloud.channel.v1.IListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableoffersrequest)

## Package

[@google-cloud/channel](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.channel.v1.IListPurchasableOffersRequest);

Constructs a new ListPurchasableOffersRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableoffersrequest)`   
Properties to set  
  
## Properties 

### changeOfferPurchase
    
    
    public changeOfferPurchase?: (google.cloud.channel.v1.ListPurchasableOffersRequest.IChangeOfferPurchase|null);

ListPurchasableOffersRequest changeOfferPurchase.

### createEntitlementPurchase
    
    
    public createEntitlementPurchase?: (google.cloud.channel.v1.ListPurchasableOffersRequest.ICreateEntitlementPurchase|null);

ListPurchasableOffersRequest createEntitlementPurchase.

### customer
    
    
    public customer: string;

ListPurchasableOffersRequest customer.

### languageCode
    
    
    public languageCode: string;

ListPurchasableOffersRequest languageCode.

### pageSize
    
    
    public pageSize: number;

ListPurchasableOffersRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListPurchasableOffersRequest pageToken.

### purchaseOption
    
    
    public purchaseOption?: ("createEntitlementPurchase"|"changeOfferPurchase");

ListPurchasableOffersRequest purchaseOption.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.channel.v1.IListPurchasableOffersRequest): google.cloud.channel.v1.ListPurchasableOffersRequest;

Creates a new ListPurchasableOffersRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableoffersrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableoffersrequest-class)` | ListPurchasableOffersRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.channel.v1.ListPurchasableOffersRequest;

Decodes a ListPurchasableOffersRequest message from the specified reader or buffer.

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
`[ListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableoffersrequest-class)` | ListPurchasableOffersRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.channel.v1.ListPurchasableOffersRequest;

Decodes a ListPurchasableOffersRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableoffersrequest-class)` | ListPurchasableOffersRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.channel.v1.IListPurchasableOffersRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListPurchasableOffersRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableoffersrequest)`   
ListPurchasableOffersRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.channel.v1.IListPurchasableOffersRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListPurchasableOffersRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistpurchasableoffersrequest)`   
ListPurchasableOffersRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.channel.v1.ListPurchasableOffersRequest;

Creates a ListPurchasableOffersRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableoffersrequest-class)` | ListPurchasableOffersRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListPurchasableOffersRequest

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

Converts this ListPurchasableOffersRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.channel.v1.ListPurchasableOffersRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListPurchasableOffersRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListPurchasableOffersRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listpurchasableoffersrequest-class)`   
ListPurchasableOffersRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListPurchasableOffersRequest message.

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
