---
url: https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.policytagmanager-class
title: Class protos.google.cloud.datacatalog.v1.PolicyTagManager (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:55.186573+00:00
---

# Class protos.google.cloud.datacatalog.v1.PolicyTagManager (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.policytagmanager-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.datacatalog.v1.PolicyTagManager (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  4.7.0  4.6.0  4.5.0  4.1.1  3.3.1  3.2.1  2.5.0  2.4.2  2.3.4 

Represents a PolicyTagManager

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.datacatalog.v1.PolicyTagManager

## Package

[@google-cloud/datacatalog](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new PolicyTagManager service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): PolicyTagManager;

Creates new PolicyTagManager service using the specified rpc implementation.

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
`[PolicyTagManager](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.policytagmanager-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createPolicyTag(request, callback)
    
    
    public createPolicyTag(request: google.cloud.datacatalog.v1.ICreatePolicyTagRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.CreatePolicyTagCallback): void;

Calls CreatePolicyTag.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreatePolicyTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.icreatepolicytagrequest)`   
CreatePolicyTagRequest message or plain object  
`callback` |  `[CreatePolicyTagCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and PolicyTag  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createPolicyTag(request)
    
    
    public createPolicyTag(request: google.cloud.datacatalog.v1.ICreatePolicyTagRequest): Promise<google.cloud.datacatalog.v1.PolicyTag>;

Calls CreatePolicyTag.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreatePolicyTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.icreatepolicytagrequest)`   
CreatePolicyTagRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datacatalog.v1.PolicyTag](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.policytag)>` | Promise  
  
### createTaxonomy(request, callback)
    
    
    public createTaxonomy(request: google.cloud.datacatalog.v1.ICreateTaxonomyRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.CreateTaxonomyCallback): void;

Calls CreateTaxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.icreatetaxonomyrequest)`   
CreateTaxonomyRequest message or plain object  
`callback` |  `[CreateTaxonomyCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and Taxonomy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTaxonomy(request)
    
    
    public createTaxonomy(request: google.cloud.datacatalog.v1.ICreateTaxonomyRequest): Promise<google.cloud.datacatalog.v1.Taxonomy>;

Calls CreateTaxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.icreatetaxonomyrequest)`   
CreateTaxonomyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datacatalog.v1.Taxonomy](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.taxonomy-class)>` | Promise  
  
### deletePolicyTag(request, callback)
    
    
    public deletePolicyTag(request: google.cloud.datacatalog.v1.IDeletePolicyTagRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.DeletePolicyTagCallback): void;

Calls DeletePolicyTag.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeletePolicyTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ideletepolicytagrequest)`   
DeletePolicyTagRequest message or plain object  
`callback` |  `[DeletePolicyTagCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deletePolicyTag(request)
    
    
    public deletePolicyTag(request: google.cloud.datacatalog.v1.IDeletePolicyTagRequest): Promise<google.protobuf.Empty>;

Calls DeletePolicyTag.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeletePolicyTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ideletepolicytagrequest)`   
DeletePolicyTagRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.protobuf.empty)>` | Promise  
  
### deleteTaxonomy(request, callback)
    
    
    public deleteTaxonomy(request: google.cloud.datacatalog.v1.IDeleteTaxonomyRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.DeleteTaxonomyCallback): void;

Calls DeleteTaxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ideletetaxonomyrequest)`   
DeleteTaxonomyRequest message or plain object  
`callback` |  `[DeleteTaxonomyCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTaxonomy(request)
    
    
    public deleteTaxonomy(request: google.cloud.datacatalog.v1.IDeleteTaxonomyRequest): Promise<google.protobuf.Empty>;

Calls DeleteTaxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ideletetaxonomyrequest)`   
DeleteTaxonomyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.protobuf.empty)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.iam.v1.IGetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.igetiampolicyrequest)`   
GetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.policy)>` | Promise  
  
### getPolicyTag(request, callback)
    
    
    public getPolicyTag(request: google.cloud.datacatalog.v1.IGetPolicyTagRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.GetPolicyTagCallback): void;

Calls GetPolicyTag.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.igetpolicytagrequest)`   
GetPolicyTagRequest message or plain object  
`callback` |  `[GetPolicyTagCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and PolicyTag  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getPolicyTag(request)
    
    
    public getPolicyTag(request: google.cloud.datacatalog.v1.IGetPolicyTagRequest): Promise<google.cloud.datacatalog.v1.PolicyTag>;

Calls GetPolicyTag.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetPolicyTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.igetpolicytagrequest)`   
GetPolicyTagRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datacatalog.v1.PolicyTag](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.policytag)>` | Promise  
  
### getTaxonomy(request, callback)
    
    
    public getTaxonomy(request: google.cloud.datacatalog.v1.IGetTaxonomyRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.GetTaxonomyCallback): void;

Calls GetTaxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.igettaxonomyrequest)`   
GetTaxonomyRequest message or plain object  
`callback` |  `[GetTaxonomyCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and Taxonomy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTaxonomy(request)
    
    
    public getTaxonomy(request: google.cloud.datacatalog.v1.IGetTaxonomyRequest): Promise<google.cloud.datacatalog.v1.Taxonomy>;

Calls GetTaxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.igettaxonomyrequest)`   
GetTaxonomyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datacatalog.v1.Taxonomy](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.taxonomy-class)>` | Promise  
  
### listPolicyTags(request, callback)
    
    
    public listPolicyTags(request: google.cloud.datacatalog.v1.IListPolicyTagsRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.ListPolicyTagsCallback): void;

Calls ListPolicyTags.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListPolicyTagsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ilistpolicytagsrequest)`   
ListPolicyTagsRequest message or plain object  
`callback` |  `[ListPolicyTagsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and ListPolicyTagsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listPolicyTags(request)
    
    
    public listPolicyTags(request: google.cloud.datacatalog.v1.IListPolicyTagsRequest): Promise<google.cloud.datacatalog.v1.ListPolicyTagsResponse>;

Calls ListPolicyTags.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListPolicyTagsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ilistpolicytagsrequest)`   
ListPolicyTagsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datacatalog.v1.ListPolicyTagsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.listpolicytagsresponse)>` | Promise  
  
### listTaxonomies(request, callback)
    
    
    public listTaxonomies(request: google.cloud.datacatalog.v1.IListTaxonomiesRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.ListTaxonomiesCallback): void;

Calls ListTaxonomies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTaxonomiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ilisttaxonomiesrequest)`   
ListTaxonomiesRequest message or plain object  
`callback` |  `[ListTaxonomiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTaxonomiesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTaxonomies(request)
    
    
    public listTaxonomies(request: google.cloud.datacatalog.v1.IListTaxonomiesRequest): Promise<google.cloud.datacatalog.v1.ListTaxonomiesResponse>;

Calls ListTaxonomies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTaxonomiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.ilisttaxonomiesrequest)`   
ListTaxonomiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datacatalog.v1.ListTaxonomiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.listtaxonomiesresponse)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.iam.v1.ISetIamPolicyRequest): Promise<google.iam.v1.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.isetiampolicyrequest)`   
SetIamPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.policy)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and TestIamPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.iam.v1.ITestIamPermissionsRequest): Promise<google.iam.v1.TestIamPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.itestiampermissionsrequest)`   
TestIamPermissionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.iam.v1.TestIamPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.iam.v1.testiampermissionsresponse)>` | Promise  
  
### updatePolicyTag(request, callback)
    
    
    public updatePolicyTag(request: google.cloud.datacatalog.v1.IUpdatePolicyTagRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.UpdatePolicyTagCallback): void;

Calls UpdatePolicyTag.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePolicyTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.iupdatepolicytagrequest)`   
UpdatePolicyTagRequest message or plain object  
`callback` |  `[UpdatePolicyTagCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and PolicyTag  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updatePolicyTag(request)
    
    
    public updatePolicyTag(request: google.cloud.datacatalog.v1.IUpdatePolicyTagRequest): Promise<google.cloud.datacatalog.v1.PolicyTag>;

Calls UpdatePolicyTag.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdatePolicyTagRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.iupdatepolicytagrequest)`   
UpdatePolicyTagRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datacatalog.v1.PolicyTag](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.policytag)>` | Promise  
  
### updateTaxonomy(request, callback)
    
    
    public updateTaxonomy(request: google.cloud.datacatalog.v1.IUpdateTaxonomyRequest, callback: google.cloud.datacatalog.v1.PolicyTagManager.UpdateTaxonomyCallback): void;

Calls UpdateTaxonomy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.iupdatetaxonomyrequest)`   
UpdateTaxonomyRequest message or plain object  
`callback` |  `[UpdateTaxonomyCallback](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/overview.html)`   
Node-style callback called with the error, if any, and Taxonomy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTaxonomy(request)
    
    
    public updateTaxonomy(request: google.cloud.datacatalog.v1.IUpdateTaxonomyRequest): Promise<google.cloud.datacatalog.v1.Taxonomy>;

Calls UpdateTaxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTaxonomyRequest](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.iupdatetaxonomyrequest)`   
UpdateTaxonomyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.datacatalog.v1.Taxonomy](https://docs.cloud.google.com/nodejs/docs/reference/datacatalog/latest/datacatalog/protos.google.cloud.datacatalog.v1.taxonomy-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
