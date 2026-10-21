---
url: https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-no-dependencies/
title: Migrate VPC firewall rules that don't use network tags and service accounts \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:24:00.495726+00:00
---

# Migrate VPC firewall rules that don't use network tags and service accounts  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-no-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Migrate VPC firewall rules that don't use network tags and service accounts Stay organized with collections  Save and categorize content based on your preferences. 

To simplify operational overhead and centralize management, you can migrate your existing Virtual Private Cloud (VPC) firewall rules to a global network firewall policy. This document describes how to complete this migration for rules that don't use network tags or service accounts.

This document is intended for network administrators and security engineers who migrate VPC firewall rules that use network tags and service accounts.

To complete this migration, you perform the following tasks:

  1. Assess your environment.
  2. Migrate the VPC firewall rules.
  3. Review the new global network firewall policy.
  4. Complete the postmigration tasks.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Make sure that you have the [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/compute.securityAdmin`).



## Assess your environment

  1. Identify the number of existing VPC firewall rules in your network.
  2. Make a note of the priorities associated with each VPC firewall rule.
  3. Make sure that you have the required Identity and Access Management (IAM) roles and permissions to [create, associate, modify, and view global network firewall policies](https://docs.cloud.google.com/vpc/docs/network-firewall-policies#iam).



## Migrate the VPC firewall rules

After assessing your environment, migrate your VPC firewall rules to a global network firewall policy by using the [`compute firewall-rules migrate` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-rules/migrate).
    
    
    gcloud beta compute firewall-rules migrate \
        --source-network=NETWORK_NAME \
        --target-firewall-policy=POLICY_NAME
    

Replace the following:

  * `NETWORK_NAME`: the name of your VPC network containing the VPC firewall rules that you want to migrate.
  * `POLICY_NAME`: the name of the global network firewall policy to create during migration.



### Exclude firewall rules from migration

To exclude specific firewall rules from migration, use the `gcloud beta compute firewall-rules migrate` command with the `--exclusion-patterns-file` flag:
    
    
    gcloud beta compute firewall-rules migrate \
        --source-network=NETWORK_NAME \
        --target-firewall-policy=POLICY_NAME \
        --exclusion-patterns-file=EXCLUSION_PATTERNS_FILE
    

Replace the following:

  * `NETWORK_NAME`: the name of your VPC network that contains the VPC firewall rules that you want to migrate.
  * `POLICY_NAME`: the name of the global network firewall policy to create during migration.
  * `EXCLUSION_PATTERNS_FILE`: the name of the file that contains regular expressions that define VPC firewall naming patterns to exclude from migration. Make sure to specify the full path of the file. Firewall rules that match the specified patterns are skipped.

When defining the exclusion patterns, consider the following:

    * Each regular expression must be on its own line and represent a single firewall naming pattern.
    * The regular expressions don't contain any leading or trailing whitespaces.



### View excluded firewall rules

Based on the excluded firewall rule naming patterns, the migration tool doesn't migrate some firewall rules, such as Google Kubernetes Engine (GKE) firewall rules. To export the list of excluded firewall rule naming patterns, use the`gcloud beta compute firewall-rules migrate` command with the `--export-exclusion-patterns` and the `--exclusion-patterns-file` flags.
    
    
    gcloud beta compute firewall-rules migrate \
        --source-network=NETWORK_NAME \
        --target-firewall-policy=POLICY_NAME \
        --exclusion-patterns-file=EXCLUSION_PATTERNS_FILE \
        --export-exclusion-patterns
    

Replace the following:

  * `NETWORK_NAME`: the name of your VPC network that contains the VPC firewall rules that you want to migrate.
  * `POLICY_NAME`: the name of the global network firewall policy to create during migration.
  * `EXCLUSION_PATTERNS_FILE`: the path of the file where the following excluded firewall rule naming patterns are exported.
        
        gke-(.+)-ipv6-all
        gke-(.+)-(.+)-((master)|(vms)|(all)|(inkubelet)|(exkubelet)|(mcsd))
        k8s-fw-(l7-)?(.+)
        k8s-(.+)-((node)|(http)|(node-http))-hc
        (.+)-hc
        k8s2-(.+)-(.+)-(.+)-(.+)(-fw)?
        k8s2-(.+)-l4-shared-hc-fw
        gke((gw)|(mcg))1-l7-(.+)-(.+)
        




To migrate excluded firewall rules that match a specific pattern, remove the pattern from the exported list and run the `gcloud beta compute firewall-rules migrate` command with the `--exclusion-patterns-file` flag.

### Force migration while preserving evaluation order

During migration, if an excluded firewall rule's evaluation order falls between the evaluation orders of user-specified firewall rules, the migration fails.This happens because the excluded firewall rules are not migrated, and the migration tool cannot preserve the original evaluation order of user-defined rules in the new network firewall policy.

For example, if your firewall rules have the following priorities, the migration fails.

  * A user-specified rule with priority 100
  * An excluded rule with priority 200
  * A user-specified rule with priority 300



To force the migration tool migrate the user-specified rules while preserving their original evaluation order and ignoring excluded firewall rules, use the `gcloud beta compute firewall-rules migrate` command with the `--force` flag.
    
    
    gcloud beta compute firewall-rules migrate \
        --source-network=NETWORK_NAME \
        --target-firewall-policy=POLICY_NAME \
        --force
    

Replace the following:

  * `NETWORK_NAME`: the name of your VPC network that contains the VPC firewall rules that you want to migrate.
  * `POLICY_NAME`: the name of the global network firewall policy to create during migration.



## Review the new global network firewall policy

Before you attach the new global network firewall policy to a VPC network, Google recommends that you review the policy to help ensure that the migration process has completed accurately.

Verify the firewall policy rules configuration, and check if the following rule components are properly migrated for each rule:

  * Relative priority
  * Direction of traffic
  * Action on match
  * Log settings
  * Target parameters
  * Source parameters (for ingress rules)
  * Destination parameters (for egress rules)
  * Protocol and port constraints



For more information about the components of a firewall policy rule, see [Firewall policy rule components](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details).

**Note:** The migration command does not apply to VPC firewall rules that are automatically created by Google Kubernetes Engine (GKE).

## Postmigration tasks

To activate and use your global network firewall policy, you must complete the postmigration tasks covered in the following sections.

### Associate the global network firewall policy with your network

The migration tool creates the global network firewall policy based on the existing VPC firewall rules. You must manually associate the policy with the required VPC network to activate the policy rules for any VMs within that network. To associate the global network firewall policy, use the [`compute network-firewall-policies associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create).
    
    
    gcloud compute network-firewall-policies associations create \
        --firewall-policy=POLICY_NAME \
        --network=NETWORK_NAME \
        --global-firewall-policy \
        --replace-association-on-target
    

Replace the following:

  * `POLICY_NAME`: the name of the global network policy that you want to associate with your VPC network.
  * `NETWORK_NAME`: the name of your VPC network.

**Note:** The `--replace-association-on-target` flag specifies that any existing association is deleted when you create the new association.

For more information about associating a global network firewall policy to a VPC network, see [Associate a policy with the network](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#associate).

### Change the policy and rule evaluation order

By default, Cloud Next Generation Firewall (Cloud NGFW) evaluates the VPC firewall rules before it evaluates a global network firewall policy. To make sure that global network firewall policies take precedence over VPC firewall rules, use the [`compute networks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/update) to change the rule evaluation order.
    
    
    gcloud compute networks update NETWORK_NAME \
        --network-firewall-policy-enforcement-order=BEFORE_CLASSIC_FIREWALL
    

Replace `NETWORK_NAME` with the name of your VPC network.

To verify whether the global network firewall policy is evaluated before the VPC firewall rules, use the [`compute networks get-effective-firewalls` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/get-effective-firewalls).
    
    
    gcloud compute networks get-effective-firewalls NETWORK_NAME
    

In the output of the preceding command, if `TYPE: network-firewall-policy` is displayed before `TYPE: network-firewall`, then the global network firewall policy is evaluated first.

For more information about the policy and rule evaluation order, see [Evaluation order for firewall policies and rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order).

### Enable logging of firewall rules

Logging helps you to determine whether a firewall rule is functioning as intended. The migration tool retains the logging status of the existing VPC firewall rules when it creates the new global network firewall policy. Make sure that logging is enabled for the rules inside the global network firewall policy. To enable logging for firewall policy rules, use the [`compute network-firewall-policies rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/update).
    
    
    gcloud compute network-firewall-policies rules update PRIORITY \
        --firewall-policy=POLICY_NAME \
        --enable-logging \
        --global-firewall-policy
    

Replace the following:

  * `PRIORITY`: the priority of the rule to be updated.
  * `POLICY_NAME`: the name of the global network firewall policy whose rule you want to update.



### Test your global network firewall policy

Before deleting your VPC firewall rules, test your global network firewall policy to check whether the policy rules are working according to your expectations for any traffic that matches the rules.

Do the following:

  1. Ensure that you have enabled logging on VPC firewall rules and the global network firewall policy.
  2. Change the rule evaluation order, so that the global network firewall policy is evaluated before your VPC firewall rules.
  3. [Monitor the logs](https://docs.cloud.google.com/firewall/docs/using-firewall-rules-logging#viewing_logs) to verify that the global network firewall policy has hit counts and the VPC firewall rules are shadowed.



### Delete the VPC firewall rules from your network

Google recommends that you disable the VPC firewall rules first before entirely deleting them. You can revert to those rules if the global network firewall policy created by the migration tool fails to provide the expected results.

To disable a VPC firewall rule, use the [`compute firewall-rules update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/update).
    
    
    gcloud compute firewall-rules update RULE_NAME --disabled
    

Replace `RULE_NAME` with the name of the VPC firewall rule to be disabled.

To delete a VPC firewall rule, use the [`compute firewall-rules delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/delete).
    
    
    gcloud compute firewall-rules delete RULE_NAME
    

## What's next

  * Learn more about [migrating VPC firewall rules](https://docs.cloud.google.com/firewall/docs/migrate-vpc-firewall-rules-overview).
  * Migrate [VPC firewall rules with dependencies](https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-with-dependencies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
