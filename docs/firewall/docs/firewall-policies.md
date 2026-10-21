---
url: https://docs.cloud.google.com/firewall/docs/firewall-policies/
title: Hierarchical firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:36.253343+00:00
---

# Hierarchical firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Hierarchical firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

_Hierarchical firewall policies_ let you create and enforce a consistent firewall policy across your organization. You can assign hierarchical firewall policies to the organization as a whole or to individual folders. These policies contain rules that can explicitly deny or allow connections, as do [Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls). In addition, hierarchical firewall policy rules can delegate evaluation to lower-level policies or VPC network firewall rules with a `goto_next` action.

Lower-level rules cannot override a rule from a higher place in the resource hierarchy. This lets organization-wide admins manage critical firewall rules in one place.

## Specifications

  * Hierarchical firewall policies are created at the organization and folder level. Creating a policy does not automatically apply the rules to the [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) or [folder](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders).
  * Policies, once created, can be applied to (_associated_ with) any resources in the organization.
  * Hierarchical firewall policies are containers for firewall rules. When you associate a policy with the organization or a folder, all rules are immediately applied. You can swap policies for a resource, which atomically swaps all the firewall rules applied to virtual machine (VM) instances under that resource.
  * Rule evaluation is hierarchical based on resource hierarchy. All rules associated with the organization are evaluated, followed by those of the first level of folders.
  * Hierarchical firewall policy rules have a new `goto_next` action that you can use to delegate connection evaluation to lower levels of the hierarchy.


  * Hierarchical firewall policy rules can be used to configure Layer 7 inspection of the matched traffic, such as the [URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering) and the [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention).

You create a firewall policy rule by using the `apply_security_profile_group` action and name of the [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups). The traffic matching the firewall policy rule is intercepted and transparently forwarded to the firewall endpoint for Layer 7 inspection, and back. To learn how to create a firewall policy rule, see [Firewall policy rule tasks](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks).



  * Hierarchical firewall policy rules can be targeted to specific VPC networks and VMs by using target resources for networks and target service accounts for VMs. This lets you create exceptions for groups of VMs. Hierarchical firewall policy rules don't support targeting by instance tags.
  * Hierarchical firewall policies don't support VPC networks that use a Remote Direct Memory Access (RDMA) network profile, such as the `RDMA_ROCE_POLICY` policy type. For more information, see [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce#specifications).
  * A hierarchical firewall policy rule can include either IPv4 or IPv6 ranges, but not both.
  * To help with compliance and debugging, firewall rules applied to a VM instance can be audited by using the VPC network details page and the VM instance's network interface details page.



## Resource hierarchy

You create and apply firewall policies as separate steps. You can create and apply firewall policies at the organization or folder level of the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). A firewall policy rule can block connections, allow connections, or defer firewall rule evaluation to lower-level folders or VPC firewall rules defined in VPC networks.

  * [Organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) is the top-level resource in the resource hierarchy in Google Cloud where you can create or associate hierarchical firewall policies. All folders and VPC networks in the organization inherit this policy.

  * [Folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) are mid-level resources in the Google Cloud resource hierarchy, between the organization and projects, where you can create or assign hierarchical firewall policies. All folders and VPC networks in a folder inherit its associated policy.

  * A project lives under a folder or the organization. You can move projects between resources in an organization. Projects contain VPC networks. Hierarchical firewall policies cannot be assigned to projects, only to the organization or folders.

  * A VPC network is the Google Cloud partition for isolated internal IP space communication. This is the level at which routes, network firewall policies, and traditional VPC firewall rules are specified and applied. Hierarchical firewall policy rules can override or delegate connection evaluation to [global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/network-firewall-policies).




By default, all hierarchical firewall policy rules apply to all VMs in all projects under the organization or folder where the policy is associated. However, you can restrict which VMs get a given rule by specifying [target networks or target service accounts](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets).

The levels of the hierarchy at which firewall rules can now be applied are represented in the following diagram. The yellow boxes represent hierarchical firewall policies that contain firewall rules, while the white boxes represent VPC firewall rules.

[ ![Hierarchical firewall policies containing rules \(yellow boxes\)
        at the organization and folder levels and VPC firewall
        rules at the VPC network level](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-1.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-1.svg) Hierarchical firewall policies containing rules (yellow boxes) are applied at the organization and folder levels. VPC firewall rules are applied at the VPC network level.**Note:** Hierarchical firewall policies are eventually consistent. If you move projects or folders, it might take a few minutes for hierarchical firewall policies to be applied.

## Hierarchical firewall policy details

Hierarchical firewall policy rules are defined in a firewall policy resource that acts as a container for firewall rules. The rules defined in a firewall policy are not enforced until the policy is associated with a resource (an organization or a folder).

A single policy can be associated with multiple resources. If you modify a rule in a policy, that rule change applies to all associated resources.

Only one firewall policy can be associated with a resource. Hierarchical firewall policy rules and VPC firewall rules are [evaluated in a well-defined order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).

A firewall policy that is not associated with any resource is an _unassociated_ hierarchical firewall policy.

### Policy names

When you create a new policy, Google Cloud automatically generates an ID for the policy. In addition, you also specify a _short name_ for the policy. When using the `gcloud` interface to update an existing policy, you can reference either the system-generated ID or a combination of the short name and your organization ID. When using the API to update the policy, you must provide the system-generated ID.

## Hierarchical firewall policy rule details

Hierarchical firewall policy rules work the same as [firewall policy rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details) and [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls), but there are a few differences:

  * Hierarchical firewall policies support target networks, while global network firewall policies don't. You can specify target networks to restrict a firewall policy rule to VMs in the specified networks. Specifying VPC networks in the rule gives you control over which networks are configured with that rule.

Combined with `goto_next` or `allow`, specifying target networks lets you create exceptions for specific networks when you want to define an otherwise restrictive policy.

  * Hierarchical firewall policies are organization-level resources, while global network firewall policies are project-level resources.

  * Rules in hierarchical firewall policies support secure tag keys as source secure tags or target secure tags. For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview).




## Predefined rules

When you create a hierarchical firewall policy, Cloud Next Generation Firewall (Cloud NGFW) adds predefined rules with the lowest priority to the policy. These rules are applied to any connections that don't match an explicitly defined rule in the policy, causing such connections to be passed down to lower-level policies or network rules.

To learn about the various types of predefined rules and their characteristics, see [Predefined rules for firewall policies](https://docs.cloud.google.com/firewall/docs/pre-defined-rules).

## Identity and Access Management (IAM) roles

**Note:** The preview releases of hierarchical firewall policies used the `compute.orgSecurityPolicyAdmin` and `compute.orgSecurityPolicyUser` IAM roles. These roles combined permissions for hierarchical firewall policies and Google Cloud Armor. To separate these permissions, we are migrating to the `compute.orgFirewallPolicyAdmin` and `compute.orgFirewallPolicyUser` roles for hierarchical firewall policies. The prior roles continue to work, but we recommend migrating to the new roles as soon as feasible.

IAM roles govern the following actions with regard to hierarchical firewall policies:

  * Creating a policy that lives at a particular resource
  * Associating a policy with a particular resource
  * Modifying an existing policy
  * Viewing the effective firewall rules for a particular network or VM



The following table describes which roles are necessary for each step:

Ability | Necessary role  
---|---  
Create a new hierarchical firewall policy  | [Organization Firewall Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyAdmin) (`roles/compute.orgFirewallPolicyAdmin`) on the resource where the policy will live  
Associate a policy with a resource  | [Organization Security Resource Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityResourceAdmin) (`roles/compute.orgSecurityResourceAdmin`) on the target resource, and either [Organization Firewall Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyAdmin) (`roles/compute.orgFirewallPolicyAdmin`) or [Organization Firewall Policy User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyUser) (`roles/compute.orgFirewallPolicyUser`) on the resource where the policy lives or on the policy itself  
Modify the policy by adding, updating, or deleting policy firewall rules  | [Organization Firewall Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyAdmin) (`roles/compute.orgFirewallPolicyAdmin`) either on the resource where the policy lives or on the policy itself  
Delete the policy  | [Organization Firewall Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyAdmin) (`roles/compute.orgFirewallPolicyAdmin`) either on the resource where the policy lives or on the policy itself  
View effective firewall rules for a VPC network  | Any of the following roles for the network:   
[Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  
[Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)  
[Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  
[Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)  
[Compute Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)   
View effective firewall rules for a VM in a network  | Any of the following roles for the VM:   
[Compute Instance Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  
[Instance Group Manager Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceGroupManagerServiceAgent) (`roles/compute.instanceGroupManagerServiceAgent`)  
[Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)  
[Compute Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)   
  
The following roles are relevant to hierarchical firewall policies.

Role name | Description  
---|---  
[Organization Firewall Policy Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyAdmin) (`roles/compute.orgFirewallPolicyAdmin`)  | Can be granted on a resource or on an individual policy. If granted at a resource, allows users to create, update, and delete hierarchical firewall policies and their rules. If granted on an individual policy, allows the user to update the policy rules, but not create or delete the policy. This role also allows the user to associate a policy with a resource if they also have the `compute.orgSecurityResourceAdmin` role on that resource.  
[Organization Security Resource Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityResourceAdmin) (`roles/compute.orgSecurityResourceAdmin`)  | Granted at the organization level or to a folder, allows folder-level administrators to associate a policy with that resource. Administrators must also have the `compute.orgFirewallPolicyUser` or `compute.orgFirewallPolicyAdmin` role on the resource that owns the policy or on the policy itself in order to make use of it.  
[Organization Firewall Policy User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyUser) (`roles/compute.orgFirewallPolicyUser`)  | Granted on a resource or on an individual policy, allows administrators to make use of the individual policy or policies associated with the resource. Users must also have the `compute.orgSecurityResourceAdmin` role on the target resource to associate a policy with that resource.  
[Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)  
  
[Compute Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)  
  
[Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)  
  
[Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  
| Allows users to view the firewall rules applied to the network or instance.  
Includes the `compute.networks.getEffectiveFirewalls` permission for networks and the `compute.instances.getEffectiveFirewalls` for instances.  
  
In the following example, Joe can create, modify, and delete any hierarchical firewall policy in the `policies` folder, but he cannot attach the hierarchical firewall policy to a folder because he does not have the `orgSecurityResourceAdmin` role on any folder.

However, because Joe granted Mary permissions to use `policy-1`, she can list and associate that hierarchical firewall policy with the `dev-projects` folder or any of its descendants. The `orgFirewallPolicyUser` role does not grant permission to associate the policies to any folders; the user must also have the `orgSecurityResourceAdmin` role on the target folder.

[ ![policy-1 example](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-4.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-4.svg) policy-1 example

## Manage hierarchical firewall policy resources

Because a hierarchical firewall policy only defines a set of firewall rules and not where they are applied, you can create these resources in a different part of the hierarchy from the resources that they apply to. This lets you associate a single hierarchical firewall policy resource with multiple folders in the organization.

In the following example, `policy-1` is applied to the `dev-projects` and `corp-projects` folders and so is enforced on all projects in those folders.

[ ![Policy location and association](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-3.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-3.svg) Policy location and association

### Modify a policy's rules

You can add, remove, and modify rules in a policy. Each change is done individually; there is no mechanism for batch updating rules in a policy. Changes are applied in roughly the order that the commands are executed, although this is not guaranteed.

If you are making extensive changes to a hierarchical firewall policy and need to ensure that they're applied at the same time, you can clone the policy to a temporary policy and assign the temporary policy to the same resources. You can then make your changes to the original, and then assign the original back to the resources. For the steps to do this, see [Cloning rules from one policy to another](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#clone-rules).

In the following example, `policy-1` is attached to the `dev-projects` folder, and you would like to make several changes that apply atomically. Create a new policy named `scratch-policy`, and then copy all of the existing rules from `policy-1` to `scratch-policy` for editing. After you finish editing, copy all the rules from `scratch-policy` back to `policy-1`.

[ ![Modify a policy](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-5.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-5.svg) Modify a policy

### Move a policy

Hierarchical firewall policies, like projects, are parented by a folder or organization resource. As your folder scheme evolves, you might need to move a hierarchical firewall policy to a new folder, perhaps before a folder deletion. Policies owned by a folder are deleted if the folder is deleted.

The following diagram illustrates [moving a policy between resources](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#move-policy) associations or the evaluation of rules in the policy.

[ ![Move a policy](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-6.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-6.svg) Move a policy

### Associate a hierarchical firewall policy with a folder

A hierarchical firewall policy is not enforced unless it is associated with an organization or a folder. After it is associated, it is applied to all VMs in all networks under that organization or folder.

[ ![Associate a policy](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-7.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-7.svg) Associate a policy

### Changes to the resource hierarchy

Changes to the resource hierarchy might take some time to propagate through the system. We recommend that you avoid simultaneous updates to the hierarchical firewall policy attachments and the resource hierarchy because networks might not immediately inherit the hierarchical firewall policy defined in the new location in the hierarchy.

[ ![Moving a policy](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-9.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-9.svg) Moving a policy

For example, if you are moving the `dept-A` folder from the `dev-projects` folder to the `eng-projects` folder and changing the association of `policy-1` to `eng-projects` instead of `dev-projects`, be sure to not disassociate `policy-1` from `dev-projects` at the same time. If the `dev-projects` folder loses its hierarchical firewall policy association before all VPC networks under it have had their ancestry updated, for a short period of time those VPC networks are not protected by `policy-1`.

## Use hierarchical firewall policies with Shared VPC

In [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) scenarios, a VM interface connected to a host project network is governed by the hierarchical firewall policy rules of the host project, not the service project.

[ ![VM in Shared VPC](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-10.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-10.svg) VM in Shared VPC

Even if the service projects are under a different folder than the host project, the VM interfaces in the shared network still inherit from the host project folder rules.

[ ![Service project VMs inherit rules from host project](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-11.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-11.svg) Service project VMs inherit rules from host project

## Use hierarchical firewall policies with VPC Network Peering

In [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) scenarios, the VM interface associated to each of the VPC networks inherits the policies in the hierarchy in the respective VPC networks. The following is a VPC Network Peering example where the VPC peered networks belong to different organizations.

[ ![VMs inherit from respective networks](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-12.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/hfw-12.svg) VMs inherit from respective networks

## What's next

  * To create and modify hierarchical firewall policies and rules, see [Create hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies) and [Manage hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/manage-hierarchical-firewall-policies).
  * For more information about examples of hierarchical firewall policy implementations, see [Hierarchical firewall policy examples](https://docs.cloud.google.com/firewall/docs/firewall-policies-examples).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
