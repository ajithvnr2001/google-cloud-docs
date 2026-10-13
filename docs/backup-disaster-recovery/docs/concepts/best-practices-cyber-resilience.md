---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/best-practices-cyber-resilience/
title: Configure cyber resilience for Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:16.966293+00:00
---

# Configure cyber resilience for Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/best-practices-cyber-resilience/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure cyber resilience for Backup and DR Stay organized with collections  Save and categorize content based on your preferences. 

A robust backup strategy is essential for cyber resilience. Google Cloud Backup and DR is a managed solution for protecting and restoring workloads. This document outlines architectural recommendations and configuration best practices to help you construct a defense against cyber threats like unauthorized data exfiltration and ransomware.

This guide details the recommended best practices for designing a secure and resilient backup strategy using Google Cloud Backup and DR.

## Before you begin

[Enable the Backup and DR API](https://console.cloud.google.com/apis/library/backupdr.googleapis.com)

### Required roles

To get the permissions that you need to create and manage Backup and DR resources, ask your administrator to grant you the following IAM roles on your project: 

  * To configure and manage Backup and DR resources: [Backup and DR Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.admin) (`roles/backupdr.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Implement a centralized backup architecture

A well-architected backup environment is the first step to limit the extent of a security breach. Use a centralized model to isolate backups from production systems. This model limits the impact of cyber attacks and simplifies data protection management.

  1. **Create a hub project** : Create a dedicated, restricted Google Cloud project for your backup vaults. This project serves as the central management hub for your backups.
  2. **Use spoke projects** : Contain your production and development workloads in separate projects. This isolation ensures that a compromised spoke project does not grant inherent access to the hub project where recovery data is stored.



For more information, see [backup vault architecture](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

## Configure IAM permissions

Protect backup administrative credentials and restrict access to prevent unauthorized deletion of your backups. Apply the principle of least privilege to your backup projects.

  1. **Separate roles** : Ensure the user who triggers a backup is not the same user who can delete a backup or modify retention policies.
  2. **Restrict admin roles** : Limit the number of users with Backup and DR Admin permissions. Assign most users Viewer or Operator roles sufficient for their duties.
  3. **Manage Service Agent permissions** : Ensure the Backup and DR Service Agent has the minimum required permissions in spoke projects to capture and recover data.
  4. **Audit permissions** : Periodically audit the Service Agent's permissions to prevent privilege creep.



For more details, see [Control access with IAM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#roles).

## Configure backup vault security features

Backup and DR provides built-in features to help ensure that your backup data cannot be deleted or altered.

  1. **Enable immutability** : Configure your backup vaults to specify and lock a minimum retention period. This setting prevents any user, including administrators, from deleting backup data before the retention period expires.
  2. **Enforce immutability with Organization Policies** : Use Google Cloud Organization Policies to enforce the use of immutable vaults across all projects.
  3. **Enable CMEK** : Use customer-managed encryption keys (CMEK) to protect backup data with a cryptographic key that you manage through Cloud Key Management Service. You can only configure CMEK when you create a backup vault.
  4. **Use multi-region vaults** : Store data across several geographic areas with multi-region vaults. This provides enhanced security and ensures backup availability during regional disruptions.
  5. **Set access restrictions** : Restrict vault access to and from its organization or project to minimize chances of unauthorized access. You can only configure this setting during vault creation.



## Integrate with Security Command Center

Integrate the Backup and DR with Security Command Center and Google Security Operations. This integration provides visibility into high-risk activities through alerts.

Integrating these services lets you perform the following actions:

  * Get immediate notifications for critical actions, such as when workload protection is disabled.
  * Conduct threat investigations and pinpoint specific backup resources that might be impacted.
  * Consolidate backup-related threats into cases to facilitate efficient and structured mitigation.



To learn more, see [View alerts in Security Command Center](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/alerts-scc).

## Apply platform security guardrails

Use Google Cloud security features to add layers of protection to your backup infrastructure.

  1. **Use Project Liens** : To protect your backup vault from accidental deletion, we strongly recommend applying a project lien to the Google Cloud project where the vault will reside. A project lien prevents the project—and your backups—from being deleted unexpectedly. For more information, see [Protect projects with liens](https://docs.cloud.google.com/resource-manager/docs/project-liens). To secure your project liens against unauthorized removal, use Privileged Access Manager (PAM) to enforce multi-party approval. For more information, see [Protect project liens by using Privileged Access Manager](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/project-liens-multi-party-approval).

  2. **Use VPC Service Controls** : Define a service perimeter around your backup projects to prevent data exfiltration. See [Configure VPC Service Controls](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/vpc-sc).

  3. **Restrict external IPs** : Ensure that your backup/recovery appliances don't have public IP addresses.




## What's next

  * Learn more about [custom constraints for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/customconstraints).
  * Learn more about [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek).
  * Learn more about [multi-region support for backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#multi-regions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
