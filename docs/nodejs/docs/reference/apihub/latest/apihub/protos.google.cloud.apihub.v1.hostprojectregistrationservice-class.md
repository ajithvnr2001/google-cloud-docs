---
url: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.hostprojectregistrationservice-class
title: Class protos.google.cloud.apihub.v1.HostProjectRegistrationService (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:01.044910+00:00
---

# Class protos.google.cloud.apihub.v1.HostProjectRegistrationService (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.hostprojectregistrationservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.apihub.v1.HostProjectRegistrationService (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a HostProjectRegistrationService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.apihub.v1.HostProjectRegistrationService

## Package

[@google-cloud/apihub](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new HostProjectRegistrationService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): HostProjectRegistrationService;

Creates new HostProjectRegistrationService service using the specified rpc implementation.

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
`[HostProjectRegistrationService](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.hostprojectregistrationservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createHostProjectRegistration(request, callback)
    
    
    public createHostProjectRegistration(request: google.cloud.apihub.v1.ICreateHostProjectRegistrationRequest, callback: google.cloud.apihub.v1.HostProjectRegistrationService.CreateHostProjectRegistrationCallback): void;

Calls CreateHostProjectRegistration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHostProjectRegistrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatehostprojectregistrationrequest)`   
CreateHostProjectRegistrationRequest message or plain object  
`callback` |  `[CreateHostProjectRegistrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and HostProjectRegistration  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createHostProjectRegistration(request)
    
    
    public createHostProjectRegistration(request: google.cloud.apihub.v1.ICreateHostProjectRegistrationRequest): Promise<google.cloud.apihub.v1.HostProjectRegistration>;

Calls CreateHostProjectRegistration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateHostProjectRegistrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.icreatehostprojectregistrationrequest)`   
CreateHostProjectRegistrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.HostProjectRegistration](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.hostprojectregistration)>` | Promise  
  
### getHostProjectRegistration(request, callback)
    
    
    public getHostProjectRegistration(request: google.cloud.apihub.v1.IGetHostProjectRegistrationRequest, callback: google.cloud.apihub.v1.HostProjectRegistrationService.GetHostProjectRegistrationCallback): void;

Calls GetHostProjectRegistration.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHostProjectRegistrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igethostprojectregistrationrequest)`   
GetHostProjectRegistrationRequest message or plain object  
`callback` |  `[GetHostProjectRegistrationCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and HostProjectRegistration  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getHostProjectRegistration(request)
    
    
    public getHostProjectRegistration(request: google.cloud.apihub.v1.IGetHostProjectRegistrationRequest): Promise<google.cloud.apihub.v1.HostProjectRegistration>;

Calls GetHostProjectRegistration.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetHostProjectRegistrationRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.igethostprojectregistrationrequest)`   
GetHostProjectRegistrationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.HostProjectRegistration](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.hostprojectregistration)>` | Promise  
  
### listHostProjectRegistrations(request, callback)
    
    
    public listHostProjectRegistrations(request: google.cloud.apihub.v1.IListHostProjectRegistrationsRequest, callback: google.cloud.apihub.v1.HostProjectRegistrationService.ListHostProjectRegistrationsCallback): void;

Calls ListHostProjectRegistrations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilisthostprojectregistrationsrequest)`   
ListHostProjectRegistrationsRequest message or plain object  
`callback` |  `[ListHostProjectRegistrationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/overview.html)`   
Node-style callback called with the error, if any, and ListHostProjectRegistrationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listHostProjectRegistrations(request)
    
    
    public listHostProjectRegistrations(request: google.cloud.apihub.v1.IListHostProjectRegistrationsRequest): Promise<google.cloud.apihub.v1.ListHostProjectRegistrationsResponse>;

Calls ListHostProjectRegistrations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListHostProjectRegistrationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.ilisthostprojectregistrationsrequest)`   
ListHostProjectRegistrationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.apihub.v1.ListHostProjectRegistrationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/apihub/latest/apihub/protos.google.cloud.apihub.v1.listhostprojectregistrationsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
