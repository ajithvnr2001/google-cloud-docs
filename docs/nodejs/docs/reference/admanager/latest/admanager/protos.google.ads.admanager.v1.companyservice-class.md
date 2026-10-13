---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.companyservice-class
title: Class protos.google.ads.admanager.v1.CompanyService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:51.204129+00:00
---

# Class protos.google.ads.admanager.v1.CompanyService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.companyservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.CompanyService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents a CompanyService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.CompanyService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CompanyService service.

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

### batchCreateCompanies(request, callback)
    
    
    public batchCreateCompanies(request: google.ads.admanager.v1.IBatchCreateCompaniesRequest, callback: google.ads.admanager.v1.CompanyService.BatchCreateCompaniesCallback): void;

Calls BatchCreateCompanies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateCompaniesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreatecompaniesrequest)`   
BatchCreateCompaniesRequest message or plain object  
`callback` |  `[BatchCreateCompaniesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateCompaniesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateCompanies(request)
    
    
    public batchCreateCompanies(request: google.ads.admanager.v1.IBatchCreateCompaniesRequest): Promise<google.ads.admanager.v1.BatchCreateCompaniesResponse>;

Calls BatchCreateCompanies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateCompaniesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreatecompaniesrequest)`   
BatchCreateCompaniesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchCreateCompaniesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchcreatecompaniesresponse)>` | Promise  
  
### batchUpdateCompanies(request, callback)
    
    
    public batchUpdateCompanies(request: google.ads.admanager.v1.IBatchUpdateCompaniesRequest, callback: google.ads.admanager.v1.CompanyService.BatchUpdateCompaniesCallback): void;

Calls BatchUpdateCompanies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateCompaniesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdatecompaniesrequest)`   
BatchUpdateCompaniesRequest message or plain object  
`callback` |  `[BatchUpdateCompaniesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateCompaniesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateCompanies(request)
    
    
    public batchUpdateCompanies(request: google.ads.admanager.v1.IBatchUpdateCompaniesRequest): Promise<google.ads.admanager.v1.BatchUpdateCompaniesResponse>;

Calls BatchUpdateCompanies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateCompaniesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdatecompaniesrequest)`   
BatchUpdateCompaniesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchUpdateCompaniesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchupdatecompaniesresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CompanyService;

Creates new CompanyService service using the specified rpc implementation.

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
`[CompanyService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.companyservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createCompany(request, callback)
    
    
    public createCompany(request: google.ads.admanager.v1.ICreateCompanyRequest, callback: google.ads.admanager.v1.CompanyService.CreateCompanyCallback): void;

Calls CreateCompany.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompanyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreatecompanyrequest)`   
CreateCompanyRequest message or plain object  
`callback` |  `[CreateCompanyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Company  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createCompany(request)
    
    
    public createCompany(request: google.ads.admanager.v1.ICreateCompanyRequest): Promise<google.ads.admanager.v1.Company>;

Calls CreateCompany.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateCompanyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreatecompanyrequest)`   
CreateCompanyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Company](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.company)>` | Promise  
  
### getCompany(request, callback)
    
    
    public getCompany(request: google.ads.admanager.v1.IGetCompanyRequest, callback: google.ads.admanager.v1.CompanyService.GetCompanyCallback): void;

Calls GetCompany.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCompanyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetcompanyrequest)`   
GetCompanyRequest message or plain object  
`callback` |  `[GetCompanyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Company  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCompany(request)
    
    
    public getCompany(request: google.ads.admanager.v1.IGetCompanyRequest): Promise<google.ads.admanager.v1.Company>;

Calls GetCompany.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCompanyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetcompanyrequest)`   
GetCompanyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Company](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.company)>` | Promise  
  
### listCompanies(request, callback)
    
    
    public listCompanies(request: google.ads.admanager.v1.IListCompaniesRequest, callback: google.ads.admanager.v1.CompanyService.ListCompaniesCallback): void;

Calls ListCompanies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCompaniesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistcompaniesrequest)`   
ListCompaniesRequest message or plain object  
`callback` |  `[ListCompaniesCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCompaniesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCompanies(request)
    
    
    public listCompanies(request: google.ads.admanager.v1.IListCompaniesRequest): Promise<google.ads.admanager.v1.ListCompaniesResponse>;

Calls ListCompanies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCompaniesRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistcompaniesrequest)`   
ListCompaniesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListCompaniesResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listcompaniesresponse)>` | Promise  
  
### updateCompany(request, callback)
    
    
    public updateCompany(request: google.ads.admanager.v1.IUpdateCompanyRequest, callback: google.ads.admanager.v1.CompanyService.UpdateCompanyCallback): void;

Calls UpdateCompany.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCompanyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdatecompanyrequest)`   
UpdateCompanyRequest message or plain object  
`callback` |  `[UpdateCompanyCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Company  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateCompany(request)
    
    
    public updateCompany(request: google.ads.admanager.v1.IUpdateCompanyRequest): Promise<google.ads.admanager.v1.Company>;

Calls UpdateCompany.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateCompanyRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdatecompanyrequest)`   
UpdateCompanyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Company](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.company)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
