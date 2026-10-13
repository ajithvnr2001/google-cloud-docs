---
url: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.accountissueservice-class
title: Class protos.google.shopping.merchant.accounts.v1.AccountIssueService (4.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:10.679974+00:00
---

# Class protos.google.shopping.merchant.accounts.v1.AccountIssueService (4.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.accountissueservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.shopping.merchant.accounts.v1.AccountIssueService (4.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.1 (latest)  3.2.0  2.2.0  1.0.0 

Represents an AccountIssueService

## Inheritance

$protobuf.rpc.Service > protos.google.shopping.merchant.accounts.v1.AccountIssueService

## Package

[@google-shopping/accounts](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AccountIssueService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AccountIssueService;

Creates new AccountIssueService service using the specified rpc implementation.

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
`[AccountIssueService](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.accountissueservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### listAccountIssues(request, callback)
    
    
    public listAccountIssues(request: google.shopping.merchant.accounts.v1.IListAccountIssuesRequest, callback: google.shopping.merchant.accounts.v1.AccountIssueService.ListAccountIssuesCallback): void;

Calls ListAccountIssues.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAccountIssuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ilistaccountissuesrequest)`   
ListAccountIssuesRequest message or plain object  
`callback` |  `[ListAccountIssuesCallback](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAccountIssuesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAccountIssues(request)
    
    
    public listAccountIssues(request: google.shopping.merchant.accounts.v1.IListAccountIssuesRequest): Promise<google.shopping.merchant.accounts.v1.ListAccountIssuesResponse>;

Calls ListAccountIssues.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAccountIssuesRequest](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.ilistaccountissuesrequest)`   
ListAccountIssuesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.shopping.merchant.accounts.v1.ListAccountIssuesResponse](https://docs.cloud.google.com/nodejs/docs/reference/accounts/latest/accounts/protos.google.shopping.merchant.accounts.v1.listaccountissuesresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
