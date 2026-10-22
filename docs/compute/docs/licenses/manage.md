---
url: https://docs.cloud.google.com/compute/docs/licenses/manage/
title: Manage licenses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:43.407516+00:00
---

# Manage licenses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/licenses/manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage licenses Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document explains how to manage licenses associated with a Compute Engine instance. This includes how to append, remove, replace, and view the history of license updates. For more information about licenses on Compute Engine see [About licenses](https://docs.cloud.google.com/compute/docs/licenses/about).

## Restrictions for changing licenses

Only certain OS licenses are eligible to be appended, removed, or replaced. License changes are supported for Red Hat Enterprise Linux (RHEL), RHEL for SAP, SUSE Linux Enterprise Server (SLES), SLES for SAP, Ubuntu, Ubuntu Pro, Windows Server, and SQL Server.

The allowed license changes are determined by the license owner and are subject to change. To validate the allowed license changes for your VM, see [Review license changes and restrictions](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions).

For changing your RHEL or SLES licenses between pay-as-you-go (PAYG) and bring-your-own-subscription (BYOS), see [Switch between PAYG and BYOS](https://docs.cloud.google.com/compute/docs/licenses/switch-between-payg-and-byos).

For changing your Windows Server licenses from bring-your-own-license (BYOL) to PAYG, see [Switch from Windows BYOL to PAYG](https://docs.cloud.google.com/compute/docs/licenses/switch-windows-byol-to-payg).

For Ubuntu LTS, to upgrade your license to Ubuntu Pro to enable Extended Security Maintenance (ESM), see [Upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro-faq#upgrade-from-ubuntu-to-ubuntu-pro).

To update your on-demand RHEL license to include extended support, see [Append the RHEL Extended lifecycle Support (ELS) Add-On to your license](https://docs.cloud.google.com/compute/docs/images/premium/rhel/append-els-licenses).

## Before you begin

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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Prepare to update a disk's license

**Caution** : Google recommends using reservations to ensure machine availability while the VM is shut down.

To update the disk's license while the disk is attached to a running instance, first either stop the instance or detach the disk.

  * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm). Temporarily shuts down the instance before updating the disk's license.
  * [Detach the disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_disk). This detaches the disk from the instance before updating the disk's license.



## View the licenses associated with a VM

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.get`



To view the licenses associated with a VM, use the Google Cloud console, gcloud CLI, or the Compute Engine API.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM to check the license of. The **Instance details** page opens.

  3. At the bottom of the **Instance details** page, click **Equivalent Code**.

  4. View the `licenses` field for the boot disk.




###  gcloud 

  1. Run the following [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
         
         gcloud compute instances describe VM_NAME
         

Replace `VM_NAME` with the name of your VM.

  2. View the `disks` section of the output. The `licenses` field shows the licenses associated with the boot disk.




###  REST 

Call the [`instances.get` v1 method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instancesVM_NAME

Replace the following:

  * `PROJECT`: the name of the project
  * `ZONE`: the zone containing the VM
  * `VM_NAME`: the name of the VM



The Compute Engine API returns the licenses associated with the boot disk in the `disks` section of the `licenses` field.

## Append a license during an image import

To append a license during the image import process, use the following [`gcloud compute images import` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/import).
    
    
    gcloud compute images import IMAGE_NAME \
      --source-file=SOURCE_FILE
      --os=OS
    

Replace the following:

  * `IMAGE_NAME`: the name of the image to create.
  * `SOURCE_FILE`: a local file or Cloud Storage URI of the virtual disk to import.
  * `OS`: the OS of the disk image to import. The license for the OS is inferred from the value of this flag; there isn't an explicit flag to provide license information when importing. For a list of the supported values, see [`--os` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/import#--os).



For more information about importing images, see [Importing virtual disks](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks).

## Append licenses when creating an image

To append licenses when creating an image, use the following [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create).
    
    
    gcloud compute images create IMAGE_NAME \
      --source-image=SOURCE_IMAGE \
      --licenses=LICENSES
    

Replace the following:

  * `IMAGE_NAME`: the name of the image to create.
  * `SOURCE_IMAGE`: the name of the image to create the new image from.
  * `LICENSES`: a comma-separated list of [license strings](https://docs.cloud.google.com/compute/docs/images/os-details#license-strings). For example, `"license1"`, `"license2"`.



For more information about creating images, see [Creating, deleting, and deprecating custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images), and [Creating a Windows image](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image).

## Append licenses to a disk

To append licenses associated with a VM, use the gcloud CLI or the Compute Engine API.

###  gcloud 

To append licenses to a disk using a license reference or code, use the following [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update).
    
    
    gcloud compute disks update DISK_NAME \
    --append-licenses=LICENSES
    

Replace the following:

  * `DISK_NAME`: the name of the disk to append.
  * `LICENSES`: a comma-separated list of [license references](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions#license-references), for example, `"projects/rhel-cloud/global/licenses/rhel-9-server"`, `"projects/rhel-cloud/global/licenses/rhel-8-server"`.



###  REST 

To append licenses to a disk using a license reference or code, call the following [`disks.update` v1 method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/update):
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/disks/DISK_NAME?paths=licenses --data '{"name":"DISK_NAME", "licenses":["https://www.googleapis.com/compute/v1/LICENSES"]}'
    

Replace the following:

  * `PROJECT`: the name of the project
  * `ZONE`: the zone containing the VM
  * `DISK_NAME`: the name of the disk
  * `LICENSES`: a comma-separated list of [license references](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions#license-references), for example, `"projects/rhel-cloud/global/licenses/rhel-9-server"`, `"projects/rhel-cloud/global/licenses/rhel-8-server"`.



## Replace licenses on a disk

To replace licenses associated with a VM, use the gcloud CLI or the Compute Engine API.

###  gcloud 

To replace a license on a disk using a license reference or code, use the following [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update).
    
    
    gcloud compute disks update DISK_NAME \
    --replace-license=PREVIOUS_LICENSE,NEW_LICENSE
    

Replace the following:

  * `DISK_NAME`: the name of the disk to append.
  * `PREVIOUS_LICENSE`: the previous [license reference](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions#license-references) being replaced, for example, `"projects/rhel-cloud/global/licenses/rhel-9-server"`, `"projects/rhel-cloud/global/licenses/rhel-8-server"`.
  * `NEW_LICENSE`: the new [license reference](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions#license-references), for example, `"projects/rhel-cloud/global/licenses/rhel-9-server"`, `"projects/rhel-cloud/global/licenses/rhel-8-server"`.



###  REST 

To replace a license on a disk using a license reference or code, call the [`disks.update` v1 method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/update) and replace the previous license with the new license in the request body as follows:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/disks/DISK_NAME?paths=licenses --data '{"name":"DISK_NAME", "licenses":["https://www.googleapis.com/compute/v1/NEW_LICENSE"]}'

Replace the following:

  * `PROJECT`: the name of the project
  * `ZONE`: the zone containing the VM
  * `DISK_NAME`: the name of the disk
  * `NEW_LICENSE`: the new [license reference](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions#license-references), for example, `"projects/rhel-cloud/global/licenses/rhel-9-server"`, `"projects/rhel-cloud/global/licenses/rhel-8-server"`.



## Remove licenses from a disk

To remove individual licenses associated with a VM, use the gcloud CLI and Compute Engine API.

###  gcloud 

To remove licenses from a disk using a license reference or code, use the [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update).
    
    
    gcloud compute disks update DISK_NAME \
    --remove-licenses=LICENSES
    

Replace the following:

  * `DISK_NAME`: the name of the disk to remove.
  * `LICENSES`: a comma-separated list of [license references](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions#license-references), for example, `"projects/rhel-cloud/global/licenses/rhel-9-server"`, `"projects/rhel-cloud/global/licenses/rhel-8-server"`.



###  REST 

To remove a license, provide an empty license field in the call request along with the path selector by calling the following [`disks.update` v1 method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/update):
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/disks/DISK_NAME?paths=licenses --data '{"name":"DISK_NAME", "licenses":[]}'
    

Replace the following:

  * `PROJECT`: the name of the project
  * `ZONE`: the zone containing the VM
  * `DISK_NAME`: the name of the disk
  * `LICENSES`: leave blank.



## View the history of license updates

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
         

  4. Replace `PROJECT_NAME` with the name of the project.

  5. Click **Run query**.




## What's next

  * [Troubleshoot licenses](https://docs.cloud.google.com/compute/docs/troubleshooting/import-migrate)

  * [Learn about Microsoft licenses on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing)

  * [Review license changes and restrictions](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions)

  * Learn more about premium operating systems:

    * [Consult the RHEL FAQ](https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq)

    * [Consult the SLES FAQ](https://docs.cloud.google.com/compute/docs/images/premium/sles-faq)

    * [Consult the Ubuntu Pro FAQ](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro-faq)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
