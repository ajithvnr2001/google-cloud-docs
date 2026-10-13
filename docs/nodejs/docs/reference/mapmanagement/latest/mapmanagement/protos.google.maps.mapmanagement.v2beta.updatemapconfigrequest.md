---
url: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapconfigrequest
title: Class protos.google.maps.mapmanagement.v2beta.UpdateMapConfigRequest (0.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:19.661647+00:00
---

# Class protos.google.maps.mapmanagement.v2beta.UpdateMapConfigRequest (0.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapconfigrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.mapmanagement.v2beta.UpdateMapConfigRequest (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an UpdateMapConfigRequest.

## Implements

[protos.google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)

## Package

[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest);

Constructs a new UpdateMapConfigRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
Properties to set  
  
## Properties 

### mapConfig
    
    
    public mapConfig?: (google.maps.mapmanagement.v2beta.IMapConfig|null);

UpdateMapConfigRequest mapConfig.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateMapConfigRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest): google.maps.mapmanagement.v2beta.UpdateMapConfigRequest;

Creates a new UpdateMapConfigRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapconfigrequest)` | UpdateMapConfigRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.mapmanagement.v2beta.UpdateMapConfigRequest;

Decodes an UpdateMapConfigRequest message from the specified reader or buffer.

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
`[UpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapconfigrequest)` | UpdateMapConfigRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.mapmanagement.v2beta.UpdateMapConfigRequest;

Decodes an UpdateMapConfigRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapconfigrequest)` | UpdateMapConfigRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateMapConfigRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
UpdateMapConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.mapmanagement.v2beta.IUpdateMapConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateMapConfigRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapconfigrequest)`   
UpdateMapConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.mapmanagement.v2beta.UpdateMapConfigRequest;

Creates an UpdateMapConfigRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapconfigrequest)` | UpdateMapConfigRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateMapConfigRequest

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

Converts this UpdateMapConfigRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.mapmanagement.v2beta.UpdateMapConfigRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateMapConfigRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateMapConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapconfigrequest)`   
UpdateMapConfigRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateMapConfigRequest message.

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
