---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest
title: Policy Simulator v1 API - Class CreateOrgPolicyViolationsPreviewRequest (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:56.038754+00:00
---

# Policy Simulator v1 API - Class CreateOrgPolicyViolationsPreviewRequest (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Policy Simulator v1 API - Class CreateOrgPolicyViolationsPreviewRequest (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.3.0/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.2.0/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.1.0/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.0.0/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest)


    
    
    public sealed class CreateOrgPolicyViolationsPreviewRequest : IMessage<CreateOrgPolicyViolationsPreviewRequest>, IEquatable<CreateOrgPolicyViolationsPreviewRequest>, IDeepCloneable<CreateOrgPolicyViolationsPreviewRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Policy Simulator v1 API class CreateOrgPolicyViolationsPreviewRequest.

CreateOrgPolicyViolationsPreviewRequest is the request message for [OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewService.CreateOrgPolicyViolationsPreview].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateOrgPolicyViolationsPreviewRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PolicySimulator.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1)

## Assembly

Google.Cloud.PolicySimulator.V1.dll

## Constructors 

### CreateOrgPolicyViolationsPreviewRequest()
    
    
    public CreateOrgPolicyViolationsPreviewRequest()

### CreateOrgPolicyViolationsPreviewRequest(CreateOrgPolicyViolationsPreviewRequest)
    
    
    public CreateOrgPolicyViolationsPreviewRequest(CreateOrgPolicyViolationsPreviewRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest)`  
  
  
## Properties 

### OrgPolicyViolationsPreview
    
    
    public OrgPolicyViolationsPreview OrgPolicyViolationsPreview { get; set; }

Required. The [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview] to generate.

**Property Value**  
---  
**Type** | **Description**  
`[OrgPolicyViolationsPreview](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.OrgPolicyViolationsPreview)` |   
  
### OrgPolicyViolationsPreviewId
    
    
    public string OrgPolicyViolationsPreviewId { get; set; }

Optional. An optional user-specified ID for the [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview]. If not provided, a random ID will be generated.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The organization under which this [OrgPolicyViolationsPreview][google.cloud.policysimulator.v1.OrgPolicyViolationsPreview] will be created.

Example: `organizations/my-example-org/locations/global`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsOrganizationLocationName
    
    
    public OrganizationLocationName ParentAsOrganizationLocationName { get; set; }

[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.OrganizationLocationName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateOrgPolicyViolationsPreviewRequest#Google_Cloud_PolicySimulator_V1_CreateOrgPolicyViolationsPreviewRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[OrganizationLocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.OrganizationLocationName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
