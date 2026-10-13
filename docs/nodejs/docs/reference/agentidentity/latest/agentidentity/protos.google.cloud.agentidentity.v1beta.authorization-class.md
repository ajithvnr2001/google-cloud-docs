---
url: https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.authorization-class
title: Class protos.google.cloud.agentidentity.v1beta.Authorization (0.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:52.132868+00:00
---

# Class protos.google.cloud.agentidentity.v1beta.Authorization (0.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.authorization-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.agentidentity.v1beta.Authorization (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an Authorization.

## Implements

[protos.google.cloud.agentidentity.v1beta.IAuthorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.iauthorization)

## Package

[@google-cloud/agentidentity](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.agentidentity.v1beta.IAuthorization);

Constructs a new Authorization.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuthorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.iauthorization)`   
Properties to set  
  
## Properties 

### clientUserId
    
    
    public clientUserId: string;

Authorization clientUserId.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Authorization createTime.

### name
    
    
    public name: string;

Authorization name.

### scopes
    
    
    public scopes: string[];

Authorization scopes.

### state
    
    
    public state: (google.cloud.agentidentity.v1beta.Authorization.State|keyof typeof google.cloud.agentidentity.v1beta.Authorization.State);

Authorization state.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Authorization updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.agentidentity.v1beta.IAuthorization): google.cloud.agentidentity.v1beta.Authorization;

Creates a new Authorization instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAuthorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.iauthorization)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Authorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.authorization-class)` | Authorization instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.agentidentity.v1beta.Authorization;

Decodes an Authorization message from the specified reader or buffer.

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
`[Authorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.authorization-class)` | Authorization  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.agentidentity.v1beta.Authorization;

Decodes an Authorization message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Authorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.authorization-class)` | Authorization  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.agentidentity.v1beta.IAuthorization, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Authorization message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuthorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.iauthorization)`   
Authorization message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.agentidentity.v1beta.IAuthorization, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Authorization message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAuthorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.iauthorization)`   
Authorization message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.agentidentity.v1beta.Authorization;

Creates an Authorization message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Authorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.authorization-class)` | Authorization  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Authorization

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

Converts this Authorization to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.agentidentity.v1beta.Authorization, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Authorization message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Authorization](https://docs.cloud.google.com/nodejs/docs/reference/agentidentity/latest/agentidentity/protos.google.cloud.agentidentity.v1beta.authorization-class)`   
Authorization  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Authorization message.

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

Last updated 2026-08-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-12 UTC."],[],[]] 
