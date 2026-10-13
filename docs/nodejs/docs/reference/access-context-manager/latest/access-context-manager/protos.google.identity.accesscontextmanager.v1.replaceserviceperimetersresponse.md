---
url: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.replaceserviceperimetersresponse
title: Class protos.google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse (5.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:43:01.093543+00:00
---

# Class protos.google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse (5.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.replaceserviceperimetersresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse (5.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  2.3.2  2.2.0  2.1.1  1.0.0  0.2.0 

Represents a ReplaceServicePerimetersResponse.

## Implements

[protos.google.identity.accesscontextmanager.v1.IReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceserviceperimetersresponse)

## Package

[@google-cloud/access-context-manager](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.identity.accesscontextmanager.v1.IReplaceServicePerimetersResponse);

Constructs a new ReplaceServicePerimetersResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceserviceperimetersresponse)`   
Properties to set  
  
## Properties 

### servicePerimeters
    
    
    public servicePerimeters: google.identity.accesscontextmanager.v1.IServicePerimeter[];

ReplaceServicePerimetersResponse servicePerimeters.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.identity.accesscontextmanager.v1.IReplaceServicePerimetersResponse): google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse;

Creates a new ReplaceServicePerimetersResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceserviceperimetersresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.replaceserviceperimetersresponse)` | ReplaceServicePerimetersResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse;

Decodes a ReplaceServicePerimetersResponse message from the specified reader or buffer.

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
`[ReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.replaceserviceperimetersresponse)` | ReplaceServicePerimetersResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse;

Decodes a ReplaceServicePerimetersResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.replaceserviceperimetersresponse)` | ReplaceServicePerimetersResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.identity.accesscontextmanager.v1.IReplaceServicePerimetersResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ReplaceServicePerimetersResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceserviceperimetersresponse)`   
ReplaceServicePerimetersResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.identity.accesscontextmanager.v1.IReplaceServicePerimetersResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ReplaceServicePerimetersResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.ireplaceserviceperimetersresponse)`   
ReplaceServicePerimetersResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse;

Creates a ReplaceServicePerimetersResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.replaceserviceperimetersresponse)` | ReplaceServicePerimetersResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ReplaceServicePerimetersResponse

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

Converts this ReplaceServicePerimetersResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ReplaceServicePerimetersResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ReplaceServicePerimetersResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-context-manager/latest/access-context-manager/protos.google.identity.accesscontextmanager.v1.replaceserviceperimetersresponse)`   
ReplaceServicePerimetersResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ReplaceServicePerimetersResponse message.

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
