---
url: https://docs.cloud.google.com/firewall/docs/network-firewall-policies/
title: Global network firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:35.535689+00:00
---

# Global network firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/network-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Global network firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

To simplify rule management across your Virtual Private Cloud (VPC) networks, use global network firewall policies to consolidate multiple rules into a single object. Review the specifications and enforcement methods of global network policies to maintain micro-segmentation and control traffic flow.

For more information, see the [Firewall policies overview](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview).

## Specifications

  * Global network firewall policies are container resources for firewall rules. Each global network firewall policy resource is defined within a project. 
    * After you create a global network firewall policy, you can add, update, and delete firewall rules in the policy.
    * For specification information about the rules in global network firewall policies, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).
  * To apply global network firewall policy rules to a VPC network, you must _associate_ the firewall policy with that VPC network. 
    * You can associate a global network firewall policy with multiple VPC networks. Make sure that the firewall policy and the associated networks belong to the same project.
    * Each VPC network can be associated with only _one_ global network firewall policy.
    * If the firewall policy isn't associated with any VPC network, the rules in that policy have no effect. A firewall policy that is not associated with any network is an _unassociated_ global network firewall policy.
  * When a global network firewall policy is associated with one or more VPC networks, the firewall policy rules are enforced in the following ways: 
    * Existing rules are enforced against applicable resources in the associated VPC networks.
    * Any changes made to the rules are enforced against applicable resources in the associated VPC networks.
  * Rules in global network firewall policies are enforced along with other firewall rules as described in [Policy and rule evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).


  * Use global network firewall policy rules to configure Layer 7 inspection of matched traffic, such as when using the [URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering) or the [intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention).

You create a firewall policy rule with `apply_security_profile_group` action and name of the [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups). The traffic matching the firewall policy rule is transparently forwarded to the firewall endpoint for Layer 7 inspection. To learn how to create a firewall policy rule, see [Add firewall policy rule](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules).




## Global network firewall policy rule details

For more information about the components and parameters of rules in a global network firewall policy, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).

The following table summarizes key differences between global network firewall policy rules and VPC firewall rules:

| Global network firewall policy rules | VPC firewall rules  
---|---|---  
Priority number | Must be unique within a policy | Duplicate priorities allowed  
Service accounts as targets | Yes | Yes  
Service accounts as sources  
(ingress rules only) | No | Yes  
Tag type | Secure tag | Network tag  
Name and description | Policy name, policy and rule description  | Rule name and description  
Batch update | Yes—for policy clone, edit, and replace functions | No  
Reuse | Yes | No  
Quota | Attribute count—based on a total complexity of each rule in the policy | Rule count—complex and simple firewall rules have the same quota impact  
  
## Predefined rules

When you create a global network firewall policy, Cloud Next Generation Firewall (Cloud NGFW) adds predefined rules with the lowest priority to the policy. These rules are applied to any connections that don't match an explicitly defined rule in the policy, causing such connections to be passed down to lower-level policies or network rules.

To learn about the various types of predefined rules and their characteristics, see [Predefined rules for firewall policies](https://docs.cloud.google.com/firewall/docs/pre-defined-rules).

## Identity and Access Management (IAM) roles

IAM roles govern the following actions with regard to global network firewall policies:

  * Creating a global network firewall policy
  * Associating a policy with a network
  * Modifying an existing policy
  * Viewing the effective firewall rules for a particular network or VM



The following table describes which roles are necessary for each action:

Action | Necessary role  
---|---  
Create a new global network firewall policy  | [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`) on the project to which the policy belongs  
Associate a policy with a network  | [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) on the project where the policy will live   
Modify the policy by adding, updating, or deleting policy firewall rules  | [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`) on the project where the policy will live  
Delete the policy  | [Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`) on the project where the policy will live  
View effective firewall rules for a VPC network  | Any of the following roles for the network:   
[Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  
[Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)  
[Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  
[Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)  
[Compute Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)   
View effective firewall rules for a VM in a network  | Any of the following roles for the VM:   
[Compute Instance Admin (v1) role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)  
[Instance Group Manager Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceGroupManagerServiceAgent) (`roles/compute.instanceGroupManagerServiceAgent`)  
[Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)  
[Compute Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)   
  
The following roles are relevant to global network firewall policies.

Role name | Description  
---|---  
[Compute Security Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)  | Can be granted at the project or policy level. If granted for a project, lets users create, update, and delete global network firewall policies and their rules. At the policy level, lets users to update the policy rules, but not create or delete the policy. This role also lets users to associate a policy with a network.  
[Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  | Granted at the project level or network level. If granted for a network, allows users to view the list of global network firewall policies.  
[Compute Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)  
  
[Compute Network User role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) (`roles/compute.networkUser`)  
  
[Compute Network Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)  
  
| Allows users to view the firewall rules applied to the network or instance.  
Includes the `compute.networks.getEffectiveFirewalls` permission for networks and the `compute.instances.getEffectiveFirewalls` for instances.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
