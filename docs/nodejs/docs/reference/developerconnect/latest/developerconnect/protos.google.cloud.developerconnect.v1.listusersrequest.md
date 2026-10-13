---
url: https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.listusersrequest
title: Class protos.google.cloud.developerconnect.v1.ListUsersRequest (0.9.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:05.141713+00:00
---

# Class protos.google.cloud.developerconnect.v1.ListUsersRequest (0.9.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.listusersrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.developerconnect.v1.ListUsersRequest (0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.5.0  0.3.1  0.2.0  0.1.0 

Represents a ListUsersRequest.

## Implements

[protos.google.cloud.developerconnect.v1.IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.ilistusersrequest)

## Package

[@google-cloud/developerconnect](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.developerconnect.v1.IListUsersRequest);

Constructs a new ListUsersRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.ilistusersrequest)`   
Properties to set  
  
## Properties 

### filter
    
    
    public filter: string;

ListUsersRequest filter.

### orderBy
    
    
    public orderBy: string;

ListUsersRequest orderBy.

### pageSize
    
    
    public pageSize: number;

ListUsersRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListUsersRequest pageToken.

### parent
    
    
    public parent: string;

ListUsersRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.developerconnect.v1.IListUsersRequest): google.cloud.developerconnect.v1.ListUsersRequest;

Creates a new ListUsersRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.ilistusersrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.listusersrequest)` | ListUsersRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.developerconnect.v1.ListUsersRequest;

Decodes a ListUsersRequest message from the specified reader or buffer.

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
`[ListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.listusersrequest)` | ListUsersRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.developerconnect.v1.ListUsersRequest;

Decodes a ListUsersRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.listusersrequest)` | ListUsersRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.developerconnect.v1.IListUsersRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListUsersRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.ilistusersrequest)`   
ListUsersRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.developerconnect.v1.IListUsersRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListUsersRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.ilistusersrequest)`   
ListUsersRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.developerconnect.v1.ListUsersRequest;

Creates a ListUsersRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.listusersrequest)` | ListUsersRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListUsersRequest

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

Converts this ListUsersRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.developerconnect.v1.ListUsersRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListUsersRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListUsersRequest](https://docs.cloud.google.com/nodejs/docs/reference/developerconnect/latest/developerconnect/protos.google.cloud.developerconnect.v1.listusersrequest)`   
ListUsersRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListUsersRequest message.

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
