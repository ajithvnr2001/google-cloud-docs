---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec
title: Vertex AI v1beta1 API - Class NasJobSpec.Types.MultiTrialAlgorithmSpec (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:34.515864+00:00
---

# Vertex AI v1beta1 API - Class NasJobSpec.Types.MultiTrialAlgorithmSpec (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class NasJobSpec.Types.MultiTrialAlgorithmSpec (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class NasJobSpec.Types.MultiTrialAlgorithmSpec : IMessage<NasJobSpec.Types.MultiTrialAlgorithmSpec>, IEquatable<NasJobSpec.Types.MultiTrialAlgorithmSpec>, IDeepCloneable<NasJobSpec.Types.MultiTrialAlgorithmSpec>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class NasJobSpec.Types.MultiTrialAlgorithmSpec.

The spec of multi-trial Neural Architecture Search (NAS).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > NasJobSpec.Types.MultiTrialAlgorithmSpec

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[NasJobSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types)[MultiTrialAlgorithmSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[NasJobSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types)[MultiTrialAlgorithmSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[NasJobSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types)[MultiTrialAlgorithmSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### MultiTrialAlgorithmSpec()
    
    
    public MultiTrialAlgorithmSpec()

### MultiTrialAlgorithmSpec(MultiTrialAlgorithmSpec)
    
    
    public MultiTrialAlgorithmSpec(NasJobSpec.Types.MultiTrialAlgorithmSpec other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[NasJobSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types)[MultiTrialAlgorithmSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec)`  
  
  
## Properties 

### Metric
    
    
    public NasJobSpec.Types.MultiTrialAlgorithmSpec.Types.MetricSpec Metric { get; set; }

Metric specs for the NAS job. Validation for this field is done at `multi_trial_algorithm_spec` field.

**Property Value**  
---  
**Type** | **Description**  
`[NasJobSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types)[MultiTrialAlgorithmSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec.Types)[MetricSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec.Types.MetricSpec)` |   
  
### MultiTrialAlgorithm
    
    
    public NasJobSpec.Types.MultiTrialAlgorithmSpec.Types.MultiTrialAlgorithm MultiTrialAlgorithm { get; set; }

The multi-trial Neural Architecture Search (NAS) algorithm type. Defaults to `REINFORCEMENT_LEARNING`.

**Property Value**  
---  
**Type** | **Description**  
`[NasJobSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types)[MultiTrialAlgorithmSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec.Types)[MultiTrialAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec.Types.MultiTrialAlgorithm)` |   
  
### SearchTrialSpec
    
    
    public NasJobSpec.Types.MultiTrialAlgorithmSpec.Types.SearchTrialSpec SearchTrialSpec { get; set; }

Required. Spec for search trials.

**Property Value**  
---  
**Type** | **Description**  
`[NasJobSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types)[MultiTrialAlgorithmSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec.Types)[SearchTrialSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec.Types.SearchTrialSpec)` |   
  
### TrainTrialSpec
    
    
    public NasJobSpec.Types.MultiTrialAlgorithmSpec.Types.TrainTrialSpec TrainTrialSpec { get; set; }

Spec for train trials. Top N [TrainTrialSpec.max_parallel_trial_count] search trials will be trained for every M [TrainTrialSpec.frequency] trials searched.

**Property Value**  
---  
**Type** | **Description**  
`[NasJobSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types)[MultiTrialAlgorithmSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec.Types)[TrainTrialSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NasJobSpec.Types.MultiTrialAlgorithmSpec.Types.TrainTrialSpec)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
