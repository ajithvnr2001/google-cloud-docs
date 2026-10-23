---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/best-practices-ransomware/
title: Best practices to defend against ransomware with Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:34.707699+00:00
---

# Best practices to defend against ransomware with Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/best-practices-ransomware/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Best practices to defend against ransomware with Backup and DR Stay organized with collections  Save and categorize content based on your preferences. 

A robust backup strategy is essential for maintaining cyber resilience. Google Cloud offers Backup and DR, a managed solution designed for protecting and restoring workloads in Google Cloud environments. This service provides a unified platform for the centralized management, monitoring, and reporting of daily backup activities, and it integrates smoothly with existing automation tools like APIs and Terraform.

This page outlines architectural recommendations and configuration best practices for Google Cloud Backup and DR. These guidelines are intended to help you construct a sturdy defense against cyber threats, with a particular focus on mitigating the risks of unauthorized data exfiltration and ransomware attacks.

## Plan the backup architecture

A well-architected backup environment is the first step to limiting the damage that can be caused in the event of a security breach.

### Implement a centralized model

Using a centralized model (similar to a hub-and-spoke model) lets you isolate your backups from your production systems, thereby limiting the impact of possible cyber attacks while also making it easier to manage and govern your data protection.

  * The Hub (Backup Project): Create a dedicated, restricted Google Cloud project for your Backup Vaults to store your backed up data. This project also becomes your central management hub for managing your backups.

  * The Spokes (Workload Projects): These include the projects that contain your production and development workloads, which need to be protected. This isolation ensures that even if a 'Spoke' project is compromised, the attacker does not have inherent access to the 'Hub' project where the recovery data is stored.




For more details about centralized and decentralized backup strategies, see [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

## Manage identity and access

Identity is often referred to as 'the new perimeter', referring to security perimeters going beyond just network firewalls. Protecting backup administrative credentials and restricting access is one of the most critical steps in preventing ransomware from deleting your backups.

### Apply minimal access to backup vaults

Apply the principle of least privilege strictly to your backup projects:

  * Separate roles: Ensure that the user who can trigger a backup is not the same user who has the authority to delete a backup or modify retention policies.

  * Restrict Backup Admin roles: Limit the number of users with Cloud Backup and DR Admin permissions. Most users should only have Viewer or Operator roles which should suffice for them to perform their duties.




[Control access to Backup and DR with IAM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#roles) throws more light on the Identity and Access Management (IAM) roles and permissions that are required by Backup and DR.

### Manage service agent permissions

Backup and DR uses a service agent to perform cross-project operations.

Ensure the service agent has the minimum required permissions in the 'Spoke' projects to capture and recover data.

Periodically audit the service agent's permissions to ensure no 'privilege creep' has occurred.

## Configure core backup capabilities

Google Cloud Backup provides various built-in features that can help you ensure that your backup data cannot be deleted, altered or bypassed.

### Enable immutability and lock settings

Immutable Backups: Configure your backup vaults to specify and lock a minimum retention period. This prevents any users, including those with administrative privileges, from deleting backup data before the intention retention period expires.

Org Policies: Use Google Cloud Organization Policies to enforce the use of immutable vaults across all projects. To learn more about using the Organization Policy Service service to implement custom constraints for specific operations, see [Creating custom constraints for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/customconstraints).

### Enable customer-managed encryption keys

Using customer-managed encryption keys (CMEK) for backups lets you protect your backup data using a cryptographic key that is managed by you through the Cloud Key Management Service (Cloud KMS).

When you use CMEK, you manage the key in Cloud KMS, and you can control who can access it by managing IAM permissions on the key. You can configure CMEK on a backup vault only when you create it. You cannot enable or disable CMEK on an existing backup vault.

Learn more about CMEK for encrypting your backups in [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek).

### Use multi-region vaults

Google Cloud Backup multi-region vaults store data across several geographic areas. This provides enhanced security and ensures backup availability during unforeseen events.

Benefits of multi-region backup vaults include:

  * Continuous access: Maintain data recoverability during regional disruptions like power outages or natural disasters.
  * Business continuity: Support on-demand recoveries to ensure reliable business operations.
  * Data security: Retain all core security advantages provided by standard backup vaults.



To learn more about support for multi-region backup vaults, see [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#multi-regions).

### Set access restrictions

Restricting vault access to and from its organization or project can help minimize chances of unauthorized access to your backup data. Note that this setting is configured during vault creation and cannot be changed later.

Refer to [Backup vault access restriction](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#access-restrictions) for more details.

## Configure integrated security alerts

Backup and DR integrates with Security Command Center and Google Security Operations to provide visibility into high-risk activities using alerts surfaced within those platforms.

By leveraging Google SecOps and Security Command Center alongside Backup and DR, you are able to:

  * Get immediate notifications regarding critical actions, such as when workload protection is disabled.
  * Conduct threat investigations and pinpoint specific backup resources that may be impacted.
  * Consolidate backup-related threats into cases to facilitate efficient and structured mitigation.



[Learn more about Security Command Center and Google SecOps for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/alerts-scc).

## Use Google Cloud platform guardrails

Use Google Cloud security features to add additional layers of protection to your backup infrastructure.

### Use project liens

To protect your backup vault from accidental deletion, we strongly recommend applying a project lien to the Google Cloud project where the vault will reside. A project lien prevents the project—and your backups—from being deleted unexpectedly. For more information, see [Protect projects with liens](https://docs.cloud.google.com/resource-manager/docs/project-liens).

To secure your project liens against unauthorized removal, use Privileged Access Manager (PAM) to enforce multi-party approval. For more information, see [Protect project liens by using Privileged Access Manager](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/project-liens-multi-party-approval).

**Important:** Beginning November 1, 2026, Backup and DR will automatically apply a project-level lien to any project containing a backup vault with backups protected by enforced retention.

### Use network constraints and VPC Service Controls

VPC Service Controls (VPC-SC): Define a service perimeter around your backup projects to prevent data exfiltration.

Restrict External IPs: Ensure that backup management appliances don't have public IP addresses.

## Summary of best practices

The following table summarizes the best practices recommended in this document:

Topic | Task  
---|---  
Plan the backup architecture | Implement a centralized model to isolate backups from production systems.  
Manage identity and access | Apply the principle of least privilege to backup vaults.  
Manage and audit service agent permissions.  
Configure core backup capabilities | Enable immutability and lock settings to prevent premature data deletion.  
Enable customer-managed encryption keys (CMEK) for data protection.  
Use multi-region vaults for enhanced availability and security.  
Set access restrictions on backup vaults.  
Configure integrated security alerts | Integrate with Security Command Center and Google SecOps for threat visibility.  
Use Google Cloud platform guardrails | Use project liens to prevent accidental or malicious project deletion.  
Use network constraints and VPC Service Controls to prevent data exfiltration.  
  
## What's next

  * Learn more about [centralized and decentralized backup strategies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).
  * Review [IAM roles and permissions for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control#roles).
  * See how to use the [Organization Policy service for custom constraints](https://docs.cloud.google.com/backup-disaster-recovery/docs/customconstraints).
  * Read about [using CMEK for encrypting backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek).
  * Learn about [monitoring and alerts with Security Command Center](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/alerts-scc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
