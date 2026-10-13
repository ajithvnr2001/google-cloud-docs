---
url: https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1.isubscription
title: Interface protos.google.apps.events.subscriptions.v1.ISubscription (0.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:14.918143+00:00
---

# Interface protos.google.apps.events.subscriptions.v1.ISubscription (0.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/subscriptions/protos.google.apps.events.subscriptions.v1.isubscription

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.apps.events.subscriptions.v1.ISubscription (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.1 (latest)  0.3.0 

Properties of a Subscription.

## Package

[@google-cloud/subscriptions](https://docs.cloud.google.com/nodejs/docs/reference/subscriptions/latest/overview.html)

## Properties 

### authority
    
    
    authority?: (string|null);

Subscription authority

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Subscription createTime

### etag
    
    
    etag?: (string|null);

Subscription etag

### eventTypes
    
    
    eventTypes?: (string[]|null);

Subscription eventTypes

### expireTime
    
    
    expireTime?: (google.protobuf.ITimestamp|null);

Subscription expireTime

### name
    
    
    name?: (string|null);

Subscription name

### notificationEndpoint
    
    
    notificationEndpoint?: (google.apps.events.subscriptions.v1.INotificationEndpoint|null);

Subscription notificationEndpoint

### payloadOptions
    
    
    payloadOptions?: (google.apps.events.subscriptions.v1.IPayloadOptions|null);

Subscription payloadOptions

### reconciling
    
    
    reconciling?: (boolean|null);

Subscription reconciling

### state
    
    
    state?: (google.apps.events.subscriptions.v1.Subscription.State|keyof typeof google.apps.events.subscriptions.v1.Subscription.State|null);

Subscription state

### suspensionReason
    
    
    suspensionReason?: (google.apps.events.subscriptions.v1.Subscription.ErrorType|keyof typeof google.apps.events.subscriptions.v1.Subscription.ErrorType|null);

Subscription suspensionReason

### targetResource
    
    
    targetResource?: (string|null);

Subscription targetResource

### ttl
    
    
    ttl?: (google.protobuf.IDuration|null);

Subscription ttl

### uid
    
    
    uid?: (string|null);

Subscription uid

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Subscription updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
