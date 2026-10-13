---
url: https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.listjobsrequest
title: Class protos.google.cloud.talent.v4beta1.ListJobsRequest (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:10.380347+00:00
---

# Class protos.google.cloud.talent.v4beta1.ListJobsRequest (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.listjobsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.talent.v4beta1.ListJobsRequest (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.2.0  6.4.0  6.3.1  6.0.2  5.1.3  5.0.1  4.1.1  3.5.1  3.4.1  3.3.0  3.2.7 

Represents a ListJobsRequest.

## Implements

[protos.google.cloud.talent.v4beta1.IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ilistjobsrequest)

## Package

[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.talent.v4beta1.IListJobsRequest);

Constructs a new ListJobsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ilistjobsrequest)`   
Properties to set  
  
## Properties 

### filter
    
    
    public filter: string;

ListJobsRequest filter.

### jobView
    
    
    public jobView: (google.cloud.talent.v4beta1.JobView|keyof typeof google.cloud.talent.v4beta1.JobView);

ListJobsRequest jobView.

### pageSize
    
    
    public pageSize: number;

ListJobsRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListJobsRequest pageToken.

### parent
    
    
    public parent: string;

ListJobsRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.talent.v4beta1.IListJobsRequest): google.cloud.talent.v4beta1.ListJobsRequest;

Creates a new ListJobsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ilistjobsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.listjobsrequest)` | ListJobsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.talent.v4beta1.ListJobsRequest;

Decodes a ListJobsRequest message from the specified reader or buffer.

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
`[ListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.listjobsrequest)` | ListJobsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.talent.v4beta1.ListJobsRequest;

Decodes a ListJobsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.listjobsrequest)` | ListJobsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.talent.v4beta1.IListJobsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListJobsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ilistjobsrequest)`   
ListJobsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.talent.v4beta1.IListJobsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListJobsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.ilistjobsrequest)`   
ListJobsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.talent.v4beta1.ListJobsRequest;

Creates a ListJobsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.listjobsrequest)` | ListJobsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListJobsRequest

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

Converts this ListJobsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.talent.v4beta1.ListJobsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListJobsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4beta1.listjobsrequest)`   
ListJobsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListJobsRequest message.

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
