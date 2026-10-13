---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.getjobexecutiondetailsrequest
title: Class protos.google.dataflow.v1beta3.GetJobExecutionDetailsRequest (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:07.194467+00:00
---

# Class protos.google.dataflow.v1beta3.GetJobExecutionDetailsRequest (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.getjobexecutiondetailsrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.dataflow.v1beta3.GetJobExecutionDetailsRequest (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.0.2  2.1.2  2.0.1  1.2.0  1.1.0  1.0.2 

Represents a GetJobExecutionDetailsRequest.

## Implements

[protos.google.dataflow.v1beta3.IGetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.igetjobexecutiondetailsrequest)

## Package

[@google-cloud/dataflow](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.dataflow.v1beta3.IGetJobExecutionDetailsRequest);

Constructs a new GetJobExecutionDetailsRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.igetjobexecutiondetailsrequest)`   
Properties to set  
  
## Properties 

### jobId
    
    
    public jobId: string;

GetJobExecutionDetailsRequest jobId.

### location
    
    
    public location: string;

GetJobExecutionDetailsRequest location.

### pageSize
    
    
    public pageSize: number;

GetJobExecutionDetailsRequest pageSize.

### pageToken
    
    
    public pageToken: string;

GetJobExecutionDetailsRequest pageToken.

### projectId
    
    
    public projectId: string;

GetJobExecutionDetailsRequest projectId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.dataflow.v1beta3.IGetJobExecutionDetailsRequest): google.dataflow.v1beta3.GetJobExecutionDetailsRequest;

Creates a new GetJobExecutionDetailsRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IGetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.igetjobexecutiondetailsrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[GetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.getjobexecutiondetailsrequest)` | GetJobExecutionDetailsRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.dataflow.v1beta3.GetJobExecutionDetailsRequest;

Decodes a GetJobExecutionDetailsRequest message from the specified reader or buffer.

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
`[GetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.getjobexecutiondetailsrequest)` | GetJobExecutionDetailsRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.dataflow.v1beta3.GetJobExecutionDetailsRequest;

Decodes a GetJobExecutionDetailsRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[GetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.getjobexecutiondetailsrequest)` | GetJobExecutionDetailsRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.dataflow.v1beta3.IGetJobExecutionDetailsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetJobExecutionDetailsRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.igetjobexecutiondetailsrequest)`   
GetJobExecutionDetailsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.dataflow.v1beta3.IGetJobExecutionDetailsRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified GetJobExecutionDetailsRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IGetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.igetjobexecutiondetailsrequest)`   
GetJobExecutionDetailsRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.dataflow.v1beta3.GetJobExecutionDetailsRequest;

Creates a GetJobExecutionDetailsRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[GetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.getjobexecutiondetailsrequest)` | GetJobExecutionDetailsRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for GetJobExecutionDetailsRequest

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

Converts this GetJobExecutionDetailsRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.dataflow.v1beta3.GetJobExecutionDetailsRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a GetJobExecutionDetailsRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[GetJobExecutionDetailsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataflow/latest/dataflow/protos.google.dataflow.v1beta3.getjobexecutiondetailsrequest)`   
GetJobExecutionDetailsRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a GetJobExecutionDetailsRequest message.

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
