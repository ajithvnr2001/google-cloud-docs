---
url: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.accesslevel
title: Class protos.google.identity.accesscontextmanager.v1.AccessLevel (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:19.101481+00:00
---

# Class protos.google.identity.accesscontextmanager.v1.AccessLevel (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.accesslevel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.identity.accesscontextmanager.v1.AccessLevel (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.3.3  5.5.0  5.3.0  5.2.0  5.1.0  5.0.1  4.6.3  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  3.23.1  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.1  3.15.5  3.14.1  3.13.0 

Represents an AccessLevel.

## Implements

[protos.google.identity.accesscontextmanager.v1.IAccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.iaccesslevel)

## Package

[@google-cloud/asset](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.identity.accesscontextmanager.v1.IAccessLevel);

Constructs a new AccessLevel.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.iaccesslevel)`   
Properties to set  
  
## Properties 

### basic
    
    
    public basic?: (google.identity.accesscontextmanager.v1.IBasicLevel|null);

AccessLevel basic.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

AccessLevel createTime.

### custom
    
    
    public custom?: (google.identity.accesscontextmanager.v1.ICustomLevel|null);

AccessLevel custom.

### description
    
    
    public description: string;

AccessLevel description.

### level
    
    
    public level?: ("basic"|"custom");

AccessLevel level.

### name
    
    
    public name: string;

AccessLevel name.

### title
    
    
    public title: string;

AccessLevel title.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

AccessLevel updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.identity.accesscontextmanager.v1.IAccessLevel): google.identity.accesscontextmanager.v1.AccessLevel;

Creates a new AccessLevel instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.iaccesslevel)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.accesslevel)` | AccessLevel instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.identity.accesscontextmanager.v1.AccessLevel;

Decodes an AccessLevel message from the specified reader or buffer.

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
`[AccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.accesslevel)` | AccessLevel  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.identity.accesscontextmanager.v1.AccessLevel;

Decodes an AccessLevel message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.accesslevel)` | AccessLevel  
  
### encode(message, writer)
    
    
    public static encode(message: google.identity.accesscontextmanager.v1.IAccessLevel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AccessLevel message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.iaccesslevel)`   
AccessLevel message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.identity.accesscontextmanager.v1.IAccessLevel, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AccessLevel message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.iaccesslevel)`   
AccessLevel message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.identity.accesscontextmanager.v1.AccessLevel;

Creates an AccessLevel message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.accesslevel)` | AccessLevel  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AccessLevel

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

Converts this AccessLevel to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.identity.accesscontextmanager.v1.AccessLevel, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AccessLevel message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AccessLevel](https://docs.cloud.google.com/nodejs/docs/reference/asset/latest/asset/protos.google.identity.accesscontextmanager.v1.accesslevel)`   
AccessLevel  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AccessLevel message.

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
