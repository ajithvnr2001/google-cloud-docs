---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificates-class
title: Class protos.google.appengine.v1.AuthorizedCertificates (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:29.230989+00:00
---

# Class protos.google.appengine.v1.AuthorizedCertificates (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificates-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.AuthorizedCertificates (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents an AuthorizedCertificates

## Inheritance

$protobuf.rpc.Service > protos.google.appengine.v1.AuthorizedCertificates

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AuthorizedCertificates service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AuthorizedCertificates;

Creates new AuthorizedCertificates service using the specified rpc implementation.

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
`[AuthorizedCertificates](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificates-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAuthorizedCertificate(request, callback)
    
    
    public createAuthorizedCertificate(request: google.appengine.v1.ICreateAuthorizedCertificateRequest, callback: google.appengine.v1.AuthorizedCertificates.CreateAuthorizedCertificateCallback): void;

Calls CreateAuthorizedCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuthorizedCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreateauthorizedcertificaterequest)`   
CreateAuthorizedCertificateRequest message or plain object  
`callback` |  `[CreateAuthorizedCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthorizedCertificate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAuthorizedCertificate(request)
    
    
    public createAuthorizedCertificate(request: google.appengine.v1.ICreateAuthorizedCertificateRequest): Promise<google.appengine.v1.AuthorizedCertificate>;

Calls CreateAuthorizedCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuthorizedCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreateauthorizedcertificaterequest)`   
CreateAuthorizedCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.AuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate)>` | Promise  
  
### deleteAuthorizedCertificate(request, callback)
    
    
    public deleteAuthorizedCertificate(request: google.appengine.v1.IDeleteAuthorizedCertificateRequest, callback: google.appengine.v1.AuthorizedCertificates.DeleteAuthorizedCertificateCallback): void;

Calls DeleteAuthorizedCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthorizedCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideleteauthorizedcertificaterequest)`   
DeleteAuthorizedCertificateRequest message or plain object  
`callback` |  `[DeleteAuthorizedCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAuthorizedCertificate(request)
    
    
    public deleteAuthorizedCertificate(request: google.appengine.v1.IDeleteAuthorizedCertificateRequest): Promise<google.protobuf.Empty>;

Calls DeleteAuthorizedCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAuthorizedCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideleteauthorizedcertificaterequest)`   
DeleteAuthorizedCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.protobuf.empty)>` | Promise  
  
### getAuthorizedCertificate(request, callback)
    
    
    public getAuthorizedCertificate(request: google.appengine.v1.IGetAuthorizedCertificateRequest, callback: google.appengine.v1.AuthorizedCertificates.GetAuthorizedCertificateCallback): void;

Calls GetAuthorizedCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthorizedCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetauthorizedcertificaterequest)`   
GetAuthorizedCertificateRequest message or plain object  
`callback` |  `[GetAuthorizedCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthorizedCertificate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAuthorizedCertificate(request)
    
    
    public getAuthorizedCertificate(request: google.appengine.v1.IGetAuthorizedCertificateRequest): Promise<google.appengine.v1.AuthorizedCertificate>;

Calls GetAuthorizedCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAuthorizedCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetauthorizedcertificaterequest)`   
GetAuthorizedCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.AuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate)>` | Promise  
  
### listAuthorizedCertificates(request, callback)
    
    
    public listAuthorizedCertificates(request: google.appengine.v1.IListAuthorizedCertificatesRequest, callback: google.appengine.v1.AuthorizedCertificates.ListAuthorizedCertificatesCallback): void;

Calls ListAuthorizedCertificates.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizedCertificatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistauthorizedcertificatesrequest)`   
ListAuthorizedCertificatesRequest message or plain object  
`callback` |  `[ListAuthorizedCertificatesCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAuthorizedCertificatesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAuthorizedCertificates(request)
    
    
    public listAuthorizedCertificates(request: google.appengine.v1.IListAuthorizedCertificatesRequest): Promise<google.appengine.v1.ListAuthorizedCertificatesResponse>;

Calls ListAuthorizedCertificates.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAuthorizedCertificatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistauthorizedcertificatesrequest)`   
ListAuthorizedCertificatesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.ListAuthorizedCertificatesResponse](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.listauthorizedcertificatesresponse)>` | Promise  
  
### updateAuthorizedCertificate(request, callback)
    
    
    public updateAuthorizedCertificate(request: google.appengine.v1.IUpdateAuthorizedCertificateRequest, callback: google.appengine.v1.AuthorizedCertificates.UpdateAuthorizedCertificateCallback): void;

Calls UpdateAuthorizedCertificate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuthorizedCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateauthorizedcertificaterequest)`   
UpdateAuthorizedCertificateRequest message or plain object  
`callback` |  `[UpdateAuthorizedCertificateCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and AuthorizedCertificate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAuthorizedCertificate(request)
    
    
    public updateAuthorizedCertificate(request: google.appengine.v1.IUpdateAuthorizedCertificateRequest): Promise<google.appengine.v1.AuthorizedCertificate>;

Calls UpdateAuthorizedCertificate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuthorizedCertificateRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateauthorizedcertificaterequest)`   
UpdateAuthorizedCertificateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.AuthorizedCertificate](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.authorizedcertificate)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
