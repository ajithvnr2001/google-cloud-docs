---
url: https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.createbacktestresultrequest
title: Class protos.google.cloud.financialservices.v1.CreateBacktestResultRequest (0.6.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:32.385992+00:00
---

# Class protos.google.cloud.financialservices.v1.CreateBacktestResultRequest (0.6.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.createbacktestresultrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.financialservices.v1.CreateBacktestResultRequest (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.3.0  0.2.0 

Represents a CreateBacktestResultRequest.

## Implements

[protos.google.cloud.financialservices.v1.ICreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatebacktestresultrequest)

## Package

[@google-cloud/financialservices](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.financialservices.v1.ICreateBacktestResultRequest);

Constructs a new CreateBacktestResultRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatebacktestresultrequest)`   
Properties to set  
  
## Properties 

### backtestResult
    
    
    public backtestResult?: (google.cloud.financialservices.v1.IBacktestResult|null);

CreateBacktestResultRequest backtestResult.

### backtestResultId
    
    
    public backtestResultId: string;

CreateBacktestResultRequest backtestResultId.

### parent
    
    
    public parent: string;

CreateBacktestResultRequest parent.

### requestId
    
    
    public requestId: string;

CreateBacktestResultRequest requestId.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.financialservices.v1.ICreateBacktestResultRequest): google.cloud.financialservices.v1.CreateBacktestResultRequest;

Creates a new CreateBacktestResultRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[ICreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatebacktestresultrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[CreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.createbacktestresultrequest)` | CreateBacktestResultRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.financialservices.v1.CreateBacktestResultRequest;

Decodes a CreateBacktestResultRequest message from the specified reader or buffer.

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
`[CreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.createbacktestresultrequest)` | CreateBacktestResultRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.financialservices.v1.CreateBacktestResultRequest;

Decodes a CreateBacktestResultRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[CreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.createbacktestresultrequest)` | CreateBacktestResultRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.financialservices.v1.ICreateBacktestResultRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateBacktestResultRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatebacktestresultrequest)`   
CreateBacktestResultRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.financialservices.v1.ICreateBacktestResultRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified CreateBacktestResultRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[ICreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.icreatebacktestresultrequest)`   
CreateBacktestResultRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.financialservices.v1.CreateBacktestResultRequest;

Creates a CreateBacktestResultRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[CreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.createbacktestresultrequest)` | CreateBacktestResultRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for CreateBacktestResultRequest

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

Converts this CreateBacktestResultRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.financialservices.v1.CreateBacktestResultRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a CreateBacktestResultRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[CreateBacktestResultRequest](https://docs.cloud.google.com/nodejs/docs/reference/financialservices/latest/financialservices/protos.google.cloud.financialservices.v1.createbacktestresultrequest)`   
CreateBacktestResultRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a CreateBacktestResultRequest message.

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
