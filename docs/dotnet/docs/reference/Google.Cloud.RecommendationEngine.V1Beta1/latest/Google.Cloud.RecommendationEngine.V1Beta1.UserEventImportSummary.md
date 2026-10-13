---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary
title: Recommendations AI v1beta1 API - Class UserEventImportSummary (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:34.249516+00:00
---

# Recommendations AI v1beta1 API - Class UserEventImportSummary (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Recommendations AI v1beta1 API - Class UserEventImportSummary (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/2.0.0-beta06/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/1.0.0-beta03/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary)


    
    
    public sealed class UserEventImportSummary : IMessage<UserEventImportSummary>, IEquatable<UserEventImportSummary>, IDeepCloneable<UserEventImportSummary>, IBufferMessage, IMessage

Reference documentation and code samples for the Recommendations AI v1beta1 API class UserEventImportSummary.

A summary of import result. The UserEventImportSummary summarizes the import status for user events.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UserEventImportSummary

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UserEventImportSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UserEventImportSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UserEventImportSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RecommendationEngine.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1)

## Assembly

Google.Cloud.RecommendationEngine.V1Beta1.dll

## Constructors 

### UserEventImportSummary()
    
    
    public UserEventImportSummary()

### UserEventImportSummary(UserEventImportSummary)
    
    
    public UserEventImportSummary(UserEventImportSummary other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UserEventImportSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventImportSummary)`  
  
  
## Properties 

### JoinedEventsCount
    
    
    public long JoinedEventsCount { get; set; }

Count of user events imported with complete existing catalog information.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### UnjoinedEventsCount
    
    
    public long UnjoinedEventsCount { get; set; }

Count of user events imported, but with catalog information not found in the imported catalog.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
