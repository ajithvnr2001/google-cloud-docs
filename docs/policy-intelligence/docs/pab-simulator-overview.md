---
url: https://docs.cloud.google.com/policy-intelligence/docs/pab-simulator-overview/
title: Policy Simulator for Principal Access Boundary policies \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:56.929962+00:00
---

# Policy Simulator for Principal Access Boundary policies  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/pab-simulator-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Policy Simulator for Principal Access Boundary policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Policy Simulator for Principal Access Boundary (PAB) policies lets you see how a change to a [Principal Access Boundary policy](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies) or [binding](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#binding) might affect your principals' access before you commit to making the change. You can use Policy Simulator to help you understand the potential impact of a change to a Principal Access Boundary policy or binding before you apply it.

This feature only evaluates access based on Principal Access Boundary policies and policy bindings.

To learn how to simulate changes to other policy types, see the following:

  * [Policy Simulator for allow policies](https://docs.cloud.google.com/policy-intelligence/docs/iam-simulator-overview)
  * [Policy Simulator for deny policies](https://docs.cloud.google.com/policy-intelligence/docs/deny-simulator-overview)
  * [Policy Simulator for organization policies](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies)



## How Policy Simulator for Principal Access Boundary policies works

Policy Simulator for Principal Access Boundary policies helps you determine how a change to a Principal Access Boundary policy or policy binding affects access for principals in your organization.

When you run a simulation for a Principal Access Boundary policy or policy binding, Policy Simulator does the following:

  * Reviews access logs from the organization that were generated during the replay period in the context of the current Principal Access Boundary policies and bindings and the simulated Principal Access Boundary policy or binding.

  * Returns a series of _access changes_. These access changes show which access attempts from the logs are likely to have different results if you applied the simulated policy or binding.




To learn more about the access changes that Policy Simulator returns, see Policy Simulator results.

### Replay period

The replay period is the time that Policy Simulator gets access logs for when running a simulation. Access logs that occur before the first day of the replay period or after the last day of the replay period aren't included in the simulation. The replay period is 90 days. If the organization resource has existed for less than that amount of time, Policy Simulator retrieves all access attempts since the organization was created. The replay window is also [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency). This means that, when you run a simulation, some data might be fresher than other data. However, eventually, all the data will have the same freshness. With eventual consistency, the replay period typically ends in a few days but can end up to up to 15 days earlier. The simulation results show the exact replay window. Access logs from after this period aren't included. 

## Policy Simulator results

Policy Simulator for Principal Access Boundary reports the impact of a proposed change to a Principal Access Boundary policy or binding as a list of access changes. An access change represents an access attempt from the replay period that would likely have a different result if the simulated policy were applied.

For each access change, Policy Simulator also reports the following information:

  * The principal, permission, and, if available, resource involved in the access attempt.
  * The number of days during the replay period that the principal tried to use the permission to access the resource. This total includes only the access attempts that have the same result as the most recent access attempt.
  * The date of the most recent access attempt.



### Access changes

An access change indicates that, based on the relevant Principal Access Boundary policies, a user's access is likely to change if you apply the simulated policy or binding. Access changes can either be _access gained_ or _access revoked_.

When calculating access changes, Policy Simulator for Principal Access Boundary only evaluates Principal Access Boundary policies and bindings. It doesn't evaluate other policy types.

Policy Simulator calculates access changes using the following information:

  * The result of the most recent access attempt
  * The impact of the current Principal Access Boundary policies and bindings
  * The impact of the proposed Principal Access Boundary policies and bindings



For access to be _gained_ , all of the following must be true:

  * The most recent access attempt was blocked
  * Access is blocked by the current Principal Access Boundary policies and bindings
  * Access is not blocked by the proposed Principal Access Boundary policies and bindings



For access to be _revoked_ , all of the following must be true:

  * The most recent access attempt was not blocked
  * Access is not blocked by the current Principal Access Boundary policies and bindings
  * Access is blocked by the proposed Principal Access Boundary policies and bindings



A set of Principal Access Boundary policies and bindings block a principal's access if _all_ of the following are true:

  * Principal Access Boundary policies do affect the principal's access. In other words, the principal is subject to at least one Principal Access Boundary policy that has an [enforcement version](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#blocked-permissions) that supports the permission in the request. 
  * None of the Principal Access Boundary policies that the principal is subject to include the resource. 



A set of Principal Access Boundary policies and bindings don't block a principal's access if _any_ of the following are true:

  * Principal Access Boundary policies don't affect the principal's access. In other words, the principal isn't subject to any Principal Access Boundary policies that have an [enforcement version](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#blocked-permissions) that supports the permission in the request. 
  * At least one of the Principal Access Boundary policies that the principal is subject to includes the resource. 



## Errors

The following errors can cause a simulation to fail:

  * **Timeout** : The simulation took too long to run and timed out. To resolve, try running the simulation again.
  * **Invalid simulation construction** : The proposed Principal Access Boundary policy or Principal Access Boundary policy binding is invalid. For example, the proposed policy has an invalid condition expression, or the proposed binding is for a principal set that is already bound to the [maximum number of policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#binding). To resolve, correct the policy or binding and try again.
  * **Permission denied** : You don't have permission to run a simulation. To resolve, ensure that you're granted the [required roles](https://docs.cloud.google.com/policy-intelligence/docs/simulate-pab-policies#required-roles) and try again.



## Supported principal types

Policy Simulator for Principal Access Boundary policies only reviews access logs for the following types of principals:

  * Google Accounts
  * Service accounts



When simulating Principal Access Boundary policies and bindings, Policy Simulator doesn't review access logs for any other principal types. As a result, it doesn't report whether the proposed changes to your policies or bindings will affect those principals' access.

### Simulating Credential Access Boundaries

You can use Credential Access Boundaries to _downscope_ , or restrict, the IAM permissions that a short-lived credential can use to access Cloud Storage resources. To downscope permissions, a user or service account (the token broker) defines the available permissions on a set of resources in a downscoped access token and then provides the access token to another user or service account (the token consumer).

The token broker must have a role that includes the permissions granted to the token consumer with a downscoped access token. Blocking the user from accessing that resource using a Principal Access Boundary also blocks access for the token consumer. However, Policy Simulator doesn't evaluate how changes to the token broker's permissions affect the token consumer's access.

For example, consider a user who has been granted the **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`) role on a resource using a downscoped access token created with a Credential Access Boundary.

  * If you simulate blocking the **Storage Legacy Bucket Reader** role from that user using a Principal Access Boundary, Policy Simulator fails to report a loss of access.

  * If you simulate blocking the **Storage Legacy Bucket Reader** role from the token broker using a Principal Access Boundary, Policy Simulator fails to report a loss of access for the user. Similarly, if the token broker's access isn't used within 90 days, their access isn't included in the simulation.




For more information, see [Credential Access Boundaries for Cloud Storage](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials).

## What's next

  * Learn how to [simulate a change to a Principal Access Boundary policy or binding](https://docs.cloud.google.com/policy-intelligence/docs/simulate-pab-policies).
  * Explore other [Policy Intelligence tools](https://docs.cloud.google.com/policy-intelligence/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
