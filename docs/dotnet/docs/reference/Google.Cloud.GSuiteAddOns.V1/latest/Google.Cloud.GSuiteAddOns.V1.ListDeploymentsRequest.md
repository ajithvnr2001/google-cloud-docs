---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest
title: Google Workspace Add-ons v1 API - Class ListDeploymentsRequest (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:51.780189+00:00
---

# Google Workspace Add-ons v1 API - Class ListDeploymentsRequest (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Workspace Add-ons v1 API - Class ListDeploymentsRequest (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/2.4.0/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/2.3.0/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/2.2.0/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/2.1.0/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/2.0.0/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/1.1.0/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/1.0.0/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)


    
    
    public sealed class ListDeploymentsRequest : IMessage<ListDeploymentsRequest>, IEquatable<ListDeploymentsRequest>, IDeepCloneable<ListDeploymentsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Google Workspace Add-ons v1 API class ListDeploymentsRequest.

Request message to list deployments for a project.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListDeploymentsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GSuiteAddOns.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1)

## Assembly

Google.Cloud.GSuiteAddOns.V1.dll

## Constructors 

### ListDeploymentsRequest()
    
    
    public ListDeploymentsRequest()

### ListDeploymentsRequest(ListDeploymentsRequest)
    
    
    public ListDeploymentsRequest(ListDeploymentsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListDeploymentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

The maximum number of deployments to return. The service may return fewer than this value. If unspecified, at most 1000 deployments will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

A page token, received from a previous `ListDeployments` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListDeployments` must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Name of the project in which to create the deployment.

Example: `projects/my_project`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GSuiteAddOns.V1/latest/Google.Cloud.GSuiteAddOns.V1.ListDeploymentsRequest#Google_Cloud_GSuiteAddOns_V1_ListDeploymentsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
