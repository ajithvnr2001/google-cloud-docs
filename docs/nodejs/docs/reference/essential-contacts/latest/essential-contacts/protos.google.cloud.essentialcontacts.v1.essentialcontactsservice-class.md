---
url: https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.essentialcontactsservice-class
title: Class protos.google.cloud.essentialcontacts.v1.EssentialContactsService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:08.543223+00:00
---

# Class protos.google.cloud.essentialcontacts.v1.EssentialContactsService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.essentialcontactsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.essentialcontacts.v1.EssentialContactsService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  4.0.1  3.2.0  3.0.0  2.1.2  2.0.2  1.1.1  1.0.6 

Represents an EssentialContactsService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.essentialcontacts.v1.EssentialContactsService

## Package

[@google-cloud/essential-contacts](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new EssentialContactsService service.

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

### computeContacts(request, callback)
    
    
    public computeContacts(request: google.cloud.essentialcontacts.v1.IComputeContactsRequest, callback: google.cloud.essentialcontacts.v1.EssentialContactsService.ComputeContactsCallback): void;

Calls ComputeContacts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IComputeContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.icomputecontactsrequest)`   
ComputeContactsRequest message or plain object  
`callback` |  `[ComputeContactsCallback](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)`   
Node-style callback called with the error, if any, and ComputeContactsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### computeContacts(request)
    
    
    public computeContacts(request: google.cloud.essentialcontacts.v1.IComputeContactsRequest): Promise<google.cloud.essentialcontacts.v1.ComputeContactsResponse>;

Calls ComputeContacts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IComputeContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.icomputecontactsrequest)`   
ComputeContactsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.essentialcontacts.v1.ComputeContactsResponse](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.computecontactsresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): EssentialContactsService;

Creates new EssentialContactsService service using the specified rpc implementation.

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
`[EssentialContactsService](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.essentialcontactsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createContact(request, callback)
    
    
    public createContact(request: google.cloud.essentialcontacts.v1.ICreateContactRequest, callback: google.cloud.essentialcontacts.v1.EssentialContactsService.CreateContactCallback): void;

Calls CreateContact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.icreatecontactrequest)`   
CreateContactRequest message or plain object  
`callback` |  `[CreateContactCallback](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)`   
Node-style callback called with the error, if any, and Contact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createContact(request)
    
    
    public createContact(request: google.cloud.essentialcontacts.v1.ICreateContactRequest): Promise<google.cloud.essentialcontacts.v1.Contact>;

Calls CreateContact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.icreatecontactrequest)`   
CreateContactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.essentialcontacts.v1.Contact](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.contact)>` | Promise  
  
### deleteContact(request, callback)
    
    
    public deleteContact(request: google.cloud.essentialcontacts.v1.IDeleteContactRequest, callback: google.cloud.essentialcontacts.v1.EssentialContactsService.DeleteContactCallback): void;

Calls DeleteContact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.ideletecontactrequest)`   
DeleteContactRequest message or plain object  
`callback` |  `[DeleteContactCallback](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteContact(request)
    
    
    public deleteContact(request: google.cloud.essentialcontacts.v1.IDeleteContactRequest): Promise<google.protobuf.Empty>;

Calls DeleteContact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.ideletecontactrequest)`   
DeleteContactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.protobuf.empty)>` | Promise  
  
### getContact(request, callback)
    
    
    public getContact(request: google.cloud.essentialcontacts.v1.IGetContactRequest, callback: google.cloud.essentialcontacts.v1.EssentialContactsService.GetContactCallback): void;

Calls GetContact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.igetcontactrequest)`   
GetContactRequest message or plain object  
`callback` |  `[GetContactCallback](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)`   
Node-style callback called with the error, if any, and Contact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getContact(request)
    
    
    public getContact(request: google.cloud.essentialcontacts.v1.IGetContactRequest): Promise<google.cloud.essentialcontacts.v1.Contact>;

Calls GetContact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.igetcontactrequest)`   
GetContactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.essentialcontacts.v1.Contact](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.contact)>` | Promise  
  
### listContacts(request, callback)
    
    
    public listContacts(request: google.cloud.essentialcontacts.v1.IListContactsRequest, callback: google.cloud.essentialcontacts.v1.EssentialContactsService.ListContactsCallback): void;

Calls ListContacts.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.ilistcontactsrequest)`   
ListContactsRequest message or plain object  
`callback` |  `[ListContactsCallback](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)`   
Node-style callback called with the error, if any, and ListContactsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listContacts(request)
    
    
    public listContacts(request: google.cloud.essentialcontacts.v1.IListContactsRequest): Promise<google.cloud.essentialcontacts.v1.ListContactsResponse>;

Calls ListContacts.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListContactsRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.ilistcontactsrequest)`   
ListContactsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.essentialcontacts.v1.ListContactsResponse](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.listcontactsresponse)>` | Promise  
  
### sendTestMessage(request, callback)
    
    
    public sendTestMessage(request: google.cloud.essentialcontacts.v1.ISendTestMessageRequest, callback: google.cloud.essentialcontacts.v1.EssentialContactsService.SendTestMessageCallback): void;

Calls SendTestMessage.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.isendtestmessagerequest)`   
SendTestMessageRequest message or plain object  
`callback` |  `[SendTestMessageCallback](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### sendTestMessage(request)
    
    
    public sendTestMessage(request: google.cloud.essentialcontacts.v1.ISendTestMessageRequest): Promise<google.protobuf.Empty>;

Calls SendTestMessage.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISendTestMessageRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.isendtestmessagerequest)`   
SendTestMessageRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.protobuf.empty)>` | Promise  
  
### updateContact(request, callback)
    
    
    public updateContact(request: google.cloud.essentialcontacts.v1.IUpdateContactRequest, callback: google.cloud.essentialcontacts.v1.EssentialContactsService.UpdateContactCallback): void;

Calls UpdateContact.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.iupdatecontactrequest)`   
UpdateContactRequest message or plain object  
`callback` |  `[UpdateContactCallback](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/overview.html)`   
Node-style callback called with the error, if any, and Contact  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateContact(request)
    
    
    public updateContact(request: google.cloud.essentialcontacts.v1.IUpdateContactRequest): Promise<google.cloud.essentialcontacts.v1.Contact>;

Calls UpdateContact.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateContactRequest](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.iupdatecontactrequest)`   
UpdateContactRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.essentialcontacts.v1.Contact](https://docs.cloud.google.com/nodejs/docs/reference/essential-contacts/latest/essential-contacts/protos.google.cloud.essentialcontacts.v1.contact)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
