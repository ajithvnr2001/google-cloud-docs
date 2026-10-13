---
url: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validationhelperv1-class
title: Class protos.google.cloud.binaryauthorization.v1.ValidationHelperV1 (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:09:09.385208+00:00
---

# Class protos.google.cloud.binaryauthorization.v1.ValidationHelperV1 (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validationhelperv1-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.binaryauthorization.v1.ValidationHelperV1 (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.5.0  4.4.0  4.2.0  3.7.0  2.5.0  2.2.1  2.1.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.6 

Represents a ValidationHelperV1

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.binaryauthorization.v1.ValidationHelperV1

## Package

[@google-cloud/binary-authorization](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ValidationHelperV1 service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ValidationHelperV1;

Creates new ValidationHelperV1 service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[ValidationHelperV1](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validationhelperv1-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### validateAttestationOccurrence(request, callback)
    
    
    public validateAttestationOccurrence(request: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceRequest, callback: google.cloud.binaryauthorization.v1.ValidationHelperV1.ValidateAttestationOccurrenceCallback): void;

Calls ValidateAttestationOccurrence.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrencerequest)`   
ValidateAttestationOccurrenceRequest message or plain object  
`callback` |  `[ValidateAttestationOccurrenceCallback](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/overview.html)`   
Node-style callback called with the error, if any, and ValidateAttestationOccurrenceResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### validateAttestationOccurrence(request)
    
    
    public validateAttestationOccurrence(request: google.cloud.binaryauthorization.v1.IValidateAttestationOccurrenceRequest): Promise<google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse>;

Calls ValidateAttestationOccurrence.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IValidateAttestationOccurrenceRequest](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.ivalidateattestationoccurrencerequest)`   
ValidateAttestationOccurrenceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.binaryauthorization.v1.ValidateAttestationOccurrenceResponse](https://docs.cloud.google.com/nodejs/docs/reference/binary-authorization/latest/binary-authorization/protos.google.cloud.binaryauthorization.v1.validateattestationoccurrenceresponse-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
