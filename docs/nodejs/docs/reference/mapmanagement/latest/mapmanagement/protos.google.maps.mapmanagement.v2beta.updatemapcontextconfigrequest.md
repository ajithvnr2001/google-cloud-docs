---
url: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapcontextconfigrequest
title: Class protos.google.maps.mapmanagement.v2beta.UpdateMapContextConfigRequest (0.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:21.235002+00:00
---

# Class protos.google.maps.mapmanagement.v2beta.UpdateMapContextConfigRequest (0.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapcontextconfigrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.maps.mapmanagement.v2beta.UpdateMapContextConfigRequest (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an UpdateMapContextConfigRequest.

## Implements

[protos.google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)

## Package

[@google-cloud/mapmanagement](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest);

Constructs a new UpdateMapContextConfigRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
Properties to set  
  
## Properties 

### mapContextConfig
    
    
    public mapContextConfig?: (google.maps.mapmanagement.v2beta.IMapContextConfig|null);

UpdateMapContextConfigRequest mapContextConfig.

### updateMask
    
    
    public updateMask?: (google.protobuf.IFieldMask|null);

UpdateMapContextConfigRequest updateMask.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest): google.maps.mapmanagement.v2beta.UpdateMapContextConfigRequest;

Creates a new UpdateMapContextConfigRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[UpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapcontextconfigrequest)` | UpdateMapContextConfigRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.maps.mapmanagement.v2beta.UpdateMapContextConfigRequest;

Decodes an UpdateMapContextConfigRequest message from the specified reader or buffer.

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
`[UpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapcontextconfigrequest)` | UpdateMapContextConfigRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.maps.mapmanagement.v2beta.UpdateMapContextConfigRequest;

Decodes an UpdateMapContextConfigRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[UpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapcontextconfigrequest)` | UpdateMapContextConfigRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateMapContextConfigRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
UpdateMapContextConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.maps.mapmanagement.v2beta.IUpdateMapContextConfigRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified UpdateMapContextConfigRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IUpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.iupdatemapcontextconfigrequest)`   
UpdateMapContextConfigRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.maps.mapmanagement.v2beta.UpdateMapContextConfigRequest;

Creates an UpdateMapContextConfigRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[UpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapcontextconfigrequest)` | UpdateMapContextConfigRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for UpdateMapContextConfigRequest

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

Converts this UpdateMapContextConfigRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.maps.mapmanagement.v2beta.UpdateMapContextConfigRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from an UpdateMapContextConfigRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[UpdateMapContextConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/mapmanagement/latest/mapmanagement/protos.google.maps.mapmanagement.v2beta.updatemapcontextconfigrequest)`   
UpdateMapContextConfigRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies an UpdateMapContextConfigRequest message.

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
