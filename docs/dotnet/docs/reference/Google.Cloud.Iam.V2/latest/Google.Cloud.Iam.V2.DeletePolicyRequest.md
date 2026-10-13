---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest/Google.Cloud.Iam.V2.DeletePolicyRequest
title: Google Cloud Identity and Access Management (IAM) v2 API - Class DeletePolicyRequest (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:41.440992+00:00
---

# Google Cloud Identity and Access Management (IAM) v2 API - Class DeletePolicyRequest (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest/Google.Cloud.Iam.V2.DeletePolicyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Identity and Access Management (IAM) v2 API - Class DeletePolicyRequest (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest/Google.Cloud.Iam.V2.DeletePolicyRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/1.3.0/Google.Cloud.Iam.V2.DeletePolicyRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/1.2.0/Google.Cloud.Iam.V2.DeletePolicyRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/1.1.0/Google.Cloud.Iam.V2.DeletePolicyRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/1.0.0/Google.Cloud.Iam.V2.DeletePolicyRequest)


    
    
    public sealed class DeletePolicyRequest : IMessage<DeletePolicyRequest>, IEquatable<DeletePolicyRequest>, IDeepCloneable<DeletePolicyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Identity and Access Management (IAM) v2 API class DeletePolicyRequest.

Request message for `DeletePolicy`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeletePolicyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeletePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest/Google.Cloud.Iam.V2.DeletePolicyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeletePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest/Google.Cloud.Iam.V2.DeletePolicyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeletePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest/Google.Cloud.Iam.V2.DeletePolicyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest/Google.Cloud.Iam.V2)

## Assembly

Google.Cloud.Iam.V2.dll

## Constructors 

### DeletePolicyRequest()
    
    
    public DeletePolicyRequest()

### DeletePolicyRequest(DeletePolicyRequest)
    
    
    public DeletePolicyRequest(DeletePolicyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeletePolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V2/latest/Google.Cloud.Iam.V2.DeletePolicyRequest)`  
  
  
## Properties 

### Etag
    
    
    public string Etag { get; set; }

Optional. The expected `etag` of the policy to delete. If the value does not match the value that is stored in IAM, the request fails with a `409` error code and `ABORTED` status.

If you omit this field, the policy is deleted regardless of its current `etag`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the policy to delete. Format: `policies/{attachment_point}/denypolicies/{policy_id}`

Use the URL-encoded full resource name, which means that the forward-slash character, `/`, must be written as `%2F`. For example, `policies/cloudresourcemanager.googleapis.com%2Fprojects%2Fmy-project/denypolicies/my-policy`.

For organizations and folders, use the numeric ID in the full resource name. For projects, you can use the alphanumeric or the numeric ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
