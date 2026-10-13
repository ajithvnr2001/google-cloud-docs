---
url: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.updategcpuseraccessbindingrequest
title: Class protos.google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest (5.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:01.978327+00:00
---

# Class protos.google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest (5.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.updategcpuseraccessbindingrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest (5.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  2.3.2  2.2.0  2.1.1  1.0.0  0.2.0 

Represents an UpdateGcpUserAccessBindingRequest.

## Implements

[protos.google.identity.accesscontextmanager.v1.IUpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdategcpuseraccessbindingrequest)

## Package

[@google-cloud/access-context-manager](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.identity.accesscontextmanager.v1.IUpdateGcpUserAccessBindingRequest);

Constructs a new UpdateGcpUserAccessBindingRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdategcpuseraccessbindingrequest)`   
Properties to set  
  
## Properties 

### gcpUserAccessBinding
    
    
    public gcpUserAccessBinding?: (google.identity.accesscontextmanager.v1.IGcpUserAccessBinding|null);

UpdateGcpUserAccessBindingRequest gcpUserAccessBinding.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateGcpUserAccessBindingRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.identity.accesscontextmanager.v1.IUpdateGcpUserAccessBindingRequest): google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest;

Creates a new UpdateGcpUserAccessBindingRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdategcpuseraccessbindingrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.updategcpuseraccessbindingrequest)` | UpdateGcpUserAccessBindingRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest;

Decodes an UpdateGcpUserAccessBindingRequest message from the specified reader or buffer.

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
`[UpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.updategcpuseraccessbindingrequest)` | UpdateGcpUserAccessBindingRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest;

Decodes an UpdateGcpUserAccessBindingRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.updategcpuseraccessbindingrequest)` | UpdateGcpUserAccessBindingRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.identity.accesscontextmanager.v1.IUpdateGcpUserAccessBindingRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateGcpUserAccessBindingRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdategcpuseraccessbindingrequest)`   
UpdateGcpUserAccessBindingRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.identity.accesscontextmanager.v1.IUpdateGcpUserAccessBindingRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateGcpUserAccessBindingRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.iupdategcpuseraccessbindingrequest)`   
UpdateGcpUserAccessBindingRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest;

Creates an UpdateGcpUserAccessBindingRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.updategcpuseraccessbindingrequest)` | UpdateGcpUserAccessBindingRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateGcpUserAccessBindingRequest

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

Converts this UpdateGcpUserAccessBindingRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateGcpUserAccessBindingRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.updategcpuseraccessbindingrequest)`   
UpdateGcpUserAccessBindingRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateGcpUserAccessBindingRequest message.

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
