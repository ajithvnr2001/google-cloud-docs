---
url: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.partnercontact
title: Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer.PartnerContact (0.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:32:04.668413+00:00
---

# Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer.PartnerContact (0.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.partnercontact

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.commerceproducer.v1beta.PrivateOffer.PartnerContact (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a PartnerContact.

## Implements

[protos.google.cloud.commerceproducer.v1beta.PrivateOffer.IPartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.ipartnercontact)

## Package

[@google-cloud/commerceproducer](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.commerceproducer.v1beta.PrivateOffer.IPartnerContact);

Constructs a new PartnerContact.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.ipartnercontact)`   
Properties to set  
  
## Properties 

### contact
    
    
    public contact: string;

PartnerContact contact.

### email
    
    
    public email: string;

PartnerContact email.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.commerceproducer.v1beta.PrivateOffer.IPartnerContact): google.cloud.commerceproducer.v1beta.PrivateOffer.PartnerContact;

Creates a new PartnerContact instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.ipartnercontact)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.partnercontact)` | PartnerContact instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.commerceproducer.v1beta.PrivateOffer.PartnerContact;

Decodes a PartnerContact message from the specified reader or buffer.

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
`[PartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.partnercontact)` | PartnerContact  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.commerceproducer.v1beta.PrivateOffer.PartnerContact;

Decodes a PartnerContact message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.partnercontact)` | PartnerContact  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.commerceproducer.v1beta.PrivateOffer.IPartnerContact, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PartnerContact message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.ipartnercontact)`   
PartnerContact message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.commerceproducer.v1beta.PrivateOffer.IPartnerContact, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PartnerContact message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.ipartnercontact)`   
PartnerContact message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.commerceproducer.v1beta.PrivateOffer.PartnerContact;

Creates a PartnerContact message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.partnercontact)` | PartnerContact  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PartnerContact

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

Converts this PartnerContact to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.commerceproducer.v1beta.PrivateOffer.PartnerContact, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PartnerContact message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PartnerContact](https://docs.cloud.google.com/nodejs/docs/reference/commerceproducer/latest/commerceproducer/protos.google.cloud.commerceproducer.v1beta.privateoffer.partnercontact)`   
PartnerContact  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PartnerContact message.

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
