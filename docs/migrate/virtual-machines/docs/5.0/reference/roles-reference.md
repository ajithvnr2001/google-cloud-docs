---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/roles-reference/
title: Roles and permissions reference \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:52.337577+00:00
---

# Roles and permissions reference  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/roles-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Roles and permissions reference Stay organized with collections  Save and categorize content based on your preferences. 

This document contains a reference for the different roles and permissions required by Migrate to Virtual Machines. In Google Cloud, roles and permissions are typically associated with [service account](https://docs.cloud.google.com/iam/docs/service-accounts) or [user account](https://docs.cloud.google.com/iam/docs/overview).

The following sections describes these roles and permissions organized by the major components of Migrate to Virtual Machines:

  * Google Cloud console user accounts
  * Migrate to Virtual Machines default service account
  * Target project service account



In addition, Cloud [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) includes two predefined roles that you can use to control access for users in your organization.

Role | Title | Description  
---|---|---  
[roles/vmmigration.admin](https://docs.cloud.google.com/iam/docs/understanding-roles) | VM Migration Administrator  | Allows users to create new Migrate to Virtual Machines sources and perform all other migration operations.   
[roles/vmmigration.viewer](https://docs.cloud.google.com/iam/docs/understanding-roles) | VM Migration Viewer  | Allows users to retrieve information about Migrate to Virtual Machines in the Google Cloud console. Intended for users who monitor migrations but don't perform them.   
  
For example, if you want to allow a user in your organization to be able to view information about a migration, but not be able to perform a migration, assign them the role `roles/vmmigration.viewer`.

## Google Cloud console user accounts

A Migrate to Virtual Machines _target_ project defines the destination project for a Compute Engine instance running your migrated VM. The Migrate to Virtual Machines _host_ project can be used as a target project. If you want to migrate VMs to additional projects, you must add them as _target_ projects to Migrate to Virtual Machines.

For a user to be able to add a target project, and to configure the details of the Compute Engine instance on the target project, that user requires the necessary [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles and permissions.

Because you perform these actions in the [Google Cloud console](https://console.cloud.google.com/), the user account that requires these permissions is the account that you use to sign in to the Google Cloud console:

  * To **add** a target project to Migrate to Virtual Machines, the user account you use to sign in to the Google Cloud console requires the permissions described in Permissions to add a target project.

  * To **configure the target details** of the Compute Engine instance running on the target project, the user account you use to sign in to the Google Cloud console requires permissions to access data in the target project, such as networks, instance types, and more. See Permissions to configure a target instance.




Depending on how you configure IAM for your environment, you might configure a single user to perform both actions, or configure two separate users.

### Permissions to add a target project

To add a target project, the user account you use to sign in to the Google Cloud console requires:

  * The role `vmmigration.admin` on the **host** project
  * The role `resourcemanager.projectIamAdmin` on the **target** project

**Note:** If your user account does not have the `resourcemanager.projectIamAdmin` role on the target project, or you are forbidden from adding it for security reasons, you can still add the target project. However, a warning icon, _warning_ , appears next to the project name when you add it and you won't be able to deploy Compute Engine instances on the target project.

As a workaround, contact the security administrator for the target project to get your user account configured with the `resourcemanager.projectIamAdmin` role, and then try to add the target project. 

Alternatively, after you add the target project, assign the role `vmmigration.serviceAgent` on the target project to the Migrate to Virtual Machines default service account.




See [Configuring permissions on host project default service account](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-sa-compute-engine) for instructions on setting these permissions.

### Permissions to configure target details for a Compute Engine instance

To configure the target details of the Compute Engine instance on the target project, the user account you use to sign in on the Google Cloud console requires:

  * The role `roles/compute.viewer` on the **target** project

**Note:** If your environment uses a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), then the user account also requires this permission on the **Shared VPC host project**.



See [Configuring permissions on host project default service account](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-sa-compute-engine) for instructions on setting these permissions.

## Migrate to Virtual Machines default service account

Migrate to Virtual Machines creates a default service account on the host project when you enable the Migrate to Virtual Machines API, and assigns it the role `vmmigration.serviceAgent`. Migrate to Virtual Machines uses this service account to create the Compute Engine instance on the target project as part of test-clone and cut over.

Depending on your environment, you might have to edit the permissions on the default service account.

### Permissions when using a Shared VPC on the target project

To deploy a Compute Engine instance to a target project that accesses a Shared VPC, you must add the `compute.networkUser` role to the Migrate to Virtual Machines default service account to allow it access to subnetworks in the Shared VPC host project.

See [Configuring permissions for a Shared VPC](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/shared-vpc) for instructions on setting these permissions.

## Target project service account

By default, when you deploy your migrated VM to a target Compute Engine instance, no service account is assigned to the instance.

If the Compute Engine instance requires access to Google Cloud services and APIs, [create a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount) in the target project with the necessary permissions to access those services and APIs. Then, attach the service account to the Compute Engine instance as part of configuring the target details.

However, to attach the target service account to the Compute Engine instance, the Migrate to Virtual Machines default service account requires the necessary permissions, as described in [Configuring permissions on target project service account](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-sa-compute-engine).

## Permissions to configure AWS as a source

This section details the fields of the permissions JSON template. For details on how to implement migration permissions review the [Create an AWS IAM policy](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-aws-source#create-an-iam-policy) section.
    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "ec2:DescribeInstances",
                    "ec2:DescribeVolumes",
                    "ec2:DescribeInstanceTypes",
                    "ec2:DescribeSnapshots",
                    "ec2:CreateTags",
                    "ec2:CreateSnapshots",
                    "ec2:StopInstances"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "ebs:ListSnapshotBlocks",
                    "ebs:ListChangedBlocks",
                    "ebs:GetSnapshotBlock",
                    "ec2:DeleteSnapshot",
                    "ec2:DeleteTags"
                ],
                "Resource": "*",
                "Condition": {
                    "StringEquals": {
                        "aws:ResourceTag/m2vm-resource": "snapshot"
                    }
                }
            }
        ]
    }
    

To show the inventory of the migration candidate instances grant Migrate to Virtual Machines permissions for **ec2:DescribeInstances, ec2:DescribeVolumes** and **ec2:DescribeInstanceTypes**.

Migrate to Virtual Machines requires the following permissions to migrate EC2 volumes from AWS to Google Cloud:

  1. To create a snapshot of the volumes, grant permissions for **ec2:DescribeSnapshots, ec2:CreateSnapshots** , and **ec2:CreateTags**.
  2. To copy the data to Google Cloud grant permissions for **ebs:ListSnapshotBlocks, ebs:ListChangedBlocks** , and **ebs:GetSnapshotBlock**.
  3. To delete old snapshots grant permissions for **ec2:DeleteSnapshot** and **ec2:DeleteTags**.



To perform a cutover grant Migrate to Virtual Machines permissions for **ec2:StopInstances**.

## Permissions to configure Azure as a source

This section describes the fields of the permissions JSON template. For details on how to implement migration permissions, review the [Create a custom role](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-azure-source#create-a-custom-role) section.

The following permissions are required to create a resource group associated with the source, verify that it exists, list the resources it contains, and delete it when the source is deleted:
    
    
    "Microsoft.Resources/subscriptions/resourceGroups/write",
    "Microsoft.Resources/subscriptions/resourceGroups/read",
    "Microsoft.Resources/subscriptions/resourceGroups/delete"
    

The following permission is required in order to obtain the inventory list and to get the details of the VMs that are being migrated:
    
    
    "Microsoft.Compute/virtualMachines/read"
    

The following permission is required to deallocate a VM when it is being cut over into a Google Cloud VM:
    
    
    "Microsoft.Compute/virtualMachines/deallocate/action"
    

The following permissions are required to create, list, and delete snapshots / restore points of the VM being migrated:
    
    
    "Microsoft.Compute/restorePointCollections/read",
    "Microsoft.Compute/restorePointCollections/write",
    "Microsoft.Compute/restorePointCollections/delete",
    "Microsoft.Compute/restorePointCollections/restorePoints/read",
    "Microsoft.Compute/restorePointCollections/restorePoints/write",
    "Microsoft.Compute/restorePointCollections/restorePoints/delete",
    "Microsoft.Compute/snapshots/delete",
    "Microsoft.Compute/snapshots/write",
    "Microsoft.Compute/snapshots/read"
    

The following permissions are required for reading snapshot / restore point data:
    
    
    "Microsoft.Compute/restorePointCollections/restorePoints/diskRestorePoints/read",
    "Microsoft.Compute/restorePointCollections/restorePoints/diskRestorePoints/beginGetAccess/action",
    "Microsoft.Compute/restorePointCollections/restorePoints/diskRestorePoints/endGetAccess/action",
    "Microsoft.Compute/snapshots/beginGetAccess/action",
    "Microsoft.Compute/snapshots/endGetAccess/action"
    

### Grant network access

In addition to granting permissions, you must verify that access to your disks is not blocked or restricted to any specific network. Your disks must be accessible to public networks.

To ensure that your disks are accessible to public networks, use the following steps:

  1. In your Azure account, go to your disk settings.
  2. In **Settings** , open the **Networking** page.
  3. Select **Enable public access from all networks**.
  4. Click **Save**.



For more information, see [Managing network access for managed disks](https://learn.microsoft.com/en-us/answers/questions/2028479/managing-network-access-for-managed-disks).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
