---
url: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.liststoredinfotypesresponse
title: Class protos.google.privacy.dlp.v2.ListStoredInfoTypesResponse (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:27.292635+00:00
---

# Class protos.google.privacy.dlp.v2.ListStoredInfoTypesResponse (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.liststoredinfotypesresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.privacy.dlp.v2.ListStoredInfoTypesResponse (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  7.0.1  6.6.0  6.2.0  6.1.0  5.13.0  5.11.0  5.10.0  5.7.0  5.5.0  5.3.0  5.0.0  4.4.2  4.2.0  4.1.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.8 

Represents a ListStoredInfoTypesResponse.

## Implements

[protos.google.privacy.dlp.v2.IListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.iliststoredinfotypesresponse)

## Package

[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.privacy.dlp.v2.IListStoredInfoTypesResponse);

Constructs a new ListStoredInfoTypesResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.iliststoredinfotypesresponse)`   
Properties to set  
  
## Properties 

### nextPageToken
    
    
    public nextPageToken: string;

ListStoredInfoTypesResponse nextPageToken.

### storedInfoTypes
    
    
    public storedInfoTypes: google.privacy.dlp.v2.IStoredInfoType[];

ListStoredInfoTypesResponse storedInfoTypes.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.privacy.dlp.v2.IListStoredInfoTypesResponse): google.privacy.dlp.v2.ListStoredInfoTypesResponse;

Creates a new ListStoredInfoTypesResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.iliststoredinfotypesresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.liststoredinfotypesresponse)` | ListStoredInfoTypesResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.privacy.dlp.v2.ListStoredInfoTypesResponse;

Decodes a ListStoredInfoTypesResponse message from the specified reader or buffer.

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
`[ListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.liststoredinfotypesresponse)` | ListStoredInfoTypesResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.privacy.dlp.v2.ListStoredInfoTypesResponse;

Decodes a ListStoredInfoTypesResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.liststoredinfotypesresponse)` | ListStoredInfoTypesResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.privacy.dlp.v2.IListStoredInfoTypesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListStoredInfoTypesResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.iliststoredinfotypesresponse)`   
ListStoredInfoTypesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.privacy.dlp.v2.IListStoredInfoTypesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListStoredInfoTypesResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.iliststoredinfotypesresponse)`   
ListStoredInfoTypesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.privacy.dlp.v2.ListStoredInfoTypesResponse;

Creates a ListStoredInfoTypesResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.liststoredinfotypesresponse)` | ListStoredInfoTypesResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListStoredInfoTypesResponse

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

Converts this ListStoredInfoTypesResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.privacy.dlp.v2.ListStoredInfoTypesResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListStoredInfoTypesResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListStoredInfoTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.liststoredinfotypesresponse)`   
ListStoredInfoTypesResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListStoredInfoTypesResponse message.

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
