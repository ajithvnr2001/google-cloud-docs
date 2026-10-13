---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetSupportEventSubscriptionRequest
title: Google Cloud Support v2 API - Class GetSupportEventSubscriptionRequest (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:40.891318+00:00
---

# Google Cloud Support v2 API - Class GetSupportEventSubscriptionRequest (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetSupportEventSubscriptionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Support v2 API - Class GetSupportEventSubscriptionRequest (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class GetSupportEventSubscriptionRequest : IMessage<GetSupportEventSubscriptionRequest>, IEquatable<GetSupportEventSubscriptionRequest>, IDeepCloneable<GetSupportEventSubscriptionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Support v2 API class GetSupportEventSubscriptionRequest.

Request message for GetSupportEventSubscription.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetSupportEventSubscriptionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetSupportEventSubscriptionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetSupportEventSubscriptionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetSupportEventSubscriptionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetSupportEventSubscriptionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetSupportEventSubscriptionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetSupportEventSubscriptionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Support.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2)

## Assembly

Google.Cloud.Support.V2.dll

## Constructors 

### GetSupportEventSubscriptionRequest()
    
    
    public GetSupportEventSubscriptionRequest()

### GetSupportEventSubscriptionRequest(GetSupportEventSubscriptionRequest)
    
    
    public GetSupportEventSubscriptionRequest(GetSupportEventSubscriptionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetSupportEventSubscriptionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetSupportEventSubscriptionRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The name of the support event subscription to retrieve. Format: organizations/{organization_id}/supportEventSubscriptions/{subscription_id}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SupportEventSubscriptionName
    
    
    public SupportEventSubscriptionName SupportEventSubscriptionName { get; set; }

[SupportEventSubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SupportEventSubscriptionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.GetSupportEventSubscriptionRequest#Google_Cloud_Support_V2_GetSupportEventSubscriptionRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SupportEventSubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.SupportEventSubscriptionName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
