---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest
title: Google Bigtable v2 API - Class ReadRowsRequest (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:02.920973+00:00
---

# Google Bigtable v2 API - Class ReadRowsRequest (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class ReadRowsRequest (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ReadRowsRequest : IMessage<ReadRowsRequest>, IEquatable<ReadRowsRequest>, IDeepCloneable<ReadRowsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class ReadRowsRequest.

Request message for Bigtable.ReadRows.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReadRowsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### ReadRowsRequest()
    
    
    public ReadRowsRequest()

### ReadRowsRequest(ReadRowsRequest)
    
    
    public ReadRowsRequest(ReadRowsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest)`  
  
  
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

Optional. The unique name of the AuthorizedView from which to read.

Values are of the form `projects/<project>/instances/<instance>/tables/<table>/authorizedViews/<authorized_view>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AuthorizedViewNameAsAuthorizedViewName
    
    
    public AuthorizedViewName AuthorizedViewNameAsAuthorizedViewName { get; set; }

[AuthorizedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewName)-typed view over the [AuthorizedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest#Google_Cloud_Bigtable_V2_ReadRowsRequest_AuthorizedViewName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AuthorizedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewName)` |   
  
### Filter
    
    
    public RowFilter Filter { get; set; }

The filter to apply to the contents of the specified row(s). If unset, reads the entirety of each row.

**Property Value**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` |   
  
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

[MaterializedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MaterializedViewName)-typed view over the [MaterializedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest#Google_Cloud_Bigtable_V2_ReadRowsRequest_MaterializedViewName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[MaterializedViewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MaterializedViewName)` |   
  
### RequestStatsView
    
    
    public ReadRowsRequest.Types.RequestStatsView RequestStatsView { get; set; }

The view into RequestStats, as described above.

**Property Value**  
---  
**Type** | **Description**  
`[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest.Types)[RequestStatsView](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest.Types.RequestStatsView)` |   
  
### Reversed
    
    
    public bool Reversed { get; set; }

Experimental API - Please note that this API is currently experimental and can change in the future.

Return rows in lexiographical descending order of the row keys. The row contents will not be affected by this flag.

Example result set:
    
    
    [
      {key: "k2", "f:col1": "v1", "f:col2": "v1"},
      {key: "k1", "f:col1": "v2", "f:col2": "v2"}
    ]
    

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Rows
    
    
    public RowSet Rows { get; set; }

The row keys and/or ranges to read sequentially. If not specified, reads from all rows.

**Property Value**  
---  
**Type** | **Description**  
`[RowSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowSet)` |   
  
### RowsLimit
    
    
    public long RowsLimit { get; set; }

The read will stop after committing to N rows' worth of results. The default (zero) is to return all results.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### TableName
    
    
    public string TableName { get; set; }

Optional. The unique name of the table from which to read.

Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TableNameAsTableName
    
    
    public TableName TableNameAsTableName { get; set; }

[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)-typed view over the [TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest#Google_Cloud_Bigtable_V2_ReadRowsRequest_TableName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
