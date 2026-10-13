---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitworkspacechangesrequest
title: Class protos.google.cloud.dataform.v1.CommitWorkspaceChangesRequest (3.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:43:12.507195+00:00
---

# Class protos.google.cloud.dataform.v1.CommitWorkspaceChangesRequest (3.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitworkspacechangesrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataform.v1.CommitWorkspaceChangesRequest (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.4.0 (latest)  3.3.1  2.5.0  2.4.0  2.1.0  1.4.0  1.0.2  0.4.2  0.2.0  0.1.0 

Represents a CommitWorkspaceChangesRequest.

## Implements

[protos.google.cloud.dataform.v1.ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitworkspacechangesrequest)

## Package

[@google-cloud/dataform](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.dataform.v1.ICommitWorkspaceChangesRequest);

Constructs a new CommitWorkspaceChangesRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitworkspacechangesrequest)`   
Properties to set  
  
## Properties 

### author
    
    
    public author?: (google.cloud.dataform.v1.ICommitAuthor|null);

CommitWorkspaceChangesRequest author.

### commitMessage
    
    
    public commitMessage: string;

CommitWorkspaceChangesRequest commitMessage.

### name
    
    
    public name: string;

CommitWorkspaceChangesRequest name.

### paths
    
    
    public paths: string[];

CommitWorkspaceChangesRequest paths.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.dataform.v1.ICommitWorkspaceChangesRequest): google.cloud.dataform.v1.CommitWorkspaceChangesRequest;

Creates a new CommitWorkspaceChangesRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitworkspacechangesrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitworkspacechangesrequest)` | CommitWorkspaceChangesRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.dataform.v1.CommitWorkspaceChangesRequest;

Decodes a CommitWorkspaceChangesRequest message from the specified reader or buffer.

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
`[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitworkspacechangesrequest)` | CommitWorkspaceChangesRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.dataform.v1.CommitWorkspaceChangesRequest;

Decodes a CommitWorkspaceChangesRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitworkspacechangesrequest)` | CommitWorkspaceChangesRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.dataform.v1.ICommitWorkspaceChangesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CommitWorkspaceChangesRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitworkspacechangesrequest)`   
CommitWorkspaceChangesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.dataform.v1.ICommitWorkspaceChangesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CommitWorkspaceChangesRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.icommitworkspacechangesrequest)`   
CommitWorkspaceChangesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.dataform.v1.CommitWorkspaceChangesRequest;

Creates a CommitWorkspaceChangesRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitworkspacechangesrequest)` | CommitWorkspaceChangesRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CommitWorkspaceChangesRequest

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

Converts this CommitWorkspaceChangesRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.dataform.v1.CommitWorkspaceChangesRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CommitWorkspaceChangesRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CommitWorkspaceChangesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataform/latest/dataform/protos.google.cloud.dataform.v1.commitworkspacechangesrequest)`   
CommitWorkspaceChangesRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CommitWorkspaceChangesRequest message.

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
