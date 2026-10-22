---
url: https://docs.cloud.google.com/compute/docs/licenses/switch-between-payg-and-byos/
title: Switch between PAYG and BYOS \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:01.228054+00:00
---

# Switch between PAYG and BYOS  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/licenses/switch-between-payg-and-byos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Switch between PAYG and BYOS Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This page explains how to switch between pay-as-you-go (PAYG) and bring-your-own-subscription (BYOS) billing models for the following Linux operating systems:

  * Red Hat Enterprise Linux (RHEL)
  * RHEL for SAP
  * SUSE Linux Enterprise Server (SLES)
  * SLES for SAP



For switching Windows Server from bring-your-own-license (BYOL) to PAYG, see [Switch Windows Server from BYOL to PAYG](https://docs.cloud.google.com/compute/docs/licenses/switch-windows-byol-to-payg). For details on license codes and how to determine allowed license modifications, see [License changes and restrictions](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions). 

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




## Prepare to update a disk's license

**Caution** : Google recommends using reservations to ensure machine availability while the VM is shut down.

To update the disk's license while the disk is attached to a running instance, first either stop the instance or detach the disk.

  * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm). Temporarily shuts down the instance before updating the disk's license.
  * [Detach the disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_disk). This detaches the disk from the instance before updating the disk's license.



## Change a BYOS license to a PAYG license

To replace a BYOS license with a PAYG license, use the Google Cloud CLI or the Compute Engine API.

###  gcloud 

To replace a disk's license with a license reference or code, use the [`gcloud compute disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update):
    
    
    gcloud compute disks update DISK_NAME \
        --replace-license=PREVIOUS_LICENSE,NEW_LICENSE
    

Replace the following:

  * `DISK_NAME`: the name of the disk to replace.
  * `PREVIOUS_LICENSE`: the previous [license reference](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions#license-references) being replaced, for example, `"projects/rhel-cloud/global/licenses/rhel-7-byos"`, `"projects/rhel-cloud/global/licenses/rhel-8-byos"`.
  * `NEW_LICENSE`: the new [license reference](https://docs.cloud.google.com/compute/docs/licenses/license-changes-and-restrictions#license-references), for example, `"projects/rhel-cloud/global/licenses/rhel-7-server"`, `"projects/rhel-cloud/global/licenses/rhel-8-server"`.



###  REST 

To replace a disk's license, add the new license to the request body and omit the previous license. Call the following [`disks.update` v1 method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/update):
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/disks/DISK_NAME?paths=licenses --data '{"name":"DISK_NAME", "licenses":["https://www.googleapis.com/compute/v1/NEW_LICENSE"]}'
    

Replace the following:

  * `PROJECT`: the name of the project
  * `ZONE`: the zone containing the VM
  * `DISK_NAME`: the name of the disk
  * `NEW_LICENSE`: the new license reference, for example, `"projects/rhel-cloud/global/licenses/rhel-6-byos"`, `"projects/rhel-cloud/global/licenses/rhel-7-byos"`, or license code, for example, `"4720191914037931587"`, `"1492188837615955530"`.



## Validate the license change

To validate that your license has been changed on the boot disk, use the following procedure:

  1. Get information about the boot disk by running the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe):
         
         gcloud compute disks describe DISK_NAME \
             --zone=ZONE \
             --format="value(licenses)"
         

Replace the following:

     * `DISK_NAME`: the name of the boot disk to validate the license of
     * `ZONE`: the zone containing the boot disk to validate the license of
  2. Verify that the output is similar to the following:
         
         https://www.googleapis.com/compute/v1/projects/rhel-cloud/global/licenses/rhel-10-server
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
