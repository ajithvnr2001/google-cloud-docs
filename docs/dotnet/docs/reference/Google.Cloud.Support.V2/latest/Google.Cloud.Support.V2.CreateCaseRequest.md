---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest
title: Google Cloud Support v2 API - Class CreateCaseRequest (1.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:37.717847+00:00
---

# Google Cloud Support v2 API - Class CreateCaseRequest (1.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Support v2 API - Class CreateCaseRequest (1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class CreateCaseRequest : IMessage<CreateCaseRequest>, IEquatable<CreateCaseRequest>, IDeepCloneable<CreateCaseRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Support v2 API class CreateCaseRequest.

The request message for the CreateCase endpoint.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateCaseRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Support.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2)

## Assembly

Google.Cloud.Support.V2.dll

## Constructors 

### CreateCaseRequest()
    
    
    public CreateCaseRequest()

### CreateCaseRequest(CreateCaseRequest)
    
    
    public CreateCaseRequest(CreateCaseRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateCaseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest)`  
  
  
## Properties 

### Case
    
    
    public Case Case { get; set; }

Required. The case to be created.

**Property Value**  
---  
**Type** | **Description**  
`[Case](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.Case)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The name of the parent under which the case should be created.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsOrganizationName
    
    
    public OrganizationName ParentAsOrganizationName { get; set; }

[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest#Google_Cloud_Support_V2_CreateCaseRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.OrganizationName.html)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest#Google_Cloud_Support_V2_CreateCaseRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
### ParentAsResourceName
    
    
    public IResourceName ParentAsResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2/latest/Google.Cloud.Support.V2.CreateCaseRequest#Google_Cloud_Support_V2_CreateCaseRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
