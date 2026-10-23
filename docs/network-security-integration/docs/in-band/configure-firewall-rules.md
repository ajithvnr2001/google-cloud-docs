---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-firewall-rules/
title: Create and manage firewall rules \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:07.577352+00:00
---

# Create and manage firewall rules  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-firewall-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

To inspect consumers' network traffic, you use [firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview) to redirect the traffic to the VPC's intercept endpoint group. The traffic then goes through the producer's intercept deployment group to their compute resources.

This page describes how to configure and manage global network firewall policies and rules. If you want to create hierarchical firewall policies and rules, see [Use hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies).

## Before you begin

  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [ Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your Google Cloud project.

  * [Enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your Google Cloud project.

  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).

  * Create a [security profile group](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-security-profile-groups).




### Roles

To create, view, or delete firewall rules, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview#iam-roles) on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the following project-level [Compute Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin) (`roles/compute.securityAdmin`), [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`), and [Compute Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) roles:

  * `compute.networks.get`
  * `compute.networks.list`
  * `compute.firewallPolicies.create`
  * `compute.firewallPolicies.update`
  * `compute.firewallPolicies.removeAssociation`



## Create firewall policies and rules

You create a firewall policy and a rule with the `APPLY_SECURITY_PROFILE_GROUP` action.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.create`
  * `compute.firewallPolicies.update`
  * `compute.firewallPolicies.get`



**Roles**

  * `compute.securityAdmin` on the project where you want to create the policy



###  Console 

To create a network firewall policy, follow these steps:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your project within your organization.

  3. Click **Create firewall policy**.

  4. In the **Name** field, enter a name for the policy.

  5. For **Deployment scope** , select **Global.**

  6. To create rules for your policy, click **Continue** , and then click **Add rule**.

     1. In the **Priority** field, set the order number for the rule, where `0` is the highest priority.
     2. For **Direction of traffic** , choose **Ingress**.
     3. For **Action on match** , choose **Proceed to L7 inspection**.
     4. For **Purpose** , choose **NSI in-band**.
     5. For **Security profile group** , select the custom intercept security profile group.
     6. For **Target type** , specify the target of the rule.
     7. For **Source filters** , specify the source filter.
     8. For **Destinations** , specify the destination filters.
     9. For **Protocols and ports** , either specify that the rule applies to all protocols and all destination ports or specify to which protocols and destination ports the rule applies.
     10. Click **Create**.
  7. Click **Add rule** to add another rule.

  8. If you want to associate the policy with a network, click **Continue** , and then click **Associate policy with VPC networks**.

  9. Click **Create**.




For more information, see [Create global network firewall rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#create-rules).

###  gcloud 

To create a network firewall policy, use the [`gcloud compute firewall-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create):
    
    
    gcloud compute network-firewall-policies create FIREWALL_POLICY
    

To create a firewall rule, use the [`gcloud compute network-firewall-policies rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/create):
    
    
    gcloud compute network-firewall-policies rules create PRIORITY \
        --action APPLY_SECURITY_PROFILE_GROUP \
        --firewall-policy FIREWALL_POLICY \
        --security-profile-group organizations/ORGANIZATION_ID/locations/global/securityProfileGroups/SECURITY_PROFILE_GROUP_ID \
        --direction DIRECTION \
        --layer4-configs LAYER4_CONIFG \
        --src-ip-ranges SRC_IP_RANGE \
        [--dest-ip-ranges DEST_IP_RANGE] \
        --global-firewall-policy
    

Replace the following:

  * `PRIORITY`: the priority of the rule to add.

  * `FIREWALL_POLICY`: the firewall policy ID with which to create a rule.

  * `ORGANIZATION_ID`: the ID of the organization where the security profile group is created.

  * `SECURITY_PROFILE_GROUP_ID`: the ID of the security profile group that has a `custom-intercept-profile` action.

  * `DIRECTION`: indicates whether the rule is an `ingress` or `egress` rule. If the direction is not specified, it defaults to applying the rule on incoming traffic. For incoming traffic, you cannot specify destination ranges. For outbound traffic, you cannot specify source ranges or source tags.

  * `LAYER4_CONFIG`: a list of destination protocols and ports to which the firewall rule applies.

  * `SRC_IP_RANGE`: the source IP ranges. This is only specified if `DIRECTION` is `ingress`.

  * `DEST_IP_RANGE`: the destination IP ranges. This is only specified if `DIRECTION` is `egress`.




###  Terraform 

To create a firewall policy, you can use a [`google_compute_firewall_policy` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy).
    
    
    resource "google_compute_network_firewall_policy" "default" {
      name = "firewall-policy"
    }

To create a firewall policy rule, you can use a [`google_compute_network_firewall_policy_rule` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_firewall_policy_rule).
    
    
    resource "google_compute_network_firewall_policy_rule" "default" {
      firewall_policy        = google_compute_network_firewall_policy.default.name
      priority               = 1000
      action                 = "apply_security_profile_group"
      direction              = "INGRESS"
      security_profile_group = google_network_security_security_profile_group.default.id
    
      match {
        layer4_configs {
          ip_protocol = "tcp"
          ports       = ["80"]
        }
        src_ip_ranges = ["10.10.0.0/16"]
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Describe firewall policies and rules

You can see all the details of a policy, including all its firewall rules.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.get`



**Roles**

  * `compute.networkAdmin`
  * `compute.securityAdmin` on the project



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. From the project picker, select your project that contains the global network firewall policy.

  3. Click your policy.

  4. To see the details of a rule, click the priority of the rule.




###  gcloud 

To describe a firewall policy, use the [`gcloud compute network-firewall-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/describe):
    
    
    gcloud compute network-firewall-policies describe FIREWALL_POLICY
    

To describe a firewall rule, use the [`gcloud compute network-firewall-policies rules describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/describe):
    
    
    gcloud compute network-firewall-policies rules describe PRIORITY \
        --firewall-policy FIREWALL_POLICY
    

Replace `FIREWALL_POLICY` with the firewall policy ID with where the rule is defined.

## Delete firewall policies and rules

You can delete a policy and its firewall rules. You must delete all associations on an organization firewall policy before you can delete it.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.firewallPolicies.removeAssociation`
  * `compute.firewallPolicies.update`



**Roles**

  * `compute.securityAdmin` on the project



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. From the project picker, select your project that contains the policy.

  3. Click your policy.

  4. Select the rule that you want to delete.

  5. Click **Delete**.

  6. Click the **Associations** tab.

  7. Select the association that you want to delete.

  8. Click **Remove Associations**.

  9. After all associations are removed, click **Delete**.




###  gcloud 

To delete a firewall rule, use the [`gcloud compute network-firewall-policies rules delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/delete):
    
    
    gcloud compute network-firewall-policies rules delete PRIORITY \
        --firewall-policy FIREWALL_POLICY
    

Replace `FIREWALL_POLICY` with the firewall policy ID with where the rule is defined.

To delete a firewall policy, use the [`gcloud compute network-firewall-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/delete):
    
    
    gcloud compute network-firewall-policies delete FIREWALL_POLICY
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
