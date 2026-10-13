---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus
title: Memorystore v1beta API - Class AclPolicyRevisionStatus (1.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:39.663649+00:00
---

# Memorystore v1beta API - Class AclPolicyRevisionStatus (1.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1beta API - Class AclPolicyRevisionStatus (1.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta07 (latest)  1.0.0-beta06 
    
    
    public sealed class AclPolicyRevisionStatus : IMessage<AclPolicyRevisionStatus>, IEquatable<AclPolicyRevisionStatus>, IDeepCloneable<AclPolicyRevisionStatus>, IBufferMessage, IMessage

Reference documentation and code samples for the Memorystore v1beta API class AclPolicyRevisionStatus.

AclPolicyRevisionStatus stores the per-revision status for an attached instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AclPolicyRevisionStatus

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AclPolicyRevisionStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AclPolicyRevisionStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AclPolicyRevisionStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta)

## Assembly

Google.Cloud.Memorystore.V1Beta.dll

## Constructors 

### AclPolicyRevisionStatus()
    
    
    public AclPolicyRevisionStatus()

### AclPolicyRevisionStatus(AclPolicyRevisionStatus)
    
    
    public AclPolicyRevisionStatus(AclPolicyRevisionStatus other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AclPolicyRevisionStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus)`  
  
  
## Properties 

### AclPolicyRevision
    
    
    public string AclPolicyRevision { get; set; }

Output only. The resource name of the ACL policy revision this status refers to. Format: "projects/{project}/locations/{location}/aclPolicies/{acl_policy}/revisions/{revision}"

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AclPolicyRevisionAsAclPolicyRevisionName
    
    
    public AclPolicyRevisionName AclPolicyRevisionAsAclPolicyRevisionName { get; set; }

[AclPolicyRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionName)-typed view over the [AclPolicyRevision](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus#Google_Cloud_Memorystore_V1Beta_AclPolicyRevisionStatus_AclPolicyRevision) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AclPolicyRevisionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionName)` |   
  
### AclPolicyRevisionNumber
    
    
    public long AclPolicyRevisionNumber { get; set; }

Output only. The revision number of the ACL policy revision this status refers to.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ErrorMessage
    
    
    public string ErrorMessage { get; set; }

Output only. Human-readable error message providing more details for FAILED states.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public AclPolicyRevisionStatus.Types.State State { get; set; }

Output only. AclPolicyRevision state.

**Property Value**  
---  
**Type** | **Description**  
`[AclPolicyRevisionStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.AclPolicyRevisionStatus.Types.State)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
