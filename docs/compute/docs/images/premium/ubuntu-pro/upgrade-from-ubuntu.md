---
url: https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu/
title: Upgrade from Ubuntu to Ubuntu Pro \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:29:14.666562+00:00
---

# Upgrade from Ubuntu to Ubuntu Pro  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Upgrade from Ubuntu to Ubuntu Pro Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

When an Ubuntu LTS image reaches its [end of life](https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol), it is no longer supported and won't receive security updates. If you upgrade to [Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_pro), you continue to receive security updates during [Extended Security Maintenance (ESM)](https://ubuntu.com/security/esm).

This document shows you how to upgrade from Ubuntu to Ubuntu Pro by doing the following for each VM:

  1. Install updates and dependencies.
  2. Replace the Ubuntu license with the Ubuntu Pro license.
  3. Validate the license.



## Supported upgrade paths

The following table shows the supported upgrade paths:

Initial version | Final version  
---|---  
Ubuntu 16.04 LTS | Ubuntu Pro 16.04 LTS  
Ubuntu 18.04 LTS | Ubuntu Pro 18.04 LTS  
Ubuntu 20.04 LTS | Ubuntu Pro 20.04 LTS  
Ubuntu 22.04 LTS | Ubuntu Pro 22.04 LTS  
Ubuntu 24.04 LTS | Ubuntu Pro 24.04 LTS  
  
## Limitations

  * You must stop a VM before replacing a license.

  * You can only upgrade from Ubuntu LTS to Ubuntu Pro LTS if they are the same version. For example, you can upgrade from Ubuntu 16.04 LTS to Ubuntu Pro 16.04 LTS, but cannot upgrade from Ubuntu 16.04 LTS to Ubuntu Pro 20.04 LTS.




## Billing

You are billed for Ubuntu Pro LTS according to the [pricing for premium images](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages).

For more information about billing, see [Cloud Billing](https://docs.cloud.google.com/billing/docs).

## Before you begin

  * Run the following commands on each VM, replacing `VM_NAME` with the name of the VM to upgrade: 

    1. Update the package index by using the following command: 
           
           gcloud compute ssh VM_NAME --command "sudo apt update"

    2. Install the newest version of the packages by using the following command: 
           
           gcloud compute ssh VM_NAME --command "sudo apt -f upgrade"

    3. Install Ubuntu Pro by using the following command: 
           
           gcloud compute ssh VM_NAME --command "sudo apt -f install ubuntu-advantage-pro"

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




## Replace the license

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.disks.update` on the boot disk



Replace the Ubuntu license with the Ubuntu Pro license by using the following procedure:

**Caution:** Google recommends using [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to ensure machine availability while the VM is shut down.

  1. Stop the VM by using the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop):
         
         gcloud compute instances stop VM_NAME \
            --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM to stop
     * `ZONE`: the zone containing the VM to stop
  2. Get the list of disks associated with the VM by using the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
         
         gcloud compute instances describe VM_NAME \
            --zone=ZONE \
            --format="yaml(disks)"
         

Replace the following:

     * `VM_NAME`: the name of the VM to get the list of associated disks from

     * `ZONE`: the zone containing the VM to get the list of associated disks from

  3. Verify that the output is similar to:
         
         disks:
         - autoDelete: true
           boot: true
           deviceName: ubuntu
           diskSizeGb: '10'
           guestOsFeatures:
           - type: VIRTIO_SCSI_MULTIQUEUE
           - type: SEV_CAPABLE
           - type: UEFI_COMPATIBLE
           - type: GVNIC
           index: 0
           interface: SCSI
           kind: compute#attachedDisk
           licenses:
           - https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-1604-xenial
           mode: READ_WRITE
           shieldedInstanceInitialState:
             dbxs:
             - content: ...
               fileType: BIN
           source: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/disks/VM_NAME
           type: PERSISTENT
         

Note that no `Licenses` have been replaced.

  4. Get the name of the boot disk by running the [`gcloud compute disks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list):
         
         gcloud compute disks list
         

  5. Update the boot disk with the Ubuntu Pro license URI by using the [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update):
         
         gcloud compute disks update DISK_NAME \
            --zone=ZONE \
            --replace-license="PREVIOUS_LICENSE,NEW_LICENSE"
         

Replace the following:

     * `DISK_NAME`: the name of the boot disk to replace the license to.

     * `ZONE`: the zone containing the boot disk to replace the license to.

     * `PREVIOUS_LICENSE`: the license URI for the Ubuntu version

     * `NEW_LICENSE`: the new Ubuntu Pro license URI.

The following table shows the license URI for the supported versions of Ubuntu Pro:


Ubuntu Pro version | License URI  
---|---  
Ubuntu Pro 16.04 LTS | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1604-lts`  
Ubuntu Pro 18.04 LTS | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1804-lts`  
Ubuntu Pro 20.04 LTS | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2004-lts`  
Ubuntu Pro 22.04 LTS | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2204-lts`  
Ubuntu Pro 24.04 LTS | `https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2404-lts`  
  
## Validate the license

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.disks.get` on the boot disk



Validate the Ubuntu Pro license by using the following procedure:

  1. Get information about the boot disk by running the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe):
         
         gcloud compute disks describe DISK_NAME \
            --zone=ZONE
         

Replace the following:

     * `DISK_NAME`: the name of the boot disk to validate the license of

     * `ZONE`: the zone containing the boot disk to validate the license of

  2. Verify output similar to:
         
         creationTimestamp: '2021-10-20T17:20:26.616-07:00'
         guestOsFeatures:
         - type: VIRTIO_SCSI_MULTIQUEUE
         - type: SEV_CAPABLE
         - type: UEFI_COMPATIBLE
         - type: GVNIC
         id: '7008232787326864549'
         kind: compute#disk
         labelFingerprint: 42WmSpB8rSM=
         lastAttachTimestamp: '2021-10-20T17:20:26.617-07:00'
         licenseCodes:
         - '8045211386737108299'
         licenses:
         - https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1604-lts
         name: ubuntu
         physicalBlockSizeBytes: '4096'
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/disks/DISK_NAME
         sizeGb: '10'
         sourceImage: https://www.googleapis.com/compute/v1/projects/IMAGE_PROJECT/global/images/IMAGE
         sourceImageId: '1233998915439563944'
         status: READY
         type: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/diskTypes/DISK_TYPE
         users:
         - https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/instances/VM_NAME
         zone: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE
         

  3. Validate that the Ubuntu Pro license is added to the boot disk by checking the output of the previous step for the `licenses` field for the appropriate license string.

If the `licenses` field doesn't contain the intended license string, you might need to clear and update the licenses. For more information, see the [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update).

  4. Start the VM by using the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
         
         gcloud compute instances start VM_NAME \
            --zone=ZONE \
            [--csek-key-file ENCRYPTION_KEY]
         

Replace the following:

     * `VM_NAME`: the name of the VM to start

     * `ZONE`: the zone containing the VM to start

     * `ENCRYPTION_KEY`: Optional: if the boot disk is encrypted with a customer-supplied encryption key (CSEK) ([deprecated](https://docs.cloud.google.com/compute/docs/deprecations)), specifies the path to the key file

  5. After the VM boots, run the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) to verify that the Ubuntu ESM is entitled and enabled:
         
         gcloud compute ssh VM_NAME --command "sudo ua status --wait" \
            --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM to verify

     * `ZONE`: the zone containing the VM to verify

  6. Check that the Ubuntu ESM is entitled and enabled by verifying that the output is similar to:
         
         SERVICE       ENTITLED  STATUS    DESCRIPTION
         cis           yes       disabled  Center for Internet Security Audit Tools
         esm-apps      yes       enabled   UA Apps: Extended Security Maintenance (ESM)
         esm-infra     yes       enabled   UA Infra: Extended Security Maintenance (ESM)
         fips          yes       n/a       NIST-certified core packages
         fips-updates  yes       n/a       NIST-certified core packages with priority security updates
         livepatch     yes       n/a       Canonical Livepatch service
         




## View activity logs

View the history of license updates for VMs in a project by using the following procedure:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the toolbar, verify that **Show query** is enabled.

  3. Copy the following expression into the query editor:
         
         resource.type="gce_disk"
         logName="projects/PROJECT_NAME/logs/cloudaudit.googleapis.com%2Factivity"
         severity>=NOTICE
         protoPayload.request.@type="type.googleapis.com/compute.disks.update"
         protoPayload.request.licenses:*
         

  4. Replace `PROJECT_NAME` with the name of your project.

  5. Click **Run query**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
