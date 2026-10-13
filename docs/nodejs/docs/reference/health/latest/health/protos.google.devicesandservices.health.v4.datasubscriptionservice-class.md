---
url: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasubscriptionservice-class
title: Class protos.google.devicesandservices.health.v4.DataSubscriptionService (0.8.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:13.521927+00:00
---

# Class protos.google.devicesandservices.health.v4.DataSubscriptionService (0.8.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasubscriptionservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.devicesandservices.health.v4.DataSubscriptionService (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Represents a DataSubscriptionService

## Inheritance

$protobuf.rpc.Service > protos.google.devicesandservices.health.v4.DataSubscriptionService

## Package

[@google-cloud/health](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataSubscriptionService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataSubscriptionService;

Creates new DataSubscriptionService service using the specified rpc implementation.

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
`[DataSubscriptionService](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.datasubscriptionservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSubscriber(request, callback)
    
    
    public createSubscriber(request: google.devicesandservices.health.v4.ICreateSubscriberRequest, callback: google.devicesandservices.health.v4.DataSubscriptionService.CreateSubscriberCallback): void;

Calls CreateSubscriber.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.icreatesubscriberrequest)`   
CreateSubscriberRequest message or plain object  
`callback` |  `[CreateSubscriberCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSubscriber(request)
    
    
    public createSubscriber(request: google.devicesandservices.health.v4.ICreateSubscriberRequest): Promise<google.longrunning.Operation>;

Calls CreateSubscriber.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.icreatesubscriberrequest)`   
CreateSubscriberRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.longrunning.operation)>` | Promise  
  
### createSubscription(request, callback)
    
    
    public createSubscription(request: google.devicesandservices.health.v4.ICreateSubscriptionRequest, callback: google.devicesandservices.health.v4.DataSubscriptionService.CreateSubscriptionCallback): void;

Calls CreateSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.icreatesubscriptionrequest)`   
CreateSubscriptionRequest message or plain object  
`callback` |  `[CreateSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Subscription  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSubscription(request)
    
    
    public createSubscription(request: google.devicesandservices.health.v4.ICreateSubscriptionRequest): Promise<google.devicesandservices.health.v4.Subscription>;

Calls CreateSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.icreatesubscriptionrequest)`   
CreateSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.Subscription](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.subscription)>` | Promise  
  
### deleteSubscriber(request, callback)
    
    
    public deleteSubscriber(request: google.devicesandservices.health.v4.IDeleteSubscriberRequest, callback: google.devicesandservices.health.v4.DataSubscriptionService.DeleteSubscriberCallback): void;

Calls DeleteSubscriber.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ideletesubscriberrequest)`   
DeleteSubscriberRequest message or plain object  
`callback` |  `[DeleteSubscriberCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSubscriber(request)
    
    
    public deleteSubscriber(request: google.devicesandservices.health.v4.IDeleteSubscriberRequest): Promise<google.longrunning.Operation>;

Calls DeleteSubscriber.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ideletesubscriberrequest)`   
DeleteSubscriberRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.longrunning.operation)>` | Promise  
  
### deleteSubscription(request, callback)
    
    
    public deleteSubscription(request: google.devicesandservices.health.v4.IDeleteSubscriptionRequest, callback: google.devicesandservices.health.v4.DataSubscriptionService.DeleteSubscriptionCallback): void;

Calls DeleteSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ideletesubscriptionrequest)`   
DeleteSubscriptionRequest message or plain object  
`callback` |  `[DeleteSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSubscription(request)
    
    
    public deleteSubscription(request: google.devicesandservices.health.v4.IDeleteSubscriptionRequest): Promise<google.protobuf.Empty>;

Calls DeleteSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ideletesubscriptionrequest)`   
DeleteSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.protobuf.empty)>` | Promise  
  
### listSubscribers(request, callback)
    
    
    public listSubscribers(request: google.devicesandservices.health.v4.IListSubscribersRequest, callback: google.devicesandservices.health.v4.DataSubscriptionService.ListSubscribersCallback): void;

Calls ListSubscribers.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubscribersRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ilistsubscribersrequest)`   
ListSubscribersRequest message or plain object  
`callback` |  `[ListSubscribersCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSubscribersResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubscribers(request)
    
    
    public listSubscribers(request: google.devicesandservices.health.v4.IListSubscribersRequest): Promise<google.devicesandservices.health.v4.ListSubscribersResponse>;

Calls ListSubscribers.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubscribersRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ilistsubscribersrequest)`   
ListSubscribersRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.ListSubscribersResponse](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.listsubscribersresponse)>` | Promise  
  
### listSubscriptions(request, callback)
    
    
    public listSubscriptions(request: google.devicesandservices.health.v4.IListSubscriptionsRequest, callback: google.devicesandservices.health.v4.DataSubscriptionService.ListSubscriptionsCallback): void;

Calls ListSubscriptions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ilistsubscriptionsrequest)`   
ListSubscriptionsRequest message or plain object  
`callback` |  `[ListSubscriptionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSubscriptionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubscriptions(request)
    
    
    public listSubscriptions(request: google.devicesandservices.health.v4.IListSubscriptionsRequest): Promise<google.devicesandservices.health.v4.ListSubscriptionsResponse>;

Calls ListSubscriptions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.ilistsubscriptionsrequest)`   
ListSubscriptionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.ListSubscriptionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.listsubscriptionsresponse)>` | Promise  
  
### updateSubscriber(request, callback)
    
    
    public updateSubscriber(request: google.devicesandservices.health.v4.IUpdateSubscriberRequest, callback: google.devicesandservices.health.v4.DataSubscriptionService.UpdateSubscriberCallback): void;

Calls UpdateSubscriber.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdatesubscriberrequest)`   
UpdateSubscriberRequest message or plain object  
`callback` |  `[UpdateSubscriberCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSubscriber(request)
    
    
    public updateSubscriber(request: google.devicesandservices.health.v4.IUpdateSubscriberRequest): Promise<google.longrunning.Operation>;

Calls UpdateSubscriber.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubscriberRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdatesubscriberrequest)`   
UpdateSubscriberRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.longrunning.operation)>` | Promise  
  
### updateSubscription(request, callback)
    
    
    public updateSubscription(request: google.devicesandservices.health.v4.IUpdateSubscriptionRequest, callback: google.devicesandservices.health.v4.DataSubscriptionService.UpdateSubscriptionCallback): void;

Calls UpdateSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdatesubscriptionrequest)`   
UpdateSubscriptionRequest message or plain object  
`callback` |  `[UpdateSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/overview.html)`   
Node-style callback called with the error, if any, and Subscription  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSubscription(request)
    
    
    public updateSubscription(request: google.devicesandservices.health.v4.IUpdateSubscriptionRequest): Promise<google.devicesandservices.health.v4.Subscription>;

Calls UpdateSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.iupdatesubscriptionrequest)`   
UpdateSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.devicesandservices.health.v4.Subscription](https://docs.cloud.google.com/nodejs/docs/reference/health/latest/health/protos.google.devicesandservices.health.v4.subscription)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
