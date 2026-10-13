---
url: https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.enablesecretversionrequest
title: Class protos.google.cloud.secretmanager.v1.EnableSecretVersionRequest (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:46.914270+00:00
---

# Class protos.google.cloud.secretmanager.v1.EnableSecretVersionRequest (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.enablesecretversionrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.secretmanager.v1.EnableSecretVersionRequest (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.3.0  6.2.0  5.5.0  5.4.0  5.2.0  4.2.2  4.1.4  3.12.0  3.11.0  3.10.1  3.9.1  3.8.1  3.7.3 

Represents an EnableSecretVersionRequest.

## Implements

[protos.google.cloud.secretmanager.v1.IEnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.ienablesecretversionrequest)

## Package

[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.secretmanager.v1.IEnableSecretVersionRequest);

Constructs a new EnableSecretVersionRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.ienablesecretversionrequest)`   
Properties to set  
  
## Properties 

### etag
    
    
    public etag: string;

EnableSecretVersionRequest etag.

### name
    
    
    public name: string;

EnableSecretVersionRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.secretmanager.v1.IEnableSecretVersionRequest): google.cloud.secretmanager.v1.EnableSecretVersionRequest;

Creates a new EnableSecretVersionRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IEnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.ienablesecretversionrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[EnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.enablesecretversionrequest)` | EnableSecretVersionRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.secretmanager.v1.EnableSecretVersionRequest;

Decodes an EnableSecretVersionRequest message from the specified reader or buffer.

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
`[EnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.enablesecretversionrequest)` | EnableSecretVersionRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.secretmanager.v1.EnableSecretVersionRequest;

Decodes an EnableSecretVersionRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[EnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.enablesecretversionrequest)` | EnableSecretVersionRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.secretmanager.v1.IEnableSecretVersionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EnableSecretVersionRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.ienablesecretversionrequest)`   
EnableSecretVersionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.secretmanager.v1.IEnableSecretVersionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified EnableSecretVersionRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IEnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.ienablesecretversionrequest)`   
EnableSecretVersionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.secretmanager.v1.EnableSecretVersionRequest;

Creates an EnableSecretVersionRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[EnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.enablesecretversionrequest)` | EnableSecretVersionRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for EnableSecretVersionRequest

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

Converts this EnableSecretVersionRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.secretmanager.v1.EnableSecretVersionRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an EnableSecretVersionRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[EnableSecretVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/secret-manager/protos.google.cloud.secretmanager.v1.enablesecretversionrequest)`   
EnableSecretVersionRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an EnableSecretVersionRequest message.

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
