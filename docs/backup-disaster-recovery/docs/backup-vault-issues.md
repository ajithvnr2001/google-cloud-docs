---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup-vault-issues/
title: Troubleshoot backup failure issues in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:46.930823+00:00
---

# Troubleshoot backup failure issues in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/backup-vault-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Troubleshoot backup failure issues in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Backup and DR for resources that are backed up within the backup vault using the [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan). To find solutions for resources protected using the [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) in the appliance management console, see [Event IDs and error messages](https://docs.cloud.google.com/backup-disaster-recovery/docs/event-codes).

## `PERMISSION_DENIED` issue

The backup job failed due to missing permissions in the source project and the following error message is displayed:
    
    
        Backup and DR agent or backup vault service agent is missing the permissions required to take backups of resources in the source project.
    

To resolve the issue, do the following:

  1. If the backup vault and the resource are in the same project, assign the Backup and DR agent (`roles/backupdr.serviceAgent`) IAM role to the [backup dr service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#agent), which is in the `service-<project-number>@gcp-sa-backupdr.iam.gserviceaccount.com` format.
  2. If the backup vault and the resource to protect are in different projects, assign the Compute instance admin (v1) (`roles/compute.instanceAdmin.v1`) IAM role to the [backup dr service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#agent), which is in the `service-<project-number>@gcp-sa-backupdr.iam.gserviceaccount.com` format.



## `FAILED_PRECONDITION` issue

The backup job failed when the protected resource was deleted and the following error message is displayed:
    
    
        Backup job failed due to unmet conditions. Check for source resource deletion or backup misconfigurations.
    

To resolve this issue, do the following:

  * Verify that the protected resource still exists from the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  * If the deletion was intentional, [unprotect the Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup#unprotect).




## Error 412: constraints/compute.storageResourceUseRestrictions violated

Error 412 occurs when an attempt to back up a Persistent Disk or Google Cloud Hyperdisk fails due to an organization policy constraint violation during backup creation, resulting in an error message stating `Error 412: Constraint constraints/compute.storageResourceUseRestrictions violated for project aaaaa. projects/aaax/zones/aa-aaaaa-a/disks/aaaa can't be used within your project., conditionNotMet`

Backup and DR creates backups of your Persistent Disks and Google Cloud Hyperdisks. The backups reside in your Google Cloud project (also known as the tenant project) that is managed by Google Cloud. The tenant project exists within the google.com organization, separate from your own organization.

Your organization policy dictates where you can create storage resources. `The Constraint constraints/compute.storageResourceUseRestrictions violated` error means that a resource or backup is violating the policy by being created in a tenant project that isn't part of your allowed organizational structure. Because the tenant project is within the google,com organization, it falls outside of your defined policy, which leads to the backup failure.

To resolve this error, use the following instructions:

  1. Locate the organization policy that implements the `constraints/compute.storageResourceUseRestrictions` constraint. For more information about how to view organization policies using the Google Cloud console, see [Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies).

  2. Modify the `constraints/compute.storageResourceUseRestrictions` policy to include the `folders/238813353932` tenant project folder used by Backup and DR in its allowlist.

**Note:** Make sure the specified folder ID is added to the list of allowed locations to permit Backup and DR to create snapshots within its tenant projects, even though they are outside your organizational hierarchy.
  3. Save the policy changes after you add the folder to the allowlist.

  4. Retest the backup operation after the organization policy updates and propagates, which usually takes a few minutes. The backup should proceed without violating the storage resource use restrictions. If the operation is still unsuccessful, contact Cloud Customer Care for further assistance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
