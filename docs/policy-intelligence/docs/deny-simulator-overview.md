---
url: https://docs.cloud.google.com/policy-intelligence/docs/deny-simulator-overview/
title: Policy Simulator for deny policies \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:44.846062+00:00
---

# Policy Simulator for deny policies  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/deny-simulator-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Policy Simulator for deny policies Stay organized with collections  Save and categorize content based on your preferences. 

Policy Simulator for deny policies lets you see how a change to an IAM [deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) might affect a principal's access before you commit to making the change. You can use Policy Simulator to ensure that the changes you're making won't cause a principal to lose access that they need.

This feature only evaluates deny policies. To learn how to simulate other policy types, see the following:

  * [Policy Simulator for organization policies](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies)
  * [Policy Simulator for allow policies](https://docs.cloud.google.com/policy-intelligence/docs/iam-simulator-overview)
  * [Policy Simulator for Principal Access Boundary policies](https://docs.cloud.google.com/policy-intelligence/docs/pab-simulator-overview)



## How Policy Simulator for deny policies works

Policy Simulator for deny policies helps you determine whether a change to a deny policy will block access that your principals are using.

When you run a simulation for a deny policy, Policy Simulator does the following:

  1. Retrieves access logs for the organization that were generated during the replay period. The replay period is 90 days.

If the organization has not existed for more than 90 days, then Policy Simulator retrieves all access logs since the organization was created.

  2. Determines which access logs are relevant to the simulation. Relevant access logs are all access logs that represent a principal's most recent attempt to use a permission to access a resource.

  3. For each relevant access log, determines whether the current deny policies, along with the proposed changes, would permit the attempted access. This process is called _replaying_ the access attempts.

  4. For each access log, compares the access state from the replay with the access state in the access logs. Then, Policy Simulator reports any historical access attempts that weren't blocked in the access log, but were blocked in the replay. These differences, which are called _access changes_ , show which access attempts would have been blocked if the simulated deny policy had been in place at the time of the attempt.

**Note:** The access state in an access log might not reflect the current access state. In these cases, Policy Simulator always compares the results of the replay to the result from the access log, _not_ to the current access state.



### Replay period

The replay period is the time that Policy Simulator gets access logs for when running a simulation. Access logs that occur before the first day of the replay period or after the last day of the replay period aren't included in the simulation. The replay period is 90 days. If the organization resource has existed for less than that amount of time, Policy Simulator retrieves all access attempts since the organization was created. The replay window is also [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency). This means that, when you run a simulation, some data might be fresher than other data. However, eventually, all the data will have the same freshness. With eventual consistency, the replay period typically ends in a few days but can end up to up to 15 days earlier. The simulation results show the exact replay window. Access logs from after this period aren't included. 

## Policy Simulator results

Policy Simulator reports the impact of a proposed change to a deny policy as a list of _access changes_. For deny policies, the only type of access change that Policy Simulator reports is the **Access revoked** access change.

Policy Simulator reports that access is revoked if the following are true:

  * The principal's most recent attempt to access the resource was successful
  * The proposed changes or another deny policy block the principal's access to the resource



For each access change, Policy Simulator also reports the following information:

  * The principal, resource, and permission involved in the access attempt.
  * The number of days during the replay period that the principal tried to use the permission to access the resource. This total includes only the access attempts that have the same result as the most recent access attempt.
  * The date of the most recent access attempt.



## Errors

The following errors can cause a simulation to fail:

  * **Maximum concurrent simulations exceeded** : The user already has 50 in-progress simulations, which is the maximum number of in-progress simulations that a user can have. To resolve, wait for one of the in-progress simulations to complete, then try running the simulation again.
  * **Timeout** : The simulation took too long to run and timed out. Any simulation that takes more than 24 hours times out automatically. To resolve, try running the simulation again or reducing the size of the simulation.
  * **Invalid simulation construction** : The proposed deny policy is invalid or contains unsupported deny rules. An example of an invalid policy is one that contains an invalid condition expression. An example of an unsupported deny rule is one that uses workforce identity principal identifiers. To resolve, correct the policy and try again.
  * **Permission denied** : You don't have permission to run a simulation. To resolve, ensure that you're granted the [required roles](https://docs.cloud.google.com/policy-intelligence/docs/simulate-deny-policies#required-roles) and try again.

**Note:** Unsupported deny policies are ignored during simulations of deny policies elsewhere in the resource hierarchy. For example, if you successfully simulate a valid deny policy on a resource and there's an unsupported deny policy on an ancestor resource, that unsupported deny policy is not evaluated by the simulation. The result of the simulation reflects the valid deny policy, and ignores the unsupported deny policy.

## Supported principal types

Policy Simulator for deny policies only reviews access logs for the following types of principals:

  * Google Workspace Accounts
  * Service accounts
  * [Service account principal sets](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny-service-account-principal-sets) for projects, folders, and organizations
  * Service agents
  * [Service agent principal sets](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny-service-agent-principal-sets) for projects, folders, and organizations



When simulating deny policies, Policy Simulator doesn't review access logs for any other principal types, including those based on federated identities in a workload identity pool. As a result, Policy Simulator doesn't report whether the proposed changes to your policies or bindings affect those principals' access.

### Simulating Credential Access Boundaries

You can use Credential Access Boundaries to _downscope_ , or restrict, the IAM permissions that a short-lived credential can use to access Cloud Storage resources. To downscope permissions, a user or service account (the token broker) defines the available permissions on a set of resources in a downscoped access token and then provides the access token to another user or service account (the token consumer).

The token broker must have a role that includes the permissions granted to the token consumer with a downscoped access token. Denying that role on the token broker also removes access from the token consumer. However, Policy Simulator doesn't evaluate how changes to the token broker's permissions affect the token consumer's access.

For example, consider a user who has been granted the **Storage Legacy Bucket Reader** (`roles/storage.legacyBucketReader`) role on a resource using a downscoped access token created with a Credential Access Boundary.

  * If you simulate denying the **Storage Legacy Bucket Reader** role on that user, Policy Simulator fails to report a loss of access.

  * If you simulate denying the **Storage Legacy Bucket Reader** role on the token broker, Policy Simulator fails to report a loss of access for the user. Similarly, if the token broker's access isn't used within 90 days, their access isn't included in the simulation.




For more information, see [Credential Access Boundaries for Cloud Storage](https://docs.cloud.google.com/iam/docs/downscoping-short-lived-credentials).

## What's next

  * Learn how to [simulate a change to a deny policy](https://docs.cloud.google.com/policy-intelligence/docs/simulate-deny-policies).
  * Explore other [Policy Intelligence tools](https://docs.cloud.google.com/policy-intelligence/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
