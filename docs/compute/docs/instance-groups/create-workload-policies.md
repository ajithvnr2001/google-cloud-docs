---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-workload-policies/
title: Create workload policies for MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:34.909054+00:00
---

# Create workload policies for MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-workload-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create workload policies for MIGs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create workload policies for managed instance groups (MIGs) that have A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D Compute Engine instances. To create a workload policy for multi-host TPU slices, see [Create a MIG with multi-host TPU slice](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-multi-host-slice#create_a_workload_policy).

A workload policy lets you specify the placement or topology for the Compute Engine instances in your MIG. For example, you can use workload policies to place compute instances closer to each other, minimizing network latency for artificial intelligence (AI), machine learning (ML), or high performance computing (HPC) workloads. To learn more about the requirements and limitations that you apply when you create workload policies, see [About workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies).

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

To get the permissions that you need to create and apply workload policies to MIGs, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and apply workload policies to MIGs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and apply workload policies to MIGs:

  * To create a workload policy: `compute.resourcePolicies.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a workload policy

To create a workload policy, use one of the following methods based on the machine series that the compute instances in your MIG use:

  * Create a workload policy for A4X Max or A4X instances

  * Create a workload policy for A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D instances




### Create a workload policy for A4X Max or A4X instances

If you apply a workload policy to A4X Max or A4X instances in a MIG, then you must specify an [accelerator topology value](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#accelerator) when you create your policy. This action helps your workloads achieve large-scale, non-blocking network performance.

To create a workload policy for A4X Max or A4X instances, select one of the following options:

###  gcloud 

To create a workload policy for A4X Max or A4X instances, use the [`gcloud compute resource-policies create workload-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/workload-policy) with the `--accelerator-topology=1x72` flag:
    
    
    gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
        --accelerator-topology=1x72 \
        --type=high-throughput \
        --region=REGION
    

Replace the following:

  * `WORKLOAD_POLICY_NAME`: the name for your workload policy.

  * `REGION`: the region where to create your workload policy. Specify a region in which you want to create the MIG, and where the machine type that you want to use is available. To review the regions in which A4X Max or A4X machine types are available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).




###  REST 

To create a workload policy for A4X Max or A4X instances, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert). In the request body, include the `acceleratorTopology` field set to `1x72`:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
    
    {
      "name": "WORKLOAD_POLICY_NAME",
      "workloadPolicy": {
        "acceleratorTopology": "1x72",
        "type": "HIGH_THROUGHPUT"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create your workload policy.

  * `REGION`: the region where to create your workload policy. Specify a region in which you want to create the MIG, and where the machine type that you want to use is available. To review the regions in which A4X Max or A4X machine types are available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * `WORKLOAD_POLICY_NAME`: the name for your workload policy.




### Create a workload policy for A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D instances

If you want to apply a workload policy to A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D instances in a MIG, then we recommend that you specify a [maximum topology distance value](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#max-distance) when you create your policy. This action helps ensure closer placement among your compute instances. However, the more compact the placement you specify, the fewer resources might be available in the zone where you want to create your compute instances.

To create a workload policy for A4, A3 Ultra, A3 Mega, or A3 High (8 GPUs) instances, select one of the following options:

###  gcloud 

To create a workload policy, use the [`gcloud compute resource-policies create workload-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/workload-policy). Based on how close you want to place compute instances in a MIG, include the following flags in the command:

  * To place your compute instances close to each other on a best-effort basis, include the `--type=high-throughput` flag:
        
        gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --type=high-throughput \
            --region=REGION
        

  * To further control the placement of your compute instances, include the `--max-topology-distance` and `--type=high-throughput` flags:
        
        gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --max-topology-distance=TOPOLOGY_DISTANCE \
            --type=high-throughput \
            --region=REGION
        




Replace the following:

  * `WORKLOAD_POLICY_NAME`: the name for your workload policy.

  * `REGION`: the region where to create your workload policy. Specify a region in which you want to create the MIG, and where the machine type that you want to use is available. To review the regions in which GPU machine types are available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * `TOPOLOGY_DISTANCE`: the maximum topology distance. A shorter maximum distance can reduce the probability of VM availability. Specify one of the following values:

    * To place A4 or H4D instances in the same cluster: `CLUSTER`

    * To place A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D instances in the same block: `BLOCK`

    * To place A4, A3 Ultra, or H4D instances in the same sub-block: `SUBBLOCK`




###  REST 

To create a workload policy, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert). Based on how close you want to place compute instances in a MIG, include the following fields in the request body:

  * To place your compute instances close to each other on a best-effort basis, include the `type` field in the request body:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
        
        {
          "name": "WORKLOAD_POLICY_NAME",
          "workloadPolicy": {
            "type": "HIGH_THROUGHPUT"
          }
        }
        

  * To further control the placement of your compute instances, include the `maxTopologyDistance` and `type` fields in the request body:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
        
        {
          "name": "WORKLOAD_POLICY_NAME",
          "workloadPolicy": {
            "maxTopologyDistance": "TOPOLOGY_DISTANCE",
            "type": "HIGH_THROUGHPUT"
          }
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create your workload policy.

  * `REGION`: the region where to create your workload policy. Specify a region in which you want to create the MIG, and where the machine type that you want to use is available. To review the regions in which GPU machine types are available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * `WORKLOAD_POLICY_NAME`: the name for your workload policy.

  * `TOPOLOGY_DISTANCE`: the maximum topology distance. A shorter maximum distance can reduce the probability of VM availability. Specify one of the following values:

    * To place A4 or H4D instances in the same cluster: `CLUSTER`

    * To place A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D instances in the same block: `BLOCK`

    * To place A4, A3 Ultra, or H4D instances in the same sub-block: `SUBBLOCK`




## What's next

  * After you create a workload policy, learn how to apply it to a MIG:

    * [Create an AI-optimized MIG with A4X Max instances](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-mig)

    * [Create an AI-optimized MIG with A4X instances](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4x)

    * [Create an AI-optimized MIG with A4 or A3 Ultra instances](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra)

    * [Create an AI-optimized MIG with A3 Mega or A3 High (8 GPUs) instances](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a3-high-mega)

    * [Create an HPC-optimized MIG with H4D instances](https://docs.cloud.google.com/compute/docs/hpc/create-mig-hpc-dense)

  * Learn how to [view compute instance topology](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology).

  * Learn how to [view workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/view-workload-policies).

  * Learn how to [replace, remove, or delete workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/manage-workload-policies).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
