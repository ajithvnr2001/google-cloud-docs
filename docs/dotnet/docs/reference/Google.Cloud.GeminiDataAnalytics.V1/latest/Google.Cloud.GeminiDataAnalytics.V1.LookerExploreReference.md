---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerExploreReference
title: Data Analytics API with Gemini v1 API - Class LookerExploreReference (2.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:25.996659+00:00
---

# Data Analytics API with Gemini v1 API - Class LookerExploreReference (2.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerExploreReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Data Analytics API with Gemini v1 API - Class LookerExploreReference (2.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class LookerExploreReference : IMessage<LookerExploreReference>, IEquatable<LookerExploreReference>, IDeepCloneable<LookerExploreReference>, IBufferMessage, IMessage

Reference documentation and code samples for the Data Analytics API with Gemini v1 API class LookerExploreReference.

Message representing a reference to a single Looker explore.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LookerExploreReference

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[LookerExploreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerExploreReference), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[LookerExploreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerExploreReference), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[LookerExploreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerExploreReference), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GeminiDataAnalytics.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1)

## Assembly

Google.Cloud.GeminiDataAnalytics.V1.dll

## Constructors 

### LookerExploreReference()
    
    
    public LookerExploreReference()

### LookerExploreReference(LookerExploreReference)
    
    
    public LookerExploreReference(LookerExploreReference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[LookerExploreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerExploreReference)`  
  
  
## Properties 

### Explore
    
    
    public string Explore { get; set; }

Required. Looker Explore, as outlined in [Major LookML structures](https://cloud.google.com/looker/docs/lookml-terms-and-concepts#major_lookml_structures). Name of the LookML Explore.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasLookerInstanceUri
    
    
    public bool HasLookerInstanceUri { get; }

Gets whether the "looker_instance_uri" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstanceCase
    
    
    public LookerExploreReference.InstanceOneofCase InstanceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[LookerExploreReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerExploreReference)[InstanceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.LookerExploreReference.InstanceOneofCase)` |   
  
### LookerInstanceUri
    
    
    public string LookerInstanceUri { get; set; }

Required. The base url of the Looker instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LookmlModel
    
    
    public string LookmlModel { get; set; }

Required. Looker model, as outlined in [Major LookML structures](https://cloud.google.com/looker/docs/lookml-terms-and-concepts#major_lookml_structures). Name of the LookML model.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrivateLookerInstanceInfo
    
    
    public PrivateLookerInstanceInfo PrivateLookerInstanceInfo { get; set; }

Private Looker instance info.

**Property Value**  
---  
**Type** | **Description**  
`[PrivateLookerInstanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.PrivateLookerInstanceInfo)` |   
  
### Schema
    
    
    public Schema Schema { get; set; }

Optional. The schema of the datasource.

**Property Value**  
---  
**Type** | **Description**  
`[Schema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1/latest/Google.Cloud.GeminiDataAnalytics.V1.Schema)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
