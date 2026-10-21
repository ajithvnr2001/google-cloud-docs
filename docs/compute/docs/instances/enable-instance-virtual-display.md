---
url: https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display/
title: Enable virtual displays on a VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:57.879473+00:00
---

# Enable virtual displays on a VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enable virtual displays on a VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to enable or disable virtual displays on a virtual machine (VM) instance.

If an application running on your VM requires a display device, but you don't need the performance of a GPU, then configure your VM to use virtual display devices. By enabling virtual displays on a VM, you can run virtual display devices on the VM, such as remote system management tools, remote desktop software, and [screen capturing](https://docs.cloud.google.com/compute/docs/instances/capturing-vm-screenshots).

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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to enable or disable virtual displays on a VM, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to enable or disable virtual displays on a VM. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to enable or disable virtual displays on a VM:

  * To enable or disable virtual displays on an existing VM: `compute.instances.updateDisplayDevice` on the VM 
  * To create a VM with virtual displays enabled: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Pricing

There are no costs associated with enabling or disabling virtual displays on a VM.

## Restrictions

For VMs with virtual displays enabled, the following limitations apply:

  * If your VM is running an x64-based Windows OS image earlier than version `v20190312`, then, after enabling virtual displays on your VM, you must install the virtual display driver as described in this document. If your VM is running a later OS image version, then the driver is already installed on the OS image.

  * You can use a virtual display device on the VM only after the guest OS boots and initializes the virtual display driver.

  * You can't use virtual display devices on VMs that run the [Sandy Bridge CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).

  * You can't use virtual display devices on [T2A Arm VMs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines).




## Enable virtual displays on a VM

To enable virtual displays on a VM, select one of the following methods described in this document:

  * Create a VM with virtual displays enabled.

  * Enable virtual displays on an existing VM.




If your VM is running an x64-based Windows OS image earlier than version `v20190312`, then, after you enable virtual displays on the VM, install the virtual display driver as described in this document.

### Create a VM with virtual displays enabled

To create a VM with virtual displays enabled, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify the properties for the VM, including the name, zone, and machine type.

  3. In the **Display device** section, select the **Enable display device** checkbox.

  4. To create the VM, click **Create**.




###  gcloud 

To create a VM with virtual displays enabled, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--enable-display-device` flag.
    
    
    gcloud compute instances create VM_NAME \
        --enable-display-device \
        --machine-type=MACHINE_TYPE \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM.

  * `MACHINE_TYPE`: the machine type to use for the VM.

  * `ZONE`: the zone in which to create the VM.




###  Terraform 

To create a VM with virtual displays enabled, use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) with the `enable_display` argument set to `true`.

For example, to create a VM in zone `us-central1-c` with virtual displays enabled, and specify `f1-micro` as the machine type, use the following resource:
    
    
    resource "google_compute_instance" "instance_virtual_display" {
      name         = "instance-virtual-display"
      machine_type = "f1-micro"
      zone         = "us-central1-c"
    
      # Set the below to true to enable virtual display
      enable_display = true
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
      network_interface {
        # A default network is created for all GCP projects
        network = "default"
        access_config {
        }
      }
    }
    

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create a VM with virtual displays enabled, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `enableDisplay` field set to `true`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "VM_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "project/IMAGE_PROJECT/global/images/IMAGE"
          }
        }
      ],
      "displayDevice": {
        "enableDisplay": true
      },
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the VM.

  * `ZONE`: the zone in which to create the VM.

  * `VM_NAME`: the name of the VM.

  * `MACHINE_TYPE`: the machine type to use for the VM.

  * `IMAGE_PROJECT`: the image project that contains the OS image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




For more information about creating a VM, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Enable virtual displays on an existing VM

Before enabling virtual displays on a VM, make sure to [stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

To enable virtual displays on an existing VM, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM.

The details page of the VM opens.

  3. Click edit **Edit**.

The page to edit the VM's properties opens.

  4. In the **Display device** section, select the **Enable display device** checkbox.

  5. Click **Save**.




###  gcloud 

To enable virtual displays on an existing VM, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update) with the `--enable-display-device` flag.
    
    
    gcloud compute instances update VM_NAME \
        --enable-display-device \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM.

  * `ZONE`: the zone where the VM is located.




###  REST 

To enable virtual displays on an existing VM, make a `POST` request to the [`instances.updateDisplayDevice` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/updateDisplayDevice). In the request body, include the `enableDisplay` field and set it to `true`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/updateDisplayDevice
    
    {
      "enableDisplay": true
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VM is located.

  * `ZONE`: the zone where the VM is located.

  * `VM_NAME`: the name of the VM.




## Disable virtual displays on an existing VM

Before disabling virtual displays on a VM, make sure to [stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

To disable virtual displays on an existing VM, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM.

The details page of the VM opens.

  3. Click edit **Edit**.

The page to edit the VM's properties opens.

  4. In the **Display device** section, clear the **Enable display device** checkbox.

  5. Click **Save**.




###  gcloud 

To disable virtual displays on an existing VM, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update) with the `--no-enable-display-device` flag.
    
    
    gcloud compute instances update VM_NAME \
        --no-enable-display-device \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM.

  * `ZONE`: the zone where the VM is located.




###  REST 

To disable virtual displays on an existing VM, make a `POST` request to the [`instances.updateDisplayDevice` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/updateDisplayDevice). In the request body, include the `enableDisplay` field and set it to `false`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/updateDisplayDevice
    
    {
      "enableDisplay": false
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VM is located.

  * `ZONE`: the zone where the VM is located.

  * `VM_NAME`: the name of the VM.




## Install the virtual display driver

If you've enabled virtual displays on a Windows VM that runs a Windows OS image earlier than version `v20190312`, then, to use a virtual display device on the VM, you must install the virtual display driver provided by Google Cloud. If the VM runs a more recent OS image version, then the driver is already installed and you can skip this section.

To install the virtual display driver on a VM with virtual displays enabled, do the following:

  1. [Connect to the Windows VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Open a PowerShell terminal as an administrator.

  3. Install the `google-compute-engine-driver-gga` component:
         
         googet install google-compute-engine-driver-gga
         

  4. [Restart the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm).




After you restart the VM, you can verify that the driver was correctly installed as described in the next section.

## Verify the virtual display driver installation

If you had to manually install the virtual display driver on a Windows VM as described in the previous section, then you can verify that the installation was successful by doing the following:

  1. If you haven't already, [connect to the Windows VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Open Device Manager.

  3. In the **Device Manager** list, in the **Display adapters** list, make sure that the Google Graphics Array (GGA) driver is listed.

If the driver isn't listed, then reinstall the virtual display driver as described in this document.




## What's next

  * Learn how to [set up Chrome Remote Desktop on Linux VMs](https://docs.cloud.google.com/solutions/chrome-desktop-remote-on-compute-engine).

  * Learn how to [connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
