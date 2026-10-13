---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanationOrBuilder
title: Interface BindingExplanationOrBuilder (0.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:16.654064+00:00
---

# Interface BindingExplanationOrBuilder (0.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BindingExplanationOrBuilder (0.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.78.0 (latest)  0.74.0  0.73.0  0.72.0  0.70.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.59.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface BindingExplanationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsMemberships(String key)
    
    
    public abstract boolean containsMemberships(String key)

Indicates whether each principal in the binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the binding, and each value indicates whether the principal in the binding includes the principal in the request.

For example, suppose that a binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

The principal in the replayed access tuple is `user:bob@example.com`. This user is a principal of the group `group:product-eng@example.com`.

For the first principal in the binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_NOT_INCLUDED`.

For the second principal in the binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_INCLUDED`.




` map<string, .google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership> memberships = 5; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccess()
    
    
    public abstract AccessState getAccess()

Required. Indicates whether _this binding_ provides the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another binding that overrides this binding. To determine whether the principal actually has the permission, use the `access` field in the TroubleshootIamPolicyResponse.

` .google.cloud.policysimulator.v1.AccessState access = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AccessState](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.AccessState)` | The access.  
  
### getAccessValue()
    
    
    public abstract int getAccessValue()

Required. Indicates whether _this binding_ provides the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another binding that overrides this binding. To determine whether the principal actually has the permission, use the `access` field in the TroubleshootIamPolicyResponse.

` .google.cloud.policysimulator.v1.AccessState access = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for access.  
  
### getCondition()
    
    
    public abstract Expr getCondition()

A condition expression that prevents this binding from granting access unless the expression evaluates to `true`.

To learn about IAM Conditions, see <https://cloud.google.com/iam/docs/conditions-overview>.

`.google.type.Expr condition = 7;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Expr` | The condition.  
  
### getConditionOrBuilder()
    
    
    public abstract ExprOrBuilder getConditionOrBuilder()

A condition expression that prevents this binding from granting access unless the expression evaluates to `true`.

To learn about IAM Conditions, see <https://cloud.google.com/iam/docs/conditions-overview>.

`.google.type.Expr condition = 7;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.ExprOrBuilder` |   
  
### getMemberships() (deprecated)
    
    
    public abstract Map<String,BindingExplanation.AnnotatedMembership> getMemberships()

Use [#getMembershipsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanationOrBuilder#com_google_cloud_policysimulator_v1_BindingExplanationOrBuilder_getMembershipsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership)>` |   
  
### getMembershipsCount()
    
    
    public abstract int getMembershipsCount()

Indicates whether each principal in the binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the binding, and each value indicates whether the principal in the binding includes the principal in the request.

For example, suppose that a binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

The principal in the replayed access tuple is `user:bob@example.com`. This user is a principal of the group `group:product-eng@example.com`.

For the first principal in the binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_NOT_INCLUDED`.

For the second principal in the binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_INCLUDED`.




` map<string, .google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership> memberships = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMembershipsMap()
    
    
    public abstract Map<String,BindingExplanation.AnnotatedMembership> getMembershipsMap()

Indicates whether each principal in the binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the binding, and each value indicates whether the principal in the binding includes the principal in the request.

For example, suppose that a binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

The principal in the replayed access tuple is `user:bob@example.com`. This user is a principal of the group `group:product-eng@example.com`.

For the first principal in the binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_NOT_INCLUDED`.

For the second principal in the binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_INCLUDED`.




` map<string, .google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership> memberships = 5; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AnnotatedMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership)>` |   
  
### getMembershipsOrDefault(String key, BindingExplanation.AnnotatedMembership defaultValue)
    
    
    public abstract BindingExplanation.AnnotatedMembership getMembershipsOrDefault(String key, BindingExplanation.AnnotatedMembership defaultValue)

Indicates whether each principal in the binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the binding, and each value indicates whether the principal in the binding includes the principal in the request.

For example, suppose that a binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

The principal in the replayed access tuple is `user:bob@example.com`. This user is a principal of the group `group:product-eng@example.com`.

For the first principal in the binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_NOT_INCLUDED`.

For the second principal in the binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_INCLUDED`.




` map<string, .google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership> memberships = 5; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[BindingExplanation.AnnotatedMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BindingExplanation.AnnotatedMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership)` |   
  
### getMembershipsOrThrow(String key)
    
    
    public abstract BindingExplanation.AnnotatedMembership getMembershipsOrThrow(String key)

Indicates whether each principal in the binding includes the principal specified in the request, either directly or indirectly. Each key identifies a principal in the binding, and each value indicates whether the principal in the binding includes the principal in the request.

For example, suppose that a binding includes the following principals:

  * `user:alice@example.com`
  * `group:product-eng@example.com`

The principal in the replayed access tuple is `user:bob@example.com`. This user is a principal of the group `group:product-eng@example.com`.

For the first principal in the binding, the key is `user:alice@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_NOT_INCLUDED`.

For the second principal in the binding, the key is `group:product-eng@example.com`, and the `membership` field in the value is set to `MEMBERSHIP_INCLUDED`.




` map<string, .google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership> memberships = 5; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BindingExplanation.AnnotatedMembership](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanation.AnnotatedMembership)` |   
  
### getRelevance()
    
    
    public abstract HeuristicRelevance getRelevance()

The relevance of this binding to the overall determination for the entire policy.

`.google.cloud.policysimulator.v1.HeuristicRelevance relevance = 6;`

**Returns**  
---  
**Type** | **Description**  
`[HeuristicRelevance](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.HeuristicRelevance)` | The relevance.  
  
### getRelevanceValue()
    
    
    public abstract int getRelevanceValue()

The relevance of this binding to the overall determination for the entire policy.

`.google.cloud.policysimulator.v1.HeuristicRelevance relevance = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for relevance.  
  
### getRole()
    
    
    public abstract String getRole()

The role that this binding grants. For example, `roles/compute.serviceAgent`.

For a complete list of predefined IAM roles, as well as the permissions in each role, see <https://cloud.google.com/iam/help/roles/reference>.

`string role = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The role.  
  
### getRoleBytes()
    
    
    public abstract ByteString getRoleBytes()

The role that this binding grants. For example, `roles/compute.serviceAgent`.

For a complete list of predefined IAM roles, as well as the permissions in each role, see <https://cloud.google.com/iam/help/roles/reference>.

`string role = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for role.  
  
### getRolePermission()
    
    
    public abstract BindingExplanation.RolePermission getRolePermission()

Indicates whether the role granted by this binding contains the specified permission.

`.google.cloud.policysimulator.v1.BindingExplanation.RolePermission role_permission = 3; `

**Returns**  
---  
**Type** | **Description**  
`[BindingExplanation.RolePermission](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.BindingExplanation.RolePermission)` | The rolePermission.  
  
### getRolePermissionRelevance()
    
    
    public abstract HeuristicRelevance getRolePermissionRelevance()

The relevance of the permission's existence, or nonexistence, in the role to the overall determination for the entire policy.

`.google.cloud.policysimulator.v1.HeuristicRelevance role_permission_relevance = 4;`

**Returns**  
---  
**Type** | **Description**  
`[HeuristicRelevance](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.HeuristicRelevance)` | The rolePermissionRelevance.  
  
### getRolePermissionRelevanceValue()
    
    
    public abstract int getRolePermissionRelevanceValue()

The relevance of the permission's existence, or nonexistence, in the role to the overall determination for the entire policy.

`.google.cloud.policysimulator.v1.HeuristicRelevance role_permission_relevance = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for rolePermissionRelevance.  
  
### getRolePermissionValue()
    
    
    public abstract int getRolePermissionValue()

Indicates whether the role granted by this binding contains the specified permission.

`.google.cloud.policysimulator.v1.BindingExplanation.RolePermission role_permission = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for rolePermission.  
  
### hasCondition()
    
    
    public abstract boolean hasCondition()

A condition expression that prevents this binding from granting access unless the expression evaluates to `true`.

To learn about IAM Conditions, see <https://cloud.google.com/iam/docs/conditions-overview>.

`.google.type.Expr condition = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the condition field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
