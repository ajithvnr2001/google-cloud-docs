---
url: https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginehttprequest
title: Class protos.google.cloud.tasks.v2beta3.AppEngineHttpRequest (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:50.269204+00:00
---

# Class protos.google.cloud.tasks.v2beta3.AppEngineHttpRequest (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginehttprequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.tasks.v2beta3.AppEngineHttpRequest (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.2.0  7.1.1  5.5.2  3.1.2  3.0.5  2.5.0  2.4.2  2.3.6 

Represents an AppEngineHttpRequest.

## Implements

[protos.google.cloud.tasks.v2beta3.IAppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginehttprequest)

## Package

[@google-cloud/tasks](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.tasks.v2beta3.IAppEngineHttpRequest);

Constructs a new AppEngineHttpRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginehttprequest)`   
Properties to set  
  
## Properties 

### appEngineRouting
    
    
    public appEngineRouting?: (google.cloud.tasks.v2beta3.IAppEngineRouting|null);

AppEngineHttpRequest appEngineRouting.

### body
    
    
    public body: (Uint8Array|Buffer|string);

AppEngineHttpRequest body.

### headers
    
    
    public headers: { [k: string]: string };

AppEngineHttpRequest headers.

### httpMethod
    
    
    public httpMethod: (google.cloud.tasks.v2beta3.HttpMethod|keyof typeof google.cloud.tasks.v2beta3.HttpMethod);

AppEngineHttpRequest httpMethod.

### relativeUri
    
    
    public relativeUri: string;

AppEngineHttpRequest relativeUri.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.tasks.v2beta3.IAppEngineHttpRequest): google.cloud.tasks.v2beta3.AppEngineHttpRequest;

Creates a new AppEngineHttpRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IAppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginehttprequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[AppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginehttprequest)` | AppEngineHttpRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.tasks.v2beta3.AppEngineHttpRequest;

Decodes an AppEngineHttpRequest message from the specified reader or buffer.

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
`[AppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginehttprequest)` | AppEngineHttpRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.tasks.v2beta3.AppEngineHttpRequest;

Decodes an AppEngineHttpRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[AppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginehttprequest)` | AppEngineHttpRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.tasks.v2beta3.IAppEngineHttpRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppEngineHttpRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginehttprequest)`   
AppEngineHttpRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.tasks.v2beta3.IAppEngineHttpRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified AppEngineHttpRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IAppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.iappenginehttprequest)`   
AppEngineHttpRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.tasks.v2beta3.AppEngineHttpRequest;

Creates an AppEngineHttpRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[AppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginehttprequest)` | AppEngineHttpRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for AppEngineHttpRequest

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

Converts this AppEngineHttpRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.tasks.v2beta3.AppEngineHttpRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an AppEngineHttpRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[AppEngineHttpRequest](https://docs.cloud.google.com/nodejs/docs/reference/tasks/latest/tasks/protos.google.cloud.tasks.v2beta3.appenginehttprequest)`   
AppEngineHttpRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an AppEngineHttpRequest message.

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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
