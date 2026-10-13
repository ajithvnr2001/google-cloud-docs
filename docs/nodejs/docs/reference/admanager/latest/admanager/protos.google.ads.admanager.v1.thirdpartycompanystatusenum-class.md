---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.thirdpartycompanystatusenum-class
title: Class protos.google.ads.admanager.v1.ThirdPartyCompanyStatusEnum (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:14.037987+00:00
---

# Class protos.google.ads.admanager.v1.ThirdPartyCompanyStatusEnum (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.thirdpartycompanystatusenum-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.ThirdPartyCompanyStatusEnum (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents a ThirdPartyCompanyStatusEnum.

## Implements

[protos.google.ads.admanager.v1.IThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ithirdpartycompanystatusenum)

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.admanager.v1.IThirdPartyCompanyStatusEnum);

Constructs a new ThirdPartyCompanyStatusEnum.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ithirdpartycompanystatusenum)`   
Properties to set  
  
## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.admanager.v1.IThirdPartyCompanyStatusEnum): google.ads.admanager.v1.ThirdPartyCompanyStatusEnum;

Creates a new ThirdPartyCompanyStatusEnum instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ithirdpartycompanystatusenum)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.thirdpartycompanystatusenum-class)` | ThirdPartyCompanyStatusEnum instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.admanager.v1.ThirdPartyCompanyStatusEnum;

Decodes a ThirdPartyCompanyStatusEnum message from the specified reader or buffer.

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
`[ThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.thirdpartycompanystatusenum-class)` | ThirdPartyCompanyStatusEnum  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.admanager.v1.ThirdPartyCompanyStatusEnum;

Decodes a ThirdPartyCompanyStatusEnum message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.thirdpartycompanystatusenum-class)` | ThirdPartyCompanyStatusEnum  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.admanager.v1.IThirdPartyCompanyStatusEnum, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ThirdPartyCompanyStatusEnum message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ithirdpartycompanystatusenum)`   
ThirdPartyCompanyStatusEnum message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.admanager.v1.IThirdPartyCompanyStatusEnum, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ThirdPartyCompanyStatusEnum message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ithirdpartycompanystatusenum)`   
ThirdPartyCompanyStatusEnum message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.admanager.v1.ThirdPartyCompanyStatusEnum;

Creates a ThirdPartyCompanyStatusEnum message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.thirdpartycompanystatusenum-class)` | ThirdPartyCompanyStatusEnum  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ThirdPartyCompanyStatusEnum

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

Converts this ThirdPartyCompanyStatusEnum to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.admanager.v1.ThirdPartyCompanyStatusEnum, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ThirdPartyCompanyStatusEnum message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ThirdPartyCompanyStatusEnum](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.thirdpartycompanystatusenum-class)`   
ThirdPartyCompanyStatusEnum  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ThirdPartyCompanyStatusEnum message.

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
