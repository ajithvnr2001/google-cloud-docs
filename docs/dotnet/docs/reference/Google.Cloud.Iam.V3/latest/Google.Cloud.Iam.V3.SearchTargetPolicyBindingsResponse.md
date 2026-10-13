---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.SearchTargetPolicyBindingsResponse
title: Identity and Access Management (IAM) v3 API - Class SearchTargetPolicyBindingsResponse (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:18.609153+00:00
---

# Identity and Access Management (IAM) v3 API - Class SearchTargetPolicyBindingsResponse (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.SearchTargetPolicyBindingsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3 API - Class SearchTargetPolicyBindingsResponse (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class SearchTargetPolicyBindingsResponse : IPageResponse<PolicyBinding>, IEnumerable<PolicyBinding>, IEnumerable, IMessage<SearchTargetPolicyBindingsResponse>, IEquatable<SearchTargetPolicyBindingsResponse>, IDeepCloneable<SearchTargetPolicyBindingsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v3 API class SearchTargetPolicyBindingsResponse.

Response message for SearchTargetPolicyBindings method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchTargetPolicyBindingsResponse

## Implements

[IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PolicyBinding), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PolicyBinding), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.SearchTargetPolicyBindingsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.SearchTargetPolicyBindingsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.SearchTargetPolicyBindingsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3)

## Assembly

Google.Cloud.Iam.V3.dll

## Constructors 

### SearchTargetPolicyBindingsResponse()
    
    
    public SearchTargetPolicyBindingsResponse()

### SearchTargetPolicyBindingsResponse(SearchTargetPolicyBindingsResponse)
    
    
    public SearchTargetPolicyBindingsResponse(SearchTargetPolicyBindingsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.SearchTargetPolicyBindingsResponse)`  
  
  
## Properties 

### NextPageToken
    
    
    public string NextPageToken { get; set; }

Optional. A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PolicyBindings
    
    
    public RepeatedField<PolicyBinding> PolicyBindings { get; }

The policy bindings bound to the specified target.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PolicyBinding)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<PolicyBinding> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[PolicyBinding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3/latest/Google.Cloud.Iam.V3.PolicyBinding)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-08 UTC."],[],[]] 
