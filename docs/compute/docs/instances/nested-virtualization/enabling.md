---
url: https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/enabling/
title: Enable nested virtualization \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:12.111591+00:00
---

# Enable nested virtualization  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/enabling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enable nested virtualization Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to enable nested virtualization on a virtual machine (VM) instance and how to confirm that you can create a nested VM. Enable nested virtualization on a VM by using one of the following methods:

  * **Recommended**. Enable nested virtualization directly on a new or existing VM by setting the `enableNestedVirtualization` field to `true` while creating the VM or by updating the VM. This is the recommended method because it doesn't require that you create a custom image or use the special license key.

  * Enable nested virtualization by using the special license key by creating a boot disk, creating a custom image with the special nested virtualization license key, and then creating a VM that uses the custom image.




## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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




## Enable nested virtualization directly on a new VM

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For enabling nested virtualization directly on a new VM, you need the `compute.instances.create` permissions on the project, folder, or organization. 



Enable nested virtualization directly on a VM by using the following procedure.

###  gcloud 

Create an L1 VM with nested virtualization enabled by using the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):
    
    
    gcloud compute instances create VM_NAME \
      --enable-nested-virtualization \
      --zone=ZONE \
    

Replace the following:

  * `VM_NAME`: the name of the new L1 VM with nested virtualization enabled

  * `ZONE`: the zone for the new L1 VM with nested virtualization enabled




###  REST 

Create an L1 VM with nested virtualization enabled by using the following [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      ...
      "name": "VM_NAME",
      ...
      "advancedMachineFeatures": {
        "enableNestedVirtualization": true
      },
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID

  * `ZONE`: the zone for the new L1 VM with nested virtualization enabled

  * `VM_NAME`: the name of the new L1 VM with nested virtualization enabled




## Enable nested virtualization directly on an existing VM

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For enabling nested virtualization directly on a new VM, you need the `compute.instances.create` permissions on the project, folder, or organization. 



Enable nested virtualization on an existing VM by using the following procedure.

###  gcloud 

  1. Export the properties of the VM by using the following [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export):
         
         gcloud compute instances export VM_NAME \
           --destination=YAML_FILE_PATH \
           --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM from which to export properties

     * `YAML_FILE_PATH`: the path and file name of a .yaml file in which to save the exported configuration data

     * `ZONE`: the zone that contains the VM

  2. In the VM configuration file that was saved in FILE_PATH, update the value for `enableNestedVirtualization`. If the value is not in the file, add the following:
         
         advancedMachineFeatures:
           enableNestedVirtualization: true
         

**Tip:** To avoid getting an error such as `"ERROR: (gcloud.compute.instances.update-from-file) Cannot parse YAML: [Expected type  for field value, found True (type )]"`, add quotes (`' '`) around any label values of `yes` or `no` in the exported instance configuration file. This indicates the values are strings, not Boolean values.
  3. Update the VM with the value for `enableNestedVirtualization` by using the following [`gcloud compute instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file):
         
         gcloud compute instances update-from-file VM_NAME \
           --source=FILE_PATH \
           --most-disruptive-allowed-action=RESTART \
           --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM to update

     * `FILE_PATH`: the path to the updated VM configuration file

     * `ZONE`: the zone that contains the VM to update




###  REST 

Update the value for `enableNestedVirtualization` by using the following [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update):
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME?most_disruptive_allowed_action=RESTART
    
    {
      ⋮
      "advanced_machine_features": {
        ⋮
        "enableNestedVirtualization": "true"
      },
      ⋮
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project

  * `ZONE`: the zone that contains the VM

  * `VM_NAME`: the name of the VM from which to export properties




## Enable nested virtualization by using the special license key

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.disks.create` on the project, folder, or organization
  * `compute.images.create` on the project, folder, or organization
  * `compute.disks.delete` on the project, folder, or organization
  * `compute.instances.create` on the project, folder, or organization



You can enable nested virtualization on VM by creating a custom image with a special license key that enables VMX on the L1 VM. The license key does not incur additional charges.

  1. Create a boot disk from a public image or from a custom image. The following example uses `debian-cloud` for the image project and `debian-10` for the image family. If you already have a VM instance with an existing disk, you can skip this step.

###  gcloud 
         
         gcloud compute disks create DISK_NAME \
           --zone=ZONE \
           --image-project=debian-cloud \
           --image-family=debian-10
         

Replace the following:

     * `DISK_NAME`: the name of the new disk

     * `ZONE`: the zone to create the disk in

###  REST 
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
    
    {
      ...
      "name": "DISK_NAME",
      "sourceImage": "projects/debian-cloud/global/images/family/debian-10",
      ...
    }
    

Replace the following:

     * `PROJECT_ID`: the project ID

     * `ZONE`: the zone to create the disk in

     * `DISK_NAME`: the name of the new disk

  2. Create a custom image with the special license key that is required for nested virtualization.

###  gcloud 
         
         gcloud compute images create IMAGE_NAME \
           --source-disk DISK_NAME \
           --source-disk-zone ZONE \
           --licenses "https://www.googleapis.com/compute/v1/projects/vm-options/global/licenses/enable-vmx"
         

Replace the following:

     * `IMAGE_NAME`: the name of the new image

     * `DISK_NAME`: the name of the previously created disk

     * `ZONE`: the zone to create the image in

###  REST 
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
    
    {
      ...
      "licenses": ["projects/vm-options/global/licenses/enable-vmx"],
      "name": "IMAGE_NAME",
      "sourceDisk": "zones/ZONE/disks/DISK_NAME",
      ...
    }
    

Replace the following:

     * `PROJECT_ID`: the project ID

     * `IMAGE_NAME`: the name of the new image

     * `ZONE`: the zone to create the image in

     * `DISK_NAME`: the name of the previously created disk

  3. Optionally delete the source disk after creating the image with the special license.

###  gcloud 
         
         gcloud compute disks delete DISK_NAME --zone=ZONE
         

Replace the following:

     * `DISK_NAME`: the name of the disk to delete

     * `ZONE`: the zone containing the disk to delete

###  REST 
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
    

Replace the following:

     * `PROJECT_ID`: the project ID

     * `ZONE`: the zone containing the disk to delete

     * `DISK_NAME`: the name of the disk to delete

  4. Create a VM that uses the new image with the special license. The minimum CPU platform for Intel VMs must be `"Intel Haswell"`.

###  gcloud 
         
         gcloud compute instances create VM_NAME \
             --zone=ZONE \
             --image IMAGE_NAME
         

Replace the following:

     * `VM_NAME`: the name of the VM

     * `ZONE`: the zone to create the VM in

     * `IMAGE_NAME`: the name of the previously created image

###  REST 
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      ...
      "name": "VM_NAME",
      "disks": [
        {
          "initializeParams": {
            "sourceImage": "IMAGE_NAME"
          }
        }
      ]
      ...
    }
    
    

Replace the following:

     * `PROJECT_ID`: the project ID

     * `VM_NAME`: the name of the VM

     * `ZONE`: the zone to create the VM in

     * `IMAGE_NAME`: the name of the previously created image




## Confirm that nested virtualization is enabled on the VM

  1. Connect to the VM instance.
         
         gcloud compute ssh VM_NAME
         

Replace `VM_NAME` with the name of the VM to connect to.

  2. Confirm that nested virtualization is enabled. Any response other than `0` confirms that nested virtualization is enabled.
         
         grep -cw vmx /proc/cpuinfo
         




## What's next

  * [Create nested VMs](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/creating-nested-vms)
  * [Troubleshoot nested virtualization](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-nested-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
