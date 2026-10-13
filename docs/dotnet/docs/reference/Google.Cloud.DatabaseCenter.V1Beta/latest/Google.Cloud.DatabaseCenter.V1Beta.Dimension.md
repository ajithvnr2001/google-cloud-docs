---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Dimension
title: Database Center v1beta API - Class Dimension (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:55.637749+00:00
---

# Database Center v1beta API - Class Dimension (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Dimension

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class Dimension (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class Dimension : IMessage<Dimension>, IEquatable<Dimension>, IDeepCloneable<Dimension>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class Dimension.

Dimension used to aggregate the fleet.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Dimension

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Dimension](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Dimension), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Dimension](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Dimension), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Dimension](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Dimension), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### Dimension()
    
    
    public Dimension()

### Dimension(Dimension)
    
    
    public Dimension(Dimension other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Dimension](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Dimension)`  
  
  
## Properties 

### Container
    
    
    public string Container { get; set; }

Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DimensionCase
    
    
    public Dimension.DimensionOneofCase DimensionCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Dimension](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Dimension)[DimensionOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Dimension.DimensionOneofCase)` |   
  
### Edition
    
    
    public Edition Edition { get; set; }

The edition of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[Edition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Edition)` |   
  
### HasContainer
    
    
    public bool HasContainer { get; }

Gets whether the "container" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDenyMaintenanceSchedules
    
    
    public bool HasDenyMaintenanceSchedules { get; set; }

Whether the resource has deny maintenance schedules.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEdition
    
    
    public bool HasEdition { get; }

Gets whether the "edition" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasHasDenyMaintenanceSchedules
    
    
    public bool HasHasDenyMaintenanceSchedules { get; }

Gets whether the "has_deny_maintenance_schedules" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasHasMaintenanceSchedule
    
    
    public bool HasHasMaintenanceSchedule { get; }

Gets whether the "has_maintenance_schedule" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLabelKey
    
    
    public bool HasLabelKey { get; }

Gets whether the "label_key" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLabelSource
    
    
    public bool HasLabelSource { get; }

Gets whether the "label_source" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLabelValue
    
    
    public bool HasLabelValue { get; }

Gets whether the "label_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLocation
    
    
    public bool HasLocation { get; }

Gets whether the "location" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaintenanceSchedule
    
    
    public bool HasMaintenanceSchedule { get; set; }

Whether the resource has a maintenance schedule.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasManagementType
    
    
    public bool HasManagementType { get; }

Gets whether the "management_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasProductEngine
    
    
    public bool HasProductEngine { get; }

Gets whether the "product_engine" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasProductType
    
    
    public bool HasProductType { get; }

Gets whether the "product_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasProductVersion
    
    
    public bool HasProductVersion { get; }

Gets whether the "product_version" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasResourceCategory
    
    
    public bool HasResourceCategory { get; }

Gets whether the "resource_category" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasResourceType
    
    
    public bool HasResourceType { get; }

Gets whether the "resource_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSubResourceType
    
    
    public bool HasSubResourceType { get; }

Gets whether the "sub_resource_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTagInherited
    
    
    public bool HasTagInherited { get; }

Gets whether the "tag_inherited" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTagKey
    
    
    public bool HasTagKey { get; }

Gets whether the "tag_key" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTagSource
    
    
    public bool HasTagSource { get; }

Gets whether the "tag_source" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTagValue
    
    
    public bool HasTagValue { get; }

Gets whether the "tag_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LabelKey
    
    
    public string LabelKey { get; set; }

Label key of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LabelSource
    
    
    public string LabelSource { get; set; }

Label source of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LabelValue
    
    
    public string LabelValue { get; set; }

Label value of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Location
    
    
    public string Location { get; set; }

The location of the resources. It supports returning only regional locations in Google Cloud.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ManagementType
    
    
    public ManagementType ManagementType { get; set; }

The management type of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[ManagementType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ManagementType)` |   
  
### ProductEngine
    
    
    public Engine ProductEngine { get; set; }

Engine refers to underlying database binary running in an instance.

**Property Value**  
---  
**Type** | **Description**  
`[Engine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Engine)` |   
  
### ProductType
    
    
    public ProductType ProductType { get; set; }

Type to identify a product

**Property Value**  
---  
**Type** | **Description**  
`[ProductType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ProductType)` |   
  
### ProductVersion
    
    
    public string ProductVersion { get; set; }

Version of the underlying database engine

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceCategory
    
    
    public ResourceCategory ResourceCategory { get; set; }

The category of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceCategory)` |   
  
### ResourceType
    
    
    public string ResourceType { get; set; }

The type of resource defined according to the pattern: {Service Name}/{Type}. Ex: sqladmin.googleapis.com/Instance alloydb.googleapis.com/Cluster alloydb.googleapis.com/Instance spanner.googleapis.com/Instance

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubResourceType
    
    
    public SubResourceType SubResourceType { get; set; }

Subtype of the resource specified at creation time.

**Property Value**  
---  
**Type** | **Description**  
`[SubResourceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SubResourceType)` |   
  
### TagInherited
    
    
    public bool TagInherited { get; set; }

Tag inheritance value of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### TagKey
    
    
    public string TagKey { get; set; }

Tag key of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TagSource
    
    
    public string TagSource { get; set; }

Tag source of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TagValue
    
    
    public string TagValue { get; set; }

Tag value of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
