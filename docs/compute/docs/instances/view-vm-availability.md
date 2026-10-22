---
url: https://docs.cloud.google.com/compute/docs/instances/view-vm-availability/
title: View the availability of Spot VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:57.648492+00:00
---

# View the availability of Spot VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-vm-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View the availability of Spot VMs Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to view the real-time availability and expected uptime for Spot VMs.

Before you create [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), you can view real-time availability and expected uptime across multiple machine types and locations by using the `advice.capacity` API. This information helps you do the following:

  * **Reduce resource availability errors**. When you see which machine types regions, or zones have available capacity, you can specify those configurations when you create Spot VMs. This action reduces your chances of encountering resource availability errors.

  * **Optimize workloads for preemption**. By comparing the expected uptime across different machine configurations and locations, you can choose the configurations that best fit your workloads. Checking these factors let you design and organize your Spot VMs so that preemption doesn't disrupt your workloads.




To learn how to compare stability and cost across different machine types and locations, see instead [View the preemption rate and pricing for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price).

## Limitations

When you send a request to the `advice.capacity` API, you can't view the availability of TPUs.

## Understand viewing resource availability for Spot VMs

When you send a request to the `advice.capacity` API, the output shows the following recommendation metrics. These metrics are based on the machine type that you want your Spot VMs to use, the zone where you want to create Spot VMs, and the real-time availability and historical preemption rates of your requested resources.

  * **Obtainability score** : the likelihood that your creation request for Spot VMs with your specified number of VMs and machine configuration succeeds. For more information, see Obtainability score for Spot VMs.

  * **Estimated uptime** : the minimum amount of time that you can expect most of your Spot VMs to run before Compute Engine preempts them. For more information, see Estimated uptime for Spot VMs.




### Obtainability score for Spot VMs

When you send a request to the `advice.capacity` API, the _obtainability score_ (`obtainability`) in the output indicates the likelihood that you can successfully create your specified number of Spot VMs in one or more zones. Compute Engine calculates this score based on the real-time availability of your requested resources and the success rate of recent creation requests.

**Caution:** Obtainability scores don't guarantee capacity. Between when you receive recommendations and when you create your VMs, resources might become unavailable.

The obtainability score ranges from `0.0` to `1.0`, and it indicates one of the following success chances:

  * **High success chances (`0.7` to `1.0`)**: you're highly likely to create your requested Spot VMs.

  * **Medium success chances (`0.4` to `0.6`)**: you're moderately likely to create your requested Spot VMs. If you create Spot VMs in bulk or in a MIG with a target size, then you might obtain only part of your requested VMs.

  * **Low success chances (`0.0` to `0.3`)**: you're unlikely to create your requested Spot VMs. We recommend that you check for resource availability in a different location or for a different machine type, or that you create VMs by using a different [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




### Estimated uptime for Spot VMs

When you send a request to the `advice.capacity` API, the _estimated uptime_ (`estimatedUptime`) in the output indicates the minimum time that most of your specified number of Spot VMs are expected to run before preemption. Compute Engine calculates this uptime based on historical and current usage patterns for your specified machine type and location.

**Caution:** Estimated uptimes don't guarantee uptime. The Spot VMs that you create might run for a longer or shorter duration than estimated before Compute Engine preempts them. If you want to limit the run time of a Spot VM to prevent unnecessary charges, then see [Limit the run time of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime).

Compute Engine can set the estimated uptime to one of the following values:

  * **60 minutes (3,600 seconds)** : most of your Spot VMs will likely run for an hour before Compute Engine preempts them. Create VMs for long-running workloads that can tolerate interruptions, such as batch workloads.

  * **10 minutes (600 seconds)** : most of your Spot VMs will likely run for 10 minutes before Compute Engine preempts them. Create VMs only for short-running tasks or for fault-tolerant workloads that save their progress at short intervals.

  * **1 minute (60 seconds)** : most of your Spot VMs will likely run for one minute before Compute Engine preempts them. We recommend that you do one of the following:

    * Create VMs only for very short tasks, testing, or non-critical workloads.

    * Check for resource availability in a different location or for a different machine type.

    * Create VMs by using a different [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




## Best practices

To maximize your chances of obtaining capacity after you use the `advice.capacity` API, we recommend the following best practices:

  * **Compare outputs across different machine types** : if your workload is flexible, then compare options with a different number of Spot VMs or machine types. For example, you can compare the output for 100 VMs with an `n1-standard-2` machine type and 50 VMs with an `n1-standard-4` machine type. Then, you can create Spot VMs by using the configuration that best balances obtainability and estimated uptime for your workload needs.

  * **Compare outputs across multiple locations** : if your workload can run in multiple regions or zones, then check the availability in each location. For example, if two regions offer the same estimated uptime, create Spot VMs in the region with the higher obtainability score.

  * **Distribute VMs across multiple zones** : if you specify a [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape) of `ANY` or `BALANCED`, then the `advice.capacity` API might recommend that you create Spot VMs across multiple zones. For example, to maximize your chances of creating 100 Spot VMs, the output might recommend you to create 90 VMs in one zone and 10 VMs in another zone.




## Before you begin

  * The `advice.capacity` API includes [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) by default in its availability and expected uptime recommendations. To help ensure that you can create Spot VMs in AI zones if the API recommends that you create VMs in one of these zones, [ verify that AI zones are enabled for your project](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#check-ai-zone-status).
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

To get the permissions that you need to view the availability of Spot VMs, ask your administrator to grant you the [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view the availability of Spot VMs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view the availability of Spot VMs:

  * To view the availability of Spot VMs: `compute.advice.capacity` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View the availability of Spot VMs

To view the availability of Spot VMs, you must specify the location, machine configuration, and the number of VMs that you want to create. Based on the results, you can either create the Spot VMs, or view resource availability in another location or for another machine configuration.

Depending on your workload requirements, consider the following:

  * To view availability across multiple machine series, machine types, and regions or zones simultaneously, use the Google Cloud console.

  * To view availability for [target distribution shapes in a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape), use the gcloud CLI or REST API.

  * To view availability for N1 GPU VMs or [Local SSD disks that aren't attached to a machine type by default](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options), use the REST API.




To view the availability of Spot VMs, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Capacity advisor** page.

[Go to Capacity advisor](https://console.cloud.google.com/compute/capacityAdvisor)

  2. In the **Filters** pane, complete the following steps:

     1. In **Location** section, in the **Region** list, select the regions where you want to view the availability of Spot VMs.

     2. In the **Machine specifications** section, specify the machine configuration and number of Spot VMs that you want to view the availability of:

        1. In the **Machine family** list, select a [machine family](https://docs.cloud.google.com/compute/docs/machine-resource).

        2. In the **Series** list, select up to three machine series.

        3. In the **Machine type** list, select up to five machine types.

        4. In the **Number of VMs** field, enter the number of Spot VMs.

        5. Optional: By default, zones that have limited resources available are hidden. To view these zones, clear the **Hide regions with limited availability** checkbox.

     3. Click search **Search**.




###  gcloud 

To view the availability of Spot VMs, use the [`gcloud beta compute advice capacity` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/advice/capacity):
    
    
    gcloud beta compute advice capacity \
        --provisioning-model=SPOT \
        --instance-selection-machine-types=MACHINE_TYPES \
        --target-distribution-shape=TARGET_DISTRIBUTION_SHAPE \
        --size=SIZE \
        --region=REGION
    

Replace the following:

  * `MACHINE_TYPES`: a comma-separated list of machine types for which you want to view availability—for example, `n2-standard-2,n2-standard-4`. You can specify up to five machine types.

  * `TARGET_DISTRIBUTION_SHAPE`: the distribution of your requested resources. Based on the type of workload that you want to run and the zones in which you want to create VMs, specify one of the following values:

    * **`ANY`** : you want to create Spot VMs in one or more zones based on availability. Specify this value for batch workloads.

    * **`ANY_SINGLE_ZONE`** : you want to create Spot VMs only in a single zone based on availability. Specify this value for workloads that require extensive communication among VMs, such as AI or high performance computing (HPC) workloads.

    * **`BALANCED`** : you want to create Spot VMs in one or more zones based on availability, and Compute Engine to distribute VMs as evenly as possible across zones. Specify this value to minimize the impact of zonal failures for highly available serving or batch workloads.

  * `SIZE`: the number of Spot VMs that you want to create.

  * `REGION`: the region where you want to view the availability of Spot VMs. To specify a comma-separated list of zones instead of a region, replace the `--region` flag with the [`--zones` flag](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/advice/capacity#--zones).




The output is similar to the following:
    
    
    recommendations:
    - scores:
      obtainability: 0.9
      estimatedUptime: 600s
    - shards:
      - instanceCount: 90
        machineType: n2-standard-2
        provisioningModel: SPOT
        zone: https://compute.googleapis.com/compute/beta/projects/example-project/zones/us-central1-a
      - instanceCount: 10
        machineType: n2-standard-4
        provisioningModel: SPOT
        zone: https://compute.googleapis.com/compute/beta/projects/example-project/zones/us-central1-c
    

###  REST 

To view the availability of Spot VMs, make a `POST` request to the [beta `advice.capacity` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/advice/capacity).

For example, to view the availability for two machine types in a region, make a request as follows. You can view availability for up to five machine types per request.
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/advice/capacity
    
    {
      "instanceProperties": {
        "scheduling": {
          "provisioningModel": "SPOT"
        }
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "MACHINE_SELECTION_1": {
            "machineTypes": [
              "MACHINE_TYPE_1"
            ]
          },
          "MACHINE_SELECTION_2": {
            "machineTypes": [
              "MACHINE_TYPE_2"
            ]
          }
        }
      },
      "distributionPolicy": {
        "targetShape": "TARGET_DISTRIBUTION_SHAPE"
      },
      "size": SIZE
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `REGION`: the region where you want to view the availability of Spot VMs. If you want to view availability only in specific zones within your specified region, then include the [`distributionPolicy.zones` array field](https://docs.cloud.google.com/compute/docs/reference/rest/beta/advice/capacity#request-body) in the request body. For example, to view the availability of Spot VMs in two zones, add the `zones` array to the `distributionPolicy` field as follows:
        
        "zones": [
          {
            "zone": "zones/ZONE_1"
          },
          {
            "zone": "zones/ZONE_2"
          }
        ]
        

Replace `ZONE_1` and `ZONE_2` with the two zones where you want to view the availability of Spot VMs.

  * `MACHINE_SELECTION_1` and `MACHINE_SELECTION_2`: a name for the machine type selection. For example, specify `selection-1` and `selection-2` respectively.

  * `MACHINE_TYPE_1` and `MACHINE_TYPE_2`: the machine types for which you want to view availability. Depending on the machine type, note the following:

    * **N1 machine types** : to attach GPUs to your N1 Spot VMs, include the `guestAccelerators` field in the `MACHINE_SELECTION_1` or `MACHINE_SELECTION_2` fields as follows:
          
          "guestAccelerators": [
            {
              "acceleratorCount": ACCELERATOR_COUNT,
              "acceleratorType": "ACCELERATOR_TYPE"
            }
          ]
          

Replace the following:

      * `ACCELERATOR_COUNT`: the number of GPUs to attach to your N1 Spot VMs.

      * `ACCELERATOR_TYPE`: a [GPU model that supports the N1 machine series](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus).

    * **Machine types without default Local SSD disks** : to attach Local SSD disks to your Spot VMs, include the `disks` field in the `MACHINE_SELECTION_1` or `MACHINE_SELECTION_2` fields. For each Local SSD disk that you want to attach, repeat the `type` field and set it to `SCRATCH`. For example, to attach two Local SSD disks, include the following:
          
          "disks": [
            {
              "type": "SCRATCH"
            },
            {
              "type": "SCRATCH"
            }
          ]
          

  * `TARGET_DISTRIBUTION_SHAPE`: the distribution of your requested resources. Based on the type of workload that you want to run and the zones in which you want to create VMs, specify one of the following values:

    * **`ANY`** : you want to create Spot VMs in one or more zones based on availability. Specify this value for batch workloads.

    * **`ANY_SINGLE_ZONE`** : you want to create Spot VMs only in a single zone based on availability. Specify this value for workloads that require extensive communication among VMs, such as AI or HPC workloads.

    * **`BALANCED`** : you want to create Spot VMs in one or more zones based on availability, and Compute Engine distributes VMs as evenly as possible across zones. Specify this value to minimize the impact of zonal failures for highly available serving or batch workloads.

  * `SIZE`: the number of Spot VMs that you want to create.




The output is similar to the following:
    
    
    {
      "recommendations": [
        {
          "scores": {
            "estimatedUptime": "600s",
            "obtainability": 0.9
          },
          "shards": [
            {
              "instanceCount": 90,
              "machineType": "n2-standard-2",
              "provisioningModel": "SPOT",
              "zone": "https://compute.googleapis.com/compute/beta/projects/example-project/zones/us-central1-a"
            },
            {
              "instanceCount": 10,
              "machineType": "n2-standard-4",
              "provisioningModel": "SPOT",
              "zone": "https://compute.googleapis.com/compute/beta/projects/example-project/zones/us-central1-c"
            }
          ]
        }
      ]
    }
    

## What's next

  * Learn how to [create and use Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot).

  * Learn more about the [best practices for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
