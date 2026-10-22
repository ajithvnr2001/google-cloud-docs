---
url: https://docs.cloud.google.com/policy-intelligence/docs/secure-apis-vpc-sc/
title: Help secure Policy Intelligence APIs with VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:02.926262+00:00
---

# Help secure Policy Intelligence APIs with VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/secure-apis-vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/policy-intelligence/docs/apis)



Send feedback 

#  Help secure Policy Intelligence APIs with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

With VPC Service Controls, you can create _perimeters_ , which are boundaries around your Google Cloud resources. You can then define security policies that help prevent access to supported services from outside of the perimeter. For more information about VPC Service Controls, see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

You can use VPC Service Controls to help secure the following Policy Intelligence APIs:

  * Policy Troubleshooter API
  * Policy Simulator API



## Help secure the Policy Troubleshooter API

**Preview — Securing the Policy Troubleshooter API with VPC Service Controls**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can help secure policy troubleshooting by using VPC Service Controls.

When you restrict the Policy Troubleshooter API with a perimeter, principals can troubleshoot IAM policies only if all resources involved in the request are in the same perimeter. There are usually two resources involved in a troubleshooting request:

  * **The resource you're troubleshooting access for.** This resource can be any type. You explicitly specify this resource when you troubleshoot an IAM policy.

  * **The resource you're using to troubleshoot access.** This resource must be a project, folder, or organization. In the Google Cloud console and gcloud CLI, this resource is inferred based on the project, folder, or organization that you have selected. In the REST API, you specify this resource using the `x-goog-user-project` header.

This resource can be the same as the resource that you're troubleshooting access for, but it doesn't need to be.




If these resources aren't in the same perimeter, the request fails.

For more details about how VPC Service Controls works with Policy Troubleshooter, see the [Policy Troubleshooter entry in the VPC Service Controls supported products table](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iam_policy_troubleshooter).

## Help secure the Policy Simulator API

You can restrict the Policy Simulator API with a perimeter when simulating organization policies or allow and deny policies.

Principals can simulate organization policies as expected inside service perimeters.

VPC Service Controls doesn't support adding folder or organization resources to service perimeters. Therefore, you cannot use VPC Service Controls to protect folder-level and organization-level deny policy simulations. Deny policy simulations on resources outside of the service perimeter still return complete results, and deny policy simulations on project-level resources are protected.

Principals can simulate allow policies only if certain resources involved in the simulation are in the same perimeter. There are several resources involved in an allow policy simulation:

  * **The resource whose allow policy you're simulating.** This resource is also called the _target resource_. In the Google Cloud console, this is the resource whose allow policy you're editing. In the gcloud CLI and REST API, you explicitly specify this resource when you simulate an allow policy.

  * **The project, folder, or organization that creates and runs the simulation.** This resource is also called the _host resource_. In the Google Cloud console and gcloud CLI, this resource is inferred based on the project, folder, or organization you have selected. In the REST API, you specify this resource using the `x-goog-user-project` header.

This resource can be the same as the target resource, but it doesn't need to be.

  * **The resource that provides access logs for the simulation.** In a simulation, there is always one resource that provides access logs for the simulation. This resource varies depending on the target resource type:

    * If you are simulating an allow policy for a project or organization, Policy Simulator retrieves the access logs for that project or organization.
    * If you are simulating an allow policy for a different type of resource, Policy Simulator retrieves the access logs for that resource's parent project or organization.
    * If you are simulating multiple resources' allow policies at once, Policy Simulator retrieves the access logs for the resources' nearest common project or organization.
  * **All supported resources with relevant allow policies.** When Policy Simulator runs a simulation, it considers all allow policies that might impact the user's access, including allow policies on the target resource's ancestor and descendant resources. As a result, these ancestor and descendant resources are also involved in simulations.




If the target resource and the host resource aren't in the same perimeter, the request fails.

If the target resource and the resource that provides access logs for the simulation aren't in the same perimeter, the request fails.

If the target resource and some supported resources with relevant allow policies aren't in the same perimeter, the requests succeeds, but the results might be incomplete. For example, if you're simulating a policy for a project in a perimeter, the results won't include the allow policy of the project's parent organization, because organizations are always outside of VPC Service Controls perimeters. To get more complete results, you can configure [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the perimeter.

For more details about how VPC Service Controls works with Policy Simulator, see the [Policy Simulator entry in the VPC Service Controls supported products table](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_iam_policy_simulator).

## What's next

  * Learn how to [create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
