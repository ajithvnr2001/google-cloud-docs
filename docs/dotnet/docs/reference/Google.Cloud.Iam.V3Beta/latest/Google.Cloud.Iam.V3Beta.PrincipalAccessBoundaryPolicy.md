---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy
title: Identity and Access Management (IAM) v3beta API - Class PrincipalAccessBoundaryPolicy (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:55.739428+00:00
---

# Identity and Access Management (IAM) v3beta API - Class PrincipalAccessBoundaryPolicy (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3beta API - Class PrincipalAccessBoundaryPolicy (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class PrincipalAccessBoundaryPolicy : IMessage<PrincipalAccessBoundaryPolicy>, IEquatable<PrincipalAccessBoundaryPolicy>, IDeepCloneable<PrincipalAccessBoundaryPolicy>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v3beta API class PrincipalAccessBoundaryPolicy.

An IAM principal access boundary policy resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PrincipalAccessBoundaryPolicy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta)

## Assembly

Google.Cloud.Iam.V3Beta.dll

## Constructors 

### PrincipalAccessBoundaryPolicy()
    
    
    public PrincipalAccessBoundaryPolicy()

### PrincipalAccessBoundaryPolicy(PrincipalAccessBoundaryPolicy)
    
    
    public PrincipalAccessBoundaryPolicy(PrincipalAccessBoundaryPolicy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy)`  
  
  
## Properties 

### Annotations
    
    
    public MapField<string, string> Annotations { get; }

Optional. User defined annotations. See <https://google.aip.dev/148#annotations> for more details such as format and size limitations

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time when the principal access boundary policy was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Details
    
    
    public PrincipalAccessBoundaryPolicyDetails Details { get; set; }

Optional. The details for the principal access boundary policy.

**Property Value**  
---  
**Type** | **Description**  
`[PrincipalAccessBoundaryPolicyDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyDetails)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Optional. The description of the principal access boundary policy. Must be less than or equal to 63 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. The etag for the principal access boundary. If this is provided on update, it must match the server's etag.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The resource name of the principal access boundary policy.

The following format is supported: `organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{policy_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrincipalAccessBoundaryPolicyName
    
    
    public PrincipalAccessBoundaryPolicyName PrincipalAccessBoundaryPolicyName { get; set; }

[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicy#Google_Cloud_Iam_V3Beta_PrincipalAccessBoundaryPolicy_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PrincipalAccessBoundaryPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.PrincipalAccessBoundaryPolicyName)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. The globally unique ID of the principal access boundary policy.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The time when the principal access boundary policy was most recently updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
