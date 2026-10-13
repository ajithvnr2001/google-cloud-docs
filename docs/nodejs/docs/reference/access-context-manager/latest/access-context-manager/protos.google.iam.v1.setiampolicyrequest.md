---
url: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.setiampolicyrequest
title: Class protos.google.iam.v1.SetIamPolicyRequest (5.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:54.089153+00:00
---

# Class protos.google.iam.v1.SetIamPolicyRequest (5.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.setiampolicyrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.iam.v1.SetIamPolicyRequest (5.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  2.3.2  2.2.0  2.1.1  1.0.0  0.2.0 

Represents a SetIamPolicyRequest.

## Implements

[protos.google.iam.v1.ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.isetiampolicyrequest)

## Package

[@google-cloud/access-context-manager](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.iam.v1.ISetIamPolicyRequest);

Constructs a new SetIamPolicyRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.isetiampolicyrequest)`   
Properties to set  
  
## Properties 

### policy
    
    
    public policy?: (google.iam.v1.IPolicy|null);

SetIamPolicyRequest policy.

### resource
    
    
    public resource: string;

SetIamPolicyRequest resource.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

SetIamPolicyRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.iam.v1.ISetIamPolicyRequest): google.iam.v1.SetIamPolicyRequest;

Creates a new SetIamPolicyRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.isetiampolicyrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[SetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.setiampolicyrequest)` | SetIamPolicyRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.iam.v1.SetIamPolicyRequest;

Decodes a SetIamPolicyRequest message from the specified reader or buffer.

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
`[SetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.setiampolicyrequest)` | SetIamPolicyRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.iam.v1.SetIamPolicyRequest;

Decodes a SetIamPolicyRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[SetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.setiampolicyrequest)` | SetIamPolicyRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.iam.v1.ISetIamPolicyRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SetIamPolicyRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.iam.v1.ISetIamPolicyRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified SetIamPolicyRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.iam.v1.SetIamPolicyRequest;

Creates a SetIamPolicyRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[SetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.setiampolicyrequest)` | SetIamPolicyRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for SetIamPolicyRequest

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

Converts this SetIamPolicyRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.iam.v1.SetIamPolicyRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a SetIamPolicyRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[SetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.iam.v1.setiampolicyrequest)`   
SetIamPolicyRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a SetIamPolicyRequest message.

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
