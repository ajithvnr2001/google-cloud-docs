---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule
title: Identity and Access Management (IAM) v3beta API - Class AccessPolicyRule (1.0.0-beta03) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:03.020424+00:00
---

# Identity and Access Management (IAM) v3beta API - Class AccessPolicyRule (1.0.0-beta03)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity and Access Management (IAM) v3beta API - Class AccessPolicyRule (1.0.0-beta03) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta03 (latest)  1.0.0-beta02 
    
    
    public sealed class AccessPolicyRule : IMessage<AccessPolicyRule>, IEquatable<AccessPolicyRule>, IDeepCloneable<AccessPolicyRule>, IBufferMessage, IMessage

Reference documentation and code samples for the Identity and Access Management (IAM) v3beta API class AccessPolicyRule.

Access Policy Rule that determines the behavior of the policy.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AccessPolicyRule

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AccessPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AccessPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AccessPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Iam.V3Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta)

## Assembly

Google.Cloud.Iam.V3Beta.dll

## Constructors 

### AccessPolicyRule()
    
    
    public AccessPolicyRule()

### AccessPolicyRule(AccessPolicyRule)
    
    
    public AccessPolicyRule(AccessPolicyRule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AccessPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule)`  
  
  
## Properties 

### Conditions
    
    
    public MapField<string, Expr> Conditions { get; }

Optional. The conditions that determine whether this rule applies to a request. Conditions are identified by their key, which is the FQDN of the service that they are relevant to. For example:
    
    
    "conditions": {
     "iam.googleapis.com": {
      "expression": <cel expression>
     }
    }
    

Each rule is evaluated independently. If this rule does not apply to a request, other rules might still apply. Currently supported keys are as follows:

  * `eventarc.googleapis.com`: Can use `CEL` functions that evaluate resource fields.

  * `iam.googleapis.com`: Can use `CEL` functions that evaluate [resource tags](https://cloud.google.com/iam/help/conditions/resource-tags) and combine them using boolean and logical operators. Other functions and operators are not supported.




**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[Expr](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Expr.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. Customer specified description of the rule. Must be less than or equal to 256 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Effect
    
    
    public AccessPolicyRule.Types.Effect Effect { get; set; }

Required. The effect of the rule.

**Property Value**  
---  
**Type** | **Description**  
`[AccessPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule.Types)[Effect](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule.Types.Effect)` |   
  
### ExcludedPrincipals
    
    
    public RepeatedField<string> ExcludedPrincipals { get; }

Optional. The identities that are excluded from the access policy rule, even if they are listed in the `principals`. For example, you could add a Google group to the `principals`, then exclude specific users who belong to that group.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasDescription
    
    
    public bool HasDescription { get; }

Gets whether the "description" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEffect
    
    
    public bool HasEffect { get; }

Gets whether the "effect" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Operation
    
    
    public AccessPolicyRule.Types.Operation Operation { get; set; }

Required. Attributes that are used to determine whether this rule applies to a request.

**Property Value**  
---  
**Type** | **Description**  
`[AccessPolicyRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule.Types)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Iam.V3Beta/latest/Google.Cloud.Iam.V3Beta.AccessPolicyRule.Types.Operation)` |   
  
### Principals
    
    
    public RepeatedField<string> Principals { get; }

Required. The identities for which this rule's effect governs using one or more permissions on Google Cloud resources. This field can contain the following values:

  * `principal://goog/subject/{email_id}`: A specific Google Account. Includes Gmail, Cloud Identity, and Google Workspace user accounts. For example, `principal://goog/subject/alice@example.com`.

  * `principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}`: A Google Cloud service account. For example, `principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com`.

  * `principalSet://goog/group/{group_id}`: A Google group. For example, `principalSet://goog/group/admins@example.com`.

  * `principalSet://goog/cloudIdentityCustomerId/{customer_id}`: All of the principals associated with the specified Google Workspace or Cloud Identity customer ID. For example, `principalSet://goog/cloudIdentityCustomerId/C01Abc35`.




If an identifier that was previously set on a policy is soft deleted, then calls to read that policy will return the identifier with a deleted prefix. Users cannot set identifiers with this syntax.

  * `deleted:principal://goog/subject/{email_id}?uid={uid}`: A specific Google Account that was deleted recently. For example, `deleted:principal://goog/subject/alice@example.com?uid=1234567890`. If the Google Account is recovered, this identifier reverts to the standard identifier for a Google Account.

  * `deleted:principalSet://goog/group/{group_id}?uid={uid}`: A Google group that was deleted recently. For example, `deleted:principalSet://goog/group/admins@example.com?uid=1234567890`. If the Google group is restored, this identifier reverts to the standard identifier for a Google group.

  * `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/{service_account_id}?uid={uid}`: A Google Cloud service account that was deleted recently. For example, `deleted:principal://iam.googleapis.com/projects/-/serviceAccounts/my-service-account@iam.gserviceaccount.com?uid=1234567890`. If the service account is undeleted, this identifier reverts to the standard identifier for a service account.




**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
