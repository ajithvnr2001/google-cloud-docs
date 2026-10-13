---
url: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cryptoreplaceffxfpeconfig-class
title: Class protos.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:21.633820+00:00
---

# Class protos.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cryptoreplaceffxfpeconfig-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.6.0  6.2.0  6.1.0  5.13.0  5.11.0  5.10.0  5.7.0  5.5.0  5.3.0  5.0.0  4.4.2  4.2.0  4.1.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.8 

Represents a CryptoReplaceFfxFpeConfig.

## Implements

[protos.google.privacy.dlp.v2.ICryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.icryptoreplaceffxfpeconfig)

## Package

[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.privacy.dlp.v2.ICryptoReplaceFfxFpeConfig);

Constructs a new CryptoReplaceFfxFpeConfig.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.icryptoreplaceffxfpeconfig)`   
Properties to set  
  
## Properties 

### alphabet
    
    
    public alphabet?: ("commonAlphabet"|"customAlphabet"|"radix");

CryptoReplaceFfxFpeConfig alphabet.

### commonAlphabet
    
    
    public commonAlphabet?: (google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet|keyof typeof google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet|null);

CryptoReplaceFfxFpeConfig commonAlphabet.

### context
    
    
    public context?: (google.privacy.dlp.v2.IFieldId|null);

CryptoReplaceFfxFpeConfig context.

### cryptoKey
    
    
    public cryptoKey?: (google.privacy.dlp.v2.ICryptoKey|null);

CryptoReplaceFfxFpeConfig cryptoKey.

### customAlphabet
    
    
    public customAlphabet?: (string|null);

CryptoReplaceFfxFpeConfig customAlphabet.

### radix
    
    
    public radix?: (number|null);

CryptoReplaceFfxFpeConfig radix.

### surrogateInfoType
    
    
    public surrogateInfoType?: (google.privacy.dlp.v2.IInfoType|null);

CryptoReplaceFfxFpeConfig surrogateInfoType.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.privacy.dlp.v2.ICryptoReplaceFfxFpeConfig): google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig;

Creates a new CryptoReplaceFfxFpeConfig instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.icryptoreplaceffxfpeconfig)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cryptoreplaceffxfpeconfig-class)` | CryptoReplaceFfxFpeConfig instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig;

Decodes a CryptoReplaceFfxFpeConfig message from the specified reader or buffer.

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
`[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cryptoreplaceffxfpeconfig-class)` | CryptoReplaceFfxFpeConfig  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig;

Decodes a CryptoReplaceFfxFpeConfig message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cryptoreplaceffxfpeconfig-class)` | CryptoReplaceFfxFpeConfig  
  
### encode(message, writer)
    
    
    public static encode(message: google.privacy.dlp.v2.ICryptoReplaceFfxFpeConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CryptoReplaceFfxFpeConfig message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.icryptoreplaceffxfpeconfig)`   
CryptoReplaceFfxFpeConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.privacy.dlp.v2.ICryptoReplaceFfxFpeConfig, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CryptoReplaceFfxFpeConfig message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.icryptoreplaceffxfpeconfig)`   
CryptoReplaceFfxFpeConfig message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig;

Creates a CryptoReplaceFfxFpeConfig message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cryptoreplaceffxfpeconfig-class)` | CryptoReplaceFfxFpeConfig  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CryptoReplaceFfxFpeConfig

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

Converts this CryptoReplaceFfxFpeConfig to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CryptoReplaceFfxFpeConfig message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.cryptoreplaceffxfpeconfig-class)`   
CryptoReplaceFfxFpeConfig  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CryptoReplaceFfxFpeConfig message.

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
