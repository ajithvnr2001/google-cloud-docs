---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetAccessPolicyRequest
title: Identity and Access Management (IAM) v3 API - Class GetAccessPolicyRequest (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:49.149927+00:00
---

# Identity and Access Management (IAM) v3 API - Class GetAccessPolicyRequest (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetAccessPolicyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3 API - Class GetAccessPolicyRequest (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class GetAccessPolicyRequest : IMessage<GetAccessPolicyRequest>, IEquatable<GetAccessPolicyRequest>, IDeepCloneable<GetAccessPolicyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v3 API class GetAccessPolicyRequest.

Request message for GetAccessPolicy method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetAccessPolicyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetAccessPolicyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetAccessPolicyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetAccessPolicyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3)

## Assembly

Google.Cloud.Iam.V3.dll

## Constructors 

### GetAccessPolicyRequest()
    
    
    public GetAccessPolicyRequest()

### GetAccessPolicyRequest(GetAccessPolicyRequest)
    
    
    public GetAccessPolicyRequest(GetAccessPolicyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetAccessPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetAccessPolicyRequest)`  
  
  
## Properties 

### AccessPolicyName
    
    
    public AccessPolicyName AccessPolicyName { get; set; }

[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.AccessPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.GetAccessPolicyRequest#Google_Cloud_Iam_V3_GetAccessPolicyRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.AccessPolicyName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the access policy to retrieve.

Format: `projects/{project_id}/locations/{location}/accessPolicies/{access_policy_id}` `projects/{project_number}/locations/{location}/accessPolicies/{access_policy_id}` `folders/{folder_id}/locations/{location}/accessPolicies/{access_policy_id}` `organizations/{organization_id}/locations/{location}/accessPolicies/{access_policy_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-08 UTC."],[],[]] 
