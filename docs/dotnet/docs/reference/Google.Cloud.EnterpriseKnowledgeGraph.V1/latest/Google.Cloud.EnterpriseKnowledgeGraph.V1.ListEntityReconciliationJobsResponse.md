---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.ListEntityReconciliationJobsResponse
title: Enterprise Knowledge Graph v1 API - Class ListEntityReconciliationJobsResponse (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:24.699817+00:00
---

# Enterprise Knowledge Graph v1 API - Class ListEntityReconciliationJobsResponse (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.ListEntityReconciliationJobsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Enterprise Knowledge Graph v1 API - Class ListEntityReconciliationJobsResponse (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.ListEntityReconciliationJobsResponse)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/1.0.0-beta04/Google.Cloud.EnterpriseKnowledgeGraph.V1.ListEntityReconciliationJobsResponse)


    
    
    public sealed class ListEntityReconciliationJobsResponse : IPageResponse<EntityReconciliationJob>, IEnumerable<EntityReconciliationJob>, IEnumerable, IMessage<ListEntityReconciliationJobsResponse>, IEquatable<ListEntityReconciliationJobsResponse>, IDeepCloneable<ListEntityReconciliationJobsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Enterprise Knowledge Graph v1 API class ListEntityReconciliationJobsResponse.

Response message for [EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs][google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListEntityReconciliationJobsResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[EntityReconciliationJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.EntityReconciliationJob), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[EntityReconciliationJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.EntityReconciliationJob), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListEntityReconciliationJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.ListEntityReconciliationJobsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListEntityReconciliationJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.ListEntityReconciliationJobsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListEntityReconciliationJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.ListEntityReconciliationJobsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.EnterpriseKnowledgeGraph.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1)

## Assembly

Google.Cloud.EnterpriseKnowledgeGraph.V1.dll

## Constructors 

### ListEntityReconciliationJobsResponse()
    
    
    public ListEntityReconciliationJobsResponse()

### ListEntityReconciliationJobsResponse(ListEntityReconciliationJobsResponse)
    
    
    public ListEntityReconciliationJobsResponse(ListEntityReconciliationJobsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListEntityReconciliationJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.ListEntityReconciliationJobsResponse)`  
  
  
## Properties 

### EntityReconciliationJobs
    
    
    public RepeatedField<EntityReconciliationJob> EntityReconciliationJobs { get; }

A list of EntityReconciliationJobs that matches the specified filter in the request.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EntityReconciliationJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.EntityReconciliationJob)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

The standard List next-page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<EntityReconciliationJob> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[EntityReconciliationJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EnterpriseKnowledgeGraph.V1/latest/Google.Cloud.EnterpriseKnowledgeGraph.V1.EntityReconciliationJob)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
