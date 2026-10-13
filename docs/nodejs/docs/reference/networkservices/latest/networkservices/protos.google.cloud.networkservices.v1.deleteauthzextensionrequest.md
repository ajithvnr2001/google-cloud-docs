---
url: https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.deleteauthzextensionrequest
title: Class protos.google.cloud.networkservices.v1.DeleteAuthzExtensionRequest (0.17.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:24.147205+00:00
---

# Class protos.google.cloud.networkservices.v1.DeleteAuthzExtensionRequest (0.17.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.deleteauthzextensionrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkservices.v1.DeleteAuthzExtensionRequest (0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.13.0  0.12.0  0.9.0  0.8.1  0.7.0  0.2.1 

Represents a DeleteAuthzExtensionRequest.

## Implements

[protos.google.cloud.networkservices.v1.IDeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ideleteauthzextensionrequest)

## Package

[@google-cloud/networkservices](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkservices.v1.IDeleteAuthzExtensionRequest);

Constructs a new DeleteAuthzExtensionRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ideleteauthzextensionrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

DeleteAuthzExtensionRequest name.

### requestId
    
    
    public requestId: string;

DeleteAuthzExtensionRequest requestId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkservices.v1.IDeleteAuthzExtensionRequest): google.cloud.networkservices.v1.DeleteAuthzExtensionRequest;

Creates a new DeleteAuthzExtensionRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ideleteauthzextensionrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.deleteauthzextensionrequest)` | DeleteAuthzExtensionRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkservices.v1.DeleteAuthzExtensionRequest;

Decodes a DeleteAuthzExtensionRequest message from the specified reader or buffer.

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
`[DeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.deleteauthzextensionrequest)` | DeleteAuthzExtensionRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkservices.v1.DeleteAuthzExtensionRequest;

Decodes a DeleteAuthzExtensionRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.deleteauthzextensionrequest)` | DeleteAuthzExtensionRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkservices.v1.IDeleteAuthzExtensionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteAuthzExtensionRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ideleteauthzextensionrequest)`   
DeleteAuthzExtensionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkservices.v1.IDeleteAuthzExtensionRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteAuthzExtensionRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.ideleteauthzextensionrequest)`   
DeleteAuthzExtensionRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkservices.v1.DeleteAuthzExtensionRequest;

Creates a DeleteAuthzExtensionRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.deleteauthzextensionrequest)` | DeleteAuthzExtensionRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteAuthzExtensionRequest

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

Converts this DeleteAuthzExtensionRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkservices.v1.DeleteAuthzExtensionRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteAuthzExtensionRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteAuthzExtensionRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.deleteauthzextensionrequest)`   
DeleteAuthzExtensionRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteAuthzExtensionRequest message.

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
