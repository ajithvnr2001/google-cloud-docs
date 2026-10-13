---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceSchedule
title: Database Center v1beta API - Class ResourceMaintenanceSchedule (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:02.273048+00:00
---

# Database Center v1beta API - Class ResourceMaintenanceSchedule (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceSchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class ResourceMaintenanceSchedule (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class ResourceMaintenanceSchedule : IMessage<ResourceMaintenanceSchedule>, IEquatable<ResourceMaintenanceSchedule>, IDeepCloneable<ResourceMaintenanceSchedule>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class ResourceMaintenanceSchedule.

Maintenance window for the database resource. It specifies preferred time and day of the week and phase in some cases, when the maintenance can start.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResourceMaintenanceSchedule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResourceMaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceSchedule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResourceMaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceSchedule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResourceMaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceSchedule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### ResourceMaintenanceSchedule()
    
    
    public ResourceMaintenanceSchedule()

### ResourceMaintenanceSchedule(ResourceMaintenanceSchedule)
    
    
    public ResourceMaintenanceSchedule(ResourceMaintenanceSchedule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceMaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceSchedule)`  
  
  
## Properties 

### Day
    
    
    public DayOfWeek Day { get; set; }

Optional. Preferred day of the week for maintenance, e.g. MONDAY, TUESDAY, etc.

**Property Value**  
---  
**Type** | **Description**  
`[DayOfWeek](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.DayOfWeek.html)` |   
  
### Phase
    
    
    public Phase Phase { get; set; }

Optional. Phase of the maintenance window. This is to capture order of maintenance. For example, for Cloud SQL resources, this can be used to capture if the maintenance window is in Week1, Week2, Week5, etc. Non production resources are usually part of early phase. For more details, refer to Cloud SQL resources - <https://cloud.google.com/sql/docs/mysql/maintenance>

**Property Value**  
---  
**Type** | **Description**  
`[Phase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Phase)` |   
  
### StartTime
    
    
    public TimeOfDay StartTime { get; set; }

Optional. Preferred time to start the maintenance operation on the specified day.

**Property Value**  
---  
**Type** | **Description**  
`[TimeOfDay](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeOfDay.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
