---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy
title: Binary Authorization v1beta1 API - Class Policy (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:53.582693+00:00
---

# Binary Authorization v1beta1 API - Class Policy (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1beta1 API - Class Policy (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta05 
    
    
    public sealed class Policy : IMessage<Policy>, IEquatable<Policy>, IDeepCloneable<Policy>, IBufferMessage, IMessage

Reference documentation and code samples for the Binary Authorization v1beta1 API class Policy.

A [policy][google.cloud.binaryauthorization.v1beta1.Policy] for Binary Authorization.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Policy

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BinaryAuthorization.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1)

## Assembly

Google.Cloud.BinaryAuthorization.V1Beta1.dll

## Constructors 

### Policy()
    
    
    public Policy()

### Policy(Policy)
    
    
    public Policy(Policy other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)`  
  
  
## Properties 

### AdmissionWhitelistPatterns
    
    
    public RepeatedField<AdmissionWhitelistPattern> AdmissionWhitelistPatterns { get; }

Optional. Admission policy allowlisting. A matching admission request will always be permitted. This feature is typically used to exclude Google or third-party infrastructure images from Binary Authorization policies.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AdmissionWhitelistPattern](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionWhitelistPattern)` |   
  
### ClusterAdmissionRules
    
    
    public MapField<string, AdmissionRule> ClusterAdmissionRules { get; }

Optional. Per-cluster admission rules. Cluster spec format: `location.clusterId`. There can be at most one admission rule per cluster spec. A `location` is either a compute zone (e.g. us-central1-a) or a region (e.g. us-central1). For `clusterId` syntax restrictions see <https://cloud.google.com/container-engine/reference/rest/v1/projects.zones.clusters>.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[AdmissionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule)` |   
  
### DefaultAdmissionRule
    
    
    public AdmissionRule DefaultAdmissionRule { get; set; }

Required. Default admission rule for a cluster without a per-cluster, per- kubernetes-service-account, or per-istio-service-identity admission rule.

**Property Value**  
---  
**Type** | **Description**  
`[AdmissionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. A descriptive comment.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. A checksum, returned by the server, that can be sent on update requests to ensure the policy has an up-to-date value before attempting to update it. See <https://google.aip.dev/154>.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GlobalPolicyEvaluationMode
    
    
    public Policy.Types.GlobalPolicyEvaluationMode GlobalPolicyEvaluationMode { get; set; }

Optional. Controls the evaluation of a Google-maintained global admission policy for common system-level images. Images not covered by the global policy will be subject to the project admission policy. This setting has no effect when specified inside a global admission policy.

**Property Value**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy.Types)[GlobalPolicyEvaluationMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy.Types.GlobalPolicyEvaluationMode)` |   
  
### IstioServiceIdentityAdmissionRules
    
    
    public MapField<string, AdmissionRule> IstioServiceIdentityAdmissionRules { get; }

Optional. Per-istio-service-identity admission rules. Istio service identity spec format: `spiffe://<domain>/ns/<namespace>/sa/<serviceaccount>` or `<domain>/ns/<namespace>/sa/<serviceaccount>` e.g. `spiffe://example.com/ns/test-ns/sa/default`

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[AdmissionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule)` |   
  
### KubernetesNamespaceAdmissionRules
    
    
    public MapField<string, AdmissionRule> KubernetesNamespaceAdmissionRules { get; }

Optional. Per-kubernetes-namespace admission rules. K8s namespace spec format: `[a-z.-]+`, e.g. `some-namespace`

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[AdmissionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule)` |   
  
### KubernetesServiceAccountAdmissionRules
    
    
    public MapField<string, AdmissionRule> KubernetesServiceAccountAdmissionRules { get; }

Optional. Per-kubernetes-service-account admission rules. Service account spec format: `namespace:serviceaccount`. e.g. `test-ns:default`

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[AdmissionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.AdmissionRule)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name, in the format `projects/*/policy`. There is at most one policy per project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PolicyName
    
    
    public PolicyName PolicyName { get; set; }

[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PolicyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.Policy#Google_Cloud_BinaryAuthorization_V1Beta1_Policy_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PolicyName)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Time when the policy was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
