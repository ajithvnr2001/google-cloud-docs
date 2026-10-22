---
url: https://docs.cloud.google.com/firewall/docs/configure-wildfire/
title: Configure Advanced malware sandbox in your network \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:09.248028+00:00
---

# Configure Advanced malware sandbox in your network  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/configure-wildfire/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Configure Advanced malware sandbox in your network Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Advanced malware sandbox (WildFire) lets you protect your network against unknown, file-based threats and malware. To enable Advanced malware sandbox in your network, you must set up multiple Cloud Next Generation Firewall (Cloud NGFW) components, including firewall endpoints, security profiles, and security profile groups. This document provides a high-level workflow that describes how to configure these components and enable Advanced malware sandbox.

To learn more about Advanced malware sandbox, see [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire).

## Required roles

Identity and Access Management (IAM) roles govern the actions for configuring and enabling Advanced malware sandbox. The following table describes the roles that are necessary for each step:

Ability | Necessary role  
---|---  
Create a firewall endpoint and a firewall endpoint association for a Virtual Private Cloud (VPC) network.  | To perform this task, ensure that you have one of the following roles: 

  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Firewall Endpoint Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.firewallEndpointAdmin) (`roles/networksecurity.firewallEndpointAdmin`) at either the project level ([Preview](https://cloud.google.com/products#product-launch-stages)) or organization level.

These roles include the following permission to create a firewall endpoint: 
  * `networksecurity.firewallEndpoints.create`

Additionally, these roles include the following permissions to create a firewall endpoint association: 
  * `networksecurity.firewallEndpointAssociations.create`
  * `networksecurity.firewallEndpoints.use` on the organization where the firewall endpoint exists

  
Create a Advanced malware sandbox security profile, a threat prevention security profile, and a security profile group  | [Security Profile Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.securityProfileAdmin) (`roles/networksecurity.securityProfileAdmin`) at either the project level ([Preview](https://cloud.google.com/products#product-launch-stages)) or organization level.  
This role includes the following required permissions: 

  * `networksecurity.securityProfileGroups.create` to create a security profile group
  * `networksecurity.securityProfiles.create` to create an Advanced malware sandbox security profile or a threat prevention security profile

  
Create a hierarchical firewall policy and its rules  | [Compute Organization Firewall Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyAdmin) (`roles/compute.orgFirewallPolicyAdmin`).   
You must have this role to create a hierarchical firewall policy. You must grant the role on the resource where you want to create the policy.  
In addition, you must have this role to create a rule in a hierarchical firewall policy. You must grant the role on the resource containing the policy or on the policy itself.  
The role includes the following required permissions: 

  * `compute.firewallPolicies.create` to create a hierarchical firewall policy
  * `compute.firewallPolicies.update` to create a hierarchical firewall policy rule

  
Associate a hierarchical firewall policy with an organization or folder  | To perform this task, ensure that you have one of the following roles: 

  * [Compute Organization Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityResourceAdmin) (`roles/compute.orgSecurityResourceAdmin`) on the target resource and [Compute Organization Firewall Policy User](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyUser) (`roles/compute.orgFirewallPolicyUser`) on the policy resource or on the policy itself
  * [Compute Organization Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgSecurityResourceAdmin) (`roles/compute.orgSecurityResourceAdmin`) on the target resource and [Compute Organization Firewall Policy Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.orgFirewallPolicyAdmin) (`roles/compute.orgFirewallPolicyAdmin`) on the policy resource or on the policy itself

These roles include the following required permissions: 
  * `compute.firewallPolicies.addAssociation` on the firewall policy
  * `compute.organizations.setFirewallPolicy` on the target resource

  
Create a global network firewall policy and its rules  | [Compute Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)  
  
You must have this role to create a global network firewall policy. You must grant the role on the project where you want to create the policy.  
  
In addition, you must have this role to create a rule in a global network firewall policy. You must grant the role on the project containing the policy or on the policy itself.  
  
The role includes the following required permissions: 

  * `compute.firewallPolicies.create` to create a global network firewall policy
  * `compute.firewallPolicies.update` to create a global network firewall policy rule

  
Associate a global network firewall policy with a VPC network  | [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)  
  
This role includes the following required permissions: 

  * `compute.firewallPolicies.use`
  * `compute.networks.setFirewallPolicy`

  
Create a CA pool  | [CA Service Operation Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/privateca#privateca.caManager) (`roles/privateca.caManager`)  
  
If you use Transport Layer Security (TLS) inspection, you must have this role to create a Certificate Authority (CA) pool.  
  
Create a TLS inspection policy  | To perform this task, ensure that you have one of the following roles: 

  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`)

If you use TLS inspection, you need one of the preceding roles to create a TLS inspection policy. These roles include the following required permissions: 
  * `certificatemanager.trustconfigs.list`
  * `certificatemanager.trustconfigs.use`
  * `networksecurity.operations.get`
  * `networksecurity.tlsInspectionPolicies.create`
  * `networksecurity.tlsInspectionPolicies.list`
  * `privateca.caPools.list`
  * `privateca.caPools.use`
  * `privateca.certificateAuthorities.list`

  
  
## Configure Advanced malware sandbox without TLS inspection

To configure Advanced malware sandbox without [Transport Layer Security (TLS)](https://docs.cloud.google.com/firewall/docs/about-tls-inspection) inspection in your network, do the following:

**Note:** The following workflow describes how you can configure Advanced malware sandbox. This workflow assumes that you have already set up your Virtual Private Cloud (VPC) network, subnets, and virtual machine (VM) instances.

  1. **Accept the Advanced malware sandbox EULA**

Before you enable Advanced malware sandbox on endpoints, you must review and accept the end-user license agreement (EULA) on the billing project. You can accept the EULA when you create or update an endpoint.

For more information, see [Create a firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#create-firewall-endpoint).

  2. **Create an Advanced malware sandbox security profile**

Create an Advanced malware sandbox security profile of type `WILDFIRE_ANALYSIS` and specify the types of files to submit for analysis and the traffic direction (upload or download).

For more information, see [Create an Advanced malware sandbox security profile](https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles#create-wildfire-security-profile).

  3. **Create a threat prevention security profile**

A threat prevention security profile is required when you use an Advanced malware sandbox security profile in a group. Create a threat prevention security profile of type `THREAT_PREVENTION`.

For more information, see [Create a threat prevention security profile](https://docs.cloud.google.com/firewall/docs/configure-security-profiles#create-tp-security-profile).

  4. **Create a security profile group**

Add the Advanced malware sandbox and threat prevention security profiles to the security profile group.

For more information, see [Create a security profile group](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups#create-security-profile-group).

  5. **Create a firewall endpoint with Advanced malware sandbox enabled**

Create a firewall endpoint. In the **Advanced configuration** section, select the **Enable Advanced malware sandbox (WildFire)** checkbox.

For more information, see [Create a firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#create-firewall-endpoint).

  6. **Associate the firewall endpoint with your VPC networks**

To enable Advanced malware sandbox, associate the firewall endpoint with your VPC networks. Ensure that your workloads run in the same zone as the firewall endpoint.

A firewall endpoint with jumbo frame support can accept packets only up to 8,500 bytes. Alternatively, a firewall endpoint without jumbo frame support can accept packets only up to 1,460 bytes. If you need Advanced malware sandbox, we recommend that you configure the associated VPC networks to use the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) limits of 8,500 bytes and 1,460 bytes. For more information, see [ Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

**Caution:** A firewall endpoint doesn't perform Advanced malware sandbox for a VPC network if the network is configured with an MTU that's greater than the firewall endpoint's limit.

For more information, see [Create firewall endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoint-associations#create-endpoint-association).

  7. **Configure and apply Advanced malware sandbox to your network traffic**

Create a global or hierarchical firewall policy rule with the `apply_security_profile_group` action. Specify your security profile group. Ensure that the firewall policy is associated with the same VPC network as the workloads to inspect.

For more information, see [Create hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies) and [Create global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies).




## Configure Advanced malware sandbox with TLS inspection

To configure Advanced malware sandbox with TLS inspection in your network, do the following:

  1. **Accept the Advanced malware sandbox EULA**

Before you enable Advanced malware sandbox on endpoints, you must review and accept the EULA on the billing project. You can accept the EULA when you create or update an endpoint.

For more information, see [Create a firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#create-firewall-endpoint).

  2. **Create an Advanced malware sandbox security profile**

Create an Advanced malware sandbox security profile of type `WILDFIRE_ANALYSIS` and specify the types of files to submit for analysis and the traffic direction (upload or download).

For more information, see [Create an Advanced malware sandbox security profile](https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles#create-wildfire-security-profile).

  3. **Create a threat prevention security profile**

A threat prevention security profile is required when you use an Advanced malware sandbox security profile in a group. Create a threat prevention security profile of type `THREAT_PREVENTION`.

For more information, see [Create a threat prevention security profile](https://docs.cloud.google.com/firewall/docs/configure-security-profiles#create-tp-security-profile).

  4. **Create a security profile group**

Add the Advanced malware sandbox and threat prevention security profiles to the security profile group.

For more information, see [Create a security profile group](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups#create-security-profile-group).

  5. **Create a firewall endpoint with Advanced malware sandbox enabled**

Create a firewall endpoint. In the **Advanced configuration** section, select the **Enable Advanced malware sandbox (WildFire)** checkbox.

For more information, see [Create a firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#create-firewall-endpoint).

  6. **Associate the firewall endpoint with your VPC networks**

To enable Advanced malware sandbox, associate the firewall endpoint with your VPC networks. Ensure that your workloads run in the same zone as the firewall endpoint.

A firewall endpoint with jumbo frame support can accept packets only up to 8,500 bytes. Alternatively, a firewall endpoint without jumbo frame support can accept packets only up to 1,460 bytes. If you need Advanced malware sandbox, we recommend that you configure the associated VPC networks to use the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) limits of 8,500 bytes and 1,460 bytes. For more information, see [ Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

**Caution:** A firewall endpoint doesn't perform Advanced malware sandbox for a VPC network if the network is configured with an MTU that's greater than the firewall endpoint's limit.

For more information, see [Create firewall endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoint-associations#create-endpoint-association).

  7. **Create and configure resources to inspect encrypted traffic**

     1. Create a CA pool

A CA pool is a collection of CAs with a common certificate issuance policy and IAM policy. A regional CA pool must exist before you can configure TLS inspection.

For more information, see [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

     2. Create a root CA

To use TLS inspection, you must have at least one root CA. The root CA signs an intermediate CA, which then signs all leaf certificates for the clients. For more information, see the [`gcloud privateca roots create` command reference](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/roots/create).

     3. Grant permissions to the Network Security service agent

Cloud NGFW requires the Network Security service agent to generate intermediate CAs for TLS inspection. The service agent needs permissions to request certificates for the CA pool.

For more information, see [Create a service account](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection#create-service-account).

  8. **Create a regional TLS inspection policy**

A TLS inspection policy specifies how to intercept encrypted traffic. A regional TLS inspection policy contains the configuration settings for TLS inspection.

For more information, see [Create a TLS inspection policy](https://docs.cloud.google.com/firewall/docs/setup-tls-inspection#create-tls-inspection-policy).

  9. **Add a TLS inspection policy to a firewall endpoint association**

To add the TLS inspection policy to a firewall endpoint association, see [Create firewall endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoint-associations#create-endpoint-association).

  10. **Configure and apply Advanced malware sandbox to your network traffic**

To configure Advanced malware sandbox, create a [global network firewall policy](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) or a [hierarchical firewall policy](https://docs.cloud.google.com/firewall/docs/firewall-policies) with Layer 7 inspection.

     * In a new or existing global firewall policy, add a rule with the `apply_security_profile_group` action. Specify the name of the security profile group that you created previously. Ensure that the firewall policy is associated with the same VPC network as the workloads to inspect.

For more information, see [Create a global network firewall policy](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-network-firewall-policy) and [Add firewall policy rule](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules).

     * In a new or existing hierarchical firewall policy, add a rule with the `apply_security_profile_group` action. Ensure that the firewall policy is associated with the same VPC network as the workloads to inspect.

For more information, see [Firewall policy rule tasks](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks).




## Upgrade an existing firewall endpoint to enable Advanced malware sandbox

If you have already deployed Cloud Next Generation Firewall Enterprise endpoints in your network with active threat prevention security profiles and security profile groups, do the following to configure and enable Advanced malware sandbox:

  1. **Accept the Advanced malware sandbox EULA**

Review and accept the Advanced malware sandbox EULA on the billing project for your endpoints.

  2. **Create an Advanced malware sandbox security profile**

Create an Advanced malware sandbox security profile of type `WILDFIRE_ANALYSIS` and define the file submission rules, custom protocol overrides, or threat overrides. For more information, see [Create an Advanced malware sandbox security profile](https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles#create-wildfire-security-profile).

  3. **Update your security profile group**

Add the new Advanced malware sandbox security profile to your security profile group. The security profile group must contain a threat prevention profile. For more information, see [Update a security profile group](https://docs.cloud.google.com/firewall/docs/configure-security-profile-groups#update-security-profile-group).

  4. **Enable Advanced malware sandbox on the firewall endpoint**

Update the firewall endpoint and select the **Enable Advanced malware sandbox (WildFire)** checkbox in the **Advanced configuration** section for the zonal endpoint. For more information, see [Update a firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#edit-firewall-endpoint).




## What's next

  * [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire)
  * [Security profile overview](https://docs.cloud.google.com/firewall/docs/about-security-profiles)
  * [Security profile group overview](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups)
  * [Firewall endpoint overview](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
