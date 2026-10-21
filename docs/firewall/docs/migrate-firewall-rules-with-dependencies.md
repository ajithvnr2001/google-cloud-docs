---
url: https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-with-dependencies/
title: Migrate VPC firewall rules that use network tags and service accounts \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:14.541707+00:00
---

# Migrate VPC firewall rules that use network tags and service accounts  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-with-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Migrate VPC firewall rules that use network tags and service accounts Stay organized with collections  Save and categorize content based on your preferences. 

To centralize management and consistently enforce security policies across your Virtual Private Cloud (VPC) networks, migrate your VPC firewall rules that use network tags and source service accounts to a global network firewall policy. By doing so, you can reduce your attack surface, optimize your firewall configurations, and tighten security boundaries by identifying and addressing overly permissive rules.

This document is intended for network administrators, security engineers, and security architects who configure and manage network security policies.

To migrate rules that don't use network tags or service accounts, see [Migrate VPC firewall rules that don't use network tags and service accounts](https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-no-dependencies).

To complete this migration, you perform the following tasks:

  1. Assess your environment.
  2. List existing network tags and service accounts.
  3. Create secure tags for each network tag and source service account.
  4. Map the network tags and service accounts to the secure tags that you create.
  5. Bind secure tags to virtual machine (VM) instances.
  6. Migrate VPC firewall rules to a global network firewall policy.
  7. Review the new network firewall policy.
  8. Complete the postmigration tasks.



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

Before you migrate your VPC firewall rules to a global network firewall policy, assess your existing environment and Identity and Access Management (IAM) roles and permissions:

  1. Identify the number of VPC firewall rules in your VPC network.
  2. Make a note of the priorities associated with each VPC firewall rule.
  3. Make sure that you have the required IAM roles and permissions to [create, associate, modify, and view global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies#iam).
  4. Make sure that you have the required IAM roles and permissions to [create, update, and delete secure tag definitions](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#iam).

The following table provides a summary of the various roles that are required to create and manage secure tags:

Role name | Tasks performed  
---|---  
[Tag Administrator role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) | Create, update, and delete tag definitions. For more information, see [Administer tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#required-permissions-administer).  
[Tag Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) | View tag definitions and tags that are attached to resources.  
[Tag User role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) | Add and remove tags that are attached to resources.  



## List existing network tags and service accounts

Determine whether your VPC firewall rules use any network tags or service accounts, and create a JSON file to save the details of the existing network tags and service accounts.

To export the network tags and service accounts in your network to a mapping JSON file, use the [`gcloud beta compute firewall-rules migrate` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-rules/migrate) with the `--export-tag-mapping` flag:
    
    
    gcloud beta compute firewall-rules migrate \
        --source-network=NETWORK_NAME \
        --export-tag-mapping \
        --tag-mapping-file=TAG_MAPPING_FILE
    

Replace the following:

  * `NETWORK_NAME`: the name of the VPC network containing the VPC firewall rules that you want to migrate.
  * `TAG_MAPPING_FILE`: the name of the mapping JSON file.



If your VPC firewall rules contain only service accounts, the generated JSON file contains only service accounts. Similarly, if your VPC firewall rules contain only network tags, the generated JSON file contains only network tags. The service accounts are prefixed with `sa`, and network tags don't have any prefix.

For example, the following generated JSON file contains a network tag `sql-server` and a service account `example@example.com`.
    
    
    {"sql-server": null, "sa:example@example.com": null}
    

## Create secure tags

Based on the network tags and source service accounts listed in the mapping file, you must create the corresponding secure tags in your network.

**Note:** Creating secure tags for target service accounts is optional—you can choose to retain target service accounts as is.

The new secure tags serve as a replacement to the network tags and service accounts and preserve the original network configuration after migration.

As a principal with the Tag Administrator role, for each network tag and service account, create the corresponding secure tag key-value pair.

To create a secure tag key and value for each network tag and service account, use the [`gcloud resource-manager tags keys create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/keys/create) and the [`gcloud resource-manager tags values create` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/values/create):
    
    
    gcloud resource-manager tags keys create TAG_KEY \
        --parent=organizations/ORGANIZATION_ID \
        --purpose=GCE_FIREWALL \
        --purpose-data=network=PROJECT_ID/NETWORK_NAME
    
    gcloud resource-manager tags values create TAG_VALUE \
        --parent=ORGANIZATION_ID/TAG_KEY
    

Replace the following:

  * `TAG_KEY`: the name of the secure tag key.
  * `ORGANIZATION_ID`: the ID of the organization.
  * `PROJECT_ID`: the ID of the project.
  * `NETWORK_NAME`: the name of the VPC network.
  * `TAG_VALUE`: the value to assign to the secure tag key.



For example, if you have a VPC firewall rule with a network tag called `sql-server`, create a corresponding secure tag key-value pair of `sql-server:production`.
    
    
    gcloud resource-manager tags keys create sql-server \
        --parent=organizations/123456 \
        --purpose=GCE_FIREWALL \
        --purpose-data=network=test-project/test-network
    
    gcloud resource-manager tags values create production \
        --parent=123456/sql-server
    

**Note:** When you create secure tag keys, the value of the `--purpose` field must be set to `GCE_FIREWALL`. Each of these secure tags must have a single target VPC network and the secure tags can only be associated with the network interfaces in that VPC network.

## Map network tags and service accounts to secure tags

After creating IAM-governed secure tags for each network tag and service account used by your VPC firewall rules, you must map the secure tags to the corresponding network tags and service accounts in the mapping JSON file.

Edit the JSON file to map the network tags and the service accounts to the corresponding secure tags.
    
    
    {"sql-server": "tagValues/yyyyy", "sa:example@example.com": "tagValues/zzzzz"}
    

For example, the following JSON file maps the network tag `sql-server` to the secure tag value of the key `sql-server` and the service account `example@example.com` to the secure tag value of the key `example@example.com`:
    
    
    {"sql-server": "tagValues/production", "sa:example@example.com": "tagValues/example"}
    

## Bind secure tags to VMs

Based on the tag mapping JSON file, bind the newly created secure tags to the VMs to which the existing network tags are attached:

  1. As a principal with the Tag Administrator role, do the following:

     1. Review the [permissions required](https://docs.cloud.google.com/vpc/docs/tags-firewalls-overview#iam) to attach secure tags to Google Cloud resources.
     2. [Assign the Tag User role to the principal](https://docs.cloud.google.com/vpc/docs/use-tags-for-firewalls#grant-tag-roles) that uses the secure tags and binds the secure tags to VMs.
  2. As a principal with the Tag User role, bind the secure tags to VM instances using the [`gcloud beta compute firewall-rules migrate` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-rules/migrate#--bind-tags-to-instances) with the `--bind-tags-to-instances` flag:
         
         gcloud beta compute firewall-rules migrate \
             --source-network=NETWORK_NAME \
             --bind-tags-to-instances \
             --tag-mapping-file=TAG_MAPPING_FILE
         

Replace the following:

     * `NETWORK_NAME`: the name of the VPC network.
     * `TAG_MAPPING_FILE`: the name of the mapping JSON file.

**Note:** The `--bind-tags-to-instances` flag binds the secure tags to only running VMs. In addition, if VMs in your network are created using instance templates or if the VMs are a part of a Google Kubernetes Engine (GKE) cluster, you must manually bind the secure tags.

## Migrate VPC firewall rules to a global network firewall policy

To migrate VPC firewall rules to a global network firewall policy, use the [`gcloud beta compute firewall-rules migrate` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/firewall-rules/migrate):
    
    
    gcloud beta compute firewall-rules migrate \
        --source-network=NETWORK_NAME \
        --target-firewall-policy=POLICY_NAME \
        --tag-mapping-file=TAG_MAPPING_FILE
    

Replace the following:

  * `NETWORK_NAME`: the name of the VPC network containing the VPC firewall rules that you want to migrate.
  * `POLICY_NAME`: the name of the global network firewall policy to create during migration.
  * `TAG_MAPPING_FILE`: the name of the mapping JSON file.



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

Before you associate the newly created policy to a VPC network, Google recommends that you review the policy to ensure that the migration process has completed accurately.

Verify the following:

  * The firewall policy rules configuration is correct, and the following rule components are properly migrated for each rule:

    * Relative priority
    * Direction of traffic
    * Action on match
    * Log settings
    * Target parameters
    * Source parameters (for ingress rules)
    * Destination parameters (for egress rules)
    * Protocol and port constraints
  * Verify whether the secure tags are attached to the correct VM. To verify this, use the [`gcloud resource-manager tags bindings list` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/list):
        
        gcloud resource-manager tags bindings list \
            --location=ZONE_ID \
            --parent=//compute.googleapis.com/projects/PROJECT_ID/zones/ZONE_ID/instances/INSTANCE_NAME \
            --effective
        

Replace the following:

    * `ZONE_ID`: the zone of the VM.
    * `PROJECT_ID`: the ID of the project.
    * `INSTANCE_NAME`: the name of the VM.



## Postmigration tasks

To activate and use the new global network firewall policy, complete the postmigration tasks. For more information, see [Postmigration tasks](https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-no-dependencies#postmigration).

## What's next

  * Learn more about [migrating VPC firewall rules](https://docs.cloud.google.com/firewall/docs/migrate-vpc-firewall-rules-overview).
  * Migrate [VPC firewall rules without any dependencies](https://docs.cloud.google.com/firewall/docs/migrate-firewall-rules-no-dependencies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
