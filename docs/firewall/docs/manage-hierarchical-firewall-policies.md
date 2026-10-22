---
url: https://docs.cloud.google.com/firewall/docs/manage-hierarchical-firewall-policies/
title: Manage hierarchical firewall policies and rules \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:45.588863+00:00
---

# Manage hierarchical firewall policies and rules  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-hierarchical-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage hierarchical firewall policies and rules Stay organized with collections  Save and categorize content based on your preferences. 

Hierarchical firewall policies provide granular control over your network traffic. This page describes how to manage hierarchical firewall policies and their rules to secure your Google Cloud resources.

Before you read this page, ensure you are familiar with the concepts described in the [Hierarchical firewall policies overview](https://docs.cloud.google.com/firewall/docs/firewall-policies). To see examples of hierarchical firewall policy implementations, see [Hierarchical firewall policy examples](https://docs.cloud.google.com/firewall/docs/firewall-policies-examples).

## Firewall policy tasks

This section describes how to manage hierarchical firewall policies.

To check the progress of an operation that results from a task listed in this section, make sure that your Identity and Access Management (IAM) principal has the following permissions or roles _in addition to_ the permissions or roles required for each task.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.globalOperations.get`
  * `compute.globalOperations.getIamPolicy`
  * `compute.globalOperations.list`
  * `compute.globalOperations.setIamPolicy`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the organization



### Describe a policy

You can view details about a hierarchical firewall policy, including the policy rules and associated rule attributes. All these rule attributes are counted as part of the rule attribute quota. For more information, see "Rule attributes per hierarchical firewall policy" in the [Per firewall policy](https://docs.cloud.google.com/firewall/docs/quotas#per-firewall-policy-quotas) table.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Organization Firewall Policy User (`roles/compute.orgFirewallPolicyUser`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. Click your policy.




###  gcloud 
    
    
    gcloud compute firewall-policies describe POLICY_NAME \
        --organization ORG_ID
    

### List policies

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.list`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Organization Firewall Policy User (`roles/compute.orgFirewallPolicyUser`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

For an organization, the **Firewall policies associated with this organization** section shows the associated policies. The **Firewall policies located in this organization** section lists policies that are _owned_ by the organization.

For a folder, the **Firewall policies associated with this folder or inherited by this folder** section shows the policies associated or inherited by the folder. The **Firewall policies located in this folder** section lists policies that are _owned_ by the folder.

**Note:** The policies owned by a resource (organization or folder) might not be associated with that resource, but are available to be associated with that or other resources.



###  gcloud 
    
    
    gcloud compute firewall-policies list \
        [--organization ORG_ID | --folder FOLDER_ID]
    

### List associations for a resource

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.organizations.listAssociations`



**Roles**

  * Compute Organization Resource Admin (`roles/compute.orgSecurityResourceAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. For the selected resource (organization or folder), a list of associated and inherited policies appears.




###  gcloud 
    
    
    gcloud compute firewall-policies associations list \
        [--organization ORG_ID | --folder FOLDER_ID]
    

### Move a policy from one resource to another

Moving a policy only changes the parent of the policy. Changing the parent of the policy might change which IAM principals can create and update rules in the policy and which IAM principals can create future associations.

Moving a policy doesn't change any existing policy associations or the evaluation of rules in the policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.move`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on both the new parent resource (organization or folder) _and_ the previous parent resource or the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on both the new parent resource (organization or folder) _and_ the previous parent resource or the policy itself



###  Console 

Use the Google Cloud CLI for this procedure.

###  gcloud 

Run these commands to move the hierarchical firewall policy to an organization:
    
    
    gcloud compute firewall-policies move POLICY_NAME \
        --organization ORG_ID
    

Run these commands to move the hierarchical firewall policy to a folder in an organization:
    
    
    gcloud compute firewall-policies move POLICY_NAME \
        --folder FOLDER_ID
    

Replace the following:

  * `POLICY_NAME`: either the short name or the system-generated name of the policy that you are moving
  * `ORG_ID`: the organization ID to which the policy is moved
  * `FOLDER_ID`: the folder ID to which the policy is moved



### Update a policy description

The only policy field that can be updated is the **Description** field.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or on the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. Click your policy.

  4. Click **Edit**.

  5. Modify the description.

  6. Click **Save**.




###  gcloud 
    
    
    gcloud compute firewall-policies update POLICY_NAME \
        --description DESCRIPTION \
        --organization ORG_ID
    

### Delete an association

If you need to change the hierarchical firewall policy that's associated with an organization or folder, we recommend that you [associate a new policy](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#associate) instead of deleting an existing associated policy. You can associate a new policy in one step, which helps to ensure that a hierarchical firewall policy is always associated with the organization or folder.

To delete an association between a hierarchical firewall policy and an organization or folder, follow the steps mentioned in this section. Rules in the hierarchical firewall policy don't apply to new connections after its association is deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.organizations.setFirewallPolicy`



**Roles**

  * Compute Organization Resource Admin (`roles/compute.orgSecurityResourceAdmin`) on the parent resource (organization or folder) with which the policy is associated



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. Click your policy.

  4. Click the **Associations** tab.

  5. Select the association that you want to delete.

  6. Click **Remove association**.




###  gcloud 
    
    
    gcloud compute firewall-policies associations delete ASSOCIATION_NAME \
        --firewall-policy POLICY_NAME \
        --organization ORG_ID
    

### Delete a policy

Before you can delete a hierarchical firewall policy, you must delete all of its associations.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.delete`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. Click the policy that you want to delete.

  4. Click the **Associations** tab.

  5. Select all associations.

  6. Click **Remove association**.

  7. After all associations are removed, click **Delete**.




###  gcloud 

Use the following command to delete the policy:
    
    
    gcloud compute firewall-policies delete POLICY_NAME \
        --organization ORG_ID
    

## Firewall policy rule tasks

This section describes how to manage hierarchical firewall policy rules.

### Clone rules from one policy to another

Remove all rules from the target policy and replace them with the rules in the source policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.copyRules`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. Click the policy that you want to copy rules from.

  4. Click **Clone** at the top of the screen.

  5. Provide the name of a target policy.

  6. Optional: If you want to associate the new policy immediately, click **Continue** to open the **Associate policy with resources** section.

  7. Click **Clone**.




###  gcloud 
    
    
    gcloud compute firewall-policies clone-rules POLICY_NAME \
        --source-firewall-policy=SOURCE_POLICY \
        --organization=ORG_ID \
    

Replace the following:

  * `POLICY_NAME`: the policy to receive the copied rules
  * `SOURCE_POLICY`: the policy to copy the rules from; must be the URL of the resource
  * `ORG_ID`: the organization ID that contains the hierarchical firewall policy.



### Describe a rule

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Organization Firewall Policy User (`roles/compute.orgFirewallPolicyUser`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. Click your policy.

  4. Click the priority of the rule.




###  gcloud 
    
    
    gcloud compute firewall-policies rules describe PRIORITY \
        --firewall-policy=POLICY_NAME \
        --organization=ORG_ID
    

Replace the following:

  * `POLICY_NAME`: the name of the hierarchical firewall policy that contains the new rule.
  * `ORG_ID`: the organization ID that contains the hierarchical firewall policy.



### List all rules in a policy

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Organization Firewall Policy User (`roles/compute.orgFirewallPolicyUser`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. Click your policy. Rules are listed on the **Firewall rules** tab.




###  gcloud 
    
    
    gcloud compute firewall-policies list-rules POLICY_NAME \
        --organization=ORG_ID
    

Replace the following:

  * `POLICY_NAME`: the name of the hierarchical firewall policy that contains the rule.
  * `ORG_ID`: the organization ID that contains the hierarchical firewall policy.



### Update a rule

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select the organization or folder that contains the hierarchical firewall policy.

  3. Click the name of the hierarchical firewall policy that contains the rule to update.

  4. Click the priority of the rule.

  5. Click **Edit**.

  6. Modify the firewall rule fields that you want to change. For descriptions about each field, see one of the following:

     * [Create an ingress rule for VM targets](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-ingress-rule-target-vm)
     * [Create an egress rule for VM targets](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-egress-rule-target-vm)
  7. Click **Save**.




###  gcloud 
    
    
    gcloud compute firewall-policies rules update PRIORITY \
        --firewall-policy=POLICY_NAME \
        --organization ORG_ID \
        [...other flags that you want to modify...]
    

Replace the following:

  * `PRIORITY`: the priority number that uniquely identifies the rule.
  * `POLICY_NAME`: the name of the policy that contains the rule.
  * `ORG_ID`: the organization ID that contains the hierarchical firewall policy.



Supply the flags that you want to modify. For flag descriptions, see one of the following:

  * [Create an ingress rule for VM targets](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-ingress-rule-target-vm)
  * [Create an egress rule for VM targets](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#create-egress-rule-target-vm)



### Delete a rule

Deleting a rule from a policy causes the rule to no longer apply to new connections to or from the rule's target.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * Compute Organization Firewall Policy Admin (`roles/compute.orgFirewallPolicyAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself
  * Compute Security Admin (`roles/compute.securityAdmin`) on the parent resource (organization or folder) that contains the policy or the policy itself



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your organization ID or the folder that contains the policy.

  3. Click your policy.

  4. Select the rule that you want to delete.

  5. Click **Delete**.




###  gcloud 
    
    
    gcloud compute firewall-policies rules delete PRIORITY \
        --firewall-policy=POLICY_NAME \
        --organization=ORG_ID
    

Replace the following:

  * `PRIORITY`: the priority of the rule that you want to delete from the policy.
  * `POLICY_NAME`: the name of the hierarchical firewall policy that contains the rule.
  * `ORG_ID`: the organization ID that contains the hierarchical firewall policy.



## Get effective firewall rules for a network

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

  3. Click **Firewalls**.

  4. Expand each firewall policy to view the rules that apply to this network.




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

  * `compute.orgSecurityResourceAdmin`
  * `compute.viewer`



Optional: To view information in the **Inherited from** and **Located at** columns:

  * `browser`
  * `resourcemanager.organizationAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. The firewall policies are listed in the **Firewall policies inherited by this project** section.

  3. Click each firewall policy to view the rules that apply to this network.




## Get effective firewall rules for a VM interface

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

  4. For **Network interfaces** , click the interface.

  5. Effective firewall rules appear in the **Firewalls** tab available in the **Network configuration analysis** section.




###  gcloud 
    
    
    gcloud compute instances network-interfaces get-effective-firewalls INSTANCE_NAME \
        [--network-interface INTERFACE] \
        [--zone ZONE]
    

Replace the following:

  * `INSTANCE_NAME`: the VM for which you want to view the effective rules; if no interface is specified, the command returns rules for the primary interface (`nic0`).
  * `INTERFACE`: the VM interface for which you want to view the effective rules; the default value is `nic0`.
  * `ZONE`: the zone of the VM; this line is optional if the chosen zone is already set as the default.



## Troubleshooting

This section contains explanations for error messages that you might encounter when creating hierarchical firewall policies.

  * `FirewallPolicy may not specify a name. One will be provided.`

You cannot specify a policy name. Hierarchical firewall policy "names" are numerical IDs generated by Google Cloud when the policy is created. However, you can specify a friendlier _short name_ that acts as an alias in many contexts.

  * `FirewallPolicy may not specify associations on creation.`

Associations can only be created after hierarchical firewall policies are created.

  * `Can't move firewall policy to a different organization.`

Hierarchical firewall policy moves must stay within the same organization.

  * `The attachment already has an association. Please set the option of replacing existing association to true if you want to replace the old one.`

If a resource is already attached with a hierarchical firewall policy, the attachment operation fails unless the option of replacing the existing associations is set to true.

  * `Can't have rules with the same priorities.`

Priorities of rules are required to be unique within a hierarchical firewall policy.

  * `Direction must be specified for a firewall policy rule.`

When creating hierarchical firewall policy rules by sending REST requests directly, the direction of the rule must be specified. When using the Google Cloud CLI and no direction is specified, the default is `INGRESS`.

  * `Can't specify enable_logging on a goto_next rule.`

Firewall Logging isn't allowed for rules with goto_next action because goto_next actions are used to represent the evaluation order of different firewall policies and aren't terminal actions—for example, ALLOW or DENY.

  * `Must specify at least one destination on Firewall policy rule.`

The `layer4Configs` flag in the firewall policy rule must specify at least one protocol or protocol and destination port.

For more information about troubleshooting firewall policy rules, see [VPC firewall rules troubleshooting](https://docs.cloud.google.com/firewall/docs/using-firewalls#troubleshooting).




## What's next

  * [VPC firewall rules overview](https://docs.cloud.google.com/firewall/docs/firewalls)
  * [Hierarchical firewall policy examples](https://docs.cloud.google.com/firewall/docs/firewall-policies-examples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
