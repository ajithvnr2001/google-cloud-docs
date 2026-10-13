---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest
title: Google Cloud Spanner v1 API - Class ExecuteBatchDmlRequest (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:45.054773+00:00
---

# Google Cloud Spanner v1 API - Class ExecuteBatchDmlRequest (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner v1 API - Class ExecuteBatchDmlRequest (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class ExecuteBatchDmlRequest : IMessage<ExecuteBatchDmlRequest>, IEquatable<ExecuteBatchDmlRequest>, IDeepCloneable<ExecuteBatchDmlRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner v1 API class ExecuteBatchDmlRequest.

The request for [ExecuteBatchDml][google.spanner.v1.Spanner.ExecuteBatchDml].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExecuteBatchDmlRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ExecuteBatchDmlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExecuteBatchDmlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ExecuteBatchDmlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1)

## Assembly

Google.Cloud.Spanner.V1.dll

## Constructors 

### ExecuteBatchDmlRequest()
    
    
    public ExecuteBatchDmlRequest()

### ExecuteBatchDmlRequest(ExecuteBatchDmlRequest)
    
    
    public ExecuteBatchDmlRequest(ExecuteBatchDmlRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ExecuteBatchDmlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest)`  
  
  
## Properties 

### LastStatements
    
    
    public bool LastStatements { get; set; }

Optional. If set to `true`, this request marks the end of the transaction. After these statements execute, you must commit or abort the transaction. Attempts to execute any other requests against this transaction (including reads and queries) are rejected.

Setting this option might cause some error reporting to be deferred until commit time (for example, validation of unique constraints). Given this, successful execution of statements shouldn't be assumed until a subsequent `Commit` call completes successfully.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RequestOptions
    
    
    public RequestOptions RequestOptions { get; set; }

Common options for this request.

**Property Value**  
---  
**Type** | **Description**  
`[RequestOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.RequestOptions)` |   
  
### Seqno
    
    
    public long Seqno { get; set; }

Required. A per-transaction sequence number used to identify this request. This field makes each request idempotent such that if the request is received multiple times, at most one succeeds.

The sequence number must be monotonically increasing within the transaction. If a request arrives for the first time with an out-of-order sequence number, the transaction might be aborted. Replays of previously handled requests yield the same response as the first execution.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Session
    
    
    public string Session { get; set; }

Required. The session in which the DML statements should be performed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SessionAsSessionName
    
    
    public SessionName SessionAsSessionName { get; set; }

[SessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionName)-typed view over the [Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest#Google_Cloud_Spanner_V1_ExecuteBatchDmlRequest_Session) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.SessionName)` |   
  
### Statements
    
    
    public RepeatedField<ExecuteBatchDmlRequest.Types.Statement> Statements { get; }

Required. The list of statements to execute in this batch. Statements are executed serially, such that the effects of statement `i` are visible to statement `i+1`. Each statement must be a DML statement. Execution stops at the first failed statement; the remaining statements are not executed.

Callers must provide at least one statement.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ExecuteBatchDmlRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest.Types)[Statement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ExecuteBatchDmlRequest.Types.Statement)` |   
  
### Transaction
    
    
    public TransactionSelector Transaction { get; set; }

Required. The transaction to use. Must be a read-write transaction.

To protect against replays, single-use transactions are not supported. The caller must either supply an existing transaction ID or begin a new transaction.

**Property Value**  
---  
**Type** | **Description**  
`[TransactionSelector](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.TransactionSelector)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
