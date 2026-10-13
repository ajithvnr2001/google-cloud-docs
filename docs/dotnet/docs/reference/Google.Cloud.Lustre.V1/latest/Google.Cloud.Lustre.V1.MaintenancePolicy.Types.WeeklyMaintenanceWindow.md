---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types.WeeklyMaintenanceWindow
title: Google Cloud Managed Lustre v1 API - Class MaintenancePolicy.Types.WeeklyMaintenanceWindow (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:24:27.318843+00:00
---

# Google Cloud Managed Lustre v1 API - Class MaintenancePolicy.Types.WeeklyMaintenanceWindow (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types.WeeklyMaintenanceWindow

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Managed Lustre v1 API - Class MaintenancePolicy.Types.WeeklyMaintenanceWindow (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class MaintenancePolicy.Types.WeeklyMaintenanceWindow : IMessage<MaintenancePolicy.Types.WeeklyMaintenanceWindow>, IEquatable<MaintenancePolicy.Types.WeeklyMaintenanceWindow>, IDeepCloneable<MaintenancePolicy.Types.WeeklyMaintenanceWindow>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Managed Lustre v1 API class MaintenancePolicy.Types.WeeklyMaintenanceWindow.

Weekly time window in which maintenance updates may occur. Duration of the window is currently fixed at 1 hour. Time zone is UTC.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MaintenancePolicy.Types.WeeklyMaintenanceWindow

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types)[WeeklyMaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types.WeeklyMaintenanceWindow), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types)[WeeklyMaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types.WeeklyMaintenanceWindow), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types)[WeeklyMaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types.WeeklyMaintenanceWindow), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Lustre.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1)

## Assembly

Google.Cloud.Lustre.V1.dll

## Constructors 

### WeeklyMaintenanceWindow()
    
    
    public WeeklyMaintenanceWindow()

### WeeklyMaintenanceWindow(WeeklyMaintenanceWindow)
    
    
    public WeeklyMaintenanceWindow(MaintenancePolicy.Types.WeeklyMaintenanceWindow other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types)[WeeklyMaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.MaintenancePolicy.Types.WeeklyMaintenanceWindow)`  
  
  
## Properties 

### DayOfWeek
    
    
    public DayOfWeek DayOfWeek { get; set; }

Required. Day of the week for the maintenance window.

**Property Value**  
---  
**Type** | **Description**  
`[DayOfWeek](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DayOfWeek.html)` |   
  
### StartTime
    
    
    public TimeOfDay StartTime { get; set; }

Required. Start time of the maintenance window in UTC time zone.

**Property Value**  
---  
**Type** | **Description**  
`[TimeOfDay](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeOfDay.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
