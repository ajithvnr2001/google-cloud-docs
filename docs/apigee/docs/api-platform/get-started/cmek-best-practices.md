---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-best-practices/
title: Best practices for Apigee CMEK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:46.762081+00:00
---

# Best practices for Apigee CMEK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Best practices for Apigee CMEK Stay organized with collections  Save and categorize content based on your preferences. 

This page describes CMEK best practices with Apigee. 

**Important:** `apigeecli` is community-contributed and is **not officially supported** by Google Cloud Support. Issues encountered while using this tool should be directed to the GitHub community: [ `apigeecli` Support](https://github.com/apigee/apigeecli?tab=readme-ov-file#support). 

## Risk prevention

Currently, Apigee supports a restricted set of customer-managed encryption key functionality. To **prevent accidental deletion** of CMEK keys or key versions, we recommend you implement the following: 

  * **Tighten access controls:** Limit the [ `roles/cloudkms.admin`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) role or key destroy/update permissions Do to only trusted admins or senior team members. 
  * **Regularly audit permissions:** Ensure permissions are not inadvertently expanded over time. 
  * **Automatic key deletion:** Do not set up automations to automatically delete/disable keys. 



## Set up key destruction duration and rotation 

  * **Consider extending the default destruction duration:** The default scheduled destruction period is 30 days. Setting a custom destruction duration during key creation or [enforcing a longer duration](https://docs.cloud.google.com/kms/docs/creating-keys#soft_delete) via organization policies can provide more time for recovery in case of accidental deletion. If you believe longer destruction times impose more risk, note that longer destruction duration also prevents you from accidentally deleting the key. You can balance the benefit and risk to see what duration works for you the best. 
  * **Require keys to be disabled before destruction:** We recommend disabling key versions before scheduling them for destruction. This helps to validate that the key isn't in active use and is an important step in determining whether it's safe to destroy a key version. 
  * **Implement key rotation:** Regularly rotating keys limits the impact of a potential compromise. In the event that a key is compromised, regular rotation limits the number of actual messages vulnerable to compromise. 



## Key rotation in Apigee

The primary purpose of key rotation is to reduce the amount of data encrypted with a single key, not to fully replace the old key version. For both runtime keys and control plane keys, the original key version remains tied to the resource from the moment it was created. 

### Illustrative examples

  * An Apigee instance will always use the primary CMEK key version that was active at the time of its creation, even after key rotation. 
  * A proxy bundle will continue to use the primary CMEK key version that was active when it was first created. However, if this proxy bundle is modified after key rotation, any new data within it will be encrypted with the new primary key version. 



### Current limitation: no automatic re-encryption

It's important to note that Apigee currently does not support automatic re-encryption of existing data when a key is rotated. Only a limited amount of new data will be encrypted with the new primary key version. The majority of your data, such as analytics, runtime disk data, and older proxy revisions, will still be encrypted with the old key version. 

## Key disablement

Disabling or destroying keys will disrupt Apigee functionality. If you disable the key first, you can re-enable it if it's a false alarm. 

If you suspect a key (or key version) compromise:

  * **High-risk scenario:** If you believe your Apigee data is sensitive and an attacker has a high chance of exploiting it, immediately [disable the key](https://docs.cloud.google.com/kms/docs/enable-disable) and [revoke access](https://docs.cloud.google.com/kms/docs/iam#revoking_access_to_a_resource) to it. You should disable the key first before you recreate an `apigee` instance and `apigee` org. 
  * **Low-risk scenario:** If minimizing downtime is more important than the potential risk, you should recreate the `apigee` instance and `apigee` org first before you disable/delete the CMEK. See below on how to proactively prevent downtime by investing in backup/restore. 
  * **Contact support:** It's recommended that you contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/) when you believe a key is compromised and you need to disable it. 



Check the impact of disabling/revoking/destroying a key below. After disabling the key, you will need to recreate your `apigee` org/instances. See best practices. 

  * **Runtime CMEK compromise:** Create new instances with a new CMEK, then delete the original instances as well as the old runtime CMEK after traffic is migrated. 
  * **All CMEK compromise:** Create a new `apigee` organization with a new CMEK key, replicate your configuration, shift traffic, and then shut down the old organization and disable/delete your original CMEK. 
  * **Contact[Google Cloud Customer Care](https://cloud.google.com/support-hub/)**: If the API for delete/recreate instances or `apigee` org takes a very long time, contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/). 



### Impact of key disablement/revoke/destroy

Disabling, revoking or destroying the key will make Apigee not function properly. The impacts are as follows: 

  * **Disabling/revoking/destroying the entire key:** Apigee's customer-facing APIs will stop functioning immediately. Internal systems will fail within minutes, impacting proxy deployment, runtime traffic, analytics, and API security. The instance will become completely unstartable in a few weeks due to disk remount issues. 
  * **Disabling/revoking/destroying a key version (including both primary key version or previous key version):** Apigee's customer-facing APIs using that key version will stop functioning immediately. Some internal systems and runtime traffic will be impacted. The instance may become unstartable if the key version was used for disk encryption. 



## Re-enabling a key

If a compromise is a false alarm or the disablement of the key is not intended, you can re-enable the key if the key is being disabled. Re-enabling a key restores functionality to customer-facing APIs. Internal systems should recover within minutes. However, there might be data loss for API security and analytics during the period of key unavailability. 

  * **If the key disablement period is short:** The system should recover except for some data loss on API security and analytics. 
  * **If the key disablement period is long:** The system will recover to serve traffic but it can lead to data inconsistencies where one region returns one value and the previously down region returns another. Contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/) to get your Apigee cluster fixed. 



## Deleting a key

Consider following before you delete a key:

  * **For cleanup purposes:** Before you delete an old key, review [key usage](https://docs.cloud.google.com/kms/docs/view-key-usage) to see which Apigee resources the key still protects. Treat this data as informational: it can be delayed, and it doesn't cover key use outside of CMEK. Don't delete a key based on key usage tracking alone. 
  * **If deletion is necessary:** Disable the key first then schedule its destruction. You can use an [org policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to enforce [disable key first and minimum duration for destruction](https://docs.cloud.google.com/kms/docs/control-key-destruction). 



## Protecting your Apigee organization with CI/CD backups

In the event of a customer-managed encryption keys (CMEK) compromise, taking immediate action to disable, revoke, or destroy the compromised key is crucial. However, this necessary security measure can render your Apigee system non-functional, leading to potential downtime and service disruptions. 

To ensure minimal or no downtime for your Apigee services, it's imperative to implement a proactive approach: continuous backups of your organization's configuration (continuous integration/continuous deployment (CI/CD) backups). See tools available and best practices for restoring an Apigee organization. 

### The power of CI/CD and IaC

Investing in tools like Terraform, an Infrastructure as Code (IaC) solution, empowers you to create a new Apigee organization seamlessly from your backed-up configuration. This streamlined process allows you to recreate your Apigee organization swiftly and efficiently, minimizing downtime and ensuring business continuity. 

### Available tools

You can combine all the following tools to periodically backup your `apigee` org and test out the recovery process. 

  * If you just want to recreate the Apigee instances, see [ Recreating an Apigee instance with zero downtime](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instance-recreate). 
  * For information on using Terraform, see [Terraform overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview). 
  * If you want to recreate Apigee organizations, you can use `[apigeecli](https://github.com/apigee/apigeecli)`, `apigeecli organizations export` and `apigeecli organizations import` to serve as the foundation for the backup. See  Exporting/recreating orgs. 
  * If you want to back up and restore more resources beyond the above list, you will need to directly interact with the [API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) or use another [apigeecli](https://github.com/apigee/apigeecli) command. 



### Best practices

  * **Regular backups** : Schedule regular backups to ensure you have the most up-to-date configuration available. See Exporting/recreating orgs. 
  * **Secure storage** : Store your backups in a secure location, such as an encrypted repository. 
  * **Test restores** : Periodically test your restore process to ensure you can recover your Apigee organization effectively. Periodically test your restore process to ensure you can switch traffic to newly created Apigee organizations swiftly. 



## Exporting/recreating orgs

The `[apigeecli](https://github.com/apigee/apigeecli)` tool is a command line tool that allows you to manage Apigee resources. It allows you to perform the same actions as the Apigee API in an easy to use command line interface, analogous to `gcloud` commands.  
If you want to recreate Apigee organizations or migrate to another Apigee organization, you can use `apigeecli organizations export` and `apigeecli organizations import`. It can also be used as the foundation for ongoing backups. It can export and import resources like: 

  * API portal docs
  * API portal categories
  * API proxies
  * API security configuration and security profiles
  * Shared flows
  * API products
  * Developers
  * Developer apps including credentials
  * AppGroups and Apps including credentials
  * Environment details
  * Environment groups
  * Data Collectors configuration
  * Environment-level keystores and alias certificates
  * Environment-level target servers
  * Environment-level references
  * Key value maps (KVM) and entries at the org, environment and proxy level
  * Keystores and alias certificates except private keys



The tool can manage all of the other Apigee resources. The complete list of commands can be viewed using `apigeecli tree`. 

This tool has a few limitations: 

  * Keystores require saving the private key at creation and including it in the local backup files 
  * OAuth tokens will not be able to backup and restore, this implies newly created Apigee instances will require re-login by your customers. 
  * Access controls such as **org policy** and **IAM rules** are not migrated. If you want to migrate those rules, you need to use the Google Cloud API. 
  * Analytics reports exports are not supported, and analytic metrics are not copied over to the new `apigee` org. 
  * This `import` command does not automatically create instance, envGroup, EnvAttachments, endpoint attachment, or deploy proxies for you. You can manage these resources but just not directly through the `import` command. 
  * This `import` command does not automatically create portal sites. Creating portal sites has to be done manually through the UI. 
  * We suggest you invest in disaster restore for key deletion and periodically test your restore process to ensure you can switch traffic to newly created Apigee organizations swiftly. 



### Prerequisites

Before you begin, ensure the following prerequisites are met:

  * **Apigee CLI installed** : Install `apigeecli` by following the steps in the [ installation guide](https://github.com/apigee/apigeecli#installation). 
  * **Authentication** : You must have the necessary permissions and authentication credentials to interact with the Apigee organizations. Ensure you have set up: 
    * **Google Cloud SDK (`gcloud`)**: Installed and authenticated. 
    * **Access token** : Obtain an access token using `gcloud auth print-access-token`. 
  * **Network access** : Ensure your network allows access to Apigee APIs. 
  * **Create org** : Create a new `apigee` org that you want to migrate to. You can create [ different types of `apigee` orgs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview); however, make sure you use the same type of org (pay-as-you-go or subscription) and same [ type of network routing](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#configure-routing) you used with your original org. 



### Exporting an Apigee organization

The following shows a sample command. See **[apigeecli organizations export](https://github.com/apigee/apigeecli/blob/main/docs/apigeecli_organizations_export.md)** for details on the different flags. 
    
    
    # Sample command
    mkdir apigee_backup
    cd apigee_backup
    
    # gcloud auth application-default login
    export ORG_FROM=REPLACE
    apigeecli organizations export -o **$ORG_FROM** --default-token
    

### Importing an Apigee organization

The following shows a sample command. See **[apigeecli organizations import](https://github.com/apigee/apigeecli/blob/main/docs/apigeecli_organizations_import.md)** for details on the different flags
    
    
    # Sample command
    # gcloud auth application-default login
    export ORG_TO=REPLACE
    apigeecli organizations import -o **$ORG_TO** -f . --default-token
    

### Post-import steps

#### Create instance and set up networks

Do the following to create an instance and set up networks:

  1. Follow the steps in [ Create a new instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances#create-a-new-instance) to create a new instance. 
  2. **Configure Northbound traffic** : Northbound refers to API traffic from external or internal clients to Apigee through a load balancer. You need to make sure you properly configure the Private Service Connect or VPC so that your instance is reachable. You will have to set up environment group host names in the new organization. 
  3. **Configure of Southbound traffic** : Southbound refers to API traffic from Apigee to your API proxy target services. So, you must reserve and activate new IP addresses for your NAT and reconfigure your firewalls/allowlisting on your target endpoints. 



See [ Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options) for more information. 

#### Backup/restore other configs

Use one of the following to backup/restore other configurations:

  * **For IAM rules** : You can use `[ gcloud projects get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy)` and `[ gcloud projects set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy)` to copy your own IAM policy, tweak the project and `apigee` org name, and apply to new Google Cloud project and `apigee` orgs. 
  * **For other Apigee configuration** : You can use [Apigee management API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest). 



#### Deploy your proxies

Use one of the following to deploy your proxies:

  * Use `apigeecli`
  * Use the [ Apigee community script](https://www.googlecloudcommunity.com/gc/Apigee/Migrating-and-Deploying-Apigee-Resources-Across-Organizations/m-p/801780) as a reference 
  * Use the [ Apigee management API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



#### Switch the traffic

Do the following to switch the traffic:

  1. Prepare automated integration tests for the new instance.
  2. Configure a load balancer to gradually shift traffic to the new instance while monitoring performance. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
