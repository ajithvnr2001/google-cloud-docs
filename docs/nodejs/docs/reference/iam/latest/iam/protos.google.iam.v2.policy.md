---
url: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.policy
title: Class protos.google.iam.v2.Policy (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:58.666524+00:00
---

# Class protos.google.iam.v2.Policy (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.policy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.iam.v2.Policy (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.2.0  0.3.2  0.2.2 

Represents a Policy.

## Implements

[protos.google.iam.v2.IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.ipolicy)

## Package

[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.iam.v2.IPolicy);

Constructs a new Policy.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.ipolicy)`   
Properties to set  
  
## Properties 

### annotations
    
    
    public annotations: { [k: string]: string };

Policy annotations.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Policy createTime.

### deleteTime
    
    
    public deleteTime?: (google.protobuf.ITimestamp|null);

Policy deleteTime.

### displayName
    
    
    public displayName: string;

Policy displayName.

### etag
    
    
    public etag: string;

Policy etag.

### kind
    
    
    public kind: string;

Policy kind.

### managingAuthority
    
    
    public managingAuthority: string;

Policy managingAuthority.

### name
    
    
    public name: string;

Policy name.

### rules
    
    
    public rules: google.iam.v2.IPolicyRule[];

Policy rules.

### uid
    
    
    public uid: string;

Policy uid.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Policy updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.iam.v2.IPolicy): google.iam.v2.Policy;

Creates a new Policy instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.ipolicy)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.policy)` | Policy instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.iam.v2.Policy;

Decodes a Policy message from the specified reader or buffer.

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
`[Policy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.policy)` | Policy  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.iam.v2.Policy;

Decodes a Policy message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.policy)` | Policy  
  
### encode(message, writer)
    
    
    public static encode(message: google.iam.v2.IPolicy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Policy message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.ipolicy)`   
Policy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.iam.v2.IPolicy, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Policy message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPolicy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.ipolicy)`   
Policy message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.iam.v2.Policy;

Creates a Policy message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.policy)` | Policy  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Policy

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

Converts this Policy to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.iam.v2.Policy, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Policy message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Policy](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/iam/protos.google.iam.v2.policy)`   
Policy  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Policy message.

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
