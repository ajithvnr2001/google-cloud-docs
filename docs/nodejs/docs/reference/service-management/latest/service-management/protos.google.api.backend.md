---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.backend
title: Class protos.google.api.Backend (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:10.020042+00:00
---

# Class protos.google.api.Backend (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.backend

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.Backend (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  2.2.0  1.2.2  1.1.3  0.4.0  0.3.1  0.2.6 

Represents a Backend.

## Implements

[protos.google.api.IBackend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.ibackend)

## Package

[@google-cloud/service-management](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.api.IBackend);

Constructs a new Backend.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBackend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.ibackend)`   
Properties to set  
  
## Properties 

### rules
    
    
    public rules: google.api.IBackendRule[];

Backend rules.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.api.IBackend): google.api.Backend;

Creates a new Backend instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBackend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.ibackend)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Backend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.backend)` | Backend instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.api.Backend;

Decodes a Backend message from the specified reader or buffer.

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
`[Backend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.backend)` | Backend  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.api.Backend;

Decodes a Backend message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Backend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.backend)` | Backend  
  
### encode(message, writer)
    
    
    public static encode(message: google.api.IBackend, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Backend message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBackend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.ibackend)`   
Backend message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.api.IBackend, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Backend message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBackend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.ibackend)`   
Backend message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.api.Backend;

Creates a Backend message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Backend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.backend)` | Backend  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Backend

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

Converts this Backend to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.api.Backend, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Backend message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Backend](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.api.backend)`   
Backend  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Backend message.

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
