---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.Runtime
title: Cloud Functions v2beta API - Class ListRuntimesResponse.Types.Runtime (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:26.362318+00:00
---

# Cloud Functions v2beta API - Class ListRuntimesResponse.Types.Runtime (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.Runtime

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2beta API - Class ListRuntimesResponse.Types.Runtime (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.Runtime)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/1.0.0-beta07/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.Runtime)


    
    
    public sealed class ListRuntimesResponse.Types.Runtime : IMessage<ListRuntimesResponse.Types.Runtime>, IEquatable<ListRuntimesResponse.Types.Runtime>, IDeepCloneable<ListRuntimesResponse.Types.Runtime>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Functions v2beta API class ListRuntimesResponse.Types.Runtime.

Describes a runtime and any special information (e.g., deprecation status) related to it.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListRuntimesResponse.Types.Runtime

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types)[Runtime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.Runtime), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types)[Runtime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.Runtime), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types)[Runtime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.Runtime), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta)

## Assembly

Google.Cloud.Functions.V2Beta.dll

## Constructors 

### Runtime()
    
    
    public Runtime()

### Runtime(Runtime)
    
    
    public Runtime(ListRuntimesResponse.Types.Runtime other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types)[Runtime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.Runtime)`  
  
  
## Properties 

### DecommissionDate
    
    
    public Date DecommissionDate { get; set; }

Decommission date for the runtime.

**Property Value**  
---  
**Type** | **Description**  
`[Date](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date.html)` |   
  
### DeprecationDate
    
    
    public Date DeprecationDate { get; set; }

Deprecation date for the runtime.

**Property Value**  
---  
**Type** | **Description**  
`[Date](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

The user facing name, eg 'Go 1.13', 'Node.js 12', etc.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Environment
    
    
    public Environment Environment { get; set; }

The environment for the runtime.

**Property Value**  
---  
**Type** | **Description**  
`[Environment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.Environment)` |   
  
### Name
    
    
    public string Name { get; set; }

The name of the runtime, e.g., 'go113', 'nodejs12', etc.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Stage
    
    
    public ListRuntimesResponse.Types.RuntimeStage Stage { get; set; }

The stage of life this runtime is in, e.g., BETA, GA, etc.

**Property Value**  
---  
**Type** | **Description**  
`[ListRuntimesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types)[RuntimeStage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.ListRuntimesResponse.Types.RuntimeStage)` |   
  
### Warnings
    
    
    public RepeatedField<string> Warnings { get; }

Warning messages, e.g., a deprecation warning.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
