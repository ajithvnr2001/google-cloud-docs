---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listhostprojectregistrationsrequest
title: Class protos.google.cloud.apihub.v1.ListHostProjectRegistrationsRequest (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:07.199706+00:00
---

# Class protos.google.cloud.apihub.v1.ListHostProjectRegistrationsRequest (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listhostprojectregistrationsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.ListHostProjectRegistrationsRequest (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a ListHostProjectRegistrationsRequest.

## Implements

[protos.google.cloud.apihub.v1.IListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilisthostprojectregistrationsrequest)

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.apihub.v1.IListHostProjectRegistrationsRequest);

Constructs a new ListHostProjectRegistrationsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilisthostprojectregistrationsrequest)`   
Properties to set  
  
## Properties 

### filter
    
    
    public filter: string;

ListHostProjectRegistrationsRequest filter.

### orderBy
    
    
    public orderBy: string;

ListHostProjectRegistrationsRequest orderBy.

### pageSize
    
    
    public pageSize: number;

ListHostProjectRegistrationsRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListHostProjectRegistrationsRequest pageToken.

### parent
    
    
    public parent: string;

ListHostProjectRegistrationsRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.apihub.v1.IListHostProjectRegistrationsRequest): google.cloud.apihub.v1.ListHostProjectRegistrationsRequest;

Creates a new ListHostProjectRegistrationsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilisthostprojectregistrationsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listhostprojectregistrationsrequest)` | ListHostProjectRegistrationsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.apihub.v1.ListHostProjectRegistrationsRequest;

Decodes a ListHostProjectRegistrationsRequest message from the specified reader or buffer.

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
`[ListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listhostprojectregistrationsrequest)` | ListHostProjectRegistrationsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.apihub.v1.ListHostProjectRegistrationsRequest;

Decodes a ListHostProjectRegistrationsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listhostprojectregistrationsrequest)` | ListHostProjectRegistrationsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.apihub.v1.IListHostProjectRegistrationsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListHostProjectRegistrationsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilisthostprojectregistrationsrequest)`   
ListHostProjectRegistrationsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.apihub.v1.IListHostProjectRegistrationsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListHostProjectRegistrationsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilisthostprojectregistrationsrequest)`   
ListHostProjectRegistrationsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.apihub.v1.ListHostProjectRegistrationsRequest;

Creates a ListHostProjectRegistrationsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listhostprojectregistrationsrequest)` | ListHostProjectRegistrationsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListHostProjectRegistrationsRequest

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

Converts this ListHostProjectRegistrationsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.apihub.v1.ListHostProjectRegistrationsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListHostProjectRegistrationsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listhostprojectregistrationsrequest)`   
ListHostProjectRegistrationsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListHostProjectRegistrationsRequest message.

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
