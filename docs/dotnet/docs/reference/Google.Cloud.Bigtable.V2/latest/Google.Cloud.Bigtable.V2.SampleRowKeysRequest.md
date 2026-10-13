---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest
title: Google Bigtable v2 API - Class SampleRowKeysRequest (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:37.994103+00:00
---

# Google Bigtable v2 API - Class SampleRowKeysRequest (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class SampleRowKeysRequest (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class SampleRowKeysRequest : IMessage<SampleRowKeysRequest>, IEquatable<SampleRowKeysRequest>, IDeepCloneable<SampleRowKeysRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class SampleRowKeysRequest.

Request message for Bigtable.SampleRowKeys.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SampleRowKeysRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### SampleRowKeysRequest()
    
    
    public SampleRowKeysRequest()

### SampleRowKeysRequest(SampleRowKeysRequest)
    
    
    public SampleRowKeysRequest(SampleRowKeysRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest)`  
  
  
## Properties 

### AppProfileId
    
    
    public string AppProfileId { get; set; }

This value specifies routing for replication. If not specified, the "default" application profile will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AuthorizedViewName
    
    
    public string AuthorizedViewName { get; set; }

Optional. The unique name of the AuthorizedView from which to sample row keys.

Values are of the form `projects/<project>/instances/<instance>/tables/<table>/authorizedViews/<authorized_view>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AuthorizedViewNameAsAuthorizedViewName
    
    
    public AuthorizedViewName AuthorizedViewNameAsAuthorizedViewName { get; set; }

[AuthorizedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewName)-typed view over the [AuthorizedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest#Google_Cloud_Bigtable_V2_SampleRowKeysRequest_AuthorizedViewName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AuthorizedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewName)` |   
  
### MaterializedViewName
    
    
    public string MaterializedViewName { get; set; }

Optional. The unique name of the MaterializedView from which to read.

Values are of the form `projects/<project>/instances/<instance>/materializedViews/<materialized_view>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaterializedViewNameAsMaterializedViewName
    
    
    public MaterializedViewName MaterializedViewNameAsMaterializedViewName { get; set; }

[MaterializedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MaterializedViewName)-typed view over the [MaterializedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest#Google_Cloud_Bigtable_V2_SampleRowKeysRequest_MaterializedViewName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[MaterializedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MaterializedViewName)` |   
  
### RowRange
    
    
    public RowRange RowRange { get; set; }

Optional. The row range to sample. If not specified, samples from all rows. The output will always return the end key in the range as the last sample returned.

**Property Value**  
---  
**Type** | **Description**  
`[RowRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowRange)` |   
  
### TableName
    
    
    public string TableName { get; set; }

Optional. The unique name of the table from which to sample row keys.

Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TableNameAsTableName
    
    
    public TableName TableNameAsTableName { get; set; }

[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)-typed view over the [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest#Google_Cloud_Bigtable_V2_SampleRowKeysRequest_TableName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
