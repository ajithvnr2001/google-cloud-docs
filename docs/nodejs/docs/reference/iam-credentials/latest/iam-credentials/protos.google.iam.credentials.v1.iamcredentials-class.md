---
url: https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.iamcredentials-class
title: Class protos.google.iam.credentials.v1.IAMCredentials (5.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:43.854519+00:00
---

# Class protos.google.iam.credentials.v1.IAMCredentials (5.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.iamcredentials-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.iam.credentials.v1.IAMCredentials (5.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.0.1 (latest)  4.1.0  2.0.4  1.2.0  1.1.1  1.0.8 

Represents a IAMCredentials

## Inheritance

$protobuf.rpc.Service > protos.google.iam.credentials.v1.IAMCredentials

## Package

[@google-cloud/iam-credentials](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new IAMCredentials service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): IAMCredentials;

Creates new IAMCredentials service using the specified rpc implementation.

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
`[IAMCredentials](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.iamcredentials-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### generateAccessToken(request, callback)
    
    
    public generateAccessToken(request: google.iam.credentials.v1.IGenerateAccessTokenRequest, callback: google.iam.credentials.v1.IAMCredentials.GenerateAccessTokenCallback): void;

Calls GenerateAccessToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAccessTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.igenerateaccesstokenrequest)`   
GenerateAccessTokenRequest message or plain object  
`callback` |  `[GenerateAccessTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateAccessTokenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAccessToken(request)
    
    
    public generateAccessToken(request: google.iam.credentials.v1.IGenerateAccessTokenRequest): Promise<google.iam.credentials.v1.GenerateAccessTokenResponse>;

Calls GenerateAccessToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAccessTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.igenerateaccesstokenrequest)`   
GenerateAccessTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.credentials.v1.GenerateAccessTokenResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.generateaccesstokenresponse)>` | Promise  
  
### generateIdToken(request, callback)
    
    
    public generateIdToken(request: google.iam.credentials.v1.IGenerateIdTokenRequest, callback: google.iam.credentials.v1.IAMCredentials.GenerateIdTokenCallback): void;

Calls GenerateIdToken.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateIdTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.igenerateidtokenrequest)`   
GenerateIdTokenRequest message or plain object  
`callback` |  `[GenerateIdTokenCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateIdTokenResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateIdToken(request)
    
    
    public generateIdToken(request: google.iam.credentials.v1.IGenerateIdTokenRequest): Promise<google.iam.credentials.v1.GenerateIdTokenResponse>;

Calls GenerateIdToken.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateIdTokenRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.igenerateidtokenrequest)`   
GenerateIdTokenRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.credentials.v1.GenerateIdTokenResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.generateidtokenresponse)>` | Promise  
  
### signBlob(request, callback)
    
    
    public signBlob(request: google.iam.credentials.v1.ISignBlobRequest, callback: google.iam.credentials.v1.IAMCredentials.SignBlobCallback): void;

Calls SignBlob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISignBlobRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignblobrequest)`   
SignBlobRequest message or plain object  
`callback` |  `[SignBlobCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/overview.html)`   
Node-style callback called with the error, if any, and SignBlobResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### signBlob(request)
    
    
    public signBlob(request: google.iam.credentials.v1.ISignBlobRequest): Promise<google.iam.credentials.v1.SignBlobResponse>;

Calls SignBlob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISignBlobRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignblobrequest)`   
SignBlobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.credentials.v1.SignBlobResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signblobresponse)>` | Promise  
  
### signJwt(request, callback)
    
    
    public signJwt(request: google.iam.credentials.v1.ISignJwtRequest, callback: google.iam.credentials.v1.IAMCredentials.SignJwtCallback): void;

Calls SignJwt.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISignJwtRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignjwtrequest)`   
SignJwtRequest message or plain object  
`callback` |  `[SignJwtCallback](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/overview.html)`   
Node-style callback called with the error, if any, and SignJwtResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### signJwt(request)
    
    
    public signJwt(request: google.iam.credentials.v1.ISignJwtRequest): Promise<google.iam.credentials.v1.SignJwtResponse>;

Calls SignJwt.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISignJwtRequest](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.isignjwtrequest)`   
SignJwtRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.credentials.v1.SignJwtResponse](https://docs.cloud.google.com/nodejs/docs/reference/iam-credentials/latest/iam-credentials/protos.google.iam.credentials.v1.signjwtresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
