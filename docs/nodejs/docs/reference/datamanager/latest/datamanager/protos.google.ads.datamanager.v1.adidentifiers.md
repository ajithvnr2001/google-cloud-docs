---
url: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adidentifiers
title: Class protos.google.ads.datamanager.v1.AdIdentifiers (1.1.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:20.563743+00:00
---

# Class protos.google.ads.datamanager.v1.AdIdentifiers (1.1.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adidentifiers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.datamanager.v1.AdIdentifiers (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0  0.5.0  0.4.0  0.3.0  0.1.0 

Represents an AdIdentifiers.

## Implements

[protos.google.ads.datamanager.v1.IAdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadidentifiers)

## Package

[@google-ads/datamanager](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.datamanager.v1.IAdIdentifiers);

Constructs a new AdIdentifiers.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadidentifiers)`   
Properties to set  
  
## Properties 

### dclid
    
    
    public dclid: string;

AdIdentifiers dclid.

### encryptedUserIds
    
    
    public encryptedUserIds: google.ads.datamanager.v1.IEncryptedUserId[];

AdIdentifiers encryptedUserIds.

### gbraid
    
    
    public gbraid: string;

AdIdentifiers gbraid.

### gclid
    
    
    public gclid: string;

AdIdentifiers gclid.

### impressionId
    
    
    public impressionId: string;

AdIdentifiers impressionId.

### landingPageDeviceInfo
    
    
    public landingPageDeviceInfo?: (google.ads.datamanager.v1.IDeviceInfo|null);

AdIdentifiers landingPageDeviceInfo.

### matchId
    
    
    public matchId: string;

AdIdentifiers matchId.

### mobileDeviceId
    
    
    public mobileDeviceId: string;

AdIdentifiers mobileDeviceId.

### sessionAttributes
    
    
    public sessionAttributes: string;

AdIdentifiers sessionAttributes.

### wbraid
    
    
    public wbraid: string;

AdIdentifiers wbraid.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.datamanager.v1.IAdIdentifiers): google.ads.datamanager.v1.AdIdentifiers;

Creates a new AdIdentifiers instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadidentifiers)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adidentifiers)` | AdIdentifiers instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.datamanager.v1.AdIdentifiers;

Decodes an AdIdentifiers message from the specified reader or buffer.

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
`[AdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adidentifiers)` | AdIdentifiers  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.datamanager.v1.AdIdentifiers;

Decodes an AdIdentifiers message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adidentifiers)` | AdIdentifiers  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.datamanager.v1.IAdIdentifiers, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdIdentifiers message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadidentifiers)`   
AdIdentifiers message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.datamanager.v1.IAdIdentifiers, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdIdentifiers message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.iadidentifiers)`   
AdIdentifiers message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.datamanager.v1.AdIdentifiers;

Creates an AdIdentifiers message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adidentifiers)` | AdIdentifiers  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AdIdentifiers

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

Converts this AdIdentifiers to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.datamanager.v1.AdIdentifiers, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AdIdentifiers message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AdIdentifiers](https://docs.cloud.google.com/nodejs/docs/reference/datamanager/latest/datamanager/protos.google.ads.datamanager.v1.adidentifiers)`   
AdIdentifiers  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AdIdentifiers message.

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
