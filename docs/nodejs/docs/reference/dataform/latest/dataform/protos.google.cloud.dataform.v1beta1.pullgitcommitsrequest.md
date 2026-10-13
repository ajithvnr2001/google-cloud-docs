---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pullgitcommitsrequest
title: Class protos.google.cloud.dataform.v1beta1.PullGitCommitsRequest (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:09.253597+00:00
---

# Class protos.google.cloud.dataform.v1beta1.PullGitCommitsRequest (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pullgitcommitsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1beta1.PullGitCommitsRequest (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents a PullGitCommitsRequest.

## Implements

[protos.google.cloud.dataform.v1beta1.IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest)

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataform.v1beta1.IPullGitCommitsRequest);

Constructs a new PullGitCommitsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest)`   
Properties to set  
  
## Properties 

### author
    
    
    public author?: (google.cloud.dataform.v1beta1.ICommitAuthor|null);

PullGitCommitsRequest author.

### name
    
    
    public name: string;

PullGitCommitsRequest name.

### remoteBranch
    
    
    public remoteBranch: string;

PullGitCommitsRequest remoteBranch.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataform.v1beta1.IPullGitCommitsRequest): google.cloud.dataform.v1beta1.PullGitCommitsRequest;

Creates a new PullGitCommitsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[PullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pullgitcommitsrequest)` | PullGitCommitsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataform.v1beta1.PullGitCommitsRequest;

Decodes a PullGitCommitsRequest message from the specified reader or buffer.

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
`[PullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pullgitcommitsrequest)` | PullGitCommitsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataform.v1beta1.PullGitCommitsRequest;

Decodes a PullGitCommitsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[PullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pullgitcommitsrequest)` | PullGitCommitsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataform.v1beta1.IPullGitCommitsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PullGitCommitsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest)`   
PullGitCommitsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataform.v1beta1.IPullGitCommitsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified PullGitCommitsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IPullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.ipullgitcommitsrequest)`   
PullGitCommitsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataform.v1beta1.PullGitCommitsRequest;

Creates a PullGitCommitsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[PullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pullgitcommitsrequest)` | PullGitCommitsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for PullGitCommitsRequest

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

Converts this PullGitCommitsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataform.v1beta1.PullGitCommitsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a PullGitCommitsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[PullGitCommitsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1beta1.pullgitcommitsrequest)`   
PullGitCommitsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a PullGitCommitsRequest message.

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
