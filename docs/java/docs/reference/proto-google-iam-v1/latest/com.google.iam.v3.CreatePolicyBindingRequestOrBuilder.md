---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3.CreatePolicyBindingRequestOrBuilder
title: Interface CreatePolicyBindingRequestOrBuilder (1.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:56.000603+00:00
---

# Interface CreatePolicyBindingRequestOrBuilder (1.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3.CreatePolicyBindingRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreatePolicyBindingRequestOrBuilder (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.73.0 (latest)  1.69.0  1.68.0  1.67.0  1.65.0  1.62.0  1.61.0  1.60.1  1.59.1  1.58.2  1.57.0  1.56.3  1.55.0  1.54.2  1.53.0  1.52.0  1.51.0  1.49.1  1.48.0  1.47.0  1.46.0  1.45.1  1.44.0  1.43.0  1.41.0  1.40.1  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.0  1.29.0  1.28.0  1.27.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.0  1.18.1  1.17.1  1.16.1  1.10.0  1.9.3  1.8.0  1.7.0  1.6.23  1.5.1  1.4.1  1.3.4  1.2.12 
    
    
    public interface CreatePolicyBindingRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getParent()
    
    
    public abstract String getParent()

Required. The parent resource where this policy binding will be created. The binding parent is the closest Resource Manager resource (project, folder or organization) to the binding target.

Format:

  * `projects/{project_id}/locations/{location}`
  * `projects/{project_number}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `organizations/{organization_id}/locations/{location}`



` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent resource where this policy binding will be created. The binding parent is the closest Resource Manager resource (project, folder or organization) to the binding target.

Format:

  * `projects/{project_id}/locations/{location}`
  * `projects/{project_number}/locations/{location}`
  * `folders/{folder_id}/locations/{location}`
  * `organizations/{organization_id}/locations/{location}`



` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getPolicyBinding()
    
    
    public abstract PolicyBinding getPolicyBinding()

Required. The policy binding to create.

` .google.iam.v3.PolicyBinding policy_binding = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBinding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3.PolicyBinding)` | The policyBinding.  
  
### getPolicyBindingId()
    
    
    public abstract String getPolicyBindingId()

Required. The ID to use for the policy binding, which will become the final component of the policy binding's resource name.

This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /a-z{2,62}/.

`string policy_binding_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The policyBindingId.  
  
### getPolicyBindingIdBytes()
    
    
    public abstract ByteString getPolicyBindingIdBytes()

Required. The ID to use for the policy binding, which will become the final component of the policy binding's resource name.

This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /a-z{2,62}/.

`string policy_binding_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for policyBindingId.  
  
### getPolicyBindingOrBuilder()
    
    
    public abstract PolicyBindingOrBuilder getPolicyBindingOrBuilder()

Required. The policy binding to create.

` .google.iam.v3.PolicyBinding policy_binding = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PolicyBindingOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3.PolicyBindingOrBuilder)` |   
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

Optional. If set, validate the request and preview the creation, but do not actually post it.

`bool validate_only = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
### hasPolicyBinding()
    
    
    public abstract boolean hasPolicyBinding()

Required. The policy binding to create.

` .google.iam.v3.PolicyBinding policy_binding = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the policyBinding field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
