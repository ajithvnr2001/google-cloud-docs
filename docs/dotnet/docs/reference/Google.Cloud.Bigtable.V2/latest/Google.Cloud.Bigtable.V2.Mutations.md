---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations
title: Google Bigtable v2 API - Class Mutations (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:54.061006+00:00
---

# Google Bigtable v2 API - Class Mutations (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class Mutations (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public static class Mutations

Reference documentation and code samples for the Google Bigtable v2 API class Mutations.

Static class with convenience methods for creating various kinds of [Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Mutations

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Methods 

### CreateEntry(BigtableByteString, params Mutation[])
    
    
    public static MutateRowsRequest.Types.Entry CreateEntry(BigtableByteString rowKey, params Mutation[] mutations)

Creates a [MutateRowsRequest.Types.Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry) to use with MutateRows requests. Each Entry is an atomic, ordered set of mutations for a particular row.

**Parameters**  
---  
**Name** | **Description**  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the `mutations` should be applied. Must not be empty.  
`mutations` | `[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row. Mutations are applied in order, meaning that earlier mutations can be masked by later ones. You must specify at least one mutation. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)` | The MutateRows entry describing mutations for a single row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

**See Also**

[MutateRows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRows_Google_Cloud_Bigtable_V2_MutateRowsRequest_Google_Api_Gax_Grpc_CallSettings_)[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)

[MutateRows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRows_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_V2_MutateRowsRequest_Types_Entry___)[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)

[MutateRows](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRows_Google_Cloud_Bigtable_Common_V2_TableName_System_Collections_Generic_IEnumerable_Google_Cloud_Bigtable_V2_MutateRowsRequest_Types_Entry__Google_Api_Gax_Grpc_CallSettings_)[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)

[MutateRowsAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRowsAsync_Google_Cloud_Bigtable_V2_MutateRowsRequest_Google_Api_Gax_Grpc_CallSettings_)[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)

[MutateRowsAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRowsAsync_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_V2_MutateRowsRequest_Types_Entry___)[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)

[MutateRowsAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRowsAsync_Google_Cloud_Bigtable_Common_V2_TableName_System_Collections_Generic_IEnumerable_Google_Cloud_Bigtable_V2_MutateRowsRequest_Types_Entry__Google_Api_Gax_Grpc_CallSettings_)[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)

### DeleteFromColumn(string, BigtableByteString, BigtableVersionRange)
    
    
    public static Mutation DeleteFromColumn(string familyName, BigtableByteString columnQualifier, BigtableVersionRange versionRange = null)

Creates a [Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation) which deletes cells from the specified column, optionally restricting the deletions to a given version range.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the family from which cells should be deleted. Must match `[-_.a-zA-Z0-9]+`  
`columnQualifier` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The qualifier of the column from which cells should be deleted. Can be any byte string, including the empty string.  
`versionRange` | `[BigtableVersionRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersionRange)`  
[Optional] The range of versions within which cells should be deleted. If unspecified, all versions will be deleted.  
**Returns**  
---  
**Type** | **Description**  
`[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)` | The created Mutation instance.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `columnQualifier` can be specified using a string as well and its UTF-8 representations will be used. 

### DeleteFromFamily(string)
    
    
    public static Mutation DeleteFromFamily(string familyName)

Creates a [Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation) which deletes all cells from the specified column family.

**Parameter**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the family from which cells should be deleted. Must match `[-_.a-zA-Z0-9]+`  
**Returns**  
---  
**Type** | **Description**  
`[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)` | The created Mutation instance.  
  
### DeleteFromRow()
    
    
    public static Mutation DeleteFromRow()

Creates a [Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation) which deletes all cells from the containing row.

**Returns**  
---  
**Type** | **Description**  
`[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)` | The created Mutation instance.  
  
### SetCell(string, BigtableByteString, BigtableByteString, BigtableVersion?)
    
    
    public static Mutation SetCell(string familyName, BigtableByteString columnQualifier, BigtableByteString value, BigtableVersion? version = null)

Creates a [Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation) which sets the value of the specified cell.

**Parameters**  
---  
**Name** | **Description**  
`familyName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the family into which new data should be written. Must match `[-_.a-zA-Z0-9]+`  
`columnQualifier` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The qualifier of the column into which new data should be written. Can be any byte string, including the empty string.  
`value` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The value to be written into the specified cell.  
`version` | `[BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion)`  
[Optional] The version of the cell into which new data should be written. If unspecified, the version will be initialized from the current UTC time.  
**Returns**  
---  
**Type** | **Description**  
`[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)` | The created Mutation instance.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `columnQualifier` or `value` can be specified using a string as well and its UTF-8 representations will be used. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
