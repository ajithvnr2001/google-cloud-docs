---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse
title: Google Cloud Spanner v1 API - Class CommitResponse (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:53.317463+00:00
---

# Google Cloud Spanner v1 API - Class CommitResponse (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner v1 API - Class CommitResponse (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class CommitResponse : IMessage<CommitResponse>, IEquatable<CommitResponse>, IDeepCloneable<CommitResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner v1 API class CommitResponse.

The response for [Commit][google.spanner.v1.Spanner.Commit].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CommitResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CommitResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CommitResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CommitResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1)

## Assembly

Google.Cloud.Spanner.V1.dll

## Constructors 

### CommitResponse()
    
    
    public CommitResponse()

### CommitResponse(CommitResponse)
    
    
    public CommitResponse(CommitResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CommitResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse)`  
  
  
## Properties 

### CacheUpdate
    
    
    public CacheUpdate CacheUpdate { get; set; }

Optional. A cache update expresses a set of changes the client should incorporate into its location cache. The client should discard the changes if they are older than the data it already has. This data can be obtained in response to requests that included a `RoutingHint` field, but may also be obtained by explicit location-fetching RPCs which may be added in the future.

**Property Value**  
---  
**Type** | **Description**  
`[CacheUpdate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CacheUpdate)` |   
  
### CommitStats
    
    
    public CommitResponse.Types.CommitStats CommitStats { get; set; }

The statistics about this `Commit`. Not returned by default. For more information, see [CommitRequest.return_commit_stats][google.spanner.v1.CommitRequest.return_commit_stats].

**Property Value**  
---  
**Type** | **Description**  
`[CommitResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse.Types)[CommitStats](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse.Types.CommitStats)` |   
  
### CommitTimestamp
    
    
    public Timestamp CommitTimestamp { get; set; }

The Cloud Spanner timestamp at which the transaction committed.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### IsolationLevel
    
    
    public TransactionOptions.Types.IsolationLevel IsolationLevel { get; set; }

The isolation level used for the read-write transaction.

**Property Value**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions.Types)[IsolationLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions.Types.IsolationLevel)` |   
  
### MultiplexedSessionRetryCase
    
    
    public CommitResponse.MultiplexedSessionRetryOneofCase MultiplexedSessionRetryCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CommitResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse)[MultiplexedSessionRetryOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.CommitResponse.MultiplexedSessionRetryOneofCase)` |   
  
### PrecommitToken
    
    
    public MultiplexedSessionPrecommitToken PrecommitToken { get; set; }

If specified, transaction has not committed yet. You must retry the commit with the new precommit token.

**Property Value**  
---  
**Type** | **Description**  
`[MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.MultiplexedSessionPrecommitToken)` |   
  
### ReadLockMode
    
    
    public TransactionOptions.Types.ReadWrite.Types.ReadLockMode ReadLockMode { get; set; }

The read lock mode used for the read-write transaction.

**Property Value**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions.Types)[ReadWrite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions.Types.ReadWrite)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions.Types.ReadWrite.Types)[ReadLockMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionOptions.Types.ReadWrite.Types.ReadLockMode)` |   
  
### SnapshotTimestamp
    
    
    public Timestamp SnapshotTimestamp { get; set; }

If `TransactionOptions.isolation_level` is set to `IsolationLevel.REPEATABLE_READ`, then the snapshot timestamp is the timestamp at which all reads in the transaction ran. This timestamp is never returned.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
