---
url: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.postaladdress
title: Class protos.google.type.PostalAddress (0.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:44.409637+00:00
---

# Class protos.google.type.PostalAddress (0.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.postaladdress

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.type.PostalAddress (0.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a PostalAddress.

## Implements

[protos.google.type.IPostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.ipostaladdress)

## Package

[@google-cloud/geocode](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.type.IPostalAddress);

Constructs a new PostalAddress.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.ipostaladdress)`   
Properties to set  
  
## Properties 

### addressLines
    
    
    public addressLines: string[];

PostalAddress addressLines.

### administrativeArea
    
    
    public administrativeArea: string;

PostalAddress administrativeArea.

### languageCode
    
    
    public languageCode: string;

PostalAddress languageCode.

### locality
    
    
    public locality: string;

PostalAddress locality.

### organization
    
    
    public organization: string;

PostalAddress organization.

### postalCode
    
    
    public postalCode: string;

PostalAddress postalCode.

### recipients
    
    
    public recipients: string[];

PostalAddress recipients.

### regionCode
    
    
    public regionCode: string;

PostalAddress regionCode.

### revision
    
    
    public revision: number;

PostalAddress revision.

### sortingCode
    
    
    public sortingCode: string;

PostalAddress sortingCode.

### sublocality
    
    
    public sublocality: string;

PostalAddress sublocality.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.type.IPostalAddress): google.type.PostalAddress;

Creates a new PostalAddress instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.ipostaladdress)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.postaladdress)` | PostalAddress instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.type.PostalAddress;

Decodes a PostalAddress message from the specified reader or buffer.

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
`[PostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.postaladdress)` | PostalAddress  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.type.PostalAddress;

Decodes a PostalAddress message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.postaladdress)` | PostalAddress  
  
### encode(message, writer)
    
    
    public static encode(message: google.type.IPostalAddress, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PostalAddress message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.ipostaladdress)`   
PostalAddress message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.type.IPostalAddress, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PostalAddress message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.ipostaladdress)`   
PostalAddress message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.type.PostalAddress;

Creates a PostalAddress message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.postaladdress)` | PostalAddress  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PostalAddress

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

Converts this PostalAddress to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.type.PostalAddress, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PostalAddress message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PostalAddress](https://docs.cloud.google.com/nodejs/docs/reference/geocode/latest/geocode/protos.google.type.postaladdress)`   
PostalAddress  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PostalAddress message.

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
