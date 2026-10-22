---
url: https://docs.cloud.google.com/compute/docs/instances/create-vm-from-shared-image/
title: Create an instance from a shared image \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:48.481768+00:00
---

# Create an instance from a shared image  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-vm-from-shared-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an instance from a shared image Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a Compute Engine instance from a [custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) that is shared by another project. An instance contains a bootloader, a boot file system, and an OS image. You can create custom images from source disks, images, snapshots, or images stored in Cloud Storage and use these images to create instances. By default, a custom image belongs only to the project in which it was created. If another user has [shared an image with you](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images), then you can use the image to create an instance. 

## Before you begin

  * When creating instances from images by using the Google Cloud CLI or the Compute Engine API, there's a limit of 20 instances per second. If you need to create a higher number of instances per second, [ request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase) for the **Images** resource.
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




### Required roles

To get the permissions that you need to create an instance from a shared image, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create an instance from a shared image. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create an instance from a shared image:

  * `compute.instances.create` on the project
  * To use a shared image to create the instance: `compute.images.useReadOnly` on the image 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an instance from a shared image

To create an instance from a shared image, follow these steps:

###  Console 

  1. In the **Google Cloud console** , go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**.

The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     2. Optional: In the **Zone** field, select a zone for this instance.

The default selection is **Any**. If you don't change this default selection, then Google automatically chooses a zone for you based on machine type and availability.

     3. Select the machine family for your instance. The **Google Cloud console** then displays the machine series that are available for your selected machine family. The following machine family options are available:

        * **General purpose**
        * **Compute optimized**
        * **Memory optimized**
        * **Storage optimized**
        * **Network optimized**
        * **GPUs**
        * **TPUs**
     4. In the **Series** column, select the machine series for your instance.

If you selected **GPUs** as the machine family in the previous step, then select the **GPU type** that you want. The machine series is then automatically selected for the selected GPU type.

     5. In the **Machine type** section, select the machine type for your instance.

  3. In the navigation menu, click **OS and storage**. In the **Operating system and storage** pane that appears, configure your boot disk by doing the following:

     1. Click **Change**. The **Boot disk** pane appears and displays the **Public images** tab.
     2. Click **Custom images**. The **Custom images** tab appears.
     3. To select the image project, click **Change** , and then select the project that contains the image.
     4. In the **Image** list, select the image that you want to import.
     5. In the **Boot disk type** list, select the type of the boot disk.
     6. In the **Size (GB)** field, specify the size of the boot disk.
     7. Optional: For Hyperdisk Balanced boot disks, specify values for the **Provisioned IOPS** and **Provisioned throughput** fields.
     8. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section.
     9. To confirm your boot disk options and return to the **Operating system and storage** pane, click **Select**.
  4. In the navigation menu, click **Networking**. In the **Networking** pane that appears, do the following:

     1. Go to the **Firewall** section.
     2. To permit HTTP or HTTPS traffic to the instance, select **Allow HTTP traffic** or **Allow HTTPS traffic**.

The **Compute Engine** adds a network tag to your instance and creates the corresponding ingress firewall rule that allows all incoming traffic on `tcp:80` (HTTP) or `tcp:443` (HTTPS). The network tag associates the firewall rule with the instance. For more information, see [Firewall rules overview](https://docs.cloud.google.com/firewall/docs/firewalls) in the **Cloud Next Generation Firewall** documentation.

  5. Optional: Specify other configuration options. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options).

  6. To create and start the instance, click **Create**.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Create an instance by using the [`gcloud compute instances create command`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create), and use the `--image` and `--image-project` flags to specify the image name and the project where the image resides:
         
         gcloud compute instances create INSTANCE_NAME \
         --image=IMAGE \
         --image-project=IMAGE_PROJECT
         

Replace the following:

     * `INSTANCE_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance
     * `IMAGE`: the name of the image
     * `IMAGE_PROJECT`: the project to which the image belongs

If the command is successful, then `gcloud` responds with the properties of the new instance, like in the following example:
    
    Created [https://compute.googleapis.com/compute/v1/projects/myproject/zones/us-central1-b/instances/example-instance].
    NAME                 ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS
    example-instance     us-central1-b  e2-standard-2               10.240.0.4   104.198.53.60  RUNNING
    




###  Terraform 

The process for creating an instance with a shared image in Terraform is the same as if you were creating an instance with a publicly available image.

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**.
  3. Specify the parameters you want.
  4. At the top or bottom of the page, click **Equivalent code** , and then click the **Terraform** tab to view the Terraform code.



###  REST 

The process for creating an instance with a shared image in the API is the same as if you were creating an instance with a publicly available image.

To create the instance from a shared image, use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
       "machineType":"zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
       "name":"VM_NAME",
       
       "disks":[
          {
             "initializeParams":{
                "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE"
             },
             "boot":true
          }
       ],
       
       
       "networkInterfaces":[
          {
             "network":"global/networks/NETWORK_NAME"
          }
       ],
       
      
       "shieldedInstanceConfig":{
          "enableSecureBoot":"ENABLE_SECURE_BOOT"
       }
    }
    

Replace the following:

  * `PROJECT_ID`: ID of the project to create the VM in
  * `ZONE`: zone to create the VM in
  * `MACHINE_TYPE_ZONE`: zone containing the machine type to use for the new VM
  * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types), for the new VM
  * `VM_NAME`: [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the new VM
  * `IMAGE_PROJECT`: name of the project that contains the shared image
  * `IMAGE`: specify one of the following: 
    * `IMAGE`: name of the shared image. For example, `"sourceImage": "projects/finance-project-1234/global/images/finance-debian-image-v2"`.
    * `IMAGE_FAMILY`: if the shared image is created as part of a [custom image family](https://docs.cloud.google.com/compute/docs/images#custom-families), specify that custom image family. 

This creates the VM from the most recent, non-deprecated OS image in your custom image family. For example, if you specify `"sourceImage": "projects/finance-project-1234/global/images/family/finance-debian-family"`, Compute Engine creates a VM from the latest version of the OS image in the custom `finance-debian-family` image family.

  * `NETWORK_NAME`: the VPC network that you want to use for the VM. You can specify `default` to use your default network.
  * `ENABLE_SECURE_BOOT`: Optional: If you chose an image that supports [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) features, Compute Engine, by default, enables the [virtual trusted platform module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm) and [integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring). Compute Engine does not enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) by default.

If you specify `true` for `enableSecureBoot`, Compute Engine creates a VM with all three Shielded VM features enabled. After Compute Engine starts your VM, to [modify Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm) options, you must stop the VM.




## What's next

  * Learn more about [custom images](https://docs.cloud.google.com/compute/docs/images/create-custom) and [how to share them](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images).
  * Learn how to [check the status of an instance](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle) to see when it is ready to use.
  * Learn how to [connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
