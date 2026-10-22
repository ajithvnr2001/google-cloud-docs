---
url: https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster/
title: Modify a cluster \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:01.264643+00:00
---

# Modify a cluster  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Modify a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to modify a cluster in Cluster Director.

After you create a cluster in Cluster Director, you can modify one or more cluster properties. Modifying a cluster can help you save costs or optimize performance when the needs of your workload change. For example, you can add or delete storage resources, update prolog or epilog scripts, or replace the compute resources that a cluster partition uses.

If you want to add a Cloud Storage bucket to your cluster only for the duration of a Slurm job, then see instead [Mount Cloud Storage buckets for specific jobs](https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets).

## Limitations

When you modify a cluster, the following limitations apply:

  * You can't modify or delete the storage resource that a cluster uses for the `/home` directory.

  * You can't use different types of storage resources in a cluster partition.

  * You can't modify the Slurm version that the controller node in your cluster uses.




## Modifiable cluster properties

You can only modify the following properties in a cluster. If you need to change any other property, then you must first create a replacement cluster with updated properties, and then delete the original cluster if you no longer need it.

  * **Description** : you can add, modify, or delete the cluster's description.

  * **Labels** : you can add, modify, or delete the labels associated with the cluster.

  * **Compute resources** : you can add new compute resource configurations or delete unused ones. You can't modify the properties of existing compute resource configurations.

  * **Storage resources** : you can add or delete Filestore instances, Google Cloud Managed Lustre instances, or Cloud Storage buckets.

  * **Orchestrator** : you can modify the Slurm orchestrator's configuration, including login nodes, OS images, prolog or epilog scripts, nodesets, and partitions.




Based on the properties that you want to modify, modifying your cluster might restart, recreate, or delete nodes. By understanding the impact of each property change in the following sections, you can better plan updates and minimize disruptions:

  * Disruptive cluster property updates

  * Non-disruptive cluster property updates




### Disruptive cluster property updates

When you modify a cluster, modifying one or more of the following properties requires stopping and restarting, recreating, or deleting nodes:

**Caution:** If you modify multiple cluster properties that require restarting or recreating nodes in a single request, then the most disruptive action applies to the affected nodes. For example, if you modify the login nodes' boot disk (which recreates login nodes) and allow OS login restarts (which restarts login nodes), then Cluster Director recreates all login nodes in your cluster.

  * **Updates that delete all affected compute nodes** : when you update one or more of the following properties, Cluster Director deletes the affected compute nodes:

    * **Delete compute resources (`computeResources`)**: deleting a compute resource configuration deletes all compute nodes that use that configuration, unless you specify a replacement configuration for the nodes. The replacement configuration can't specify a different consumption option or zone. If you don't specify a replacement configuration, then you must delete any nodesets that use the compute resource configuration that you want to delete. Otherwise, modifying the cluster fails.

    * **Decrease static or dynamic node count (`staticNodeCount` or `maxDynamicNodeCount`)**: deleting compute nodes from a nodeset stops and deletes those nodes. Slurm abruptly stops any running jobs on the deleted nodes.

  * **Updates to storage resources that can disrupt jobs** : when you update one or more of the following properties, Cluster Director might disrupt the running jobs in your cluster:

    * **Delete or modify storage resources (`storageResources`)**: deleting or modifying Filestore instances, Managed Lustre instances, or Cloud Storage buckets disrupts any running jobs that are reading files from that resource that you're modifying. We recommend that you modify or delete these storage resources when all jobs on the affected compute nodes have finished running.

    * **Delete storage configurations (`storageConfigs`)**: deleting storage resource configurations is likely to disrupt any running jobs that are reading files from any resources that use those configurations. All nodesets in your cluster must use the same storage configuration. Otherwise, modifying your cluster fails.

  * **Updates that restart, recreate, or delete all login nodes** : when you update one or more of the properties within the login nodes configuration (`orchestrator.slurm.loginNodes`), Cluster Director recreates, deletes, or stops and restarts the login nodes. Recreating or restarting login nodes doesn't affect the queued or running jobs.

    * **Modify boot disks (`bootDisk`)**: if you modify any boot disk property (`type`, `sizeGb`, `image`, or `storagePools`), then Cluster Director recreates all login nodes.

    * **Decrease the number of login nodes (`count`)**: decreasing the number of login nodes deletes the affected nodes.

    * **Enable or disable OS login operations (`enableOsLogin`)**: allowing or disallowing OS login restarts all login nodes.

    * **Enable or disable external IP addresses (`enablePublicIps`)**: allowing or disallowing resources from being publicly accessible restarts all login nodes.

    * **Modify machine type (`machineType`)**: changing the machine type restarts or recreates all login nodes based on the chosen machine type and its availability.

    * **Modify startup script (`startupScript`)**: modifying the startup script for the login nodes stops and restarts all login nodes.

    * **Modify startup script timeout (`startupScriptTimeout`)**: modifying the timeout for the startup script doesn't restart or recreate login nodes. The new timeout is enforced the next time a login node restarts.




### Non-disruptive cluster property updates

When you modify a cluster, modifying one or more of the following properties doesn't restart or recreate existing nodes:

  * **Modify description (`description`)**: modifying the description for your cluster doesn't restart or recreate nodes.

  * **Modify labels (`labels`)**: adding, modifying, or deleting labels that are associated with your cluster doesn't restart or recreate nodes.

  * **Add storage resources (`storageResources`)**: adding Filestore instances, Managed Lustre instances, or Cloud Storage buckets doesn't restart or recreate nodes.

  * **Slurm login nodes (`orchestrator.slurm.loginNodes`)**:

    * **Modify labels (`labels`)**: modifying labels for login nodes doesn't disrupt your workloads.

    * **Add or delete storage configurations (`storageConfigs`)**: adding or deleting storage resources that are mounted on login nodes doesn't disrupt your workloads.

    * **Modify service account** (`serviceAccount`): modifying the service account doesn't disrupt your workloads.

  * **Slurm nodesets (`orchestrator.slurm.nodeSets`)**:

    * **Increase static or dynamic node count (`staticNodeCount` or `maxDynamicNodeCount`)**: increasing the number of static or dynamic nodes in a nodeset doesn't restart or recreate existing nodes.

    * **Modify labels (`labels`)**: modifying labels for a nodeset doesn't restart or recreate nodes.

    * **Modify startup script (`computeInstance.startupScript`) or boot disks (`computeInstance.bootDisk`)**: modifying the startup script or boot disk properties for a nodeset doesn't disrupt running jobs. Cluster Director applies the changes to new compute nodes, and to existing compute nodes after they finish running all jobs and their state changes to `idle`.

    * **Add storage configurations (`storageConfigs`)**: adding storage resources in a nodeset doesn't restart or recreate existing compute nodes. All nodesets in a Slurm cluster must use the same storage configuration.

  * **Create or delete Slurm partitions (`orchestrator.slurm.partitions`)**: creating or deleting Slurm partitions doesn't restart, recreate, or delete nodes. However, if you delete a partition that has running jobs, Slurm stops those jobs.

  * **Modify Slurm default partition (`orchestrator.slurm.defaultPartition`)**: modifying the default Slurm partition doesn't restart or recreate nodes. If you have scheduled jobs, verify that modifying the default partition isn't disruptive.

  * **Modify Slurm prolog script (`orchestrator.slurm.prologBashScripts`)**: modifying the prolog script runs the script for only new and queued jobs; existing jobs are unaffected.

  * **Modify Slurm epilog script (`orchestrator.slurm.epilogBashScripts`)**: modifying the epilog script updates the script for all jobs. The updated script runs when any active job on a node finishes, even if the job started before you update the script.

  * **Modify Slurm settings (`orchestrator.slurm.config`, `orchestrator.slurm.partitions[].config`, `orchestrator.slurm.nodeSets[].config`)**: modifying custom Slurm settings for the cluster, specific partitions, or nodes in specific nodesets doesn't restart or recreate compute or login nodes. Your running jobs continue to run without interruptions. The controller node restarts the Slurm controller daemon to apply configuration updates. For a list of supported parameters, see [Supported Slurm settings in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/slurm-settings).




## Before you begin

Before you modify a cluster, consider the following:

  * If you want to delete a storage resource, then back up any data that you want to retain. Deleting a storage resource is irreversible. To review your options for backing up data, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection).

  * Don't modify or delete Compute Engine resources that contain the label `hypercomputeClusterResource` set to `true`. Cluster Director provisions and manages these resources. If you modify them, then you might encounter errors. To check the labels for a Compute Engine resource, see [View labels](https://docs.cloud.google.com/compute/docs/labeling-resources#view_labels).

  * Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permission that you need to modify a cluster, ask your administrator to grant you the [Cluster Director Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `hypercomputecluster.clusters.update` permission, which is required to modify a cluster. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Modify a cluster

Before you modify a cluster, understand how changes can impact your running workloads:

  * **Disruptive updates** : modifying some properties stops or recreates nodes. If you haven't already, then review which updates can disrupt your workload. For a list of these properties, see Disruptive cluster property updates.

  * **Planned maintenance** : to minimize disruptions, we recommend that you update cluster properties that restart or recreate nodes during planned maintenance. Unless your nodes use N2 machine types, host maintenance events stop and restart nodes. To start a host maintenance event before its planned time, see [Manually start planned host maintenance events](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#start-maintenance).




To modify a cluster, select one of the following options. If you want to edit the cluster description or labels, then use the gcloud CLI or REST API. If you want to edit custom Slurm settings, then use the REST API.

###  Console 

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director)

  2. In the navigation menu, click **Clusters**. The **Clusters** page opens.

  3. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to modify. The page that gives the details of your cluster opens.

  4. Click edit **Edit**. A page that lets you edit your cluster opens.

  5. In the **Compute** section, you can modify the compute resource configurations that your cluster uses. To do so, do one of more of the following:

     * To add or edit a compute resource configuration, do one of the following:

       * To add a compute resource configuration, click add **Add resource configuration**.

       * To edit a compute resource configuration, click edit **Edit resource configuration**.

     * In the **Add resource configuration** pane that appears, you can do one or more of the following:

       * To specify a machine type, click the **General purpose** or **GPUs** tab, and then follow the prompts to specify the machine type.

       * In the **Number of instances** field, enter the number of compute instances for the resource configuration.

     * To delete a resource configuration, click delete **Delete resource configuration**.

  6. Click **Continue**.

  7. To add or delete storage resources in your cluster, in the **Storage** section, do one or more of the following:

     * To add a storage resource, click add **Add storage configuration** , and then follow the prompts to specify the configuration for the storage resource.

     * To delete a storage resource other than the one used for the `/home` directory, locate the storage resource, and then click delete **Delete storage plan**.

  8. Click **Continue**.

  9. To modify the login nodes in your cluster, expand the **Login node** section, and then do one or more of the following:

     * In the **Node count** field, enter the number of compute instances for the node.

     * In the **Machine type** list, select the machine type to use for the login node.

     * In the **Source image** list, select the OS image.

     * In the **Startup script** field, enter or modify the startup script for your cluster.

     * In the **Startup script timeout** field, enter or modify the timeout for the startup script. The value must be at least `1` (one second).

     * In the **Boot disk type** list, select the [type of boot disk](https://docs.cloud.google.com/compute/docs/disks) that you want your login node to use.

     * In the **Boot disk size** field, enter the number of GB for the disk. You must enter a value of `50` or higher. However, to help ensure that your nodes boot up quickly, we recommend that you specify a value of at least `100`.

  10. To modify partitions and nodesets, expand the **Partitions** section, and then add, delete, or edit the partitions and nodesets as needed.

  11. To add or edit prolog or epilog scripts, expand **Advanced orchestration settings** , and then add or edit your scripts.

  12. Click **Save**. A page that gives the details of your cluster opens. Based on the properties that you modify, modifying the cluster can take some time to complete.




###  gcloud 

To modify a cluster, use the [`gcloud alpha cluster-director clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/update).

Based on how you want to specify the cluster configuration, use one of the following methods. To modify storage resources, you must modify the cluster by specifying a configuration file.

  * **Specify a configuration file** : to modify a cluster by specifying the cluster configuration in a JSON file, use the `--config` flag. To run the command, select one of the following options:

###  Bash 
        
        gcloud alpha cluster-director clusters update CLUSTER_NAME \
            --location=REGION \
            --config=CONFIGURATION_FILE
        

###  Powershell 
        
        gcloud alpha cluster-director clusters update CLUSTER_NAME `
            --location=REGION `
            --config=CONFIGURATION_FILE
        

###  cmd.exe 
        
        gcloud alpha cluster-director clusters update CLUSTER_NAME ^
            --location=REGION ^
            --config=CONFIGURATION_FILE
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster that you want to modify.

    * `REGION`: the region where your cluster exists.

    * `CONFIGURATION_FILE`: the path to the JSON file that contains the configuration details for the cluster. To review the configuration details that you can specify, review the [request body for modifying a cluster by using REST](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters#Cluster).

  * **Specify each cluster property** : to modify a cluster by specifying each configuration property directly, include one or more of the following flags based on the cluster properties that you want to modify:

    * To modify the cluster description: `--description`

    * To add or delete labels in the cluster, use one of the following flags:

      * To add labels: `--add-labels`

      * To delete labels: `--remove-labels`

    * To modify the Slurm nodesets, use one of the following flags:

      * To add a nodeset: `--add-slurm-node-sets`

      * To update a nodeset: `--update-slurm-node-sets`

      * To delete a nodeset: `--remove-slurm-node-sets`

    * To modify the Slurm partitions, use one of the following flags:

      * To add a partition: `--add-slurm-partitions`

      * To update a partition: `--update-slurm-partitions`

      * To delete a partition: `--remove-slurm-partitions`

      * To modify the default partition: `--slurm-default-partition`

    * To add or delete on-demand compute instances, use one of the following flags:

      * To add on-demand compute instances: `--add-on-demand-instances`

      * To delete on-demand compute instances: `--remove-on-demand-instances`

    * To add or delete reserved compute instances, use one of the following flags:

      * To add reserved compute instances: `--add-reserved-instances`

      * To delete reserved compute instances: `--remove-reserved-instances`

    * To add or delete Spot VMs, use one of the following flags:

      * To add Spot VMs: `--add-spot-instances`

      * To delete Spot VMs: `--remove-spot-instances`

    * To add or delete Flex-start VMs, use one of the following flags:

      * To add Flex-start VMs: `--add-dws-flex-instances`

      * To delete Flex-start VMs: `--remove-dws-flex-instances`

For example, suppose that you want to modify a cluster by modifying the cluster description, adding a new label, modifying the login nodes, adding a new nodeset, partition, and compute resource configuration. To make these changes in your cluster, select one of the following options:

###  Bash 
    
    gcloud alpha cluster-director clusters update CLUSTER_NAME \
        --location=REGION \
        --description="DESCRIPTION" \
        --add-labels=CLUSTER_LABEL_KEY=CLUSTER_LABEL_VALUE \
        --add-on-demand-instances=id=NEW_COMPUTE_RESOURCE_NAME,zone=NEW_ZONE,machineType=NEW_MACHINE_TYPE \
        --add-slurm-node-sets=id=NODESET_NAME,computeId=COMPUTE_RESOURCE_NAME,staticNodeCount=STATIC_NUMBER_VMS,maxDynamicNodeCount=MAX_DYNAMIC_NUMBER_VMS,startupScript=STARTUP_SCRIPT_NODESET,labels="NODESET_LABEL" \
        --add-slurm-partitions=id=PARTITION_NAME,nodesetIds=[NODESET_NAME]
    

###  Powershell 
    
    gcloud alpha cluster-director clusters update CLUSTER_NAME `
        --location=REGION `
        --description="DESCRIPTION" `
        --add-labels=CLUSTER_LABEL_KEY=CLUSTER_LABEL_VALUE `
        --add-on-demand-instances=id=NEW_COMPUTE_RESOURCE_NAME,zone=NEW_ZONE,machineType=NEW_MACHINE_TYPE `
        --add-slurm-node-sets=id=NODESET_NAME,computeId=COMPUTE_RESOURCE_NAME,staticNodeCount=STATIC_NUMBER_VMS,maxDynamicNodeCount=MAX_DYNAMIC_NUMBER_VMS,startupScript=STARTUP_SCRIPT_NODESET,labels="NODESET_LABEL" `
        --add-slurm-partitions=id=PARTITION_NAME,nodesetIds=[NODESET_NAME]
    

###  cmd.exe 
    
    gcloud alpha cluster-director clusters update CLUSTER_NAME ^
        --location=REGION ^
        --description="DESCRIPTION" ^
        --add-labels=CLUSTER_LABEL_KEY=CLUSTER_LABEL_VALUE ^
        --add-on-demand-instances=id=NEW_COMPUTE_RESOURCE_NAME,zone=NEW_ZONE,machineType=NEW_MACHINE_TYPE ^
        --add-slurm-node-sets=id=NODESET_NAME,computeId=COMPUTE_RESOURCE_NAME,staticNodeCount=STATIC_NUMBER_VMS,maxDynamicNodeCount=MAX_DYNAMIC_NUMBER_VMS,startupScript=STARTUP_SCRIPT_NODESET,labels="NODESET_LABEL" ^
        --add-slurm-partitions=id=PARTITION_NAME,nodesetIds=[NODESET_NAME]
    

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster that you want to modify.

    * `REGION`: the region where your cluster exists.

    * `DESCRIPTION`: a new description for your cluster.

    * `CLUSTER_LABEL_KEY`: the key for the new label that you want to apply to your cluster. For more information about applying labels to Compute Engine resources, see [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources).

    * `CLUSTER_LABEL_VALUE`: the value for the new label.

    * `NEW_COMPUTE_RESOURCE_NAME`: the name of the new compute resource configuration.

    * `NEW_ZONE`: the new zone for the new compute resource configuration.

    * `NEW_MACHINE_TYPE`: a supported machine type based on your specified [consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option).

    * `NODESET_NAME`: the name of the new nodeset to add to your cluster.

    * `COMPUTE_RESOURCE_NAME`: the name of the compute resource configuration for the new nodeset to use.

    * `STATIC_NUMBER_VMS`: the minimum number of compute instances that your nodeset must use.

    * `MAX_DYNAMIC_NUMBER_VMS`: the maximum number of compute instances that Cluster Director can add to the nodeset.

    * `STARTUP_SCRIPT_NODESET`: the startup script for the nodeset.

    * `NODESET_LABEL`: a label to apply to the nodeset.

    * `PARTITION_NAME`: the name of the new partition.




The output is similar to the following:
    
    
    Update request issued for: [cluster000]
    Waiting for operation [projects/example-project/locations/us-central1/operations/operation-1759940551889-640a8176bd2a2-0e460b9d-4281a5ca] to complete...working...
    

Based on the properties that you modify in your cluster, modifying the cluster can take some time to complete. When it does complete, the output is similar to the following:
    
    
    Updated cluster [cluster000].
    

###  REST 

To modify a cluster, make a `PATCH` request to the [`clusters.patch` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/patch).

Your request must include the following HTTP method and request URL:
    
    
    PATCH https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME?updateMask=FIELDS_TO_UPDATE
    

Based on the cluster properties that you want to modify, include one or more of the following fields in the request body:

  * **`description`** : a description for your cluster.

  * **`labels`** : key-value pairs of labels to help you organize and filter your clusters, as well as their associated resources.

  * **`computeResources`** : the compute resources for your cluster, including the machine types and provisioning models to use for the compute instances in the cluster.

  * **`storageResources`** : the storage resources for your cluster; namely, the Filestore instances, Managed Lustre instances, or Cloud Storage buckets.

  * **`orchestrator`** : the settings for the Slurm workload scheduler for your cluster, as well as the configurations for the cluster partitions and nodesets.




For example, suppose that you want to modify a cluster by modifying the cluster description, adding a new label, modifying the login nodes, adding a new nodeset, partition, and compute resource configuration. To make these changes in your cluster, include the following in a JSON file named `request-body.json`:
    
    
    {
      "description": "DESCRIPTION",
      "labels": {
        "CLUSTER_LABEL_KEY": "CLUSTER_LABEL_VALUE"
      },
      "orchestrator": {
        "slurm": {
          "loginNodes": {
            "count": "LOGIN_NODE_VMS",
            "startupScript": "STARTUP_SCRIPT",
            "startupScriptTimeout": "STARTUP_SCRIPT_TIMEOUT"
          },
          "nodeSets": [
            {
              "id": "NODESET_NAME",
              "computeId": "COMPUTE_RESOURCE_NAME",
              "storageConfigs": [
                {
                  "id": "STORAGE_NAME",
                  "localMount": "STORAGE_PATH"
                }
              ],
              "staticNodeCount": "STATIC_NUMBER_VMS",
              "maxDynamicNodeCount": "MAX_DYNAMIC_NUMBER_VMS",
              "computeInstance": {
                "startupScript": "STARTUP_SCRIPT_NODESET",
                "startupScriptTimeout": "STARTUP_SCRIPT_TIMEOUT",
                "labels": {
                  "nodesetLabel": "NODESET_LABEL"
                },
                "bootDisk": {
                  "type": "projects/PROJECT_ID/zones/DISK_ZONE/diskTypes/DISK_TYPE",
                  "sizeGb": "DISK_SIZE"
                }
              }
            }
          ],
          "partitions": [
            {
              "id": "PARTITION_NAME",
              "nodeSetIds": [
                "NODESET_NAME"
              ]
            }
          ]
        }
      },
      "computeResources": {
        "NEW_COMPUTE_RESOURCE_NAME": {
          "config": {
            "newOnDemandInstances": {
              "machineType": "NEW_MACHINE_TYPE",
              "zone": "NEW_ZONE"
            }
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.

  * `REGION`: the region where your cluster exists.

  * `CLUSTER_NAME`: the name of the cluster that you want to modify.

  * `FIELDS_TO_UPDATE`: a comma-separated list of fields that you want to update. Based on how you want to update a field, do one of the following:

    * To update the field's value, specify the field in the `updateMask` query parameter _and_ in the request body.

    * To delete a field from the cluster configuration details, specify the field in the `updateMask` query parameter but omit it from the request body.

For this example, the `updateMask` query parameter is as follows:
    
    description,labels,orchestrator.slurm.loginNodes.count,orchestrator.slurm.loginNodes.startupScript,orchestrator.slurm.nodeSets,orchestrator.slurm.partitions,computeResources
    

  * `DESCRIPTION`: a new description for your cluster.

  * `CLUSTER_LABEL_KEY`: the key for the new label that you want to apply to your cluster. For more information about applying labels to Compute Engine resources, see [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources).

  * `CLUSTER_LABEL_VALUE`: the value for the new label.

  * `LOGIN_NODE_VMS`: the new number of compute instances for the login nodeset.

  * `STARTUP_SCRIPT`: the startup script for the login nodeset. For more information about using startup scripts in compute instances, see [About startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts).

  * `STARTUP_SCRIPT_TIMEOUT`: the maximum time that the startup script can run, for example `300s`. The default value is `300s` (300 seconds, or five minutes). The minimum allowed value is `1s` (one second).

  * `NODESET_NAME`: the name of the new nodeset to add to your cluster.

  * `COMPUTE_RESOURCE_NAME`: the name of the compute resource configuration for the new nodeset to use.

  * `STORAGE_NAME`: the name of the storage resource to mount.

  * `STORAGE_PATH`: the path on the compute instance where the storage resource is mounted. For example, to mount the storage resource in your home directory, enter `/home`.

  * `STATIC_NUMBER_VMS`: the minimum number of compute instances that your nodeset must use.

  * `MAX_DYNAMIC_NUMBER_VMS`: the maximum number of compute instances that Cluster Director can add to the nodeset.

  * `STARTUP_SCRIPT_NODESET`: the startup script for the nodeset.

  * `NODESET_LABEL`: a label to apply to the nodeset.

  * `DISK_ZONE`: the zone where you want to create the boot disks for the nodesets.

  * `DISK_TYPE`: the type of boot disk for the nodeset. Based on the machine type in the node, specify one of the following values:

    * For A4X instances: `hyperdisk-balanced`

    * For A4 instances: `hyperdisk-balanced`

    * For A3 Ultra instances: `hyperdisk-balanced`

    * For A3 Mega instances: `pd-balanced`, `pd-ssd`, `hyperdisk-balanced`, `hyperdisk-ml`, `hyperdisk-extreme`, or `hyperdisk-throughput`

    * For N2 instances: `pd-standard`, `pd-balanced`, `pd-ssd`, `pd-extreme`, `hyperdisk-extreme`, or `hyperdisk-throughput`

For an overview of the different types of boot disks that you can use, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks) in the Compute Engine documentation.

  * `DISK_SIZE`: the size of the boot disk in GB. The value must be `50` or higher. However, to help ensure that your nodes boot up quickly, we recommend that you specify a value of at least `100`.

  * `PARTITION_NAME`: the name of the new partition.

  * `NEW_COMPUTE_RESOURCE_NAME`: the name of the new compute resource configuration.

  * `NEW_MACHINE_TYPE`: a supported machine type based on your specified [consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option).

  * `NEW_ZONE`: the new zone for the new compute resource configuration.




To send your request, select one of the following options:

###  curl (Bash) 
    
    
    curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request-body.json \
         "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME?updateMask=FIELDS_TO_UPDATE"
    

###  Powershell 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method PATCH `
        -Headers $headers `
        -ContentType: "application/json; charset=utf-8" `
        -InFile request-body.json `
        -Uri "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME?updateMask=FIELDS_TO_UPDATE" | Select-Object -Expand Content
    

###  curl (cmd.exe) 
    
    
    curl -X PATCH ^
         -H "Authorization: Bearer $(gcloud auth print-access-token)" ^
         -H "Content-Type: application/json; charset=utf-8" ^
         -d @request-body.json ^
         "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME?updateMask=FIELDS_TO_UPDATE"
    

The response is similar to the following:
    
    
    {
      "name": "projects/example-project/locations/us-central1/operations/operation-1758842430697-63fa86a4c3030-028b6436-2fbda8e1",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.hypercomputecluster.v1.OperationMetadata",
        "createTime": "2025-09-25T23:20:30.707315354Z",
        "target": "projects/example-project/locations/us-central1/clusters/clusterp6a",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Based on the properties that you modify in your cluster, modifying the cluster can take some time to complete.

## What's next

  * [View clusters](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters)

  * [Connect to a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
