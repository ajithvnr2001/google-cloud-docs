---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest
title: DataStream v1alpha1 API - Class DiscoverConnectionProfileRequest (2.0.0-alpha06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:13.267256+00:00
---

# DataStream v1alpha1 API - Class DiscoverConnectionProfileRequest (2.0.0-alpha06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  DataStream v1alpha1 API - Class DiscoverConnectionProfileRequest (2.0.0-alpha06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-alpha06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest)
  * [ 2.0.0-alpha05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/2.0.0-alpha05/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/1.0.0-beta02/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest)


    
    
    public sealed class DiscoverConnectionProfileRequest : IMessage<DiscoverConnectionProfileRequest>, IEquatable<DiscoverConnectionProfileRequest>, IDeepCloneable<DiscoverConnectionProfileRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the DataStream v1alpha1 API class DiscoverConnectionProfileRequest.

Request message for 'discover' ConnectionProfile request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DiscoverConnectionProfileRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Datastream.V1Alpha1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1)

## Assembly

Google.Cloud.Datastream.V1Alpha1.dll

## Constructors 

### DiscoverConnectionProfileRequest()
    
    
    public DiscoverConnectionProfileRequest()

### DiscoverConnectionProfileRequest(DiscoverConnectionProfileRequest)
    
    
    public DiscoverConnectionProfileRequest(DiscoverConnectionProfileRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest)`  
  
  
## Properties 

### ConnectionProfile
    
    
    public ConnectionProfile ConnectionProfile { get; set; }

An ad-hoc ConnectionProfile configuration.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.ConnectionProfile)` |   
  
### ConnectionProfileName
    
    
    public string ConnectionProfileName { get; set; }

A reference to an existing ConnectionProfile.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DataObjectCase
    
    
    public DiscoverConnectionProfileRequest.DataObjectOneofCase DataObjectCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest)[DataObjectOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest.DataObjectOneofCase)` |   
  
### DepthCase
    
    
    public DiscoverConnectionProfileRequest.DepthOneofCase DepthCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest)[DepthOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest.DepthOneofCase)` |   
  
### HasConnectionProfileName
    
    
    public bool HasConnectionProfileName { get; }

Gets whether the "connection_profile_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRecursionDepth
    
    
    public bool HasRecursionDepth { get; }

Gets whether the "recursion_depth" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRecursive
    
    
    public bool HasRecursive { get; }

Gets whether the "recursive" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MysqlRdbms
    
    
    public MysqlRdbms MysqlRdbms { get; set; }

MySQL RDBMS to enrich with child data objects and metadata.

**Property Value**  
---  
**Type** | **Description**  
`[MysqlRdbms](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.MysqlRdbms)` |   
  
### OracleRdbms
    
    
    public OracleRdbms OracleRdbms { get; set; }

Oracle RDBMS to enrich with child data objects and metadata.

**Property Value**  
---  
**Type** | **Description**  
`[OracleRdbms](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.OracleRdbms)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource of the ConnectionProfile type. Must be in the format `projects/*/locations/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest#Google_Cloud_Datastream_V1Alpha1_DiscoverConnectionProfileRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### RecursionDepth
    
    
    public int RecursionDepth { get; set; }

The number of hierarchy levels below the current level to be retrieved.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Recursive
    
    
    public bool Recursive { get; set; }

Whether to retrieve the full hierarchy of data objects (TRUE) or only the current level (FALSE).

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### TargetCase
    
    
    public DiscoverConnectionProfileRequest.TargetOneofCase TargetCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest)[TargetOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Datastream.V1Alpha1/latest/Google.Cloud.Datastream.V1Alpha1.DiscoverConnectionProfileRequest.TargetOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
