---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIDependentRequestsConfig
title: Chronicle v1 API - Class CustomAPIDependentRequestsConfig (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:51.938323+00:00
---

# Chronicle v1 API - Class CustomAPIDependentRequestsConfig (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIDependentRequestsConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class CustomAPIDependentRequestsConfig (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class CustomAPIDependentRequestsConfig : IMessage<CustomAPIDependentRequestsConfig>, IEquatable<CustomAPIDependentRequestsConfig>, IDeepCloneable<CustomAPIDependentRequestsConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class CustomAPIDependentRequestsConfig.

Configuration for dependent requests (child chaining).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CustomAPIDependentRequestsConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CustomAPIDependentRequestsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIDependentRequestsConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CustomAPIDependentRequestsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIDependentRequestsConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CustomAPIDependentRequestsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIDependentRequestsConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### CustomAPIDependentRequestsConfig()
    
    
    public CustomAPIDependentRequestsConfig()

### CustomAPIDependentRequestsConfig(CustomAPIDependentRequestsConfig)
    
    
    public CustomAPIDependentRequestsConfig(CustomAPIDependentRequestsConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CustomAPIDependentRequestsConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPIDependentRequestsConfig)`  
  
  
## Properties 

### DependentRequests
    
    
    public RepeatedField<CustomAPITransferNode> DependentRequests { get; }

Optional. Add follow-up API calls triggered for each item found in the primary request (e.g., fetching full event details for a list of basic alert IDs). Note: In MVP, the child depth fan-out limit is capped at 1.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CustomAPITransferNode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CustomAPITransferNode)` |   
  
### ItemIdJsonPath
    
    
    public string ItemIdJsonPath { get; set; }

Required. Enter the specific field in the response that uniquely identifies an individual record or alert.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ItemIdVariable
    
    
    public string ItemIdVariable { get; set; }

Optional. Specify a custom variable name to hold the extracted ID, which can be linked as a placeholder in dependent requests.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
