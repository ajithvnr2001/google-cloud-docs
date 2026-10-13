---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient
title: Google Bigtable v2 API - Class BigtableClient (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:39.413389+00:00
---

# Google Bigtable v2 API - Class BigtableClient (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class BigtableClient (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public abstract class BigtableClient

Reference documentation and code samples for the Google Bigtable v2 API class BigtableClient.

BigtableServiceApi client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigtableClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[BigtableClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClientImpl)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Remarks

Service for reading from and writing to existing Bigtable tables.

## Properties 

### AppProfileId
    
    
    public virtual string AppProfileId { get; }

Gets the value which specifies routing for replication. If null or empty, the "default" application profile will be used by the server.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### CheckAndMutateRow(TableName, BigtableByteString, RowFilter, params Mutation[])
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(TableName tableName, BigtableByteString rowKey, RowFilter predicateFilter, params Mutation[] trueMutations)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the conditional mutation should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the conditional mutation should be applied. Must not be empty.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, `trueMutations` may or may not be executed. If null, checks that the row contains any values at all.  
`trueMutations` | `[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicateFilter` yields at least one cell when applied to `rowKey`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The response from trying to mutate the row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [CheckAndMutateRow(CheckAndMutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_CheckAndMutateRow_Google_Cloud_Bigtable_V2_CheckAndMutateRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### CheckAndMutateRow(TableName, BigtableByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(TableName tableName, BigtableByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the conditional mutation should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the conditional mutation should be applied. Must not be empty.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `trueMutations` or `falseMutations` will be executed. If null, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicateFilter` yields at least one cell when applied to `rowKey`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `falseMutations` is null or empty, and at most 100000. Can be null or empty, but must not contain null elements.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicateFilter` does not yield any cells when applied to `rowKey`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `trueMutations` is null or empty, and at most 100000. Can be null or empty, but must not contain null elements.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The response from trying to mutate the row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [CheckAndMutateRow(CheckAndMutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_CheckAndMutateRow_Google_Cloud_Bigtable_V2_CheckAndMutateRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### CheckAndMutateRow(CheckAndMutateRowRequest, CallSettings)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(CheckAndMutateRowRequest request, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest#Google_Cloud_Bigtable_V2_CheckAndMutateRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The RPC response.  
  
### CheckAndMutateRowAsync(TableName, BigtableByteString, RowFilter, params Mutation[])
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(TableName tableName, BigtableByteString rowKey, RowFilter predicateFilter, params Mutation[] trueMutations)

Asynchronously mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the conditional mutation should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the conditional mutation should be applied. Must not be empty.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, `trueMutations` may or may not be executed. If null, checks that the row contains any values at all.  
`trueMutations` | `[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicateFilter` yields at least one cell when applied to `rowKey`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The response from trying to mutate the row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [CheckAndMutateRowAsync(CheckAndMutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_CheckAndMutateRowAsync_Google_Cloud_Bigtable_V2_CheckAndMutateRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

**Example**
    
    
    CheckAndMutateRowResponse response = await client.CheckAndMutateRowAsync(
        new TableName(projectId, instanceId, tableId),
        "user12345",
        // If the latest value in the "Address:Country" column is "USA"...
        RowFilters.Chain(
            RowFilters.FamilyNameExact("Address"),
            RowFilters.ColumnQualifierExact("Country"),
            RowFilters.CellsPerColumnLimit(1),
            RowFilters.ValueExact("USA")),
        // ...remove all previous Level 1 scores and set the value to 0.
        Mutations.DeleteFromColumn("Score", "Level 1"),
        Mutations.SetCell("Score", "Level 1", 0, new BigtableVersion(1)));
    
    if (response.PredicateMatched)
    {
        Console.WriteLine("The level 1 scores have been reset");
    }
    else
    {
        Console.WriteLine("The level 1 scores were not modified.");
    }
    

### CheckAndMutateRowAsync(TableName, BigtableByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(TableName tableName, BigtableByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, CallSettings callSettings = null)

Asynchronously mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the conditional mutation should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the conditional mutation should be applied. Must not be empty.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `trueMutations` or `falseMutations` will be executed. If null, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicateFilter` yields at least one cell when applied to `rowKey`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `falseMutations` is null or empty, and at most 100000. Can be null or empty, but must not contain null elements.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicateFilter` does not yield any cells when applied to `rowKey`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `trueMutations` is null or empty, and at most 100000. Can be null or empty, but must not contain null elements.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The response from trying to mutate the row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [CheckAndMutateRowAsync(CheckAndMutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_CheckAndMutateRowAsync_Google_Cloud_Bigtable_V2_CheckAndMutateRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### CheckAndMutateRowAsync(CheckAndMutateRowRequest, CallSettings)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(CheckAndMutateRowRequest request, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest#Google_Cloud_Bigtable_V2_CheckAndMutateRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
  
### CheckAndMutateRowAsync(CheckAndMutateRowRequest, CancellationToken)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(CheckAndMutateRowRequest request, CancellationToken cancellationToken)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest#Google_Cloud_Bigtable_V2_CheckAndMutateRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
  
### Create()
    
    
    public static BigtableClient Create()

Synchronously creates a [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [BigtableClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient)` | The created [BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient).  
  
### Create(BigtableServiceApiClient)
    
    
    public static BigtableClient Create(BigtableServiceApiClient client)

Synchronously creates a [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient) from a pre-existing API client.

**Parameter**  
---  
**Name** | **Description**  
`client` | `[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)`  
The [BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient) to use in the [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient). Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient)` | The created [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient).  
  
### CreateAsync()
    
    
    public static Task<BigtableClient> CreateAsync()

Asynchronously creates a [BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [BigtableClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient)` | The created [BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient).  
  
### ExecuteQuery(InstanceName, string, CallSettings)
    
    
    [Obsolete]
    public virtual BigtableServiceApiClient.ExecuteQueryStream ExecuteQuery(InstanceName instanceName, string query, CallSettings callSettings = null)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string. Exactly one of `query` and `prepared_query` is required. Setting both or neither is an `INVALID_ARGUMENT`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ExecuteQueryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ExecuteQueryStream)` | The server stream.  
  
### ExecuteQuery(InstanceName, string, string, CallSettings)
    
    
    [Obsolete]
    public virtual BigtableServiceApiClient.ExecuteQueryStream ExecuteQuery(InstanceName instanceName, string query, string appProfileId, CallSettings callSettings = null)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string. Exactly one of `query` and `prepared_query` is required. Setting both or neither is an `INVALID_ARGUMENT`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. This value specifies routing for replication. If not specified, the `default` application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ExecuteQueryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ExecuteQueryStream)` | The server stream.  
  
### ExecuteQuery(ExecuteQueryRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ExecuteQueryStream ExecuteQuery(ExecuteQueryRequest request, CallSettings callSettings = null)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest#Google_Cloud_Bigtable_V2_ExecuteQueryRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ExecuteQueryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ExecuteQueryStream)` | The server stream.  
  
### ExecuteQuery(string, string, CallSettings)
    
    
    [Obsolete]
    public virtual BigtableServiceApiClient.ExecuteQueryStream ExecuteQuery(string instanceName, string query, CallSettings callSettings = null)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string. Exactly one of `query` and `prepared_query` is required. Setting both or neither is an `INVALID_ARGUMENT`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ExecuteQueryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ExecuteQueryStream)` | The server stream.  
  
### ExecuteQuery(string, string, string, CallSettings)
    
    
    [Obsolete]
    public virtual BigtableServiceApiClient.ExecuteQueryStream ExecuteQuery(string instanceName, string query, string appProfileId, CallSettings callSettings = null)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string. Exactly one of `query` and `prepared_query` is required. Setting both or neither is an `INVALID_ARGUMENT`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. This value specifies routing for replication. If not specified, the `default` application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ExecuteQueryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ExecuteQueryStream)` | The server stream.  
  
### GenerateInitialChangeStreamPartitions(TableName, CallSettings)
    
    
    public virtual BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream GenerateInitialChangeStreamPartitions(TableName tableName, CallSettings callSettings = null)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Required. The unique name of the table from which to get change stream partitions. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[GenerateInitialChangeStreamPartitionsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream)` | The server stream.  
  
### GenerateInitialChangeStreamPartitions(TableName, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream GenerateInitialChangeStreamPartitions(TableName tableName, string appProfileId, CallSettings callSettings = null)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Required. The unique name of the table from which to get change stream partitions. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used. Single cluster routing must be configured on the profile.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[GenerateInitialChangeStreamPartitionsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream)` | The server stream.  
  
### GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest request, CallSettings callSettings = null)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest#Google_Cloud_Bigtable_V2_GenerateInitialChangeStreamPartitionsRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[GenerateInitialChangeStreamPartitionsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream)` | The server stream.  
  
### GenerateInitialChangeStreamPartitions(string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream GenerateInitialChangeStreamPartitions(string tableName, CallSettings callSettings = null)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the table from which to get change stream partitions. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[GenerateInitialChangeStreamPartitionsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream)` | The server stream.  
  
### GenerateInitialChangeStreamPartitions(string, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream GenerateInitialChangeStreamPartitions(string tableName, string appProfileId, CallSettings callSettings = null)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the table from which to get change stream partitions. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used. Single cluster routing must be configured on the profile.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[GenerateInitialChangeStreamPartitionsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream)` | The server stream.  
  
### GetClientConfiguration(GetClientConfigurationRequest, CallSettings)
    
    
    public virtual ClientConfiguration GetClientConfiguration(GetClientConfigurationRequest request, CallSettings callSettings = null)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest#Google_Cloud_Bigtable_V2_GetClientConfigurationRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | The RPC response.  
  
### GetClientConfigurationAsync(GetClientConfigurationRequest, CallSettings)
    
    
    public virtual Task<ClientConfiguration> GetClientConfigurationAsync(GetClientConfigurationRequest request, CallSettings callSettings = null)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest#Google_Cloud_Bigtable_V2_GetClientConfigurationRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | A Task containing the RPC response.  
  
### GetClientConfigurationAsync(GetClientConfigurationRequest, CancellationToken)
    
    
    public virtual Task<ClientConfiguration> GetClientConfigurationAsync(GetClientConfigurationRequest request, CancellationToken cancellationToken)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest#Google_Cloud_Bigtable_V2_GetClientConfigurationRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | A Task containing the RPC response.  
  
### MutateRow(TableName, BigtableByteString, params Mutation[])
    
    
    public virtual MutateRowResponse MutateRow(TableName tableName, BigtableByteString rowKey, params Mutation[] mutations)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutations`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the mutation should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the mutation should be applied. Must not be empty.  
`mutations` | `[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The response from mutating the row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [MutateRow(MutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRow_Google_Cloud_Bigtable_V2_MutateRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### MutateRow(TableName, BigtableByteString, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual MutateRowResponse MutateRow(TableName tableName, BigtableByteString rowKey, IEnumerable<Mutation> mutations, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutations`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the mutation should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the mutation should be applied. Must not be empty.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000. Must not be null, or contain null elements.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The response from mutating the row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [MutateRow(MutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRow_Google_Cloud_Bigtable_V2_MutateRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### MutateRow(MutateRowRequest, CallSettings)
    
    
    public virtual MutateRowResponse MutateRow(MutateRowRequest request, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest#Google_Cloud_Bigtable_V2_MutateRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The RPC response.  
  
### MutateRowAsync(TableName, BigtableByteString, params Mutation[])
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(TableName tableName, BigtableByteString rowKey, params Mutation[] mutations)

Asynchronously mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutations`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the mutation should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the mutation should be applied. Must not be empty.  
`mutations` | `[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The response from mutating the row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [MutateRowAsync(MutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRowAsync_Google_Cloud_Bigtable_V2_MutateRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

**Example**
    
    
    await client.MutateRowAsync(
        new TableName(projectId, instanceId, tableId),
        // From the row with key '0xABCD1234'...
        new byte[] { 0xAB, 0xCD, 0x12, 0x34 },
        // delete all cells from the column family "Address",
        Mutations.DeleteFromFamily("Address"),
        // and all cells from the "Score:Level 1" column which are older than a day (assuming UTC
        // timestamp micros have been used as version values in this column).
        Mutations.DeleteFromColumn(
            "Score",
            "Level 1",
            new BigtableVersionRange(null, DateTime.UtcNow.AddDays(-1))));
    

### MutateRowAsync(TableName, BigtableByteString, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(TableName tableName, BigtableByteString rowKey, IEnumerable<Mutation> mutations, CallSettings callSettings = null)

Asynchronously mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutations`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the mutation should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the mutation should be applied. Must not be empty.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000. Must not be null, or contain null elements.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The response from mutating the row.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [MutateRowAsync(MutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRowAsync_Google_Cloud_Bigtable_V2_MutateRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### MutateRowAsync(MutateRowRequest, CallSettings)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(MutateRowRequest request, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest#Google_Cloud_Bigtable_V2_MutateRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
  
### MutateRowAsync(MutateRowRequest, CancellationToken)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(MutateRowRequest request, CancellationToken cancellationToken)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest#Google_Cloud_Bigtable_V2_MutateRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
  
### MutateRows(TableName, params Entry[])
    
    
    public virtual MutateRowsResponse MutateRows(TableName tableName, params MutateRowsRequest.Types.Entry[] entries)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in [MutateRow(MutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRow_Google_Cloud_Bigtable_V2_MutateRowRequest_Google_Api_Gax_Grpc_CallSettings_), but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the mutations should be applied. Must not be null.  
`entries` | `[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)`  
The row keys and corresponding mutations to be applied in bulk. Each entry is applied as an atomic mutation, but the entries may be applied in arbitrary order (even between entries for the same row). At least one entry must be specified, and in total the entries can contain at most 100000 mutations.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The response from mutating the rows.  
**Remarks**

This method simply delegates to [MutateRows(TableName, IEnumerable<Entry>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRows_Google_Cloud_Bigtable_Common_V2_TableName_System_Collections_Generic_IEnumerable_Google_Cloud_Bigtable_V2_MutateRowsRequest_Types_Entry__Google_Api_Gax_Grpc_CallSettings_). 

### MutateRows(TableName, IEnumerable<Entry>, CallSettings)
    
    
    public virtual MutateRowsResponse MutateRows(TableName tableName, IEnumerable<MutateRowsRequest.Types.Entry> entries, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in [MutateRow(MutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRow_Google_Cloud_Bigtable_V2_MutateRowRequest_Google_Api_Gax_Grpc_CallSettings_), but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the mutations should be applied. Must not be null.  
`entries` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)`  
The row keys and corresponding mutations to be applied in bulk. Each entry is applied as an atomic mutation, but the entries may be applied in arbitrary order (even between entries for the same row). At least one entry must be specified, and in total the entries can contain at most 100000 mutations. Must not be null, or contain null elements.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The response from mutating the rows.  
**Remarks**

This method simply delegates to [MutateRows(MutateRowsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRows_Google_Cloud_Bigtable_V2_MutateRowsRequest_Google_Api_Gax_Grpc_CallSettings_). 

### MutateRows(MutateRowsRequest, CallSettings)
    
    
    public virtual MutateRowsResponse MutateRows(MutateRowsRequest request, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest#Google_Cloud_Bigtable_V2_MutateRowsRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The RPC response.  
  
### MutateRowsAsync(TableName, params Entry[])
    
    
    public virtual Task<MutateRowsResponse> MutateRowsAsync(TableName tableName, params MutateRowsRequest.Types.Entry[] entries)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in [MutateRow(MutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRow_Google_Cloud_Bigtable_V2_MutateRowRequest_Google_Api_Gax_Grpc_CallSettings_), but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the mutations should be applied. Must not be null.  
`entries` | `[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)`  
The row keys and corresponding mutations to be applied in bulk. Each entry is applied as an atomic mutation, but the entries may be applied in arbitrary order (even between entries for the same row). At least one entry must be specified, and in total the entries can contain at most 100000 mutations.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The response from mutating the rows.  
**Remarks**

This method simply delegates to [MutateRowsAsync(TableName, IEnumerable<Entry>, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRowsAsync_Google_Cloud_Bigtable_Common_V2_TableName_System_Collections_Generic_IEnumerable_Google_Cloud_Bigtable_V2_MutateRowsRequest_Types_Entry__Google_Api_Gax_Grpc_CallSettings_). 

**Example**
    
    
    MutateRowsResponse response = await client.MutateRowsAsync(
        new TableName(projectId, instanceId, tableId),
        // From row 'user12345'...
        Mutations.CreateEntry("user12345",
            // delete all cells from the column family "Score",
            Mutations.DeleteFromFamily("Score"),
            // and all cells from the "metrics:clicks" column which are older than a day (assuming UTC
            // timestamp micros have been used as version values in this column).
            Mutations.DeleteFromColumn(
                "metrics",
                "clicks",
                new BigtableVersionRange(null, DateTime.UtcNow.AddDays(-1)))),
        // Delete all data from row 'user23456'
        Mutations.CreateEntry("user23456", Mutations.DeleteFromRow()));
    
    foreach (MutateRowsResponse.Types.Entry entry in response.Entries)
    {
        switch (entry.Index)
        {
            case 0:
                Console.WriteLine($"The mutations to row 'user12345' finished with status code {entry.Status.Code}");
                break;
            case 1:
                Console.WriteLine($"The mutations to row 'user23456' finished with status code {entry.Status.Code}");
                break;
            default:
                throw new ArgumentOutOfRangeException();
        }
    }
    

### MutateRowsAsync(TableName, IEnumerable<Entry>, CallSettings)
    
    
    public virtual Task<MutateRowsResponse> MutateRowsAsync(TableName tableName, IEnumerable<MutateRowsRequest.Types.Entry> entries, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in [MutateRow(MutateRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRow_Google_Cloud_Bigtable_V2_MutateRowRequest_Google_Api_Gax_Grpc_CallSettings_), but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the mutations should be applied. Must not be null.  
`entries` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)`  
The row keys and corresponding mutations to be applied in bulk. Each entry is applied as an atomic mutation, but the entries may be applied in arbitrary order (even between entries for the same row). At least one entry must be specified, and in total the entries can contain at most 100000 mutations. Must not be null, or contain null elements.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The response from mutating the rows.  
**Remarks**

This method simply delegates to [MutateRowsAsync(MutateRowsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_MutateRowsAsync_Google_Cloud_Bigtable_V2_MutateRowsRequest_Google_Api_Gax_Grpc_CallSettings_). 

### MutateRowsAsync(MutateRowsRequest, CallSettings)
    
    
    public virtual Task<MutateRowsResponse> MutateRowsAsync(MutateRowsRequest request, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest#Google_Cloud_Bigtable_V2_MutateRowsRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The RPC response.  
  
### MutateRowsAsync(MutateRowsRequest, CancellationToken)
    
    
    public virtual Task<MutateRowsResponse> MutateRowsAsync(MutateRowsRequest request, CancellationToken cancellationToken)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest#Google_Cloud_Bigtable_V2_MutateRowsRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsResponse)` | The RPC response.  
  
### OpenAuthorizedView(CallSettings, BidirectionalStreamingSettings)
    
    
    public virtual BigtableServiceApiClient.OpenAuthorizedViewStream OpenAuthorizedView(CallSettings callSettings = null, BidirectionalStreamingSettings streamingSettings = null)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
`streamingSettings` | `[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)`  
If not null, applies streaming overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[OpenAuthorizedViewStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.OpenAuthorizedViewStream)` | The client-server stream.  
  
### OpenMaterializedView(CallSettings, BidirectionalStreamingSettings)
    
    
    public virtual BigtableServiceApiClient.OpenMaterializedViewStream OpenMaterializedView(CallSettings callSettings = null, BidirectionalStreamingSettings streamingSettings = null)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
`streamingSettings` | `[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)`  
If not null, applies streaming overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[OpenMaterializedViewStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.OpenMaterializedViewStream)` | The client-server stream.  
  
### OpenTable(CallSettings, BidirectionalStreamingSettings)
    
    
    public virtual BigtableServiceApiClient.OpenTableStream OpenTable(CallSettings callSettings = null, BidirectionalStreamingSettings streamingSettings = null)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
`streamingSettings` | `[BidirectionalStreamingSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingSettings.html)`  
If not null, applies streaming overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[OpenTableStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.OpenTableStream)` | The client-server stream.  
  
### PingAndWarm(InstanceName, CallSettings)
    
    
    public virtual PingAndWarmResponse PingAndWarm(InstanceName name, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The RPC response.  
  
### PingAndWarm(InstanceName, string, CallSettings)
    
    
    public virtual PingAndWarmResponse PingAndWarm(InstanceName name, string appProfileId, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The RPC response.  
  
### PingAndWarm(PingAndWarmRequest, CallSettings)
    
    
    public virtual PingAndWarmResponse PingAndWarm(PingAndWarmRequest request, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest#Google_Cloud_Bigtable_V2_PingAndWarmRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The RPC response.  
  
### PingAndWarm(string, CallSettings)
    
    
    public virtual PingAndWarmResponse PingAndWarm(string name, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The RPC response.  
  
### PingAndWarm(string, string, CallSettings)
    
    
    public virtual PingAndWarmResponse PingAndWarm(string name, string appProfileId, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The RPC response.  
  
### PingAndWarmAsync(InstanceName, CallSettings)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(InstanceName name, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(InstanceName, string, CallSettings)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(InstanceName name, string appProfileId, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(InstanceName, string, CancellationToken)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(InstanceName name, string appProfileId, CancellationToken cancellationToken)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(InstanceName, CancellationToken)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(InstanceName name, CancellationToken cancellationToken)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(PingAndWarmRequest, CallSettings)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(PingAndWarmRequest request, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest#Google_Cloud_Bigtable_V2_PingAndWarmRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(PingAndWarmRequest, CancellationToken)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(PingAndWarmRequest request, CancellationToken cancellationToken)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest#Google_Cloud_Bigtable_V2_PingAndWarmRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(string, CallSettings)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(string name, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(string, string, CallSettings)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(string name, string appProfileId, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(string, string, CancellationToken)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(string name, string appProfileId, CancellationToken cancellationToken)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PingAndWarmAsync(string, CancellationToken)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(string name, CancellationToken cancellationToken)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance to check permissions for as well as respond. Values are of the form `projects/<project>/instances/<instance>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
  
### PrepareQuery(InstanceName, string, CallSettings)
    
    
    public virtual PrepareQueryResponse PrepareQuery(InstanceName instanceName, string query, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The RPC response.  
  
### PrepareQuery(InstanceName, string, string, CallSettings)
    
    
    public virtual PrepareQueryResponse PrepareQuery(InstanceName instanceName, string query, string appProfileId, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The RPC response.  
  
### PrepareQuery(PrepareQueryRequest, CallSettings)
    
    
    public virtual PrepareQueryResponse PrepareQuery(PrepareQueryRequest request, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest#Google_Cloud_Bigtable_V2_PrepareQueryRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The RPC response.  
  
### PrepareQuery(string, string, CallSettings)
    
    
    public virtual PrepareQueryResponse PrepareQuery(string instanceName, string query, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The RPC response.  
  
### PrepareQuery(string, string, string, CallSettings)
    
    
    public virtual PrepareQueryResponse PrepareQuery(string instanceName, string query, string appProfileId, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The RPC response.  
  
### PrepareQueryAsync(InstanceName, string, CallSettings)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(InstanceName instanceName, string query, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(InstanceName, string, string, CallSettings)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(InstanceName instanceName, string query, string appProfileId, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(InstanceName, string, string, CancellationToken)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(InstanceName instanceName, string query, string appProfileId, CancellationToken cancellationToken)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(InstanceName, string, CancellationToken)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(InstanceName instanceName, string query, CancellationToken cancellationToken)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.InstanceName.html)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(PrepareQueryRequest, CallSettings)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(PrepareQueryRequest request, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest#Google_Cloud_Bigtable_V2_PrepareQueryRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(PrepareQueryRequest, CancellationToken)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(PrepareQueryRequest request, CancellationToken cancellationToken)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest#Google_Cloud_Bigtable_V2_PrepareQueryRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(string, string, CallSettings)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(string instanceName, string query, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(string, string, string, CallSettings)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(string instanceName, string query, string appProfileId, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(string, string, string, CancellationToken)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(string instanceName, string query, string appProfileId, CancellationToken cancellationToken)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. This value specifies routing for preparing the query. Note that this `app_profile_id` is only used for preparing the query. The actual query execution will use the app profile specified in the `ExecuteQueryRequest`. If not specified, the `default` application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### PrepareQueryAsync(string, string, CancellationToken)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(string instanceName, string query, CancellationToken cancellationToken)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`instanceName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the instance against which the query should be executed. Values are of the form `projects/<project>/instances/<instance>`  
`query` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The query string.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
  
### ReadChangeStream(TableName, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadChangeStreamStream ReadChangeStream(TableName tableName, CallSettings callSettings = null)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Required. The unique name of the table from which to read a change stream. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadChangeStreamStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadChangeStreamStream)` | The server stream.  
  
### ReadChangeStream(TableName, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadChangeStreamStream ReadChangeStream(TableName tableName, string appProfileId, CallSettings callSettings = null)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Required. The unique name of the table from which to read a change stream. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used. Single cluster routing must be configured on the profile.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadChangeStreamStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadChangeStreamStream)` | The server stream.  
  
### ReadChangeStream(ReadChangeStreamRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadChangeStreamStream ReadChangeStream(ReadChangeStreamRequest request, CallSettings callSettings = null)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadChangeStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamRequest#Google_Cloud_Bigtable_V2_ReadChangeStreamRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadChangeStreamStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadChangeStreamStream)` | The server stream.  
  
### ReadChangeStream(string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadChangeStreamStream ReadChangeStream(string tableName, CallSettings callSettings = null)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the table from which to read a change stream. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadChangeStreamStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadChangeStreamStream)` | The server stream.  
  
### ReadChangeStream(string, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadChangeStreamStream ReadChangeStream(string tableName, string appProfileId, CallSettings callSettings = null)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The unique name of the table from which to read a change stream. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`. Change streaming must be enabled on the table.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used. Single cluster routing must be configured on the profile.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadChangeStreamStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadChangeStreamStream)` | The server stream.  
  
### ReadModifyWriteRow(TableName, BigtableByteString, params ReadModifyWriteRule[])
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(TableName tableName, BigtableByteString rowKey, params ReadModifyWriteRule[] rules)

Modifies a row atomically on the server. The method reads the latest existing version and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the version is the greater of the previous value's version or the current server version. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the read/modify/write rules should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the read/modify/write rules should be applied. Must not be empty.  
`rules` | `[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The response from modifying the row.  
**Remarks**

Note that the server version is based on the current timestamp since the Unix epoch, so for columns which are updated using ReadModifyWriteRow, other reads and writes of those columns should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [ReadModifyWriteRow(ReadModifyWriteRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_ReadModifyWriteRow_Google_Cloud_Bigtable_V2_ReadModifyWriteRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### ReadModifyWriteRow(TableName, BigtableByteString, IEnumerable<ReadModifyWriteRule>, CallSettings)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(TableName tableName, BigtableByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing version and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the version is the greater of the previous value's version or the current server version. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the read/modify/write rules should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the read/modify/write rules should be applied. Must not be empty.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. Must not be null, or contain null elements.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The response from modifying the row.  
**Remarks**

Note that the server version is based on the current timestamp since the Unix epoch, so for columns which are updated using ReadModifyWriteRow, other reads and writes of those columns should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [ReadModifyWriteRow(ReadModifyWriteRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_ReadModifyWriteRow_Google_Cloud_Bigtable_V2_ReadModifyWriteRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### ReadModifyWriteRow(ReadModifyWriteRowRequest, CallSettings)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(ReadModifyWriteRowRequest request, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest#Google_Cloud_Bigtable_V2_ReadModifyWriteRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The RPC response.  
  
### ReadModifyWriteRowAsync(TableName, BigtableByteString, params ReadModifyWriteRule[])
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(TableName tableName, BigtableByteString rowKey, params ReadModifyWriteRule[] rules)

Asynchronously modifies a row atomically on the server. The method reads the latest existing version and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the version is the greater of the previous value's version or the current server version. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the read/modify/write rules should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the read/modify/write rules should be applied. Must not be empty.  
`rules` | `[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The response from modifying the row.  
**Remarks**

Note that the server version is based on the current timestamp since the Unix epoch, so for columns which are updated using ReadModifyWriteRow, other reads and writes of those columns should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [ReadModifyWriteRowAsync(ReadModifyWriteRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_ReadModifyWriteRowAsync_Google_Cloud_Bigtable_V2_ReadModifyWriteRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

**Example**
    
    
    // Increase the value of the cell with the "Level 1" qualifier in the
    // "Score" column family by 55.
    ReadModifyWriteRowResponse response = await client.ReadModifyWriteRowAsync(
        new TableName(projectId, instanceId, tableId),
        "user12345",
        ReadModifyWriteRules.Increment("Score", "Level 1", 55));
    
    Cell modifiedCell = response.Row.Families[0].Columns[0].Cells[0];
    
    // Implicitly convert the ByteString Value into a BigtableByteString,
    // which supports additional conversions specific to Bigtable.
    BigtableByteString value = modifiedCell.Value;
    
    // Convert the BigtableByteString to a long to obtain the updated value.
    long newScore = (long) value;
    Console.WriteLine($"The total score for level 1 is now {newScore}");
    

### ReadModifyWriteRowAsync(TableName, BigtableByteString, IEnumerable<ReadModifyWriteRule>, CallSettings)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(TableName tableName, BigtableByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, CallSettings callSettings = null)

Asynchronously modifies a row atomically on the server. The method reads the latest existing version and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the version is the greater of the previous value's version or the current server version. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table to which the read/modify/write rules should be applied. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to which the read/modify/write rules should be applied. Must not be empty.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. Must not be null, or contain null elements.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The response from modifying the row.  
**Remarks**

Note that the server version is based on the current timestamp since the Unix epoch, so for columns which are updated using ReadModifyWriteRow, other reads and writes of those columns should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `rowKey` can be specified using a string as well and its UTF-8 representations will be used. 

This method simply delegates to [ReadModifyWriteRowAsync(ReadModifyWriteRowRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_ReadModifyWriteRowAsync_Google_Cloud_Bigtable_V2_ReadModifyWriteRowRequest_Google_Api_Gax_Grpc_CallSettings_). 

### ReadModifyWriteRowAsync(ReadModifyWriteRowRequest, CallSettings)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(ReadModifyWriteRowRequest request, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest#Google_Cloud_Bigtable_V2_ReadModifyWriteRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
  
### ReadModifyWriteRowAsync(ReadModifyWriteRowRequest, CancellationToken)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(ReadModifyWriteRowRequest request, CancellationToken cancellationToken)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest#Google_Cloud_Bigtable_V2_ReadModifyWriteRowRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
  
### ReadRow(TableName, BigtableByteString, RowFilter, CallSettings)
    
    
    public virtual Row ReadRow(TableName tableName, BigtableByteString rowKey, RowFilter filter = null, CallSettings callSettings = null)

Returns the contents of the requested row, optionally applying the specified Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table from which to read. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to read. Must not be empty.  
`filter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to apply to the contents of the specified row. If null, reads the entirety of the row.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Row](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row)` | The row from the server or null if it does not exist.  
**Remarks**

This method simply delegates to [ReadRowAsync(TableName, BigtableByteString, RowFilter, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_ReadRowAsync_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_Common_V2_BigtableByteString_Google_Cloud_Bigtable_V2_RowFilter_Google_Api_Gax_Grpc_CallSettings_). 

### ReadRowAsync(TableName, BigtableByteString, RowFilter, CallSettings)
    
    
    public virtual Task<Row> ReadRowAsync(TableName tableName, BigtableByteString rowKey, RowFilter filter = null, CallSettings callSettings = null)

Asynchronously returns the contents of the requested row, optionally applying the specified Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table from which to read. Must not be null.  
`rowKey` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The key of the row to read. Must not be empty.  
`filter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to apply to the contents of the specified row. If null, reads the entirety of the row.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Row](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Row)` | The row from the server or null if it does not exist.  
**Remarks**

This method simply delegates to [ReadRows(TableName, RowSet, RowFilter, long?, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_ReadRows_Google_Cloud_Bigtable_Common_V2_TableName_Google_Cloud_Bigtable_V2_RowSet_Google_Cloud_Bigtable_V2_RowFilter_System_Nullable_System_Int64__Google_Api_Gax_Grpc_CallSettings_) and takes the single row result or null if no rows are returned. 

**Example**
    
    
    // Only read cells from the "Line X" columns, where X is some
    // digit, in the Address column family and only take the most
    // recent cell from each column.
    Row row = await client.ReadRowAsync(
        new TableName(projectId, instanceId, tableId),
        "user12345",
        RowFilters.Chain(
            RowFilters.FamilyNameExact("Address"),
            RowFilters.ColumnQualifierRegex(@"Line \d"),
            RowFilters.CellsPerColumnLimit(1)),
        CallSettings.FromCancellationToken(cancellationToken));
    
    Family addressFamily = row.Families.FirstOrDefault();
    if (addressFamily != null)
    {
        foreach (Column column in addressFamily.Columns)
        {
            Console.WriteLine($"    Column qualifier: {column.Qualifier.ToStringUtf8()}");
            foreach (Cell cell in column.Cells)
            {
                Console.WriteLine($"      Cell value: {cell.Value.ToStringUtf8()}");
                Console.WriteLine($"      Timestamp: {cell.Version.ToDateTime()}");
                Console.WriteLine($"      Labels: {string.Join(", ", cell.Labels)}");
            }
        }
    }
    

### ReadRows(TableName, RowSet, RowFilter, long?, CallSettings)
    
    
    public virtual ReadRowsStream ReadRows(TableName tableName, RowSet rows = null, RowFilter filter = null, long? rowsLimit = null, CallSettings callSettings = null)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
The unique name of the table from which to read. Must not be null.  
`rows` | `[RowSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowSet)`  
The row keys and/or ranges to read. If null, reads from all rows.  
`filter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to apply to the contents of the specified row(s). If null, reads the entirety of each row.  
`rowsLimit` | `[long](https://learn.microsoft.com/dotnet/api/system.int64)`  
The read will terminate after committing to N rows' worth of results. If null or 0, returns all results.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsStream)` | The server stream.  
**Remarks**

This method simply delegates to [ReadRows(ReadRowsRequest, CallSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableClient#Google_Cloud_Bigtable_V2_BigtableClient_ReadRows_Google_Cloud_Bigtable_V2_ReadRowsRequest_Google_Api_Gax_Grpc_CallSettings_). 

**Example**
    
    
    TableName tableName = new TableName(projectId, instanceId, tableId);
    
    // Read rows whose keys are greater than or equal to 'user00000'
    // and less than 'user99999'.
    RowSet rows = RowSet.FromRowRanges(
        RowRange.ClosedOpen("user00000", "user99999"));
    
    // Only read cells from the "Address" column family and only take the most recent cell from each column.
    RowFilter filter = RowFilters.Chain(
        RowFilters.FamilyNameExact("Address"),
        RowFilters.CellsPerColumnLimit(1));
    
    // Just read the first 10 rows.
    long rowsLimit = 10;
    
    // Make the request
    ReadRowsStream streamingResponse = client.ReadRows(
        tableName,
        rows,
        filter,
        rowsLimit,
        CallSettings.FromCancellationToken(cancellationToken));
    
    // Read streaming responses from server until complete
    await foreach (Row row in streamingResponse)
    {
        Console.WriteLine($"Row key: {row.Key.ToStringUtf8()}");
        foreach (Family family in row.Families)
        {
            Console.WriteLine($"  Family name: {family.Name}");
            foreach (Column column in family.Columns)
            {
                Console.WriteLine($"    Column qualifier: {column.Qualifier.ToStringUtf8()}");
                foreach (Cell cell in column.Cells)
                {
                    Console.WriteLine($"      Cell value: {cell.Value.ToStringUtf8()}");
                    Console.WriteLine($"      Timestamp: {cell.Version.ToDateTime()}");
                    Console.WriteLine($"      Labels: {string.Join(", ", cell.Labels)}");
                }
            }
        }
    }
    

### ReadRows(ReadRowsRequest, CallSettings)
    
    
    public virtual ReadRowsStream ReadRows(ReadRowsRequest request, CallSettings callSettings = null)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest#Google_Cloud_Bigtable_V2_ReadRowsRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsStream)` | The server stream.  
  
### SampleRowKeys(TableName, CallSettings)
    
    
    public virtual BigtableServiceApiClient.SampleRowKeysStream SampleRowKeys(TableName tableName, CallSettings callSettings = null)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table from which to sample row keys. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[SampleRowKeysStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.SampleRowKeysStream)` | The server stream.  
**Example**
    
    
    BigtableServiceApiClient.SampleRowKeysStream streamingResponse = client.SampleRowKeys(
        new TableName(projectId, instanceId, tableId),
        CallSettings.FromCancellationToken(cancellationToken));
    
    // Get all streaming responses from server in a list so they can be easily iterated.
    IList<SampleRowKeysResponse> rowKeySamples =
        await streamingResponse.ToListAsync(cancellationToken);
    
    long previousRowOffsetBytes = 0;
    foreach (SampleRowKeysResponse rowKeySample in rowKeySamples)
    {
        // The OffsetBytes are non-decreasing, so their difference should always be 0 or more.
        long offsetDifference = rowKeySample.OffsetBytes - previousRowOffsetBytes;
    
        Console.WriteLine($"Row key: {rowKeySample.RowKey.ToStringUtf8()}, at offset {rowKeySample.OffsetBytes}");
        Console.WriteLine($"  Approximate bytes since previous row sample: {offsetDifference}");
    
        previousRowOffsetBytes = rowKeySample.OffsetBytes;
    }
    

### SampleRowKeys(TableName, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.SampleRowKeysStream SampleRowKeys(TableName tableName, string appProfileId, CallSettings callSettings = null)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table from which to sample row keys. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[SampleRowKeysStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.SampleRowKeysStream)` | The server stream.  
  
### SampleRowKeys(SampleRowKeysRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.SampleRowKeysStream SampleRowKeys(SampleRowKeysRequest request, CallSettings callSettings = null)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest)`  
The request object containing all of the parameters for the API call. If the [AppProfileId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest#Google_Cloud_Bigtable_V2_SampleRowKeysRequest_AppProfileId) has not been specified, it will be initialized from the value stored in the client.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[SampleRowKeysStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.SampleRowKeysStream)` | The server stream.  
  
### SampleRowKeys(string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.SampleRowKeysStream SampleRowKeys(string tableName, CallSettings callSettings = null)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table from which to sample row keys. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[SampleRowKeysStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.SampleRowKeysStream)` | The server stream.  
  
### SampleRowKeys(string, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.SampleRowKeysStream SampleRowKeys(string tableName, string appProfileId, CallSettings callSettings = null)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table from which to sample row keys. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[SampleRowKeysStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.SampleRowKeysStream)` | The server stream.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
