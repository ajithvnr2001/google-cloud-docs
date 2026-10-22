---
url: https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies/
title: Manage global network firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:08.114415+00:00
---

# Manage global network firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage global network firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

To control network traffic across your Google Cloud environment, manage global network firewall policies and their rules. This page describes how to list, describe, and update policies and their individual rules. You learn to clone rules between policies and manage policy associations with your Virtual Private Cloud (VPC) networks.

Before you read this page, ensure you are familiar with the concepts described in the [Global network firewall policies overview](https://docs.cloud.google.com/firewall/docs/network-firewall-policies).

## Firewall policy tasks

This section describes how to manage global network firewall policies.

### Describe a global network firewall policy

You can view details about a global network firewall policy, including the policy rules and the associated rule attributes. All these rule attributes are counted as part of the rule attribute quota. For more information, see "Rule attributes per global network firewall policy" in the [Per firewall policy](https://docs.cloud.google.com/firewall/docs/quotas#per-firewall-policy-quotas) table.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the firewall policy or project containing the firewall policy _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the global network firewall policy.

  3. Click your policy.




###  gcloud 
    
    
    gcloud compute network-firewall-policies describe POLICY_NAME \
        --global
    

### Update a global network firewall policy description

The only policy field that can be updated is the **Description** field.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the global network firewall policy.

  3. Click your policy.

  4. Click **Edit**.

  5. In the **Description** field, change the text.

  6. Click **Save**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies update POLICY_NAME \
        --description DESCRIPTION \
        --global
    

### List global network firewall policies

You can view a list of the policies available in your project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.list`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the firewall policy or project containing the firewall policy _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy.

The **Network firewall policies** section shows the policies available in your project.




###  gcloud 
    
    
    gcloud compute network-firewall-policies list --global
    

### Remove the network association

If you need to change the global network firewall policy that's associated with a VPC network, we recommend that you first [associate a new policy](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate) instead of deleting an existing associated policy. You can associate a new policy in one step, which helps to ensure that a global network firewall policy is always associated with the VPC network.

To delete an association between a global network firewall policy and a VPC network, follow the steps mentioned in this section. Rules in the global network firewall policy don't apply to new connections after its association is deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.networks.setFirewallPolicy`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the project containing the network



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project or the folder that contains the policy.

  3. Click your policy.

  4. Click the **Associations** tab.

  5. Select the association that you want to delete.

  6. Click **Remove association**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies associations delete \
        --firewall-policy FIREWALL_POLICY \
        --name ASSOCIATION_NAME \
        --firewall-policy-region FIREWALL_POLICY_REGION \
        --global-firewall-policy
    

### Delete a global network firewall policy

Before you can delete a global network firewall policy, you must delete all of its associations.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.delete`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy.

  3. Click the policy that you want to delete.

  4. Click the **Associations** tab.

  5. Select all associations.

  6. Click **Remove association**.

  7. After all associations are removed, click **Delete**.




###  gcloud 

Use the following command to delete the policy:
    
    
    gcloud compute network-firewall-policies delete POLICY_NAME \
        --global
    

## Firewall policy rule tasks

This section describes how to manage global network firewall policy rules.

### Clone rules from one policy to another

Cloning copies the rules from a source policy to a target policy, replacing all existing rules in the target policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.cloneRules`
  * `compute.networks.setFirewallPolicy`



**Roles**

  * Compute Editor (`roles/compute.editor`) on the firewall policy or project containing the firewall policy _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy.

  3. Click the policy from which you want to copy the rules.

  4. Click **Clone** at the top of the screen.

  5. Provide the name of a target policy.

  6. If you want to associate the new policy immediately, click **Continue > Associate**.

  7. In the **Associate policy with VPC networks** page, select the networks and click **Associate**.

  8. Click **Continue**.

  9. Click **Clone**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies clone-rules TARGET_POLICY \
        --global \
        --source-firewall-policy SOURCE_POLICY
    

Replace the following:

  * `TARGET_POLICY`: the name of the target policy.
  * `SOURCE_POLICY`: the URL of the source policy.



### Describe a rule

You can view details about a specific rule in a global network firewall policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the firewall policy or project containing the firewall policy _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy.

  3. Click your policy.

  4. Click the priority of the rule.




###  gcloud 
    
    
    gcloud compute network-firewall-policies rules describe PRIORITY \
        --firewall-policy=POLICY_NAME \
        --global-firewall-policy
    

Replace the following:

  * `PRIORITY`: the priority number that uniquely identifies the rule.
  * `POLICY_NAME`: the name of the policy that contains the rule.



### Update a global network firewall policy rule

You can modify a global network firewall policy rule to change rule attributes, such as action on match, IP address ranges, or protocols and ports.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`
  * `compute.firewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the global network firewall policy.

  3. Click the name of the global network firewall policy that contains the rule to update.

  4. Click the priority of the rule.

  5. Click **Edit**.

  6. Modify the firewall rule fields that you want to change. For descriptions about each field, see one of the following:

     * [Create an ingress rule for VM targets](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-ingress-rule-target-vm)
     * [Create an egress rule for VM targets](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-egress-rule-target-vm)
  7. Click **Save**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies rules update PRIORITY \
        --firewall-policy=POLICY_NAME \
        --global-firewall-policy \
        [...other flags that you want to modify...]
    

Replace the following:

  * `PRIORITY`: the priority number that uniquely identifies the rule.
  * `POLICY_NAME`: the name of the policy that contains the rule.



Supply the flags that you want to modify. For flag descriptions, see one of the following:

  * [Create an ingress rule for VM targets](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-ingress-rule-target-vm)
  * [Create an egress rule for VM targets](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-egress-rule-target-vm)



### View effective firewall rules for a VM interface

You can view all firewall rules—from all applicable firewall policies and VPC firewall rules—that apply to a network interface of a Compute Engine VM.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.instances.getEffectiveFirewalls`



**Roles**

  * Compute Instance Admin (`roles/compute.instanceAdmin`) on the project containing the VM instance _or_
  * Instance Group Manager Service Agent (`roles/compute.instanceGroupManagerServiceAgent`) on the project containing the VM instance _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the project containing the VM instance _or_
  * Compute Viewer (`roles/compute.viewer`) on the project containing the VM instance



###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the project selector menu, select the project that contains the VM.

  3. Click the VM.

  4. For **Network interfaces** , click the name of the interface.

  5. In **Network configuration analysis** section, click the **Firewalls** tab.

  6. To view the effective firewall rules, click **Firewall rule view** tab.




###  gcloud 
    
    
    gcloud compute instances network-interfaces get-effective-firewalls INSTANCE_NAME \
        [--network-interface INTERFACE] \
        [--zone ZONE]
    

Replace the following:

  * `INSTANCE_NAME`: the VM for which you want to view the effective rules; if no interface is specified, the command returns rules for the primary interface (`nic0`).
  * `INTERFACE`: the VM interface for which you want to view the effective rules; the default value is `nic0`.
  * `ZONE`: the zone of the VM; this line is optional if the chosen zone is already set as the default.



### View effective firewall rules for a network

You can view all hierarchical firewall policy rules, VPC firewall rules, and global network firewall policy rules that apply to all regions of a VPC network.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.networks.getEffectiveFirewalls`
  * `compute.networks.getRegionEffectiveFirewalls`



**Roles**

    * Compute Network Admin (`roles/compute.networkAdmin`) on the project containing the network _or_
    * Compute Network User (`roles/compute.networkUser`) on the project containing the network _or_
    * Compute Network Viewer (`roles/compute.networkViewer`) on the project containing the network _or_
    * Compute Security Admin (`roles/compute.securityAdmin`) on the project containing the network _or_
    * Compute Viewer (`roles/compute.viewer`) on the project containing the network



###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the network you want to view firewall policy rules for.

  3. On the **VPC network details** page, click **Firewalls** tab.

  4. To view the rules that apply to this network, click **Firewall rule view** tab.




###  gcloud 
    
    
    gcloud compute networks get-effective-firewalls NETWORK_NAME
    

Replace `NETWORK_NAME` with the network for which you want to view the effective rules.

You can also view effective firewall rules for a network from the **Firewall** page.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.organizations.listAssociations` on the network
  * Optional: `resourcemanager.folders.get` and `resourcemanager.organizations.get` to view information in the **Inherited from** and **Located at** columns



**Roles**

To view firewall rules:

  * Compute Organization Resource Admin (`roles/compute.orgSecurityResourceAdmin`)
  * Compute Viewer (`roles/compute.viewer`)



Optional: To view information in the **Inherited from** and **Located at** columns:

  * Browser (`roles/browser`)
  * Organization Administrator (`roles/resourcemanager.organizationAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. The firewall policies are listed in the **Firewall policies inherited by this project** section.

  3. Click each firewall policy to view the rules that apply to this network.




### Delete a rule from a policy

Deleting a rule from a policy causes the rule to no longer apply to new connections to or from the rule's target.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy.

  3. Click your policy.

  4. Select the rule that you want to delete.

  5. Click **Delete**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies rules delete PRIORITY \
        --firewall-policy=POLICY_NAME \
        --global-firewall-policy
    

Replace the following:

  * `PRIORITY`: the priority number that uniquely identifies the rule.
  * `POLICY_NAME`: the name of the policy that contains the rule.



## What's next

  * [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies)
  * [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies)
  * [Create global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
