---
url: https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.listfoldersrequest
title: Class protos.google.cloud.resourcemanager.v3.ListFoldersRequest (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:12:10.739431+00:00
---

# Class protos.google.cloud.resourcemanager.v3.ListFoldersRequest (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.listfoldersrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.resourcemanager.v3.ListFoldersRequest (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.3.0  6.1.0  4.3.0  4.2.1  4.1.3  3.2.0  3.1.0  3.0.0  2.0.1 

Represents a ListFoldersRequest.

## Implements

[protos.google.cloud.resourcemanager.v3.IListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ilistfoldersrequest)

## Package

[@google-cloud/resource-manager](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.resourcemanager.v3.IListFoldersRequest);

Constructs a new ListFoldersRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ilistfoldersrequest)`   
Properties to set  
  
## Properties 

### pageSize
    
    
    public pageSize: number;

ListFoldersRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListFoldersRequest pageToken.

### parent
    
    
    public parent: string;

ListFoldersRequest parent.

### showDeleted
    
    
    public showDeleted: boolean;

ListFoldersRequest showDeleted.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.resourcemanager.v3.IListFoldersRequest): google.cloud.resourcemanager.v3.ListFoldersRequest;

Creates a new ListFoldersRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ilistfoldersrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.listfoldersrequest)` | ListFoldersRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.resourcemanager.v3.ListFoldersRequest;

Decodes a ListFoldersRequest message from the specified reader or buffer.

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
`[ListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.listfoldersrequest)` | ListFoldersRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.resourcemanager.v3.ListFoldersRequest;

Decodes a ListFoldersRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.listfoldersrequest)` | ListFoldersRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.resourcemanager.v3.IListFoldersRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListFoldersRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ilistfoldersrequest)`   
ListFoldersRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.resourcemanager.v3.IListFoldersRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListFoldersRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.ilistfoldersrequest)`   
ListFoldersRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.resourcemanager.v3.ListFoldersRequest;

Creates a ListFoldersRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.listfoldersrequest)` | ListFoldersRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListFoldersRequest

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

Converts this ListFoldersRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.resourcemanager.v3.ListFoldersRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListFoldersRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListFoldersRequest](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/resource-manager/protos.google.cloud.resourcemanager.v3.listfoldersrequest)`   
ListFoldersRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListFoldersRequest message.

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
