---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.updatespecrequest
title: Class protos.google.cloud.apihub.v1.UpdateSpecRequest (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:07.223071+00:00
---

# Class protos.google.cloud.apihub.v1.UpdateSpecRequest (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.updatespecrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.UpdateSpecRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an UpdateSpecRequest.

## Implements

[protos.google.cloud.apihub.v1.IUpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatespecrequest)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IUpdateSpecRequest);

Constructs a new UpdateSpecRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatespecrequest)`   
Properties to set  
  
## Properties 

### spec
    
    
    public spec?: (google.cloud.apihub.v1.ISpec|null);

UpdateSpecRequest spec.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateSpecRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IUpdateSpecRequest): google.cloud.apihub.v1.UpdateSpecRequest;

Creates a new UpdateSpecRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatespecrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.updatespecrequest)` | UpdateSpecRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.UpdateSpecRequest;

Decodes an UpdateSpecRequest message from the specified reader or buffer.

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
`[UpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.updatespecrequest)` | UpdateSpecRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.UpdateSpecRequest;

Decodes an UpdateSpecRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.updatespecrequest)` | UpdateSpecRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IUpdateSpecRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateSpecRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatespecrequest)`   
UpdateSpecRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IUpdateSpecRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateSpecRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iupdatespecrequest)`   
UpdateSpecRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.UpdateSpecRequest;

Creates an UpdateSpecRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.updatespecrequest)` | UpdateSpecRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateSpecRequest

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

Converts this UpdateSpecRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.UpdateSpecRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateSpecRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateSpecRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.updatespecrequest)`   
UpdateSpecRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateSpecRequest message.

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
