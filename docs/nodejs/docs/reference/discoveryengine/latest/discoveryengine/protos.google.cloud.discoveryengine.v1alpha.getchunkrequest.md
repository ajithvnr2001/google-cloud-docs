---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.getchunkrequest
title: Class protos.google.cloud.discoveryengine.v1alpha.GetChunkRequest (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:06.885336+00:00
---

# Class protos.google.cloud.discoveryengine.v1alpha.GetChunkRequest (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.getchunkrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1alpha.GetChunkRequest (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents a GetChunkRequest.

## Implements

[protos.google.cloud.discoveryengine.v1alpha.IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetchunkrequest)

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.discoveryengine.v1alpha.IGetChunkRequest);

Constructs a new GetChunkRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetchunkrequest)`   
Properties to set  
  
## Properties 

### name
    
    
    public name: string;

GetChunkRequest name.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.discoveryengine.v1alpha.IGetChunkRequest): google.cloud.discoveryengine.v1alpha.GetChunkRequest;

Creates a new GetChunkRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetchunkrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.getchunkrequest)` | GetChunkRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.discoveryengine.v1alpha.GetChunkRequest;

Decodes a GetChunkRequest message from the specified reader or buffer.

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
`[GetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.getchunkrequest)` | GetChunkRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.discoveryengine.v1alpha.GetChunkRequest;

Decodes a GetChunkRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.getchunkrequest)` | GetChunkRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.discoveryengine.v1alpha.IGetChunkRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetChunkRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetchunkrequest)`   
GetChunkRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.discoveryengine.v1alpha.IGetChunkRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetChunkRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.igetchunkrequest)`   
GetChunkRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.discoveryengine.v1alpha.GetChunkRequest;

Creates a GetChunkRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.getchunkrequest)` | GetChunkRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetChunkRequest

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

Converts this GetChunkRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.discoveryengine.v1alpha.GetChunkRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetChunkRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetChunkRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1alpha.getchunkrequest)`   
GetChunkRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetChunkRequest message.

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
