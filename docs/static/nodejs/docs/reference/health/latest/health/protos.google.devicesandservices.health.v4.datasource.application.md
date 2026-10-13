---
url: https://docs.cloud.google.com/static/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.application
title: Class protos.google.devicesandservices.health.v4.DataSource.Application (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:05.751009+00:00
---

# Class protos.google.devicesandservices.health.v4.DataSource.Application (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/static/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.application

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.DataSource.Application (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an Application.

## Implements

[protos.google.devicesandservices.health.v4.DataSource.IApplication](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.iapplication)

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.devicesandservices.health.v4.DataSource.IApplication);

Constructs a new Application.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApplication](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.iapplication)`   
Properties to set  
  
## Properties 

### googleWebClientId
    
    
    public googleWebClientId: string;

Application googleWebClientId.

### packageName
    
    
    public packageName: string;

Application packageName.

### webClientId
    
    
    public webClientId: string;

Application webClientId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.devicesandservices.health.v4.DataSource.IApplication): google.devicesandservices.health.v4.DataSource.Application;

Creates a new Application instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IApplication](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.iapplication)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.application)` | Application instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.devicesandservices.health.v4.DataSource.Application;

Decodes an Application message from the specified reader or buffer.

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
`[Application](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.application)` | Application  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.devicesandservices.health.v4.DataSource.Application;

Decodes an Application message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.application)` | Application  
  
### encode(message, writer)
    
    
    public static encode(message: google.devicesandservices.health.v4.DataSource.IApplication, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Application message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApplication](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.iapplication)`   
Application message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.devicesandservices.health.v4.DataSource.IApplication, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Application message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IApplication](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.iapplication)`   
Application message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.devicesandservices.health.v4.DataSource.Application;

Creates an Application message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Application](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.application)` | Application  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Application

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

Converts this Application to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.devicesandservices.health.v4.DataSource.Application, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an Application message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Application](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasource.application)`   
Application  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an Application message.

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
