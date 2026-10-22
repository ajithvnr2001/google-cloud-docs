---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-aws-source/
title: Create an AWS source \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:25.139580+00:00
---

# Create an AWS source  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-aws-source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Create an AWS source Stay organized with collections  Save and categorize content based on your preferences. 

## Introduction

[Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines) lets you migrate your EC2 instances from your AWS account to Google Compute Engine instances.

## Prerequisites

  * Review [Migrating VMs with Migrate to Virtual Machines: Getting started](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started) documentation. This document provides insight into the overall structure of Migrate to Virtual Machines, including important terms, concepts, and reference information that help you migrate your workload efficiently and effectively.
  * Enable the **VM Migration API** on your host project using <https://console.cloud.google.com/apis/library/vmmigration.googleapis.com>.
  * Review the [operating systems that support migrating VMs from AWS as a source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions#supported_operating_systems_aws_as_a_source) to Google Cloud.



## Migrate your workload from an AWS source

Before initiating your migration with AWS as a source, set up your AWS environment by completing the following tasks:

  1. Create an AWS IAM policy.
  2. Create an IAM user to be accessed by the Migrate to Virtual Machines service.
  3. Recommended but optional: Tag EC2 instances intended for migration.
  4. Create a source using Google Cloud.



### Create an AWS IAM policy

Before creating an IAM user, create a policy that describes the permissions for your intended workload. To create a policy, see the AWS IAM documentation for [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html).

Use the provided JSON template to provide migration permissions for your policy:
    
    
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
    

If your EC2 instances use encrypted volumes with non-AWS managed keys, you must add the following statement to the preceding policy to grant the created user permission to access the encryption key.
    
    
    {
        "Effect": "Allow",
        "Action": [
            "kms:Decrypt",
            "kms:DescribeKey"
        ],
        "Resource": "<<KMS key ARN>>"
    }
    

For more information about the permissions breakdown for the JSON template fields, see [permissions breakdown](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/roles-reference#permissions_to_configure_aws_as_a_source).

### Create an IAM user

To migrate your AWS workload, create an IAM user for use by Migrate to Virtual Machines. The IAM user enables Migrate to Virtual Machines to interact with your account using the AWS public API.

To configure IAM user permissions to use AWS as source for your migration, [create an API user in the AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

**Note:** Alternatively, you can configure an AWS source with temporary credentials using an AWS Security Token Service (STS) token. For more information, see [AwsSourceDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources#awssourcedetails).

During user creation, make sure you do the following:

  1. Create a user with **Programmatic access**.
  2. Attach the IAM policy you created in the previous section to your new user.
  3. Store the **Access key ID** and **Secret access key** generated during this step. You need them when creating your source using Migrate to Virtual Machines.



### Recommended but optional: Tag the EC2 instances that you want to migrate

Recommended: Tag the instances that you want to migrate. The tags `wantToMigrate` and `true` provided in the image are examples.

![M2VM EC2 instance tags example](https://docs.cloud.google.com/static/migrate/virtual-machines/docs/5.0/images/m2vm-aws-tags.png)

For more information about tagging EC2 instances, see the [AWS IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags_users.html#id_tags_users_procs-console).

### Create an AWS source

After you have created an IAM user and have added that user to your new IAM policy for Migrate to Virtual Machines, you must create an AWS source before you can begin your migration process.

To create an AWS source:

  1. In the Google Cloud console, go to the [Migrate to Virtual Machines](https://console.cloud.google.com/compute/mfce/dashboard) page.
  2. Select the **SOURCES** tab.
  3. Open the **ADD SOURCE** drop-down and select **＋Add AWS Source**.
  4. Enter your source details on the **Create AWS source** panel.

**Caution:** You cannot edit the **GCP region** or **AWS region** fields after creating your source. **Access key ID** and **Secret access key** fields can be edited post-creation if necessary. Editing credentials post-creation may interrupt an ongoing replication cycle. We recommended you wait 24 hours before revoking your previous credentials.

The following table describes the parameters for AWS source details.

**Detail** |  **Description**  
---|---  
**Name (mandatory)** |  A string that identifies the source. The string must conform to [Compute Engine naming conventions](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). You cannot update this field after creating your source.  
**GCP region (mandatory)** |  The region in Google Cloud that you want to migrate your instances to. You cannot update this field after creating your source.  
  
For more information, see [locations](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/locations) documentation.  
**AWS region (mandatory)** |  The region in AWS (e.g. **eu-west-1**) from which you want to migrate EC2 instances. The inventory displayed in the Migrate to Virtual Machines console only includes EC2 instances from this AWS region. You cannot update this field after creating your source.  
  
Note: We recommend that you copy the region from your AWS console and paste it into the source detail field to avoid typos. A typo results in the _source failing to become active_ and is indicated in the console. If this happens, you must create a new source.  
**Access Key ID (mandatory)** |  Part of the IAM user credentials.  
**Secret access key (mandatory)** |  Part of the IAM user credentials.  
**Customer managed encryption key** | The key you want to use to protect your data in Google Cloud. By default, Google Cloud automatically [ encrypts data when it is at rest](https://docs.cloud.google.com/security/encryption-at-rest/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use [ customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) to encrypt and decrypt your data at rest. These encryption keys are created, managed, and owned by you.   
  
**Note:** The encryption key that you set will be used for all the resources created under this source.   
**Optional: Filter inventory by security groups** |  Filter visible EC2 instances in the Migrate to Virtual Machines inventory.  
  
You can specify several group names, in which case Migrate to Virtual Machines displays instances that belong to any of those security groups.  
**Recommended but optional: Filter inventory by VM tags** |  Specify the tags you want to filter your inventory by. We _highly recommend_ that you specify tags, as this lets you _mark a subset_ of your EC2 instances you intend to migrate.   
You can add the tags to the instances after you create the source, but you cannot change the tags the source filters by. If you specify several VM tags, Migrate to Virtual Machines only displays instances that have all of these tags.   
If you specify several VM tags, Migrate to Virtual Machines only displays instances that have all of these tags.  
**Optional: User tags for migration resource** |  Migrate to Virtual Machines creates snapshots of your EC2 volumes to migrate them to Google Cloud.   
  
If you would like to have a custom tag associated with these resources, specify them here. This can help you identify all resources created by Migrate to Virtual Machines in your AWS environment. Snapshots already have tags as detailed in [Snapshots](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#snapshots_created_when_migrating_from_aws).  
  5. Press the **CREATE** button. A notice detailing your new source appears.

  6. Wait (up to 15 minutes but usually less) until the **Source status** is indicated as **Active**.




Check your inventory to verify that there are instances that correspond to the tags (and/or security groups) that you specified when you created your source.

As part of source creation, your project is automatically added as a target project.

#### Cloud sources limitations

You can host a maximum of 15 cloud sources (AWS sources, Azure sources, or both the sources combined) on a host project at a time. For example, you can host 10 AWS sources and 5 Azure sources on a host project at a time. Conversely, you can host 7 AWS sources and 8 Azure sources on a host project at a time. If you want to add a new cloud source to a project that already hosts 15 cloud sources, you must delete an existing source, and then add the new source. You can also try using a different project to host the new cloud source if you don't want to delete any existing sources.

### Next steps: Start your migration

After you've created an AWS source, you are ready to start your migration. The rest of the process for migrating your workload from an AWS source matches the process for other sources for Migrate to Virtual Machines.

For details on how to start your migration process, see **[Migrating individual VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms)**.

## Differences from using Azure as a source

The usage is almost identical to the usage of Azure as a source.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
