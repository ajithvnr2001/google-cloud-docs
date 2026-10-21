---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-permissions-reference/
title: Backup and DR installation permissions and roles reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T22:00:24.302092+00:00
---

# Backup and DR installation permissions and roles reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-permissions-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Backup and DR installation permissions and roles reference Stay organized with collections  Save and categorize content based on your preferences. 

During the deployment process, a service account created on your behalf uses these permissions for the duration of the deployment.

## The service account uses these permissions to install the backup/recovery appliance

The service account is highly privileged in the target, VPC project, and consumer projects during the installation. Most of these permissions are removed as the installation progresses. The following table contains the roles granted to the service account and the permissions needed within each role.

Role | Permissions needed | If Shared VPC, then assign to:  
---|---|---  
resourcemanager.projectIamAdmin | resourcemanager.projects.getIamPolicy | VPC Owner, Backup Admin, and Workload projects  
| resourcemanager.projects.setIamPolicy | VPC Owner, Backup Admin, and Workload projects  
iam.serviceAccountUser | iam.serviceAccounts.actAs | Workload project  
iam.serviceAccountTokenCreator | iam.serviceAccounts.getOpenIdToken | Workload project  
cloudkms.admin | cloudkms.keyRings.create | VPC Owner, Backup Admin, and Workload projects  
| cloudkms.keyRings.getIamPolicy | VPC Owner, Backup Admin, and Workload projects  
| cloudkms.keyRings.setIamPolicy | VPC Owner, Backup Admin, and Workload projects  
logging.logWriter | logging.logs.write | Workload project  
compute.admin | compute.instances.create | Workload project  
| compute.instances.delete | Workload project  
| compute.disks.create | Workload project  
| compute.disks.delete | Workload project  
| compute.instances.setMetadata | Workload project  
| compute.subnetworks.get | VPC project  
| compute.subnetworks.use | VPC project  
| compute.subnetworks.setPrivateIpGoogleAccess | VPC project  
| compute.firewalls.create | VPC project  
| compute.firewalls.delete | VPC project  
backupdr.admin | backupdr.managementservers.manageInternalACL | Backup Admin project  
  
## After installation is finished, for daily operation on the workload project

All of the permissions required for deployment and installation are removed except for `iam.serviceAccountUser` and `iam.serviceAccounts.actAs`. Two cloudkms roles needed for daily operation are added, restricted to a single key ring.

Role | Permissions needed  
---|---  
iam.serviceAccountUser | iam.serviceAccounts.actAs  
cloudkms.cryptoKeyEncrypterDecrypter* | cloudkms.cryptoKeyVersions.useToDecrypt  
| cloudkms.cryptoKeyVersions.useToEncrypt  
cloudkms.admin* | cloudkms.keyRings.get  
backupdr.computeEngineOperator* | All permissions listed in the role.  
backupdr.cloudStorageOperator** | All permissions listed in the role.  
  
`*` The `cloudkms` roles are on a single key ring.  
`**` The `cloudStorageOperator` role is on buckets with names that start with the name of the backup/recovery appliance.

## Permissions used to create a firewall on the project

These IAM permissions are used to create a firewall on the project that owns the VPC only during firewall creation.
    
    
    compute.firewalls.create
    compute.firewalls.delete
    compute.firewalls.get
    compute.firewalls.list
    compute.firewalls.update
    compute.networks.list
    compute.networks.get
    compute.networks.updatePolicy
    

**All other permissions are no longer needed after installation.**

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
