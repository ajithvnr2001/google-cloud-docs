---
url: https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.subscriber-class
title: Class protos.google.pubsub.v1.Subscriber (0.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:39.823101+00:00
---

# Class protos.google.pubsub.v1.Subscriber (0.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.subscriber-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.pubsub.v1.Subscriber (0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.1 

Represents a Subscriber

## Inheritance

$protobuf.rpc.Service > protos.google.pubsub.v1.Subscriber

## Package

[@google-cloud/pubsub-api](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Subscriber service.

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

### acknowledge(request, callback)
    
    
    public acknowledge(request: google.pubsub.v1.IAcknowledgeRequest, callback: google.pubsub.v1.Subscriber.AcknowledgeCallback): void;

Calls Acknowledge.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.iacknowledgerequest)`   
AcknowledgeRequest message or plain object  
`callback` |  `[AcknowledgeCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### acknowledge(request)
    
    
    public acknowledge(request: google.pubsub.v1.IAcknowledgeRequest): Promise<google.protobuf.Empty>;

Calls Acknowledge.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.iacknowledgerequest)`   
AcknowledgeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.protobuf.empty)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Subscriber;

Creates new Subscriber service using the specified rpc implementation.

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
`[Subscriber](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.subscriber-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSnapshot(request, callback)
    
    
    public createSnapshot(request: google.pubsub.v1.ICreateSnapshotRequest, callback: google.pubsub.v1.Subscriber.CreateSnapshotCallback): void;

Calls CreateSnapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.icreatesnapshotrequest)`   
CreateSnapshotRequest message or plain object  
`callback` |  `[CreateSnapshotCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Snapshot  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSnapshot(request)
    
    
    public createSnapshot(request: google.pubsub.v1.ICreateSnapshotRequest): Promise<google.pubsub.v1.Snapshot>;

Calls CreateSnapshot.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.icreatesnapshotrequest)`   
CreateSnapshotRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.Snapshot](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.snapshot)>` | Promise  
  
### createSubscription(request, callback)
    
    
    public createSubscription(request: google.pubsub.v1.ISubscription, callback: google.pubsub.v1.Subscriber.CreateSubscriptionCallback): void;

Calls CreateSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubscription](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.isubscription)`   
Subscription message or plain object  
`callback` |  `[CreateSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Subscription  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSubscription(request)
    
    
    public createSubscription(request: google.pubsub.v1.ISubscription): Promise<google.pubsub.v1.Subscription>;

Calls CreateSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISubscription](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.isubscription)`   
Subscription message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.Subscription](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.subscription-class)>` | Promise  
  
### deleteSnapshot(request, callback)
    
    
    public deleteSnapshot(request: google.pubsub.v1.IDeleteSnapshotRequest, callback: google.pubsub.v1.Subscriber.DeleteSnapshotCallback): void;

Calls DeleteSnapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ideletesnapshotrequest)`   
DeleteSnapshotRequest message or plain object  
`callback` |  `[DeleteSnapshotCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSnapshot(request)
    
    
    public deleteSnapshot(request: google.pubsub.v1.IDeleteSnapshotRequest): Promise<google.protobuf.Empty>;

Calls DeleteSnapshot.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ideletesnapshotrequest)`   
DeleteSnapshotRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.protobuf.empty)>` | Promise  
  
### deleteSubscription(request, callback)
    
    
    public deleteSubscription(request: google.pubsub.v1.IDeleteSubscriptionRequest, callback: google.pubsub.v1.Subscriber.DeleteSubscriptionCallback): void;

Calls DeleteSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ideletesubscriptionrequest)`   
DeleteSubscriptionRequest message or plain object  
`callback` |  `[DeleteSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSubscription(request)
    
    
    public deleteSubscription(request: google.pubsub.v1.IDeleteSubscriptionRequest): Promise<google.protobuf.Empty>;

Calls DeleteSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ideletesubscriptionrequest)`   
DeleteSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.protobuf.empty)>` | Promise  
  
### getSnapshot(request, callback)
    
    
    public getSnapshot(request: google.pubsub.v1.IGetSnapshotRequest, callback: google.pubsub.v1.Subscriber.GetSnapshotCallback): void;

Calls GetSnapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.igetsnapshotrequest)`   
GetSnapshotRequest message or plain object  
`callback` |  `[GetSnapshotCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Snapshot  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSnapshot(request)
    
    
    public getSnapshot(request: google.pubsub.v1.IGetSnapshotRequest): Promise<google.pubsub.v1.Snapshot>;

Calls GetSnapshot.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.igetsnapshotrequest)`   
GetSnapshotRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.Snapshot](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.snapshot)>` | Promise  
  
### getSubscription(request, callback)
    
    
    public getSubscription(request: google.pubsub.v1.IGetSubscriptionRequest, callback: google.pubsub.v1.Subscriber.GetSubscriptionCallback): void;

Calls GetSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.igetsubscriptionrequest)`   
GetSubscriptionRequest message or plain object  
`callback` |  `[GetSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Subscription  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSubscription(request)
    
    
    public getSubscription(request: google.pubsub.v1.IGetSubscriptionRequest): Promise<google.pubsub.v1.Subscription>;

Calls GetSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.igetsubscriptionrequest)`   
GetSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.Subscription](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.subscription-class)>` | Promise  
  
### listSnapshots(request, callback)
    
    
    public listSnapshots(request: google.pubsub.v1.IListSnapshotsRequest, callback: google.pubsub.v1.Subscriber.ListSnapshotsCallback): void;

Calls ListSnapshots.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ilistsnapshotsrequest)`   
ListSnapshotsRequest message or plain object  
`callback` |  `[ListSnapshotsCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSnapshotsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSnapshots(request)
    
    
    public listSnapshots(request: google.pubsub.v1.IListSnapshotsRequest): Promise<google.pubsub.v1.ListSnapshotsResponse>;

Calls ListSnapshots.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSnapshotsRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ilistsnapshotsrequest)`   
ListSnapshotsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.ListSnapshotsResponse](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.listsnapshotsresponse)>` | Promise  
  
### listSubscriptions(request, callback)
    
    
    public listSubscriptions(request: google.pubsub.v1.IListSubscriptionsRequest, callback: google.pubsub.v1.Subscriber.ListSubscriptionsCallback): void;

Calls ListSubscriptions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ilistsubscriptionsrequest)`   
ListSubscriptionsRequest message or plain object  
`callback` |  `[ListSubscriptionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSubscriptionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSubscriptions(request)
    
    
    public listSubscriptions(request: google.pubsub.v1.IListSubscriptionsRequest): Promise<google.pubsub.v1.ListSubscriptionsResponse>;

Calls ListSubscriptions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSubscriptionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ilistsubscriptionsrequest)`   
ListSubscriptionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.ListSubscriptionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.listsubscriptionsresponse)>` | Promise  
  
### modifyAckDeadline(request, callback)
    
    
    public modifyAckDeadline(request: google.pubsub.v1.IModifyAckDeadlineRequest, callback: google.pubsub.v1.Subscriber.ModifyAckDeadlineCallback): void;

Calls ModifyAckDeadline.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IModifyAckDeadlineRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.imodifyackdeadlinerequest)`   
ModifyAckDeadlineRequest message or plain object  
`callback` |  `[ModifyAckDeadlineCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### modifyAckDeadline(request)
    
    
    public modifyAckDeadline(request: google.pubsub.v1.IModifyAckDeadlineRequest): Promise<google.protobuf.Empty>;

Calls ModifyAckDeadline.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IModifyAckDeadlineRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.imodifyackdeadlinerequest)`   
ModifyAckDeadlineRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.protobuf.empty)>` | Promise  
  
### modifyPushConfig(request, callback)
    
    
    public modifyPushConfig(request: google.pubsub.v1.IModifyPushConfigRequest, callback: google.pubsub.v1.Subscriber.ModifyPushConfigCallback): void;

Calls ModifyPushConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IModifyPushConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.imodifypushconfigrequest)`   
ModifyPushConfigRequest message or plain object  
`callback` |  `[ModifyPushConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### modifyPushConfig(request)
    
    
    public modifyPushConfig(request: google.pubsub.v1.IModifyPushConfigRequest): Promise<google.protobuf.Empty>;

Calls ModifyPushConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IModifyPushConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.imodifypushconfigrequest)`   
ModifyPushConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.protobuf.empty)>` | Promise  
  
### pull(request, callback)
    
    
    public pull(request: google.pubsub.v1.IPullRequest, callback: google.pubsub.v1.Subscriber.PullCallback): void;

Calls Pull.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPullRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ipullrequest)`   
PullRequest message or plain object  
`callback` |  `[PullCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and PullResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### pull(request)
    
    
    public pull(request: google.pubsub.v1.IPullRequest): Promise<google.pubsub.v1.PullResponse>;

Calls Pull.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPullRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.ipullrequest)`   
PullRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.PullResponse](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.pullresponse)>` | Promise  
  
### seek(request, callback)
    
    
    public seek(request: google.pubsub.v1.ISeekRequest, callback: google.pubsub.v1.Subscriber.SeekCallback): void;

Calls Seek.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISeekRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.iseekrequest)`   
SeekRequest message or plain object  
`callback` |  `[SeekCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and SeekResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### seek(request)
    
    
    public seek(request: google.pubsub.v1.ISeekRequest): Promise<google.pubsub.v1.SeekResponse>;

Calls Seek.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISeekRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.iseekrequest)`   
SeekRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.SeekResponse](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.seekresponse)>` | Promise  
  
### streamingPull(request, callback)
    
    
    public streamingPull(request: google.pubsub.v1.IStreamingPullRequest, callback: google.pubsub.v1.Subscriber.StreamingPullCallback): void;

Calls StreamingPull.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStreamingPullRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.istreamingpullrequest)`   
StreamingPullRequest message or plain object  
`callback` |  `[StreamingPullCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and StreamingPullResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### streamingPull(request)
    
    
    public streamingPull(request: google.pubsub.v1.IStreamingPullRequest): Promise<google.pubsub.v1.StreamingPullResponse>;

Calls StreamingPull.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStreamingPullRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.istreamingpullrequest)`   
StreamingPullRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.StreamingPullResponse](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.streamingpullresponse-class)>` | Promise  
  
### updateSnapshot(request, callback)
    
    
    public updateSnapshot(request: google.pubsub.v1.IUpdateSnapshotRequest, callback: google.pubsub.v1.Subscriber.UpdateSnapshotCallback): void;

Calls UpdateSnapshot.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.iupdatesnapshotrequest)`   
UpdateSnapshotRequest message or plain object  
`callback` |  `[UpdateSnapshotCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Snapshot  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSnapshot(request)
    
    
    public updateSnapshot(request: google.pubsub.v1.IUpdateSnapshotRequest): Promise<google.pubsub.v1.Snapshot>;

Calls UpdateSnapshot.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSnapshotRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.iupdatesnapshotrequest)`   
UpdateSnapshotRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.Snapshot](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.snapshot)>` | Promise  
  
### updateSubscription(request, callback)
    
    
    public updateSubscription(request: google.pubsub.v1.IUpdateSubscriptionRequest, callback: google.pubsub.v1.Subscriber.UpdateSubscriptionCallback): void;

Calls UpdateSubscription.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.iupdatesubscriptionrequest)`   
UpdateSubscriptionRequest message or plain object  
`callback` |  `[UpdateSubscriptionCallback](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/overview.html)`   
Node-style callback called with the error, if any, and Subscription  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSubscription(request)
    
    
    public updateSubscription(request: google.pubsub.v1.IUpdateSubscriptionRequest): Promise<google.pubsub.v1.Subscription>;

Calls UpdateSubscription.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSubscriptionRequest](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.iupdatesubscriptionrequest)`   
UpdateSubscriptionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.pubsub.v1.Subscription](https://docs.cloud.google.com/nodejs/docs/reference/pubsub-api/latest/pubsub-api/protos.google.pubsub.v1.subscription-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
