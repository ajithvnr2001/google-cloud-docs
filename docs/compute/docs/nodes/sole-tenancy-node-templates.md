---
url: https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates/
title: Create sole-tenant node templates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:40.245560+00:00
---

# Create sole-tenant node templates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create sole-tenant node templates Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to create and delete sole-tenant node templates. Before creating sole-tenant node templates, review the [sole-tenant node overview](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) to learn about important concepts and terminology.

[Sole-tenant node templates](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_templates) are regional resources that specify properties for sole-tenant node groups. You must create a node template before you create a node group. 

## Create a sole-tenant node template

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeTemplates.create` on the project or organization



If you use the gcloud CLI or REST, you can create a node template resource that you can use later to create one or more node groups. If you use the Google Cloud console, you must create node templates when you create a node group.

To create a sole-tenant node template, use one of the following methods:

###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Create node group**. The process of creating a node group in the console includes creating or selecting a node template.

  3. Specify a **Name** for the node group.

  4. Specify a **Region** to create the node template in. You can use the node template to create node groups in any zone of this region.

  5. Specify the **Zone** and click **Continue**.

  6. In the **Node template** list, click **Create node template** to begin creating a sole-tenant node template.

  7. Specify a **Name** for the node template.

  8. Specify the **Node type** for each sole-tenant node in the node group to create based on this node template.

  9. Optionally, you can also specify the following properties for the node template:

     * Add a **Local SSD** and **GPU accelerator**.
     * Select **Enable CPU overcommit** to control [CPU overcommit levels](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms) for each VM scheduled on the node.
     * Add **Node affinity labels**. Affinity labels let you logically group nodes and node groups, and later, when provisioning VMs, you can specify affinity labels on the VMs to schedule VMs on a specific set of nodes or node groups. For more information, see [Node affinity and anti-affinity](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity).
  10. Click **Create** to finish creating your node template.

  11. Optional: to add a new sole-tenant node template in a different region, repeat the preceding steps.




To view the node templates, click **Node templates** in the **Sole-tenant nodes** page.

###  gcloud 

Use the [`gcloud compute sole-tenancy node-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create) to create a node template:
    
    
    gcloud compute sole-tenancy node-templates create TEMPLATE_NAME \
      --node-type=NODE_TYPE \
      [--region=REGION] \
      [--node-affinity-labels=AFFINITY_LABELS] \
      [--accelerator type=GPU_TYPE,count=GPU_COUNT] \
      [--disk type=local-ssd,count=DISK_COUNT,size=DISK_SIZE] \
      [--cpu-overcommit-type=CPU_OVERCOMMIT_TYPE]
    

Replace the following:

  * `TEMPLATE_NAME`: the name for the new node template.

  * `NODE_TYPE`: the node type for sole-tenant nodes created based on this template. Use the [`gcloud compute sole-tenancy node-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-types/list) to get a list of the node types available in each zone.

  * `REGION`: the region to create the node template in. You can use this template to create node groups in any zone of this region.

  * `AFFINITY_LABELS`: the keys and values, `[KEY=VALUE,...]`, for affinity labels. Affinity labels let you logically group nodes and node groups and later, when provisioning VMs, you can specify affinity labels on the VMs to schedule VMs on a specific set of nodes or node groups. For more information, see [Node affinity and anti-affinity](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity).

  * `GPU_TYPE`: the type of GPU for each sole-tenant node created based on this node template. For information on the zonal availability of GPUs, use the `gcloud compute accelerator-types list` command and choose a zone where either the `n1`, `g2`, `g4`, `a3-highgpu`, or `a3-megagpu` sole-tenant node type is available. Depending on the zonal availability, set to one of:

    * For A3 High: `nvidia-h100-80gb`
    * For A3 Mega: `nvidia-h100-mega-80gb`
    * For G2: `nvidia-l4`
    * For G4: `nvidia-rtx-pro-6000`
    * For N1: 
      * `nvidia-tesla-p4`
      * `nvidia-tesla-t4`
      * `nvidia-tesla-v100`
  * `GPU_COUNT`: the number of GPUs to specify depending on the type of GPU. Set to the value specified for the type of GPU as shown in the following table:

`GPU_TYPE` | `GPU_COUNT`  
---|---  
`nvidia-h100-80gb` | 8  
`nvidia-h100-mega-80gb` | 8  
`nvidia-l4` | 8  
`nvidia-rtx-pro-6000` | 8  
`nvidia-tesla-p4` | 4  
`nvidia-tesla-t4` | 4  
`nvidia-tesla-v100` | 8  
  * `DISK_COUNT`: number of Local SSD disks. Set to `16` or `24`. This parameter is not required for A3 High and A3 Mega node types because they include a fixed number of Local SSD disks.

  * `DISK_SIZE`: optional value for the partition size of the Local SSD in GB. The only supported partition size is `375`, and if you don't set this value it defaults to `375`.



  * `CPU_OVERCOMMIT_TYPE`: the overcommit type for CPUs on a VM. Set to `enabled` or `none`.



###  REST 

Use the [`nodeTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates/insert) to create a node template:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/nodeTemplates
    
    {
      "name": "TEMPLATE_NAME",
      "nodeType": "NODE_TYPE",
      "nodeAffinityLabels": {
        "KEY": "VALUE",
        ...
      },
      "accelerators": [
        {
          "acceleratorType": "GPU_TYPE",
          "acceleratorCount": GPU_COUNT
        }
      ],
      "disks": [
        {
          "diskType": "local-ssd",
          "diskSizeGb": DISK_SIZE,
          "diskCount": DISK_COUNT
        }
      ],
      "cpuOvercommitType": CPU_OVERCOMMIT_TYPE
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID.

  * `REGION`: the region to create the node template in. You can use this template to create node groups in any zone of this region.

  * `TEMPLATE_NAME`: the name for the new node template.

  * `NODE_TYPE`: the node type for sole-tenant nodes created based on this template. Use the [`nodeTypes.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeTypes/list) to get a list of the node types available in each zone.

  * `KEY`: the `nodeAffinityLabels` value that specifies the key portion of a node affinity label expressed as a key-value pair. Affinity labels let you logically group nodes and node groups, and later, when provisioning VMs, you can specify affinity labels on the VMs to schedule VMs on a specific set of nodes or node groups. For more information, see [Node affinity and anti-affinity](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity).

  * `VALUE`: the `nodeAffinityLabels` value that specifies the value portion of a node affinity label key-value pair.

  * `GPU_TYPE`: the type of GPU for each sole-tenant node created based on this node template. For information on the zonal availability of GPUs, use the `gcloud compute accelerator-types list` command and choose a zone where either the `n1`, `g2`, `g4`, `a3-highgpu`, or `a3-megagpu` sole-tenant node type is available. Depending on the zonal availability, set to one of:

    * For A3 High: `nvidia-h100-80gb`
    * For A3 Mega: `nvidia-h100-mega-80gb`
    * For G2: `nvidia-l4`
    * For G4: `nvidia-rtx-pro-6000`
    * For N1: 
      * `nvidia-tesla-p4`
      * `nvidia-tesla-t4`
      * `nvidia-tesla-v100`
  * `GPU_COUNT`: the number of GPUs for each sole-tenant node created based on this node template. Set to the value specified for the type of GPU as shown in the following table:

`GPU_TYPE` | `GPU_COUNT`  
---|---  
`nvidia-h100-80gb` | 8  
`nvidia-h100-mega-80gb` | 8  
`nvidia-l4` | 8  
`nvidia-rtx-pro-6000` | 8  
`nvidia-tesla-p4` | 4  
`nvidia-tesla-t4` | 4  
`nvidia-tesla-v100` | 8  
  * `DISK_SIZE`: optional value for the partition size of the Local SSD in GB. The only supported partition size is `375`, and if you don't set this value it defaults to `375`.

  * `DISK_COUNT`: number of Local SSD disks. Set to `16` or `24`. This parameter is not required for A3 High and A3 Mega node types because they include a fixed number of Local SSD disks.

  * `CPU_OVERCOMMIT_TYPE`: CPU overcommit type. Set to `enabled`, `none`, or `CPU_OVERCOMMIT_TYPE_UNSPECIFIED`.




## Delete a node template

You can delete a node template after you've deleted all of the node groups that are using the template.

###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Node templates**.

  3. Select the name of an unused node template.

  4. Click **Delete**.




###  gcloud 

Use the [`gcloud compute sole-tenancy node-templates delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/delete) to delete an unused node template:
    
    
    gcloud compute sole-tenancy node-templates delete TEMPLATE_NAME \
      --region=REGION
    

Replace the following:

  * TEMPLATE_NAME: the name of the node template to delete

  * REGION: the region of the node template




###  REST 

Use the [`compute.nodeTemplates.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeTemplates/delete) to delete an unused node template:
    
    
     DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/nodeTemplates/TEMPLATE_NAME
     

Replace the following:

  * PROJECT_ID: your project ID

  * REGION: the Google Cloud region that contains the node template

  * TEMPLATE_NAME: the name of the node template to delete




## What's next

  * [Create sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-groups).

  * [Provision VMs on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms).



  * For information about sole-tenant node pricing, see [Sole-tenant nodes pricing](https://cloud.google.com/compute/sole-tenant-pricing).


  * For information about how to enable autoscaling on sole-tenant node groups, see [Node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups).

  * For more information about bringing existing licenses to Google Cloud, see [Bring existing licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses).

  * For more information about sole-tenant nodes, see [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
