---
url: https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.undeletekeyrequest
title: Class protos.google.api.apikeys.v2.UndeleteKeyRequest (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:17.928883+00:00
---

# Class protos.google.api.apikeys.v2.UndeleteKeyRequest (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.undeletekeyrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.apikeys.v2.UndeleteKeyRequest (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  3.1.0  1.2.0  0.2.2  0.1.3 

Represents an UndeleteKeyRequest.

## Implements

[protos.google.api.apikeys.v2.IUndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.iundeletekeyrequest)

## Package

[@google-cloud/apikeys](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.apikeys.v2.IUndeleteKeyRequest);

Constructs a new UndeleteKeyRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.iundeletekeyrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

UndeleteKeyRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.apikeys.v2.IUndeleteKeyRequest): google.api.apikeys.v2.UndeleteKeyRequest;

Creates a new UndeleteKeyRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.iundeletekeyrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.undeletekeyrequest)` | UndeleteKeyRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.apikeys.v2.UndeleteKeyRequest;

Decodes an UndeleteKeyRequest message from the specified reader or buffer.

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
`[UndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.undeletekeyrequest)` | UndeleteKeyRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.apikeys.v2.UndeleteKeyRequest;

Decodes an UndeleteKeyRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.undeletekeyrequest)` | UndeleteKeyRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.apikeys.v2.IUndeleteKeyRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UndeleteKeyRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.iundeletekeyrequest)`   
UndeleteKeyRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.apikeys.v2.IUndeleteKeyRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UndeleteKeyRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.iundeletekeyrequest)`   
UndeleteKeyRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.apikeys.v2.UndeleteKeyRequest;

Creates an UndeleteKeyRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.undeletekeyrequest)` | UndeleteKeyRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UndeleteKeyRequest

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

Converts this UndeleteKeyRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.apikeys.v2.UndeleteKeyRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UndeleteKeyRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UndeleteKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/apikeys/latest/apikeys/protos.google.api.apikeys.v2.undeletekeyrequest)`   
UndeleteKeyRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UndeleteKeyRequest message.

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
