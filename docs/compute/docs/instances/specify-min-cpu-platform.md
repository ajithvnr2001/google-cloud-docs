---
url: https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform/
title: Specify a minimum CPU platform for compute instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:52.541625+00:00
---

# Specify a minimum CPU platform for compute instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Specify a minimum CPU platform for compute instances Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

For machine types that can run on different CPU platforms, this page explains how to create or update a Compute Engine instance to use a specified CPU compatibility level instead of the default one.

Google Cloud data centers offer different generations of CPU processors. These processors support incremental features like [Advanced Vector Extensions](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/what-is-intel-avx-512.html?wapkw=AVX)— for example, AVX2 and AVX-512. Also, some fundamental features like clock speed, NUMA splits, and memory access seek time can vary among the CPU processors. The term [_CPU platform_](https://docs.cloud.google.com/compute/docs/cpu-platforms) refers to this CPU-based configuration.

Each machine series works with one or more CPU processors. For example, C4 instances can run on either Intel Emerald Rapids or Granite Rapids CPUs. If a machine series supports multiple CPUs, you can choose a _minimum CPU platform_ when you create an instance. The value you can set for the minimum CPU depends on the machine type, and the region and zone you choose for your compute instances.

Choosing a specific CPU is useful if your workload is sensitive to CPU-specific features, like instruction sets (AVX2 instead of AVX-512), cache sizes, or clock speeds which can vary between CPU platforms.

  * You can set the minimum CPU to a more recent processor to take advantage of higher clock frequency
  * You might set the minimum CPU to an older processor to ensure compatibility for your applications.



However using the minimum CPU setting can limit which zones your compute instances can run in.

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




### Required roles and permissions

To get the permissions that you need to change the minimum CPU platform, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a compute instance that can run as a service account: Service Account User (v1) (`roles/iam.serviceAccountUser` role) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## When to select a minimum CPU platform

Each Compute Engine zone has a default CPU for each machine series. If you don't specify a value for the minimum CPU for your instance, then your compute instance uses the default CPU assigned to the machine type and zone.

We recommend choosing a CPU platform compatibility level only in these cases:

  * **Performance** : If a specific processor gives your workload a significant speed boost or has features like AVX-512 that your code needs
  * **Compatibility** : If your compute instance requires a certain operating system, instruction set, or libraries that aren't supported on a more recent CPU platform
  * **Reservations** : If you use [reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type), your compute instance must use the same CPU platform as the reservation.

**Note:** Choosing a minimum CPU platform might prevent you from creating a compute instance if that CPU type isn't available in the specified zone.

## Using the default CPU platform

If you don't specify a minimum CPU for your instance, then the minimum CPU is set to `AUTOMATIC`. This means that the instance uses the default CPU platform for the machine type.

On rare occasions, Google Cloud updates a CPU platform for a machine type and zone.

## How selecting a minimum CPU platform works

When you specify a value for the minimum CPU, Compute Engine provides that CPU platform for your instance to use. Your compute instance continues to use that CPU platform unless you change it.

Your compute instance uses the specified CPU platform even after live migration during a maintenance operation.

## Limitations

  * Each [region and zone](https://docs.cloud.google.com/compute/docs/regions-zones) supports multiple CPU platforms, but a region or zone might not offer all CPU platforms.
  * You can't specify a minimum CPU platform for compute instances that run on sole-tenant nodes.
  * You can't select a minimum CPU platform for any E2 virtual machine (VM) instance.
  * You can't specify a minimum CPU platform for VM instances that were created with [shared-core, general-purpose machine types](https://docs.cloud.google.com/compute/docs/machine-resource#shared-core-types).



## Availability of CPU platforms

The availability of CPU platforms varies across zones and is based on the hardware and machine series that is available in each zone. To see what CPU platforms are available in Google Cloud and the machine series associated with each CPU platform, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).

The following list shows the supported minimum CPU platforms and the valid syntax for each platform:

Processor | Syntax  
---|---  
6th Generation Intel Xeon (Granite Rapids) | `Intel Granite Rapids`  
5th Generation Intel Xeon (Emerald Rapids) | `Intel Emerald Rapids`  
4th Generation Intel Xeon (Sapphire Rapids) | `Intel Sapphire Rapids`  
3rd Generation Intel Xeon (Ice Lake) | `Intel Ice Lake`  
2nd Generation Intel Xeon (Cascade Lake) | `Intel Cascade Lake`  
1st Generation Intel Xeon (Skylake) | `Intel Skylake`  
Intel Xeon E7 or E5 v4 (Broadwell) | `Intel Broadwell`  
Intel Xeon E5 v3 (Haswell) | `Intel Haswell`  
Intel Xeon E5 v2 (Ivy Bridge) | `Intel Ivy Bridge`  
Intel Xeon E5 (Sandy Bridge) | `Intel Sandy Bridge`  
5th Generation AMD EPYC Turin | `AMD Turin`  
4th Generation AMD EPYC Genoa | `AMD Genoa`  
3rd Generation AMD EPYC Milan | `AMD Milan`  
NVIDIA Grace (Arm Neoverse V2) | `NVIDIA Grace`  
Google Axion (Neoverse V2 Armv9) | `Google Axion`  
Google Axion (Neoverse N3 Armv9.2) | `Google Axion`  
Ampere Altra (Arm Neoverse N1) | `Ampere Altra`  
  
## View available CPUs by zone

Some regions and zones support multiple CPU platforms for the same machine series. You can check which CPUs are available in a zone using Google Cloud CLI or REST.

If you're using sole-tenant nodes, each node uses the CPU platform corresponding to the [node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) that you defined in the node template.

###  gcloud 

  * To view the CPU platforms that are available in your zone, use the [`gcloud compute zones describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/describe):
        
        gcloud compute zones describe ZONE
        

Replace `ZONE` with the name of the zone to check for available CPU platforms—for example, `europe-west10-a`.

The following output from this command lists CPU platforms for the `europe-west10-a` zone:
        
        gcloud compute zones describe europe-west10-a
        availableCpuPlatforms:
        - Intel Broadwell
        - Intel Cascade Lake
        - Intel Ice Lake
        - AMD Milan
        - Intel Skylake
        
        ...
        




###  REST 

  * Make a [`GET` request](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zones/get) to the zone that you're considering:
        
        GET https://compute.googleapis.com/compute/v1/projects/myproject/zones/ZONE
        

Replace `ZONE` with the name of the zone to check for available CPU platforms.

The following output from this command lists supported CPU platforms for a zone:
        
        {
          "kind": "compute#zone",
          "id": "2210",
          "creationTimestamp": "1969-12-31T09:30:55.189-07:00",
          "name": "europe-west10-a",
          "description": "europe-west10-a",
          "status": "UP",
          "region": "https://www.googleapis.com/compute/v1/projects/myproject/regions/europe-west10-a",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/myproject/zones/europe-west10-a",
          "availableCpuPlatforms": [
           "Intel Broadwell",
           "Intel Cascade Lake",
           "Intel Ice Lake",
           "AMD Milan",
           "Intel Skylake"
          ],
          "supportsPzs": true
         }




## Changes to default CPU platforms

On rare occasions, Google Cloud updates the default CPU platform for a machine series in a zone. When this happens, Google Cloud notifies you with a timeline and instructions for moving to the new platform.

  * **If you specified a minimum CPU platform for your compute instance** : the change to the default CPU platform has no impact on your instance. Compute Engine never provides a CPU platform that is older than the one specified by the minimum CPU property for an instance.
  * **If you didn't specify a value for the minimum CPU** : the instance can run on a newer CPU platform; if the instance used the old default CPU platform for a zone, that CPU platform might not be available after Google Cloud changes the default CPU platform for that zone.



If Compute Engine runs your compute instance on a newer CPU platform, the cost of your compute instance doesn't change.

If the default CPU platform changes for a machine series, you can either:

  * Set the minimum CPU property for your instance if you want to keep the compatibility level of the previous default CPU platform.
  * Leave the minimum CPU property set to `AUTOMATIC` and let your compute instance use the newer CPU platform by stopping and restarting the instance.



## Choose a CPU platform for a new instance

When you create a compute instance, if the machine series supports more than one CPU platform, then you can use the minimum CPU property to specify the [CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms) that you want the instance to use.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** section, expand the **Advanced configurations** section.

  3. In the **CPU Platform** list, select a platform for the instances's CPU.

  4. Continue with the rest of the instance creation process.




###  gcloud 

  * To create a new compute instance that uses a minimum CPU platform, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and provide the `--min-cpu-platform` flag:
        
        gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --min-cpu-platform="PLATFORM"

Replace the following:

    * `INSTANCE_NAME`: the name of the instance that you want to create
    * `ZONE`: the name of the zone where you want to create your instance—for example, `europe-west1-b`
    * `PLATFORM`: the friendly name of the minimum CPU platform that you want the instance to use—for example, `Intel Sandy Bridge`

If you want to clear the minimum CPU platform specification, replace `PLATFORM` with `AUTOMATIC`.

To check which CPU platforms are available in a zone, see View available CPU platforms by zone.




###  REST 

  * Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) and include the `minCpuPlatform` property as part of the request body.

For example, a request body might look like this:
        
        "name": "INSTANCE_NAME",
        "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
        "minCpuPlatform": "PLATFORM",
        "networkInterfaces": [{
          "accessConfigs": [{
            "type": "ONE_TO_ONE_NAT",
            "name": "External NAT"
           }],
          "network": "global/networks/default"
        }],
        "disks": [{
           "autoDelete": "true",
           "boot": "true",
           "type": "PERSISTENT",
           "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
           }
         }]

Replace the following:

    * `INSTANCE_NAME`: the name of the new compute instance
    * `ZONE`: the name of the zone where you want to create your compute instance—for example, `europe-west1-b`
    * `MACHINE_TYPE`: the machine type of the new compute instance
    * `PLATFORM`: the friendly name of the minimum CPU platform that you want the instance to use—for example, `Intel Ivy Bridge`

To clear the minimum CPU platform specification, replace `PLATFORM` with `AUTOMATIC`.

To check which CPU platforms are available in a zone, see View available CPU platforms by zone.

    * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details) of the image family

    * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the image to use to create the compute instance




## Change the CPU for an existing instance

To change the CPU for an existing compute instance, you must first [stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance).

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If prompted, select your project and click **Continue**.

  3. Select the compute instance that you want to change.

  4. Click stop **Stop** to stop the compute instance. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

  5. Click **Edit**.

  6. In the **Machine configuration** section, click **Advanced configurations**.

  7. From the **CPU Platform** drop-down menu, select an option.

  8. Save your changes.

  9. Select the compute instance that you changed.

  10. Click **Start/Resume**.




###  gcloud 

  1. To stop a compute instance, use the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop):
         
         gcloud compute instances stop INSTANCE_NAME
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance that you want to specify a minimum CPU platform for
     * `ZONE`: the name of the zone where you created your compute instance—for example, `europe-west1-b`
  2. To specify a minimum CPU platform, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update), and provide the `--min-cpu-platform` flag:
         
         gcloud compute instances update INSTANCE_NAME \
             --zone=ZONE \
             --min-cpu-platform="PLATFORM"

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance to update
     * `ZONE`: the name of the zone where you created your compute instance
     * `PLATFORM`: the friendly name of the CPU platform that you want the compute instance to use—for example, `Intel Granite Rapids`.
  3. To start the updated compute instance, use the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
         
         gcloud compute instances start INSTANCE_NAME
             --zone=ZONE
         




###  REST 

  1. To stop a compute instance, construct a `POST` request using the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/stop):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: the ID of the project
     * `ZONE`: the zone where your compute instance is located
     * `INSTANCE_NAME`: the name of the compute instance that you want to specify a minimum CPU platform for
  2. To set the minimum CPU platform, construct a `POST` request to the [`setMinCpuPlatform` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setMinCpuPlatform) and set the `minCpuPlatform` property in the request body:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/setMinCpuPlatform
         {
           "minCpuPlatform": "PLATFORM"
         }
         

Replace `PLATFORM` with the friendly name of the minimum CPU platform that you want the compute instance to use—for example, `Intel Skylake`.

  3. To restart the compute instance, construct a `POST` request using the [`instances.start` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/start):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/start
         




## Reset to the default CPU

To go back to using the default CPU, you must stop the compute instance if it's running.

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If prompted, select your project and click **Continue**.

  3. Select the instance that you want to change.

  4. Click **Stop**.

  5. To edit the instance, click **Edit**.

  6. In the **Machine configuration** section, click **Advanced configurations**.

  7. Change the **CPU Platform** option to **Automatic**.

  8. Select the instance that you changed.

  9. Click **Start/Resume**.




###  gcloud 

  1. To stop a compute instance, use the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop):
         
         gcloud compute instances stop INSTANCE_NAME
         

Replace `INSTANCE_NAME` with the name of the compute instance that you want to change.

  2. To reset the minimum CPU platform, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update) and set the `--min-cpu-platform` flag to `AUTOMATIC`:
         
         gcloud compute instances update INSTANCE_NAME \
             --min-cpu-platform="AUTOMATIC"
         

  3. To start the updated compute instance, use the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
         
         gcloud compute instances start INSTANCE_NAME
         




###  REST 

  1. To stop a compute instance, construct a `POST` request using the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/stop):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: the ID of the project
     * `ZONE`: the zone where your compute instance is located
     * `INSTANCE_NAME`: the name of the compute instance that you want to change
  2. To reset the minimum CPU platform, construct a `POST` request to the [`setMinCpuPlatform`](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setMinCpuPlatform) method. In the request body, set the `minCpuPlatform` property value to `AUTOMATIC`.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/setMinCpuPlatform
         {
           "minCpuPlatform": "AUTOMATIC"
         }
         

  3. To restart the updated instance, construct a `POST` request using the [`instances.start` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/start):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/start
         




## Use a CPU platform compatibility level in instance templates

If you use [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances), you can set a CPU platform compatibility level for all compute instances in the group.

To do this, create an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates#creating_an_instance_template) and set the `minCpuPlatform` property.

###  Console 

  1. Go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. If prompted, select your project and click **Continue**.

  3. Click **Create instance template**.

  4. In the **Machine configuration** section, click **Advanced configurations**.

  5. From the **CPU Platform** drop-down menu, select an option.

  6. Continue with the instance template creation process.




###  gcloud 

  * When you create an instance template using the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create), provide the `--min-cpu-platform` flag:
        
        gcloud compute instance-templates create TEMPLATE_NAME \
            --min-cpu-platform="PLATFORM"

Replace the following:

    * `TEMPLATE_NAME`: the name of the instance template
    * `PLATFORM`: the friendly name of the minimum CPU platform that you want the instance to use—for example, `Intel Skylake`



###  REST 

  * Add the `minCpuPlatform` as part of your request to create a new instance template using the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates).

For example, the following instance template contains the minimum required fields for creating a new template with the addition of the `minCpuPlatform` property:
        
        {
        "name": "example-template",
        "properties": {
          "machineType": "zones/us-central1-a/machineTypes/n2d-standard-2",
          "minCpuPlatform": "AMD Milan",
          "networkInterfaces": [
            {
              "network": "global/networks/default"
            }
          ],
          "disks":
          [
            {
              "type": "PERSISTENT",
              "boot": true,
              "mode": "READ_WRITE",
              "initializeParams":
              {
                "sourceImage": "projects/debian-cloud/global/images/family/debian-13"
              }
            }
          ]
          }
        }




## What's next

  * See a list of [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms) on Compute Engine.
  * [Change the machine type for a compute instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).
  * Learn more about [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).
  * [Create and start Windows Server or SQL Server instances](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
