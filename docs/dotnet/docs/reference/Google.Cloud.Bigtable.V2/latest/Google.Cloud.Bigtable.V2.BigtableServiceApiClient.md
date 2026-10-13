---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient
title: Google Bigtable v2 API - Class BigtableServiceApiClient (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:40.926659+00:00
---

# Google Bigtable v2 API - Class BigtableServiceApiClient (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class BigtableServiceApiClient (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public abstract class BigtableServiceApiClient

Reference documentation and code samples for the Google Bigtable v2 API class BigtableServiceApiClient.

BigtableServiceApi client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigtableServiceApiClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[BigtableServiceApiClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClientImpl)

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
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the BigtableServiceApi service, which is a host of "bigtable.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default BigtableServiceApi scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default BigtableServiceApi scopes are:

  * <https://www.googleapis.com/auth/bigtable.data>
  * <https://www.googleapis.com/auth/bigtable.data.readonly>
  * <https://www.googleapis.com/auth/cloud-bigtable.data>
  * <https://www.googleapis.com/auth/cloud-bigtable.data.readonly>
  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/cloud-platform.read-only>



### GrpcClient
    
    
    public virtual Bigtable.BigtableClient GrpcClient { get; }

The underlying gRPC BigtableServiceApi client

**Property Value**  
---  
**Type** | **Description**  
`[Bigtable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable)[BigtableClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Bigtable.BigtableClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### CheckAndMutateRow(TableName, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(TableName tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = bigtableServiceApiClient.CheckAndMutateRow(tableName, rowKey, predicateFilter, trueMutations, falseMutations);
    

### CheckAndMutateRow(TableName, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, string, CallSettings)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(TableName tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, string appProfileId, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::CheckAndMutateRowResponse response = bigtableServiceApiClient.CheckAndMutateRow(tableName, rowKey, predicateFilter, trueMutations, falseMutations, appProfileId);
    

### CheckAndMutateRow(CheckAndMutateRowRequest, CallSettings)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(CheckAndMutateRowRequest request, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::CheckAndMutateRowRequest request = new gcbv::CheckAndMutateRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        TrueMutations =
        {
            new gcbv::Mutation(),
        },
        FalseMutations =
        {
            new gcbv::Mutation(),
        },
        PredicateFilter = new gcbv::RowFilter(),
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = bigtableServiceApiClient.CheckAndMutateRow(request);
    

### CheckAndMutateRow(string, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(string tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = bigtableServiceApiClient.CheckAndMutateRow(tableName, rowKey, predicateFilter, trueMutations, falseMutations);
    

### CheckAndMutateRow(string, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, string, CallSettings)
    
    
    public virtual CheckAndMutateRowResponse CheckAndMutateRow(string tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, string appProfileId, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::CheckAndMutateRowResponse response = bigtableServiceApiClient.CheckAndMutateRow(tableName, rowKey, predicateFilter, trueMutations, falseMutations, appProfileId);
    

### CheckAndMutateRowAsync(TableName, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(TableName tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(tableName, rowKey, predicateFilter, trueMutations, falseMutations);
    

### CheckAndMutateRowAsync(TableName, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, string, CallSettings)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(TableName tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, string appProfileId, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(tableName, rowKey, predicateFilter, trueMutations, falseMutations, appProfileId);
    

### CheckAndMutateRowAsync(TableName, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, string, CancellationToken)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(TableName tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, string appProfileId, CancellationToken cancellationToken)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(tableName, rowKey, predicateFilter, trueMutations, falseMutations, appProfileId);
    

### CheckAndMutateRowAsync(TableName, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, CancellationToken)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(TableName tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, CancellationToken cancellationToken)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(tableName, rowKey, predicateFilter, trueMutations, falseMutations);
    

### CheckAndMutateRowAsync(CheckAndMutateRowRequest, CallSettings)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(CheckAndMutateRowRequest request, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::CheckAndMutateRowRequest request = new gcbv::CheckAndMutateRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        TrueMutations =
        {
            new gcbv::Mutation(),
        },
        FalseMutations =
        {
            new gcbv::Mutation(),
        },
        PredicateFilter = new gcbv::RowFilter(),
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(request);
    

### CheckAndMutateRowAsync(CheckAndMutateRowRequest, CancellationToken)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(CheckAndMutateRowRequest request, CancellationToken cancellationToken)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::CheckAndMutateRowRequest request = new gcbv::CheckAndMutateRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        TrueMutations =
        {
            new gcbv::Mutation(),
        },
        FalseMutations =
        {
            new gcbv::Mutation(),
        },
        PredicateFilter = new gcbv::RowFilter(),
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(request);
    

### CheckAndMutateRowAsync(string, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(string tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(tableName, rowKey, predicateFilter, trueMutations, falseMutations);
    

### CheckAndMutateRowAsync(string, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, string, CallSettings)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(string tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, string appProfileId, CallSettings callSettings = null)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(tableName, rowKey, predicateFilter, trueMutations, falseMutations, appProfileId);
    

### CheckAndMutateRowAsync(string, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, string, CancellationToken)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(string tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, string appProfileId, CancellationToken cancellationToken)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(tableName, rowKey, predicateFilter, trueMutations, falseMutations, appProfileId);
    

### CheckAndMutateRowAsync(string, ByteString, RowFilter, IEnumerable<Mutation>, IEnumerable<Mutation>, CancellationToken)
    
    
    public virtual Task<CheckAndMutateRowResponse> CheckAndMutateRowAsync(string tableName, ByteString rowKey, RowFilter predicateFilter, IEnumerable<Mutation> trueMutations, IEnumerable<Mutation> falseMutations, CancellationToken cancellationToken)

Mutates a row atomically based on the output of a predicate Reader filter.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the conditional mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the conditional mutation should be applied.  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to be applied to the contents of the specified row. Depending on whether or not any results are yielded, either `true_mutations` or `false_mutations` will be executed. If unset, checks that the row contains any values at all.  
`trueMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` yields at least one cell when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `false_mutations` is empty, and at most 100000.  
`falseMutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Changes to be atomically applied to the specified row if `predicate_filter` does not yield any cells when applied to `row_key`. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry if `true_mutations` is empty, and at most 100000.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[CheckAndMutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.CheckAndMutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    gcbv::RowFilter predicateFilter = new gcbv::RowFilter();
    IEnumerable<gcbv::Mutation> trueMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    IEnumerable<gcbv::Mutation> falseMutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::CheckAndMutateRowResponse response = await bigtableServiceApiClient.CheckAndMutateRowAsync(tableName, rowKey, predicateFilter, trueMutations, falseMutations);
    

### Create()
    
    
    public static BigtableServiceApiClient Create()

Synchronously creates a [BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [BigtableServiceApiClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClientBuilder) .

**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)` | The created [BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<BigtableServiceApiClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [BigtableServiceApiClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClientBuilder) .

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)` | The task representing the created [BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient).  
  
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
**Example**
    
    
                // Create client
                gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
                // Initialize request argument(s)
                InstanceName instanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
                string query = "";
                // Make the request, returning a streaming response
    #pragma warning disable CS0612
                using gcbv::BigtableServiceApiClient.ExecuteQueryStream response = bigtableServiceApiClient.ExecuteQuery(instanceName, query);
    #pragma warning restore CS0612
    
                // Read streaming responses from server until complete
                // Note that C# 8 code can use await foreach
                AsyncResponseStream<gcbv::ExecuteQueryResponse> responseStream = response.GetResponseStream();
                while (await responseStream.MoveNextAsync())
                {
                    gcbv::ExecuteQueryResponse responseItem = responseStream.Current;
                    // Do something with streamed response
                }
                // The response stream has completed
    

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
**Example**
    
    
                // Create client
                gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
                // Initialize request argument(s)
                InstanceName instanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
                string query = "";
                string appProfileId = "";
                // Make the request, returning a streaming response
    #pragma warning disable CS0612
                using gcbv::BigtableServiceApiClient.ExecuteQueryStream response = bigtableServiceApiClient.ExecuteQuery(instanceName, query, appProfileId);
    #pragma warning restore CS0612
    
                // Read streaming responses from server until complete
                // Note that C# 8 code can use await foreach
                AsyncResponseStream<gcbv::ExecuteQueryResponse> responseStream = response.GetResponseStream();
                while (await responseStream.MoveNextAsync())
                {
                    gcbv::ExecuteQueryResponse responseItem = responseStream.Current;
                    // Do something with streamed response
                }
                // The response stream has completed
    

### ExecuteQuery(ExecuteQueryRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ExecuteQueryStream ExecuteQuery(ExecuteQueryRequest request, CallSettings callSettings = null)

Executes a SQL query against a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExecuteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ExecuteQueryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ExecuteQueryStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ExecuteQueryStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::ExecuteQueryRequest request = new gcbv::ExecuteQueryRequest
    {
        InstanceNameAsInstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
        Params =
        {
            {
                "",
                new gcbv::Value()
            },
        },
        ResumeToken = ByteString.Empty,
        PreparedQuery = ByteString.Empty,
        ViewParameters =
        {
            {
                "",
                new gcbv::Value()
            },
        },
    };
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ExecuteQueryStream response = bigtableServiceApiClient.ExecuteQuery(request);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ExecuteQueryResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ExecuteQueryResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
                // Create client
                gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
                // Initialize request argument(s)
                string instanceName = "projects/[PROJECT]/instances/[INSTANCE]";
                string query = "";
                // Make the request, returning a streaming response
    #pragma warning disable CS0612
                using gcbv::BigtableServiceApiClient.ExecuteQueryStream response = bigtableServiceApiClient.ExecuteQuery(instanceName, query);
    #pragma warning restore CS0612
    
                // Read streaming responses from server until complete
                // Note that C# 8 code can use await foreach
                AsyncResponseStream<gcbv::ExecuteQueryResponse> responseStream = response.GetResponseStream();
                while (await responseStream.MoveNextAsync())
                {
                    gcbv::ExecuteQueryResponse responseItem = responseStream.Current;
                    // Do something with streamed response
                }
                // The response stream has completed
    

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
**Example**
    
    
                // Create client
                gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
                // Initialize request argument(s)
                string instanceName = "projects/[PROJECT]/instances/[INSTANCE]";
                string query = "";
                string appProfileId = "";
                // Make the request, returning a streaming response
    #pragma warning disable CS0612
                using gcbv::BigtableServiceApiClient.ExecuteQueryStream response = bigtableServiceApiClient.ExecuteQuery(instanceName, query, appProfileId);
    #pragma warning restore CS0612
    
                // Read streaming responses from server until complete
                // Note that C# 8 code can use await foreach
                AsyncResponseStream<gcbv::ExecuteQueryResponse> responseStream = response.GetResponseStream();
                while (await responseStream.MoveNextAsync())
                {
                    gcbv::ExecuteQueryResponse responseItem = responseStream.Current;
                    // Do something with streamed response
                }
                // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream response = bigtableServiceApiClient.GenerateInitialChangeStreamPartitions(tableName);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::GenerateInitialChangeStreamPartitionsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::GenerateInitialChangeStreamPartitionsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream response = bigtableServiceApiClient.GenerateInitialChangeStreamPartitions(tableName, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::GenerateInitialChangeStreamPartitionsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::GenerateInitialChangeStreamPartitionsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream GenerateInitialChangeStreamPartitions(GenerateInitialChangeStreamPartitionsRequest request, CallSettings callSettings = null)

Returns the current list of partitions that make up the table's change stream. The union of partitions will cover the entire keyspace. Partitions can be read with `ReadChangeStream`. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateInitialChangeStreamPartitionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GenerateInitialChangeStreamPartitionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[GenerateInitialChangeStreamPartitionsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::GenerateInitialChangeStreamPartitionsRequest request = new gcbv::GenerateInitialChangeStreamPartitionsRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        AppProfileId = "",
    };
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream response = bigtableServiceApiClient.GenerateInitialChangeStreamPartitions(request);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::GenerateInitialChangeStreamPartitionsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::GenerateInitialChangeStreamPartitionsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream response = bigtableServiceApiClient.GenerateInitialChangeStreamPartitions(tableName);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::GenerateInitialChangeStreamPartitionsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::GenerateInitialChangeStreamPartitionsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.GenerateInitialChangeStreamPartitionsStream response = bigtableServiceApiClient.GenerateInitialChangeStreamPartitions(tableName, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::GenerateInitialChangeStreamPartitionsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::GenerateInitialChangeStreamPartitionsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### GetClientConfiguration(GetClientConfigurationRequest, CallSettings)
    
    
    public virtual ClientConfiguration GetClientConfiguration(GetClientConfigurationRequest request, CallSettings callSettings = null)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::GetClientConfigurationRequest request = new gcbv::GetClientConfigurationRequest
    {
        InstanceNameAsInstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
    };
    // Make the request
    gcbv::ClientConfiguration response = bigtableServiceApiClient.GetClientConfiguration(request);
    

### GetClientConfigurationAsync(GetClientConfigurationRequest, CallSettings)
    
    
    public virtual Task<ClientConfiguration> GetClientConfigurationAsync(GetClientConfigurationRequest request, CallSettings callSettings = null)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::GetClientConfigurationRequest request = new gcbv::GetClientConfigurationRequest
    {
        InstanceNameAsInstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
    };
    // Make the request
    gcbv::ClientConfiguration response = await bigtableServiceApiClient.GetClientConfigurationAsync(request);
    

### GetClientConfigurationAsync(GetClientConfigurationRequest, CancellationToken)
    
    
    public virtual Task<ClientConfiguration> GetClientConfigurationAsync(GetClientConfigurationRequest request, CancellationToken cancellationToken)

This RPC is only intended to be used by the official Cloud Bigtable client libraries to implement the Bigtable Session based protocol. It is subject to change without notice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClientConfigurationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.GetClientConfigurationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ClientConfiguration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ClientConfiguration)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::GetClientConfigurationRequest request = new gcbv::GetClientConfigurationRequest
    {
        InstanceNameAsInstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
    };
    // Make the request
    gcbv::ClientConfiguration response = await bigtableServiceApiClient.GetClientConfigurationAsync(request);
    

### MutateRow(TableName, ByteString, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual MutateRowResponse MutateRow(TableName tableName, ByteString rowKey, IEnumerable<Mutation> mutations, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::MutateRowResponse response = bigtableServiceApiClient.MutateRow(tableName, rowKey, mutations);
    

### MutateRow(TableName, ByteString, IEnumerable<Mutation>, string, CallSettings)
    
    
    public virtual MutateRowResponse MutateRow(TableName tableName, ByteString rowKey, IEnumerable<Mutation> mutations, string appProfileId, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::MutateRowResponse response = bigtableServiceApiClient.MutateRow(tableName, rowKey, mutations, appProfileId);
    

### MutateRow(MutateRowRequest, CallSettings)
    
    
    public virtual MutateRowResponse MutateRow(MutateRowRequest request, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::MutateRowRequest request = new gcbv::MutateRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        Mutations =
        {
            new gcbv::Mutation(),
        },
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
        Idempotency = new gcbv::Idempotency(),
    };
    // Make the request
    gcbv::MutateRowResponse response = bigtableServiceApiClient.MutateRow(request);
    

### MutateRow(string, ByteString, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual MutateRowResponse MutateRow(string tableName, ByteString rowKey, IEnumerable<Mutation> mutations, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::MutateRowResponse response = bigtableServiceApiClient.MutateRow(tableName, rowKey, mutations);
    

### MutateRow(string, ByteString, IEnumerable<Mutation>, string, CallSettings)
    
    
    public virtual MutateRowResponse MutateRow(string tableName, ByteString rowKey, IEnumerable<Mutation> mutations, string appProfileId, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::MutateRowResponse response = bigtableServiceApiClient.MutateRow(tableName, rowKey, mutations, appProfileId);
    

### MutateRowAsync(TableName, ByteString, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(TableName tableName, ByteString rowKey, IEnumerable<Mutation> mutations, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(tableName, rowKey, mutations);
    

### MutateRowAsync(TableName, ByteString, IEnumerable<Mutation>, string, CallSettings)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(TableName tableName, ByteString rowKey, IEnumerable<Mutation> mutations, string appProfileId, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(tableName, rowKey, mutations, appProfileId);
    

### MutateRowAsync(TableName, ByteString, IEnumerable<Mutation>, string, CancellationToken)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(TableName tableName, ByteString rowKey, IEnumerable<Mutation> mutations, string appProfileId, CancellationToken cancellationToken)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(tableName, rowKey, mutations, appProfileId);
    

### MutateRowAsync(TableName, ByteString, IEnumerable<Mutation>, CancellationToken)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(TableName tableName, ByteString rowKey, IEnumerable<Mutation> mutations, CancellationToken cancellationToken)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(tableName, rowKey, mutations);
    

### MutateRowAsync(MutateRowRequest, CallSettings)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(MutateRowRequest request, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::MutateRowRequest request = new gcbv::MutateRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        Mutations =
        {
            new gcbv::Mutation(),
        },
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
        Idempotency = new gcbv::Idempotency(),
    };
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(request);
    

### MutateRowAsync(MutateRowRequest, CancellationToken)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(MutateRowRequest request, CancellationToken cancellationToken)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::MutateRowRequest request = new gcbv::MutateRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        Mutations =
        {
            new gcbv::Mutation(),
        },
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
        Idempotency = new gcbv::Idempotency(),
    };
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(request);
    

### MutateRowAsync(string, ByteString, IEnumerable<Mutation>, CallSettings)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(string tableName, ByteString rowKey, IEnumerable<Mutation> mutations, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(tableName, rowKey, mutations);
    

### MutateRowAsync(string, ByteString, IEnumerable<Mutation>, string, CallSettings)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(string tableName, ByteString rowKey, IEnumerable<Mutation> mutations, string appProfileId, CallSettings callSettings = null)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(tableName, rowKey, mutations, appProfileId);
    

### MutateRowAsync(string, ByteString, IEnumerable<Mutation>, string, CancellationToken)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(string tableName, ByteString rowKey, IEnumerable<Mutation> mutations, string appProfileId, CancellationToken cancellationToken)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(tableName, rowKey, mutations, appProfileId);
    

### MutateRowAsync(string, ByteString, IEnumerable<Mutation>, CancellationToken)
    
    
    public virtual Task<MutateRowResponse> MutateRowAsync(string tableName, ByteString rowKey, IEnumerable<Mutation> mutations, CancellationToken cancellationToken)

Mutates a row atomically. Cells already present in the row are left unchanged unless explicitly changed by `mutation`.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the mutation should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the mutation should be applied.  
`mutations` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Mutation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.Mutation)`  
Required. Changes to be atomically applied to the specified row. Entries are applied in order, meaning that earlier mutations can be masked by later ones. Must contain at least one entry and at most 100000.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[MutateRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::Mutation> mutations = new gcbv::Mutation[]
    {
        new gcbv::Mutation(),
    };
    // Make the request
    gcbv::MutateRowResponse response = await bigtableServiceApiClient.MutateRowAsync(tableName, rowKey, mutations);
    

### MutateRows(TableName, IEnumerable<Entry>, CallSettings)
    
    
    public virtual BigtableServiceApiClient.MutateRowsStream MutateRows(TableName tableName, IEnumerable<MutateRowsRequest.Types.Entry> entries, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the mutations should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`entries` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)`  
Required. The row keys and corresponding mutations to be applied in bulk. Each entry is applied as an atomic mutation, but the entries may be applied in arbitrary order (even between entries for the same row). At least one entry must be specified, and in total the entries can contain at most 100000 mutations.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[MutateRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.MutateRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    IEnumerable<gcbv::MutateRowsRequest.Types.Entry> entries = new gcbv::MutateRowsRequest.Types.Entry[]
    {
        new gcbv::MutateRowsRequest.Types.Entry(),
    };
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.MutateRowsStream response = bigtableServiceApiClient.MutateRows(tableName, entries);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::MutateRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::MutateRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### MutateRows(TableName, IEnumerable<Entry>, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.MutateRowsStream MutateRows(TableName tableName, IEnumerable<MutateRowsRequest.Types.Entry> entries, string appProfileId, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the mutations should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`entries` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)`  
Required. The row keys and corresponding mutations to be applied in bulk. Each entry is applied as an atomic mutation, but the entries may be applied in arbitrary order (even between entries for the same row). At least one entry must be specified, and in total the entries can contain at most 100000 mutations.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[MutateRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.MutateRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    IEnumerable<gcbv::MutateRowsRequest.Types.Entry> entries = new gcbv::MutateRowsRequest.Types.Entry[]
    {
        new gcbv::MutateRowsRequest.Types.Entry(),
    };
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.MutateRowsStream response = bigtableServiceApiClient.MutateRows(tableName, entries, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::MutateRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::MutateRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### MutateRows(MutateRowsRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.MutateRowsStream MutateRows(MutateRowsRequest request, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[MutateRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.MutateRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::MutateRowsRequest request = new gcbv::MutateRowsRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        Entries =
        {
            new gcbv::MutateRowsRequest.Types.Entry(),
        },
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
    };
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.MutateRowsStream response = bigtableServiceApiClient.MutateRows(request);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::MutateRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::MutateRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### MutateRows(string, IEnumerable<Entry>, CallSettings)
    
    
    public virtual BigtableServiceApiClient.MutateRowsStream MutateRows(string tableName, IEnumerable<MutateRowsRequest.Types.Entry> entries, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the mutations should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`entries` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)`  
Required. The row keys and corresponding mutations to be applied in bulk. Each entry is applied as an atomic mutation, but the entries may be applied in arbitrary order (even between entries for the same row). At least one entry must be specified, and in total the entries can contain at most 100000 mutations.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[MutateRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.MutateRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    IEnumerable<gcbv::MutateRowsRequest.Types.Entry> entries = new gcbv::MutateRowsRequest.Types.Entry[]
    {
        new gcbv::MutateRowsRequest.Types.Entry(),
    };
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.MutateRowsStream response = bigtableServiceApiClient.MutateRows(tableName, entries);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::MutateRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::MutateRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### MutateRows(string, IEnumerable<Entry>, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.MutateRowsStream MutateRows(string tableName, IEnumerable<MutateRowsRequest.Types.Entry> entries, string appProfileId, CallSettings callSettings = null)

Mutates multiple rows in a batch. Each individual row is mutated atomically as in MutateRow, but the entire batch is not executed atomically.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the mutations should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`entries` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[MutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types)[Entry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.MutateRowsRequest.Types.Entry)`  
Required. The row keys and corresponding mutations to be applied in bulk. Each entry is applied as an atomic mutation, but the entries may be applied in arbitrary order (even between entries for the same row). At least one entry must be specified, and in total the entries can contain at most 100000 mutations.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[MutateRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.MutateRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    IEnumerable<gcbv::MutateRowsRequest.Types.Entry> entries = new gcbv::MutateRowsRequest.Types.Entry[]
    {
        new gcbv::MutateRowsRequest.Types.Entry(),
    };
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.MutateRowsStream response = bigtableServiceApiClient.MutateRows(tableName, entries, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::MutateRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::MutateRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize streaming call, retrieving the stream object
    using gcbv::BigtableServiceApiClient.OpenAuthorizedViewStream response = bigtableServiceApiClient.OpenAuthorizedView();
    
    // Sending requests and retrieving responses can be arbitrarily interleaved
    // Exact sequence will depend on client/server behavior
    
    // Create task to do something with responses from server
    Task responseHandlerTask = Task.Run(async () =>
    {
        // Note that C# 8 code can use await foreach
        AsyncResponseStream<gcbv::SessionResponse> responseStream = response.GetResponseStream();
        while (await responseStream.MoveNextAsync())
        {
            gcbv::SessionResponse responseItem = responseStream.Current;
            // Do something with streamed response
        }
        // The response stream has completed
    });
    
    // Send requests to the server
    bool done = false;
    while (!done)
    {
        // Initialize a request
        gcbv::SessionRequest request = new gcbv::SessionRequest
        {
            OpenSession = new gcbv::OpenSessionRequest(),
        };
        // Stream a request to the server
        await response.WriteAsync(request);
        // Set "done" to true when sending requests is complete
    }
    
    // Complete writing requests to the stream
    await response.WriteCompleteAsync();
    // Await the response handler
    // This will complete once all server responses have been processed
    await responseHandlerTask;
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize streaming call, retrieving the stream object
    using gcbv::BigtableServiceApiClient.OpenMaterializedViewStream response = bigtableServiceApiClient.OpenMaterializedView();
    
    // Sending requests and retrieving responses can be arbitrarily interleaved
    // Exact sequence will depend on client/server behavior
    
    // Create task to do something with responses from server
    Task responseHandlerTask = Task.Run(async () =>
    {
        // Note that C# 8 code can use await foreach
        AsyncResponseStream<gcbv::SessionResponse> responseStream = response.GetResponseStream();
        while (await responseStream.MoveNextAsync())
        {
            gcbv::SessionResponse responseItem = responseStream.Current;
            // Do something with streamed response
        }
        // The response stream has completed
    });
    
    // Send requests to the server
    bool done = false;
    while (!done)
    {
        // Initialize a request
        gcbv::SessionRequest request = new gcbv::SessionRequest
        {
            OpenSession = new gcbv::OpenSessionRequest(),
        };
        // Stream a request to the server
        await response.WriteAsync(request);
        // Set "done" to true when sending requests is complete
    }
    
    // Complete writing requests to the stream
    await response.WriteCompleteAsync();
    // Await the response handler
    // This will complete once all server responses have been processed
    await responseHandlerTask;
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize streaming call, retrieving the stream object
    using gcbv::BigtableServiceApiClient.OpenTableStream response = bigtableServiceApiClient.OpenTable();
    
    // Sending requests and retrieving responses can be arbitrarily interleaved
    // Exact sequence will depend on client/server behavior
    
    // Create task to do something with responses from server
    Task responseHandlerTask = Task.Run(async () =>
    {
        // Note that C# 8 code can use await foreach
        AsyncResponseStream<gcbv::SessionResponse> responseStream = response.GetResponseStream();
        while (await responseStream.MoveNextAsync())
        {
            gcbv::SessionResponse responseItem = responseStream.Current;
            // Do something with streamed response
        }
        // The response stream has completed
    });
    
    // Send requests to the server
    bool done = false;
    while (!done)
    {
        // Initialize a request
        gcbv::SessionRequest request = new gcbv::SessionRequest
        {
            OpenSession = new gcbv::OpenSessionRequest(),
        };
        // Stream a request to the server
        await response.WriteAsync(request);
        // Set "done" to true when sending requests is complete
    }
    
    // Complete writing requests to the stream
    await response.WriteCompleteAsync();
    // Await the response handler
    // This will complete once all server responses have been processed
    await responseHandlerTask;
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    // Make the request
    gcbv::PingAndWarmResponse response = bigtableServiceApiClient.PingAndWarm(name);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string appProfileId = "";
    // Make the request
    gcbv::PingAndWarmResponse response = bigtableServiceApiClient.PingAndWarm(name, appProfileId);
    

### PingAndWarm(PingAndWarmRequest, CallSettings)
    
    
    public virtual PingAndWarmResponse PingAndWarm(PingAndWarmRequest request, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::PingAndWarmRequest request = new gcbv::PingAndWarmRequest
    {
        InstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
    };
    // Make the request
    gcbv::PingAndWarmResponse response = bigtableServiceApiClient.PingAndWarm(request);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/instances/[INSTANCE]";
    // Make the request
    gcbv::PingAndWarmResponse response = bigtableServiceApiClient.PingAndWarm(name);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/instances/[INSTANCE]";
    string appProfileId = "";
    // Make the request
    gcbv::PingAndWarmResponse response = bigtableServiceApiClient.PingAndWarm(name, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(name);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string appProfileId = "";
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(name, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string appProfileId = "";
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(name, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName name = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(name);
    

### PingAndWarmAsync(PingAndWarmRequest, CallSettings)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(PingAndWarmRequest request, CallSettings callSettings = null)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::PingAndWarmRequest request = new gcbv::PingAndWarmRequest
    {
        InstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
    };
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(request);
    

### PingAndWarmAsync(PingAndWarmRequest, CancellationToken)
    
    
    public virtual Task<PingAndWarmResponse> PingAndWarmAsync(PingAndWarmRequest request, CancellationToken cancellationToken)

Warm up associated instance metadata for this connection. This call is not required but may be useful for connection keep-alive.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PingAndWarmRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PingAndWarmResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PingAndWarmResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::PingAndWarmRequest request = new gcbv::PingAndWarmRequest
    {
        InstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
    };
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(request);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/instances/[INSTANCE]";
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(name);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/instances/[INSTANCE]";
    string appProfileId = "";
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(name, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/instances/[INSTANCE]";
    string appProfileId = "";
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(name, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/instances/[INSTANCE]";
    // Make the request
    gcbv::PingAndWarmResponse response = await bigtableServiceApiClient.PingAndWarmAsync(name);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    InstanceName instanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string query = "";
    // Make the request
    gcbv::PrepareQueryResponse response = bigtableServiceApiClient.PrepareQuery(instanceName, query);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    InstanceName instanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string query = "";
    string appProfileId = "";
    // Make the request
    gcbv::PrepareQueryResponse response = bigtableServiceApiClient.PrepareQuery(instanceName, query, appProfileId);
    

### PrepareQuery(PrepareQueryRequest, CallSettings)
    
    
    public virtual PrepareQueryResponse PrepareQuery(PrepareQueryRequest request, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::PrepareQueryRequest request = new gcbv::PrepareQueryRequest
    {
        InstanceNameAsInstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
        Query = "",
        ProtoFormat = new gcbv::ProtoFormat(),
        ParamTypes =
        {
            {
                "",
                new gcbv::Type()
            },
        },
    };
    // Make the request
    gcbv::PrepareQueryResponse response = bigtableServiceApiClient.PrepareQuery(request);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string instanceName = "projects/[PROJECT]/instances/[INSTANCE]";
    string query = "";
    // Make the request
    gcbv::PrepareQueryResponse response = bigtableServiceApiClient.PrepareQuery(instanceName, query);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string instanceName = "projects/[PROJECT]/instances/[INSTANCE]";
    string query = "";
    string appProfileId = "";
    // Make the request
    gcbv::PrepareQueryResponse response = bigtableServiceApiClient.PrepareQuery(instanceName, query, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName instanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string query = "";
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(instanceName, query);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName instanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string query = "";
    string appProfileId = "";
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(instanceName, query, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName instanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string query = "";
    string appProfileId = "";
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(instanceName, query, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    InstanceName instanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]");
    string query = "";
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(instanceName, query);
    

### PrepareQueryAsync(PrepareQueryRequest, CallSettings)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(PrepareQueryRequest request, CallSettings callSettings = null)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::PrepareQueryRequest request = new gcbv::PrepareQueryRequest
    {
        InstanceNameAsInstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
        Query = "",
        ProtoFormat = new gcbv::ProtoFormat(),
        ParamTypes =
        {
            {
                "",
                new gcbv::Type()
            },
        },
    };
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(request);
    

### PrepareQueryAsync(PrepareQueryRequest, CancellationToken)
    
    
    public virtual Task<PrepareQueryResponse> PrepareQueryAsync(PrepareQueryRequest request, CancellationToken cancellationToken)

Prepares a GoogleSQL query for execution on a particular Bigtable instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PrepareQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[PrepareQueryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PrepareQueryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::PrepareQueryRequest request = new gcbv::PrepareQueryRequest
    {
        InstanceNameAsInstanceName = InstanceName.FromProjectInstance("[PROJECT]", "[INSTANCE]"),
        AppProfileId = "",
        Query = "",
        ProtoFormat = new gcbv::ProtoFormat(),
        ParamTypes =
        {
            {
                "",
                new gcbv::Type()
            },
        },
    };
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(request);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string instanceName = "projects/[PROJECT]/instances/[INSTANCE]";
    string query = "";
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(instanceName, query);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string instanceName = "projects/[PROJECT]/instances/[INSTANCE]";
    string query = "";
    string appProfileId = "";
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(instanceName, query, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string instanceName = "projects/[PROJECT]/instances/[INSTANCE]";
    string query = "";
    string appProfileId = "";
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(instanceName, query, appProfileId);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string instanceName = "projects/[PROJECT]/instances/[INSTANCE]";
    string query = "";
    // Make the request
    gcbv::PrepareQueryResponse response = await bigtableServiceApiClient.PrepareQueryAsync(instanceName, query);
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadChangeStreamStream response = bigtableServiceApiClient.ReadChangeStream(tableName);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadChangeStreamResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadChangeStreamResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadChangeStreamStream response = bigtableServiceApiClient.ReadChangeStream(tableName, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadChangeStreamResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadChangeStreamResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### ReadChangeStream(ReadChangeStreamRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadChangeStreamStream ReadChangeStream(ReadChangeStreamRequest request, CallSettings callSettings = null)

Reads changes from a table's change stream. Changes will reflect both user-initiated mutations and mutations that are caused by garbage collection. NOTE: This API is only intended to be used by Apache Beam BigtableIO.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadChangeStreamRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadChangeStreamStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadChangeStreamStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::ReadChangeStreamRequest request = new gcbv::ReadChangeStreamRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        AppProfileId = "",
        Partition = new gcbv::StreamPartition(),
        StartTime = new Timestamp(),
        EndTime = new Timestamp(),
        HeartbeatDuration = new Duration(),
    };
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadChangeStreamStream response = bigtableServiceApiClient.ReadChangeStream(request);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadChangeStreamResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadChangeStreamResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadChangeStreamStream response = bigtableServiceApiClient.ReadChangeStream(tableName);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadChangeStreamResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadChangeStreamResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadChangeStreamStream response = bigtableServiceApiClient.ReadChangeStream(tableName, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadChangeStreamResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadChangeStreamResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### ReadModifyWriteRow(TableName, ByteString, IEnumerable<ReadModifyWriteRule>, CallSettings)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(TableName tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = bigtableServiceApiClient.ReadModifyWriteRow(tableName, rowKey, rules);
    

### ReadModifyWriteRow(TableName, ByteString, IEnumerable<ReadModifyWriteRule>, string, CallSettings)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(TableName tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, string appProfileId, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = bigtableServiceApiClient.ReadModifyWriteRow(tableName, rowKey, rules, appProfileId);
    

### ReadModifyWriteRow(ReadModifyWriteRowRequest, CallSettings)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(ReadModifyWriteRowRequest request, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::ReadModifyWriteRowRequest request = new gcbv::ReadModifyWriteRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        Rules =
        {
            new gcbv::ReadModifyWriteRule(),
        },
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = bigtableServiceApiClient.ReadModifyWriteRow(request);
    

### ReadModifyWriteRow(string, ByteString, IEnumerable<ReadModifyWriteRule>, CallSettings)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(string tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = bigtableServiceApiClient.ReadModifyWriteRow(tableName, rowKey, rules);
    

### ReadModifyWriteRow(string, ByteString, IEnumerable<ReadModifyWriteRule>, string, CallSettings)
    
    
    public virtual ReadModifyWriteRowResponse ReadModifyWriteRow(string tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, string appProfileId, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = bigtableServiceApiClient.ReadModifyWriteRow(tableName, rowKey, rules, appProfileId);
    

### ReadModifyWriteRowAsync(TableName, ByteString, IEnumerable<ReadModifyWriteRule>, CallSettings)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(TableName tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(tableName, rowKey, rules);
    

### ReadModifyWriteRowAsync(TableName, ByteString, IEnumerable<ReadModifyWriteRule>, string, CallSettings)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(TableName tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, string appProfileId, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(tableName, rowKey, rules, appProfileId);
    

### ReadModifyWriteRowAsync(TableName, ByteString, IEnumerable<ReadModifyWriteRule>, string, CancellationToken)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(TableName tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, string appProfileId, CancellationToken cancellationToken)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(tableName, rowKey, rules, appProfileId);
    

### ReadModifyWriteRowAsync(TableName, ByteString, IEnumerable<ReadModifyWriteRule>, CancellationToken)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(TableName tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, CancellationToken cancellationToken)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(tableName, rowKey, rules);
    

### ReadModifyWriteRowAsync(ReadModifyWriteRowRequest, CallSettings)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(ReadModifyWriteRowRequest request, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::ReadModifyWriteRowRequest request = new gcbv::ReadModifyWriteRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        Rules =
        {
            new gcbv::ReadModifyWriteRule(),
        },
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(request);
    

### ReadModifyWriteRowAsync(ReadModifyWriteRowRequest, CancellationToken)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(ReadModifyWriteRowRequest request, CancellationToken cancellationToken)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    gcbv::ReadModifyWriteRowRequest request = new gcbv::ReadModifyWriteRowRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        RowKey = ByteString.Empty,
        Rules =
        {
            new gcbv::ReadModifyWriteRule(),
        },
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(request);
    

### ReadModifyWriteRowAsync(string, ByteString, IEnumerable<ReadModifyWriteRule>, CallSettings)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(string tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(tableName, rowKey, rules);
    

### ReadModifyWriteRowAsync(string, ByteString, IEnumerable<ReadModifyWriteRule>, string, CallSettings)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(string tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, string appProfileId, CallSettings callSettings = null)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(tableName, rowKey, rules, appProfileId);
    

### ReadModifyWriteRowAsync(string, ByteString, IEnumerable<ReadModifyWriteRule>, string, CancellationToken)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(string tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, string appProfileId, CancellationToken cancellationToken)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    string appProfileId = "";
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(tableName, rowKey, rules, appProfileId);
    

### ReadModifyWriteRowAsync(string, ByteString, IEnumerable<ReadModifyWriteRule>, CancellationToken)
    
    
    public virtual Task<ReadModifyWriteRowResponse> ReadModifyWriteRowAsync(string tableName, ByteString rowKey, IEnumerable<ReadModifyWriteRule> rules, CancellationToken cancellationToken)

Modifies a row atomically on the server. The method reads the latest existing timestamp and value from the specified columns and writes a new entry based on pre-defined read/modify/write rules. The new value for the timestamp is the greater of the existing timestamp or the current server time. The method returns the new contents of all modified cells.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table to which the read/modify/write rules should be applied. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`rowKey` | `[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)`  
Required. The key of the row to which the read/modify/write rules should be applied.  
`rules` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[ReadModifyWriteRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRule)`  
Required. Rules specifying how the specified row's contents are to be transformed into writes. Entries are applied in order, meaning that earlier rules will affect the results of later ones. At least one entry must be specified, and there can be at most 100000 rules.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ReadModifyWriteRowResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadModifyWriteRowResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = await gcbv::BigtableServiceApiClient.CreateAsync();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    ByteString rowKey = ByteString.Empty;
    IEnumerable<gcbv::ReadModifyWriteRule> rules = new gcbv::ReadModifyWriteRule[]
    {
        new gcbv::ReadModifyWriteRule(),
    };
    // Make the request
    gcbv::ReadModifyWriteRowResponse response = await bigtableServiceApiClient.ReadModifyWriteRowAsync(tableName, rowKey, rules);
    

### ReadRows(TableName, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadRowsStream ReadRows(TableName tableName, CallSettings callSettings = null)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each. Depending on their size, rows and cells may be broken up across multiple responses, but atomicity of each row will still be preserved. See the ReadRowsResponse documentation for details.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table from which to read. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadRowsStream response = bigtableServiceApiClient.ReadRows(tableName);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### ReadRows(TableName, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadRowsStream ReadRows(TableName tableName, string appProfileId, CallSettings callSettings = null)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each. Depending on their size, rows and cells may be broken up across multiple responses, but atomicity of each row will still be preserved. See the ReadRowsResponse documentation for details.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[TableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.TableName.html)`  
Optional. The unique name of the table from which to read. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadRowsStream response = bigtableServiceApiClient.ReadRows(tableName, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### ReadRows(ReadRowsRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadRowsStream ReadRows(ReadRowsRequest request, CallSettings callSettings = null)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each. Depending on their size, rows and cells may be broken up across multiple responses, but atomicity of each row will still be preserved. See the ReadRowsResponse documentation for details.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::ReadRowsRequest request = new gcbv::ReadRowsRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        Rows = new gcbv::RowSet(),
        Filter = new gcbv::RowFilter(),
        RowsLimit = 0L,
        AppProfileId = "",
        RequestStatsView = gcbv::ReadRowsRequest.Types.RequestStatsView.Unspecified,
        Reversed = false,
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
        MaterializedViewNameAsMaterializedViewName = gcbv::MaterializedViewName.FromProjectInstanceMaterializedView("[PROJECT]", "[INSTANCE]", "[MATERIALIZED_VIEW]"),
    };
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadRowsStream response = bigtableServiceApiClient.ReadRows(request);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### ReadRows(string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadRowsStream ReadRows(string tableName, CallSettings callSettings = null)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each. Depending on their size, rows and cells may be broken up across multiple responses, but atomicity of each row will still be preserved. See the ReadRowsResponse documentation for details.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table from which to read. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadRowsStream response = bigtableServiceApiClient.ReadRows(tableName);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### ReadRows(string, string, CallSettings)
    
    
    public virtual BigtableServiceApiClient.ReadRowsStream ReadRows(string tableName, string appProfileId, CallSettings callSettings = null)

Streams back the contents of all requested rows in key order, optionally applying the same Reader filter to each. Depending on their size, rows and cells may be broken up across multiple responses, but atomicity of each row will still be preserved. See the ReadRowsResponse documentation for details.

**Parameters**  
---  
**Name** | **Description**  
`tableName` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Optional. The unique name of the table from which to read. Values are of the form `projects/<project>/instances/<instance>/tables/<table>`.  
`appProfileId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
This value specifies routing for replication. If not specified, the "default" application profile will be used.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[ReadRowsStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.ReadRowsStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.ReadRowsStream response = bigtableServiceApiClient.ReadRows(tableName, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::ReadRowsResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::ReadRowsResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.SampleRowKeysStream response = bigtableServiceApiClient.SampleRowKeys(tableName);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::SampleRowKeysResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::SampleRowKeysResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    TableName tableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]");
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.SampleRowKeysStream response = bigtableServiceApiClient.SampleRowKeys(tableName, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::SampleRowKeysResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::SampleRowKeysResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### SampleRowKeys(SampleRowKeysRequest, CallSettings)
    
    
    public virtual BigtableServiceApiClient.SampleRowKeysStream SampleRowKeys(SampleRowKeysRequest request, CallSettings callSettings = null)

Returns a sample of row keys in the table. The returned row keys will delimit contiguous sections of the table of approximately equal size, which can be used to break up the data for distributed tasks like mapreduces.

If a `row_range` is provided in the request, the returned samples will be restricted to the specified range.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SampleRowKeysRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SampleRowKeysRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BigtableServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient)[SampleRowKeysStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient.SampleRowKeysStream)` | The server stream.  
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    gcbv::SampleRowKeysRequest request = new gcbv::SampleRowKeysRequest
    {
        TableNameAsTableName = TableName.FromProjectInstanceTable("[PROJECT]", "[INSTANCE]", "[TABLE]"),
        AppProfileId = "",
        AuthorizedViewNameAsAuthorizedViewName = gcbv::AuthorizedViewName.FromProjectInstanceTableAuthorizedView("[PROJECT]", "[INSTANCE]", "[TABLE]", "[AUTHORIZED_VIEW]"),
        MaterializedViewNameAsMaterializedViewName = gcbv::MaterializedViewName.FromProjectInstanceMaterializedView("[PROJECT]", "[INSTANCE]", "[MATERIALIZED_VIEW]"),
        RowRange = new gcbv::RowRange(),
    };
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.SampleRowKeysStream response = bigtableServiceApiClient.SampleRowKeys(request);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::SampleRowKeysResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::SampleRowKeysResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.SampleRowKeysStream response = bigtableServiceApiClient.SampleRowKeys(tableName);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::SampleRowKeysResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::SampleRowKeysResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

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
**Example**
    
    
    // Create client
    gcbv::BigtableServiceApiClient bigtableServiceApiClient = gcbv::BigtableServiceApiClient.Create();
    // Initialize request argument(s)
    string tableName = "projects/[PROJECT]/instances/[INSTANCE]/tables/[TABLE]";
    string appProfileId = "";
    // Make the request, returning a streaming response
    using gcbv::BigtableServiceApiClient.SampleRowKeysStream response = bigtableServiceApiClient.SampleRowKeys(tableName, appProfileId);
    
    // Read streaming responses from server until complete
    // Note that C# 8 code can use await foreach
    AsyncResponseStream<gcbv::SampleRowKeysResponse> responseStream = response.GetResponseStream();
    while (await responseStream.MoveNextAsync())
    {
        gcbv::SampleRowKeysResponse responseItem = responseStream.Current;
        // Do something with streamed response
    }
    // The response stream has completed
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient#Google_Cloud_Bigtable_V2_BigtableServiceApiClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient#Google_Cloud_Bigtable_V2_BigtableServiceApiClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient#Google_Cloud_Bigtable_V2_BigtableServiceApiClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableServiceApiClient#Google_Cloud_Bigtable_V2_BigtableServiceApiClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
