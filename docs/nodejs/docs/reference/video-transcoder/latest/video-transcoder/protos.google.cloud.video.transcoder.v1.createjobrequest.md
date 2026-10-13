---
url: https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.createjobrequest
title: Class protos.google.cloud.video.transcoder.v1.CreateJobRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:21.972130+00:00
---

# Class protos.google.cloud.video.transcoder.v1.CreateJobRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.createjobrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.video.transcoder.v1.CreateJobRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.3  2.6.0  2.5.0  2.4.1  2.2.3  1.10.0  1.9.0  1.8.1  1.7.2  1.6.1  1.5.0  1.4.4 

Represents a CreateJobRequest.

## Implements

[protos.google.cloud.video.transcoder.v1.ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.icreatejobrequest)

## Package

[@google-cloud/video-transcoder](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.video.transcoder.v1.ICreateJobRequest);

Constructs a new CreateJobRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.icreatejobrequest)`   
Properties to set  
  
## Properties 

### job
    
    
    public job?: (google.cloud.video.transcoder.v1.IJob|null);

CreateJobRequest job.

### parent
    
    
    public parent: string;

CreateJobRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.video.transcoder.v1.ICreateJobRequest): google.cloud.video.transcoder.v1.CreateJobRequest;

Creates a new CreateJobRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.icreatejobrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.createjobrequest)` | CreateJobRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.video.transcoder.v1.CreateJobRequest;

Decodes a CreateJobRequest message from the specified reader or buffer.

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
`[CreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.createjobrequest)` | CreateJobRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.video.transcoder.v1.CreateJobRequest;

Decodes a CreateJobRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.createjobrequest)` | CreateJobRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.video.transcoder.v1.ICreateJobRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateJobRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.icreatejobrequest)`   
CreateJobRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.video.transcoder.v1.ICreateJobRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateJobRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.icreatejobrequest)`   
CreateJobRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.video.transcoder.v1.CreateJobRequest;

Creates a CreateJobRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.createjobrequest)` | CreateJobRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateJobRequest

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

Converts this CreateJobRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.video.transcoder.v1.CreateJobRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateJobRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/video-transcoder/latest/video-transcoder/protos.google.cloud.video.transcoder.v1.createjobrequest)`   
CreateJobRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateJobRequest message.

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
