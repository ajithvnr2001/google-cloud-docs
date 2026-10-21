---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/backup-plan-default/
title: Protect new resources using the default backup plan \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:41.405643+00:00
---

# Protect new resources using the default backup plan  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/backup-plan-default/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protect new resources using the default backup plan Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan)

This page describes the default backup plan for vaulted backups, its benefits, how it works, and its limitations.

Backup and DR employs backup plans to control when and how your data resources are backed up, and how long and how securely to retain the backups. You can create different backup plans for different needs, and Backup and DR provides a default backup plan to protect Compute Engine, Filestore, and Cloud SQL instances, and AlloyDB clusters.

[What's a backup plan?](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan)

## Overview of the Backup and DR default backup plan

A default backup plan, similar to [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan) created in the Google Cloud console, offers a streamlined approach to protect your Compute Engine, Filestore, and Cloud SQL instances, and AlloyDB clusters. You can automatically apply the default backup plan to a new instance when you enable Backup and DR in your project and have the required permissions to create the instance. The default backup plan eliminates the need to manually create a backup plan through Backup and DR, creating a baseline level of protection for your instances.

## Default backup plan settings

The default backup plan creates a daily backup. It stores the backup for 14 days in the default backup vault, of which the first day is immutable. For the remainder of the 14 days, the backup can be deleted by an authorized user. After 14 days the backup is automatically deleted.

**Note:** Cloud SQL instances and AlloyDB clusters are stored for 8 days.Setting | Value  
---|---  
Backup schedule | Daily between 00:00 and 06:00 in the local timezone for the region.  
Storage | Compute Engine: Regional vault created in the same region and project as the source instance.  
Filestore: Regional vault created in the same region and project as the source instance.  
Cloud SQL: Multi-regional vault in same project for supported source regions; Regional vault in same project for unsupported multi-region source regions.  
AlloyDB: Regional vault created in the same region and project as the source cluster.  
Retention | 14 days (8 days for Cloud SQL instances and AlloyDB clusters)  
Enforced retention | One day  
  
You can modify the backup schedule and storage duration in the [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create#create).

You can modify the enforced retention period by editing the [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#update).

**Note:** For more information on how enforced retention compares with the expiration period set in the backup plan, see [Overview of data retention in Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan#retention-types).

If the default backup plan doesn't meet your organization's requirements, you can select a different plan altogether during instance creation or choose to opt-out using the **No backups** option.

**Note:** For complex backup requirements, such as custom schedules, retention policies, and granular control, you can create a backup plan within Backup and DR. For instructions, see [Create and manage a backup plan for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create).

## How the default backup plan works

When you create a new Compute Engine, Filestore, or Cloud SQL instance, or AlloyDB cluster, you can specify if you want the instance or cluster to use a default backup plan or [create a new backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create) with manual configuration. If you select the default backup plan option, a default backup vault is automatically created within the same project with the minimum enforced retention period for one day. The default backup vault doesn't lock the retention period, however you can modify the minimum retention period, and enable retention lock. For instructions, see [Update the minimum enforced retention period on an existing backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#update). Note that the default backup plan cannot be modified after creation. You can apply only one default backup plan per supported region for a Compute Engine or Filestore instance, or AlloyDB cluster.

The default backup plan automatically creates daily backups between 00:00 and 06:00 in the local time region of the workload. These backups are retained for 14 days in the default backup vault. The default backup plan has a backup deletion policy for one day.

**Note:** Cloud SQL instances and AlloyDB clusters are stored for 8 days.

  * Compute Engine: The default backup plan is named `default-compute-instance-plan-<region>`. There is one default backup plan for each supported region.

  * Filestore: The default backup plan is named `default-filestore-plan-<region>`. There is one default backup plan for each supported region.

  * AlloyDB: The default backup plan is named `default-alloydb-plan-<region>`. There is one default backup plan for each supported region.

  * Cloud SQL:

    * Plans with multi-regional backup vaults: A plan in a project for supported [multi-regions](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#multi-regions) for Cloud SQL:

      * For Cloud SQL Enterprise Plus edition instances: The default backup plan is named  
`default-csql-instance-ep-plan-<region>-bv-<multi-region-vault-location>`

      * For Cloud SQL Enterprise edition instances: The default backup plan is named  
`default-csql-instance-e-plan-<region>-bv-<multi-region-vault-location>`.

    * Plans with regional backup vaults: A plan in a project for unsupported multi-region source regions:

      * For Cloud SQL Enterprise Plus edition instances the default backup plan is named  
`default-csql-instance-ep-plan-<region>`.

      * For Cloud SQL Enterprise edition instances the default backup plan is named  
`default-csql-instance-e-plan-<region>`.




There is one default backup plan for each supported region. This plan provides the same protection for all associated instances in the region.

The default backup plan is available only for new Compute Engine, Filestore, and Cloud SQL instances, and AlloyDB clusters created through the Google Cloud console. It doesn't impact existing resources or their data protection configurations. If you are protecting instances using multi-regional Persistent Disk snapshots, you can manually configure protection into multi-region backup vaults.

## Limitations

  * A default backup plan cannot be used if the instance is created in a region that is not supported by Backup and DR.
  * You can use the default backup plan only in the same region where the Compute Engine instance resides.
  * You can apply only one default backup plan per region.



## Default backup plans for new instances

Backup and DR offers a default backup plan for Compute Engine, Filestore, and Cloud SQL instances, and AlloyDB clusters created through the Google Cloud console. Here's what you need to know:

### How new instances are affected

New Compute Engine, Filestore, and Cloud SQL instances, and AlloyDB clusters created through the Google Cloud console will have a default backup plan automatically applied if the project has Backup and DR enabled and the user creating the instance has the necessary permissions.

### Benefits

Default backup plans:

  * **Enhance data protection** : The default backup plan improves the baseline level of protection for all new instances created through the Google Cloud console. This minimizes the risk of data loss due to accidental deletions, cyber-attacks, or other unforeseen events.
  * **Simplify data protection management** : The automatic application of a default backup plan removes the need for manual configuration, making it easier to protect your instances from day one.
  * **Promote best practices** : This change encourages the adoption of robust data protection measures across your Google Cloud environment.



With this enhancement, your workloads have an improved foundational level of protection in place, allowing you to focus on other critical aspects of your business.

### How existing instances are affected

This change doesn't impact your existing instances or their current data protection configurations. Only new instances created through the Google Cloud console are affected.

### How instances created using automation or Terraform are affected

Instances created using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or other APIs won't be impacted by this change.

**Q: Can I opt out of the default backup plan?**

A: Yes, you can opt out or choose another backup plan during the instance creation process in the Google Cloud console. You'll find these options under the new **Data protection** tab. [Configure your project defaults](https://docs.cloud.google.com/compute/docs/disks/default-backup#change-default-backup-setting) to the value of your choosing.

**Q: I'm protecting instances with Backup and DR tag-based protection. Will that protection change?**

A: No, your existing Backup and DR protection, including tag-based protection, will remain unchanged. This update only affects new instances created through the Google Cloud console. Tag-based protection can identify if an instance has a default plan and won't double protect your instance if a tag is applied. You will need to mark the instance as **No Backups** and continue to tag the instance if you want to use tag-based protection.

**Q: Should I transition to this new scheme of protection using the default plan?**

A: It depends on your specific needs and current setup. Consider these factors:

  * Ease of use: The default plan offers a basic solution for basic instance protection providing a daily backup retained for 14 days.

**Note:** Cloud SQL instances and AlloyDB clusters are stored for 8 days.
  * Customization: If the default plan does not meet your organizational requirements, you can choose a different plan altogether during instance creation or choose to opt-out using the **No backups** option.


**Note:** The default vault in which your backups are stored resides in the same project as your workload. The default plan takes a backup daily between 00:00 and 06:00 and stores it in the default backup vault. Compute Engine instance, disk, and Filestore backups are stored for 14 days, Cloud SQL and AlloyDB backups are stored for 8 days. Backup deletion is prevented for one day.

**Q: If I'm protecting instances using multi-regional Persistent Disk snapshots, then I probably don't want my new instances to go to a regional backup vault. How do I prevent that?**

A: You can manually configure protection into multi-region backup vaults.

**Q: I'm a Backup and DR customer but I'm not protecting Compute Engine, Filestore, or Cloud SQL instances or AlloyDB clusters yet. Does this mean that my new instances will start to be protected with a backup vault?**

A: Yes, if you create new instances through the Google Cloud console and have Backup and DR enabled with the necessary permissions, they will be protected with the default backup plan and associated default vault. If you want to use a different backup plan, you can select it when you create the instance. If you don't want to protect your instance through this new experience, then select the **No backups** option.

**Q: How does this new default backup plan compare with my current persistent disk protection (assuming I use snapshots)?**

A: Both offer data protection, but with [key differences](https://docs.cloud.google.com/compute/docs/disks/default-backup#options):

  * Snapshots: Individual disk backups that are prone to cyberattacks and malicious deletions if a bad actor has access to projects in which snapshots reside.
  * Backup and DR: Offers the capability to store backups into a backup vault that provides safeguarding against ransomware attacks and malicious deletions. You define the duration of both the backup storage and its enforced retention.



**Q: Should I use the backup plan default protection or not?**

A: Ultimately, the decision depends on your specific organization's requirements and preferences. The default backup plan gives you peace of mind to know that all instances have a baseline level of protection. You can remove the protection and switch to using persistent disk snapshots, or choose a different backup plan within Backup and DR to take backups. If you have complex backup needs, we recommend configuring your own backup plan policies for specific workloads. 

**Q: What would happen if the instance created is in a different region where the backup plan is not supported?**

A: You cannot use default backup plans if the instance is created in a region that is not supported by Backup and DR.

**Q: Can I disable this feature through an organization policy?**

A: No, you cannot use organization policy to disable this feature. If you don't intend to protect your data resource then select the **No backups** option. In addition, you can customize your default configuration.

**Q: What permissions will I need to use the default backup plans?**

A: You need the `backupdr.serviceConfig.initialize` permission in order to use backup plans if you are using a custom role within your IAM settings. If you are using one of the Backup and DR predefined roles such as `Backup and DR Admin` or `Backup and DR User V2`, the permissions will automatically be available to use. If you are using a `computeAdmin` or `computeInstanceAdmin` role, the permissions have also been automatically added to these roles. The final list of permissions we will be adding to the `roles/compute.admin`, `roles/compute.instanceAdmin` and `roles/compute.instanceAdmin.v1` roles are:

  * `backupdr.backupPlans.useForComputeInstance`
  * `backupdr.serviceConfig.initialize`
  * `backupdr.backupPlanAssociations.createForComputeInstance`
  * `backupdr.backupPlanAssociations.deleteForComputeInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.locations.list`



**Q: Who can I contact if I have further questions?**

A: If you have any further questions, contact us at gcbdr-default-backup-plans@google.com.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
