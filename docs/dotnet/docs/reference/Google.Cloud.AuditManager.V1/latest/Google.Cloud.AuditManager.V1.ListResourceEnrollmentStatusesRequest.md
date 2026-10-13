---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.ListResourceEnrollmentStatusesRequest
title: Audit Manager v1 API - Class ListResourceEnrollmentStatusesRequest (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:28.666778+00:00
---

# Audit Manager v1 API - Class ListResourceEnrollmentStatusesRequest (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.ListResourceEnrollmentStatusesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Audit Manager v1 API - Class ListResourceEnrollmentStatusesRequest (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ListResourceEnrollmentStatusesRequest : IMessage<ListResourceEnrollmentStatusesRequest>, IEquatable<ListResourceEnrollmentStatusesRequest>, IDeepCloneable<ListResourceEnrollmentStatusesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Audit Manager v1 API class ListResourceEnrollmentStatusesRequest.

Request message for [ListResourceEnrollmentStatuses][google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatuses].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListResourceEnrollmentStatusesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.ListResourceEnrollmentStatusesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.ListResourceEnrollmentStatusesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.ListResourceEnrollmentStatusesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AuditManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1)

## Assembly

Google.Cloud.AuditManager.V1.dll

## Constructors 

### ListResourceEnrollmentStatusesRequest()
    
    
    public ListResourceEnrollmentStatusesRequest()

### ListResourceEnrollmentStatusesRequest(ListResourceEnrollmentStatusesRequest)
    
    
    public ListResourceEnrollmentStatusesRequest(ListResourceEnrollmentStatusesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.ListResourceEnrollmentStatusesRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. Maximum number of items to return in a single page. The service might return fewer items than this value. If unspecified, the service picks an appropriate default. The maximum value is 100; values above 100 are reduced to 100.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous call, to retrieve the next page of results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Parent organization or folder to list enrollment statuses for, in one of the following formats:

  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsEnrollmentStatusScopeName
    
    
    public EnrollmentStatusScopeName ParentAsEnrollmentStatusScopeName { get; set; }

[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.ListResourceEnrollmentStatusesRequest#Google_Cloud_AuditManager_V1_ListResourceEnrollmentStatusesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[EnrollmentStatusScopeName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.EnrollmentStatusScopeName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
