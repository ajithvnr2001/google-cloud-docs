---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.KernelRootkit
title: Security Command Center v2 API - Class KernelRootkit (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:52.300175+00:00
---

# Security Command Center v2 API - Class KernelRootkit (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.KernelRootkit

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class KernelRootkit (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class KernelRootkit : IMessage<KernelRootkit>, IEquatable<KernelRootkit>, IDeepCloneable<KernelRootkit>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Command Center v2 API class KernelRootkit.

Kernel mode rootkit signatures.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > KernelRootkit

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[KernelRootkit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.KernelRootkit), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[KernelRootkit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.KernelRootkit), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[KernelRootkit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.KernelRootkit), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### KernelRootkit()
    
    
    public KernelRootkit()

### KernelRootkit(KernelRootkit)
    
    
    public KernelRootkit(KernelRootkit other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[KernelRootkit](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.KernelRootkit)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Rootkit name, when available.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UnexpectedCodeModification
    
    
    public bool UnexpectedCodeModification { get; set; }

True if unexpected modifications of kernel code memory are present.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### UnexpectedFtraceHandler
    
    
    public bool UnexpectedFtraceHandler { get; set; }

True if `ftrace` points are present with callbacks pointing to regions that are not in the expected kernel or module code range.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### UnexpectedInterruptHandler
    
    
    public bool UnexpectedInterruptHandler { get; set; }

True if interrupt handlers that are are not in the expected kernel or module code regions are present.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### UnexpectedKernelCodePages
    
    
    public bool UnexpectedKernelCodePages { get; set; }

True if kernel code pages that are not in the expected kernel or module code regions are present.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### UnexpectedKprobeHandler
    
    
    public bool UnexpectedKprobeHandler { get; set; }

True if `kprobe` points are present with callbacks pointing to regions that are not in the expected kernel or module code range.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### UnexpectedProcessesInRunqueue
    
    
    public bool UnexpectedProcessesInRunqueue { get; set; }

True if unexpected processes in the scheduler run queue are present. Such processes are in the run queue, but not in the process task list.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### UnexpectedReadOnlyDataModification
    
    
    public bool UnexpectedReadOnlyDataModification { get; set; }

True if unexpected modifications of kernel read-only data memory are present.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### UnexpectedSystemCallHandler
    
    
    public bool UnexpectedSystemCallHandler { get; set; }

True if system call handlers that are are not in the expected kernel or module code regions are present.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
