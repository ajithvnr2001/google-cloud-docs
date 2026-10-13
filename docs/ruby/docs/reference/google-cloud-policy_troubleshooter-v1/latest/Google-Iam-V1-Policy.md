---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-v1/latest/Google-Iam-V1-Policy/
title: IAM Policy Troubleshooter V1 API - Class Google::Iam::V1::Policy (v1.7.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:18.016698+00:00
---

# IAM Policy Troubleshooter V1 API - Class Google::Iam::V1::Policy (v1.7.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-v1/latest/Google-Iam-V1-Policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  IAM Policy Troubleshooter V1 API - Class Google::Iam::V1::Policy (v1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the IAM Policy Troubleshooter V1 API class Google::Iam::V1::Policy.

An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources.

A `Policy` is a collection of `bindings`. A `binding` binds one or more `members`, or principals, to a single `role`. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions; each `role` can be an IAM predefined role or a user-created custom role.

For some types of Google Cloud resources, a `binding` can also specify a `condition`, which is a logical expression that allows access to a resource only if the expression evaluates to `true`. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies).

**JSON example:**

` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ &quot;user:mike@example.com", &quot;group:admins@example.com", "domain:google.com", &quot;serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ &quot;user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01T00:00:00.000Z')", } } ], "etag": "BwWWja0YfJA=", "version": 3 } `

**YAML example:**

` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01T00:00:00.000Z') etag: BwWWja0YfJA= version: 3 `

For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #audit_configs
    
    
    def audit_configs() -> ::Array<::Google::Iam::V1::AuditConfig>

**Returns**

  * (::Array<[::Google::Iam::V1::AuditConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-v1/latest/Google-Iam-V1-AuditConfig)>) — Specifies cloud audit logging configuration for this policy. 



### #audit_configs=
    
    
    def audit_configs=(value) -> ::Array<::Google::Iam::V1::AuditConfig>

**Parameter**

  * **value** (::Array<[::Google::Iam::V1::AuditConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-v1/latest/Google-Iam-V1-AuditConfig)>) — Specifies cloud audit logging configuration for this policy. 



**Returns**

  * (::Array<[::Google::Iam::V1::AuditConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-v1/latest/Google-Iam-V1-AuditConfig)>) — Specifies cloud audit logging configuration for this policy. 



### #bindings
    
    
    def bindings() -> ::Array<::Google::Iam::V1::Binding>

**Returns**

  * (::Array<[::Google::Iam::V1::Binding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-v1/latest/Google-Iam-V1-Binding)>) — Associates a list of `members`, or principals, with a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one principal.

The `bindings` in a `Policy` can refer to up to 1,500 principals; up to 250 of these principals can be Google groups. Each occurrence of a principal counts towards these limits. For example, if the `bindings` grant 50 different roles to `user:alice@example.com`, and not to any other principal, then you can add another 1,450 principals to the `bindings` in the `Policy`. 




### #bindings=
    
    
    def bindings=(value) -> ::Array<::Google::Iam::V1::Binding>

**Parameter**

  * **value** (::Array<[::Google::Iam::V1::Binding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-v1/latest/Google-Iam-V1-Binding)>) — Associates a list of `members`, or principals, with a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one principal.

The `bindings` in a `Policy` can refer to up to 1,500 principals; up to 250 of these principals can be Google groups. Each occurrence of a principal counts towards these limits. For example, if the `bindings` grant 50 different roles to `user:alice@example.com`, and not to any other principal, then you can add another 1,450 principals to the `bindings` in the `Policy`. 




**Returns**

  * (::Array<[::Google::Iam::V1::Binding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-v1/latest/Google-Iam-V1-Binding)>) — Associates a list of `members`, or principals, with a `role`. Optionally, may specify a `condition` that determines how and when the `bindings` are applied. Each of the `bindings` must contain at least one principal.

The `bindings` in a `Policy` can refer to up to 1,500 principals; up to 250 of these principals can be Google groups. Each occurrence of a principal counts towards these limits. For example, if the `bindings` grant 50 different roles to `user:alice@example.com`, and not to any other principal, then you can add another 1,450 principals to the `bindings` in the `Policy`. 




### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy.

**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. 




### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy.

**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. 




**Returns**

  * (::String) — `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform policy updates in order to avoid race conditions: An `etag` is returned in the response to `getIamPolicy`, and systems are expected to put that etag in the request to `setIamPolicy` to ensure that their change will be applied to the same version of the policy.

**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost. 




### #version
    
    
    def version() -> ::Integer

**Returns**

  * (::Integer) — Specifies the format of the policy.

Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected.

Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations:

    * Getting a policy that includes a conditional role binding
    * Adding a conditional role binding to a policy
    * Changing a conditional role binding in a policy
    * Removing any role binding, with or without a condition, from a policy that includes conditions

**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.

If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.

To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). 




### #version=
    
    
    def version=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Specifies the format of the policy.

Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected.

Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations:

    * Getting a policy that includes a conditional role binding
    * Adding a conditional role binding to a policy
    * Changing a conditional role binding in a policy
    * Removing any role binding, with or without a condition, from a policy that includes conditions

**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.

If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.

To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). 




**Returns**

  * (::Integer) — Specifies the format of the policy.

Valid values are `0`, `1`, and `3`. Requests that specify an invalid value are rejected.

Any operation that affects conditional role bindings must specify version `3`. This requirement applies to the following operations:

    * Getting a policy that includes a conditional role binding
    * Adding a conditional role binding to a policy
    * Changing a conditional role binding in a policy
    * Removing any role binding, with or without a condition, from a policy that includes conditions

**Important:** If you use IAM Conditions, you must include the `etag` field whenever you call `setIamPolicy`. If you omit this field, then IAM allows you to overwrite a version `3` policy with a version `1` policy, and all of the conditions in the version `3` policy are lost.

If a policy does not include any conditions, operations on that policy may specify any valid version or leave the field unset.

To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
