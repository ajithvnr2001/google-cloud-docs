---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create/
title: Create and manage a backup vault in the Google Cloud console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:14.898857+00:00
---

# Create and manage a backup vault in the Google Cloud console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Create and manage a backup vault in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault)

This page explains how to create and manage a backup vault in the Google Cloud console. You can learn more about backup vaults at [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

## Before you begin

To get the permissions that you need to create and manage a backup vault, ask your administrator to grant you the [Backup and DR Backup Vault Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`) IAM role on the project where you want to create a backup vault. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage a backup vault. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage a backup vault:

  * `backupdr.backupVaults.create`
  * `backupdr.backupVaults.list`
  * `backupdr.backupVaults.get`
  * `backupdr.backupVaults.update`
  * `backupdr.backupVaults.delete`
  * `backupdr.bvbackups.restore`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Apply a lien

To protect your backup vault from accidental deletion, we strongly recommend applying a project lien to the Google Cloud project where the vault will reside. A project lien prevents the project—and your backups—from being deleted unexpectedly. For more information, see [Protect projects with liens](https://docs.cloud.google.com/resource-manager/docs/project-liens).

To secure your project liens against unauthorized removal, use Privileged Access Manager (PAM) to enforce multi-party approval. For more information, see [Protect project liens by using Privileged Access Manager](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/project-liens-multi-party-approval).

**Important:** Beginning November 1, 2026, Backup and DR will automatically apply a project-level lien to any project containing a backup vault with backups protected by enforced retention.

## Create a backup vault

**Note:** When you create a backup vault, you have the option to set enforced retention of backups so they can't be deleted for a set period. If you are participating in the [30-day free trial](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial), then you will be billed for any backups that are retained beyond the end of the trial.

Use the following instructions to create a backup vault.

###  Console 

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. Click **Create backup vault**.

  3. On the **Create a backup vault** page, enter your backup vault information.

     1. In the **Name your backup vault** field, enter a name that meets the [backup vault name requirements](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#name).
     2. From the **Choose where to store your data** list, select a [supported location](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#regions) where the backup data will be permanently stored.
     3. In the **Prevent backup deletion** field, enter the [minimum enforced retention](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#enforced-retention) period defining how long backups are protected against deletion. The minimum is 1 day and the maximum is 99 years.

If you want to lock the value of the minimum enforced retention period, select **Lock the enforced retention** and then click the calendar_month icon and select the date from the calendar.

        * **Prevent deletion for duration specified in backup rule** : You can set the vault to inherit the **Delete backups after** value set in a backup plan. Backups can't be manually deleted, they will be deleted according to the value in their associated backup plan.

        * **Lock the enforced retention** : If you want to lock the value of the minimum enforced retention period, check this and then click the calendar_month icon and select the date from the calendar.

**Note:** For more information on how enforced retention compares with the expiration period set in the backup plan, see [Overview of data retention in Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan#retention-types).
     4. If you want to use your own encryption key, then under **Encryption** , select the **Customer-managed encryption key (CMEK)** option, and then select your key from the drop-down list. Only keys from the same location as the backup vault are displayed. You can only configure CMEK when you create a backup vault. For more details on using CMEK, see [Encryption](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#encryption).

For required permissions, see [CMEK permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek#permissions_required_to_use_cmek).

**Note:** Backup and DR supports CMEK protection only for Compute Engine instance and Persistent Disk backups stored in backup vaults.
     1. In the **Define access to your backup vault** section, select an option to define [access restrictions](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#access-restrictions) for the backup vault. If you don't select an option, the backup vault is created with the **Restrict access to current organization** restriction.
  4. Click **Create**.




###  gcloud 

  1. In one of the following development environments, set up the gcloud CLI:
  2. **Cloud Shell** : to use an online terminal with the gcloud CLI already set up, activate Cloud Shell. At the bottom of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.
  3. **Local shell** : to use a local development environment, [install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI.

  4. Create a backup vault.
         
         gcloud backup-dr backup-vaults create BACKUPVAULT_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --backup-retention-inheritance=RETENTION_PERIOD_INHERITANCE \
           --backup-min-enforced-retention=RETENTION_PERIOD_IN_DAYS \
           --kms-key=KMS_KEY \
           --access-restriction=ACCESS_RESTRICTION
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault.
     * `PROJECT_ID`: the name of the project where you want to create the backup vault.
     * `LOCATION`: the location where you want to create a backup vault.
     * `RETENTION_PERIOD_INHERITANCE`: the inheritance mode for enforced retention end time of the backup within this backup vault. Once set, the inheritance mode cannot be changed. The default is `inherit-vault-retention`.

       * If set to inherit-vault-retention, then the backup retention period will be inherited from the backup vault.
       * If set to match-backup-expire-time, the backup retention period will be the same as the backup expiration time.
     * `RETENTION_PERIOD_IN_DAYS`: the period of time that each backup in the backup vault cannot be deleted. The minimum is 1 day and the maximum is 99 years. For example, `2w1d` is two weeks and one day. For more information, see [Backup vault minimum enforced retention period](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#enforced-retention).

     * `KMS_KEY`: The customer-managed encryption key (CMEK) to use for encryption, in the format `projects/KMS_PROJECT_ID/locations/KMS_LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME`. If you provide a key, CMEK is enabled on the backup vault. You can only configure CMEK when you create a backup vault. For more details on using CMEK, see [Encryption](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#encryption). For required permissions, see [CMEK permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek#permissions_required_to_use_cmek).

     * `ACCESS_RESTRICTION`: specify [access restrictions](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#access-restrictions) for the backup vault. The allowed values are `within-project`, `within-org`, `unrestricted`, and `within-org-but-unrestricted-for-ba`. If you don't specify a value, then the backup vault is created with the `within-org` restriction.

Backup and DR supports CMEK protection only for Compute Engine instance and Persistent Disk backups stored in backup vaults. 

  5. Check the status of the operation.
         
         gcloud backup-dr operations describe FULL_OPERATION_ID
         

Replace the following:

     * `FULL_OPERATION_ID` the operation ID that is displayed for the backup vault. It is in the following format `projects/test-project/locations/us-central1/operations/operationID`

The output is displayed as the following:
    
    Create in progress for backup vault [projects/test-project/locations/us-central1/operations/operation-1721893921568-41e0dab8938a1-f1dc6ad2-3051b3ce]. Run the [gcloud backup-dr operations describe] command to check the status of this operation.
    




### Terraform

You can use a [Terraform resource to create a backup vault](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/backup_dr_backup_vault).
    
    
    resource "google_backup_dr_backup_vault" "default" {
      provider                                   = google-beta
      location                                   = "us-central1"
      backup_vault_id                            = "my-vault"
      description                                = "This vault is created usingTerraform."
      backup_minimum_enforced_retention_duration = "100000s"
      force_update                               = "true"
      ignore_inactive_datasources                = "true"
      allow_missing                              = "true"
    }
    

## List backup vaults in a project

Use the following instructions to list backup vaults in a project.

###  Console 

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

Backup vaults that are part of the selected project appear in the list.




###  gcloud 

  1. List the backup vaults.
         
         gcloud backup-dr backup-vaults list \
           --project=PROJECT_ID \
           --location=LOCATION
         

Replace the following:

     * `PROJECT_ID`: the name of the project where the backup vaults are created.
     * `LOCATION`: the location where the backup vaults are created.



## View backup vault details

The backup vault details page displays the configuration information and lets you to update the editable items.

  * **Created** : The date that the backup vault was created.
  * **Last updated** : The most recent date that the backup vault was modified.
  * **Description** : An optional description for the backup vault.
  * **Status** : Active
  * **Location type** : Region or Multi-region
  * **Location** : The selected region or multi-region, such as `us-central1 (Iowa)` or `us`.
  * **Stored bytes** : The amount of data stored within the backup vault.
  * **Enforced retention**
    * **Minimum for backups** : Select a minimum value for this backup vault
    * **Inherited from backup rule** : Use the value already set in a backup rule for backups that will be stored in this backup vault.
  * **Retention lock status**
    * **Unlocked** : A lock is neither applied nor pending for the backup vault.
    * **Lock takes effect on datetime** : A lock has been set to take effect on the backup vault at the specified date.
    * **Locked** : The value of the backup vault's minimum enforced retention periods is locked against reduction or removal.
  * **Encryption type** : Google-managed encryption key 
    * **Encryption key** : The customer managed encryption key in use.
  * **Access restriction** : No restrictions or Restrict access to current organization



Use the following instructions to view backup vault details.

###  Console 

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

Backup vaults that are part of the selected project are listed on this page.

  2. Click the backup vault that you want to view.

The backup vault details page displays the configuration information, including the value of the minimum enforced retention period, and its lock status.




###  gcloud 

  1. View the backup vault details.
         
         gcloud backup-dr backup-vaults describe BACKUPVAULT_NAME \
           --location=LOCATION \
           --project=PROJECT_ID
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault.
     * `LOCATION`: the location of the backup vault.
     * `PROJECT_ID`: the name of the project where the backup vault is created.



## Update the minimum enforced retention period on an existing backup vault

You can update the minimum enforced retention period based on the lock's status.

  * **Unlocked** : You can increase or decrease the minimum enforced retention period.
  * **Locked** : You can only increase the minimum enforced retention period.



The lock cannot be removed if the effective date has been reached. However, if the effective date has not yet been reached, you can remove the lock, which clears the originally-specified effective date.

Changes to the value of the minimum enforced retention period only apply to backups created after the update. Changes to the value of the minimum enforced retention period don't impact the enforced retention remaining for backups that already exist in the backup vault.

When increasing the enforced retention period for a backup vault, the backup vault enforced retention period shouldn't exceed the retention period in the backup plan for any backups you will store in the backup vault. If the changed value is longer than the backup retention period, the Backup and DR handles these changes differently based on the backup plan type.

  * **Google Cloud console-based plans** : Changes to the backup vault value are prevented.

  * **Management console-based plans** : Changes to the backup vault value are allowed, but you should immediately update the relevant backup plans to specify retention that is equal to or longer than the updated backup vault minimum enforced retention period.

Backups generated while the plan retention is shorter than the backup vault minimum enforced retention are created with the enforced retention period set to the backup vault's minimum enforced retention. Additionally, the backup's expiration is set to occur after the enforced retention period has been satisfied.


**Note:** When you create a backup vault, you have the option to set enforced retention of backups so they can't be deleted for a set period. If you are participating in the [30-day free trial](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial), then you will be billed for any backups that are retained beyond the end of the trial.

Use the following instructions to update the minimum enforced retention period on an existing backup vault.

###  Console 

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. In the list of backup vaults, click the name of the backup vault that you want to update.

  3. Click the edit icon.

  4. In the **Edit minimum enforced retention** dialog, enter the **New minimum enforced retention period** value. This is the period of time that each backup in the backup vault cannot be deleted. The minimum is 1 day and the maximum is 99 years.

  5. If you want to lock the minimum enforced retention period, select the **Lock the enforced retention** checkbox, and then select the lock effective date from the calendar.

  6. Click **Save**.




###  gcloud 

  1. Update the minimum enforced retention period on an existing backup vault.
         
         gcloud backup-dr backup-vaults update BACKUPVAULT_NAME\
           --project=PROJECT_ID \
           --location=LOCATION \
           --backup-min-enforced-retention=RETENTION_PERIOD_IN_DAYS
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault.
     * `PROJECT_ID`: the name of the project where the backup vault is created.
     * `LOCATION`: the location of the backup vault.
     * `RETENTION_PERIOD_IN_DAYS`: the period of time that each backup in the backup vault cannot be deleted. The minimum is 1 day and the maximum is 99 years.



## Resource restrictions for enforced retention

When backing up some resource types into a backup vault, there are restrictions governing compatibility with the backup vault's minimum enforced retention settings.

Resource type | Min. enforced retention (backups) | Min. enforced retention (logs) | Prevent manual deletion  
---|---|---|---  
AlloyDB for PostgreSQL | 1-365 days | 1-35 days | Required  
Cloud SQL | 1 day-10 years | Not applicable | Optional  
Compute Engine instance | 1 day-99 years | Not applicable | Optional  
Compute Engine disk | 1 day-99 years | Not applicable | Optional  
Filestore | 1 day-99 years | Not applicable | Optional  
**Note:** AlloyDB for PostgreSQL and Cloud SQL logs are stored outside of the backup vault.

## Delete a backup vault

You cannot delete a backup vault until all contained backups meet their enforced retention and are expired or manually deleted.

Use the following instructions to delete a backup vault after all of its contained backups have expired or been deleted.

###  Console 

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. Click the backup vault you want to delete.

  3. Click **Delete**.

  4. In the overlay window that appears, confirm you want to delete the backup vault and its contents.

  5. Click **Delete**.




###  gcloud 

  1. Delete a backup vault.
         
         gcloud backup-dr backup-vaults delete BACKUPVAULT_NAME \
           --project=PROJECT_ID \
           --location=LOCATION
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault.
     * `PROJECT_ID`: the name of the project where the backup vault is created.
     * `LOCATION`: the location of the backup vault.



## Grant access to the backup vault service agent and to backup/recovery appliances

Every backup vault created has a unique service agent linked to it. For some resource types, the service agent is leveraged to perform actions on behalf of the Backup and DR and, therefore, needs to be granted appropriate permissions on the projects, where the backup vault service agent needs to access. A service agent is a Google-managed service account; for more information, see [Service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).

For some resource types, such as Google Cloud VMware Engine, Oracle databases, and SQL Server databases, the Backup and DR backup/recovery appliance must perform actions on the backup vault. In those cases, the backup/recovery appliance needs appropriate permissions on the backup vault. In addition, the target backup vault must be set with the UNRESTRICTED or WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA [access restrictions](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#access-restrictions).

### Grant a role to the service agent

After you find the service agent's email address, you can grant the backup vault service agent a role just like you would grant a role to any other principal.

To back up a Compute Engine VM instance in a project different from where the backup vault is created, you must grant the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) IAM role to the backup vault service agent within the Compute Engine project. However, to back up a Compute Engine VM instance in the project same as where the backup vault is created, no roles are required to be granted.

To restore a Compute Engine instance, you need to grant the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) IAM role in your restore project to the backup vault service agent.

Use the following instructions to grant a role to the service agent.

###  Console 

  1. In the Google Cloud console, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. Click the backup vault name and copy the service agent's email address.

  3. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. In the **New principles** field, enter the service agent's email address.

  5. From the **Select a role** list, select the appropriate role based on the resource type. For example, to back up a Compute Engine instance in a project different from where the backup vault is created, select the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) IAM role.

  6. Click **Save**.




###  gcloud 

  1. Grant roles to the service agent.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member='serviceAccount:SERVICE_ACCOUNT \
           --role=ROLE
         

Replace the following:

     * `PROJECT_ID`: the name of the project.
     * `SERVICE_ACCOUNT`: the email address of the backup vault service agent. For example, `my-service-account@my-project.iam.gserviceaccount.com`.
     * `ROLE`: the role required to grant on the resource project. For example, to back up a Compute Engine instance in a project different from where the backup vault is created, select the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) IAM role.



### Grant roles to the backup/recovery appliance service account

You can access a backup vault from the backup/recovery appliance project only after the appliance service account is granted the Backup and DR Backup Vault Accessor (`roles/backupdr.backupvaultAccessor`) IAM role in the backup vault project. Without this role, you cannot access the backup vault to complete the setup to enable backup creation.

After granting roles to the backup/recovery appliance service account, you can back up and restore Google Cloud VMware Engine, Oracle databases, and SQL Server databases into a backup vault using the appliance management console.

**Note:** The backup/recovery appliance and the backup vault don't need to be in the same project.

Use the following instructions to grant roles to the backup/recovery appliance service account:

  1. In the Google Cloud console, go to the **VM instances** page where your appliance was created.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the Compute Engine instance that you want to get the service account for.

  3. In the **API and identity management** section, copy the email address of the service account from the **Service account** field.

  4. In the Google Cloud console, go to **IAM** roles in your backup vault project.

**Note:** The backup vault project can be different from the backup/recovery appliance project.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  5. Click **Grant access**.

  6. In the **New principles** field, enter the appliance's service account email address.

  7. From the **Select a role** list, select the **Backup and DR Backup Vault Accessor** role.

  8. Optional: To restrict your backup/recovery appliance to only have access to a specific backup vault, click **add Add IAM condition** next to the **Backup and DR Backup Vault Accessor** role.

     1. In the **Title** field, enter a name for the condition.
     2. Click the **Condition editor** tab.

        * In the **Expression CEL editor** field, enter the following expression.
              
              resource.name.extract("projects/PROJECT_ID/locations/LOCATION/backupVaults
              /{name}/") == ("BACKUPVAULT_NAME") || resource.name.extract("projects/PROJECT_ID/locations/LOCATION/backupVaults
              /{name}") == ("BACKUPVAULT_NAME") || resource.name.extract("operations/{op}") != ""
              

Replace the following:

        * `BACKUPVAULT_NAME`: the name of the backup vault.
        * `PROJECT_ID`: the name of the project where the backup vault is created.
        * `LOCATION`: the location of the backup vault.

To add access for additional backup vaults, append additional "resource.name.startsWith" statements (with the "||" OR logical operator) as necessary.

For example, the following statement authorizes a backup vault named "bv-test" and a backup vault named "user-bv1", both located in a project named "testproject" and in the location "us-central1".
              
              resource.name.extract("projects/testproject/locations/us-central1/backupVaults
              /{name}/") == ("bv-test") || resource.name.extract("projects/testproject/locations/us-central1/backupVaults
              /{name}") == ("bv-test") || resource.name.extract("projects/testproject/locations/us-central1/backupVaults
              /{name}/") == ("user-bv1") || resource.name.extract("projects/testproject/locations/us-central1/backupVaults
              /{name}") == ("user-bv1") || resource.name.extract("operations/{op}") != ""
              

     3. Click **Save**.

  9. Click **Save**.




## What's next

  * [Manage data sources](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage)
  * [Manage backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
