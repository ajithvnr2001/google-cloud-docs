---
url: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budgetservice-class
title: Class protos.google.cloud.billing.budgets.v1beta1.BudgetService (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:52.723302+00:00
---

# Class protos.google.cloud.billing.budgets.v1beta1.BudgetService (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budgetservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.billing.budgets.v1beta1.BudgetService (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  4.2.2  4.1.2  3.3.0  3.2.8 

Represents a BudgetService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.billing.budgets.v1beta1.BudgetService

## Package

[@google-cloud/billing-budgets](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new BudgetService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): BudgetService;

Creates new BudgetService service using the specified rpc implementation.

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
`[BudgetService](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budgetservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createBudget(request, callback)
    
    
    public createBudget(request: google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest, callback: google.cloud.billing.budgets.v1beta1.BudgetService.CreateBudgetCallback): void;

Calls CreateBudget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.icreatebudgetrequest)`   
CreateBudgetRequest message or plain object  
`callback` |  `[CreateBudgetCallback](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)`   
Node-style callback called with the error, if any, and Budget  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createBudget(request)
    
    
    public createBudget(request: google.cloud.billing.budgets.v1beta1.ICreateBudgetRequest): Promise<google.cloud.billing.budgets.v1beta1.Budget>;

Calls CreateBudget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.icreatebudgetrequest)`   
CreateBudgetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.billing.budgets.v1beta1.Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget)>` | Promise  
  
### deleteBudget(request, callback)
    
    
    public deleteBudget(request: google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest, callback: google.cloud.billing.budgets.v1beta1.BudgetService.DeleteBudgetCallback): void;

Calls DeleteBudget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ideletebudgetrequest)`   
DeleteBudgetRequest message or plain object  
`callback` |  `[DeleteBudgetCallback](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteBudget(request)
    
    
    public deleteBudget(request: google.cloud.billing.budgets.v1beta1.IDeleteBudgetRequest): Promise<google.protobuf.Empty>;

Calls DeleteBudget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ideletebudgetrequest)`   
DeleteBudgetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.protobuf.empty)>` | Promise  
  
### getBudget(request, callback)
    
    
    public getBudget(request: google.cloud.billing.budgets.v1beta1.IGetBudgetRequest, callback: google.cloud.billing.budgets.v1beta1.BudgetService.GetBudgetCallback): void;

Calls GetBudget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.igetbudgetrequest)`   
GetBudgetRequest message or plain object  
`callback` |  `[GetBudgetCallback](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)`   
Node-style callback called with the error, if any, and Budget  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBudget(request)
    
    
    public getBudget(request: google.cloud.billing.budgets.v1beta1.IGetBudgetRequest): Promise<google.cloud.billing.budgets.v1beta1.Budget>;

Calls GetBudget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.igetbudgetrequest)`   
GetBudgetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.billing.budgets.v1beta1.Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget)>` | Promise  
  
### listBudgets(request, callback)
    
    
    public listBudgets(request: google.cloud.billing.budgets.v1beta1.IListBudgetsRequest, callback: google.cloud.billing.budgets.v1beta1.BudgetService.ListBudgetsCallback): void;

Calls ListBudgets.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest)`   
ListBudgetsRequest message or plain object  
`callback` |  `[ListBudgetsCallback](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBudgetsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBudgets(request)
    
    
    public listBudgets(request: google.cloud.billing.budgets.v1beta1.IListBudgetsRequest): Promise<google.cloud.billing.budgets.v1beta1.ListBudgetsResponse>;

Calls ListBudgets.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBudgetsRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.ilistbudgetsrequest)`   
ListBudgetsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.billing.budgets.v1beta1.ListBudgetsResponse](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.listbudgetsresponse)>` | Promise  
  
### updateBudget(request, callback)
    
    
    public updateBudget(request: google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest, callback: google.cloud.billing.budgets.v1beta1.BudgetService.UpdateBudgetCallback): void;

Calls UpdateBudget.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.iupdatebudgetrequest)`   
UpdateBudgetRequest message or plain object  
`callback` |  `[UpdateBudgetCallback](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/overview.html)`   
Node-style callback called with the error, if any, and Budget  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateBudget(request)
    
    
    public updateBudget(request: google.cloud.billing.budgets.v1beta1.IUpdateBudgetRequest): Promise<google.cloud.billing.budgets.v1beta1.Budget>;

Calls UpdateBudget.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateBudgetRequest](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.iupdatebudgetrequest)`   
UpdateBudgetRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.billing.budgets.v1beta1.Budget](https://docs.cloud.google.com/nodejs/docs/reference/billing-budgets/latest/billing-budgets/protos.google.cloud.billing.budgets.v1beta1.budget)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
