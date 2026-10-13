---
url: https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signblobresponse
title: Class protos.google.iam.credentials.v1.SignBlobResponse (5.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:43.636822+00:00
---

# Class protos.google.iam.credentials.v1.SignBlobResponse (5.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signblobresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.iam.credentials.v1.SignBlobResponse (5.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  2.0.4  1.2.0  1.1.1  1.0.8 

Represents a SignBlobResponse.

## Implements

[protos.google.iam.credentials.v1.ISignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignblobresponse)

## Package

[@google-cloud/iam-credentials](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.iam.credentials.v1.ISignBlobResponse);

Constructs a new SignBlobResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignblobresponse)`   
Properties to set  
  
## Properties 

### keyId
    
    
    public keyId: string;

SignBlobResponse keyId.

### signedBlob
    
    
    public signedBlob: (Uint8Array|Buffer|string);

SignBlobResponse signedBlob.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.iam.credentials.v1.ISignBlobResponse): google.iam.credentials.v1.SignBlobResponse;

Creates a new SignBlobResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignblobresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signblobresponse)` | SignBlobResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.iam.credentials.v1.SignBlobResponse;

Decodes a SignBlobResponse message from the specified reader or buffer.

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
`[SignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signblobresponse)` | SignBlobResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.iam.credentials.v1.SignBlobResponse;

Decodes a SignBlobResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signblobresponse)` | SignBlobResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.iam.credentials.v1.ISignBlobResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SignBlobResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignblobresponse)`   
SignBlobResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.iam.credentials.v1.ISignBlobResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SignBlobResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignblobresponse)`   
SignBlobResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.iam.credentials.v1.SignBlobResponse;

Creates a SignBlobResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signblobresponse)` | SignBlobResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SignBlobResponse

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

Converts this SignBlobResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.iam.credentials.v1.SignBlobResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SignBlobResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signblobresponse)`   
SignBlobResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SignBlobResponse message.

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
