---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag
title: AlloyDB v1 API - Class SupportedDatabaseFlag (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:24.934187+00:00
---

# AlloyDB v1 API - Class SupportedDatabaseFlag (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1 API - Class SupportedDatabaseFlag (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class SupportedDatabaseFlag : IMessage<SupportedDatabaseFlag>, IEquatable<SupportedDatabaseFlag>, IDeepCloneable<SupportedDatabaseFlag>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1 API class SupportedDatabaseFlag.

SupportedDatabaseFlag gives general information about a database flag, like type and allowed values. This is a static value that is defined on the server side, and it cannot be modified by callers. To set the Database flags on a particular Instance, a caller should modify the Instance.database_flags field.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SupportedDatabaseFlag

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1)

## Assembly

Google.Cloud.AlloyDb.V1.dll

## Constructors 

### SupportedDatabaseFlag()
    
    
    public SupportedDatabaseFlag()

### SupportedDatabaseFlag(SupportedDatabaseFlag)
    
    
    public SupportedDatabaseFlag(SupportedDatabaseFlag other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag)`  
  
  
## Properties 

### AcceptsMultipleValues
    
    
    public bool AcceptsMultipleValues { get; set; }

Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### FlagName
    
    
    public string FlagName { get; set; }

The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasRecommendedStringValue
    
    
    public bool HasRecommendedStringValue { get; }

Gets whether the "recommended_string_value" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IntegerRestrictions
    
    
    public SupportedDatabaseFlag.Types.IntegerRestrictions IntegerRestrictions { get; set; }

Restriction on INTEGER type value.

**Property Value**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.Types)[IntegerRestrictions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.Types.IntegerRestrictions)` |   
  
### Name
    
    
    public string Name { get; set; }

The name of the flag resource, following Google Cloud conventions, e.g.:

  * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RecommendedIntegerValue
    
    
    public long? RecommendedIntegerValue { get; set; }

The recommended value for an INTEGER flag.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### RecommendedStringValue
    
    
    public string RecommendedStringValue { get; set; }

The recommended value for a STRING flag.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RecommendedValueCase
    
    
    public SupportedDatabaseFlag.RecommendedValueOneofCase RecommendedValueCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag)[RecommendedValueOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.RecommendedValueOneofCase)` |   
  
### RequiresDbRestart
    
    
    public bool RequiresDbRestart { get; set; }

Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO's).

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RestrictionsCase
    
    
    public SupportedDatabaseFlag.RestrictionsOneofCase RestrictionsCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag)[RestrictionsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.RestrictionsOneofCase)` |   
  
### Scope
    
    
    public SupportedDatabaseFlag.Types.Scope Scope { get; set; }

The scope of the flag.

**Property Value**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.Types)[Scope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.Types.Scope)` |   
  
### StringRestrictions
    
    
    public SupportedDatabaseFlag.Types.StringRestrictions StringRestrictions { get; set; }

Restriction on STRING type value.

**Property Value**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.Types)[StringRestrictions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.Types.StringRestrictions)` |   
  
### SupportedDatabaseFlagName
    
    
    public SupportedDatabaseFlagName SupportedDatabaseFlagName { get; set; }

[SupportedDatabaseFlagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlagName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag#Google_Cloud_AlloyDb_V1_SupportedDatabaseFlag_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlagName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlagName)` |   
  
### SupportedDbVersions
    
    
    public RepeatedField<DatabaseVersion> SupportedDbVersions { get; }

Major database engine versions for which this flag is supported.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.DatabaseVersion)` |   
  
### ValueType
    
    
    public SupportedDatabaseFlag.Types.ValueType ValueType { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.Types)[ValueType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1/latest/Google.Cloud.AlloyDb.V1.SupportedDatabaseFlag.Types.ValueType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
