---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResource
title: Database Center v1beta API - Class DatabaseResource (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:54.475512+00:00
---

# Database Center v1beta API - Class DatabaseResource (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Center v1beta API - Class DatabaseResource (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta08 (latest)  1.0.0-beta07 
    
    
    public sealed class DatabaseResource : IMessage<DatabaseResource>, IEquatable<DatabaseResource>, IDeepCloneable<DatabaseResource>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Center v1beta API class DatabaseResource.

DatabaseResource represents every individually configured database unit representing compute and/or storage.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DatabaseResource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DatabaseResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DatabaseResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DatabaseResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DatabaseCenter.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta)

## Assembly

Google.Cloud.DatabaseCenter.V1Beta.dll

## Constructors 

### DatabaseResource()
    
    
    public DatabaseResource()

### DatabaseResource(DatabaseResource)
    
    
    public DatabaseResource(DatabaseResource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DatabaseResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResource)`  
  
  
## Properties 

### Affiliations
    
    
    public RepeatedField<Affiliation> Affiliations { get; }

Optional. Affiliation details of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Affiliation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Affiliation)` |   
  
### BackupdrConfig
    
    
    public BackupDRConfig BackupdrConfig { get; set; }

Optional. Backup and disaster recovery details for the resource.

**Property Value**  
---  
**Type** | **Description**  
`[BackupDRConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.BackupDRConfig)` |   
  
### ChildResources
    
    
    public RepeatedField<DatabaseResource> ChildResources { get; }

List of children associated with a database group.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DatabaseResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.DatabaseResource)` |   
  
### Container
    
    
    public string Container { get; set; }

Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Edition
    
    
    public Edition Edition { get; set; }

The edition of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[Edition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Edition)` |   
  
### FullResourceName
    
    
    public string FullResourceName { get; set; }

The full resource name, based on CAIS resource name format <https://cloud.google.com/asset-inventory/docs/resource-name-format>

Example:

`//cloudsql.googleapis.com/projects/project-number/instances/mysql-1` `//cloudsql.googleapis.com/projects/project-number/instances/postgres-1` `//spanner.googleapis.com/projects/project-number/instances/spanner-instance-1` `//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1` `//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1/instances/i1`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Labels
    
    
    public RepeatedField<Label> Labels { get; }

Labels applied on the resource. The requirements for labels assigned to Google Cloud resources may be found at <https://cloud.google.com/resource-manager/docs/labels-overview#requirements>

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Label](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Label)` |   
  
### Location
    
    
    public string Location { get; set; }

The location of the resources. It supports returning only regional locations in Google Cloud. These are of the form: "us-central1", "us-east1", etc. See <https://cloud.google.com/about/locations> for a list of such regions.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MachineConfig
    
    
    public MachineConfig MachineConfig { get; set; }

Machine configuration like CPU, memory, etc for the resource.

**Property Value**  
---  
**Type** | **Description**  
`[MachineConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MachineConfig)` |   
  
### MaintenanceInfo
    
    
    public MaintenanceInfo MaintenanceInfo { get; set; }

Optional. The maintenance information of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[MaintenanceInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.MaintenanceInfo)` |   
  
### Metrics
    
    
    public Metrics Metrics { get; set; }

Observable metrics for the resource e.g. CPU utilization, memory utilization, etc.

**Property Value**  
---  
**Type** | **Description**  
`[Metrics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Metrics)` |   
  
### Product
    
    
    public Product Product { get; set; }

The product this resource represents.

**Property Value**  
---  
**Type** | **Description**  
`[Product](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Product)` |   
  
### ResourceCategory
    
    
    public ResourceCategory ResourceCategory { get; set; }

The category of the resource.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.ResourceCategory)` |   
  
### ResourceName
    
    
    public string ResourceName { get; set; }

The name of the resource(The last part of the full resource name). Example: For full resource name - `//cloudsql.googleapis.com/projects/project-number/instances/mysql-1`, resource name - `mysql-1` For full resource name - `//cloudsql.googleapis.com/projects/project-number/instances/postgres-1` , resource name - `postgres-1` Note: In some cases, there might be more than one resource with the same resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResourceType
    
    
    public string ResourceType { get; set; }

The type of resource defined according to the pattern: {Service Name}/{Type}. Ex: sqladmin.googleapis.com/Instance alloydb.googleapis.com/Cluster alloydb.googleapis.com/Instance spanner.googleapis.com/Instance

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SignalGroups
    
    
    public RepeatedField<SignalGroup> SignalGroups { get; }

The list of signal groups and count of issues related to the resource. Only those signals which have been requested would be included.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[SignalGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SignalGroup)` |   
  
### SubResourceType
    
    
    public SubResourceType SubResourceType { get; set; }

Subtype of the resource specified at creation time.

**Property Value**  
---  
**Type** | **Description**  
`[SubResourceType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.SubResourceType)` |   
  
### Tags
    
    
    public RepeatedField<Tag> Tags { get; }

Tags applied on the resource. The requirements for tags assigned to Google Cloud resources may be found at <https://cloud.google.com/resource-manager/docs/tags/tags-overview>

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Tag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DatabaseCenter.V1Beta/latest/Google.Cloud.DatabaseCenter.V1Beta.Tag)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
