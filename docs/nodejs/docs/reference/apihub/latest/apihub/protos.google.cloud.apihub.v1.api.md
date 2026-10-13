---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api
title: Class protos.google.cloud.apihub.v1.Api (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:05:39.359232+00:00
---

# Class protos.google.cloud.apihub.v1.Api (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.Api (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an Api.

## Implements

[protos.google.cloud.apihub.v1.IApi](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapi)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IApi);

Constructs a new Api.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApi](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapi)`   
Properties to set  
  
## Properties 

### apiFunctionalRequirements
    
    
    public apiFunctionalRequirements?: (google.cloud.apihub.v1.IAttributeValues|null);

Api apiFunctionalRequirements.

### apiRequirements
    
    
    public apiRequirements?: (google.cloud.apihub.v1.IAttributeValues|null);

Api apiRequirements.

### apiStyle
    
    
    public apiStyle?: (google.cloud.apihub.v1.IAttributeValues|null);

Api apiStyle.

### apiTechnicalRequirements
    
    
    public apiTechnicalRequirements?: (google.cloud.apihub.v1.IAttributeValues|null);

Api apiTechnicalRequirements.

### attributes
    
    
    public attributes: { [k: string]: google.cloud.apihub.v1.IAttributeValues };

Api attributes.

### businessUnit
    
    
    public businessUnit?: (google.cloud.apihub.v1.IAttributeValues|null);

Api businessUnit.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

Api createTime.

### description
    
    
    public description: string;

Api description.

### displayName
    
    
    public displayName: string;

Api displayName.

### documentation
    
    
    public documentation?: (google.cloud.apihub.v1.IDocumentation|null);

Api documentation.

### fingerprint
    
    
    public fingerprint: string;

Api fingerprint.

### maturityLevel
    
    
    public maturityLevel?: (google.cloud.apihub.v1.IAttributeValues|null);

Api maturityLevel.

### name
    
    
    public name: string;

Api name.

### owner
    
    
    public owner?: (google.cloud.apihub.v1.IOwner|null);

Api owner.

### selectedVersion
    
    
    public selectedVersion: string;

Api selectedVersion.

### sourceMetadata
    
    
    public sourceMetadata: google.cloud.apihub.v1.ISourceMetadata[];

Api sourceMetadata.

### targetUser
    
    
    public targetUser?: (google.cloud.apihub.v1.IAttributeValues|null);

Api targetUser.

### team
    
    
    public team?: (google.cloud.apihub.v1.IAttributeValues|null);

Api team.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

Api updateTime.

### versions
    
    
    public versions: string[];

Api versions.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IApi): google.cloud.apihub.v1.Api;

Creates a new Api instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApi](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapi)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Api](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api)` | Api instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.Api;

Decodes an Api message from the specified reader or buffer.

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
`[Api](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api)` | Api  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.Api;

Decodes an Api message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Api](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api)` | Api  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IApi, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Api message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApi](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapi)`   
Api message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IApi, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Api message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApi](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.iapi)`   
Api message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.Api;

Creates an Api message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Api](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api)` | Api  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Api

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

Converts this Api to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.Api, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Api message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Api](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.api)`   
Api  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Api message.

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
