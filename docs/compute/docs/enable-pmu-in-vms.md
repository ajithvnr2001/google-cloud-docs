---
url: https://docs.cloud.google.com/compute/docs/enable-pmu-in-vms/
title: Enable the PMU in Compute Engine instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:15.938576+00:00
---

# Enable the PMU in Compute Engine instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/enable-pmu-in-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enable the PMU in Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to enable the performance monitoring unit (PMU) in A4X, C4A, C4, or M4 Compute Engine instances. After you enable the PMU, you can use it to optimize performance-sensitive workloads, such as high performance computing (HPC) or machine learning (ML), by identifying and addressing application bottlenecks.

To learn more about the requirements and limitations that you apply when you enable the PMU in a compute instance, see [PMU overview](https://docs.cloud.google.com/compute/docs/pmu-overview).

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

To get the permissions that you need to enable the PMU in a new or existing compute instance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to enable the PMU in a new or existing compute instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to enable the PMU in a new or existing compute instance:

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
  * To update a compute instance: `compute.instances.update` on the compute instance 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable the PMU in compute instances

To enable the PMU in one or more compute instances, use one of the following methods:

  * Enable the PMU in an existing compute instance
  * Enable the PMU while creating a compute instance
  * Enable the PMU while creating compute instances in bulk
  * Enable the PMU while creating an instance template



After you've enabled the PMU in one or more compute instances, you can install and use performance-monitoring software on the compute instances.

### Enable the PMU in an existing compute instance

Before you enable the PMU in an existing compute instance, you must verify that the compute instance uses a [supported machine series and CPU platform](https://docs.cloud.google.com/compute/docs/pmu-overview#supported-series). To verify the machine series and CPU platform that your compute instance uses, [view the details of the compute instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).

If your compute instance doesn't use a supported machine series, then replace the compute instance's machine type. You can do this either by [migrating your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm) that uses a supported machine type, or by changing the machine type for supported configurations:

  * If you need to move your existing compute instance to a new compute instance to change the machine type, then create a new compute instance that has the PMU enabled in a zone that offers the CPU platform you want to use with PMU events.

  * If you can change the machine type, then complete the following steps:

    1. Verify that a supported CPU platform is available in the zone where your compute instance exists by reviewing the [available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

    2. If a supported CPU platform isn't available in the zone of your compute instance, then [migrate the compute instance to a zone that has a supported CPU platform](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones).

    3. [Change the machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance). To enable the architectural or standard PMU type, you can specify any A4X, C4A, C4, or M4 machine type. However, to enable the enhanced PMU type, you must specify one of the following C4 or M4 machine types:

       * Any C4 machine type with 144 or 288 vCPUs

       * One of the following M4 machine types:

         * `m4-megamem-112`

         * `m4-megamem-224`

         * `m4-ultramem-56`

         * `m4-ultramem-112`

         * `m4-ultramem-224`




You don't have to stop the compute instance to enable the PMU. However, to make the change effective, you must restart the compute instance as described in this section.

To enable the PMU in an existing compute instance, select one of the following options:

###  gcloud 

  1. Create an empty YAML file.

  2. To export the properties of a compute instance into the YAML file that you've just created, use the [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export):
         
         gcloud compute instances export INSTANCE_NAME \
             --destination=YAML_FILE \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name for the compute instance.

     * `YAML_FILE`: the path to the YAML file that you created in the previous step.

     * `ZONE`: the zone where the compute instance exists.

  3. In the YAML configuration file, in the `advancedMachineFeatures` field, add the `performanceMonitoringUnit` field. If the `advancedMachineFeatures` field doesn't exist, then add it as well:
         
         advancedMachineFeatures:
           performanceMonitoringUnit: PMU_TYPE
         

Replace `PMU_TYPE` with one of the following values:

     * Architectural PMU type: `ARCHITECTURAL`

     * Standard PMU type: `STANDARD`

     * Enhanced PMU type: `ENHANCED`

  4. To update the compute instance and restart it, use the [`gcloud compute instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) with the `--most-disruptive-allowed-action` flag set to `RESTART`:
         
         gcloud compute instances update-from-file INSTANCE_NAME \
             --most-disruptive-allowed-action=RESTART \
             --source=YAML_FILE \
             --zone=ZONE
         

Replace `YAML_FILE` with the path to the YAML file with the configuration data that you modified in the previous step.




###  REST 

  1. To view the properties of an existing compute instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where you created the compute instance.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name for the compute instance.

  2. To update the compute instance and restart it, make a `PUT` request to the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update) as follows:

     * In the request URL, include the `mostDisruptiveAllowedAction` query parameter set to `RESTART`.

     * For the request body, use the `GET` request output from the previous step. However, in the `advancedMachineFeatures` field, you must add the `performanceMonitoringUnit` field to enable the PMU. If the `advancedMachineFeatures` field doesn't exist in the request output, then add it as well:

The `PUT` request is similar to the following:
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?mostDisruptiveAllowedAction=RESTART
    
    {
      "advancedMachineFeatures": {
        "performanceMonitoringUnit": "PMU_TYPE"
      },
      ...
    }
    

Replace `PMU_TYPE` with one of the following values:

     * Architectural PMU type: `ARCHITECTURAL`

     * Standard PMU type: `STANDARD`

     * Enhanced PMU type: `ENHANCED`




For more information about updating the properties of a compute instance, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update).

### Enable the PMU while creating a compute instance

You can create a compute instance that has the PMU enabled only in a zone that contains a [supported CPU platform](https://docs.cloud.google.com/compute/docs/pmu-overview#supported-series). For a list of available CPUs by zone, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

To create a compute instance that has the PMU enabled, select one of the following options:

###  gcloud 

To create a compute instance that has the PMU enabled, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--performance-monitoring-unit` flag:
    
    
    gcloud compute instances create INSTANCE_NAME \
        --machine-type=MACHINE_TYPE \
        --performance-monitoring-unit=PMU_TYPE \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name for the compute instance.

  * `MACHINE_TYPE`: the machine type for the compute instance. If you want to enable the enhanced PMU type in a compute instance, then you can enable it only if your compute instance uses a [supported machine type](https://docs.cloud.google.com/compute/docs/pmu-overview#limitations).

  * `PMU_TYPE`: the PMU type to enable in the compute instance. Specify one of the following values:

    * Architectural PMU type: `architectural`

    * Standard PMU type: `standard`

    * Enhanced PMU type: `enhanced`

  * `ZONE`: the zone in which to create the compute instance.




###  REST 

To create a compute instance that has the PMU enabled, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the `performanceMonitoringUnit` field:
    
    
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
      "advancedMachineFeatures": {
        "performanceMonitoringUnit": "PMU_TYPE"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the compute instance.

  * `ZONE`: the zone in which to create the compute instance.

  * `INSTANCE_NAME`: the name for the compute instance.

  * `MACHINE_TYPE`: the machine type for the compute instance. If you want to enable the enhanced PMU type in a compute instance, then you can enable it only if your compute instance uses a [supported machine type](https://docs.cloud.google.com/compute/docs/pmu-overview#limitations).

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `PMU_TYPE`: the PMU type to enable in the compute instance. Specify one of the following values:

    * Architectural PMU type: `ARCHITECTURAL`

    * Standard PMU type: `STANDARD`

    * Enhanced PMU type: `ENHANCED`




For more information about creating a compute instance, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Enable the PMU while creating compute instances in bulk

You can create compute instances in bulk that have the PMU enabled only in a zone that contains a [supported CPU platform](https://docs.cloud.google.com/compute/docs/pmu-overview#supported-series). For a list of available CPUs by zone, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

To create compute instances in bulk that have the PMU enabled, select one of the following options:

###  gcloud 

To create compute instances in bulk that have the PMU enabled, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with the `--performance-monitoring-unit` flag.

For example, to create compute instances in bulk in a single zone and specify a name pattern, run the following command:
    
    
    gcloud compute instances bulk create \
        --count=COUNT \
        --machine-type=MACHINE_TYPE \
        --name-pattern="NAME_PATTERN" \
        --performance-monitoring-unit=PMU_TYPE \
        --zone=ZONE
    

Replace the following:

  * `COUNT`: the number of compute instances to create.

  * `MACHINE_TYPE`: the machine type for the compute instances. If you want to enable the enhanced PMU type in a compute instance, then you can enable it only if your compute instance uses a [supported machine type](https://docs.cloud.google.com/compute/docs/pmu-overview#limitations).

  * `NAME_PATTERN`: the name pattern for the compute instances. To replace a sequence of numbers in a compute instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates compute instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of compute instances specified by `COUNT`.

  * `PMU_TYPE`: the PMU type to enable in the compute instances. Specify one of the following values:

    * Architectural PMU type: `architectural`

    * Standard PMU type: `standard`

    * Enhanced PMU type: `enhanced`

  * `ZONE`: the zone in which to create compute instances in bulk.




###  REST 

To create compute instances in bulk that have the PMU enabled, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). In the request body, include the `performanceMonitoringUnit` field.

For example, to create compute instances in bulk in a single zone and specify a name pattern, make a `POST` request as follows:
    
    
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
        "advancedMachineFeatures": {
          "performanceMonitoringUnit": "PMU_TYPE"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create compute instances in bulk.

  * `ZONE`: the zone in which to create compute instances in bulk.

  * `COUNT`: the number of compute instances to create.

  * `NAME_PATTERN`: the name pattern for the compute instances. To replace a sequence of numbers in a compute instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates compute instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of compute instances specified by `COUNT`.

  * `MACHINE_TYPE`: the machine type for the compute instances. If you want to enable the enhanced PMU type in a compute instance, then you can enable it only if your compute instance uses a [supported machine type](https://docs.cloud.google.com/compute/docs/pmu-overview#limitations).

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `PMU_TYPE`: the PMU type to enable in the compute instances. Specify one of the following values:

    * Architectural PMU type: `ARCHITECTURAL`

    * Standard PMU type: `STANDARD`

    * Enhanced PMU type: `ENHANCED`




For more information about creating compute instances in bulk, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

### Enable the PMU while creating an instance template

If you want to create a regional instance template that specifies to enable the PMU, then ensure that at least one zone within the selected region contains a [supported CPU platform](https://docs.cloud.google.com/compute/docs/pmu-overview#supported-series). For a list of available CPUs by zone, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

After you create an instance template that specifies to enable the PMU, you can use the template to do the following:

  * Enable the PMU in the compute instances of a managed instance group (MIG) when you do the following:

    * [Create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group)

    * [Apply new compute instance configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs)

  * [Create a compute instance that has the PMU enabled](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)




To create an instance template that specifies to enable the PMU, select one of the following options:

###  gcloud 

To create an instance template that specifies to enable the PMU, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the `--performance-monitoring-unit` flag.

For example, use the following command to create a regional instance template. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --instance-template-region=REGION \
        --machine-type=MACHINE_TYPE \
        --performance-monitoring-unit=PMU_TYPE
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name for the instance template.

  * `REGION`: the region in which to create the instance template.

  * `MACHINE_TYPE`: the machine type for the compute instances. If you want to enable the enhanced PMU type in a compute instance, then you can enable it only if your compute instance uses a [supported machine type](https://docs.cloud.google.com/compute/docs/pmu-overview#limitations).

  * `PMU_TYPE`: the PMU type to include in the instance template. Specify one of the following values:

    * Architectural PMU type: `architectural`

    * Standard PMU type: `standard`

    * Enhanced PMU type: `enhanced`




###  REST 

To create an instance template that specifies to enable the PMU, make a `POST` request to one of the following methods:

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).




In the request body, include the `performanceMonitoringUnit` field.

For example, to create a regional instance template that specifies to enable the PMU, make a `POST` request as follows:
    
    
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
        "advancedMachineFeatures": {
          "performanceMonitoringUnit": "PMU_TYPE"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instance template.

  * `REGION`: the region in which to create the instance template.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type for the compute instances. If you want to enable the enhanced PMU type in a compute instance, then you can enable it only if your compute instance uses a [supported machine type](https://docs.cloud.google.com/compute/docs/pmu-overview#limitations).

  * `PMU_TYPE`: the PMU type to include in the instance template. Specify one of the following values:

    * Architectural PMU type: `ARCHITECTURAL`

    * Standard PMU type: `STANDARD`

    * Enhanced PMU type: `ENHANCED`




For more information about creating an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## What's next

  * [Connect to a compute instance](https://docs.cloud.google.com/compute/docs/instances/ssh)

  * [Change PMU type in an instance or disable the PMU](https://docs.cloud.google.com/compute/docs/manage-pmu-in-vms)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
