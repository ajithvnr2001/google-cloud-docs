---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/create-manage-mirroring-rules/
title: Create and manage mirroring rules \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:16.068210+00:00
---

# Create and manage mirroring rules  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/create-manage-mirroring-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage mirroring rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage mirroring rules by using the Google Cloud CLI. Before you create a packet mirroring rule, you must create an endpoint group and endpoint group associations. For more information, see [Set up consumer services](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-consumer-service).

## Create and manage mirroring rules for network firewall policies

In this section, learn how to create and manage mirroring rules for [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies).

### Create a firewall policy with a mirroring rule

Create a packet mirroring rule in a network firewall policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * [Compute Security Admin (`roles/compute.securityAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin)



###  Console 

To create a network firewall policy, follow these steps:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your Google Cloud project within your organization.

  3. Click **Create firewall policy**.

  4. In the **Policy name** field, enter a name for the policy.

  5. For **Deployment scope** , select **Global**.

  6. To create mirroring rules for your policy, click **Continue > Continue**.

  7. In the **Add mirroring rules** section, click **Create mirroring rule**.

     1. In the **Priority** field, set the order number for the rule, where `0` is the highest priority.
     2. For **Direction of traffic** , choose **Ingress**.
     3. For **Action on match** , choose **Mirror**.
     4. For **Security profile group** , select the custom mirroring security profile group.
     5. For **Target** , specify the target of the rule.
     6. For **Source** , specify the source filter.
     7. For **Destinations** , specify the destination filters.
     8. For **Protocols and ports** , either specify that the rule applies to all protocols and all destination ports or which protocols and destination ports the rule applies to.
     9. Click **Create**.
  8. If you want to associate the policy with a network, click **Continue** , and then click **Associate policy with networks**. For more information, see [Associate a policy with the network](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#associate).

**Note:** You can associate the policy with networks after it is created.
  9. Click **Create**.




###  gcloud 

To create a mirroring rule in a network firewall policy, use the [`gcloud compute network-firewall-policies mirroring-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/create):
    
    
     gcloud compute network-firewall-policies mirroring-rules create PRIORITY \
         --action ACTION \
         --firewall-policy FIREWALL_POLICY \
         --global-firewall-policy \
         --security-profile-group SECURITY_PROFILE_GROUP \
         --description DESCRIPTION \
         --direction DIRECTION \
         --layer4-configs LAYER4_CONIFG \
         --src-ip-ranges SRC_IP_RANGE \
         --dest-ip-ranges DEST_IP_RANGE
    

Replace the following:

  * `PRIORITY`: the priority of the rule to add.

  * `ACTION`: the action to take if the request matches the match condition. `ACTION` must be `mirror` or `do_not_mirror`.

  * `FIREWALL_POLICY`: the firewall policy ID with which to create a rule.

  * `SECURITY_PROFILE_GROUP`: the name of the security profile group that has a `CUSTOM_MIRRORING` security profile and is used with `mirror` action.

  * `DESCRIPTION`: an optional description for the mirroring rule.

  * `DIRECTION`: indicates whether the rule is an `ingress` or `egress` rule. If the direction isn't specified, it defaults to applying the rule on incoming traffic. For incoming traffic, you cannot specify destination ranges. For outbound traffic, you cannot specify source ranges or source tags.

  * `LAYER4_CONFIG`: a list of destination protocols and ports to which the firewall rule applies.

  * `SRC_IP_RANGE`: the source IP ranges. This is only specified if `DIRECTION` is `ingress`.

  * `DEST_IP_RANGE`: the destination IP ranges. This is only specified if `DIRECTION` is `egress`.




###  Terraform 

To create a mirroring rule, you can use a [`google_compute_network_firewall_policy_packet_mirroring_rule` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_firewall_policy_packet_mirroring_rule).
    
    
    resource "google_compute_network_firewall_policy_packet_mirroring_rule" "default" {
      provider               = google-beta
      firewall_policy        = google_compute_network_firewall_policy.default.name
      priority               = 1000
      action                 = "mirror"
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

### Describe mirroring rule

Describe the network firewall policy mirroring rule at the specified priority.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `compute.firewallPolicies.get`



**Roles**

  * [Compute Security Admin (`roles/compute.securityAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin)
  * [Compute Network Admin (`roles/compute.networkAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin)



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. From the project picker, select your Google Cloud project that contains the global network firewall policy.

  3. Click your policy.

  4. To see the details of a rule, click the priority of the rule.




###  gcloud 

To describe a mirroring rule in a network firewall policy, use the [`gcloud compute network-firewall-policies mirroring-rules describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/describe):
    
    
     gcloud compute network-firewall-policies mirroring-rules describe PRIORITY \
         --firewall-policy FIREWALL_POLICY \
         --global-firewall-policy
    

Replace the following:

  * `PRIORITY`: the priority of the rule to describe

  * `FIREWALL_POLICY`: the firewall policy ID with which to describe the rule




### Update mirroring rule

Update a mirroring rule in a network firewall policy.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * [Compute Security Admin (`roles/compute.securityAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin)



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. From the project picker, select your Google Cloud project that contains the policy.

  3. Click your policy.

  4. In the **Mirroring rules** section, click the priority of rule that you want to update.

  5. Click **Edit**.

  6. After you edit the rule, click **Save**.




###  gcloud 

To update a mirroring rule in a network firewall policy, use the [`gcloud compute network-firewall-policies mirroring-rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/update):
    
    
     gcloud compute network-firewall-policies mirroring-rules update PRIORITY \
         --action ACTION \
         --firewall-policy FIREWALL_POLICY \
         --global-firewall-policy \
         --security-profile-group SECURITY_PROFILE_GROUP \
         --description DESCRIPTION \
         --direction DIRECTION \
         --layer4-configs LAYER4_CONIFG \
         --src-ip-ranges SRC_IP_RANGE \
         --dest-ip-ranges DEST_IP_RANGE
    

Replace the following:

  * `PRIORITY`: the priority of the rule to update.

  * `ACTION`: the action to take if the request matches the match condition. `ACTION` must be `mirror` or `do_not_mirror`.

  * `FIREWALL_POLICY`: the firewall policy ID with which to update a rule.

  * `SECURITY_PROFILE_GROUP`: the name of the security profile group that has a `CUSTOM_MIRRORING` security profile or whether `ACTION` is `mirror`.

  * `DESCRIPTION`: an optional description for the mirroring rule.

  * `DIRECTION`: indicates whether the rule is an `ingress` or `egress` rule. If the direction isn't specified, it defaults to applying the rule on incoming traffic. For incoming traffic, you cannot specify destination ranges. For outbound traffic, you cannot specify source ranges or source tags.

  * `LAYER4_CONFIG`: a list of destination protocols and ports to which the firewall rule will apply.

  * `SRC_IP_RANGE`: the source IP ranges. This is only specified if `DIRECTION` is `ingress`.

  * `DEST_IP_RANGE`: the destination IP ranges. This is only specified if `DIRECTION` is `egress`.




### Delete mirroring rule

Delete the packet mirroring rule at the specified priority.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `compute.firewallPolicies.update`



**Roles**

  * [Compute Security Admin (`roles/compute.securityAdmin`)](https://cloud.google.com/iam/docs/roles-permissions/compute#compute.securityAdmin)



###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. From the project picker, select your Google Cloud project that contains the policy.

  3. Click your policy.

  4. Select the mirroring rule that you want to delete.

  5. Click **Delete**.




###  gcloud 

To delete a mirroring rule from a network firewall policy, use the [`gcloud compute network-firewall-policies mirroring-rules delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/mirroring-rules/delete):
    
    
     gcloud compute network-firewall-policies mirroring-rules delete PRIORITY \
         --firewall-policy FIREWALL_POLICY \
         --global-firewall-policy
    

Replace the following:

  * `PRIORITY`: the priority of the rule to delete

  * `FIREWALL_POLICY`: the firewall policy ID with which to delete a rule




## What's next

  * [Firewall policies and rules overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/firewall-policies-overview)
  * [Network Security Integration overview](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)
  * [Monitor out-of-band integration](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/monitor-out-of-band-integration)
  * [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
