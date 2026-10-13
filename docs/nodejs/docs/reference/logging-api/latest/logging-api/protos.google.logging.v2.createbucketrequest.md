---
url: https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.createbucketrequest
title: Class protos.google.logging.v2.CreateBucketRequest (0.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:30.582421+00:00
---

# Class protos.google.logging.v2.CreateBucketRequest (0.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.createbucketrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.logging.v2.CreateBucketRequest (0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a CreateBucketRequest.

## Implements

[protos.google.logging.v2.ICreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.icreatebucketrequest)

## Package

[@google-cloud/logging-api](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.logging.v2.ICreateBucketRequest);

Constructs a new CreateBucketRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.icreatebucketrequest)`   
Properties to set  
  
## Properties 

### bucket
    
    
    public bucket?: (google.logging.v2.ILogBucket|null);

CreateBucketRequest bucket.

### bucketId
    
    
    public bucketId: string;

CreateBucketRequest bucketId.

### parent
    
    
    public parent: string;

CreateBucketRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.logging.v2.ICreateBucketRequest): google.logging.v2.CreateBucketRequest;

Creates a new CreateBucketRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.icreatebucketrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.createbucketrequest)` | CreateBucketRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.logging.v2.CreateBucketRequest;

Decodes a CreateBucketRequest message from the specified reader or buffer.

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
`[CreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.createbucketrequest)` | CreateBucketRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.logging.v2.CreateBucketRequest;

Decodes a CreateBucketRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.createbucketrequest)` | CreateBucketRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.logging.v2.ICreateBucketRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateBucketRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.icreatebucketrequest)`   
CreateBucketRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.logging.v2.ICreateBucketRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateBucketRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.icreatebucketrequest)`   
CreateBucketRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.logging.v2.CreateBucketRequest;

Creates a CreateBucketRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.createbucketrequest)` | CreateBucketRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateBucketRequest

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

Converts this CreateBucketRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.logging.v2.CreateBucketRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateBucketRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateBucketRequest](https://docs.cloud.google.com/nodejs/docs/reference/logging-api/latest/logging-api/protos.google.logging.v2.createbucketrequest)`   
CreateBucketRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateBucketRequest message.

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

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
