---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-prep/
title: Prepare to deploy a backup/recovery appliance \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:35.446898+00:00
---

# Prepare to deploy a backup/recovery appliance  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-prep/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Prepare to deploy a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## Before you begin

It's a good idea to read [Plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan) before you begin this section.

This page details the Google Cloud requirements that must be met before you enable Google Cloud Backup and DR which must be done in the Google Cloud console.

All of the tasks outlined in this page must be performed in the Google Cloud project where you are deploying your backup/recovery appliance. If this project is a Shared VPC service project, then some tasks are performed in the VPC project and some in the workload project.

## Allow trusted image projects

#### Permissions required for this task

This is an organization level policy that might not be set or even exist. To change this, your user needs to have the following permissions:

  * `orgpolicy.policies.create`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policies.delete`
  * `orgpolicy.policy.get`
Example roles that have this permission include: **Organization Policy Administrator** 


If you have enabled the `constraint/compute.trustedImageProjects` policy in the **Organization** policies, then the Google Cloud-managed source project for the images used to deploy the backup/recovery appliance is not allowed. You need to customize this organization policy in the projects where backup/recovery appliances are deployed to avoid getting a policy violation error during the deployment as detailed in the following instructions:

  1. Go to the **Organization policies** page and select the project where you deploy your appliances. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/)

  2. In the policies list, click **Define trusted image projects**.

  3. Click **Edit** to customize your existing trusted image constraints.

  4. On the **Edit** page, select **Customize**.

  5. Select from the following three possibilities:

### Existing inherited policy

If there is an existing inherited policy, complete the following:

     1. For **Policy enforcement** select **Merge with parent**.

     2. Click **Add rule**.

     3. Select **Custom** from the **Policy values** drop-down list to set the constraint on specific image projects.

     4. Select **Allow** from the **Policy type** drop-down list to remove restrictions for the specified image projects.

     5. In the **Custom values** field, enter the custom value as **projects/backupdr-images**.

     6. Click **Done**.

### Existing **Allow** rule

If there is an existing **Allow** rule, then complete the following steps:

     1. Leave the **Policy enforcement** to the default selected.

     2. Select the existing **Allow** rule.

**Caution:** If a rule exists, use it. Don't try to add an additional rule.
     3. Click **Add value** to add additional image projects and enter the value as **projects/backupdr-images**.

     4. Click **Done**.

### No existing policy or rule

If there is no existing rule, select **Add rule** and then complete the following steps:

     1. Leave the **Policy enforcement** to the default selected.

     2. Select **Custom** from the **Policy values** drop-down list to set the constraint on specific image projects.

     3. Select **Allow** from the **Policy type** drop-down list to remove restrictions for the specified image projects.

     4. In the **Custom values** field, enter the custom value as **projects/backupdr-images**.

     5. If you are setting project-level constraints, then they might conflict with the [existing constraints set on your organization or folder](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

     6. Click **Add value** to add additional image projects and click **Done**.

     7. Click **Save**.

  6. Click **Save** to apply the constraint.

For more information about creating organization policies, see [Create and manage organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).




## The deployment process

To launch the installation, Backup and DR creates a service account to run the installer. The service account requires privileges in the host project, the backup/recovery appliance service project, and the appliance management console service project. For more information, see [service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

The service account used for installation becomes the service account of the backup/recovery appliance. After installation, the permissions of the service account are reduced to just the permissions required by the backup/recovery appliance.

If you deploy multiple backup/recovery appliances, each appliance must be associated with a unique Service Account. Using the same Service Account for multiple appliances can lead to registration timeouts or management failures.

The appliance management console is deployed when you install the first backup/recovery appliance. You can deploy Backup and DR in a Shared VPC or in a non-shared VPC.

## Backup and DR in a non-shared VPC

When deploying the appliance management console and the first backup/recovery appliance is in a single project with a non-shared VPC, then all three Backup and DR components are in the same project.

**Note:** CMEK must be disabled on the project where the backup/recovery appliance is deployed.

If the VPC is shared, see Backup and DR in a Shared VPC.

### Enable the required APIs for installation in a non-shared VPC

Before enabling the required APIs for installation in a non-shared VPC, review the Backup and DR deployment supported regions. See [Supported regions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan#regions).

To run the installer in a non-shared VPC, the following APIs must be enabled. To enable APIs, you need the role **Service usage admin**.

API | Service name  
---|---  
Compute Engine | compute.googleapis.com  
Resource Manager | cloudresourcemanager.googleapis.com  
Workflows 1 | workflows.googleapis.com  
Cloud Key Management Service (KMS) | cloudkms.googleapis.com  
Identity and Access Management | iam.googleapis.com  
Cloud Logging | logging.googleapis.com  
  
1 Workflow service is supported in the listed [regions](https://docs.cloud.google.com/workflows/docs/locations). If the Workflows service is not available in a region where the backup/recovery appliance is being deployed, then Backup and DR defaults to "us-central1" region. If you have an organization policy that is set to prevent creating resources in other regions, then you need to temporarily update your organization policy to allow creation of resources in "us-central1" region. You can restrict the "us-central1" region after the backup/recovery appliance deployment.

### The user account requires these permissions in the non-shared VPC project

Preferred role | Permissions needed  
---|---  
resourcemanager.projectIamAdmin (Project IAM Admin) | resourcemanager.projects.getIamPolicy  
| resourcemanager.projects.setIamPolicy  
| resourcemanager.projects.get  
| iam.serviceAccounts.delete  
| iam.serviceAccounts.get  
| workflows.workflows.delete  
| workflows.executions.create  
| workflows.executions.get  
| workflows.operations.get  
serviceusage.serviceUsageAdmin (Service Usage Admin) | serviceusage.services.list  
iam.serviceAccountUser (Service Account User) | iam.serviceAccounts.actAs  
iam.serviceAccountAdmin (Service Account Admin) | iam.serviceAccounts.create  
| iam.serviceAccounts.delete  
| iam.serviceAccounts.get  
workflows.editor (Workflows Editor) | workflows.workflows.create  
| workflows.workflows.delete  
| workflows.executions.create  
| workflows.executions.get  
| workflows.operations.get  
backupdr.admin (Backup and DR Admin) | backupdr.*  
viewer (Basic) | Grants the [permissions](https://docs.cloud.google.com/iam/docs/roles-overview#basic) required to view   
most of Google Cloud resources.  
  
## Backup and DR in a Shared VPC

When deploying the appliance management console and the first backup/recovery appliance in a Shared VPC project, you must configure these three projects in either the host project or in one or more service projects:

Before enabling the required APIs for installation in a Shared VPC, review the Backup and DR deployment supported regions. See [Supported regions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan#regions).

**Note:** CMEK must be disabled on the project where any backup/recovery appliance is deployed.

  * **VPC owner project** : This owns the selected VPC. The VPC owner is always the host project.

  * **appliance management console project** : This is where the Backup and DR API is activated and where you access the appliance management console to manage workloads.

  * **Backup/recovery appliance project** : This is where the backup/recovery appliance is installed and usually where the protected resources reside.




In a Shared VPC, these may be one, two, or three projects.

Type | VPC Owner | Appliance management console | Backup/recovery appliance  
---|---|---|---  
HHH | Host project | Host project | Host project  
HHS | Host project | Host project | Service project  
HSH | Host project | Service project | Host project  
HSS | Host project | Service project | Service project  
HS2 | Host project | Service project | A different service project  
  
### Descriptions of the deployment strategies

  * **HHH** : Shared VPC. The VPC owner, the appliance management console, and the backup/recovery appliance are all in the host project.

  * **HHS** : Shared VPC. The VPC owner and the appliance management console are in the host project, and the backup/recovery appliance is in a service project.

  * **HSH** : Shared VPC. The VPC owner and the backup/recovery appliance are in the host project, and the appliance management console is in a service project.

  * **HSS** : Shared VPC. The VPC owner is in the host project, and the backup/recovery appliance and the appliance management console are in one service project.

  * **HS2** : Shared VPC. The VPC owner is in the host project, and the backup/recovery appliance and the appliance management console are in two different service projects.




### Enable these required APIs for installation in the host project

To run the installer, the following APIs must be enabled. To enable APIs, you need the role **Service usage admin**.

API | Service name  
---|---  
Compute Engine | compute.googleapis.com  
Resource Manager | cloudresourcemanager.googleapis.com  
  
### Enable these required APIs for installation in the backup/recovery appliance project

API | Service name  
---|---  
Compute Engine | compute.googleapis.com  
Resource Manager | cloudresourcemanager.googleapis.com  
Workflows 1 | workflows.googleapis.com  
Cloud Key Management Service (KMS) | cloudkms.googleapis.com  
Identity and Access Management | iam.googleapis.com  
Cloud Logging | logging.googleapis.com  
**Note:** The backup/recovery appliance requires access to the Google Cloud APIs. If the subnet network settings don't allow the VMs to access the Google Cloud APIs, then the backup/recovery appliance deployment fails. Make sure the subnet where you have deployed the backup/recovery appliance has access to Google Cloud APIs and services. Refer to [Configure private Google Cloud access|VPC](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config) for additional information on how to configure this.

1 Workflow service is supported in the listed [regions](https://docs.cloud.google.com/workflows/docs/locations). If the Workflows service is not available in a region where backup/recovery appliance is being deployed, then Backup and DR defaults to the "us-central1" region. If you have an organization policy that is set to prevent creating resources in other regions, then you need to temporarily update your organization policy to allow creation of resources in "us-central1" region. You can restrict the "us-central1" region after the backup/recovery appliance deployment.

### The user account requires these permissions in the VPC owner project

**Note:** The roles may grant more permissions than you need. For minimum required permissions, assign only those listed in the **Permissions needed** column.Preferred Role | Permissions needed  
---|---  
resourcemanager.projectIamAdmin (Project IAM Admin) | resourcemanager.projects.getIamPolicy  
| resourcemanager.projects.setIamPolicy  
| resourcemanager.projects.get  
| iam.serviceAccounts.delete  
| iam.serviceAccounts.get  
| workflows.workflows.delete  
| workflows.executions.create  
| workflows.executions.get  
| workflows.operations.get  
serviceusage.serviceUsageAdmin (Service Usage Admin) | serviceusage.services.list  
  
### The user account requires these permissions in the appliance management console project

**Note:** The roles may grant more permissions than you need. For minimum required permissions, assign only those listed in the **Permissions** needed column.

The appliance management console is deployed when you install the first backup/recovery appliance.

Preferred Role | Permissions needed  
---|---  
resourcemanager.projectIamAdmin (Project IAM Admin) | resourcemanager.projects.getIamPolicy  
| resourcemanager.projects.setIamPolicy  
| resourcemanager.projects.get  
| iam.serviceAccounts.delete  
| iam.serviceAccounts.get  
| workflows.workflows.delete  
| workflows.executions.create  
| workflows.executions.get  
| workflows.operations.get  
backupdr.admin (Backup and DR Admin) | backupdr.*  
viewer (Basic) | Grants the [permissions](https://docs.cloud.google.com/iam/docs/roles-overview#basic) required to view   
most Google Cloud resources.  
  
### The user account requires these permissions in the backup/recovery appliance project

**Note:** The roles may grant more permissions than you need. For minimum required permissions, assign only those listed in the **Permissions** needed column.Preferred Role | Permissions needed  
---|---  
resourcemanager.projectIamAdmin (Project IAM Admin) | resourcemanager.projects.getIamPolicy  
| resourcemanager.projects.setIamPolicy  
| resourcemanager.projects.get  
iam.serviceAccountUser (Service Account User) | iam.serviceAccounts.actAs  
|   
iam.serviceAccountAdmin (Service Account Admin) | iam.serviceAccounts.create  
| iam.serviceAccounts.delete  
| iam.serviceAccounts.get  
workflows.editor (Workflows Editor) | workflows.workflows.create  
| workflows.workflows.delete  
| workflows.executions.create  
| workflows.executions.get  
| workflows.operations.get  
serviceusage.serviceUsageAdmin (Service Usage Admin) | serviceusage.services.list  
  
In addition to the end user account permissions, [other permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-permissions-reference) are temporarily granted to the service account created on your behalf until the installation is complete.

## Configure networks

If a VPC network has not already been created for your target project, you need one created before proceeding. See [Create and modify Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) for details. You need a subnet in each region where you plan to deploy a backup/recovery appliance, and the should be assigned with the `compute.networks.create` permission create it.

If you are deploying backup/recovery appliances in multiple networks, use subnets that don't share the same IP address ranges to prevent multiple backup/recovery appliances from having the same IP address.

## Configure Private Google Access

The backup/recovery appliance communicates with the appliance management console using [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access). It's recommended that you enable Private Google Access for each subnet where you want to deploy a backup/recovery appliance.

The subnet where the backup/recovery appliance is deployed needs to communicate to a unique domain hosted under the domain `backupdr.googleusercontent.com`. It's recommended that you include the following configuration in Cloud DNS:

  1. [Create a private zone](https://docs.cloud.google.com/dns/docs/zones#create-private-zone) for the DNS name `backupdr.googleusercontent.com`.
  2. Create an `A` record for the domain `backupdr.googleusercontent.com` and include each of the four IP addresses `199.36.153.8`, `199.36.153.9`, `199.36.153.10`, `199.36.153.11` from the `private.googleapis.com` subnet `199.36.153.8/30`. If you're using VPC Service Controls, then use `199.36.153.4`, `199.36.153.5`, `199.36.153.6`, `199.36.153.7` from the `restricted.googleapis.com` subnet `199.36.153.4/30`.
  3. Create a `CNAME` record for `*.backupdr.googleusercontent.com` that points to the domain name `backupdr.googleusercontent.com`.



This ensures that any DNS resolution for your unique appliance management console domain traverses using Private Google Access.

Ensure that your firewall rules have an egress rule that allows access on TCP `443` to either the `199.36.153.8/30` or `199.36.153.4/30` subnet. Also, if you have an egress rule that allows all traffic to `0.0.0.0/0`, then connectivity between the backup/recovery appliances and the appliance management console should succeed.

## Create a Cloud Storage bucket

You need a Cloud Storage bucket if you want to protect databases and file systems using the Backup and DR agent, and then copy the backups to Cloud Storage for long term retention. This also applies for VMware VM backups created using VMware vSphere storage APIs data protection.

#### Permissions required for this task

To create a Cloud Storage bucket you need a role that contains the following permissions:

  * `storage.buckets.get`
  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.get`
  * `storage.objects.list`
  * `iam.serviceAccountKeys.create`
Roles that have these permissions include `Storage Admin` and `Editor`. 


Create a Cloud Storage bucket using the following instructions:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.   


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click **Create bucket**.

  3. Enter a name for the bucket.

  4. Choose a region to store your data in and click **Continue**.

  5. Choose a default storage class and click **Continue**. Use nearline when retention is 30 days or less or coldline when retention is 90 days or more. If retention is between 30 and 90 days then consider using coldline.

  6. Leave **Uniform access control** selected and click **Continue**. Don't use fine-grained.

  7. Leave **Protection** tools set to **None** and click **Continue**. Don't select other choices as they don't work with Backup and DR.

  8. Click **Create**.

  9. Validate that your service account has access to your bucket:

     1. Select your new bucket to display the bucket details.

     2. Go to **Permissions**.

     3. Under **Principals** , ensure your new service accounts are listed. If they are not then use the **Add** button to add both reader and writer service accounts as principals.

**Note:** The service account attached to the appliance by default cannot access user-created buckets as the `Backup and DR Cloud Storage Operator` role is added with an IAM condition that only allows it to access buckets if the bucket that is created starts with the same name of the appliance. Due to this, you must manually add the service account as a principal against each user-created bucket that you add to an OnVault pool.



## What's next

  * [Deploy Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-guide)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
