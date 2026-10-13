---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchupdategenerativequestionconfigsrequest
title: Class protos.google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:06.011499+00:00
---

# Class protos.google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchupdategenerativequestionconfigsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a BatchUpdateGenerativeQuestionConfigsRequest.

## Implements

[protos.google.cloud.retail.v2beta.IBatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchupdategenerativequestionconfigsrequest)

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.retail.v2beta.IBatchUpdateGenerativeQuestionConfigsRequest);

Constructs a new BatchUpdateGenerativeQuestionConfigsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchupdategenerativequestionconfigsrequest)`   
Properties to set  
  
## Properties 

### parent
    
    
    public parent: string;

BatchUpdateGenerativeQuestionConfigsRequest parent.

### requests
    
    
    public requests: google.cloud.retail.v2beta.IUpdateGenerativeQuestionConfigRequest[];

BatchUpdateGenerativeQuestionConfigsRequest requests.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.retail.v2beta.IBatchUpdateGenerativeQuestionConfigsRequest): google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest;

Creates a new BatchUpdateGenerativeQuestionConfigsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IBatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchupdategenerativequestionconfigsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchupdategenerativequestionconfigsrequest)` | BatchUpdateGenerativeQuestionConfigsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest;

Decodes a BatchUpdateGenerativeQuestionConfigsRequest message from the specified reader or buffer.

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
`[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchupdategenerativequestionconfigsrequest)` | BatchUpdateGenerativeQuestionConfigsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest;

Decodes a BatchUpdateGenerativeQuestionConfigsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchupdategenerativequestionconfigsrequest)` | BatchUpdateGenerativeQuestionConfigsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.retail.v2beta.IBatchUpdateGenerativeQuestionConfigsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchUpdateGenerativeQuestionConfigsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchupdategenerativequestionconfigsrequest)`   
BatchUpdateGenerativeQuestionConfigsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.retail.v2beta.IBatchUpdateGenerativeQuestionConfigsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified BatchUpdateGenerativeQuestionConfigsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IBatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.ibatchupdategenerativequestionconfigsrequest)`   
BatchUpdateGenerativeQuestionConfigsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest;

Creates a BatchUpdateGenerativeQuestionConfigsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchupdategenerativequestionconfigsrequest)` | BatchUpdateGenerativeQuestionConfigsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for BatchUpdateGenerativeQuestionConfigsRequest

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

Converts this BatchUpdateGenerativeQuestionConfigsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.retail.v2beta.BatchUpdateGenerativeQuestionConfigsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a BatchUpdateGenerativeQuestionConfigsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[BatchUpdateGenerativeQuestionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.batchupdategenerativequestionconfigsrequest)`   
BatchUpdateGenerativeQuestionConfigsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a BatchUpdateGenerativeQuestionConfigsRequest message.

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
