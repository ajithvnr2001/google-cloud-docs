---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.method
title: Class protos.google.protobuf.Method (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:03.509102+00:00
---

# Class protos.google.protobuf.Method (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.method

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.protobuf.Method (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  4.1.0  2.2.0  1.2.2  1.1.3  0.4.0  0.3.1  0.2.6 

Represents a Method.

## Implements

[protos.google.protobuf.IMethod](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.imethod)

## Package

[@google-cloud/service-management](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.protobuf.IMethod);

Constructs a new Method.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMethod](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.imethod)`   
Properties to set  
  
## Properties 

### edition
    
    
    public edition: string;

Method edition.

### name
    
    
    public name: string;

Method name.

### options
    
    
    public options: google.protobuf.IOption[];

Method options.

### requestStreaming
    
    
    public requestStreaming: boolean;

Method requestStreaming.

### requestTypeUrl
    
    
    public requestTypeUrl: string;

Method requestTypeUrl.

### responseStreaming
    
    
    public responseStreaming: boolean;

Method responseStreaming.

### responseTypeUrl
    
    
    public responseTypeUrl: string;

Method responseTypeUrl.

### syntax
    
    
    public syntax: (google.protobuf.Syntax|keyof typeof google.protobuf.Syntax);

Method syntax.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.protobuf.IMethod): google.protobuf.Method;

Creates a new Method instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IMethod](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.imethod)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[Method](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.method)` | Method instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.protobuf.Method;

Decodes a Method message from the specified reader or buffer.

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
`[Method](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.method)` | Method  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.protobuf.Method;

Decodes a Method message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[Method](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.method)` | Method  
  
### encode(message, writer)
    
    
    public static encode(message: google.protobuf.IMethod, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Method message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMethod](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.imethod)`   
Method message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.protobuf.IMethod, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified Method message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IMethod](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.imethod)`   
Method message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.protobuf.Method;

Creates a Method message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[Method](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.method)` | Method  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for Method

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

Converts this Method to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.protobuf.Method, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a Method message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[Method](https://docs.cloud.google.com/nodejs/docs/reference/service-management/latest/service-management/protos.google.protobuf.method)`   
Method  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a Method message.

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
