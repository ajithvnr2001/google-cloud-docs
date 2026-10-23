---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/protect/automate-protection/
title: Automate resource protection \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:13.035607+00:00
---

# Automate resource protection  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/protect/automate-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Automate resource protection Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This tutorial shows you how to use auto-protection policies and resource labels to automatically protect Compute Engine instances and disks at scale in Backup and DR.

Instead of manually selecting individual resources to protect, auto-protection policies evaluate user-defined resource labels to identify qualifying resources across projects and automatically assign a specified backup plan to them.

## Objectives

  * Configure required Identity and Access Management roles and permissions.
  * Prepare your environment with resource labels.
  * Create an auto-protection policy.
  * View auto-protection policies and protected resources.
  * View applied auto-protection policies in a workload project.
  * Update resource projects associated with an auto-protection policy.
  * Delete an auto-protection policy.



## Costs

This tutorial uses the following billable components of Google Cloud:

  * Backup and DR
  * Compute Engine instances and disks



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

## Before you begin

  1. Select or create a Google Cloud project for your backup vault resources and workload resources:

     * **Backup vault project** : The project that contains your backup vaults, backup plans, and auto-protection policies.

     * **Workload project** : The project that contains the Compute Engine instances or disks to protect.

[Go to Project Selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable billing for your projects.

  3. Enable the Backup and DR API and Compute Engine API in both your backup vault project and workload projects:

[Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=backupdr.googleapis.com,compute.googleapis.com)

  4. [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create) in your backup vault project to store your backups.

  5. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create) in your backup vault project for the resource type (Compute Engine instances or disks) and region that you want to protect.

  6. Ensure that you have the required IAM roles and permissions.




### Required roles and permissions

To get the permissions that you need to create, manage, and view auto-protection policies and policy bindings, ask your administrator to grant you the following IAM roles on the specified projects:

  * **Backup vault project:**
    * To create, edit, and delete auto-protection policies and policy bindings: **Backup and DR Admin** (`roles/backupdr.admin`) or **Backup and DR Editor** (`roles/backupdr.editor`)
    * To view auto-protection policies, policy bindings, and matching resources: **Backup and DR Viewer** (`roles/backupdr.viewer`)
  * **Workload projects:**
    * To authorize auto-protection policies to be applied to the project and manage bindings: **Backup and DR Admin** (`roles/backupdr.admin`) or **Backup and DR Editor** (`roles/backupdr.editor`)
    * To view applied auto-protection policies and matching resources: **Backup and DR Viewer** (`roles/backupdr.viewer`)



#### Service agent roles for cross-project protection

If your workload resources (Compute Engine instances or disks) reside in a different project from your backup vault project, you must grant the appropriate operator role to the backup vault service agent in each target workload project:

  * For Compute Engine instances: **Backup and DR Compute Engine Operator** (`roles/backupdr.computeEngineOperator`)
  * For disks: **Backup and DR Disk Operator** (`roles/backupdr.diskOperator`)



These roles grant the backup vault service agent the necessary permissions to perform backup operations on workload resources in the workload project. For more information, see [Grant a role to the service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup#backup-agent).

**Note:** In both same-project and cross-project configurations, the workload project's Backup and DR service agent is automatically granted the **Backup and DR Service Agent** (`roles/backupdr.serviceAgent`) role to manage backup plan associations within the project.

#### Granular permissions for custom roles

If you prefer to use custom roles instead of predefined roles, ensure that your custom roles include the granular permissions listed in the following table:

Action or operation | Granular permissions | Project where permission is required  
---|---|---  
**Create auto-protection policy** | `backupdr.autoProtectionPolicies.create`  
`backupdr.backupPlans.useForComputeInstance` (for VM instances) or  
`backupdr.backupPlans.useForComputeDisk` (for disks) | Backup vault project  
**Update auto-protection policy** | `backupdr.autoProtectionPolicies.update`  
`backupdr.backupPlans.useForComputeInstance` (for VM instances) or  
`backupdr.backupPlans.useForComputeDisk` (disks) | Backup vault project  
**Delete auto-protection policy** | `backupdr.autoProtectionPolicies.delete` | Backup vault project  
**View auto-protection policies** | `backupdr.autoProtectionPolicies.get`  
`backupdr.autoProtectionPolicies.list` | Backup vault project  
**Create policy binding**  
(Add project to policy) | `backupdr.autoProtectionPolicyBindings.create`  
`backupdr.appliedAutoProtectionPolicies.authorize` | Backup vault project  
Workload project  
**Delete policy binding**  
(Remove project from policy) | `backupdr.autoProtectionPolicyBindings.delete` | Backup vault project  
**View policy bindings** | `backupdr.autoProtectionPolicyBindings.get`  
`backupdr.autoProtectionPolicyBindings.list` | Backup vault project  
**View matching resources** | `backupdr.bindingMatchingResources.list`  
`backupdr.appliedAutoProtectionPolicies.viewMatchingResources` | Backup vault project  
Workload project  
**View applied policies** | `backupdr.appliedAutoProtectionPolicies.list` | Workload project  
  
### Limitations

Keep the following preview limitations in mind:

  * **Supported resources** : Auto-protection policies support Compute Engine instances and disks only.

  * **Scale recommendations** : Do not use production resources. Protect up to 100 projects per policy.

  * **Label key constraint** : When you apply multiple auto-protection policies to a specific project, all policies applied to that project must share the same label key (for example, `env=prod` and `env=test`). You cannot use different label keys (such as `env=prod` and `tier=gold`) for multiple policies applied to the same project. However, different projects can use policies with different label keys.

  * **Management interfaces** : Auto-protection policies can be managed using the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), and API. Support for Terraform will be added in future releases.

  * **Single-region support** : An auto-protection policy protects resources located in a single region. To protect resources across multiple regions, create separate policies for each region.




## Prepare your environment

Before creating an auto-protection policy, apply resource labels (key-value pairs) to the Compute Engine resources you want to protect.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page or **Disks** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Select the resource you want to label.

  3. Add a label key and value (for example, key `env` and value `prod`).

  4. Click **Save**.




###  gcloud 

To label a Compute Engine instance:
    
    
    gcloud compute instances add-labels INSTANCE_NAME \
        --labels=KEY=VALUE \
        --zone=ZONE
    

To label a disk:
    
    
    gcloud compute disks add-labels DISK_NAME \
        --labels=KEY=VALUE \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the VM instance.
  * `DISK_NAME`: the name of the disk.
  * `KEY`: the label key.
  * `VALUE`: the label value.
  * `ZONE`: the zone where the resource resides. For regional disks, use `--region` instead of `--zone`.



## Create an auto-protection policy

To create an auto-protection policy that automatically assigns a backup plan to labeled resources:

###  Console 

  1. In the Google Cloud console, go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  2. In the navigation menu, select **Auto-protection policies**.

  3. Click **Create Auto-protection policy**.

  4. In the **Name your auto-protection policy** section enter the following details:

     1. In the **Auto-protection policy name** field, enter a name for the policy.

     2. In the **Policy description** field, enter an optional description.

     3. Click **Continue**.

  5. In the **Choose the region where your resources are located and select a backup plan** section, enter the following details:

     1. From the **Region** drop-down list, select the region where your resources are located.

     2. In the **This policy is for** section:

        1. Select the resource type to protect, either Compute Engine or disks.

        2. In the **Backup plan** field, click **Select** to choose the backup plan to apply to qualifying resources.

        3. From the **Select a backup plan** pane, select the backup plan you want to associate with the auto-protection policy.

        4. Click **Select**.

     3. Click **Continue**.

  6. In the **Choose projects where your resources are** section, select one or multiple projects in the same organization to protect.

  7. In the **Choose resources to protect** section, enter key-value pairs associated with the resources you want to protect. For example, `env` = `prod`.

  8. Click **Create policy**.




###  gcloud 

  1. Create an auto-protection policy.
         
         gcloud beta backup-dr auto-protection-policies create POLICY_NAME \
             --location=LOCATION \
             --criteria=key=LABEL_KEY,values=LABEL_VALUE \
             --backup-plan-details="resource-type=RESOURCE_TYPE,backup-plan=projects/BACKUP_VAULT_PROJECT/locations/LOCATION/backupPlans/BACKUP_PLAN" \
             --description="DESCRIPTION"
         

Replace the following:

     * `POLICY_NAME`: the name of the auto-protection policy.
     * `LOCATION`: the region where the policy and resources reside.
     * `LABEL_KEY`: the label key to use for matching resources.
     * `LABEL_VALUE`: the label value to use for matching resources.
     * `RESOURCE_TYPE`: the resource type to protect (`compute.googleapis.com/Instance` or `compute.googleapis.com/Disk`).
     * `BACKUP_VAULT_PROJECT`: the project ID where the backup vault and backup plan reside.
     * `BACKUP_PLAN`: the name of the backup plan to assign to matching resources.
     * `DESCRIPTION`: an optional description for the policy.
  2. Add workload projects to the policy by creating a policy binding.
         
         gcloud beta backup-dr auto-protection-bindings create BINDING_NAME \
             --auto-protection-policy=POLICY_NAME \
             --location=LOCATION \
             --scope=projects/WORKLOAD_PROJECT_ID
         

Replace the following:

     * `BINDING_NAME`: a name for the policy binding.
     * `WORKLOAD_PROJECT_ID`: the project ID of the workload project to protect.

Repeat this step for each workload project you want to add to the policy.




Once created, the policy automatically identifies matching resources and schedules backup plan associations. Initial configuration and protection scheduling typically takes up to 2 hours, but in some cases can take up to 8 hours.

## View auto-protection policies

As a backup administrator, you can view auto-protection policies created in your backup vault project and monitor the workload projects and resources they protect.

To view auto-protection policies and their protected resources:

###  Console 

  1. In the Google Cloud console, select your backup vault project.

  2. Go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  3. In the navigation menu, select **Auto-protection policies**.

  4. On the **Policies created in this project** tab, select the **Auto-protection policies** view.

  5. Click the policy you want to view.

The **Auto-protection policy details** page appears.

  6. To view the workload projects associated with the policy and their matching, protected, and failed resource counts, select the **Protected resources** tab.




###  gcloud 

To list all auto-protection policies in a specific location:
    
    
    gcloud beta backup-dr auto-protection-policies list --location=LOCATION
    

To view details of a specific auto-protection policy:
    
    
    gcloud beta backup-dr auto-protection-policies describe POLICY_NAME --location=LOCATION
    

To list resources matching a specific policy binding (workload project):
    
    
    gcloud beta backup-dr binding-matching-resources list \
        --auto-protection-policy-binding=BINDING_NAME \
        --auto-protection-policy=POLICY_NAME \
        --location=LOCATION
    

Replace the following:

  * `LOCATION`: the location of the auto-protection policies.
  * `POLICY_NAME`: the name of the auto-protection policy.
  * `BINDING_NAME`: the name of the policy binding.



## View applied auto-protection policies

As a workload administrator, you can view auto-protection policies applied to resources in your workload project. These policies are created and managed within their respective backup vault projects.

To view applied auto-protection policies in a workload project:

###  Console 

  1. In the Google Cloud console, select your workload project.

  2. Go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  3. In the navigation menu, select **Auto-protection policies**.

  4. Select the **Policies applied on this project** tab.




###  gcloud 

To list applied auto-protection policies in a specific location:
    
    
    gcloud beta backup-dr applied-auto-protection-policies list --location=LOCATION
    

Replace the following:

  * `LOCATION`: the location of the applied auto-protection policies.



The **Applied auto-protection policies** table displays the policies applied to resources in the project, along with the following information:

  * **Policy name** : The name of the auto-protection policy. Click the policy name to view policy details in the backup vault project.
  * **Resource type** : The resource type protected by the policy (Compute Engine instances or disks).
  * **Criteria** : The resource labels (key-value pairs) used to match resources in the project.
  * **Backup vault project** : The backup vault project where the policy and backup vault are managed.
  * **Status** : The status of the policy binding (for example, `Active`).
  * **Region** : The region where the policy and protected resources reside.
  * **Backup plan** : The backup plan assigned to matching resources. Click the backup plan name to view its details in the backup vault project.
  * **Matching resources** : The number of resources in the workload project that match the label criteria.
  * **Protected resources** : The number of matching resources successfully protected by the backup plan.
  * **Resources failed to protect** : The number of matching resources that failed protection.



## Edit an auto-protection policy

To edit auto-protection policies and their protected resources:

###  Console 

  1. In the Google Cloud console, go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  2. In the navigation menu, select **Auto-protection policies**.

The **Auto-protection policies** page appears.

  3. Click the auto-protection policy you want to edit.

  4. In the **Auto-protection policy details** page, click **Edit policy**.

  5. Make the necessary changes to the auto-protection policy.

  6. Click **Save changes**.




###  gcloud 

To update the description of an auto-protection policy:
    
    
    gcloud beta backup-dr auto-protection-policies update POLICY_NAME \
        --location=LOCATION \
        --description="UPDATED_DESCRIPTION"
    

To update the criteria (labels) of an auto-protection policy:
    
    
    gcloud beta backup-dr auto-protection-policies update POLICY_NAME \
        --location=LOCATION \
        --criteria=key=NEW_LABEL_KEY,values=NEW_LABEL_VALUE
    

To update the backup plan details:
    
    
    gcloud beta backup-dr auto-protection-policies update POLICY_NAME \
        --location=LOCATION \
        --backup-plan-details="resource-type=RESOURCE_TYPE,backup-plan=projects/BACKUP_VAULT_PROJECT/locations/LOCATION/backupPlans/NEW_BACKUP_PLAN"
    

Replace the following:

  * `POLICY_NAME`: the name of the auto-protection policy to update.
  * `LOCATION`: the location of the auto-protection policy.
  * `UPDATED_DESCRIPTION`: the updated description for the policy.
  * `NEW_LABEL_KEY`: the new label key to use for matching resources.
  * `NEW_LABEL_VALUE`: the new label value to use for matching resources.
  * `RESOURCE_TYPE`: the resource type to protect (`compute.googleapis.com/Instance` or `compute.googleapis.com/Disk`).
  * `BACKUP_VAULT_PROJECT`: the project ID where the backup vault and backup plan reside.
  * `NEW_BACKUP_PLAN`: the name of the new backup plan to assign.



## Update resource projects in an auto-protection policy

You can modify the scope of an existing auto-protection policy by adding or removing workload projects.

### Add projects to a policy

###  Console 

  1. In the Google Cloud console, go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  2. In the navigation menu, select **Auto-protection policies**.

  3. Click the policy you want to update.

  4. Click **Add projects**.

The **Add projects to policy** page appears.

  5. Click **Select projects**.

  6. In the **Search projects** field, enter the name of the project you want to add to the policy.

  7. Check the box next to the name of the project you want to add to the policy.

  8. Click **Select**.

  9. Click **Add**.

A confirmation message appears.




###  gcloud 

To add a workload project to an auto-protection policy, create a policy binding:
    
    
    gcloud beta backup-dr auto-protection-bindings create BINDING_NAME \
        --auto-protection-policy=POLICY_NAME \
        --location=LOCATION \
        --scope=projects/WORKLOAD_PROJECT_ID
    

Replace the following:

  * `BINDING_NAME`: a name for the policy binding.
  * `POLICY_NAME`: the name of the auto-protection policy.
  * `LOCATION`: the location of the auto-protection policy.
  * `WORKLOAD_PROJECT_ID`: the project ID of the workload project to protect.



### Remove projects from a policy

###  Console 

  1. In the Google Cloud console, go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  2. In the navigation menu, select **Auto-protection policies**.

  3. Click the policy you want to update.

  4. Select the **Protected resources** tab.

  5. Select the projects you want to remove from the policy scope.

  6. Click **Remove projects**.

  7. To confirm that you want to remove the auto-protection policy from the project, enter `confirm`.

  8. Click **Remove**.

A confirmation notification appears.




###  gcloud 

To remove a workload project from an auto-protection policy, delete the policy binding:
    
    
    gcloud beta backup-dr auto-protection-bindings delete BINDING_NAME \
        --auto-protection-policy=POLICY_NAME \
        --location=LOCATION
    

Replace the following:

  * `BINDING_NAME`: the name of the policy binding to delete.
  * `POLICY_NAME`: the name of the auto-protection policy.
  * `LOCATION`: the location of the auto-protection policy.



Unprotecting resources and removing projects typically takes up to 2 hours, but in some cases can take up to 8 hours.

## Delete an auto-protection policy

Before deleting an auto-protection policy, you must remove all workload projects from the policy's scope. For instructions, see Remove projects from a policy.

To delete an auto-protection policy:

###  Console 

  1. In the Google Cloud console, go to the **Backup and DR** page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  2. In the navigation menu, select **Auto-protection policies**.

  3. Click the policy you want to delete.

  4. Click **Delete policy**.

  5. In the confirmation dialog, click **Delete**.




###  gcloud 

To delete an auto-protection policy:
    
    
    gcloud beta backup-dr auto-protection-policies delete POLICY_NAME --location=LOCATION
    

Replace the following:

  * `POLICY_NAME`: the name of the auto-protection policy to delete.
  * `LOCATION`: the location of the auto-protection policy.



## Clean up

To avoid incurring charges to your Google Cloud account for resources used in this tutorial:

  1. Delete any auto-protection policies created during this tutorial.

  2. Remove resource labels from test Compute Engine VMs and disks if you no longer want them protected.

  3. If you created a dedicated Google Cloud project for this tutorial, delete the project:

     1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

     2. Select the project and click **Delete**.

     3. Enter the project ID and click **Shut down**.




## What's next

  * Learn more about [Backup plans in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan).
  * Learn how to [Back up Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup).
  * Learn about [Customer-managed encryption keys (CMEK) with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek).
  * For questions or feedback regarding the preview, contact [backupdr-autoprot-preview-feedback@google.com](mailto:backupdr-autoprot-preview-feedback@google.com).
  * Try out other Google Cloud features for yourself. Have a look at our [tutorials](https://cloud.google.com/docs/tutorials).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
