---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchAccessPolicyBindingsRequest
title: Identity and Access Management (IAM) v3beta API - Class SearchAccessPolicyBindingsRequest (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:37.082714+00:00
---

# Identity and Access Management (IAM) v3beta API - Class SearchAccessPolicyBindingsRequest (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchAccessPolicyBindingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3beta API - Class SearchAccessPolicyBindingsRequest (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class SearchAccessPolicyBindingsRequest : IPageRequest, IMessage<SearchAccessPolicyBindingsRequest>, IEquatable<SearchAccessPolicyBindingsRequest>, IDeepCloneable<SearchAccessPolicyBindingsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v3beta API class SearchAccessPolicyBindingsRequest.

Request message for SearchAccessPolicyBindings rpc.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchAccessPolicyBindingsRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchAccessPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchAccessPolicyBindingsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchAccessPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchAccessPolicyBindingsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchAccessPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchAccessPolicyBindingsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta)

## Assembly

Google.Cloud.Iam.V3Beta.dll

## Constructors 

### SearchAccessPolicyBindingsRequest()
    
    
    public SearchAccessPolicyBindingsRequest()

### SearchAccessPolicyBindingsRequest(SearchAccessPolicyBindingsRequest)
    
    
    public SearchAccessPolicyBindingsRequest(SearchAccessPolicyBindingsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchAccessPolicyBindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchAccessPolicyBindingsRequest)`  
  
  
## Properties 

### AccessPolicyName
    
    
    public AccessPolicyName AccessPolicyName { get; set; }

[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.SearchAccessPolicyBindingsRequest#Google_Cloud_Iam_V3Beta_SearchAccessPolicyBindingsRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the access policy. Format: `organizations/{organization_id}/locations/{location}/accessPolicies/{access_policy_id}` `folders/{folder_id}/locations/{location}/accessPolicies/{access_policy_id}` `projects/{project_id}/locations/{location}/accessPolicies/{access_policy_id}` `projects/{project_number}/locations/{location}/accessPolicies/{access_policy_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of policy bindings to return. The service may return fewer than this value.

If unspecified, at most 50 policy bindings will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous `SearchAccessPolicyBindingsRequest` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `SearchAccessPolicyBindingsRequest` must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
