---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAclPolicyRequest
title: Memorystore v1beta API - Class DeleteAclPolicyRequest (1.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:28:47.076424+00:00
---

# Memorystore v1beta API - Class DeleteAclPolicyRequest (1.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAclPolicyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1beta API - Class DeleteAclPolicyRequest (1.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta07 (latest)  1.0.0-beta06 
    
    
    public sealed class DeleteAclPolicyRequest : IMessage<DeleteAclPolicyRequest>, IEquatable<DeleteAclPolicyRequest>, IDeepCloneable<DeleteAclPolicyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Memorystore v1beta API class DeleteAclPolicyRequest.

Request for `DeleteAclPolicy`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteAclPolicyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAclPolicyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAclPolicyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAclPolicyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta)

## Assembly

Google.Cloud.Memorystore.V1Beta.dll

## Constructors 

### DeleteAclPolicyRequest()
    
    
    public DeleteAclPolicyRequest()

### DeleteAclPolicyRequest(DeleteAclPolicyRequest)
    
    
    public DeleteAclPolicyRequest(DeleteAclPolicyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteAclPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAclPolicyRequest)`  
  
  
## Properties 

### AclPolicyName
    
    
    public AclPolicyName AclPolicyName { get; set; }

[AclPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.DeleteAclPolicyRequest#Google_Cloud_Memorystore_V1Beta_DeleteAclPolicyRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AclPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyName)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. Etag of the ACL policy. If this is different from the server's etag, the request will fail with an ABORTED error.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Memorystore ACL policy resource name using the form: `projects/{project}/locations/{location}/aclPolicies/{acl_policy_id}` where `location` refers to a Google Cloud region.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. Idempotent request UUID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
