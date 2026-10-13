---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator
title: Vertex AI v1beta1 API - Class OnlineEvaluator (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:48.772085+00:00
---

# Vertex AI v1beta1 API - Class OnlineEvaluator (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class OnlineEvaluator (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class OnlineEvaluator : IMessage<OnlineEvaluator>, IEquatable<OnlineEvaluator>, IDeepCloneable<OnlineEvaluator>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class OnlineEvaluator.

An OnlineEvaluator contains the configuration for an Online Evaluation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OnlineEvaluator

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### OnlineEvaluator()
    
    
    public OnlineEvaluator()

### OnlineEvaluator(OnlineEvaluator)
    
    
    public OnlineEvaluator(OnlineEvaluator other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator)`  
  
  
## Properties 

### AgentResource
    
    
    public string AgentResource { get; set; }

Required. Immutable. The name of the agent that the OnlineEvaluator evaluates periodically. This value is used to filter the traces with a matching cloud.resource_id and link the evaluation results with relevant dashboards/UIs.

This field is immutable. Once set, it cannot be changed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CloudObservability
    
    
    public OnlineEvaluator.Types.CloudObservability CloudObservability { get; set; }

Data source for the OnlineEvaluator, based on GCP Observability stack (Cloud Trace & Cloud Logging).

**Property Value**  
---  
**Type** | **Description**  
`[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.Types)[CloudObservability](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.Types.CloudObservability)` |   
  
### Config
    
    
    public OnlineEvaluator.Types.Config Config { get; set; }

Required. Configuration for the OnlineEvaluator.

**Property Value**  
---  
**Type** | **Description**  
`[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.Types)[Config](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.Types.Config)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Timestamp when the OnlineEvaluator was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DataSourceCase
    
    
    public OnlineEvaluator.DataSourceOneofCase DataSourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator)[DataSourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.DataSourceOneofCase)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. Human-readable name for the `OnlineEvaluator`.

The name doesn't have to be unique.

The name can consist of any UTF-8 characters. The maximum length is `63` characters. If the display name exceeds max characters, an `INVALID_ARGUMENT` error is returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MetricSources
    
    
    public RepeatedField<MetricSource> MetricSources { get; }

Required. A list of metric sources to be used for evaluating samples. At least one MetricSource must be provided. Right now, only predefined metrics and registered metrics are supported.

Every registered metric must have `display_name` (or `title`) and `score_range` defined. Otherwise, the evaluations will fail.

The maximum number of `metric_sources` is 25.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[MetricSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MetricSource)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The resource name of the OnlineEvaluator. Format: projects/{project}/locations/{location}/onlineEvaluators/{id}.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OnlineEvaluatorName
    
    
    public OnlineEvaluatorName OnlineEvaluatorName { get; set; }

[OnlineEvaluatorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluatorName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator#Google_Cloud_AIPlatform_V1Beta1_OnlineEvaluator_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OnlineEvaluatorName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluatorName)` |   
  
### State
    
    
    public OnlineEvaluator.Types.State State { get; set; }

Output only. The state of the OnlineEvaluator.

**Property Value**  
---  
**Type** | **Description**  
`[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.Types.State)` |   
  
### StateDetails
    
    
    public RepeatedField<OnlineEvaluator.Types.StateDetails> StateDetails { get; }

Output only. Contains additional information about the state of the OnlineEvaluator. This is used to provide more details in the event of a failure.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[OnlineEvaluator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.Types)[StateDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluator.Types.StateDetails)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Timestamp when the OnlineEvaluator was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
