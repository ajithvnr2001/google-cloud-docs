---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools/
title: Creating and managing node pools \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:57.599658+00:00
---

# Creating and managing node pools  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Creating and managing node pools Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/managing-node-pools)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/managing-node-pools)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



When you create a user cluster, you have to configure at least one [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools), which is a group of nodes that all have the same configuration. After the cluster is created, you can add new node pools, update node pool settings, and delete node pools.

## Choose a tool to manage node pools

How you create, update, and delete node pools depends on whether the cluster is managed by the GKE On-Prem API. A user cluster is managed by the GKE On-Prem API if one of the following is true:

  * The cluster was created in the Google Cloud console or using the Google Cloud CLI (gcloud CLI), which automatically configures the GKE On-Prem API to manage the cluster.

  * The cluster was created using `gkectl`, but it was [configured to be managed by the GKE On-Prem API](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/enroll-cluster).




If the GKE On-Prem API is managing a user cluster, you can use the console or the gcloud CLI to manage node pools. If the user cluster isn't managed by the GKE On-Prem API, use `gkectl` on the admin workstation to manage node pools.

If you plan to use the gcloud CLI, do the following on a computer that has the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) installed:

  1. Log in with your Google account
         
         gcloud auth login
         

  2. Update components:
         
         gcloud components update
         




## Add a node pool

If the cluster is managed by the GKE On-Prem API, you can use either the console or the gcloud CLI to add a node pool; however, you need to use `gkectl` on your admin workstation to configure the following node pool settings:

  * [Windows for the OS image type](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-osimage-field)
  * [vSphere datastore](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-vsphere-datastore-field)
  * [vSphere tags](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-vsphere-tags-field) If you want to attach tags to all VMs in a node pool, your vCenter user account must have these [vSphere tagging privileges](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-2F8C5B02-7EF6-428A-BDB6-B2CC3D307097.html):

    * vSphere Tagging.Assign or Unassign vSphere Tag
    * vSphere Tagging.Assign or Unassign vSphere Tag on Object (vSphere 7)
  * [Automatic scaling for the node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-autoscaling-section)




Before you add another node pool, [verify that enough IP addresses are available](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/resizing-a-user-cluster#verify_ips) on the cluster.

### gkectl

Do the following on your admin workstation:

  1. In your [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file), fill in the [`nodePools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepools-section) section.

You must specify the following fields:

     * `nodePools.[i].name`
     * `nodePools[i].cpus`
     * `nodePools.[i].memoryMB`
     * `nodePools.[i].replicas`

The following fields are optional. If you don't include [`nodePools[i].bootDiskSizeGB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-bootdisksizegb-field) or [`nodePools[i].osImageType`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepool-osimagetype-field), the default values are used.

     * `nodePools[i].labels`
     * `nodePools[i].taints`
     * `nodePools[i].bootDiskSizeGB`
     * `nodePools[i].osImageType`
     * `nodePools[i].vsphere.datastore`
     * `nodePools[i].vsphere.tags`
**Note:** The **Ubuntu** OS Image type for node pools will be deprecated in Google Distributed Cloud version 1.12 and unsupported in version 1.13. Consider changing your node pools now to use either **Ubuntu Containerd** or **COS** for the OS Image type.
  2. Run the following command:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG` with the path of the kubeconfig file for your admin cluster.

     * `USER_CLUSTER_CONFIG` with the path of your user cluster configuration file.




### Example configuration

In the following example configuration, there are four node pools, each with different attributes:

  * `pool-1`: only the minimum required attributes are specified
  * `pool-2`: includes `vsphere.datastore` and `vsphere.tags`
  * `pool-3`: includes `taints` and `labels`
  * `pool-4`: includes `osImageType`and `bootDiskSizeGB`


    
    
    nodePools:
    - name: pool-1
      cpus: 4
      memoryMB: 8192
      replicas: 5
    - name: pool-2
      cpus: 8
      memoryMB: 16384
      replicas: 3
      vsphere:
        datastore: my_datastore
        tags:
        - category: "purpose"
          name: "testing"
    - name: pool-3
      cpus: 4
      memoryMB: 8192
      replicas: 5
      taints:
        - key: "example-key"
          effect: NoSchedule
      labels:
        environment: production
        app: nginx
    - name: pool-4
      cpus: 4
      memoryMB: 8192
      replicas: 5
      osImageType: cos
      bootDiskSizeGB: 40
    

### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **View details** in the **Details** panel.

  4. Click add_box **Add node pool**.

  5. Configure the node pool:

     1. Enter the **Node pool name**.
     2. Enter the number of **vCPUs** for each node in the pool (minimum 4 per user cluster worker).
     3. Enter the **memory** size in mebibytes (MiB) for each node in the pool (minimum 8192 MiB per user cluster worker node and must be a multiple of 4).
     4. In the **Nodes** field, enter the number of nodes in the pool (minimum of 3).
     5. Select the **OS image type** : **Ubuntu Containerd** or **COS**.

     6. Enter the **Boot disk size** in gibibytes (GiB) (default is 40 GiB).

  6. In the **Node pool metadata (optional)** section, if you want to add Kubernetes [labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) and [taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/), do the following:

     1. Click **\+ Add Kubernetes Labels**. Enter the **Key** and **Value** for the label. Repeat as needed.
     2. Click **\+ Add Taint**. Enter the **Key** , **Value** , and **Effect** for the taint. Repeat as needed.
  7. Click **Create**.

  8. The Google Cloud console displays **Cluster status: changes in progress**. Click **Show Details** to view the **Resource status condition** and **Status messages**.




###  gcloud CLI 

Run the following command to create a node pool:
    
    
    gcloud container vmware node-pools create NODE_POOL_NAME \
      --cluster=USER_CLUSTER_NAME  \
      --project=FLEET_HOST_PROJECT_ID \
      --location=LOCATION \
      --image-type=IMAGE_TYPE  \
      --boot-disk-size=BOOT_DISK_SIZE \
      --cpus=vCPUS \
      --memory=MEMORY \
      --replicas=NODES
    

Replace the following:

  * `NODE_POOL_NAME`: A name of your choice for the node pool. The name must:

    * contain at most 40 characters
    * contain only lowercase alphanumeric characters or a hyphen (`-`)
    * start with an alphabetic character
    * end with an alphanumeric character
  * `USER_CLUSTER_NAME`: The name of the user cluster in which the node pool will be created.




  * `FLEET_HOST_PROJECT_ID`: The ID of the project that the cluster is registered to.

    * `LOCATION`: The Google Cloud location associated with the user cluster.

    * `IMAGE_TYPE`: The type of OS image to run on the VMs in the node pool. Set to one of the follow: `ubuntu_containerd` or `cos`.

    * `BOOT_DISK_SIZE`: The size of the boot disk in gibibytes (GiB) for each node in the pool. The minimum is 40 GiB.

    * `vCPUs`: The number of vCPUs for each node in the node pool. The minimum is 4.

    * `MEMORY`: The memory size in mebibytes (MiB) for each node in the pool. The minimum is 8192 MiB per user cluster worker node and the value must be a multiple of 4.

    * `NODES`: The number of nodes in the node pool. The minimum is 3.

For example:
    
    gcloud container vmware node-pools create default-pool \
      --cluster=user-cluster-1  \
      --location=us-west1 \
      --image-type=ubuntu_containerd  \
      --boot-disk-size=40 \
      --cpus=8 \
      --memory=8192 \
      --replicas=5
    

Optionally, you can specify the following: 

    * `--enable-load-balancer`: Only relevant for the MetalLB load balancer. If specified, lets the MetalLB speaker run on the nodes in the pool. At least one node pool must be enabled for the MetalLB load balancer.

    * `--image=IMAGE`: OS image name in vCenter.

    * `--node-labels=KEY=VALUE,...`: A comma-separated list of [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) (key-value pairs) applied to each node in the pool.

    * `--node-taints=KEY=VALUE:EFFECT,...` A comma-separated list of [Kubernetes taints](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-taints) applied to each node in the pool. Taints are key-value pairs associated with an effect. Taints are used with tolerations for Pod scheduling. Specify one of the following for EFFECT: `NoSchedule`, `PreferNoSchedule`, `NoExecute`.

For example:
    
    gcloud container vmware node-pools create default-pool \
        --cluster=user-cluster-1  \
        --location=us-west1 \
        --image-type=ubuntu_containerd  \
        --boot-disk-size=40 \
        --cpus=8 \
        --memory=8192 \
        --replicas=5 \
        --node-taints=key1=val1:NoSchedule,key2=val2:NoExecute
    

For information on other optional flags, see the [gcloud reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools/create).




## Update a node pool

When you increase the number of replicas, Google Distributed Cloud adds the required number of nodes to the user cluster, and when you decrease the number of replicas, nodes are removed. Changing the number of replicas for a node pool doesn't interrupt workloads. Make sure that you have IP addresses available if you increase the number of replicas.

If you update any other node pool field, this triggers a [rolling update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) on the cluster. In a rolling update, Google Distributed Cloud creates a new node and then deletes an old node. This process is repeated until all the old nodes have been replaced with new nodes. This process doesn't cause downtime, but the cluster must have an extra IP address available to use during the update.

Suppose a node pool will have N nodes at the end of an update. Then you must have at least N + 1 IP addresses available for nodes in that pool. This means that if you are resizing a cluster by adding nodes to one or more pools, you must have at least one more IP address than the total number of nodes that will be in all of the cluster's node pools at the end of the resizing. For more information, see [Verify that enough IP addresses are available](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/resizing-a-user-cluster#verify_ips).

To update a node pool on a user cluster:

### gkectl

  1. Modify the values for the fields that you want to change in the [`nodePools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepools-section) section of the user cluster configuration file.

  2. Update the cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG` with the path of the kubeconfig file for your admin cluster.

     * `USER_CLUSTER_CONFIG` with the path of your user cluster configuration file.




### Update the `osImageType` used by a node pool

To update a node pool to use a different `osImageType`, you have to use the command line. To change the `osImageType` used by a node pool, update the configuration file for the node pool, as shown in the following example, and run `gkectl update cluster`.
    
    
    nodePools:
    - name: np-1
      cpus: 4
      memoryMB: 8192
      replicas: 3
      osImageType: ubuntu_containerd
    

**Warning:** As Docker Engine support is removed in Kubernetes 1.24, `ubuntu` OS image type [is no longer supported](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/using-containerd). You should plan to convert your node pools to use the `ubuntu_containerd` or `cos` OS image type as soon as possible.

### Console

You can update only the following fields using the console:

  * Number of replicas
  * Memory
  * Number of vCPUs



To update other fields, use the gcloud CLI or `gkectl`.

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **View details** in the **Details** panel.

  4. Click the **Nodes** tab.

  5. Click the name of the node pool that you want to modify.

  6. Click edit **Edit** next to the field that you want to modify, and click **Done**.

  7. Click arrow_back to go back to the previous page.

  8. The Google Cloud console displays **Cluster status: changes in progress**. Click **Show Details** to view the **Resource status condition** and **Status messages**.




###  gcloud CLI 

  1. Optionally, list the node pools to get the name of the node pool that you want to update:
         
         gcloud container vmware node-pools list \
           --cluster=USER_CLUSTER_NAME \
           --project=FLEET_HOST_PROJECT_ID \
           --location=LOCATION
         

  2. Run the following command to update the node pool:
         
         gcloud container vmware node-pools update NODE_POOL_NAME \
           --cluster=USER_CLUSTER_NAME \
           --project=FLEET_HOST_PROJECT_ID \
           --location=LOCATION \
           --ATTRIBUTE_TO_UPDATE \
           ...
         

Replace the following:

     * `NODE_POOL_NAME`: The name of the node pool to update.

     * `USER_CLUSTER_NAME`: The name of the user cluster that contains the node pool.

     * `LOCATION`: The Google Cloud location associated with the user cluster.

     * `ATTRIBUTE_TO_UPDATE`: One or more flags to update node pool attributes. For example, to change the number of vCPUs and nodes in the pool, run the following command.
    
    gcloud container vmware node-pools update default-pool \
        --cluster=user-cluster-1  \
        --project=example-project-12345
        --location=us-west1 \
        --cpus=10 \
        --replicas=6
    

For information on the node pool attributes that you can update, see the [gcloud reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools/update).




## Verify your changes

To verify that your node pools have been created or updated as intended, inspect the cluster nodes:

### gkectl

Run the following command:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get nodes -o wide
    

If you need to revert your changes, edit the cluster configuration file and run `gkectl update cluster`.

### Console

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the cluster list, click the name of the cluster, and then click **View details** in the **Details** panel.

  4. Click the **Nodes** tab.

  5. Click the name of the node pool you want to view.




###  gcloud CLI 

Run the following command:
    
    
    gcloud container vmware node-pools describe NODE_POOL_NAME \
      --cluster=USER_CLUSTER_NAME \
      --project=FLEET_HOST_PROJECT_ID \
      --location=LOCATION
    

## Delete a node pool

Although you can delete node pools, your user cluster must have at least one node pool. Deleting a node pool causes immediate removal of the pool's nodes regardless of whether those nodes are running workloads.

**Caution:** If the cluster is managed by the GKE On-Prem API, be sure to use the Google Cloud console or the gcloud CLI to delete the node pool. Using `gketcl` to delete a node pool on a cluster that is managed by the GKE On-Prem API leaves orphaned resources in the cluster.

To delete a node pool from a user cluster:

### gkectl

  1. Ensure that there are no workloads running on the affected nodes.

  2. Remove its definition from the [`nodePools`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#nodepools-section) section of the user cluster configuration file.

  3. Update the cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `[ADMIN_CLUSTER_KUBECONFIG]` with the path of the kubeconfig file for your admin cluster.

     * `[USER_CLUSTER_CONFIG]` with the path of your user cluster configuration file.




### Console

  1. Ensure that there are no workloads running on the affected nodes.

  2. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  3. Select the Google Cloud project that the user cluster is in.

  4. In the cluster list, click the name of the cluster, and then click **View details** in the **Details** panel.

  5. Click the **Nodes** tab.

  6. Click the name of the node pool that you want to delete.

  7. Click delete **Delete**.

  8. Click arrow_back to go back to the previous page.

  9. The Google Cloud console displays **Cluster status: changes in progress**. Click **Show Details** to view the **Resource status condition** and **Status messages**.




###  gcloud CLI 

  1. Optionally, list the node pools to get the name of the node pool that you want to delete:
         
         gcloud container vmware node-pools list \
           --cluster=USER_CLUSTER_NAME \
           --project=FLEET_HOST_PROJECT_ID \
           --location=LOCATION
         

  2. Run the following command to delete the node pool:
         
         gcloud container vmware node-pools delete NODE_POOL_NAME \
           --cluster=USER_CLUSTER_NAME \
           --project=FLEET_HOST_PROJECT_ID \
           --location=LOCATION
         

Replace the following:

     * `NODE_POOL_NAME`: The name of the node pool to delete.

     * `USER_CLUSTER_NAME`: The name of the user cluster that contains the node pool.

     * `LOCATION`: The Google Cloud location associated with the user cluster.




## Troubleshooting

  * In general, the `gkectl update cluster` command provides specifics when it fails. If the command succeeded and you don't see the nodes, you can troubleshoot with the [Diagnosing cluster issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#diagnose_user_cluster) guide.

  * It is possible that there are insufficient cluster resources like a lack of available IP addresses during node pool creation or update. See the [Resizing a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/resizing-a-user-cluster) topic for details about verifying that IP addresses are available.

  * You can also review the general [Troubleshooting](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshooting) guide.

  * Won't proceed past `Creating node MachineDeployment(s) in user cluster…`.

It can take a while to create or update the node pools in your user cluster. However, if the wait time is extremely long and you suspect that something might have failed, you can run the following commands:

    1. Run `kubectl get nodes` to obtain the state of your nodes.
    2. For any nodes that are not ready, run `kubectl describe node NODE_NAME` to obtain details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
