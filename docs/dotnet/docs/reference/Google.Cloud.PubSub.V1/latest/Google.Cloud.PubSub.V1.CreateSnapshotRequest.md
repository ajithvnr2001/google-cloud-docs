---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSnapshotRequest
title: Cloud Pub/Sub v1 API - Class CreateSnapshotRequest (3.39.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:35.351147+00:00
---

# Cloud Pub/Sub v1 API - Class CreateSnapshotRequest (3.39.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSnapshotRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Pub/Sub v1 API - Class CreateSnapshotRequest (3.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.39.0 (latest)  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.1  3.9.1  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class CreateSnapshotRequest : IMessage<CreateSnapshotRequest>, IEquatable<CreateSnapshotRequest>, IDeepCloneable<CreateSnapshotRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Pub/Sub v1 API class CreateSnapshotRequest.

Request for the `CreateSnapshot` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateSnapshotRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSnapshotRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSnapshotRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSnapshotRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1)

## Assembly

Google.Cloud.PubSub.V1.dll

## Constructors 

### CreateSnapshotRequest()
    
    
    public CreateSnapshotRequest()

### CreateSnapshotRequest(CreateSnapshotRequest)
    
    
    public CreateSnapshotRequest(CreateSnapshotRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSnapshotRequest)`  
  
  
## Properties 

### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels).

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. User-provided name for this snapshot. If the name is not provided in the request, the server will assign a random name for this snapshot on the same project as the subscription. Note that for REST API requests, you must specify a name. See the [resource name rules](https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names). Format is `projects/{project}/snapshots/{snap}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SnapshotName
    
    
    public SnapshotName SnapshotName { get; set; }

[SnapshotName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SnapshotName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSnapshotRequest#Google_Cloud_PubSub_V1_CreateSnapshotRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SnapshotName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SnapshotName)` |   
  
### Subscription
    
    
    public string Subscription { get; set; }

Required. The subscription whose backlog the snapshot retains. Specifically, the created snapshot is guaranteed to retain: (a) The existing backlog on the subscription. More precisely, this is defined as the messages in the subscription's backlog that are unacknowledged upon the successful completion of the `CreateSnapshot` request; as well as: (b) Any messages published to the subscription's topic following the successful completion of the CreateSnapshot request. Format is `projects/{project}/subscriptions/{sub}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubscriptionAsSubscriptionName
    
    
    public SubscriptionName SubscriptionAsSubscriptionName { get; set; }

[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName)-typed view over the [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CreateSnapshotRequest#Google_Cloud_PubSub_V1_CreateSnapshotRequest_Subscription) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName)` |   
  
### Tags
    
    
    public MapField<string, string> Tags { get; }

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing" See https://{$universe.dns_names.final_documentation_domain}/pubsub/docs/tags for more information on using tags with Pub/Sub resources.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
