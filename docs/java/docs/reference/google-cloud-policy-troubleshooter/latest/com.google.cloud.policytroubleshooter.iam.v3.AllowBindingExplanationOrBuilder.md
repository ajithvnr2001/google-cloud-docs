---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanationOrBuilder
title: Interface AllowBindingExplanationOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:51.458902+00:00
---

# Interface AllowBindingExplanationOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AllowBindingExplanationOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6  1.1.0  1.0.4  0.4.4 
    
    
    public interface AllowBindingExplanationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsMemberships(String key)
    
    
    public abstract boolean containsMemberships(String key)

Indicates whether each role binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the role binding, and each value indicates whether the principal in the role binding includes the principal in the request.

For example, suppose that a role binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

You want to troubleshoot access for `user:bob@example.com`. This user is a member of the group `group:product-eng@example.com`.

For the first principal in the role binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `NOT_INCLUDED`.

For the second principal in the role binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `INCLUDED`.




` map<string, .google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership> memberships = 6; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllowAccessState()
    
    
    public abstract AllowAccessState getAllowAccessState()

Required. Indicates whether _this role binding_ gives the specified permission to the specified principal on the specified resource.

This field does _not_ indicate whether the principal actually has the permission on the resource. There might be another role binding that overrides this role binding. To determine whether the principal actually has the permission, use the `overall_access_state` field in the TroubleshootIamPolicyResponse.

` .google.cloud.policytroubleshooter.iam.v3.AllowAccessState allow_access_state = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AllowAccessState](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowAccessState)` | The allowAccessState.  
  
### getAllowAccessStateValue()
    
    
    public abstract int getAllowAccessStateValue()

Required. Indicates whether _this role binding_ gives the specified permission to the specified principal on the specified resource.

This field does _not_ indicate whether the principal actually has the permission on the resource. There might be another role binding that overrides this role binding. To determine whether the principal actually has the permission, use the `overall_access_state` field in the TroubleshootIamPolicyResponse.

` .google.cloud.policytroubleshooter.iam.v3.AllowAccessState allow_access_state = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for allowAccessState.  
  
### getCombinedMembership()
    
    
    public abstract AllowBindingExplanation.AnnotatedAllowMembership getCombinedMembership()

The combined result of all memberships. Indicates if the principal is included in any role binding, either directly or indirectly.

` .google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership combined_membership = 5; `

**Returns**  
---  
**Type** | **Description**  
`[AllowBindingExplanation.AnnotatedAllowMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership)` | The combinedMembership.  
  
### getCombinedMembershipOrBuilder()
    
    
    public abstract AllowBindingExplanation.AnnotatedAllowMembershipOrBuilder getCombinedMembershipOrBuilder()

The combined result of all memberships. Indicates if the principal is included in any role binding, either directly or indirectly.

` .google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership combined_membership = 5; `

**Returns**  
---  
**Type** | **Description**  
`[AllowBindingExplanation.AnnotatedAllowMembershipOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembershipOrBuilder)` |   
  
### getCondition()
    
    
    public abstract Expr getCondition()

A condition expression that specifies when the role binding grants access.

To learn about IAM Conditions, see <https://cloud.google.com/iam/help/conditions/overview>.

`.google.type.Expr condition = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Expr` | The condition.  
  
### getConditionExplanation()
    
    
    public abstract ConditionExplanation getConditionExplanation()

Condition evaluation state for this role binding.

`.google.cloud.policytroubleshooter.iam.v3.ConditionExplanation condition_explanation = 9; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.ConditionExplanation)` | The conditionExplanation.  
  
### getConditionExplanationOrBuilder()
    
    
    public abstract ConditionExplanationOrBuilder getConditionExplanationOrBuilder()

Condition evaluation state for this role binding.

`.google.cloud.policytroubleshooter.iam.v3.ConditionExplanation condition_explanation = 9; `

**Returns**  
---  
**Type** | **Description**  
`[ConditionExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.ConditionExplanationOrBuilder)` |   
  
### getConditionOrBuilder()
    
    
    public abstract ExprOrBuilder getConditionOrBuilder()

A condition expression that specifies when the role binding grants access.

To learn about IAM Conditions, see <https://cloud.google.com/iam/help/conditions/overview>.

`.google.type.Expr condition = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.ExprOrBuilder` |   
  
### getMemberships() (deprecated)
    
    
    public abstract Map<String,AllowBindingExplanation.AnnotatedAllowMembership> getMemberships()

Use [#getMembershipsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanationOrBuilder#com_google_cloud_policytroubleshooter_iam_v3_AllowBindingExplanationOrBuilder_getMembershipsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedAllowMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership)>` |   
  
### getMembershipsCount()
    
    
    public abstract int getMembershipsCount()

Indicates whether each role binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the role binding, and each value indicates whether the principal in the role binding includes the principal in the request.

For example, suppose that a role binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

You want to troubleshoot access for `user:bob@example.com`. This user is a member of the group `group:product-eng@example.com`.

For the first principal in the role binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `NOT_INCLUDED`.

For the second principal in the role binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `INCLUDED`.




` map<string, .google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership> memberships = 6; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMembershipsMap()
    
    
    public abstract Map<String,AllowBindingExplanation.AnnotatedAllowMembership> getMembershipsMap()

Indicates whether each role binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the role binding, and each value indicates whether the principal in the role binding includes the principal in the request.

For example, suppose that a role binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

You want to troubleshoot access for `user:bob@example.com`. This user is a member of the group `group:product-eng@example.com`.

For the first principal in the role binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `NOT_INCLUDED`.

For the second principal in the role binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `INCLUDED`.




` map<string, .google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership> memberships = 6; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedAllowMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership)>` |   
  
### getMembershipsOrDefault(String key, AllowBindingExplanation.AnnotatedAllowMembership defaultValue)
    
    
    public abstract AllowBindingExplanation.AnnotatedAllowMembership getMembershipsOrDefault(String key, AllowBindingExplanation.AnnotatedAllowMembership defaultValue)

Indicates whether each role binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the role binding, and each value indicates whether the principal in the role binding includes the principal in the request.

For example, suppose that a role binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

You want to troubleshoot access for `user:bob@example.com`. This user is a member of the group `group:product-eng@example.com`.

For the first principal in the role binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `NOT_INCLUDED`.

For the second principal in the role binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `INCLUDED`.




` map<string, .google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership> memberships = 6; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[AllowBindingExplanation.AnnotatedAllowMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllowBindingExplanation.AnnotatedAllowMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership)` |   
  
### getMembershipsOrThrow(String key)
    
    
    public abstract AllowBindingExplanation.AnnotatedAllowMembership getMembershipsOrThrow(String key)

Indicates whether each role binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the role binding, and each value indicates whether the principal in the role binding includes the principal in the request.

For example, suppose that a role binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

You want to troubleshoot access for `user:bob@example.com`. This user is a member of the group `group:product-eng@example.com`.

For the first principal in the role binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `NOT_INCLUDED`.

For the second principal in the role binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `INCLUDED`.




` map<string, .google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership> memberships = 6; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AllowBindingExplanation.AnnotatedAllowMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership)` |   
  
### getRelevance()
    
    
    public abstract HeuristicRelevance getRelevance()

The relevance of this role binding to the overall determination for the entire policy.

`.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance relevance = 7;`

**Returns**  
---  
**Type** | **Description**  
`[HeuristicRelevance](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance)` | The relevance.  
  
### getRelevanceValue()
    
    
    public abstract int getRelevanceValue()

The relevance of this role binding to the overall determination for the entire policy.

`.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance relevance = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for relevance.  
  
### getRole()
    
    
    public abstract String getRole()

The role that this role binding grants. For example, `roles/compute.admin`.

For a complete list of predefined IAM roles, as well as the permissions in each role, see <https://cloud.google.com/iam/help/roles/reference>.

`string role = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The role.  
  
### getRoleBytes()
    
    
    public abstract ByteString getRoleBytes()

The role that this role binding grants. For example, `roles/compute.admin`.

For a complete list of predefined IAM roles, as well as the permissions in each role, see <https://cloud.google.com/iam/help/roles/reference>.

`string role = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for role.  
  
### getRolePermission()
    
    
    public abstract RolePermissionInclusionState getRolePermission()

Indicates whether the role granted by this role binding contains the specified permission.

` .google.cloud.policytroubleshooter.iam.v3.RolePermissionInclusionState role_permission = 3; `

**Returns**  
---  
**Type** | **Description**  
`[RolePermissionInclusionState](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.RolePermissionInclusionState)` | The rolePermission.  
  
### getRolePermissionRelevance()
    
    
    public abstract HeuristicRelevance getRolePermissionRelevance()

The relevance of the permission's existence, or nonexistence, in the role to the overall determination for the entire policy.

` .google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance role_permission_relevance = 4; `

**Returns**  
---  
**Type** | **Description**  
`[HeuristicRelevance](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/com.google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance)` | The rolePermissionRelevance.  
  
### getRolePermissionRelevanceValue()
    
    
    public abstract int getRolePermissionRelevanceValue()

The relevance of the permission's existence, or nonexistence, in the role to the overall determination for the entire policy.

` .google.cloud.policytroubleshooter.iam.v3.HeuristicRelevance role_permission_relevance = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for rolePermissionRelevance.  
  
### getRolePermissionValue()
    
    
    public abstract int getRolePermissionValue()

Indicates whether the role granted by this role binding contains the specified permission.

` .google.cloud.policytroubleshooter.iam.v3.RolePermissionInclusionState role_permission = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for rolePermission.  
  
### hasCombinedMembership()
    
    
    public abstract boolean hasCombinedMembership()

The combined result of all memberships. Indicates if the principal is included in any role binding, either directly or indirectly.

` .google.cloud.policytroubleshooter.iam.v3.AllowBindingExplanation.AnnotatedAllowMembership combined_membership = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the combinedMembership field is set.  
  
### hasCondition()
    
    
    public abstract boolean hasCondition()

A condition expression that specifies when the role binding grants access.

To learn about IAM Conditions, see <https://cloud.google.com/iam/help/conditions/overview>.

`.google.type.Expr condition = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the condition field is set.  
  
### hasConditionExplanation()
    
    
    public abstract boolean hasConditionExplanation()

Condition evaluation state for this role binding.

`.google.cloud.policytroubleshooter.iam.v3.ConditionExplanation condition_explanation = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the conditionExplanation field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
