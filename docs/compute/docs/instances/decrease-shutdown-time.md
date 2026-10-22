---
url: https://docs.cloud.google.com/compute/docs/instances/decrease-shutdown-time/
title: Decrease Compute Engine instances shutdown time \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:28.714752+00:00
---

# Decrease Compute Engine instances shutdown time  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/decrease-shutdown-time/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Decrease Compute Engine instances shutdown time Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to decrease the shutdown time for a Compute Engine instance by configuring the instance to skip the guest OS shutdown on stop or deletion.

If you configure an instance to skip the guest OS shutdown on stop or deletion, then Compute Engine immediately shuts down the guest OS when the instance state changes to `STOPPING`. This action helps you release quota or resources faster by speeding up an instance stop or deletion. To learn more about the phases that an instance goes through during stop or deletion, including the default interval for clean guest OS shutdown, see [Stop operation](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#stopping-instance).

**Warning:** An abrupt shutdown of the guest OS can cause permanent data loss or file system corruption. Configure an instance to skip the guest OS shutdown only if you plan to delete the instance, or if you plan to stop an instance but you aren't concerned about the integrity of the data on the instance boot disk.

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




### Required roles

To get the permissions that you need to configure an instance to skip the guest OS shutdown, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to configure an instance to skip the guest OS shutdown. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure an instance to skip the guest OS shutdown:

  * To create an instance: 
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
  * To create an instance template: `compute.instanceTemplates.create` on the project 
  * To update an instance: `compute.instances.update` on the instance 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure instances to skip guest OS shutdown

To configure a compute instance to skip the guest OS shutdown when you stop or delete the instance, use one of the following methods:

  * Configure guest OS shutdown in an existing instance

  * Configure guest OS shutdown while you create an instance

  * Configure guest OS shutdown while you create instances in bulk

  * Configure guest OS shutdown while you create an instance template




### Configure guest OS shutdown in an existing instance

You can only configure a compute instance to skip the guest OS shutdown if the instance is stopped (`TERMINATED`).

To configure an instance to skip the guest OS shutdown, select one of the following options:

###  gcloud 

  1. If you haven't already, then [stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

  2. To configure an instance to skip the guest OS shutdown, use the [`gcloud beta compute instances set-scheduling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling) with the `--skip-guest-os-shutdown` flag:
         
         gcloud compute instances set-scheduling INSTANCE_NAME \
             --skip-guest-os-shutdown \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.

     * `ZONE`: the zone where the instance exists.




###  REST 

  1. If you haven't already, then [stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

  2. To configure an instance to skip the guest OS shutdown, make a `POST` request to the [`instances.setScheduling` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setScheduling). In the request body, include the `skipGuestOsShutdown` field and set it to `true`:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/setScheduling
         
         {
           "skipGuestOsShutdown": true
         }
         




For more information on how to update an instance, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties).

### Configure guest OS shutdown while you create an instance

To create a compute instance that is configured to skip the guest OS shutdown, select one of the following options:

###  gcloud 

To create an instance that is configured to skip the guest OS shutdown, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--skip-guest-os-shutdown` flag:
    
    
    gcloud compute instances create INSTANCE_NAME \
        --machine-type=MACHINE_TYPE \
        --skip-guest-os-shutdown \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.

  * `MACHINE_TYPE`: the machine type to use for the instance.

  * `ZONE`: the zone where you want to create the instance.




###  REST 

To create an instance that is configured to skip the guest OS shutdown, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `skipGuestOsShutdown` field set to `true`:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      "scheduling": {
        "skipGuestOsShutdown": true
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the instance.

  * `ZONE`: the zone where you want to create the instance.

  * `INSTANCE_NAME`: the name of the instance.

  * `MACHINE_TYPE`: the machine type to use for the instance.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which you must format as `family/IMAGE_FAMILY`. This value specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine uses the latest version in the Debian 12 image family. For more information on how to use image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




For more information on how to create an instance, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Configure guest OS shutdown while you create instances in bulk

To create compute instances in bulk that are configured to skip the guest OS shutdown, select one of the following options:

###  gcloud 

To create instances in bulk that are configured to skip the guest OS shutdown, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--skip-guest-os-shutdown` flag.

For example, to create instances in bulk that use a name pattern in a single zone, run the following command:
    
    
    gcloud compute instances bulk create \
        --count=COUNT \
        --machine-type=MACHINE_TYPE \
        --name-pattern="NAME_PATTERN" \
        --skip-guest-os-shutdown \
        --zone=ZONE
    

Replace the following:

  * `COUNT`: the number of instances to create.

  * `MACHINE_TYPE`: the machine type to use for the instances.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, if you use `instance-#` as a name pattern, Compute Engine generates instances with names that start with `instance-1`, `instance-2`, and it continues this incremental pattern up to the number of instances that you specify in `COUNT`.

  * `ZONE`: the zone where you want to create instances.




###  REST 

To create instances in bulk that are configured to skip the guest OS shutdown, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). In the request body, include the `skipGuestOsShutdown` field set to `true`.

For example, to create instances in bulk that use a name pattern in a single zone, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    
    {
      "count": COUNT,
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "machineType": "MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "scheduling": {
          "skipGuestOsShutdown": true
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create instances in bulk.

  * `ZONE`: the zone where you want to create instances.

  * `COUNT`: the number of instances to create.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, if you use `instance-#` as a name pattern, Compute Engine generates instances with names that start with `instance-1`, `instance-2`, and it continues this incremental pattern up to the number of instances that you specify in `COUNT`.

  * `MACHINE_TYPE`: the machine type to use for the instances.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which you must format as `family/IMAGE_FAMILY`. This value specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine uses the latest version in the Debian 12 image family. For more information on how to use image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




For more information on how to create instances in bulk, see [Create instances in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

### Configure guest OS shutdown while you create an instance template

After you create an instance template configured to skip the guest OS shutdown when you stop or delete compute instances, you can use the instance template to do the following:

  * You can configure the instances in a managed instance group (MIG) to skip the guest OS shutdown on stop or deletion when you do the following:

    * [Create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group)

    * [Apply new instance configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs)

  * [Create an instance configured to skip the guest OS shutdown](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)




To create an instance template that is configured to skip the guest OS shutdown, select one of the following options:

###  gcloud 

To create an instance template that is configured to skip the guest OS shutdown, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--skip-guest-os-shutdown` flag.

For example, to create a regional instance template that specifies to skip the guest OS shutdown, run the following command. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --instance-template-region=REGION \
        --machine-type=MACHINE_TYPE \
        --skip-guest-os-shutdown
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `REGION`: the region where you want to create the instance template.

  * `MACHINE_TYPE`: the machine type to specify in the instance template.




###  REST 

To create an instance template that is configured to skip the guest OS shutdown, make a `POST` request to one of the following methods:

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert)

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert)




In the request body, include the `skipGuestOsShutdown` field set to `true`.

For example, to create a regional instance template that specifies to skip the guest OS shutdown, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "scheduling": {
          "skipGuestOsShutdown": true
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the instance template.

  * `REGION`: the region where you want to create the instance template.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type to specify in the instance template.




For more information about creating an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## View guest OS shutdown setting

You can check whether Compute Engine skips the guest OS shutdown when you stop or delete a compute instance.

To view the guest OS shutdown time in an instance, select one of the following options:

###  gcloud 

To view the details of an instance and whether it skips the guest OS shutdown, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.

  * `ZONE`: the zone where the instance exists.




If you configured the instance to skip the guest OS shutdown, then the output contains the `skipGuestOsShutdown` field set to `true`, such as in the following example:
    
    
    ...
    scheduling:
      automaticRestart: true
      **skipGuestOsShutdown: true**
      onHostMaintenance: MIGRATE
      preemptible: false
      provisioningModel: STANDARD
    ...
    

Otherwise, if the `skipGuestOsShutdown` field is missing or is set to `false`, the guest OS uses the [default shutdown time](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#stopping-instance).

###  REST 

To view the details of an instance and whether it skips the guest OS shutdown, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the instance exists.

  * `ZONE`: the zone where the instance exists.

  * `INSTANCE_NAME`: the name of the instance.




If you configured the instance to skip the guest OS shutdown, then the output contains the `skipGuestOsShutdown` field set to `true`, such as in the following example:
    
    
    {
      ...
      "scheduling": {
        "automaticRestart": true,
        **"skipGuestOsShutdown": true** ,
        "onHostMaintenance": "MIGRATE",
        "preemptible": false,
        "provisioningModel": "STANDARD"
      },
      ...
    }
    

Otherwise, if the `skipGuestOsShutdown` field is missing or is set to `false`, the guest OS uses the [default shutdown time](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#stopping-instance).

## What's next

  * [Stop or restart an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)

  * [Schedule an instance to start and stop](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop)

  * [Limit the runtime of an instance](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime)

  * [Delete an instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
