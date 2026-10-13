---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ShellCommand
title: Workload Manager v1 API - Class ShellCommand (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:31.393167+00:00
---

# Workload Manager v1 API - Class ShellCommand (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ShellCommand

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Workload Manager v1 API - Class ShellCommand (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class ShellCommand : IMessage<ShellCommand>, IEquatable<ShellCommand>, IDeepCloneable<ShellCommand>, IBufferMessage, IMessage

Reference documentation and code samples for the Workload Manager v1 API class ShellCommand.

A ShellCommand is invoked via the agent's command line executor.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ShellCommand

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ShellCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ShellCommand), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ShellCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ShellCommand), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ShellCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ShellCommand), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.WorkloadManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1)

## Assembly

Google.Cloud.WorkloadManager.V1.dll

## Constructors 

### ShellCommand()
    
    
    public ShellCommand()

### ShellCommand(ShellCommand)
    
    
    public ShellCommand(ShellCommand other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ShellCommand](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ShellCommand)`  
  
  
## Properties 

### Args
    
    
    public string Args { get; set; }

Arguments to be passed to the command.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Command
    
    
    public string Command { get; set; }

The name of the command to be executed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TimeoutSeconds
    
    
    public int TimeoutSeconds { get; set; }

Optional. If not specified, the default timeout is 60 seconds.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-22 UTC."],[],[]] 
