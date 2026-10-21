---
url: https://docs.cloud.google.com/compute/docs/instances/enable-graceful-shutdown/
title: Enable graceful shutdown in a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:40.385191+00:00
---

# Enable graceful shutdown in a Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/enable-graceful-shutdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enable graceful shutdown in a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to enable graceful shutdown in a new or existing Compute Engine instance.

When you enable graceful shutdown in a compute instance, you can give its guest OS up to six hours to cleanly shut down when you stop or delete the compute instance. This action helps prevent data loss or corrupted file systems when your applications need more time to finish running tasks. To learn more about the requirements and limitations that you apply when you gracefully shutdown a compute instance, see [About graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview).

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




### Required roles

To get the permissions that you need to enable graceful shutdown in a compute instance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to enable graceful shutdown in a compute instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to enable graceful shutdown in a compute instance:

  * To create compute instances: 
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
  * To enable graceful shutdown in an existing compute instance: `compute.instances.update` on the compute instance 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable graceful shutdown

To enable graceful shutdown in a compute instance, use one of the following methods:

  * Enable graceful shutdown in an existing compute instance

  * Enable graceful shutdown while creating a compute instance

  * Enable graceful shutdown while creating compute instances in bulk

  * Enable graceful shutdown while creating an instance template




### Enable graceful shutdown in an existing compute instance

If you enable graceful shutdown in an existing compute instance, then you must restart the compute instance as described in this section.

To enable graceful shutdown in an existing compute instance, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the compute instance in which you want to enable graceful shutdown. The details page of the compute instance opens.

  3. Click edit **Edit**.

  4. In the **Management** section, do the following:

     1. Select the **Gracefully shut down the VM** checkbox.

     2. In the **Maximum duration** field that appears, enter the number of minutes or seconds that you want your graceful shutdown to last. The value must be between one second and 360 minutes (six hours).

  5. Click **Save**.




###  gcloud 

To enable graceful shutdown in an existing compute instance, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update) with the `--graceful-shutdown` and `--graceful-shutdown-max-duration` flags:
    
    
    gcloud compute instances update INSTANCE_NAME \
        --graceful-shutdown \
        --graceful-shutdown-max-duration=MAX_DURATION \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `MAX_DURATION`: the maximum duration of the graceful shutdown. The value must be formatted as the number of hours, minutes, or seconds followed by `h`, `m`, and `s` respectively. For example, specify `1h` for one hour, or `20m10s` for 20 minutes and 10 seconds. The value must be between one second and six hours.

  * `ZONE`: the zone where the compute instance exists.




###  REST 

  1. Create an empty JSON file.

  2. To view the properties of an existing compute instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the compute instance exists.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name of an existing compute instance.

  3. In the empty JSON file that you created in the previous steps, do the following:

     1. Enter the compute instance configuration details from the `GET` request output.

     2. In the `scheduling` field, add the `gracefulShutdown` field as follows:
            
            {
              ...
              "scheduling": {
                ...
                "gracefulShutdown": {
                  "enabled": true,
                  "maxDuration": {
                    "seconds": "MAX_DURATION"
                  }
                }
              },
              ...
            }
            

Replace `MAX_DURATION` with the maximum duration of the graceful shutdown, in seconds. The value must be between `1` (one second) and `21600` (21,600 seconds, or six hours).

  4. To update the compute instance and restart it, make a `PUT` request to the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update). In the request, do the following:

     * In the request URL, include the `mostDisruptiveAllowedAction` query parameter set to `RESTART`.

     * In the request body, include the compute instance properties from the JSON file that you created and updated in the previous steps.

The `PUT` request to update the compute instance is similar to the following:
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?mostDisruptiveAllowedAction=RESTART
    
    {
      ...
      "scheduling": {
        ...
        "gracefulShutdown": {
          "enabled": true
        }
      },
      ...
    }
    




For more information about updating the properties of a compute instance, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update).

### Enable graceful shutdown while creating a compute instance

To create a compute instance that has graceful shutdown enabled, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click **Create instance**. The **Create an instance** page opens.

  3. In the **Name** field, enter a name for the compute instance.

  4. In the **Region** and **Zone** lists, enter the region and zone in which to create your compute instance.

  5. Specify the machine type for your compute instance.

  6. Expand the expand_more **VM provisioning model advanced settings** section, and then do the following:

     1. Select the **Gracefully shut down the VM** checkbox.

     2. In the **Maximum duration** field that appears, enter the number of minutes or seconds that you want your graceful shutdown to last. The value must be between one second and 360 minutes (six hours).

  7. Click **Create**.




###  gcloud 

To create a compute instance that has graceful shutdown enabled, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--graceful-shutdown` flag:
    
    
    gcloud compute instances create INSTANCE_NAME \
        --graceful-shutdown \
        --graceful-shutdown-max-duration=MAX_DURATION \
        --machine-type=MACHINE_TYPE \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `MAX_DURATION`: the maximum duration of the graceful shutdown. The value must be formatted as the number of hours, minutes, or seconds followed by `h`, `m`, and `s` respectively. For example, specify `1h` for one hour, or `20m10s` for 20 minutes and 10 seconds. The value must be between one second and six hours.

  * `MACHINE_TYPE`: the machine type to use for the compute instance.

  * `ZONE`: the zone in which to create the compute instance.




###  REST 

To create a compute instance that has graceful shutdown enabled, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `gracefulShutdown` field:
    
    
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
        "gracefulShutdown": {
          "enabled": true,
          "maxDuration": {
            "seconds": "MAX_DURATION"
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the compute instance.

  * `ZONE`: the zone in which to create the compute instance.

  * `INSTANCE_NAME`: the name of the compute instance.

  * `MACHINE_TYPE`: the machine type for the compute instance.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This formatting specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MAX_DURATION`: the maximum duration of the graceful shutdown, in seconds. The value must be between `1` (one second) and `21600` (21,600 seconds, or six hours).




For more information about creating a compute instance, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Enable graceful shutdown while creating instances in bulk

Before you can gracefully shut down or modify graceful shutdown settings for your compute instances, you must wait for Compute Engine to finish creating all your compute instances. Otherwise, you encounter errors.

To create compute instances in bulk that have graceful shutdown enabled, select one of the following options:

###  gcloud 

To create compute instances in bulk that have graceful shutdown enabled, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--graceful-shutdown` and `--graceful-shutdown-max-duration` flags.

For example, to create compute instances in bulk in a single zone and specify a name pattern for the compute instances, run the following command:
    
    
    gcloud compute instances bulk create \
        --count=COUNT \
        --graceful-shutdown \
        --graceful-shutdown-max-duration=MAX_DURATION \
        --machine-type=MACHINE_TYPE \
        --name-pattern="NAME_PATTERN" \
        --zone=ZONE
    

Replace the following:

  * `COUNT`: the number of instances to create.

  * `MAX_DURATION`: the maximum duration of the graceful shutdown. The value must be formatted as the number of hours, minutes, or seconds followed by `h`, `m`, and `s` respectively. For example, specify `1h` for one hour, or `20m10s` for 20 minutes and 10 seconds. The value must be between one second and six hours.

  * `MACHINE_TYPE`: the machine type for the instances.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of instances specified by `COUNT`.

  * `ZONE`: the zone in which to create instances in bulk.




###  REST 

To create instances in bulk that have graceful shutdown enabled, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). In the request body, include the `gracefulShutdown` field.

For example, to create instances in bulk in a single zone and specify a name pattern for the instances, make a `POST` request as follows:
    
    
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
          "gracefulShutdown": {
            "enabled": true,
            "maxDuration": {
              "seconds": "MAX_DURATION"
            }
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create instances in bulk.

  * `ZONE`: the zone in which to create instances in bulk.

  * `COUNT`: the number of instances to create.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of instances specified by `COUNT`.

  * `MACHINE_TYPE`: the machine type for the instances.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This formatting specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MAX_DURATION`: the maximum duration of the graceful shutdown, in seconds. The value must be between `1` (one second) and `21600` (21,600 seconds, or six hours).




For more configuration options when creating instances in bulk, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

### Enable graceful shutdown while creating an instance template

When you create an instance template that has graceful shutdown enabled, the default period for graceful shutdown is 10 minutes. Optionally, you can specify a custom period between one second and six hours. All compute instances that you create by using the instance template have graceful shutdown enabled.

To create an instance template that has graceful shutdown enabled, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page appears.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select whether you want to create a regional or global instance template based on your use case:

     * To reduce cross-region dependency, create a regional instance template by completing the following steps:

       1. Select **Regional**.

       2. In the **Region** field, select the region in which to create your instance template.

     * To use the instance template across regions, select **Global**.

  5. In the **Machine configuration** section, specify a machine type.

  6. Expand the expand_more **VM provisioning model advanced settings** section, and then do the following:

     1. Select the **Gracefully shut down the VM** checkbox.

     2. In the **Maximum duration** field that appears, enter the number of minutes or seconds that you want your graceful shutdown to last. The value must be between one second and 360 minutes (six hours).

  7. Click **Create**.




###  gcloud 

To create an instance template that has graceful shutdown enabled, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--graceful-shutdown` flag.

For example, to create a regional instance template that has graceful shutdown enabled, run the following command. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --graceful-shutdown \
        --graceful-shutdown-max-duration=MAX_DURATION
        --instance-template-region=REGION \
        --machine-type=MACHINE_TYPE
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the compute instance template.

  * `MAX_DURATION`: the maximum duration of the graceful shutdown. The value must be formatted as the number of hours, minutes, or seconds followed by `h`, `m`, and `s` respectively. For example, specify `1h` for one hour, or `20m10s` for 20 minutes and 10 seconds. The value must be between one second and six hours.

  * `REGION`: the region in which to create the compute instance template.

  * `MACHINE_TYPE`: the machine type for the compute instances that you create by using the instance template.




###  REST 

To create an instance template that has graceful shutdown enabled, make a `POST` request to one of the following methods:

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).




For example, to create a regional instance template that has graceful shutdown enabled, make a `POST` request as follows:
    
    
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
          "gracefulShutdown": {
            "enabled": true,
            "maxDuration": {
              "seconds": "MAX_DURATION"
            }
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where to create the instance template.

  * `REGION`: the region where to create the compute instance template.

  * `INSTANCE_TEMPLATE_NAME`: the name of the compute instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This formatting specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type for the compute instances that you create by using the instance template.

  * `MAX_DURATION`: the maximum duration of the graceful shutdown, in seconds. The value must be between `1` (one second) and `21600` (21,600 seconds, or six hours).




For more configuration options when creating an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## What's next

  * [Stop or restart a compute instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)

  * [Scheduling a VM instance to start and stop](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop)

  * [Delete a compute instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)

  * [View graceful shutdown in a compute instance](https://docs.cloud.google.com/compute/docs/instances/view-graceful-shutdown)

  * [Disable graceful shutdown in a compute instance](https://docs.cloud.google.com/compute/docs/instances/disable-graceful-shutdown)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
