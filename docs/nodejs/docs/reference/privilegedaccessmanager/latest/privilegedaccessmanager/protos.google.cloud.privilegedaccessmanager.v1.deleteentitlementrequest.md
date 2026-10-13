---
url: https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.deleteentitlementrequest
title: Class protos.google.cloud.privilegedaccessmanager.v1.DeleteEntitlementRequest (0.8.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:09.322810+00:00
---

# Class protos.google.cloud.privilegedaccessmanager.v1.DeleteEntitlementRequest (0.8.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.deleteentitlementrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.privilegedaccessmanager.v1.DeleteEntitlementRequest (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.4.0  0.3.1  0.2.0 

Represents a DeleteEntitlementRequest.

## Implements

[protos.google.cloud.privilegedaccessmanager.v1.IDeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ideleteentitlementrequest)

## Package

[@google-cloud/privilegedaccessmanager](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.privilegedaccessmanager.v1.IDeleteEntitlementRequest);

Constructs a new DeleteEntitlementRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ideleteentitlementrequest)`   
Properties to set  
  
## Properties 

### force
    
    
    public force: boolean;

DeleteEntitlementRequest force.

### name
    
    
    public name: string;

DeleteEntitlementRequest name.

### requestId
    
    
    public requestId: string;

DeleteEntitlementRequest requestId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.privilegedaccessmanager.v1.IDeleteEntitlementRequest): google.cloud.privilegedaccessmanager.v1.DeleteEntitlementRequest;

Creates a new DeleteEntitlementRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ideleteentitlementrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.deleteentitlementrequest)` | DeleteEntitlementRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.privilegedaccessmanager.v1.DeleteEntitlementRequest;

Decodes a DeleteEntitlementRequest message from the specified reader or buffer.

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
`[DeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.deleteentitlementrequest)` | DeleteEntitlementRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.privilegedaccessmanager.v1.DeleteEntitlementRequest;

Decodes a DeleteEntitlementRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.deleteentitlementrequest)` | DeleteEntitlementRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.privilegedaccessmanager.v1.IDeleteEntitlementRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteEntitlementRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ideleteentitlementrequest)`   
DeleteEntitlementRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.privilegedaccessmanager.v1.IDeleteEntitlementRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteEntitlementRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ideleteentitlementrequest)`   
DeleteEntitlementRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.privilegedaccessmanager.v1.DeleteEntitlementRequest;

Creates a DeleteEntitlementRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.deleteentitlementrequest)` | DeleteEntitlementRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteEntitlementRequest

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

Converts this DeleteEntitlementRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.privilegedaccessmanager.v1.DeleteEntitlementRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteEntitlementRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.deleteentitlementrequest)`   
DeleteEntitlementRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteEntitlementRequest message.

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
