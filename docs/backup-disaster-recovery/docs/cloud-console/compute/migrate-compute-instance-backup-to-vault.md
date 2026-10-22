---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/migrate-compute-instance-backup-to-vault/
title: Migrate a Compute Engine instance backup configuration from the appliance management console to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:04.695924+00:00
---

# Migrate a Compute Engine instance backup configuration from the appliance management console to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/migrate-compute-instance-backup-to-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Migrate a Compute Engine instance backup configuration from the appliance management console to a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

Migrate a Compute Engine instance protection from the appliance management console backup plan to a backup vault backup plan using Compute Engine instance protection without experiencing disruption, uninstalling the backup agent, network peering, or making changes to your VPC firewalls.

## Benefits

  * **Enhanced ransomware protection** : advanced indelibility and immutability features that secure your data against ransomware and accidental or malicious deletion.

  * **Immediate cost savings** : reduce management fees as soon as you complete migration.

  * **Streamlined infrastructure** : move to a zero-infrastructure model that eliminates the need for backup appliances, lowering your total cost of ownership (TCO).

  * **Seamless management** : use an integrated Google Cloud console experience with full support for [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, and Google Cloud APIs for effortless, at scale automation.

  * **Expanded support** : gain a unified platform that also supports Cloud SQL, AlloyDB for PostgreSQL, and Filestore.

  * **Available across all Google Cloud regions**.




## Limitations

  * Migration isn't supported if your current appliance management console backup plan or Compute Engine instance configuration includes any of the following features:

    * Appliance management console backup plans with high-frequency backups using a backup frequency of one hour or less.

    * Appliance management console backup plans configured with archive snapshots.

    * Compute Engine instances that use Google Cloud Hyperdisk.

    * Compute Engine instances that exclude specific disks from backups.

  * You can only migrate standard Compute Engine instances. Other application workloads types, such as Microsoft SQL, SAP HANA, Oracle, and VMware VMs cannot be migrated using this page.

  * You cannot migrate existing backups.




## Considerations

  * To perform a bulk migration, you need a migration script to automate the transition for large-scale environments. Contact Cloud Customer Care to receive a bulk migration script.

  * If you maintain protection for a Compute Engine instance through the backup vault and the management console, you can incur billing charges for both environments.

  * If a Compute Engine instance automates backups using [Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) dynamic protection, the scheduled job will re-protect the instances after the migration unless the tag is manually removed.

  * We recommend that you avoid migrating VMs that use Google Cloud Hyperdisk.

  * Your existing Backup and DR service roles continue to work as expected. However, if you plan to back up Compute Engine instances from multiple service projects into one centralized backup vault (that is, a backup vault created in a central backup project), you must grant the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) role to the backup vault service agent in all service projects hosting the instances that need to be backed up. For more information, see [Grant a role to the service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#agent).




## How it works

When you perform a migration, your historical backups remain in the appliance management console and aren't migrated to the backup vault. You retain access in the appliance management console until they expire according to their original retention policy.

After the migration completes, you can view historical recovery points in the appliance management console and new recovery points in the Google Cloud console.

To migrate your Compute Engine instance from the appliance management console to a backup vault, you perform the following steps:

  1. **Configure protection** : use the `MigrateToBackupVault` command to protect Compute Engine instances with a backup vault backup plan.

  2. **Perform verification** : confirm that the backup vault creates backups successfully.

  3. **Remove protection from the appliance management console** : use the `UnprotectVMsFromManagementConsole` command to remove protection from the appliance management console.




## Before you begin

  1. Verify that you have the permissions required to complete this guide.

  2. Ensure you have the following resources:

     * A pre-existing backup vault. For instructions, see [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#create).
     * A pre-existing backup plan configured to use the backup vault. Create this backup plan in the Google Cloud console. It can be equivalent to the appliance management console backup plan. For instructions, see [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create#create).



### Required roles

To get the permissions that you need to migrate a Compute Engine instance backup configuration, ask your administrator to grant you the following IAM roles on your project: 

  * Backup and DR Admin (Legacy role for appliance management console operations) 
  * [Backup and DR Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Install the migration tool

To run the migration commands, you must install the `backupdr_gcevm_migration_tool` standalone executable in your chosen environment, either within `Cloud Shell` or on your local workstation.

###  Google Cloud Shell 

  1. Open Cloud Shell in the Google Cloud console.

  2. Click **More** more_vert and then click **Upload**.

  3. Select the `backupdr_gcevm_migration_tool` file.

  4. Make the tool executable:
         
         chmod +x ~/backupdr_gcevm_migration_tool
         

  5. Run the tool using `~/backupdr_gcevm_migration_tool`.




### Local Environment

  1. Download the `backupdr_gcevm_migration_tool` executable.

  2. Install and authenticate the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). For more information, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

  3. Move the executable to a directory, for example `~/tools`, and make it executable:
         
         mkdir -p ~/tools
         mv ~/Downloads/backupdr_gcevm_migration_tool ~/tools/
         chmod +x ~/tools/backupdr_gcevm_migration_tool
         

  4. Optional: To run the tool from any directory, add it to your `PATH`. Add the following line to your `~/.bashrc` or `~/.zshrc` file:
         
         export PATH="$PATH:$HOME/tools"
         

  5. Reload your shell:
         
         source ~/.bashrc
         




## Migrate Compute Engine instances

To migrate your instances, run the migration tool commands in the terminal environment where you installed the tool, replacing the placeholder values in the examples with your actual resource names, project IDs, and URLs.

### Protect Compute Engine instances with a backup vault backup plan

Run the `MigrateToBackupVault` command to identify eligible Compute Engine instances in a appliance management console backup plan and protect them with the specified backup vault backup plan.

  1. Run the `MigrateToBackupVault` command:
         
         ./backupdr_gcevm_migration_tool MigrateToBackupVault \
           --slt_name=SLT_NAME \
           --management_server_url=MANAGEMENT_SERVER_URL \
           --backup_plan=projects/PROJECT_ID/locations/REGION/backupPlans/BACKUP_PLAN_NAME \
           --workload_projects=PROJECT_ID_1,PROJECT_ID_2 \
           --apply \
           --trigger_backup
         

Replace the following:

     * `SLT_NAME`: the name of the source appliance management console backup plan (formerly known as a service level template or SLT).
     * `MANAGEMENT_SERVER_URL`: the URL of the appliance management console.
     * `PROJECT_ID`: your Google Cloud project ID.
     * `REGION`: the region where your backup plan is located.
     * `BACKUP_PLAN_NAME`: the name of the backup plan to apply.
     * `PROJECT_ID_1,PROJECT_ID_2`: a comma-separated list of project IDs that contain Compute Engine instances, or `all`.

Additional flags:

     * `--apply`: executes the protection. If omitted, the tool runs in dry-run mode.
     * `--trigger_backup`: initiates an on-demand backup immediately after the protection is applied.

The command creates an output file named `MigrateToBackupVault_{slt_name}_output.txt` that summarizes the actions taken and VM status.

  2. To verify that the instances are protected by the backup plan, go to the **Backup and DR > Vaulted Backups** page in the Google Cloud console.




### Unprotect Compute Engine instances from the appliance management console

The `UnprotectVMsFromManagementConsole` command removes protection from Compute Engine instances in the appliance management console. This command only unprotects a VM if it is protected by the new backup plan and has at least one successful backup vault backup.

  1. Run the `UnprotectVMsFromManagementConsole` command:
         
         ./backupdr_gcevm_migration_tool UnprotectVMsFromManagementConsole \
           --slt_name=SLT_NAME \
           --management_server_url=MANAGEMENT_SERVER_URL \
           --workload_projects=PROJECT_ID_1,PROJECT_ID_2 \
           --apply
         

Replace the following:

     * `SLT_NAME`: The name of the source appliance management console backup plan.
     * `MANAGEMENT_SERVER_URL`: The URL of the appliance management console.
     * `PROJECT_ID_1,PROJECT_ID_2`: A comma-separated list of project IDs or `all`.

Additional flags:

     * `--apply`: Executes the unprotection. If omitted, the tool runs in dry-run mode.




The command creates an output file named `UnprotectVMsFromManagementConsole_{slt_name}_output.txt` that summarizes the actions.

  1. Verify that the eligible instances are no longer protected in the appliance management console.



The migration tool checks your environment to ensure a safe transition. For example, the tool removes protection from the appliance management console only after it verifies that a successful backup vault backup exists for the instance.

## Encryption

The backup vault fully supports customer-managed encryption keys (CMEK) for Compute Engine instances, which lets you encrypt your backups using your own encryption keys.

## Monitoring, reporting, and alerting changes

Post-migration, you use Cloud Monitoring and Cloud Logging for observability instead of legacy management console email reports. This lets you create custom dashboards and configure alerts directly in the Google Cloud console. To schedule email alerts or configure alerting policies from your monitoring dashboards, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

### Access historical reporting data

Your existing pre-migration monitoring and reporting data remains accessible by logging in to the appliance management console. For post-migration monitoring and reporting data, you access it directly in the Google Cloud console.

If you want to analyze pre-migration and post-migration data together in BigQuery, you can route your logs to a BigQuery dataset using a log sink. To configure log sinks and prebuilt reports, see [Set up prebuilt reports in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery).

After your logs are in BigQuery, you can do the following:

  * Write custom SQL queries to analyze your log data. For more information, see [Run interactive and batch queries](https://docs.cloud.google.com/bigquery/docs/queries-overview).

  * Create custom infrastructure reports and visualizations using Data Studio. For more information, see [Introduction to Data Studio](https://docs.cloud.google.com/looker/docs/looker-studio-overview).

  * Set up log-based alerts in the Google Cloud console. For more information, see [Configure log-based alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).




## Run a hybrid environment

A hybrid environment is fully supported. We recommend migrating all eligible Compute Engine instances to a backup vault immediately to gain the cost and security benefits. However, if your environment includes configurations that the backup vault doesn't support, you can maintain protection for those instances using the appliance management console. As Backup and DR adds support for those features, you can migrate the remaining instances to the backup vault. If you have questions about supported configurations, contact Cloud Customer Care.

## Roll back a migration

If you encounter issues during migration, you can roll back your changes. To mitigate risk, we strongly recommend an overlap strategy: do not unprotect the instance in the appliance management console until you confirm that the new backup vault backup job completes successfully. This strategy ensures that your instances maintain continuous backup coverage.

Your historical instance backups created before the migration cutover remain available and accessible in the appliance management console. You access new backups created in the backup vault directly in the Google Cloud console.

## What's next

  * Learn more about [Backup plans in the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan).
  * Learn how to [Manage backups in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
