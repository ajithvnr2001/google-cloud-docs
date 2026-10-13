---
url: https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.startserverrequest
title: Class protos.google.cloud.ftp.v1.StartServerRequest (0.3.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:39.772142+00:00
---

# Class protos.google.cloud.ftp.v1.StartServerRequest (0.3.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.startserverrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.ftp.v1.StartServerRequest (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a StartServerRequest.

## Implements

[protos.google.cloud.ftp.v1.IStartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.istartserverrequest)

## Package

[@google-cloud/ftp](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.ftp.v1.IStartServerRequest);

Constructs a new StartServerRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.istartserverrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

StartServerRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.ftp.v1.IStartServerRequest): google.cloud.ftp.v1.StartServerRequest;

Creates a new StartServerRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IStartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.istartserverrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[StartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.startserverrequest)` | StartServerRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.ftp.v1.StartServerRequest;

Decodes a StartServerRequest message from the specified reader or buffer.

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
`[StartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.startserverrequest)` | StartServerRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.ftp.v1.StartServerRequest;

Decodes a StartServerRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[StartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.startserverrequest)` | StartServerRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.ftp.v1.IStartServerRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StartServerRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.istartserverrequest)`   
StartServerRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.ftp.v1.IStartServerRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified StartServerRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IStartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.istartserverrequest)`   
StartServerRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.ftp.v1.StartServerRequest;

Creates a StartServerRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[StartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.startserverrequest)` | StartServerRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for StartServerRequest

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

Converts this StartServerRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.ftp.v1.StartServerRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a StartServerRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[StartServerRequest](https://docs.cloud.google.com/nodejs/docs/reference/ftp/latest/ftp/protos.google.cloud.ftp.v1.startserverrequest)`   
StartServerRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a StartServerRequest message.

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
