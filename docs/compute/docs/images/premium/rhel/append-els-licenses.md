---
url: https://docs.cloud.google.com/compute/docs/images/premium/rhel/append-els-licenses/
title: Append RHEL ELS licenses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:29:36.951618+00:00
---

# Append RHEL ELS licenses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/premium/rhel/append-els-licenses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Append RHEL ELS licenses Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document shows you how to append the ELS Add-On to RHEL compute instances that have on-demand licenses for their images and have reached end of maintenance.

When a Red Hat Enterprise Linux (RHEL) version [reaches end of maintenance](https://docs.cloud.google.com/compute/docs/eol/rhel-eol) and your OS image uses an on-demand license, support and access to these Compute Engine instances are limited according to the [Maintenance policy for lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages).

For extended support, which provides critical impact security fixes and selected urgent priority bug fixes, you can append the RHEL Extended Life Cycle Support (ELS) Add-On. The ELS Add-On applies to the last minor release of a major release as follows:

  * For RHEL 7, the ELS Add-On applies to the latest minor release which is RHEL 7.9 or RHEL 7.9 for SAP. The ELS Add-On for RHEL 7 is available until June 30, 2028.
  * For RHEL 6, the ELS Add-On applies to the latest minor release which is RHEL 6.10. The ELS Add-On for RHEL 6 is available until June 30, 2024. The ELS Add-On is appended automatically to the RHEL 6.10 instances when you migrate them to Google Cloud.



For more information, see the [RHEL Life Cycle](https://access.redhat.com/support/policy/updates/errata) and the [FAQ](https://access.redhat.com/articles/4665701).

## Overview

You append the ELS license by doing the following for each compute instance:

  1. Stop the instance and append the license to the boot disk.

**Caution:** Google recommends using [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to ensure machine availability while the compute instance is shut down.
  2. Validate the license and start the instance.

  3. Install the Red Hat Update Infrastructure (RHUI) ELS client package on the instance.




## Before you begin

  * The ELS Add-On only applies to the latest minor release. For each RHEL instance, update to the latest minor release by [connecting to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) and running the following command: 
        
        sudo yum -y update

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).




### Required roles

To get the permissions that you need to append the ELS license to your instance, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to an instance that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to append the ELS license to your instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to append the ELS license to your instance:

  * To start and stop the instance: 
    * `compute.instances.stop` on the project
    * `compute.instances.start` on the project
  * To view the disks attached to the instance: 
    * `compute.instances.get` on the instance
    * `compute.disks.get` on the instance
    * `compute.disks.list` on the instance
  * To update the boot disk of the instance: 
    * `compute.disks.get` on the boot disk
    * `compute.disks.update` on the boot disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Billing

After you attach RHEL ELS to a disk, Compute Engine adds an additional SKU to your bill.

For example if you are using RHEL 7, [your bill](https://console.cloud.google.com/billing/reports) includes one line item for RHEL 7 and another for RHEL 7 ELS.

You are billed for RHEL instances according to the [pricing for premium images](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages).

## Limitations

You must stop the instance before appending a license.

## Append the RHEL ELS license

Append the RHEL ELS license to the Linux VM's boot disk by using the following procedure:

**Caution:** Google recommends using [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to ensure machine availability while the VM is shut down.

  1. Stop the VM by using the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop):
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the name of the VM to stop.

  2. List the disks associated with the VM by using the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
         
         gcloud compute instances describe VM_NAME --format="yaml(disks)"
         

Replace `VM_NAME` with the name of the VM.

  3. Verify that the output is similar to the following:
         
         disks:
         - autoDelete: true
           boot: true
           deviceName: persistent-disk-0
           diskSizeGb: '20'
           index: 0
           interface: SCSI
           kind: compute#attachedDisk
           licenses:
           - https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/RHEL_VERSION
           - https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/RHEL_ELS_VERSION
           mode: READ_WRITE
           source: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/disks/VM_NAME
           type: PERSISTENT
         

Note that no `Licenses` have been appended yet.

  4. Get the name of the boot disk by running the [`gcloud compute disks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list):
         
         gcloud compute disks list
         

  5. Update the boot disk with the RHEL ELS license URI by using the [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update):
         
         gcloud compute disks update BOOT_DISK_NAME \
            --zone ZONE \
            --append-licenses="https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/RHEL_ELS_VERSION"
         

Replace the following:

     * `RHEL_VERSION`: the RHEL version. For example, `rhel-7-server`.

     * `BOOT_DISK_NAME`: the name of the boot disk obtained in the previous step

     * `ZONE`: the zone containing the boot disk

     * `RHEL_ELS_VERSION`: the RHEL ELS version. For example, `rhel-7-els`.




## Validate the RHEL ELS license

Check that the RHEL ELS license is appended to the Linux VM boot disk by using the following procedure:

  1. Get information about the boot disk by using the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe):
         
         gcloud compute disks describe BOOT_DISK_NAME \
            --zone ZONE
         

Replace the following:

     * `BOOT_DISK_NAME`: the name of the boot disk to check for the appended license

     * `ZONE`: the zone containing the boot disk

  2. Verify that the output is similar to the following:
         
         creationTimestamp: '2021-05-05T15:26:27.835-07:00'
         id: '727854272460268924'
         interface: SCSI
         kind: compute#disk
         labelFingerprint: 42WmSpB8rSM=
         lastAttachTimestamp: '2021-05-05T15:26:27.836-07:00'
         licenseCodes:
         - '1000006'
         - '6213885950785916969'
         licenses:
         - https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/RHEL_VERSION
         - https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/RHEL_ELS_VERSION
         multiWriter: false
         name: VM_NAME
         physicalBlockSizeBytes: '4096'
         selfLink: https://www.googleapis.com/compute/projects/PROJECT_NAME/zones/ZONE/disks/DISK_NAME
         selfLinkWithId: https://www.googleapis.com/compute/projects/PROJECT_NAME/zones/ZONE/disks/DISK_ID
         sizeGb: '20'
         sourceImage: https://www.googleapis.com/compute/projects/IMAGE_PROJECT/global/images/IMAGE
         sourceImageId: '7397991294075835597'
         status: READY
         type: https://www.googleapis.com/compute/projects/PROJECT_NAME/zones/ZONE/diskTypes/DISK_TYPE
         users:
         - https://www.googleapis.com/compute/projects/PROJECT_NAME/zones/ZONE/instances/VM_NAME
         zone: https://www.googleapis.com/compute/projects/PROJECT_NAME/zones/ZONE
         

  3. Validate that the RHEL ELS license is appended to the Linux VM boot disk by checking the output of the previous step for the `Licenses` field for the appropriate license string.

If the `Licenses` field doesn't contain the intended licensing string, you might need to clear and then update the user licenses. For more information, see the [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update).

  4. Start the VM by using the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
         
         gcloud compute instances start VM_NAME \
            [--csek-key-file ENCRYPTION_KEY]
         

Replace the following:

     * `VM_NAME`: the name of the VM to start

     * `ENCRYPTION_KEY`: Optional: if the boot disk is encrypted with a customer-supplied encryption key (CSEK) ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)), specifies the path to the key file




## Install the RHUI ELS client package

After appending the license string to the RHEL disk, install the RHUI ELS client package on the VM by [connecting to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) and running the following commands:

###  RHEL 7 

  1. Check that you are using RHEL 7.9 or RHEL 7.9 for SAP:
         
         cat /etc/redhat-release
          

  2. Download and install the latest update:
         
         sudo yum -y update
          

  3. Remove the RHUI client packages and install the RHUI ELS client package:
         
         sudo yum -y remove google-rhui-client-rhel7 google-rhui-client-rhel79-sap google-rhui-client-rhel7-sap
          sudo yum makecache
          sudo yum -y install google-rhui-client-rhel7-els
          




###  RHEL 6 

  1. Check that you are using RHEL 6.10:
         
         cat /etc/redhat-release
          

  2. Download and install the latest update:
         
         sudo yum -y update
          

  3. Remove the RHUI client package and install the RHUI ELS client package:
         
         sudo yum -y remove google-rhui-client-rhel6
          sudo yum makecache
          sudo yum -y install google-rhui-client-rhel6-els
          




## View audit logs

View the history of license updates for compute instances by using the following procedure:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the toolbar, ensure that **Show query** is enabled.

  3. Copy the following expression into the query editor:
         
         resource.type="gce_disk"
          logName="projects/PROJECT_NAME/logs/cloudaudit.googleapis.com%2Factivity"
          severity>=NOTICE
          protoPayload.request.@type="type.googleapis.com/compute.disks.update"
          protoPayload.request.licenses:*
         

  4. Replace PROJECT_NAME with the name of your project.

  5. Click **Run query**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
