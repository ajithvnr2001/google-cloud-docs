---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.contactservice-class
title: Class protos.google.ads.admanager.v1.ContactService (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:03.454630+00:00
---

# Class protos.google.ads.admanager.v1.ContactService (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.contactservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.ads.admanager.v1.ContactService (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Represents a ContactService

## Inheritance

$protobuf.rpc.Service > protos.google.ads.admanager.v1.ContactService

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ContactService service.

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

### batchCreateContacts(request, callback)
    
    
    public batchCreateContacts(request: google.ads.admanager.v1.IBatchCreateContactsRequest, callback: google.ads.admanager.v1.ContactService.BatchCreateContactsCallback): void;

Calls BatchCreateContacts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreatecontactsrequest)`   
BatchCreateContactsRequest message or plain object  
`callback` |  `[BatchCreateContactsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchCreateContactsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateContacts(request)
    
    
    public batchCreateContacts(request: google.ads.admanager.v1.IBatchCreateContactsRequest): Promise<google.ads.admanager.v1.BatchCreateContactsResponse>;

Calls BatchCreateContacts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchcreatecontactsrequest)`   
BatchCreateContactsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchCreateContactsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchcreatecontactsresponse)>` | Promise  
  
### batchUpdateContacts(request, callback)
    
    
    public batchUpdateContacts(request: google.ads.admanager.v1.IBatchUpdateContactsRequest, callback: google.ads.admanager.v1.ContactService.BatchUpdateContactsCallback): void;

Calls BatchUpdateContacts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdatecontactsrequest)`   
BatchUpdateContactsRequest message or plain object  
`callback` |  `[BatchUpdateContactsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateContactsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateContacts(request)
    
    
    public batchUpdateContacts(request: google.ads.admanager.v1.IBatchUpdateContactsRequest): Promise<google.ads.admanager.v1.BatchUpdateContactsResponse>;

Calls BatchUpdateContacts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ibatchupdatecontactsrequest)`   
BatchUpdateContactsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.BatchUpdateContactsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.batchupdatecontactsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ContactService;

Creates new ContactService service using the specified rpc implementation.

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
`[ContactService](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.contactservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createContact(request, callback)
    
    
    public createContact(request: google.ads.admanager.v1.ICreateContactRequest, callback: google.ads.admanager.v1.ContactService.CreateContactCallback): void;

Calls CreateContact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreatecontactrequest)`   
CreateContactRequest message or plain object  
`callback` |  `[CreateContactCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Contact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createContact(request)
    
    
    public createContact(request: google.ads.admanager.v1.ICreateContactRequest): Promise<google.ads.admanager.v1.Contact>;

Calls CreateContact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.icreatecontactrequest)`   
CreateContactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Contact](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.contact)>` | Promise  
  
### getContact(request, callback)
    
    
    public getContact(request: google.ads.admanager.v1.IGetContactRequest, callback: google.ads.admanager.v1.ContactService.GetContactCallback): void;

Calls GetContact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetcontactrequest)`   
GetContactRequest message or plain object  
`callback` |  `[GetContactCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Contact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getContact(request)
    
    
    public getContact(request: google.ads.admanager.v1.IGetContactRequest): Promise<google.ads.admanager.v1.Contact>;

Calls GetContact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.igetcontactrequest)`   
GetContactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Contact](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.contact)>` | Promise  
  
### listContacts(request, callback)
    
    
    public listContacts(request: google.ads.admanager.v1.IListContactsRequest, callback: google.ads.admanager.v1.ContactService.ListContactsCallback): void;

Calls ListContacts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistcontactsrequest)`   
ListContactsRequest message or plain object  
`callback` |  `[ListContactsCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListContactsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listContacts(request)
    
    
    public listContacts(request: google.ads.admanager.v1.IListContactsRequest): Promise<google.ads.admanager.v1.ListContactsResponse>;

Calls ListContacts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilistcontactsrequest)`   
ListContactsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.ListContactsResponse](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.listcontactsresponse)>` | Promise  
  
### updateContact(request, callback)
    
    
    public updateContact(request: google.ads.admanager.v1.IUpdateContactRequest, callback: google.ads.admanager.v1.ContactService.UpdateContactCallback): void;

Calls UpdateContact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdatecontactrequest)`   
UpdateContactRequest message or plain object  
`callback` |  `[UpdateContactCallback](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Contact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateContact(request)
    
    
    public updateContact(request: google.ads.admanager.v1.IUpdateContactRequest): Promise<google.ads.admanager.v1.Contact>;

Calls UpdateContact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.iupdatecontactrequest)`   
UpdateContactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.ads.admanager.v1.Contact](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.contact)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
