---
url: https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.listslatesrequest
title: Class protos.google.cloud.video.stitcher.v1.ListSlatesRequest (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:00:50.151706+00:00
---

# Class protos.google.cloud.video.stitcher.v1.ListSlatesRequest (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.listslatesrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.stitcher.v1.ListSlatesRequest (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.1.0  2.4.0  2.0.1  0.3.2  0.2.2  0.1.1 

Represents a ListSlatesRequest.

## Implements

[protos.google.cloud.video.stitcher.v1.IListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.ilistslatesrequest)

## Package

[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.video.stitcher.v1.IListSlatesRequest);

Constructs a new ListSlatesRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.ilistslatesrequest)`   
Properties to set  
  
## Properties 

### filter
    
    
    public filter: string;

ListSlatesRequest filter.

### orderBy
    
    
    public orderBy: string;

ListSlatesRequest orderBy.

### pageSize
    
    
    public pageSize: number;

ListSlatesRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListSlatesRequest pageToken.

### parent
    
    
    public parent: string;

ListSlatesRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.video.stitcher.v1.IListSlatesRequest): google.cloud.video.stitcher.v1.ListSlatesRequest;

Creates a new ListSlatesRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.ilistslatesrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.listslatesrequest)` | ListSlatesRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.video.stitcher.v1.ListSlatesRequest;

Decodes a ListSlatesRequest message from the specified reader or buffer.

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
`[ListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.listslatesrequest)` | ListSlatesRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.video.stitcher.v1.ListSlatesRequest;

Decodes a ListSlatesRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.listslatesrequest)` | ListSlatesRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.video.stitcher.v1.IListSlatesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListSlatesRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.ilistslatesrequest)`   
ListSlatesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.video.stitcher.v1.IListSlatesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListSlatesRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.ilistslatesrequest)`   
ListSlatesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.video.stitcher.v1.ListSlatesRequest;

Creates a ListSlatesRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.listslatesrequest)` | ListSlatesRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListSlatesRequest

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

Converts this ListSlatesRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.video.stitcher.v1.ListSlatesRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListSlatesRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListSlatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/protos.google.cloud.video.stitcher.v1.listslatesrequest)`   
ListSlatesRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListSlatesRequest message.

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
