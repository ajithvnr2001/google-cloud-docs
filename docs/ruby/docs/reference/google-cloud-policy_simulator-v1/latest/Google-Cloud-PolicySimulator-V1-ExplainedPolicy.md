---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-ExplainedPolicy/
title: Policy Simulator V1 API - Class Google::Cloud::PolicySimulator::V1::ExplainedPolicy (v1.9.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:24.155919+00:00
---

# Policy Simulator V1 API - Class Google::Cloud::PolicySimulator::V1::ExplainedPolicy (v1.9.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-ExplainedPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Simulator V1 API - Class Google::Cloud::PolicySimulator::V1::ExplainedPolicy (v1.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.4.0  0.3.2  0.2.0  0.1.1 

Reference documentation and code samples for the Policy Simulator V1 API class Google::Cloud::PolicySimulator::V1::ExplainedPolicy.

Details about how a specific IAM [Policy][google.iam.v1.Policy] contributed to the access check.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #access
    
    
    def access() -> ::Google::Cloud::PolicySimulator::V1::AccessState

**Returns**

  * ([::Google::Cloud::PolicySimulator::V1::AccessState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-AccessState)) — Indicates whether _this policy_ provides the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another policy that overrides this policy. To determine whether the principal actually has the permission, use the `access` field in the [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.v3.TroubleshootIamPolicyResponse]. 




### #access=
    
    
    def access=(value) -> ::Google::Cloud::PolicySimulator::V1::AccessState

**Parameter**

  * **value** ([::Google::Cloud::PolicySimulator::V1::AccessState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-AccessState)) — Indicates whether _this policy_ provides the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another policy that overrides this policy. To determine whether the principal actually has the permission, use the `access` field in the [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.v3.TroubleshootIamPolicyResponse]. 




**Returns**

  * ([::Google::Cloud::PolicySimulator::V1::AccessState](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-AccessState)) — Indicates whether _this policy_ provides the specified permission to the specified principal for the specified resource.

This field does _not_ indicate whether the principal actually has the permission for the resource. There might be another policy that overrides this policy. To determine whether the principal actually has the permission, use the `access` field in the [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.v3.TroubleshootIamPolicyResponse]. 




### #binding_explanations
    
    
    def binding_explanations() -> ::Array<::Google::Cloud::PolicySimulator::V1::BindingExplanation>

**Returns**

  * (::Array<[::Google::Cloud::PolicySimulator::V1::BindingExplanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-BindingExplanation)>) — Details about how each binding in the policy affects the principal's ability, or inability, to use the permission for the resource.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted. 




### #binding_explanations=
    
    
    def binding_explanations=(value) -> ::Array<::Google::Cloud::PolicySimulator::V1::BindingExplanation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::PolicySimulator::V1::BindingExplanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-BindingExplanation)>) — Details about how each binding in the policy affects the principal's ability, or inability, to use the permission for the resource.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted. 




**Returns**

  * (::Array<[::Google::Cloud::PolicySimulator::V1::BindingExplanation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-BindingExplanation)>) — Details about how each binding in the policy affects the principal's ability, or inability, to use the permission for the resource.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted. 




### #full_resource_name
    
    
    def full_resource_name() -> ::String

**Returns**

  * (::String) — The full resource name that identifies the resource. For example, `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance`.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted.

For examples of full resource names for Google Cloud services, see https://cloud.google.com/iam/help/troubleshooter/full-resource-names. 




### #full_resource_name=
    
    
    def full_resource_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The full resource name that identifies the resource. For example, `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance`.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted.

For examples of full resource names for Google Cloud services, see https://cloud.google.com/iam/help/troubleshooter/full-resource-names. 




**Returns**

  * (::String) — The full resource name that identifies the resource. For example, `//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance`.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted.

For examples of full resource names for Google Cloud services, see https://cloud.google.com/iam/help/troubleshooter/full-resource-names. 




### #policy
    
    
    def policy() -> ::Google::Iam::V1::Policy

**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Iam-V1-Policy)) — The IAM policy attached to the resource.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is empty. 




### #policy=
    
    
    def policy=(value) -> ::Google::Iam::V1::Policy

**Parameter**

  * **value** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Iam-V1-Policy)) — The IAM policy attached to the resource.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is empty. 




**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Iam-V1-Policy)) — The IAM policy attached to the resource.

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is empty. 




### #relevance
    
    
    def relevance() -> ::Google::Cloud::PolicySimulator::V1::HeuristicRelevance

**Returns**

  * ([::Google::Cloud::PolicySimulator::V1::HeuristicRelevance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-HeuristicRelevance)) — The relevance of this policy to the overall determination in the [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.v3.TroubleshootIamPolicyResponse].

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted. 




### #relevance=
    
    
    def relevance=(value) -> ::Google::Cloud::PolicySimulator::V1::HeuristicRelevance

**Parameter**

  * **value** ([::Google::Cloud::PolicySimulator::V1::HeuristicRelevance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-HeuristicRelevance)) — The relevance of this policy to the overall determination in the [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.v3.TroubleshootIamPolicyResponse].

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted. 




**Returns**

  * ([::Google::Cloud::PolicySimulator::V1::HeuristicRelevance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-HeuristicRelevance)) — The relevance of this policy to the overall determination in the [TroubleshootIamPolicyResponse][google.cloud.policytroubleshooter.v3.TroubleshootIamPolicyResponse].

If the user who created the [Replay](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_simulator-v1/latest/Google-Cloud-PolicySimulator-V1-Replay "Google::Cloud::PolicySimulator::V1::Replay \(class\)") does not have access to the policy, this field is omitted. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
