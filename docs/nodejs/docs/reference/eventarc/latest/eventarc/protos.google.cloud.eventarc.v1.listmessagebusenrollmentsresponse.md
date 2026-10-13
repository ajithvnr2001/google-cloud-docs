---
url: https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusenrollmentsresponse
title: Class protos.google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:59:54.414325+00:00
---

# Class protos.google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusenrollmentsresponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.3.0  4.1.0  4.0.1  3.2.0  2.3.2  2.2.0  2.1.1  1.2.0  1.1.2  1.0.3 

Represents a ListMessageBusEnrollmentsResponse.

## Implements

[protos.google.cloud.eventarc.v1.IListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusenrollmentsresponse)

## Package

[@google-cloud/eventarc](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.eventarc.v1.IListMessageBusEnrollmentsResponse);

Constructs a new ListMessageBusEnrollmentsResponse.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusenrollmentsresponse)`   
Properties to set  
  
## Properties 

### enrollments
    
    
    public enrollments: string[];

ListMessageBusEnrollmentsResponse enrollments.

### nextPageToken
    
    
    public nextPageToken: string;

ListMessageBusEnrollmentsResponse nextPageToken.

### unreachable
    
    
    public unreachable: string[];

ListMessageBusEnrollmentsResponse unreachable.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.eventarc.v1.IListMessageBusEnrollmentsResponse): google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse;

Creates a new ListMessageBusEnrollmentsResponse instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusenrollmentsresponse)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusenrollmentsresponse)` | ListMessageBusEnrollmentsResponse instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse;

Decodes a ListMessageBusEnrollmentsResponse message from the specified reader or buffer.

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
`[ListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusenrollmentsresponse)` | ListMessageBusEnrollmentsResponse  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse;

Decodes a ListMessageBusEnrollmentsResponse message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusenrollmentsresponse)` | ListMessageBusEnrollmentsResponse  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.eventarc.v1.IListMessageBusEnrollmentsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListMessageBusEnrollmentsResponse message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusenrollmentsresponse)`   
ListMessageBusEnrollmentsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.eventarc.v1.IListMessageBusEnrollmentsResponse, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListMessageBusEnrollmentsResponse message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.ilistmessagebusenrollmentsresponse)`   
ListMessageBusEnrollmentsResponse message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse;

Creates a ListMessageBusEnrollmentsResponse message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusenrollmentsresponse)` | ListMessageBusEnrollmentsResponse  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListMessageBusEnrollmentsResponse

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

Converts this ListMessageBusEnrollmentsResponse to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.eventarc.v1.ListMessageBusEnrollmentsResponse, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListMessageBusEnrollmentsResponse message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListMessageBusEnrollmentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/eventarc/latest/eventarc/protos.google.cloud.eventarc.v1.listmessagebusenrollmentsresponse)`   
ListMessageBusEnrollmentsResponse  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListMessageBusEnrollmentsResponse message.

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
