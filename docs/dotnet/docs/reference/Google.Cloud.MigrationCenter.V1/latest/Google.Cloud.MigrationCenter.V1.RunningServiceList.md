---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.RunningServiceList
title: Migration Center v1 API - Class RunningServiceList (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:37.552638+00:00
---

# Migration Center v1 API - Class RunningServiceList (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.RunningServiceList

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Migration Center v1 API - Class RunningServiceList (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.RunningServiceList)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.4.0/Google.Cloud.MigrationCenter.V1.RunningServiceList)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.3.0/Google.Cloud.MigrationCenter.V1.RunningServiceList)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.2.0/Google.Cloud.MigrationCenter.V1.RunningServiceList)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.1.0/Google.Cloud.MigrationCenter.V1.RunningServiceList)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/1.0.0/Google.Cloud.MigrationCenter.V1.RunningServiceList)


    
    
    public sealed class RunningServiceList : IMessage<RunningServiceList>, IEquatable<RunningServiceList>, IDeepCloneable<RunningServiceList>, IBufferMessage, IMessage

Reference documentation and code samples for the Migration Center v1 API class RunningServiceList.

List of running guest OS services.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RunningServiceList

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RunningServiceList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.RunningServiceList), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RunningServiceList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.RunningServiceList), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RunningServiceList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.RunningServiceList), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.MigrationCenter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1)

## Assembly

Google.Cloud.MigrationCenter.V1.dll

## Constructors 

### RunningServiceList()
    
    
    public RunningServiceList()

### RunningServiceList(RunningServiceList)
    
    
    public RunningServiceList(RunningServiceList other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RunningServiceList](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.RunningServiceList)`  
  
  
## Properties 

### Entries
    
    
    public RepeatedField<RunningService> Entries { get; }

Running service entries.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[RunningService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MigrationCenter.V1/latest/Google.Cloud.MigrationCenter.V1.RunningService)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
