---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile
title: Google Cloud Data Loss Prevention v2 API - Class ColumnDataProfile (4.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:46:42.418473+00:00
---

# Google Cloud Data Loss Prevention v2 API - Class ColumnDataProfile (4.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Data Loss Prevention v2 API - Class ColumnDataProfile (4.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.27.0 (latest)  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.5.0  3.4.0  3.3.0  3.2.0  2.16.0  2.15.0 
    
    
    public sealed class ColumnDataProfile : IMessage<ColumnDataProfile>, IEquatable<ColumnDataProfile>, IDeepCloneable<ColumnDataProfile>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Data Loss Prevention v2 API class ColumnDataProfile.

The profile for a scanned column within a table.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ColumnDataProfile

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ColumnDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ColumnDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ColumnDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2)

## Assembly

Google.Cloud.Dlp.V2.dll

## Constructors 

### ColumnDataProfile()
    
    
    public ColumnDataProfile()

### ColumnDataProfile(ColumnDataProfile)
    
    
    public ColumnDataProfile(ColumnDataProfile other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ColumnDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile)`  
  
  
## Properties 

### Column
    
    
    public string Column { get; set; }

The name of the column.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ColumnDataProfileName
    
    
    public ColumnDataProfileName ColumnDataProfileName { get; set; }

[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile#Google_Cloud_Dlp_V2_ColumnDataProfile_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ColumnDataProfileName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfileName)` |   
  
### ColumnInfoType
    
    
    public InfoTypeSummary ColumnInfoType { get; set; }

If it's been determined this column can be identified as a single type, this will be set. Otherwise the column either has unidentifiable content or mixed types.

**Property Value**  
---  
**Type** | **Description**  
`[InfoTypeSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeSummary)` |   
  
### ColumnType
    
    
    public ColumnDataProfile.Types.ColumnDataType ColumnType { get; set; }

The data type of a given column.

**Property Value**  
---  
**Type** | **Description**  
`[ColumnDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types)[ColumnDataType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types.ColumnDataType)` |   
  
### DataRiskLevel
    
    
    public DataRiskLevel DataRiskLevel { get; set; }

The data risk level for this column.

**Property Value**  
---  
**Type** | **Description**  
`[DataRiskLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DataRiskLevel)` |   
  
### DatasetId
    
    
    public string DatasetId { get; set; }

The BigQuery dataset ID, if the resource profiled is a BigQuery table.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DatasetLocation
    
    
    public string DatasetLocation { get; set; }

If supported, the location where the dataset's data is stored. See <https://docs.cloud.google.com/bigquery/docs/locations> for supported BigQuery locations.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DatasetProjectId
    
    
    public string DatasetProjectId { get; set; }

The Google Cloud project ID that owns the profiled resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EstimatedNullPercentage
    
    
    public NullPercentageLevel EstimatedNullPercentage { get; set; }

Approximate percentage of entries being null in the column.

**Property Value**  
---  
**Type** | **Description**  
`[NullPercentageLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.NullPercentageLevel)` |   
  
### EstimatedUniquenessScore
    
    
    public UniquenessScoreLevel EstimatedUniquenessScore { get; set; }

Approximate uniqueness of the column.

**Property Value**  
---  
**Type** | **Description**  
`[UniquenessScoreLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UniquenessScoreLevel)` |   
  
### FreeTextScore
    
    
    public double FreeTextScore { get; set; }

The likelihood that this column contains free-form text. A value close to 1 may indicate the column is likely to contain free-form or natural language text. Range in 0-1.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### Name
    
    
    public string Name { get; set; }

The name of the profile.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### OtherMatches
    
    
    public RepeatedField<OtherInfoTypeSummary> OtherMatches { get; }

Other types found within this column. List will be unordered.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[OtherInfoTypeSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.OtherInfoTypeSummary)` |   
  
### PolicyState
    
    
    public ColumnDataProfile.Types.ColumnPolicyState PolicyState { get; set; }

Indicates if a policy tag has been applied to the column.

**Property Value**  
---  
**Type** | **Description**  
`[ColumnDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types)[ColumnPolicyState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types.ColumnPolicyState)` |   
  
### ProfileLastGenerated
    
    
    public Timestamp ProfileLastGenerated { get; set; }

The last time the profile was generated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ProfileStatus
    
    
    public ProfileStatus ProfileStatus { get; set; }

Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated.

**Property Value**  
---  
**Type** | **Description**  
`[ProfileStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ProfileStatus)` |   
  
### SensitivityScore
    
    
    public SensitivityScore SensitivityScore { get; set; }

The sensitivity of this column.

**Property Value**  
---  
**Type** | **Description**  
`[SensitivityScore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.SensitivityScore)` |   
  
### State
    
    
    public ColumnDataProfile.Types.State State { get; set; }

State of a profile.

**Property Value**  
---  
**Type** | **Description**  
`[ColumnDataProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ColumnDataProfile.Types.State)` |   
  
### TableDataProfile
    
    
    public string TableDataProfile { get; set; }

The resource name of the table data profile.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TableFullResource
    
    
    public string TableFullResource { get; set; }

The resource name of the resource this column is within.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TableId
    
    
    public string TableId { get; set; }

The table ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
