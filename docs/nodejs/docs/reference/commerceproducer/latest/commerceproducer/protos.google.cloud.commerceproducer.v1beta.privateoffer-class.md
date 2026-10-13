---
url: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class
title: Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer (0.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:32:05.754846+00:00
---

# Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer (0.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a PrivateOffer.

## Implements

[protos.google.cloud.commerceproducer.v1beta.IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)

## Package

[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.commerceproducer.v1beta.IPrivateOffer);

Constructs a new PrivateOffer.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)`   
Properties to set  
  
## Properties 

### acceptDeadlineTime
    
    
    public acceptDeadlineTime?: (google.type.IDateTime|null);

PrivateOffer acceptDeadlineTime.

### acceptTime
    
    
    public acceptTime?: (google.protobuf.ITimestamp|null);

PrivateOffer acceptTime.

### cancellationNote
    
    
    public cancellationNote: string;

PrivateOffer cancellationNote.

### cancelTime
    
    
    public cancelTime?: (google.protobuf.ITimestamp|null);

PrivateOffer cancelTime.

### content
    
    
    public content?: "singleProductOffer";

PrivateOffer content.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

PrivateOffer createTime.

### customer
    
    
    public customer?: (google.cloud.commerceproducer.v1beta.PrivateOffer.ICustomer|null);

PrivateOffer customer.

### customerNote
    
    
    public customerNote: string;

PrivateOffer customerNote.

### endTime
    
    
    public endTime?: (google.protobuf.ITimestamp|null);

PrivateOffer endTime.

### internalNote
    
    
    public internalNote: string;

PrivateOffer internalNote.

### name
    
    
    public name: string;

PrivateOffer name.

### offerDealType
    
    
    public offerDealType: (google.cloud.commerceproducer.v1beta.PrivateOffer.OfferDealType|keyof typeof google.cloud.commerceproducer.v1beta.PrivateOffer.OfferDealType);

PrivateOffer offerDealType.

### partnerContact
    
    
    public partnerContact?: (google.cloud.commerceproducer.v1beta.PrivateOffer.IPartnerContact|null);

PrivateOffer partnerContact.

### publishRequirementGoogleReview
    
    
    public publishRequirementGoogleReview?: (google.cloud.commerceproducer.v1beta.PrivateOffer.IPublishRequirementGoogleReview|null);

PrivateOffer publishRequirementGoogleReview.

### publishTime
    
    
    public publishTime?: (google.protobuf.ITimestamp|null);

PrivateOffer publishTime.

### resellerContact
    
    
    public resellerContact?: (google.cloud.commerceproducer.v1beta.PrivateOffer.IResellerContact|null);

PrivateOffer resellerContact.

### singleProductOffer
    
    
    public singleProductOffer?: (google.cloud.commerceproducer.v1beta.PrivateOffer.ISingleProductOffer|null);

PrivateOffer singleProductOffer.

### state
    
    
    public state: (google.cloud.commerceproducer.v1beta.PrivateOffer.State|keyof typeof google.cloud.commerceproducer.v1beta.PrivateOffer.State);

PrivateOffer state.

### term
    
    
    public term?: (google.cloud.commerceproducer.v1beta.PrivateOffer.ITerm|null);

PrivateOffer term.

### title
    
    
    public title: string;

PrivateOffer title.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

PrivateOffer updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.commerceproducer.v1beta.IPrivateOffer): google.cloud.commerceproducer.v1beta.PrivateOffer;

Creates a new PrivateOffer instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)` | PrivateOffer instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.commerceproducer.v1beta.PrivateOffer;

Decodes a PrivateOffer message from the specified reader or buffer.

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
`[PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)` | PrivateOffer  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.commerceproducer.v1beta.PrivateOffer;

Decodes a PrivateOffer message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)` | PrivateOffer  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.commerceproducer.v1beta.IPrivateOffer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PrivateOffer message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)`   
PrivateOffer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.commerceproducer.v1beta.IPrivateOffer, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PrivateOffer message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.iprivateoffer)`   
PrivateOffer message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.commerceproducer.v1beta.PrivateOffer;

Creates a PrivateOffer message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)` | PrivateOffer  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PrivateOffer

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

Converts this PrivateOffer to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.commerceproducer.v1beta.PrivateOffer, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PrivateOffer message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PrivateOffer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer-class)`   
PrivateOffer  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PrivateOffer message.

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
