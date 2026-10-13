---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceDenySchedule
title: Database Center v1beta API - Class ResourceMaintenanceDenySchedule (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:02.076245+00:00
---

# Database Center v1beta API - Class ResourceMaintenanceDenySchedule (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceDenySchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class ResourceMaintenanceDenySchedule (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class ResourceMaintenanceDenySchedule : IMessage<ResourceMaintenanceDenySchedule>, IEquatable<ResourceMaintenanceDenySchedule>, IDeepCloneable<ResourceMaintenanceDenySchedule>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class ResourceMaintenanceDenySchedule.

Deny maintenance period for the database resource. It specifies the time range during which the maintenance cannot start. This is configured by the customer.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResourceMaintenanceDenySchedule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceDenySchedule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceDenySchedule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceDenySchedule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### ResourceMaintenanceDenySchedule()
    
    
    public ResourceMaintenanceDenySchedule()

### ResourceMaintenanceDenySchedule(ResourceMaintenanceDenySchedule)
    
    
    public ResourceMaintenanceDenySchedule(ResourceMaintenanceDenySchedule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceMaintenanceDenySchedule)`  
  
  
## Properties 

### EndDate
    
    
    public Date EndDate { get; set; }

Optional. Deny period end date.

**Property Value**  
---  
**Type** | **Description**  
`[Date](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date.html)` |   
  
### StartDate
    
    
    public Date StartDate { get; set; }

Optional. The start date of the deny maintenance period.

**Property Value**  
---  
**Type** | **Description**  
`[Date](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Date.html)` |   
  
### Time
    
    
    public TimeOfDay Time { get; set; }

Optional. Time in UTC when the deny period starts on start_date and ends on end_date.

**Property Value**  
---  
**Type** | **Description**  
`[TimeOfDay](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.TimeOfDay.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
