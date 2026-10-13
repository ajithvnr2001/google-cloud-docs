---
url: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.deletecustomclassrequest
title: Class protos.google.cloud.speech.v2.DeleteCustomClassRequest (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:49.619548+00:00
---

# Class protos.google.cloud.speech.v2.DeleteCustomClassRequest (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.deletecustomclassrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.speech.v2.DeleteCustomClassRequest (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  8.0.1  7.5.0  7.4.0  6.6.1  6.3.0  6.1.1  6.0.1  5.4.1  5.3.1  5.1.0  5.0.3  4.10.0  4.9.0  4.8.1  4.7.0  4.6.1  4.5.6  4.1.3 

Represents a DeleteCustomClassRequest.

## Implements

[protos.google.cloud.speech.v2.IDeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.ideletecustomclassrequest)

## Package

[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.speech.v2.IDeleteCustomClassRequest);

Constructs a new DeleteCustomClassRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.ideletecustomclassrequest)`   
Properties to set  
  
## Properties 

### allowMissing
    
    
    public allowMissing: boolean;

DeleteCustomClassRequest allowMissing.

### etag
    
    
    public etag: string;

DeleteCustomClassRequest etag.

### name
    
    
    public name: string;

DeleteCustomClassRequest name.

### validateOnly
    
    
    public validateOnly: boolean;

DeleteCustomClassRequest validateOnly.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.speech.v2.IDeleteCustomClassRequest): google.cloud.speech.v2.DeleteCustomClassRequest;

Creates a new DeleteCustomClassRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.ideletecustomclassrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.deletecustomclassrequest)` | DeleteCustomClassRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.speech.v2.DeleteCustomClassRequest;

Decodes a DeleteCustomClassRequest message from the specified reader or buffer.

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
`[DeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.deletecustomclassrequest)` | DeleteCustomClassRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.speech.v2.DeleteCustomClassRequest;

Decodes a DeleteCustomClassRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.deletecustomclassrequest)` | DeleteCustomClassRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.speech.v2.IDeleteCustomClassRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteCustomClassRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.ideletecustomclassrequest)`   
DeleteCustomClassRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.speech.v2.IDeleteCustomClassRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteCustomClassRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.ideletecustomclassrequest)`   
DeleteCustomClassRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.speech.v2.DeleteCustomClassRequest;

Creates a DeleteCustomClassRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.deletecustomclassrequest)` | DeleteCustomClassRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteCustomClassRequest

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

Converts this DeleteCustomClassRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.speech.v2.DeleteCustomClassRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteCustomClassRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteCustomClassRequest](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/speech/protos.google.cloud.speech.v2.deletecustomclassrequest)`   
DeleteCustomClassRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteCustomClassRequest message.

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
