---
url: https://docs.cloud.google.com/iam/docs/policy-types/
title: IAM policy types \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:07.099462+00:00
---

# IAM policy types  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/policy-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  IAM policy types Stay organized with collections  Save and categorize content based on your preferences. 

Identity and Access Management (IAM) offers several types of policies to help you control which resources principals can access. This page helps you understand the differences between how you use and manage these policy types.

## Types of IAM policies in Google Cloud

IAM offers the following types of policies:

  * Allow policies
  * Deny policies
  * Principal Access Boundary (PAB) policies
  * Access policies



The following table summarizes the differences between these policy types:

Policy | Policy function | API used to manage the policy | Relationship between policies and targets | Method of attaching policies to target | Policy's parent resource  
---|---|---|---|---|---  
Allow policies | Grant principals access to resources | The API for the resource that you want to manage allow policies for |  One-to-one relationship Each allow policy is attached to one resource; each resource can only have one allow policy | Specify resource when creating the policy | Same as the resource that the allow policy is attached to  
Deny policies | Ensure that principals can't use specific permissions |  The [IAM v2 API](https://docs.cloud.google.com/iam/docs/reference/libraries#iam-v2) |  One-to-many relationship Each deny policy is attached to one resource; each resource can have up to 500 deny policies  | Specify resource when creating the deny policy | Same as the resource that the deny policy is attached to  
PAB policies | Restrict the resources a principal is eligible to access |  The [IAM v3 API](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies) |  Many-to-many relationship Each PAB policy can be attached to an unlimited number of principal sets; each principal set can have up to 10 PAB policies bound to it  |  Create a policy binding that attaches the PAB policy to a principal set  | The organization  
Access policies | Grant or deny principals access to resources for supported services |  The [IAM v3 API](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.accessPolicies) |  Many-to-many relationship Each access policy can be attached to up to 5 resources; each resource can have up to 5 access policies bound to it  |  Create an access policy binding that attaches the access policy to the resource  |  The project, folder, or organization where the access policy is created   
  
The following sections provide details about each policy type.

## Policies to grant access to principals

To grant principals access to resources, use one of the following policies:

  * Use allow policies to grant access to any resource type.
  * Use access policies to grant access to Eventarc resources.



_Allow policies_ let you grant access to resources in Google Cloud. Allow policies are made up of role bindings and metadata. Role bindings specify which principals should have a certain role on the resource.

Allow policies are always attached to a single resource. After you attach an allow policy to a resource, the policy is [inherited](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control) by that resource's descendants.

To create and apply an allow policy, you identify a resource that [accepts allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies), then use that resource's `setIamPolicy` method to create the allow policy. All principals in the allow policy are granted the specified roles on the resource and all of the resource's descendants. Each resource can have only one allow policy attached to it.

For more information about allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

_Access policies_ let you control access to Eventarc resources. Access policies can both allow and deny access to resources. To create and apply an access policy, you create an access policy, and then create a policy binding to connect that policy to a project with Eventarc resources. 

Each policy binding binds one access policy to one resource. An access policy can be bound to up to 5 resources. Each resource can have up to 5 access policies bound to it. When an access policy is deleted, all of the policy bindings related to that policy are also deleted.

To learn more about using access policies to control access to Eventarc resources, see the [Eventarc documentation](https://docs.cloud.google.com/eventarc/advanced/docs/control-publishing-access). 

## Policies to deny access to principals

To deny principals access to resources, use one of the following:

  * Use deny policies to deny access for any resource type.
  * Use access policies to deny access for Eventarc resources.



_Deny policies_ , like allow policies, are always attached to a single resource. You can attach a deny policy to a project, folder, or organization. This project, folder, or organization also acts as the policy's parent in the resource hierarchy. After you attach a deny policy to a resource, the policy is [inherited](https://docs.cloud.google.com/iam/docs/deny-overview#inheritance) by that resource's descendants.

To create and apply deny policies, you use the IAM v2 API. When you create a deny policy, you specify the resource that the deny policy is attached to. All principals in the deny policy are prevented from using the specified permissions to access that resource and any of that resource's descendants. Each resource can have up to 500 deny policies attached to it.

For more information about deny policies, see [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview).

_Access policies_ let you control access to Eventarc resources. Access policies can both allow and deny access to resources. To create and apply an access policy, you create an access policy, and then create a policy binding to connect that policy to a project with Eventarc resources. 

Each policy binding binds one access policy to one resource. An access policy can be bound to up to 5 resources. Each resource can have up to 5 access policies bound to it. When an access policy is deleted, all of the policy bindings related to that policy are also deleted.

To learn more about using access policies to control access to Eventarc resources, see the [Eventarc documentation](https://docs.cloud.google.com/eventarc/advanced/docs/control-publishing-access). 

## Policies to restrict the resources a principal can access

To restrict the resources that a principal is eligible to access, use a Principal Access Boundary policy. Principal Access Boundary policies are available in the [IAM v3 API](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/organizations.locations.principalAccessBoundaryPolicies).

To create and apply a Principal Access Boundary policy, you create a Principal Access Boundary policy, and then create a policy binding to connect that policy to a principal set.

Principal Access Boundary policies are always children of your organization. Policy bindings for Principal Access Boundary policies are children of the project, folder, or organization that is closest to the principal set referenced in the policy binding.

Each policy binding binds one Principal Access Boundary policy to one principal set. A Principal Access Boundary policy can be bound to any number of principal sets. Each principal set can have up to 10 Principal Access Boundary policies bound to it. When a Principal Access Boundary policy is deleted, all of the policy bindings related to that policy are also deleted.

For more information about Principal Access Boundary policies, see [Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies).

## Policy evaluation

When a principal tries to access a resource, IAM evaluates all relevant allow, deny, and Principal Access Boundary policies to see if the principal is allowed to access the resource. If any of these policies indicates that the principal shouldn't be able to access the resource, then IAM prevents access.

In reality, IAM evaluates all policy types simultaneously, then compiles the results to determine whether the principal can access the resource. However, it can be helpful to think of this policy evaluation taking place in the following stages:

  1. IAM [evaluates the Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#policy-evaluation) that the principal is subject to. These policies indicate whether the principal is eligible to access the resource. 

     * If the principal isn't eligible to access the resource, then IAM prevents them from accessing the resource. 
     * If the principal is eligible to access the resource, then IAM continues to the next step. 
     * If the principal isn't subject to any Principal Access Boundary policies, then IAM continues to the next step. 
  2. IAM checks all relevant deny policies to see if the principal has been denied the permission. Relevant deny policies are the deny policies attached to the resource, as well as any [inherited deny policies](https://docs.cloud.google.com/iam/docs/deny-overview#inheritance). 

For Eventarc resources, IAM also evaluates any access policies with the `DENY` action. If IAM fails to evaluate access policies, then it ignores them and continues with the evaluation. 
     * If _any_ of these deny policies prevent the principal from using a required permission, then IAM prevents them from accessing the resource. 
     * If no deny policies prevent the principal from using a required permission, then IAM continues to the next step. 
  3. IAM checks all relevant allow policies to see if the principal has the required permissions. Relevant allow policies are the allow policies attached to the resource, as well as any [inherited allow policies](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control). 

For Eventarc resources, IAM also evaluates any access policies with the `ALLOW` action. If IAM fails to evaluate access policies, then it ignores them and continues with the evaluation. 
     * If the principal does not have the required permissions, then IAM prevents them from accessing the resource. 
     * If the principal has the required permissions, then IAM lets them access the resource. 



The following diagram shows this policy evaluation flow:

![The IAM policy evaluation flow](https://docs.cloud.google.com/static/iam/img/iam-policy-evaluation.svg)

![The IAM policy evaluation flow](https://docs.cloud.google.com/static/iam/img/iam-policy-evaluation.svg)

## What's next

  * Learn more about [allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).
  * Learn more about [deny policies](https://docs.cloud.google.com/iam/docs/deny-overview). 
  * Learn more about [Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
