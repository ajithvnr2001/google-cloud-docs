---
url: https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.listtranscriptentriesresponse
title: Class protos.google.apps.meet.v2beta.ListTranscriptEntriesResponse (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:43.791054+00:00
---

# Class protos.google.apps.meet.v2beta.ListTranscriptEntriesResponse (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.listtranscriptentriesresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.apps.meet.v2beta.ListTranscriptEntriesResponse (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.9.0  0.4.0  0.2.0 

Represents a ListTranscriptEntriesResponse.

## Implements

[protos.google.apps.meet.v2beta.IListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.ilisttranscriptentriesresponse)

## Package

[@google-apps/meet](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.apps.meet.v2beta.IListTranscriptEntriesResponse);

Constructs a new ListTranscriptEntriesResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.ilisttranscriptentriesresponse)`   
Properties to set  
  
## Properties 

### nextPageToken
    
    
    public nextPageToken: string;

ListTranscriptEntriesResponse nextPageToken.

### transcriptEntries
    
    
    public transcriptEntries: google.apps.meet.v2beta.ITranscriptEntry[];

ListTranscriptEntriesResponse transcriptEntries.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.apps.meet.v2beta.IListTranscriptEntriesResponse): google.apps.meet.v2beta.ListTranscriptEntriesResponse;

Creates a new ListTranscriptEntriesResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.ilisttranscriptentriesresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.listtranscriptentriesresponse)` | ListTranscriptEntriesResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.apps.meet.v2beta.ListTranscriptEntriesResponse;

Decodes a ListTranscriptEntriesResponse message from the specified reader or buffer.

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
`[ListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.listtranscriptentriesresponse)` | ListTranscriptEntriesResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.apps.meet.v2beta.ListTranscriptEntriesResponse;

Decodes a ListTranscriptEntriesResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.listtranscriptentriesresponse)` | ListTranscriptEntriesResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.apps.meet.v2beta.IListTranscriptEntriesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListTranscriptEntriesResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.ilisttranscriptentriesresponse)`   
ListTranscriptEntriesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.apps.meet.v2beta.IListTranscriptEntriesResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListTranscriptEntriesResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.ilisttranscriptentriesresponse)`   
ListTranscriptEntriesResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.apps.meet.v2beta.ListTranscriptEntriesResponse;

Creates a ListTranscriptEntriesResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.listtranscriptentriesresponse)` | ListTranscriptEntriesResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListTranscriptEntriesResponse

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

Converts this ListTranscriptEntriesResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.apps.meet.v2beta.ListTranscriptEntriesResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListTranscriptEntriesResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListTranscriptEntriesResponse](https://docs.cloud.google.com/nodejs/docs/reference/meet/latest/meet/protos.google.apps.meet.v2beta.listtranscriptentriesresponse)`   
ListTranscriptEntriesResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListTranscriptEntriesResponse message.

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
