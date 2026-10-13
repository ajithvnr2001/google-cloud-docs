---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation
title: Google Cloud Datastore v1 API - Class Mutation (5.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:52.955199+00:00
---

# Google Cloud Datastore v1 API - Class Mutation (5.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Datastore v1 API - Class Mutation (5.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.2.0 (latest)  5.1.0  5.0.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0 
    
    
    public sealed class Mutation : IMessage<Mutation>, IEquatable<Mutation>, IDeepCloneable<Mutation>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Datastore v1 API class Mutation.

A mutation to apply to an entity.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Mutation

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1)

## Assembly

Google.Cloud.Datastore.V1.dll

## Constructors 

### Mutation()
    
    
    public Mutation()

### Mutation(Mutation)
    
    
    public Mutation(Mutation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation)`  
  
  
## Properties 

### BaseVersion
    
    
    public long BaseVersion { get; set; }

The version of the entity that this mutation is being applied to. If this does not match the current version on the server, the mutation conflicts.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ConflictDetectionStrategyCase
    
    
    public Mutation.ConflictDetectionStrategyOneofCase ConflictDetectionStrategyCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation)[ConflictDetectionStrategyOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation.ConflictDetectionStrategyOneofCase)` |   
  
### ConflictResolutionStrategy
    
    
    public Mutation.Types.ConflictResolutionStrategy ConflictResolutionStrategy { get; set; }

The strategy to use when a conflict is detected. Defaults to `SERVER_VALUE`. If this is set, then `conflict_detection_strategy` must also be set.

**Property Value**  
---  
**Type** | **Description**  
`[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation.Types)[ConflictResolutionStrategy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation.Types.ConflictResolutionStrategy)` |   
  
### Delete
    
    
    public Key Delete { get; set; }

The key of the entity to delete. The entity may or may not already exist. Must have a complete key path and must not be reserved/read-only.

**Property Value**  
---  
**Type** | **Description**  
`[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Key)` |   
  
### HasBaseVersion
    
    
    public bool HasBaseVersion { get; }

Gets whether the "base_version" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Insert
    
    
    public Entity Insert { get; set; }

The entity to insert. The entity must not already exist. The entity key's final path element may be incomplete.

**Property Value**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Entity)` |   
  
### OperationCase
    
    
    public Mutation.OperationOneofCase OperationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation)[OperationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Mutation.OperationOneofCase)` |   
  
### PropertyMask
    
    
    public PropertyMask PropertyMask { get; set; }

The properties to write in this mutation. None of the properties in the mask may have a reserved name, except for `__key__`. This field is ignored for `delete`.

If the entity already exists, only properties referenced in the mask are updated, others are left untouched. Properties referenced in the mask but not in the entity are deleted.

**Property Value**  
---  
**Type** | **Description**  
`[PropertyMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PropertyMask)` |   
  
### PropertyTransforms
    
    
    public RepeatedField<PropertyTransform> PropertyTransforms { get; }

Optional. The transforms to perform on the entity.

This field can be set only when the operation is `insert`, `update`, or `upsert`. If present, the transforms are be applied to the entity regardless of the property mask, in order, after the operation.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[PropertyTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.PropertyTransform)` |   
  
### Update
    
    
    public Entity Update { get; set; }

The entity to update. The entity must already exist. Must have a complete key path.

**Property Value**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Entity)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

The update time of the entity that this mutation is being applied to. If this does not match the current update time on the server, the mutation conflicts.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Upsert
    
    
    public Entity Upsert { get; set; }

The entity to upsert. The entity may or may not already exist. The entity key's final path element may be incomplete.

**Property Value**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastore.V1/latest/Google.Cloud.Datastore.V1.Entity)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
