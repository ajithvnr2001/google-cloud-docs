---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewRequest
title: Google Bigtable v2 API - Class AuthorizedViewRequest (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:37.534889+00:00
---

# Google Bigtable v2 API - Class AuthorizedViewRequest (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class AuthorizedViewRequest (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class AuthorizedViewRequest : IMessage<AuthorizedViewRequest>, IEquatable<AuthorizedViewRequest>, IDeepCloneable<AuthorizedViewRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class AuthorizedViewRequest.

A request wrapper for operations on an authorized view. Internal usage only.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AuthorizedViewRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AuthorizedViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AuthorizedViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AuthorizedViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### AuthorizedViewRequest()
    
    
    public AuthorizedViewRequest()

### AuthorizedViewRequest(AuthorizedViewRequest)
    
    
    public AuthorizedViewRequest(AuthorizedViewRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AuthorizedViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewRequest)`  
  
  
## Properties 

### CheckAndMutateRow
    
    
    public SessionCheckAndMutateRowRequest CheckAndMutateRow { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[SessionCheckAndMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionCheckAndMutateRowRequest)` |   
  
### MutateRow
    
    
    public SessionMutateRowRequest MutateRow { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[SessionMutateRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionMutateRowRequest)` |   
  
### MutateRows
    
    
    public SessionMutateRowsRequest MutateRows { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[SessionMutateRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionMutateRowsRequest)` |   
  
### PayloadCase
    
    
    public AuthorizedViewRequest.PayloadOneofCase PayloadCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[AuthorizedViewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewRequest)[PayloadOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.AuthorizedViewRequest.PayloadOneofCase)` |   
  
### ReadModifyWriteRow
    
    
    public SessionReadModifyWriteRowRequest ReadModifyWriteRow { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[SessionReadModifyWriteRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionReadModifyWriteRowRequest)` |   
  
### ReadRow
    
    
    public SessionReadRowRequest ReadRow { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[SessionReadRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionReadRowRequest)` |   
  
### ReadRows
    
    
    public SessionReadRowsRequest ReadRows { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[SessionReadRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.SessionReadRowsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
