---
url: https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.updateendpointpolicyrequest
title: Class protos.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest (0.17.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:07.531252+00:00
---

# Class protos.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest (0.17.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.updateendpointpolicyrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest (0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.13.0  0.12.0  0.9.0  0.8.1  0.7.0  0.2.1 

Represents an UpdateEndpointPolicyRequest.

## Implements

[protos.google.cloud.networkservices.v1.IUpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.iupdateendpointpolicyrequest)

## Package

[@google-cloud/networkservices](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.networkservices.v1.IUpdateEndpointPolicyRequest);

Constructs a new UpdateEndpointPolicyRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.iupdateendpointpolicyrequest)`   
Properties to set  
  
## Properties 

### endpointPolicy
    
    
    public endpointPolicy?: (google.cloud.networkservices.v1.IEndpointPolicy|null);

UpdateEndpointPolicyRequest endpointPolicy.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateEndpointPolicyRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.networkservices.v1.IUpdateEndpointPolicyRequest): google.cloud.networkservices.v1.UpdateEndpointPolicyRequest;

Creates a new UpdateEndpointPolicyRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.iupdateendpointpolicyrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.updateendpointpolicyrequest)` | UpdateEndpointPolicyRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.networkservices.v1.UpdateEndpointPolicyRequest;

Decodes an UpdateEndpointPolicyRequest message from the specified reader or buffer.

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
`[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.updateendpointpolicyrequest)` | UpdateEndpointPolicyRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.networkservices.v1.UpdateEndpointPolicyRequest;

Decodes an UpdateEndpointPolicyRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.updateendpointpolicyrequest)` | UpdateEndpointPolicyRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.networkservices.v1.IUpdateEndpointPolicyRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateEndpointPolicyRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.iupdateendpointpolicyrequest)`   
UpdateEndpointPolicyRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.networkservices.v1.IUpdateEndpointPolicyRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateEndpointPolicyRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.iupdateendpointpolicyrequest)`   
UpdateEndpointPolicyRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.networkservices.v1.UpdateEndpointPolicyRequest;

Creates an UpdateEndpointPolicyRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.updateendpointpolicyrequest)` | UpdateEndpointPolicyRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateEndpointPolicyRequest

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

Converts this UpdateEndpointPolicyRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.networkservices.v1.UpdateEndpointPolicyRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateEndpointPolicyRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/networkservices/latest/networkservices/protos.google.cloud.networkservices.v1.updateendpointpolicyrequest)`   
UpdateEndpointPolicyRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateEndpointPolicyRequest message.

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
