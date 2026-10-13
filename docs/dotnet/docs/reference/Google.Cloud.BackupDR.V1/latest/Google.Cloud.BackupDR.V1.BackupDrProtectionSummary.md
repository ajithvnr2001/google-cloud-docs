---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupDrProtectionSummary
title: Backup and DR Service v1 API - Class BackupDrProtectionSummary (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:51.780624+00:00
---

# Backup and DR Service v1 API - Class BackupDrProtectionSummary (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupDrProtectionSummary

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup and DR Service v1 API - Class BackupDrProtectionSummary (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.0 (latest)  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.2.0  1.1.0  1.0.0-beta02 
    
    
    public static class BackupDrProtectionSummary

Reference documentation and code samples for the Backup and DR Service v1 API class BackupDrProtectionSummary.

The Protection Summary service.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackupDrProtectionSummary

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BackupDR.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1)

## Assembly

Google.Cloud.BackupDR.V1.dll

## Methods 

### BindService(BackupDrProtectionSummaryBase)
    
    
    public static ServerServiceDefinition BindService(BackupDrProtectionSummary.BackupDrProtectionSummaryBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[BackupDrProtectionSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupDrProtectionSummary)[BackupDrProtectionSummaryBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupDrProtectionSummary.BackupDrProtectionSummaryBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, BackupDrProtectionSummaryBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, BackupDrProtectionSummary.BackupDrProtectionSummaryBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[BackupDrProtectionSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupDrProtectionSummary)[BackupDrProtectionSummaryBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupDrProtectionSummary.BackupDrProtectionSummaryBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-31 UTC."],[],[]] 
