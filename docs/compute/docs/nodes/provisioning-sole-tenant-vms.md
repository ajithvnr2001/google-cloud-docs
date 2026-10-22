---
url: https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms/
title: Provision VMs on sole-tenant nodes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:14.794644+00:00
---

# Provision VMs on sole-tenant nodes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Provision VMs on sole-tenant nodes Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page describes how to provision VMs on sole-tenant nodes, which are physical servers that run VMs only from a single project. Before provisioning VMs on sole-tenant nodes, read the [sole-tenant node overview](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

## Before you begin

  * Before provisioning VMs on sole-tenant nodes, [check your quota](https://docs.cloud.google.com/compute/quotas-limits#check_your_allocation_quota). Depending on the number and size of nodes that you reserve, you might need to [request additional quota](https://docs.cloud.google.com/compute/quotas-limits#edit_your_quota). 
  * [Create a sole-tenant node template](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates). 
  * [Create a sole-tenant node group](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-groups). 
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




## Create a sole-tenant node template

[Sole-tenant node templates](https://docs.cloud.google.com/compute/docs/nodes#node_templates_and_node_types) are regional resources that specify properties for sole-tenant node groups. You must create a node template before you create a node group. However, if you're using the Google Cloud console, you must create node templates during the creation of a sole-tenant node group.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeTemplates.create` on the project or organization



###  Console 

You must create a sole-tenant node template before you create a node group. By using the Google Cloud console, you must create the node template during the creation of a sole-tenant node group. The new node template is created in the same region that you specify in the node group properties.

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Create node group**.

  3. Specify a **Name** for the node group.

  4. Specify a **Region** to create the node template in. You can use the node template to create node groups in any zone of this region.

  5. Specify the **Zone** and click **Continue**.

  6. In the **Node template** list, click **Create node template** to begin creating a sole-tenant node template.

  7. Specify a **Name** for the node template.

  8. Specify the **Node type** for each sole-tenant node in the node group to create based on this node template.

  9. Optional: you can also specify the following properties for the node template.

     * Add a **local SSD** and **GPU accelerator**.
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

  * `GPU_TYPE`: the type of GPU for each sole-tenant node created based on this node template. For information on the zonal availability of the required sole-tenant node type, use the [`gcloud compute sole-tenancy node-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-types/list). For example, to see zones for `a2-highgpu` node types, add the flag `--filter="name~'a2-highgpu'"`. For the GPU and node types available, see the table in the `GPU_COUNT` description.

  * `GPU_COUNT`: the number of GPUs to attach to each sole-tenant node. The value for `GPU_COUNT` depends on the `GPU_TYPE` and the sole-tenant node type. Set `GPU_COUNT` to the value shown in the following table:

Node type | `GPU_TYPE` | `GPU_COUNT`  
---|---|---  
`a2-highgpu` | `nvidia-tesla-a100` | 8  
`a2-megagpu` | `nvidia-tesla-a100` | 16  
`a2-ultragpu` | `nvidia-a100-80gb` | 8  
`a3-highgpu` | `nvidia-h100-80gb` | 8  
`a3-megagpu` | `nvidia-h100-mega-80gb` | 8  
`g2` | `nvidia-l4` | 8  
`g4` | `nvidia-rtx-pro-6000` | 8  
`n1` | `nvidia-tesla-p4` | 4  
`n1` | `nvidia-tesla-t4` | 4  
`n1` | `nvidia-tesla-v100` | 8  
  * `DISK_COUNT`: number of Local SSD disks. Set to `16` or `24`. This parameter is not required for A2 Ultra, A3 High, and A3 Mega node types because they include a fixed number of Local SSD disks.

  * `DISK_SIZE`: optional value for the partition size of the local SSD in GB. The only supported partition size is `375`, and if you do not set this value it defaults to `375`.



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

  * `GPU_TYPE`: the type of GPU for each sole-tenant node created based on this node template. For information on the zonal availability of the required sole-tenant node type, use the [`nodeTypes.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeTypes/list). For example, to see zones for `a2-highgpu` node types, use the filter `name~"a2-highgpu.*"`. For the GPU and node types available, see the table in the `GPU_COUNT` description.

  * `GPU_COUNT`: the number of GPUs for each sole-tenant node created based on this node template. The value for `GPU_COUNT` depends on the `GPU_TYPE` and the sole-tenant node type. Set `GPU_COUNT` to the value shown in the following table:

Node type | `GPU_TYPE` | `GPU_COUNT`  
---|---|---  
`a2-highgpu` | `nvidia-tesla-a100` | 8  
`a2-megagpu` | `nvidia-tesla-a100` | 16  
`a2-ultragpu` | `nvidia-a100-80gb` | 8  
`a3-highgpu` | `nvidia-h100-80gb` | 8  
`a3-megagpu` | `nvidia-h100-mega-80gb` | 8  
`g2` | `nvidia-l4` | 8  
`g4` | `nvidia-rtx-pro-6000` | 8  
`n1` | `nvidia-tesla-p4` | 4  
`n1` | `nvidia-tesla-t4` | 4  
`n1` | `nvidia-tesla-v100` | 8  
  * `DISK_SIZE`: optional value for the partition size of the local SSD in GB. The only supported partition size is `375`, and if you don't set this value it defaults to `375`.

  * `DISK_COUNT`: number of Local SSD disks. Set to `16` or `24`. This parameter is not required for A3 High and A3 Mega node types because they include a fixed number of Local SSD disks.

  * `CPU_OVERCOMMIT_TYPE`: CPU overcommit type. Set to `enabled`, `none`, or `CPU_OVERCOMMIT_TYPE_UNSPECIFIED`.




## Create a sole-tenant node group

With the previously created sole-tenant node template, create a sole-tenant node group. A sole-tenant node group inherits properties specified by the sole-tenant node template and has additional values that you must specify.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeTemplates.use` on the node template
  * `compute.nodeGroups.create` on the project or organization



###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Create node group** to begin creating a node group.

  3. Specify a **Name** for the node group.

  4. Specify the **Region** for the node group to display the available node templates in that region.

  5. Specify the **Zone** within the region to create the node group in.

  6. Specify the **Node template** to create the node group or click **Create node template** to create a new sole-tenant node template. The selected node template is applied to the node group.

  7. Choose one of the following for the **Autoscaling mode** for the [node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups):

     * **Off** : Manually manage the size of the node group.

     * **On** : Have nodes automatically added to or removed from the node group.

     * **Only scale out** : Add nodes to the node group when extra capacity is required.

  8. Specify the **Number of nodes** for the group. If you enable the [node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups), specify a range for the size of the node group. You can manually change the values later.

  9. Set the **Maintenance policy** of the sole-tenant node group in the **Configure Maintenance Settings** section to one of the following values. The maintenance policy lets you configure the behavior of VMs on the node group during host maintenance events. For more information, see [Maintenance policies](https://docs.cloud.google.com/compute/docs/nodes#maintenance_policies).

     * **Default**
     * **Restart in place**
     * **Migrate within node group**
  10. You can choose between _regular maintenance windows_ and _advanced maintenance control_ to handle maintenance for your sole-tenant node group, as follows:

     * **Maintenance Window:** Select the time period during which you want planned maintenance events to happen for the nodes in the sole-tenant node groups.

     * **Opt-in for advanced maintenance control for sole-tenancy:** [Advanced maintenance control for sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control#opt-in) lets you control planned maintenance events for sole-tenant node groups and minimize maintenance-related disruptions. To opt-in for advanced maintenance control, click the **Opt-in for advanced maintenance control for sole-tenancy** toggle to the _on_ position. If you choose to use this option for node maintenance, the **Maintenance window** field is disabled, and maintenance occurs as configured in advanced maintenance control.

Note that advanced maintenance control only supports the _Default_ maintenance policy.

  11. Configure the share settings by specifying one of the following in **Configure share settings** :

     * To share the node group with all projects in your organization, choose **Share this node group with all projects within the organization**.
     * To share the node group with specific projects within your organization, choose **Share this node group with selected projects within the organization**.

If you do not want to share the node group, choose **Do not share this node group with other projects**. For more information about sharing node groups, see [Share sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups).

  12. Click **Create** to finish creating the node group.




###  gcloud 

Run the [`gcloud compute sole-tenancy node-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create) command to create a node group based on a previously created node template:
    
    
    gcloud compute sole-tenancy node-groups create GROUP_NAME \
      --node-template=TEMPLATE_NAME \
      --target-size=TARGET_SIZE \
      [--zone=ZONE] \
      [--maintenance-policy=MAINTENANCE_POLICY] \
      [--maintenance-window-start-time=START_TIME] \
      [--autoscaler-mode=AUTOSCALER_MODE \
      --min-nodes=MIN_NODES \
      --max-nodes=MAX_NODES]
    

Replace the following:

  * `GROUP_NAME`: the name for the new node group.

  * `TEMPLATE_NAME`: the name of the node template to use to create this group.

  * `TARGET_SIZE`: the number of nodes to create in the group.

  * `ZONE`: the zone to create the node group in. This must be the same region as the node template on which you are basing the node group.

  * `MAINTENANCE_POLICY`: the maintenance policy for the node group. For more information, see [Maintenance policies](https://docs.cloud.google.com/compute/docs/nodes#maintenance_policies). This must be one of the following values:

    * `default`
    * `restart-in-place`
    * `migrate-within-node-group`

Alternately, you can opt in for advanced maintenance control for the sole-tenant node group, using the `--maintenance-interval` flag. For more information, see [Enable advanced maintenance control on a sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control#opt-in).

  * `START_TIME`: the start time in GMT for the maintenance window for the VMs in this node group. Set to one of: `00:00`, `04:00`, `08:00`, `12:00`, `16:00`, or `20:00`. If not set, the node group does not have a set maintenance window.

  * `AUTOSCALER_MODE`: the autoscaler policy for the node group. This must be one of:

    * `off`: manually manage the size of the node group.

    * `on`: have nodes automatically added to or removed from the node group.

    * `only-scale-out`: add nodes to the node group when extra capacity is required.

  * `MIN_NODES`: the minimum size of the node group. The default value is `0` and must be an integer value less than or equal to `MAX_NODES`.

  * `MAX_NODES`: the maximum size of the node group. This must be less than or equal to `100` and greater than or equal to `MIN_NODES`. Required if `AUTOSCALER_MODE` is not set to `off`.




###  REST 

Use the [`nodeGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/insert) to create a node group based on a previously created node template:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/nodeGroups?initialNodeCount=TARGET_SIZE  
    
    {
      "nodeTemplate": "regions/REGION/nodeTemplates/TEMPLATE_NAME",
      "name": "GROUP_NAME",
      "maintenancePolicy": MAINTENANCE_POLICY,
      "maintenanceWindow": {
          "startTime": "START_TIME"
      }
      "autoscalingPolicy": {
          "mode": AUTOSCALER_MODE,
          "minNodes": MIN_NODES,
          "maxNodes": MAX_NODES
      },
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID.

  * `ZONE`: the zone to create the node group in. This must be in the same region as the node template on which you are basing the node group.

  * `TARGET_SIZE`: the number of nodes to create in the group.

  * `REGION`: the region to create the node group in. You must have a node template in the selected region.

  * `TEMPLATE_NAME`: the name of the node template to use to create this group.

  * `GROUP_NAME`: the name for the new node group.

  * `MAINTENANCE_POLICY`: the [maintenance policy](https://docs.cloud.google.com/compute/docs/nodes#maintenance_policies) for the node group. This must be one of the following values:

    * `DEFAULT`
    * `RESTART_IN_PLACE`
    * `MIGRATE_WITHIN_NODE_GROUP`

Alternately, you can opt-in for advanced maintenance control for the sole-tenant node group, using the `maintenanceInterval` field. For more information, see [Enable advanced maintenance control on a sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control#opt-in).

  * `START_TIME`: the start time in GMT for the maintenance window for the VMs in this node group. Set to one of: `00:00`, `04:00`, `08:00`, `12:00`, `16:00`, or `20:00`. If not set, the node group does not have a set maintenance window.

  * `AUTOSCALER_MODE`: the autoscaler policy for the node group. This must be one of the following values:

    * `OFF`: manually manage the size of the node group.

    * `ON`: have nodes automatically added to or removed from the node group.

    * `ONLY_SCALE_OUT`: add nodes to the node group when extra capacity is required.

  * `MIN_NODES`: the minimum size of the node group. The default is `0` and must be an integer value less than or equal to `MAX_NODES`.

  * `MAX_NODES`: the maximum size of the node group. This must be less than or equal to `100` and greater than or equal to `MIN_NODES`. Required if `AUTOSCALER_MODE` is not set to `OFF`.




## Provision a sole-tenant VM

After creating a node group based on a previously created node template, you can provision individual VMs on a sole-tenant node group.

To provision a VM on a specific node or node group that has affinity labels that match those you previously assigned to the node template, follow the [standard procedure for creating a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance), and assign [affinity labels](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity) to the VM.

Or, you can use the following procedure to provision a VM on a sole-tenant node from the node group details page. Based on the node group that you provision VMs on, Compute Engine assigns [affinity labels](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity).

###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Node groups**.

  3. Click the **Name** of the node group to provision a VM instance on, and then optionally, to provision a VM on a specific sole-tenant node, click the name of the specific sole-tenant node to provision the VM.

  4. Click **Create instance** to provision a VM instance on this node group, note the values automatically applied for the **Name** , **Region** , and **Zone** , and modify those values as necessary.

  5. Select a **Machine configuration** by specifying the **Machine family** , **Series** , and **Machine type**. Choose the **Series** that corresponds to the [sole-tenant node type](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types).

  6. Modify the **Boot disk** , **Firewall** , and other settings as necessary.

  7. Click **Sole Tenancy** , note the automatically assigned **Node affinity labels** , and use **Browse** to adjust as necessary.

  8. Click **Management** , and for **On host maintenance** , choose one of the following:

     * **Migrate VM instance (recommended)** : VM migrated to another node in the node group during maintenance events.

     * **Terminate** : VM stopped during maintenance events.

  9. Choose one of the following for the **Automatic restart** :

     * **On (recommended)** : Automatically restarts VMs if they are stopped for maintenance events.

     * **Off** : Does not automatically restart VMs after a maintenance event.

  10. Click **Create** to finish creating your sole-tenant VM.




###  gcloud 

Use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) command to provision a VM on a sole-tenant node group:
    
    
    gcloud compute instances create VM_NAME \
      [--zone=ZONE \]
      --image-family=IMAGE_FAMILY \
      --image-project=IMAGE_PROJECT \
      --node-group=GROUP_NAME \
      --machine-type=MACHINE_TYPE \
      [--maintenance-policy=MAINTENANCE_POLICY \]
      [--accelerator type=GPU_TYPE,count=GPU_COUNT \]
      [--local-ssd interface=SSD_INTERFACE \]
      [--restart-on-failure]
    

The `--restart-on-failure` flag indicates whether sole-tenant VMs restart after stopping. This flag is enabled by default. Use `--no-restart-on-failure` to disable.

Replace the following:

  * `VM_NAME`: the name of the new sole-tenant VM.

  * `ZONE`: the zone to provision the sole-tenant VM in.

  * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the image to use to create the VM.

  * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details) of the image family.

  * `GROUP_NAME`: the name of the node group to provision the VM on.

  * `MACHINE_TYPE`: the machine type of the sole-tenant VM. Use the [`gcloud compute machine-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-types/list) to get a list of available machine types for the project.

  * `MAINTENANCE_POLICY`: specifies restart behavior of sole-tenant VMs during maintenance events. Set to one of the following:

    * `MIGRATE`: VM migrated to another node in the node group during maintenance events.

    * `TERMINATE`: VM stopped during maintenance events.

  * `GPU_TYPE`: type of GPU. Set to one of the accelerator types specified when the node template was created.

  * `GPU_COUNT`: number of GPUs of the total specified by the node template to attach to this VM. Default value is `1`.

  * `SSD_INTERFACE`: type of local SSD interface. You can only set this for instances created from a node template with local SSD support. If you specify this while creating the instance, and the node template does not support local SSD, instance creation fails. Set to `nvme` if the boot disk image drivers are optimized for NVMe, otherwise set to `scsi`. Specify this flag and a corresponding value once for each local SSD partition.




###  REST 

Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to provision a VM on a sole-tenant node group:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/VM_ZONE/instances  
    
    {
      "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
      "name": "VM_NAME",
      "scheduling": {
        "onHostMaintenance": MAINTENANCE_POLICY,
        "automaticRestart": RESTART_ON_FAILURE,
        "nodeAffinities": [
          {
            "key": "compute.googleapis.com/node-group-name",
            "operator": "IN",
            "values": [
              "GROUP_NAME"
            ]
          }
        ]
      },
      "networkInterfaces": [
        {
          "network": "global/networks/NETWORK",
          "subnetwork": "regions/REGION/subnetworks/SUBNETWORK"
        }
      ],
      "guestAccelerators": [
        {
          "acceleratorType": GPU_TYPE,
          "acceleratorCount": GPU_COUNT
        }
      ],
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
          }
        },
        {
          "type":"SCRATCH",
          "initializeParams":{
            "diskType":"zones/LOCAL_SSD_ZONE/diskTypes/local-ssd"
          },
          "autoDelete":true,
          "interface":"SSD_INTERFACE"
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID.

  * `VM_ZONE`: the zone to provision the sole-tenant VM in.

  * `MACHINE_TYPE_ZONE`: the zone of the machine type.

  * `MACHINE_TYPE`: the machine type of the sole-tenant VM. Use the [`machineTypes.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/machineTypes/list) to get a list of available machine types for the project.

  * `VM_NAME`: the name of the new sole-tenant VM.

  * `MAINTENANCE_POLICY`: specifies restart behavior of sole-tenant VMs during maintenance events. Set to one of the following:

    * `MIGRATE`: VM migrated to another node in the node group during maintenance events.

    * `TERMINATE`: VM stopped during maintenance events.

  * `RESTART_ON_FAILURE`: indicates whether sole-tenant VMs restart after stopping. Default is `true`.

  * `GROUP_NAME`: the name of the node group to provision the VM on.

  * `NETWORK`: the URL of the network resource for this VM.

  * `REGION`: the region containing the subnetwork for this VM.

  * `SUBNETWORK`: the URL of the subnetwork resource for this VM.

  * `GPU_TYPE`: the type of GPU. Set to one of the accelerator types specified when the node template was created.

  * `GPU_COUNT`: the number of GPUs of the total specified by the node template to attach to this VM. Default value is `1`.

  * `IMAGE_PROJECT`: [image project](https://docs.cloud.google.com/compute/docs/images/os-details) of the image family.

  * `IMAGE_FAMILY`: [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the image to use to create the VM.

  * `LOCAL_SSD_ZONE`: the local SSD's zone.

  * `SSD_INTERFACE`: the type of local SSD interface. Set to `NVME` if the boot disk image drivers are optimized for NVMe, otherwise set to `SCSI`.




## Provision a group of sole-tenant VMs

[Managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups) let you provision a group of identical sole-tenant VMs. [Affinity labels](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity) let you specify the sole-tenant node or node group on which to provision the group of sole-tenant VMs.

For regional MIGs, you must create node groups in each of the regional MIG's zones and you must specify node affinities for those node groups in the regional MIG's instance template.

**Warning:** For regional MIGs, you must set the MIG's [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape) to `EVEN`. If you use a different shape, the MIG's VMs might not be created in your sole-tenant nodes.

###  gcloud 

  1. Use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) to create a managed instance group template for a group of VMs to create on a sole-tenant node group:
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE \
           --machine-type=MACHINE_TYPE \
           --image-project=IMAGE_PROJECT \
           --image-family=IMAGE_FAMILY \
           --node-group=GROUP_NAME \
           [--accelerator type=GPU_TYPE,count=GPU_COUNT \]
           [--local-ssd interface=SSD_INTERFACE]
         

Replace the following:

     * `INSTANCE_TEMPLATE`: the name for the new instance template.

     * `MACHINE_TYPE`: the machine type of the sole-tenant VM. Use the [`gcloud compute machine-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/machine-types/list) to get a list of available machine types for the project.

     * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details) of the image family.

     * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the image to use to create the VM.

     * `GROUP_NAME`: the name of the node group to provision the VM on. Alternatively, if you want to use this instance template to create a regional MIG that exists in more than one zone, use the [`--node-affinity-file` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--node-affinity-file) to specify a list of values for the regional MIG's node groups.

     * `GPU_TYPE`: type of GPU. Set to one of the accelerator types specified when the node template was created.

     * `GPU_COUNT`: number of GPUs of the total specified by the node template to attach to this VM. Default value is `1`.

     * `SSD_INTERFACE`: type of local SSD interface. Set to `nvme` if the boot disk image drivers are optimized for NVMe, otherwise set to `scsi`. Specify this flag and a corresponding value once for each local SSD partition.

  2. Use the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) command to create a managed instance group within your sole-tenant node group:
         
         gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
           --size=SIZE \
           --template=INSTANCE_TEMPLATE \
           --zone=ZONE
         

Replace the following:

     * `INSTANCE_GROUP_NAME`: the name for this instance group.

     * `SIZE`: the number of VMs to include in this instance group. Your node group must have enough resources to accommodate the instances in this managed instance group. Use the [managed instance group autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler) to automatically manage the size of managed instance groups.

     * `INSTANCE_TEMPLATE`: the name of the instance template to use to create this MIG. The template must have one or more [node affinity labels](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity) pointing to the appropriate node groups.

     * `ZONE`: the zone to create the managed instance group in. For a regional MIG, replace the `--zone` flag with the `--region` flag and specify a region; also add the `--zones` flag to specify all of the zones where the node groups exist.




###  REST 

  1. Use the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert) to create a managed instance group template within your sole-tenant node group:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/TEMPLATE_ZONE/instance-templates
         {
           "name": "INSTANCE_TEMPLATE",
           "properties": {
             "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
             "scheduling": {
               "nodeAffinities": [
                 {
                   "key": "compute.googleapis.com/node-group-name",
                   "operator": "IN",
                   "values": [
                     "GROUP_NAME"
                   ]
                 }
               ]
             },
             "networkInterfaces": [
               {
                 "network": "global/networks/NETWORK",
                 "subnetwork": "regions/REGION/subnetworks/SUBNETWORK"
               }
             ],
             "guestAccelerators": [
               {
                 "acceleratorType": GPU_TYPE,
                 "acceleratorCount": GPU_COUNT
               }
             ],
             "disks": [
               {
                 "boot": true,
                 "initializeParams": {
                   "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
                 }
               },
               {
                 "type":"SCRATCH",
                 "initializeParams":{
                   "diskType":"zones/LOCAL_SSD_ZONE/diskTypes/local-ssd"
                   },
                 "autoDelete":true,
                 "interface":"SSD_INTERFACE"
               }
             ]
           }
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID.

     * `TEMPLATE_ZONE`: the zone to create the instance template in.

     * `INSTANCE_TEMPLATE`: the name of the new instance template.

     * `MACHINE_TYPE_ZONE`: the zone of the machine type.

     * `MACHINE_TYPE`: the machine type of the sole-tenant VM. Use the [`machineTypes.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/machineTypes/list) to get a list of available machine types for the project.

     * `GROUP_NAME`: name of the node group to provision the VM on. If you want to use this instance template to create a regional MIG that exists in more than one zone, specify a list of node groups that exist in the same zones as the regional MIG's zones.

     * `NETWORK`: the URL of the network resource for this instance template.

     * `REGION`: the region containing the subnetwork for this instance template.

     * `SUBNETWORK`: the URL of the subnetwork resource for this instance template.

     * `GPU_TYPE`: the type of GPU. Set to one of the accelerator types specified when the node template was created.

     * `GPU_COUNT`: the number of GPUs of the total specified by the node template to attach to this VM. Default value is `1`.

     * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details) of the image family.

     * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details) of the image to use to create the VM.

     * `LOCAL_SSD_ZONE`: the local SSD's zone.

     * `SSD_INTERFACE`: the type of local SSD interface. Set to `NVME` if the boot disk image drivers are optimized for NVMe, otherwise set to `SCSI`.

  2. Use the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) to create a MIG within your sole-tenant node group based on the previously created instance template. Or, if you want to create a regional MIG, use the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) and specify the region and zones of all of the node groups as specified in the instance template.

For example, to create a zonal MIG, use the following request:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
         {
           "baseInstanceName": "NAME_PREFIX",
           "name": "INSTANCE_GROUP_NAME",
           "targetSize": SIZE,
           "instanceTemplate": "global/instanceTemplates/INSTANCE_TEMPLATE"
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID.

     * `ZONE`: the zone to create the managed instance group in.

     * `NAME_PREFIX`: the prefix name for each of the instances in the managed instance group.

     * `INSTANCE_GROUP_NAME`: the name for the instance group.

     * `SIZE`: the number of VMs to include in this instance group. Your node group must have enough resources to accommodate the instances in this managed instance group. Use the [managed instance group autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler) to automatically manage the size of managed instance groups.

     * `INSTANCE_TEMPLATE`: the URL of the instance template to use to create this group. The template must have a [node affinity label](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity) pointing to the appropriate node group.




## Configure node affinity labels

Node affinity labels let you logically group node groups and schedule VMs on a specific set of node groups. You can also use node affinity labels to schedule VMs on node groups across different zones, and still keep the node groups in a logical group. The following procedure is an example of using affinity labels to associate VMs with a specific node group that is used for production workloads. This example shows how to schedule a single VM, but you could also use [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) to schedule a group of VMs.

###  gcloud 

  1. Use the [`gcloud compute sole-tenancy node-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create) to create a node template with a set of affinity labels for a production workload:
         
         gcloud compute sole-tenancy node-templates create prod-template \
           --node-type=n1-node-96-624 \
           --node-affinity-labels workload=frontend,environment=prod
         

  2. Use the [`gcloud compute sole-tenancy node-templates describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/describe) to view the node affinity labels assigned to the node template.

  3. Use the [`gcloud compute sole-tenancy node-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create) to create a node group that uses the production template:
         
         gcloud compute sole-tenancy node-groups create prod-group \
           --node-template=prod-template \
           --target-size=1
         

  4. For your production VMs, create a `node-affinity-prod.json` file to specify the affinity of your production VMs. For example, you might create a file that specifies that VMs run only on nodes with both the `workload=frontend` and `environment=prod` affinities. Create the node affinity file by using [Cloud Shell](https://docs.cloud.google.com/shell/docs/viewing-and-editing-files) or create it in a location of your choice.
         
         [
           {
             "key" : "workload",
             "operator" : "IN",
             "values" : ["frontend"]
           },
           {
             "key" : "environment",
             "operator" : "IN",
             "values" : ["prod"]
           }
         ]
         

  5. Use the `node-affinity-prod.json` file with the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to schedule a VM on the node group with matching affinity labels.
         
         gcloud compute instances create prod-vm \
           --node-affinity-file node-affinity-prod.json \
           --machine-type=n1-standard-2
         

  6. Use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) and check the `scheduling` field to view the node affinities assigned to the VM.




## Configure node anti-affinity labels

Node affinity labels can be configured as anti-affinity labels to prevent VMs from running on specific nodes. For example, you can use anti-affinity labels to prevent VMs that you are using for development purposes from being scheduled on the same nodes as your production VM. The following example shows how to use affinity labels to prevent VMs from running on specific node groups. This example shows how to schedule a single VM, but you could also use [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) to schedule a group of VMs.

###  gcloud 

  1. For development VMs, specify the affinity of your development VMs by creating a `node-affinity-dev.json` with [Cloud Shell](https://docs.cloud.google.com/shell/docs/viewing-and-editing-files), or by creating it in a location of your choice. For example, create a file that configures VMs to run on any node group with the `workload=frontend` affinity as long as it is not `environment=prod`:
         
         [
           {
             "key" : "workload",
             "operator" : "IN",
             "values" : ["frontend"]
           },
           {
             "key" : "environment",
             "operator" : "NOT_IN",
             "values" : ["prod"]
           }
         ]
         

  2. Use the `node-affinity-dev.json` file with the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create the development VM:
         
         gcloud compute instances create dev-vm \
           --node-affinity-file=node-affinity-dev.json \
           --machine-type=n1-standard-2
         

  3. Use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) and check the `scheduling` field to view the node anti-affinities assigned to the VM.




## What's next

  * [Create sole-tenant node templates](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates).

  * [Create sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-groups).



  * For information about sole-tenant node pricing, see [Sole-tenant nodes pricing](https://cloud.google.com/compute/sole-tenant-pricing).


  * For information about how to enable autoscaling on sole-tenant node groups, see [Node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups).

  * For more information about bringing existing licenses to Google Cloud, see [Bring existing licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses).

  * For more information about sole-tenant nodes, see [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
