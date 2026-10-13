---
url: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.retryjobrequest
title: Class protos.google.cloud.deploy.v1.RetryJobRequest (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:48.960233+00:00
---

# Class protos.google.cloud.deploy.v1.RetryJobRequest (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.retryjobrequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.deploy.v1.RetryJobRequest (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.0.1  4.4.0  4.3.0  4.0.0  3.6.0  3.5.0  3.4.0  3.1.0  3.0.0  2.5.0  2.4.1  2.3.1  2.2.2  2.1.1  1.0.0  0.2.0 

Represents a RetryJobRequest.

## Implements

[protos.google.cloud.deploy.v1.IRetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iretryjobrequest)

## Package

[@google-cloud/deploy](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/overview.html)

## Constructors 

### (constructor)(properties)
    
    
    constructor(properties?: google.cloud.deploy.v1.IRetryJobRequest);

Constructs a new RetryJobRequest.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iretryjobrequest)`   
Properties to set  
  
## Properties 

### jobId
    
    
    public jobId: string;

RetryJobRequest jobId.

### overrideDeployPolicy
    
    
    public overrideDeployPolicy: string[];

RetryJobRequest overrideDeployPolicy.

### phaseId
    
    
    public phaseId: string;

RetryJobRequest phaseId.

### rollout
    
    
    public rollout: string;

RetryJobRequest rollout.

## Methods 

### create(properties)
    
    
    public static create(properties?: google.cloud.deploy.v1.IRetryJobRequest): google.cloud.deploy.v1.RetryJobRequest;

Creates a new RetryJobRequest instance using the specified properties.

**Parameter**  
---  
**Name** | **Description**  
`properties` |  `[IRetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iretryjobrequest)`   
Properties to set  
**Returns**  
---  
**Type** | **Description**  
`[RetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.retryjobrequest)` | RetryJobRequest instance  
  
### decode(reader, length)
    
    
    public static decode(reader: ($protobuf.Reader|Uint8Array), length?: number): google.cloud.deploy.v1.RetryJobRequest;

Decodes a RetryJobRequest message from the specified reader or buffer.

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
`[RetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.retryjobrequest)` | RetryJobRequest  
  
### decodeDelimited(reader)
    
    
    public static decodeDelimited(reader: ($protobuf.Reader|Uint8Array)): google.cloud.deploy.v1.RetryJobRequest;

Decodes a RetryJobRequest message from the specified reader or buffer, length delimited.

**Parameter**  
---  
**Name** | **Description**  
`reader` |  `(Reader|Uint8Array)`   
Reader or buffer to decode from  
**Returns**  
---  
**Type** | **Description**  
`[RetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.retryjobrequest)` | RetryJobRequest  
  
### encode(message, writer)
    
    
    public static encode(message: google.cloud.deploy.v1.IRetryJobRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RetryJobRequest message. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iretryjobrequest)`   
RetryJobRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### encodeDelimited(message, writer)
    
    
    public static encodeDelimited(message: google.cloud.deploy.v1.IRetryJobRequest, writer?: $protobuf.Writer): $protobuf.Writer;

Encodes the specified RetryJobRequest message, length delimited. Does not implicitly messages.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[IRetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.iretryjobrequest)`   
RetryJobRequest message or plain object to encode  
`writer` |  `$protobuf.Writer`   
Writer to encode to  
**Returns**  
---  
**Type** | **Description**  
`$protobuf.Writer` | Writer  
  
### fromObject(object)
    
    
    public static fromObject(object: { [k: string]: any }): google.cloud.deploy.v1.RetryJobRequest;

Creates a RetryJobRequest message from a plain object. Also converts values to their respective internal types.

**Parameter**  
---  
**Name** | **Description**  
`object` |  `{ [k: string]: any }`   
Plain object  
**Returns**  
---  
**Type** | **Description**  
`[RetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.retryjobrequest)` | RetryJobRequest  
  
### getTypeUrl(typeUrlPrefix)
    
    
    public static getTypeUrl(typeUrlPrefix?: string): string;

Gets the default type url for RetryJobRequest

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

Converts this RetryJobRequest to JSON.

**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | JSON object  
  
### toObject(message, options)
    
    
    public static toObject(message: google.cloud.deploy.v1.RetryJobRequest, options?: $protobuf.IConversionOptions): { [k: string]: any };

Creates a plain object from a RetryJobRequest message. Also converts values to other types if specified.

**Parameters**  
---  
**Name** | **Description**  
`message` |  `[RetryJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/deploy/latest/deploy/protos.google.cloud.deploy.v1.retryjobrequest)`   
RetryJobRequest  
`options` |  `$protobuf.IConversionOptions`   
Conversion options  
**Returns**  
---  
**Type** | **Description**  
`{ [k: string]: any }` | Plain object  
  
### verify(message)
    
    
    public static verify(message: { [k: string]: any }): (string|null);

Verifies a RetryJobRequest message.

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
