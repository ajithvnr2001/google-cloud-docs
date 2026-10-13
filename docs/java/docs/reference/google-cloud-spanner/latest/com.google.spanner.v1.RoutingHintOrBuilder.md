---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.RoutingHintOrBuilder
title: Interface RoutingHintOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:30.194233+00:00
---

# Interface RoutingHintOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.RoutingHintOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RoutingHintOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface RoutingHintOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getClientLocation()
    
    
    public abstract String getClientLocation()

If present, the client's current location. This should be the name of a Google Cloud zone or region, such as "us-central1".

If absent, the client's location will be assumed to be the same as the location of the server the client ends up connected to.

Locations are primarily valuable for clients that connect from regions other than the ones that contain the Spanner database.

`string client_location = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clientLocation.  
  
### getClientLocationBytes()
    
    
    public abstract ByteString getClientLocationBytes()

If present, the client's current location. This should be the name of a Google Cloud zone or region, such as "us-central1".

If absent, the client's location will be assumed to be the same as the location of the server the client ends up connected to.

Locations are primarily valuable for clients that connect from regions other than the ones that contain the Spanner database.

`string client_location = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clientLocation.  
  
### getDatabaseId()
    
    
    public abstract long getDatabaseId()

The database ID of the database being accessed, see `CacheUpdate.database_id`. Should match the cache entries that were used to generate the rest of the fields in this `RoutingHint`.

`uint64 database_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The databaseId.  
  
### getGroupUid()
    
    
    public abstract long getGroupUid()

The group UID of the group that the client believes serves the range defined by `key` and `limit_key`. See `Range.group_uid` for more details.

`uint64 group_uid = 6;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The groupUid.  
  
### getKey()
    
    
    public abstract ByteString getKey()

The key / key range that this request accesses. For operations that access a single key, `key` should be set and `limit_key` should be empty. For operations that access a key range, `key` and `limit_key` should both be set, to the inclusive start and exclusive end of the range respectively.

The keys are encoded in "sortable string format" (ssformat), using a `KeyRecipe` that is appropriate for the request. See `KeyRecipe` for more details.

`bytes key = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The key.  
  
### getLimitKey()
    
    
    public abstract ByteString getLimitKey()

If this request targets a key range, this is the exclusive end of the range. See `key` for more details.

`bytes limit_key = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The limitKey.  
  
### getOperationUid()
    
    
    public abstract long getOperationUid()

A session-scoped unique ID for the operation, computed client-side. Requests with the same `operation_uid` should have a shared 'shape', meaning that some fields are expected to be the same, such as the SQL query, the target table/columns (for reads) etc. Requests with the same `operation_uid` are meant to differ only in fields like keys/key ranges/query parameters, transaction IDs, etc.

`operation_uid` must be non-zero for `RoutingHint` to be valid.

`uint64 operation_uid = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The operationUid.  
  
### getSchemaGeneration()
    
    
    public abstract ByteString getSchemaGeneration()

The schema generation of the recipe that was used to generate `key` and `limit_key`. See also `RecipeList.schema_generation`.

`bytes schema_generation = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The schemaGeneration.  
  
### getSkippedTabletUid(int index)
    
    
    public abstract RoutingHint.SkippedTablet getSkippedTabletUid(int index)

If the client had multiple options for tablet selection, and some of its first choices were unhealthy (e.g., the server is unreachable, or `Tablet.skip` is true), this field will contain the tablet UIDs of those tablets, with their incarnations. The server may include a `CacheUpdate` with new locations for those tablets.

`repeated .google.spanner.v1.RoutingHint.SkippedTablet skipped_tablet_uid = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RoutingHint.SkippedTablet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.RoutingHint.SkippedTablet)` |   
  
### getSkippedTabletUidCount()
    
    
    public abstract int getSkippedTabletUidCount()

If the client had multiple options for tablet selection, and some of its first choices were unhealthy (e.g., the server is unreachable, or `Tablet.skip` is true), this field will contain the tablet UIDs of those tablets, with their incarnations. The server may include a `CacheUpdate` with new locations for those tablets.

`repeated .google.spanner.v1.RoutingHint.SkippedTablet skipped_tablet_uid = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSkippedTabletUidList()
    
    
    public abstract List<RoutingHint.SkippedTablet> getSkippedTabletUidList()

If the client had multiple options for tablet selection, and some of its first choices were unhealthy (e.g., the server is unreachable, or `Tablet.skip` is true), this field will contain the tablet UIDs of those tablets, with their incarnations. The server may include a `CacheUpdate` with new locations for those tablets.

`repeated .google.spanner.v1.RoutingHint.SkippedTablet skipped_tablet_uid = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SkippedTablet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.RoutingHint.SkippedTablet)>` |   
  
### getSkippedTabletUidOrBuilder(int index)
    
    
    public abstract RoutingHint.SkippedTabletOrBuilder getSkippedTabletUidOrBuilder(int index)

If the client had multiple options for tablet selection, and some of its first choices were unhealthy (e.g., the server is unreachable, or `Tablet.skip` is true), this field will contain the tablet UIDs of those tablets, with their incarnations. The server may include a `CacheUpdate` with new locations for those tablets.

`repeated .google.spanner.v1.RoutingHint.SkippedTablet skipped_tablet_uid = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RoutingHint.SkippedTabletOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.RoutingHint.SkippedTabletOrBuilder)` |   
  
### getSkippedTabletUidOrBuilderList()
    
    
    public abstract List<? extends RoutingHint.SkippedTabletOrBuilder> getSkippedTabletUidOrBuilderList()

If the client had multiple options for tablet selection, and some of its first choices were unhealthy (e.g., the server is unreachable, or `Tablet.skip` is true), this field will contain the tablet UIDs of those tablets, with their incarnations. The server may include a `CacheUpdate` with new locations for those tablets.

`repeated .google.spanner.v1.RoutingHint.SkippedTablet skipped_tablet_uid = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.spanner.v1.RoutingHint.SkippedTabletOrBuilder>` |   
  
### getSplitId()
    
    
    public abstract long getSplitId()

The split ID of the split that the client believes contains the range defined by `key` and `limit_key`. See `Range.split_id` for more details.

`uint64 split_id = 7;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The splitId.  
  
### getTabletUid()
    
    
    public abstract long getTabletUid()

The tablet UID of the tablet from group `group_uid` that the client believes is best to serve this request. See `Group.local_tablet_uids` and `Group.leader_tablet_uid`.

`uint64 tablet_uid = 8;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The tabletUid.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
