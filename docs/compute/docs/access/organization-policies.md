---
url: https://docs.cloud.google.com/compute/docs/access/organization-policies/
title: Organization policies for Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:46.020833+00:00
---

# Organization policies for Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/access/organization-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Organization policies for Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

The Organization Policy Service provides centralized, programmatic control over your organization's resources. You can use organization policies to enforce constraints on how Compute Engine resources, such as virtual machine (VM) instances, disks, and networks, are configured. For more information about Organization Policy, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

You can set policies at the organization, folder, or project level. Descendant resources inherit policies, which lets you enforce broad controls at the organization level and apply more specific constraints at the folder or project level.

This document provides an overview of how you can use Organization Policy to manage your Compute Engine resources.

## Use cases

You can use organization policies to enforce governance across your Compute Engine resources. Common goals include:

  * **Cost management** : Control spending by restricting which VM machine types or Persistent Disk sizes can be created in a given project.
  * **Security posture** : Enforce security best practices, such as requiring OS Login for all VM instance access, or disabling the interactive serial console.
  * **Compliance** : Meet regulatory requirements such as requiring VMs in a specific project to run on sole-tenant nodes to support hardware isolation.



## Constraint types

When you use the Organization Policy, you can apply the following types of constraints:

  * **Managed constraints** : Google-provided, predefined constraints that are built on a modern platform, identifiable by the `compute.managed.*` prefix. They support safe rollout tooling, such as dry run and Policy Simulator, and tag-conditioned statements, which let you grant granular exemptions to specific resources.
  * **Managed constraints (legacy)** : Google-provided, predefined constraints identifiable by the `compute.*` prefix. While functional, they generally lack support for modern safe rollout tools, such as Dry Run and Policy Simulator, and don't support tag-conditioned statements. When an equivalent alternative is available, we recommend migrating to managed constraints to take advantage of enhanced governance and safe rollout capabilities.
  * **Custom constraints** : Constraints that you create for your specific needs using the Common Expression Language (CEL). Custom constraints let you enforce policies on specific fields that are not addressed by managed constraints. Like managed constraints, custom constraints support tag-conditioned statements and safe rollout tools, such as Dry Run and Policy Simulator. To learn more about creating and managing custom constraints for Compute Engine, see [Custom constraints](https://docs.cloud.google.com/compute/docs/access/custom-constraints).



A limit of 20 constraints per Compute Engine resource applies to the total number of managed constraints and custom constraints combined. Legacy managed constraints don't count toward this limit.

## Compute Engine constraints

The following sections list the Compute Engine constraints that Organization Policy supports.

### Managed constraints

Managed constraints for Compute Engine simplify governance for common security scenarios and integrate with safe rollout tools, such as dry-run and Policy Simulator, which let you test their impact before enforcement. For a list of managed constraints for Compute Engine, see [Managed constraints](https://docs.cloud.google.com/compute/docs/access/managed-constraints).

### Managed constraints (legacy)

These constraints are from the previous generation and don't support safe rollout tools. We recommend migrating to managed constraints when an equivalent is available.

#### Legacy constraints

Constraint | Description  
---|---  
`compute.allowedDeviceEncryptionKeys` | Restricts the Cloud Key Management Service keys that can be used to encrypt device resources.  
`compute.disableAllIpv6` | Disables creation of or update to subnet stacks of type `IPV4_IPV6` but does not affect existing `IPV4_IPV6` stack type subnets. If this constraint is active, any existing `IPV4_IPV6` stack type subnetworks continue to function. However, if there are `IPV4_IPV6` stack type subnetworks in the project when this constraint is activated, you must delete them before you can create an `IPV4_ONLY` stack type subnetwork in the same region, even if you are using a different VPC network.  
`compute.disableGuestAttributes` | Disables Compute Engine guest attributes, which can be used to publish hostnames, IP addresses, and other instance-related information from within a virtual machine instance.  
`compute.disableInstanceDataAccessApis` | Disables access to Compute Engine instance metadata APIs needed to access sensitive instance metadata, such as sshKeys, serialPortLogging, and startup-/shutdown-scripts.  
`compute.disableInternetNetworkEndpointGroup` | Disables creation of Internet Network Endpoint Groups.  
`compute.disableNestedVirtualization` | When set to `true`, disables hardware-accelerated nested virtualization for all Compute Engine VMs in the project.  
`compute.disableSerialPortAccess` | Disables serial port access to Compute Engine VMs.  
`compute.disableSerialPortLogging` | Disables serial port logging to Google Cloud Observability from Compute Engine VMs.  
`compute.disableVpcExternalIpv6` | If this constraint is active, you cannot create VPC networks with ULA internal IPv6 ranges, or assign external IPv6 addresses to VMs in VPC networks. This constraint does not affect internal IPv6 addresses in VPC networks.  
`compute.enableComplianceMemoryProtection` | Enables memory protection features on Compute Engine virtual machines.  
`compute.requireConfidentialVm` | Requires that all new Compute Engine VM instances use Confidential VM.  
`compute.requireGuestAttributes` | Requires Compute Engine guest attributes, which can be used to publish hostnames, IP addresses, and other instance-related information from within a virtual machine instance.  
`compute.requireOsLogin` | Requires all new Compute Engine VM instances to enable OS Login.  
`compute.requireShieldedVm` | Requires that all new VM instances are Shielded VMs.  
`compute.restrictCloudNATUsage` | Restricts Cloud NAT usage to only specified VPC networks.  
`compute.restrictDedicatedInterconnectUsage` | Restricts Dedicated Interconnect usage to only specified VPC networks.  
`compute.restrictLoadBalancerCreationForTypes` | Restricts creation of load balancers to only allowed types.  
`compute.restrictPartnerInterconnectUsage` | Restricts Partner Interconnect usage to only specified VPC networks.  
`compute.restrictProtocolForwardingCreationForTypes` | Restricts creation of protocol forwarding to internal or external target instances.  
`compute.restrictSharedVpcHostProjects` | Restricts the set of host projects that projects in scope can attach to.  
`compute.restrictSharedVpcSubnetworks` | Restricts the set of Shared VPC subnetworks that projects in scope can use.  
`compute.restrictVpcPeering` | Restricts VPC Network Peering to only allowed VPC networks.  
`compute.restrictVpnPeerIPs` | Restricts VPN peer IPs to only allowed IPs.  
`compute.setNewProjectDefaultToZonalDnsOnly` | When set to `true`, new projects default to Zonal DNS only; VMs created in these projects have zonal DNS names (`.zone.c.project-id.internal`). Projects for which Global DNS is disabled cannot be reverted to Global DNS.  
`compute.skipDefaultNetworkCreation` | Skips the automatic creation of the `default` VPC network and related resources during Google Cloud Project creation.  
`compute.storageResourceUseRestrictions` | Restricts the use of Compute Engine storage resources (such as PD-Standard, PD-SSD, PD-Balanced, Local-SSD) based on location.  
`compute.trustedImageProjects` | Restricts image access to only trusted images from the specified projects.  
`compute.vmCanIpForward` | Restricts which VM instances can enable IP forwarding.  
`compute.vmExternalIpAccess` | Restricts VM instances that are allowed to use external IP addresses.  
  
## What's next

  * To learn how to apply these constraints, see [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) in the Resource Manager documentation.
  * To test the effect of a new policy before enforcing it, see [Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies).
  * To learn about creating custom constraints, see [Custom constraints](https://docs.cloud.google.com/compute/docs/access/custom-constraints).
  * To see a complete list of all constraints available across Google Cloud, see [Organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
