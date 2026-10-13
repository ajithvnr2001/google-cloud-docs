---
url: https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.caseservice-class
title: Class protos.google.cloud.support.v2beta.CaseService (3.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:18.076546+00:00
---

# Class protos.google.cloud.support.v2beta.CaseService (3.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.caseservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.support.v2beta.CaseService (3.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.1 (latest)  2.5.0  2.4.0  1.0.2 

Represents a CaseService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.support.v2beta.CaseService

## Package

[@google-cloud/support](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CaseService service.

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

### closeCase(request, callback)
    
    
    public closeCase(request: google.cloud.support.v2beta.ICloseCaseRequest, callback: google.cloud.support.v2beta.CaseService.CloseCaseCallback): void;

Calls CloseCase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloseCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iclosecaserequest)`   
CloseCaseRequest message or plain object  
`callback` |  `[CloseCaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)`   
Node-style callback called with the error, if any, and Case  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### closeCase(request)
    
    
    public closeCase(request: google.cloud.support.v2beta.ICloseCaseRequest): Promise<google.cloud.support.v2beta.Case>;

Calls CloseCase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICloseCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iclosecaserequest)`   
CloseCaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.support.v2beta.Case](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.case-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CaseService;

Creates new CaseService service using the specified rpc implementation.

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
`[CaseService](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.caseservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCase(request, callback)
    
    
    public createCase(request: google.cloud.support.v2beta.ICreateCaseRequest, callback: google.cloud.support.v2beta.CaseService.CreateCaseCallback): void;

Calls CreateCase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.icreatecaserequest)`   
CreateCaseRequest message or plain object  
`callback` |  `[CreateCaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)`   
Node-style callback called with the error, if any, and Case  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCase(request)
    
    
    public createCase(request: google.cloud.support.v2beta.ICreateCaseRequest): Promise<google.cloud.support.v2beta.Case>;

Calls CreateCase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.icreatecaserequest)`   
CreateCaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.support.v2beta.Case](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.case-class)>` | Promise  
  
### escalateCase(request, callback)
    
    
    public escalateCase(request: google.cloud.support.v2beta.IEscalateCaseRequest, callback: google.cloud.support.v2beta.CaseService.EscalateCaseCallback): void;

Calls EscalateCase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEscalateCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iescalatecaserequest)`   
EscalateCaseRequest message or plain object  
`callback` |  `[EscalateCaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)`   
Node-style callback called with the error, if any, and Case  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### escalateCase(request)
    
    
    public escalateCase(request: google.cloud.support.v2beta.IEscalateCaseRequest): Promise<google.cloud.support.v2beta.Case>;

Calls EscalateCase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEscalateCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iescalatecaserequest)`   
EscalateCaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.support.v2beta.Case](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.case-class)>` | Promise  
  
### getCase(request, callback)
    
    
    public getCase(request: google.cloud.support.v2beta.IGetCaseRequest, callback: google.cloud.support.v2beta.CaseService.GetCaseCallback): void;

Calls GetCase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.igetcaserequest)`   
GetCaseRequest message or plain object  
`callback` |  `[GetCaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)`   
Node-style callback called with the error, if any, and Case  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCase(request)
    
    
    public getCase(request: google.cloud.support.v2beta.IGetCaseRequest): Promise<google.cloud.support.v2beta.Case>;

Calls GetCase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.igetcaserequest)`   
GetCaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.support.v2beta.Case](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.case-class)>` | Promise  
  
### listCases(request, callback)
    
    
    public listCases(request: google.cloud.support.v2beta.IListCasesRequest, callback: google.cloud.support.v2beta.CaseService.ListCasesCallback): void;

Calls ListCases.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistcasesrequest)`   
ListCasesRequest message or plain object  
`callback` |  `[ListCasesCallback](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCasesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCases(request)
    
    
    public listCases(request: google.cloud.support.v2beta.IListCasesRequest): Promise<google.cloud.support.v2beta.ListCasesResponse>;

Calls ListCases.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.ilistcasesrequest)`   
ListCasesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.support.v2beta.ListCasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.listcasesresponse)>` | Promise  
  
### searchCaseClassifications(request, callback)
    
    
    public searchCaseClassifications(request: google.cloud.support.v2beta.ISearchCaseClassificationsRequest, callback: google.cloud.support.v2beta.CaseService.SearchCaseClassificationsCallback): void;

Calls SearchCaseClassifications.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchCaseClassificationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isearchcaseclassificationsrequest)`   
SearchCaseClassificationsRequest message or plain object  
`callback` |  `[SearchCaseClassificationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchCaseClassificationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchCaseClassifications(request)
    
    
    public searchCaseClassifications(request: google.cloud.support.v2beta.ISearchCaseClassificationsRequest): Promise<google.cloud.support.v2beta.SearchCaseClassificationsResponse>;

Calls SearchCaseClassifications.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchCaseClassificationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isearchcaseclassificationsrequest)`   
SearchCaseClassificationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.support.v2beta.SearchCaseClassificationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.searchcaseclassificationsresponse)>` | Promise  
  
### searchCases(request, callback)
    
    
    public searchCases(request: google.cloud.support.v2beta.ISearchCasesRequest, callback: google.cloud.support.v2beta.CaseService.SearchCasesCallback): void;

Calls SearchCases.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchCasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isearchcasesrequest)`   
SearchCasesRequest message or plain object  
`callback` |  `[SearchCasesCallback](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchCasesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchCases(request)
    
    
    public searchCases(request: google.cloud.support.v2beta.ISearchCasesRequest): Promise<google.cloud.support.v2beta.SearchCasesResponse>;

Calls SearchCases.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchCasesRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.isearchcasesrequest)`   
SearchCasesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.support.v2beta.SearchCasesResponse](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.searchcasesresponse)>` | Promise  
  
### updateCase(request, callback)
    
    
    public updateCase(request: google.cloud.support.v2beta.IUpdateCaseRequest, callback: google.cloud.support.v2beta.CaseService.UpdateCaseCallback): void;

Calls UpdateCase.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iupdatecaserequest)`   
UpdateCaseRequest message or plain object  
`callback` |  `[UpdateCaseCallback](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/overview.html)`   
Node-style callback called with the error, if any, and Case  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCase(request)
    
    
    public updateCase(request: google.cloud.support.v2beta.IUpdateCaseRequest): Promise<google.cloud.support.v2beta.Case>;

Calls UpdateCase.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCaseRequest](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.iupdatecaserequest)`   
UpdateCaseRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.support.v2beta.Case](https://docs.cloud.google.com/nodejs/docs/reference/support/latest/support/protos.google.cloud.support.v2beta.case-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
