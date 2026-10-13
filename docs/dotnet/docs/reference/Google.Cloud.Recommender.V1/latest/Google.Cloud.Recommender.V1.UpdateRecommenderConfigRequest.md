---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.UpdateRecommenderConfigRequest
title: Google Cloud Recommender v1 API - Class UpdateRecommenderConfigRequest (3.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:20.193642+00:00
---

# Google Cloud Recommender v1 API - Class UpdateRecommenderConfigRequest (3.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.UpdateRecommenderConfigRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Recommender v1 API - Class UpdateRecommenderConfigRequest (3.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.9.0 (latest)  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.8.0  2.7.0  2.6.0  2.5.0 
    
    
    public sealed class UpdateRecommenderConfigRequest : IMessage<UpdateRecommenderConfigRequest>, IEquatable<UpdateRecommenderConfigRequest>, IDeepCloneable<UpdateRecommenderConfigRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Recommender v1 API class UpdateRecommenderConfigRequest.

Request for the `UpdateRecommenderConfig` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateRecommenderConfigRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateRecommenderConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.UpdateRecommenderConfigRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateRecommenderConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.UpdateRecommenderConfigRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateRecommenderConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.UpdateRecommenderConfigRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Recommender.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1)

## Assembly

Google.Cloud.Recommender.V1.dll

## Constructors 

### UpdateRecommenderConfigRequest()
    
    
    public UpdateRecommenderConfigRequest()

### UpdateRecommenderConfigRequest(UpdateRecommenderConfigRequest)
    
    
    public UpdateRecommenderConfigRequest(UpdateRecommenderConfigRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateRecommenderConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.UpdateRecommenderConfigRequest)`  
  
  
## Properties 

### RecommenderConfig
    
    
    public RecommenderConfig RecommenderConfig { get; set; }

Required. The RecommenderConfig to update.

**Property Value**  
---  
**Type** | **Description**  
`[RecommenderConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Recommender.V1/latest/Google.Cloud.Recommender.V1.RecommenderConfig)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

The list of fields to be updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

If true, validate the request and preview the change, but do not actually update it.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
