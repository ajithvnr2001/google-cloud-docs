---
url: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.deletemapconfigrequest
title: Class protos.google.maps.mapmanagement.v2beta.DeleteMapConfigRequest (0.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:16.013094+00:00
---

# Class protos.google.maps.mapmanagement.v2beta.DeleteMapConfigRequest (0.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.deletemapconfigrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.mapmanagement.v2beta.DeleteMapConfigRequest (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DeleteMapConfigRequest.

## Implements

[protos.google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)

## Package

[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest);

Constructs a new DeleteMapConfigRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
Properties to set  
  
## Properties 

### force
    
    
    public force: boolean;

DeleteMapConfigRequest force.

### name
    
    
    public name: string;

DeleteMapConfigRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest): google.maps.mapmanagement.v2beta.DeleteMapConfigRequest;

Creates a new DeleteMapConfigRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[DeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.deletemapconfigrequest)` | DeleteMapConfigRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.mapmanagement.v2beta.DeleteMapConfigRequest;

Decodes a DeleteMapConfigRequest message from the specified reader or buffer.

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
`[DeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.deletemapconfigrequest)` | DeleteMapConfigRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.mapmanagement.v2beta.DeleteMapConfigRequest;

Decodes a DeleteMapConfigRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[DeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.deletemapconfigrequest)` | DeleteMapConfigRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteMapConfigRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
DeleteMapConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.mapmanagement.v2beta.IDeleteMapConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified DeleteMapConfigRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IDeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.ideletemapconfigrequest)`   
DeleteMapConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.mapmanagement.v2beta.DeleteMapConfigRequest;

Creates a DeleteMapConfigRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[DeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.deletemapconfigrequest)` | DeleteMapConfigRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for DeleteMapConfigRequest

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

Converts this DeleteMapConfigRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.mapmanagement.v2beta.DeleteMapConfigRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a DeleteMapConfigRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[DeleteMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.deletemapconfigrequest)`   
DeleteMapConfigRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a DeleteMapConfigRequest message.

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

Last updated 2026-06-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-25 UTC."],[],[]] 
