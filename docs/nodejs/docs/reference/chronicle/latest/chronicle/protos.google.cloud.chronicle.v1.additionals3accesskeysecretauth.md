---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.additionals3accesskeysecretauth
title: Class protos.google.cloud.chronicle.v1.AdditionalS3AccessKeySecretAuth (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:50:51.285756+00:00
---

# Class protos.google.cloud.chronicle.v1.AdditionalS3AccessKeySecretAuth (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.additionals3accesskeysecretauth

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.AdditionalS3AccessKeySecretAuth (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents an AdditionalS3AccessKeySecretAuth.

## Implements

[protos.google.cloud.chronicle.v1.IAdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iadditionals3accesskeysecretauth)

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.chronicle.v1.IAdditionalS3AccessKeySecretAuth);

Constructs a new AdditionalS3AccessKeySecretAuth.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iadditionals3accesskeysecretauth)`   
Properties to set  
  
## Properties 

### accessKeyId
    
    
    public accessKeyId: string;

AdditionalS3AccessKeySecretAuth accessKeyId.

### secretAccessKey
    
    
    public secretAccessKey: string;

AdditionalS3AccessKeySecretAuth secretAccessKey.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.chronicle.v1.IAdditionalS3AccessKeySecretAuth): google.cloud.chronicle.v1.AdditionalS3AccessKeySecretAuth;

Creates a new AdditionalS3AccessKeySecretAuth instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iadditionals3accesskeysecretauth)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.additionals3accesskeysecretauth)` | AdditionalS3AccessKeySecretAuth instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.chronicle.v1.AdditionalS3AccessKeySecretAuth;

Decodes an AdditionalS3AccessKeySecretAuth message from the specified reader or buffer.

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
`[AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.additionals3accesskeysecretauth)` | AdditionalS3AccessKeySecretAuth  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.chronicle.v1.AdditionalS3AccessKeySecretAuth;

Decodes an AdditionalS3AccessKeySecretAuth message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.additionals3accesskeysecretauth)` | AdditionalS3AccessKeySecretAuth  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.chronicle.v1.IAdditionalS3AccessKeySecretAuth, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdditionalS3AccessKeySecretAuth message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iadditionals3accesskeysecretauth)`   
AdditionalS3AccessKeySecretAuth message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.chronicle.v1.IAdditionalS3AccessKeySecretAuth, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AdditionalS3AccessKeySecretAuth message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iadditionals3accesskeysecretauth)`   
AdditionalS3AccessKeySecretAuth message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.chronicle.v1.AdditionalS3AccessKeySecretAuth;

Creates an AdditionalS3AccessKeySecretAuth message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.additionals3accesskeysecretauth)` | AdditionalS3AccessKeySecretAuth  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AdditionalS3AccessKeySecretAuth

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

Converts this AdditionalS3AccessKeySecretAuth to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.chronicle.v1.AdditionalS3AccessKeySecretAuth, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AdditionalS3AccessKeySecretAuth message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AdditionalS3AccessKeySecretAuth](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.additionals3accesskeysecretauth)`   
AdditionalS3AccessKeySecretAuth  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AdditionalS3AccessKeySecretAuth message.

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
