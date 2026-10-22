---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault-with-ba/
title: Overview of backup vaults managed from the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:18.061694+00:00
---

# Overview of backup vaults managed from the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault-with-ba/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Overview of backup vaults managed from the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).**Note:** This page describes how to use backup vaults with the **appliance management console**. If you are managing backups for Compute Engine, Cloud SQL, or Filestore directly through the **Google Cloud console** , see [Backup vaults for immutable and indelible backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

Self-managed workloads, such as Oracle, SAP HANA, and Google Cloud VMware Engine, leverage Google-managed backup vaults for long-term, immutable storage through the OnVault storage mechanism. This integration requires explicit authorization of backup and recovery appliances and the registration of these appliances as authorized accessors.

## Backup model

This section describes the two backup models for resources protected using the appliance management console.

### Centralized model

In the centralized model, organizations streamline backup management by creating backup vaults and deploying the appliance management console within a designated central administrator project. This central repository consolidates backups of various resources, such as VMware Engine VMs running across multiple service projects. Organizations configure policies within the appliance management console to protect their resources residing in different service projects.

### Decentralized model

In the decentralized model, appliance management consoles and backup vaults exist in various projects based on the organization's specific needs and required isolation levels. For example, an organization chooses to have a separate appliance management console for each line of business. This approach serves decentralized organizations where the responsibility for managing and backing up resources splits between multiple teams.

## Integration with backup vaults

Integrating backup vaults with the Management Console stack allows legacy and complex workloads to achieve the same ransomware resilience as Google Cloud console managed resources.

### Architecture and orchestration

Data protection involves a two-step process: a Snapshot Phase for local staging followed by a Vault Phase for transfer to the backup vault. The appliance's UDP Engine orchestrates the flow, while a component called Cloudbacker performs the actual data transfer to the vault using downscoped tokens.

Appliances don't have permission to write to a vault by default. Each appliance requires registration as an "accessor" for the specific vault. Once data writes to the vault, the appliance finalizes the backup with the backup vault service, which updates the internal Spanner database and marks the backup as immutable.

## Set up self-managed backup vaults

These are the steps to configure a backup vault in a appliance management console environment.

### IAM authorization for the appliance

  1. In the Google Cloud console, go to the Compute Engine > VM instances page.
  2. Locate your backup/recovery appliance and copy its service account email address.
  3. Switch to the project where the backup vault is located.
  4. Go to Identity and Access Management (IAM) & Admin > IAM and click **Grant Access**.
  5. Paste the appliance's service account email.
  6. Select the role: `Backup and DR Backup Vault Accessor` (roles/backupdr.backupvaultAccessor).
  7. (Optional) Add a condition to restrict access to a specific vault name.



### Register accessor and configure pool

  1. Ensure the vault's access restriction is set to UNRESTRICTED to allow cross-project appliance connections.
  2. Sign into the Backup and DR management console.
  3. Navigate to the storage management section and create a new OnVault Pool.
  4. Select the target backup vault from the list.
  5. Save the pool. The appliance registers itself as an accessor for that vault.



### Enable protection for workloads

  1. In the management console, edit the Resource Profile used by your workloads.
  2. Set the OnVault Pool to the one created in the previous step.
  3. Assign the profile to your workloads using an SLA Domain or Backup Template.
  4. Verify the job status; you see the Snapshot Phase followed by the Vault Phase.



## What's next

  * Learn more about [Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/overview).
  * Review [IAM roles and permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/iam).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
