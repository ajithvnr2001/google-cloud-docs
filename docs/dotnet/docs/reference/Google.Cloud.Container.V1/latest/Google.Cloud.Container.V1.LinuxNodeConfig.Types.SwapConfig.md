---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig
title: Google Kubernetes Engine v1 API - Class LinuxNodeConfig.Types.SwapConfig (3.40.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:42.688290+00:00
---

# Google Kubernetes Engine v1 API - Class LinuxNodeConfig.Types.SwapConfig (3.40.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Kubernetes Engine v1 API - Class LinuxNodeConfig.Types.SwapConfig (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0 
    
    
    public sealed class LinuxNodeConfig.Types.SwapConfig : IMessage<LinuxNodeConfig.Types.SwapConfig>, IEquatable<LinuxNodeConfig.Types.SwapConfig>, IDeepCloneable<LinuxNodeConfig.Types.SwapConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Kubernetes Engine v1 API class LinuxNodeConfig.Types.SwapConfig.

Configuration for swap memory on a node pool.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LinuxNodeConfig.Types.SwapConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Container.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1)

## Assembly

Google.Cloud.Container.V1.dll

## Constructors 

### SwapConfig()
    
    
    public SwapConfig()

### SwapConfig(SwapConfig)
    
    
    public SwapConfig(LinuxNodeConfig.Types.SwapConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig)`  
  
  
## Properties 

### BootDiskProfile
    
    
    public LinuxNodeConfig.Types.SwapConfig.Types.BootDiskProfile BootDiskProfile { get; set; }

Swap on the node's boot disk.

**Property Value**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.Types)[BootDiskProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.Types.BootDiskProfile)` |   
  
### DedicatedLocalSsdProfile
    
    
    public LinuxNodeConfig.Types.SwapConfig.Types.DedicatedLocalSsdProfile DedicatedLocalSsdProfile { get; set; }

Provisions a new, separate local NVMe SSD exclusively for swap.

**Property Value**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.Types)[DedicatedLocalSsdProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.Types.DedicatedLocalSsdProfile)` |   
  
### Enabled
    
    
    public bool Enabled { get; set; }

Optional. Enables or disables swap for the node pool.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EncryptionConfig
    
    
    public LinuxNodeConfig.Types.SwapConfig.Types.EncryptionConfig EncryptionConfig { get; set; }

Optional. If omitted, swap space is encrypted by default.

**Property Value**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.Types)[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.Types.EncryptionConfig)` |   
  
### EphemeralLocalSsdProfile
    
    
    public LinuxNodeConfig.Types.SwapConfig.Types.EphemeralLocalSsdProfile EphemeralLocalSsdProfile { get; set; }

Swap on the local SSD shared with pod ephemeral storage.

**Property Value**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.Types)[EphemeralLocalSsdProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.Types.EphemeralLocalSsdProfile)` |   
  
### HasEnabled
    
    
    public bool HasEnabled { get; }

Gets whether the "enabled" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### PerformanceProfileCase
    
    
    public LinuxNodeConfig.Types.SwapConfig.PerformanceProfileOneofCase PerformanceProfileCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types)[SwapConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig)[PerformanceProfileOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Container.V1/latest/Google.Cloud.Container.V1.LinuxNodeConfig.Types.SwapConfig.PerformanceProfileOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
