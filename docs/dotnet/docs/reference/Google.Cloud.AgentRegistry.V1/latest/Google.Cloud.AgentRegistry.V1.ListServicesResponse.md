---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse
title: Agent Registry v1 API - Class ListServicesResponse (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:56.114259+00:00
---

# Agent Registry v1 API - Class ListServicesResponse (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Agent Registry v1 API - Class ListServicesResponse (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class ListServicesResponse : IPageResponse<Service>, IEnumerable<Service>, IEnumerable, IMessage<ListServicesResponse>, IEquatable<ListServicesResponse>, IDeepCloneable<ListServicesResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Agent Registry v1 API class ListServicesResponse.

Message for response to listing Services

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListServicesResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Service), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Service), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AgentRegistry.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1)

## Assembly

Google.Cloud.AgentRegistry.V1.dll

## Constructors 

### ListServicesResponse()
    
    
    public ListServicesResponse()

### ListServicesResponse(ListServicesResponse)
    
    
    public ListServicesResponse(ListServicesResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListServicesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.ListServicesResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token identifying a page of results the server should return. Used in [page_token][google.cloud.agentregistry.v1main.ListServicesRequest.page_token].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Services
    
    
    public RepeatedField<Service> Services { get; }

The list of Service resources matching the parent and filter criteria in the request. Each Service resource follows the format: `projects/{project}/locations/{location}/services/{service}`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Service)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Service> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Service)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
