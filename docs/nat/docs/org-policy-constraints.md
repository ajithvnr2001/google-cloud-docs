---
url: https://docs.cloud.google.com/nat/docs/org-policy-constraints/
title: Organization policy constraints \u00a0|\u00a0 Cloud NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:46.788658+00:00
---

# Organization policy constraints  |  Cloud NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/docs/org-policy-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Guides ](https://docs.cloud.google.com/nat/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Organization policy constraints

This page provides information about the [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) constraints that you can configure for Cloud NAT.

Network administrators can create Cloud NAT configurations and specify which subnetworks (subnets) can use the gateway. By default, there are no limits to what subnets the administrator creates or which of them can use a Cloud NAT configuration.

An Organization Policy Administrator (`roles/orgpolicy.policyAdmin`) can use the [`constraints/compute.restrictCloudNATUsage`](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints#constraints/compute.restrictCloudNATUsage) constraint to limit which subnets can use Cloud NAT.

You create and enforce organizational constraints in an organization policy.

## Prerequisites

### IAM permissions

  * The person creating the constraints must have the [roles/orgpolicy.policyAdmin](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy) role.
  * If using Shared VPC, the user role must be in the host project.



### Organization policy background

If you have not worked with organization policy constraints before, first review the following documentation:

  * [Understanding constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints)
  * [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy)



## Planning your constraints

To define which subnetworks can use Cloud NAT, you specify `allowedValues` or `deniedValues` in your organization policy. These values can be scoped to the following levels of the resource hierarchy, where the placeholders represent your target resource identifiers and names:

  * **Organization** : `under:organizations/ORGANIZATION_ID`
  * **Folder** : `under:folders/FOLDER_ID`
  * **Project** : `under:projects/PROJECT_ID`
  * **Subnetwork** : `projects/PROJECT_ID/regions/REGION_NAME/subnetworks/SUBNETWORK_NAME`



By default, a constraint created at a node is inherited by all child nodes. However, an Organization Policy Administrator for a given folder can decide if a given folder inherits from its parents, so inheritance is not automatic. For more information, see [Inheritance](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy#inheritance) in _Understanding hierarchy evaluation_.

Constraints are not applied retroactively. Existing configurations continue to work even if they violate the constraints.

Constraints consist of `allow` and `deny` settings.

### Interaction between allowed and denied values

  * If a `restrictCloudNatUsage` constraint is configured but neither `allowedValues` nor `deniedValues` is specified, everything is allowed.
  * If `allowedValues` is configured and `deniedValues` is not configured, everything not specified in `allowedValues` is denied.
  * If `deniedValues` is configured and `allowedValues` is not configured, everything not specified in `deniedValues` is allowed.
  * If both `allowedValues` and `deniedValues` are configured, everything not specified in `allowedValues` is denied.
  * If two values conflict, `deniedValues` takes precedence.



### Interaction between subnets and gateways

Constraints do not prevent subnets from using a NAT gateway. Instead, constraints prevent a configuration that would violate the constraint by preventing the creation of either a gateway or a subnet.

#### Example 1: Trying to create a subnet that violates a `deny` rule

  1. A gateway exists in a region.
  2. The gateway is configured to allow all subnets in a region to use it.
  3. A single subnet (`subnet-1`) exists in the region.
  4. A constraint is created so that only `subnet-1` can use the gateway.
  5. Administrators are not able to create more subnets in that network in that region. The constraint prevents the creation of subnets that _would_ be able to use the gateway. If the new subnets should exist, then the Organization Policy Administrator can add these subnets to the list of permitted subnets.



#### Example 2: Trying to create a gateway that violates a `deny` rule

  1. Two subnets (`subnet-1` and `subnet-2`) exist in a region.
  2. A constraint exists that only allows `subnet-1` to use a gateway.
  3. Administrators are not able to create a gateway that is open to all subnets in the region. Instead, either they have to create a gateway that only serves `subnet-1`, or the Organization Policy Administrator has to add `subnet-2` to the list of permitted subnets.



## Creating your constraints

To create an organization policy with a particular constraint, see [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints).

## What's next

  * Learn about how to [use custom organization policies](https://docs.cloud.google.com/nat/docs/custom-constraints)
  * [Set up and manage network address translation with Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation)
  * [Set up and manage network address translation with Private NAT](https://docs.cloud.google.com/nat/docs/set-up-private-nat)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
