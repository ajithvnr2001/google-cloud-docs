---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types.MaintenanceWindow
title: AlloyDB v1beta API - Class MaintenanceUpdatePolicy.Types.MaintenanceWindow (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:28.911759+00:00
---

# AlloyDB v1beta API - Class MaintenanceUpdatePolicy.Types.MaintenanceWindow (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types.MaintenanceWindow

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class MaintenanceUpdatePolicy.Types.MaintenanceWindow (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class MaintenanceUpdatePolicy.Types.MaintenanceWindow : IMessage<MaintenanceUpdatePolicy.Types.MaintenanceWindow>, IEquatable<MaintenanceUpdatePolicy.Types.MaintenanceWindow>, IDeepCloneable<MaintenanceUpdatePolicy.Types.MaintenanceWindow>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class MaintenanceUpdatePolicy.Types.MaintenanceWindow.

MaintenanceWindow specifies a preferred day and time for maintenance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MaintenanceUpdatePolicy.Types.MaintenanceWindow

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MaintenanceUpdatePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types)[MaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types.MaintenanceWindow), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MaintenanceUpdatePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types)[MaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types.MaintenanceWindow), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MaintenanceUpdatePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types)[MaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types.MaintenanceWindow), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### MaintenanceWindow()
    
    
    public MaintenanceWindow()

### MaintenanceWindow(MaintenanceWindow)
    
    
    public MaintenanceWindow(MaintenanceUpdatePolicy.Types.MaintenanceWindow other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MaintenanceUpdatePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types)[MaintenanceWindow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy.Types.MaintenanceWindow)`  
  
  
## Properties 

### Day
    
    
    public DayOfWeek Day { get; set; }

Preferred day of the week for maintenance, e.g. MONDAY, TUESDAY, etc.

**Property Value**  
---  
**Type** | **Description**  
`[DayOfWeek](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DayOfWeek.html)` |   
  
### StartTime
    
    
    public TimeOfDay StartTime { get; set; }

Preferred time to start the maintenance operation on the specified day. Maintenance will start within 1 hour of this time.

**Property Value**  
---  
**Type** | **Description**  
`[TimeOfDay](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeOfDay.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
