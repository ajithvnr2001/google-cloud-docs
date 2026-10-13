---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/google.cloud.policytroubleshooter.v1.Explanations.ExplainedPolicyOrBuilder
title: Interface Explanations.ExplainedPolicyOrBuilder (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:44.370468+00:00
---

# Interface Explanations.ExplainedPolicyOrBuilder (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/google.cloud.policytroubleshooter.v1.Explanations.ExplainedPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Explanations.ExplainedPolicyOrBuilder (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6  1.1.0  1.0.4  0.4.4 
    
    
    public static interface Explanations.ExplainedPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccess()
    
    
    public abstract Explanations.AccessState getAccess()

Indicates whether _this policy_ provides the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another policy that overrides this policy. To determine whether the principal actually has the permission, use the `access` field in the TroubleshootIamPolicyResponse.

`.google.cloud.policytroubleshooter.v1.AccessState access = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Explanations.AccessState](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/google.cloud.policytroubleshooter.v1.Explanations.AccessState)` | The access.  
  
### getAccessValue()
    
    
    public abstract int getAccessValue()

Indicates whether _this policy_ provides the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another policy that overrides this policy. To determine whether the principal actually has the permission, use the `access` field in the TroubleshootIamPolicyResponse.

`.google.cloud.policytroubleshooter.v1.AccessState access = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for access.  
  
### getBindingExplanations(int index)
    
    
    public abstract Explanations.BindingExplanation getBindingExplanations(int index)

Details about how each binding in the policy affects the principal's ability, or inability, to use the permission for the resource.

If the sender of the request does not have access to the policy, this field is omitted.

` repeated .google.cloud.policytroubleshooter.v1.BindingExplanation binding_explanations = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanations.BindingExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/google.cloud.policytroubleshooter.v1.Explanations.BindingExplanation)` |   
  
### getBindingExplanationsCount()
    
    
    public abstract int getBindingExplanationsCount()

Details about how each binding in the policy affects the principal's ability, or inability, to use the permission for the resource.

If the sender of the request does not have access to the policy, this field is omitted.

` repeated .google.cloud.policytroubleshooter.v1.BindingExplanation binding_explanations = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBindingExplanationsList()
    
    
    public abstract List<Explanations.BindingExplanation> getBindingExplanationsList()

Details about how each binding in the policy affects the principal's ability, or inability, to use the permission for the resource.

If the sender of the request does not have access to the policy, this field is omitted.

` repeated .google.cloud.policytroubleshooter.v1.BindingExplanation binding_explanations = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BindingExplanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/google.cloud.policytroubleshooter.v1.Explanations.BindingExplanation)>` |   
  
### getBindingExplanationsOrBuilder(int index)
    
    
    public abstract Explanations.BindingExplanationOrBuilder getBindingExplanationsOrBuilder(int index)

Details about how each binding in the policy affects the principal's ability, or inability, to use the permission for the resource.

If the sender of the request does not have access to the policy, this field is omitted.

` repeated .google.cloud.policytroubleshooter.v1.BindingExplanation binding_explanations = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Explanations.BindingExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/google.cloud.policytroubleshooter.v1.Explanations.BindingExplanationOrBuilder)` |   
  
### getBindingExplanationsOrBuilderList()
    
    
    public abstract List<? extends Explanations.BindingExplanationOrBuilder> getBindingExplanationsOrBuilderList()

Details about how each binding in the policy affects the principal's ability, or inability, to use the permission for the resource.

If the sender of the request does not have access to the policy, this field is omitted.

` repeated .google.cloud.policytroubleshooter.v1.BindingExplanation binding_explanations = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends google.cloud.policytroubleshooter.v1.Explanations.BindingExplanationOrBuilder>` |   
  
### getFullResourceName()
    
    
    public abstract String getFullResourceName()

The full resource name that identifies the resource. For example, `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance`.

If the sender of the request does not have access to the policy, this field is omitted.

For examples of full resource names for Google Cloud services, see <https://cloud.google.com/iam/help/troubleshooter/full-resource-names>.

`string full_resource_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fullResourceName.  
  
### getFullResourceNameBytes()
    
    
    public abstract ByteString getFullResourceNameBytes()

The full resource name that identifies the resource. For example, `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance`.

If the sender of the request does not have access to the policy, this field is omitted.

For examples of full resource names for Google Cloud services, see <https://cloud.google.com/iam/help/troubleshooter/full-resource-names>.

`string full_resource_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fullResourceName.  
  
### getPolicy()
    
    
    public abstract Policy getPolicy()

The IAM policy attached to the resource.

If the sender of the request does not have access to the policy, this field is empty.

`.google.iam.v1.Policy policy = 3;`

**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` | The policy.  
  
### getPolicyOrBuilder()
    
    
    public abstract PolicyOrBuilder getPolicyOrBuilder()

The IAM policy attached to the resource.

If the sender of the request does not have access to the policy, this field is empty.

`.google.iam.v1.Policy policy = 3;`

**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.PolicyOrBuilder` |   
  
### getRelevance()
    
    
    public abstract Explanations.HeuristicRelevance getRelevance()

The relevance of this policy to the overall determination in the TroubleshootIamPolicyResponse.

If the sender of the request does not have access to the policy, this field is omitted.

`.google.cloud.policytroubleshooter.v1.HeuristicRelevance relevance = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Explanations.HeuristicRelevance](https://docs.cloud.google.com/java/docs/reference/google-cloud-policy-troubleshooter/latest/google.cloud.policytroubleshooter.v1.Explanations.HeuristicRelevance)` | The relevance.  
  
### getRelevanceValue()
    
    
    public abstract int getRelevanceValue()

The relevance of this policy to the overall determination in the TroubleshootIamPolicyResponse.

If the sender of the request does not have access to the policy, this field is omitted.

`.google.cloud.policytroubleshooter.v1.HeuristicRelevance relevance = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for relevance.  
  
### hasPolicy()
    
    
    public abstract boolean hasPolicy()

The IAM policy attached to the resource.

If the sender of the request does not have access to the policy, this field is empty.

`.google.iam.v1.Policy policy = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the policy field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
