---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivatecmsmetadatavaluesrequest
title: Class protos.google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:18:58.334898+00:00
---

# Class protos.google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivatecmsmetadatavaluesrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents a BatchActivateCmsMetadataValuesRequest.

## Implements

[protos.google.ads.admanager.v1.IBatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivatecmsmetadatavaluesrequest)

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.ads.admanager.v1.IBatchActivateCmsMetadataValuesRequest);

Constructs a new BatchActivateCmsMetadataValuesRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivatecmsmetadatavaluesrequest)`   
Properties to set  
  
## Properties 

### names
    
    
    public names: string[];

BatchActivateCmsMetadataValuesRequest names.

### parent
    
    
    public parent: string;

BatchActivateCmsMetadataValuesRequest parent.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.ads.admanager.v1.IBatchActivateCmsMetadataValuesRequest): google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest;

Creates a new BatchActivateCmsMetadataValuesRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivatecmsmetadatavaluesrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivatecmsmetadatavaluesrequest)` | BatchActivateCmsMetadataValuesRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest;

Decodes a BatchActivateCmsMetadataValuesRequest message from the specified reader or buffer.

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
`[BatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivatecmsmetadatavaluesrequest)` | BatchActivateCmsMetadataValuesRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest;

Decodes a BatchActivateCmsMetadataValuesRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivatecmsmetadatavaluesrequest)` | BatchActivateCmsMetadataValuesRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.ads.admanager.v1.IBatchActivateCmsMetadataValuesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchActivateCmsMetadataValuesRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivatecmsmetadatavaluesrequest)`   
BatchActivateCmsMetadataValuesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.ads.admanager.v1.IBatchActivateCmsMetadataValuesRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchActivateCmsMetadataValuesRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchactivatecmsmetadatavaluesrequest)`   
BatchActivateCmsMetadataValuesRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest;

Creates a BatchActivateCmsMetadataValuesRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivatecmsmetadatavaluesrequest)` | BatchActivateCmsMetadataValuesRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BatchActivateCmsMetadataValuesRequest

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

Converts this BatchActivateCmsMetadataValuesRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.ads.admanager.v1.BatchActivateCmsMetadataValuesRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BatchActivateCmsMetadataValuesRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BatchActivateCmsMetadataValuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchactivatecmsmetadatavaluesrequest)`   
BatchActivateCmsMetadataValuesRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BatchActivateCmsMetadataValuesRequest message.

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
