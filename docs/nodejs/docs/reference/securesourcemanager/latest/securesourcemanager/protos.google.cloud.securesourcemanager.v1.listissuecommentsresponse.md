---
url: https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.listissuecommentsresponse
title: Class protos.google.cloud.securesourcemanager.v1.ListIssueCommentsResponse (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:52.041813+00:00
---

# Class protos.google.cloud.securesourcemanager.v1.ListIssueCommentsResponse (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.listissuecommentsresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.securesourcemanager.v1.ListIssueCommentsResponse (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.11.0  0.10.0  0.1.0 

Represents a ListIssueCommentsResponse.

## Implements

[protos.google.cloud.securesourcemanager.v1.IListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.ilistissuecommentsresponse)

## Package

[@google-cloud/securesourcemanager](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.securesourcemanager.v1.IListIssueCommentsResponse);

Constructs a new ListIssueCommentsResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.ilistissuecommentsresponse)`   
Properties to set  
  
## Properties 

### issueComments
    
    
    public issueComments: google.cloud.securesourcemanager.v1.IIssueComment[];

ListIssueCommentsResponse issueComments.

### nextPageToken
    
    
    public nextPageToken: string;

ListIssueCommentsResponse nextPageToken.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.securesourcemanager.v1.IListIssueCommentsResponse): google.cloud.securesourcemanager.v1.ListIssueCommentsResponse;

Creates a new ListIssueCommentsResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.ilistissuecommentsresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.listissuecommentsresponse)` | ListIssueCommentsResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.securesourcemanager.v1.ListIssueCommentsResponse;

Decodes a ListIssueCommentsResponse message from the specified reader or buffer.

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
`[ListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.listissuecommentsresponse)` | ListIssueCommentsResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.securesourcemanager.v1.ListIssueCommentsResponse;

Decodes a ListIssueCommentsResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.listissuecommentsresponse)` | ListIssueCommentsResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.securesourcemanager.v1.IListIssueCommentsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListIssueCommentsResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.ilistissuecommentsresponse)`   
ListIssueCommentsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.securesourcemanager.v1.IListIssueCommentsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListIssueCommentsResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.ilistissuecommentsresponse)`   
ListIssueCommentsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.securesourcemanager.v1.ListIssueCommentsResponse;

Creates a ListIssueCommentsResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.listissuecommentsresponse)` | ListIssueCommentsResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListIssueCommentsResponse

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

Converts this ListIssueCommentsResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.securesourcemanager.v1.ListIssueCommentsResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListIssueCommentsResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListIssueCommentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/securesourcemanager/latest/securesourcemanager/protos.google.cloud.securesourcemanager.v1.listissuecommentsresponse)`   
ListIssueCommentsResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListIssueCommentsResponse message.

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
