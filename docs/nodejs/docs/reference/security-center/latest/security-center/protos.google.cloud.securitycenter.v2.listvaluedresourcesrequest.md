---
url: https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.listvaluedresourcesrequest
title: Class protos.google.cloud.securitycenter.v2.ListValuedResourcesRequest (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:22.457089+00:00
---

# Class protos.google.cloud.securitycenter.v2.ListValuedResourcesRequest (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.listvaluedresourcesrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.securitycenter.v2.ListValuedResourcesRequest (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  10.0.1  9.5.0  9.4.0  9.3.0  8.12.0  8.11.0  8.10.0  8.9.0  8.7.0  8.5.0  8.4.0  8.3.0  8.1.0  8.0.0  7.4.0  7.2.1  7.0.0  6.3.1  6.2.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.1  5.4.1  5.3.5 

Represents a ListValuedResourcesRequest.

## Implements

[protos.google.cloud.securitycenter.v2.IListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.ilistvaluedresourcesrequest)

## Package

[@google-cloud/security-center](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.securitycenter.v2.IListValuedResourcesRequest);

Constructs a new ListValuedResourcesRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.ilistvaluedresourcesrequest)`   
Properties to set  
  
## Properties 

### filter
    
    
    public filter: string;

ListValuedResourcesRequest filter.

### orderBy
    
    
    public orderBy: string;

ListValuedResourcesRequest orderBy.

### pageSize
    
    
    public pageSize: number;

ListValuedResourcesRequest pageSize.

### pageToken
    
    
    public pageToken: string;

ListValuedResourcesRequest pageToken.

### parent
    
    
    public parent: string;

ListValuedResourcesRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.securitycenter.v2.IListValuedResourcesRequest): google.cloud.securitycenter.v2.ListValuedResourcesRequest;

Creates a new ListValuedResourcesRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.ilistvaluedresourcesrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[ListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.listvaluedresourcesrequest)` | ListValuedResourcesRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.securitycenter.v2.ListValuedResourcesRequest;

Decodes a ListValuedResourcesRequest message from the specified reader or buffer.

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
`[ListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.listvaluedresourcesrequest)` | ListValuedResourcesRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.securitycenter.v2.ListValuedResourcesRequest;

Decodes a ListValuedResourcesRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[ListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.listvaluedresourcesrequest)` | ListValuedResourcesRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.securitycenter.v2.IListValuedResourcesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListValuedResourcesRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.ilistvaluedresourcesrequest)`   
ListValuedResourcesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.securitycenter.v2.IListValuedResourcesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified ListValuedResourcesRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.ilistvaluedresourcesrequest)`   
ListValuedResourcesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.securitycenter.v2.ListValuedResourcesRequest;

Creates a ListValuedResourcesRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[ListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.listvaluedresourcesrequest)` | ListValuedResourcesRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for ListValuedResourcesRequest

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

Converts this ListValuedResourcesRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.securitycenter.v2.ListValuedResourcesRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a ListValuedResourcesRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ListValuedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/security-center/latest/security-center/protos.google.cloud.securitycenter.v2.listvaluedresourcesrequest)`   
ListValuedResourcesRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a ListValuedResourcesRequest message.

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
