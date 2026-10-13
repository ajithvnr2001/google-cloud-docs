---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetTopicRequest
title: Cloud Pub/Sub v1 API - Class GetTopicRequest (3.39.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:52.708549+00:00
---

# Cloud Pub/Sub v1 API - Class GetTopicRequest (3.39.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetTopicRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Pub/Sub v1 API - Class GetTopicRequest (3.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.39.0 (latest)  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.1  3.9.1  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class GetTopicRequest : IMessage<GetTopicRequest>, IEquatable<GetTopicRequest>, IDeepCloneable<GetTopicRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Pub/Sub v1 API class GetTopicRequest.

Request for the GetTopic method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetTopicRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetTopicRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetTopicRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetTopicRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1)

## Assembly

Google.Cloud.PubSub.V1.dll

## Constructors 

### GetTopicRequest()
    
    
    public GetTopicRequest()

### GetTopicRequest(GetTopicRequest)
    
    
    public GetTopicRequest(GetTopicRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetTopicRequest)`  
  
  
## Properties 

### Topic
    
    
    public string Topic { get; set; }

Required. The name of the topic to get. Format is `projects/{project}/topics/{topic}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TopicAsTopicName
    
    
    public TopicName TopicAsTopicName { get; set; }

[TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName)-typed view over the [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.GetTopicRequest#Google_Cloud_PubSub_V1_GetTopicRequest_Topic) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
