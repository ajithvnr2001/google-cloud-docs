---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig
title: Policy Simulator v1 API - Class ReplayConfig (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:40.560723+00:00
---

# Policy Simulator v1 API - Class ReplayConfig (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Policy Simulator v1 API - Class ReplayConfig (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.3.0/Google.Cloud.PolicySimulator.V1.ReplayConfig)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.2.0/Google.Cloud.PolicySimulator.V1.ReplayConfig)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.1.0/Google.Cloud.PolicySimulator.V1.ReplayConfig)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.0.0/Google.Cloud.PolicySimulator.V1.ReplayConfig)


    
    
    public sealed class ReplayConfig : IMessage<ReplayConfig>, IEquatable<ReplayConfig>, IDeepCloneable<ReplayConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Policy Simulator v1 API class ReplayConfig.

The configuration used for a [Replay][google.cloud.policysimulator.v1.Replay].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReplayConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReplayConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReplayConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReplayConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PolicySimulator.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1)

## Assembly

Google.Cloud.PolicySimulator.V1.dll

## Constructors 

### ReplayConfig()
    
    
    public ReplayConfig()

### ReplayConfig(ReplayConfig)
    
    
    public ReplayConfig(ReplayConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReplayConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig)`  
  
  
## Properties 

### LogSource
    
    
    public ReplayConfig.Types.LogSource LogSource { get; set; }

The logs to use as input for the [Replay][google.cloud.policysimulator.v1.Replay].

**Property Value**  
---  
**Type** | **Description**  
`[ReplayConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig.Types)[LogSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ReplayConfig.Types.LogSource)` |   
  
### PolicyOverlay
    
    
    public MapField<string, Policy> PolicyOverlay { get; }

A mapping of the resources that you want to simulate policies for and the policies that you want to simulate.

Keys are the full resource names for the resources. For example, `//cloudresourcemanager.googleapis.com/projects/my-project`. For examples of full resource names for Google Cloud services, see <https://cloud.google.com/iam/help/troubleshooter/full-resource-names>.

Values are [Policy][google.iam.v1.Policy] objects representing the policies that you want to simulate.

Replays automatically take into account any IAM policies inherited through the resource hierarchy, and any policies set on descendant resources. You do not need to include these policies in the policy overlay.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V1/latest/Google.Cloud.Iam.V1.Policy.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
