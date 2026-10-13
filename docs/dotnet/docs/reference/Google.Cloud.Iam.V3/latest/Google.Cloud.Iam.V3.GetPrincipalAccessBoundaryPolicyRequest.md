---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetPrincipalAccessBoundaryPolicyRequest
title: Identity and Access Management (IAM) v3 API - Class GetPrincipalAccessBoundaryPolicyRequest (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:12.307628+00:00
---

# Identity and Access Management (IAM) v3 API - Class GetPrincipalAccessBoundaryPolicyRequest (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetPrincipalAccessBoundaryPolicyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3 API - Class GetPrincipalAccessBoundaryPolicyRequest (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class GetPrincipalAccessBoundaryPolicyRequest : IMessage<GetPrincipalAccessBoundaryPolicyRequest>, IEquatable<GetPrincipalAccessBoundaryPolicyRequest>, IDeepCloneable<GetPrincipalAccessBoundaryPolicyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v3 API class GetPrincipalAccessBoundaryPolicyRequest.

Request message for GetPrincipalAccessBoundaryPolicy method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetPrincipalAccessBoundaryPolicyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetPrincipalAccessBoundaryPolicyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetPrincipalAccessBoundaryPolicyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetPrincipalAccessBoundaryPolicyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3)

## Assembly

Google.Cloud.Iam.V3.dll

## Constructors 

### GetPrincipalAccessBoundaryPolicyRequest()
    
    
    public GetPrincipalAccessBoundaryPolicyRequest()

### GetPrincipalAccessBoundaryPolicyRequest(GetPrincipalAccessBoundaryPolicyRequest)
    
    
    public GetPrincipalAccessBoundaryPolicyRequest(GetPrincipalAccessBoundaryPolicyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetPrincipalAccessBoundaryPolicyRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The name of the principal access boundary policy to retrieve.

Format: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{principal_access_boundary_policy_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrincipalAccessBoundaryPolicyName
    
    
    public PrincipalAccessBoundaryPolicyName PrincipalAccessBoundaryPolicyName { get; set; }

[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PrincipalAccessBoundaryPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetPrincipalAccessBoundaryPolicyRequest#Google_Cloud_Iam_V3_GetPrincipalAccessBoundaryPolicyRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PrincipalAccessBoundaryPolicyName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-08 UTC."],[],[]] 
