---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types.Maintenance
title: Maintenance v1 API - Class ResourceMaintenance.Types.Maintenance (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:03.528545+00:00
---

# Maintenance v1 API - Class ResourceMaintenance.Types.Maintenance (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types.Maintenance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Maintenance v1 API - Class ResourceMaintenance.Types.Maintenance (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class ResourceMaintenance.Types.Maintenance : IMessage<ResourceMaintenance.Types.Maintenance>, IEquatable<ResourceMaintenance.Types.Maintenance>, IDeepCloneable<ResourceMaintenance.Types.Maintenance>, IBufferMessage, IMessage

Reference documentation and code samples for the Maintenance v1 API class ResourceMaintenance.Types.Maintenance.

Maintenance is the maintenance details of a resource's maintenance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResourceMaintenance.Types.Maintenance

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types)[Maintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types.Maintenance), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types)[Maintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types.Maintenance), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types)[Maintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types.Maintenance), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Maintenance.Api.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1)

## Assembly

Google.Cloud.Maintenance.Api.V1.dll

## Constructors 

### Maintenance()
    
    
    public Maintenance()

### Maintenance(Maintenance)
    
    
    public Maintenance(ResourceMaintenance.Types.Maintenance other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResourceMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types)[Maintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.ResourceMaintenance.Types.Maintenance)`  
  
  
## Properties 

### Category
    
    
    public MaintenanceCategory Category { get; set; }

Output only. The category of the maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[MaintenanceCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Maintenance.Api.V1/latest/Google.Cloud.Maintenance.Api.V1.MaintenanceCategory)` |   
  
### Description
    
    
    public string Description { get; set; }

Output only. The description of the maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaintenanceName
    
    
    public string MaintenanceName { get; set; }

Maintenance is the name of the corresponding maintenance resource following the standard naming scheme: `"{maintenance-id}"`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Title
    
    
    public string Title { get; set; }

Output only. The title of the maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
