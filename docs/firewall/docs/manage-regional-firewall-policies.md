---
url: https://docs.cloud.google.com/firewall/docs/manage-regional-firewall-policies/
title: Manage regional network firewall policies \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:07.863373+00:00
---

# Manage regional network firewall policies  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-regional-firewall-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage regional network firewall policies Stay organized with collections  Save and categorize content based on your preferences. 

To control network traffic within specific regions, use regional network firewall policies and their rules. This page provides instructions to clone, list, describe, view, update, and delete regional network firewall policy associations and rules.

Before you read this page, ensure you are familiar with the concepts described in the [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies).

## Firewall policy tasks

This section describes how to manage regional network firewall policies.

### Describe a regional network firewall policy

You can view details about a regional network firewall policy, including the policy rules and associated rule attributes. All these rule attributes are counted as part of the rule attribute quota. For more information, see "Rule attributes per regional network firewall policy" in the [Per firewall policy](https://docs.cloud.google.com/firewall/docs/quotas#per-firewall-policy-quotas) table. In addition, you can view the priorities of the existing VPC network associations.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.get`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the firewall policy or project containing the firewall policy _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the regional network firewall policy.

  3. Click your policy.




###  gcloud 
    
    
    gcloud compute network-firewall-policies describe POLICY_NAME \
        --region=REGION_NAME
    

### Update a regional network firewall policy description

The only policy field that can be updated is the **Description** field.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the regional network firewall policy.

  3. Click your policy.

  4. Click **Edit**.

  5. In the **Description** field, modify the description.

  6. Click **Save**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies update POLICY_NAME \
        --description DESCRIPTION \
        --region=REGION_NAME
    

### List regional network firewall policies

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.list`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the firewall policy or project containing the firewall policy _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy.

The **Network firewall policies** section shows the policies available in your project.




###  gcloud 
    
    
    gcloud compute network-firewall-policies list \
        --regions=LIST_OF_REGIONS
    

Replace `LIST_OF_REGIONS` with a comma-separated list of regions for which you want to list the policies.

### Delete the network association

To stop enforcement of a firewall policy on a network, delete the association.

However, if you intend to _swap out_ one firewall policy for another, you need not delete the existing association first. Deleting that association leaves a period of time where neither policy is enforced. Instead, replace the existing policy when you [associate a new policy](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#associate).

To delete an association between a regional network firewall policy and a region of a VPC network, follow the steps mentioned in this section. Rules in the regional network firewall policy don't apply to new connections after its association is deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.use`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the project containing the network



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
        --name ASSOCIATION_NAME \
        --firewall-policy POLICY_NAME \
        --firewall-policy-region=POLICY_REGION
    

### Delete a regional network firewall policy

Before you can delete a regional network firewall policy, you must delete all of its associations.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.delete`



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
        --region=REGION_NAME
    

Replace the following:

  * `POLICY_NAME`: the name of the regional network firewall policy.
  * `REGION_NAME`: the region of the regional network firewall policy.



## Firewall policy rule tasks

This section describes how to manage regional network firewall policy rules.

### Clone rules from one policy to another

Cloning copies the rules from a source policy to a target policy, replacing all existing rules in the target policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.cloneRules`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy.

  3. Click the policy that you want to copy rules from.

  4. Click **Clone** at the top of the screen.

  5. Provide the name of a target policy.

  6. If you want to associate the new policy immediately, click **Continue > Associate**.

  7. In the **Associate policy with VPC networks** page, select the networks and click **Associate**.

  8. Click **Continue**.

  9. Click **Clone**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies clone-rules TARGET_POLICY \
        --region=TARGET_POLICY_REGION \
        --source-firewall-policy=SOURCE_POLICY
    

Replace the following:

  * `TARGET_POLICY`: the name of the target policy.
  * `TARGET_POLICY_REGION`: the region of the target policy.
  * `SOURCE_POLICY`: the URL of the source policy.



### Describe a rule

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.get`



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
        --firewall-policy-region=POLICY_REGION
    

Replace the following:

  * `PRIORITY`: the priority number that uniquely identifies the rule.
  * `POLICY_NAME`: the name of the policy that contains the rule.
  * `POLICY_REGION`: the region of the policy that contains the rule.



### Update a rule

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.get`
  * `compute.regionFirewallPolicies.update`



**Roles**

  * Compute Security Admin (`roles/compute.securityAdmin`) on the firewall policy or project containing the firewall policy



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the regional network firewall policy.

  3. Click the name of the regional network firewall policy that contains the rule to update.

  4. Click the priority of the rule.

  5. Click **Edit**.

  6. Modify the firewall rule fields that you want to change. For descriptions about each field, see one of the following:

     * [Create an ingress rule for VM targets](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-ingress-rule-target-vm)
     * [Create an ingress rule for internal Application Load Balancer and internal proxy Network Load Balancer targets](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-ingress-rule-target-lb)
     * [Create an egress rule for VM targets](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-egress-rule-target-vm)
  7. Click **Save**.




###  gcloud 
    
    
    gcloud compute network-firewall-policies rules update PRIORITY \
        --firewall-policy=POLICY_NAME \
        --firewall-policy-region=POLICY_REGION \
        [...other flags that you want to modify...]
    

Replace the following:

  * `PRIORITY`: the priority number that uniquely identifies the rule.
  * `POLICY_NAME`: the name of the policy that contains the rule.
  * `POLICY_REGION`: the region of the policy that contains the rule.



Supply the flags that you want to modify. For flag descriptions, see one of the following:

  * [Create an ingress rule for VM targets](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-ingress-rule-target-vm)
  * [Create an ingress rule for internal Application Load Balancer and internal proxy Network Load Balancer targets](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-ingress-rule-target-lb)
  * [Create an egress rule for VM targets](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#create-egress-rule-target-vm)



### Delete a rule

Deleting a rule from a policy causes the rule to no longer apply to new connections to or from the rule's target.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.regionFirewallPolicies.update`



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
        --firewall-policy-region=POLICY_REGION
    

Replace the following:

  * `PRIORITY`: the priority number that uniquely identifies the rule.
  * `POLICY_NAME`: the name of the policy that contains the rule.
  * `POLICY_REGION`: the region of the policy that contains the rule.



## Get effective firewall rules for a region of a network

You can view all hierarchical firewall policy rules, VPC firewall rules, global network firewall policy rules, and regional network firewall policy rules that apply to a specific region of a VPC network.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.networks.getEffectiveFirewalls`
  * `compute.networks.getRegionEffectiveFirewalls`



**Roles**

  * Compute Network User (`roles/compute.networkUser`) on the project containing the network _or_
  * Compute Network Viewer (`roles/compute.networkViewer`) on the project containing the network _or_
  * Compute Security Admin (`roles/compute.securityAdmin`) on the project containing the network _or_
  * Compute Viewer (`roles/compute.viewer`) on the project containing the network



###  gcloud 
    
    
    gcloud compute network-firewall-policies get-effective-firewalls \
        --region=REGION_NAME \
        --network=NETWORK_NAME
    

Replace the following:

  * `REGION_NAME`: the region for which you want to view the effective rules.
  * `NETWORK_NAME`: the network for which you want to view the effective rules.



## What's next

  * [Regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies)
  * [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies)
  * [Create global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
