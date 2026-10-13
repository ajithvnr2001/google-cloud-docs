---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.changerequest-class
title: Class protos.google.cloud.dataplex.v1.ChangeRequest (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:25.098183+00:00
---

# Class protos.google.cloud.dataplex.v1.ChangeRequest (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.changerequest-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.ChangeRequest (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a ChangeRequest.

## Implements

[protos.google.cloud.dataplex.v1.IChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ichangerequest)

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataplex.v1.IChangeRequest);

Constructs a new ChangeRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ichangerequest)`   
Properties to set  
  
## Properties 

### approver
    
    
    public approver: string;

ChangeRequest approver.

### author
    
    
    public author: string;

ChangeRequest author.

### changePayload
    
    
    public changePayload?: ("createEntry"|"updateEntry"|"deleteEntry"|"createEntryLink"|"deleteEntryLink"|"createGlossary"|"updateGlossary"|"deleteGlossary"|"createGlossaryCategory"|"updateGlossaryCategory"|"deleteGlossaryCategory"|"createGlossaryTerm"|"updateGlossaryTerm"|"deleteGlossaryTerm"|"dataProductAccessRequest");

ChangeRequest changePayload.

### changeType
    
    
    public changeType: (google.cloud.dataplex.v1.ChangeRequest.ChangeType|keyof typeof google.cloud.dataplex.v1.ChangeRequest.ChangeType);

ChangeRequest changeType.

### createEntry
    
    
    public createEntry?: (google.cloud.dataplex.v1.ICreateEntryRequest|null);

ChangeRequest createEntry.

### createEntryLink
    
    
    public createEntryLink?: (google.cloud.dataplex.v1.ICreateEntryLinkRequest|null);

ChangeRequest createEntryLink.

### createGlossary
    
    
    public createGlossary?: (google.cloud.dataplex.v1.ICreateGlossaryRequest|null);

ChangeRequest createGlossary.

### createGlossaryCategory
    
    
    public createGlossaryCategory?: (google.cloud.dataplex.v1.ICreateGlossaryCategoryRequest|null);

ChangeRequest createGlossaryCategory.

### createGlossaryTerm
    
    
    public createGlossaryTerm?: (google.cloud.dataplex.v1.ICreateGlossaryTermRequest|null);

ChangeRequest createGlossaryTerm.

### createTime
    
    
    public createTime?: (google.protobuf.ITimestamp|null);

ChangeRequest createTime.

### dataProductAccessRequest
    
    
    public dataProductAccessRequest?: (google.cloud.dataplex.v1.IDataProductAccessRequest|null);

ChangeRequest dataProductAccessRequest.

### deleteEntry
    
    
    public deleteEntry?: (google.cloud.dataplex.v1.IDeleteEntryRequest|null);

ChangeRequest deleteEntry.

### deleteEntryLink
    
    
    public deleteEntryLink?: (google.cloud.dataplex.v1.IDeleteEntryLinkRequest|null);

ChangeRequest deleteEntryLink.

### deleteGlossary
    
    
    public deleteGlossary?: (google.cloud.dataplex.v1.IDeleteGlossaryRequest|null);

ChangeRequest deleteGlossary.

### deleteGlossaryCategory
    
    
    public deleteGlossaryCategory?: (google.cloud.dataplex.v1.IDeleteGlossaryCategoryRequest|null);

ChangeRequest deleteGlossaryCategory.

### deleteGlossaryTerm
    
    
    public deleteGlossaryTerm?: (google.cloud.dataplex.v1.IDeleteGlossaryTermRequest|null);

ChangeRequest deleteGlossaryTerm.

### etag
    
    
    public etag: string;

ChangeRequest etag.

### justification
    
    
    public justification: string;

ChangeRequest justification.

### labels
    
    
    public labels: { [k: string]: string };

ChangeRequest labels.

### name
    
    
    public name: string;

ChangeRequest name.

### rejectionComment
    
    
    public rejectionComment: string;

ChangeRequest rejectionComment.

### resource
    
    
    public resource: string;

ChangeRequest resource.

### state
    
    
    public state: (google.cloud.dataplex.v1.ChangeRequest.State|keyof typeof google.cloud.dataplex.v1.ChangeRequest.State);

ChangeRequest state.

### uid
    
    
    public uid: string;

ChangeRequest uid.

### updateEntry
    
    
    public updateEntry?: (google.cloud.dataplex.v1.IUpdateEntryRequest|null);

ChangeRequest updateEntry.

### updateGlossary
    
    
    public updateGlossary?: (google.cloud.dataplex.v1.IUpdateGlossaryRequest|null);

ChangeRequest updateGlossary.

### updateGlossaryCategory
    
    
    public updateGlossaryCategory?: (google.cloud.dataplex.v1.IUpdateGlossaryCategoryRequest|null);

ChangeRequest updateGlossaryCategory.

### updateGlossaryTerm
    
    
    public updateGlossaryTerm?: (google.cloud.dataplex.v1.IUpdateGlossaryTermRequest|null);

ChangeRequest updateGlossaryTerm.

### updateTime
    
    
    public updateTime?: (google.protobuf.ITimestamp|null);

ChangeRequest updateTime.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataplex.v1.IChangeRequest): google.cloud.dataplex.v1.ChangeRequest;

Creates a new ChangeRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ichangerequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.changerequest-class)` | ChangeRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataplex.v1.ChangeRequest;

Decodes a ChangeRequest message from the specified reader or buffer.

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
`[ChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.changerequest-class)` | ChangeRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataplex.v1.ChangeRequest;

Decodes a ChangeRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.changerequest-class)` | ChangeRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataplex.v1.IChangeRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ChangeRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ichangerequest)`   
ChangeRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataplex.v1.IChangeRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ChangeRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ichangerequest)`   
ChangeRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataplex.v1.ChangeRequest;

Creates a ChangeRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.changerequest-class)` | ChangeRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ChangeRequest

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

Converts this ChangeRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataplex.v1.ChangeRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ChangeRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ChangeRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.changerequest-class)`   
ChangeRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ChangeRequest message.

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
