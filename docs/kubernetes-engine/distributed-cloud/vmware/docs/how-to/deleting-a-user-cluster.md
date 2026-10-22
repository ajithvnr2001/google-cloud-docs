---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-a-user-cluster/
title: Deleting a user cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:18.142188+00:00
---

# Deleting a user cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/deleting-a-user-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Deleting a user cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a Google Distributed Cloud user cluster. User cluster deletion unregisters the cluster from the fleet and deletes the workloads, node pools, control plane nodes, and the corresponding resources, like VMs, F5 partitions, and data disks.

## Choose a tool to delete a cluster

If you created the cluster with [`enableAdvancedCluster`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) set to `true` (which is required for [setting up topology domains](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/topology-domains-set-up)), you must use `gkectl` to delete the cluster.

Otherwise, how you delete a user cluster depends on whether the cluster is enrolled in the GKE On-Prem API. A user cluster is enrolled in the GKE On-Prem API if one of the following is true:

  * The cluster was created by using the Google Cloud console, the Google Cloud CLI (gcloud CLI), or Terraform, which automatically enrolls the cluster in the GKE On-Prem API. Collectively, these tools are referred to as GKE On-Prem API clients.

  * The cluster was created using `gkectl`, but it was [enrolled in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/enroll-cluster).




If the cluster is enrolled in the GKE On-Prem API, use a GKE On-Prem API client to delete the cluster. If the cluster isn't enrolled in the GKE On-Prem API, use `gkectl` on the admin workstation to delete the cluster.

To find all user clusters that are enrolled in the GKE On-Prem API in a specific project, run the following command:
    
    
    gcloud container vmware clusters list \
        --project=PROJECT_ID \
        --location=-
    

The output is similar to the following:
    
    
    NAME                      LOCATION    VERSION             ADMIN_CLUSTER.            STATE
    example-user-cluster-1a   us-west1    1.36.100-gke.144    example-admin-cluster-1   RUNNING
    

When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, you can set `--location` to a specific [region](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/reference/supported-regions-on-prem-api).

If the cluster is listed, it is enrolled in the GKE On-Prem API. If you aren't a project owner, minimally, you must be granted the Identity and Access Management role `roles/gkeonprem.admin` on the project to delete enrolled clusters. For details on the permissions included in this role, see [GKE On-Prem API roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem) in the IAM documentation.

If you are using `gkectl` to delete a cluster, make sure that your admin workstation has the needed version of `gkectl`. Typically, you use the same version of `gkectl` as the version of the cluster that you are deleting. The following version rules are enforced during the delete:

  * The `gkectl` minor version can't be lower than the cluster minor version. For example, deleting a 1.30 cluster using `gkectl` version 1.29 isn't allowed. Patch versions don't matter. For example, you can use `gkectl` version 1.29.0-gke.1456 to delete a cluster with a higher patch version, such as 1.29.1000-gke.94.

  * The `gkectl` minor version can't be more than two minor versions higher than the cluster version. For example, if you are deleting a 1.28 cluster, the `gkectl` version can be 1.29 or 1.30. But you can't use `gkectl` version 1.31 because that is three minor versions higher than the cluster version.




If needed, see [Download `gkectl`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#download_gkectl) to get a supported version of `gkectl`.

## Delete stateful workloads

Before you delete your cluster, delete your stateful workloads, PVCs, and PVs by running `kubectl delete`.

## Delete a user cluster

### gkectl

You can use `gkectl` to delete clusters that aren't enrolled in the GKE On-Prem API. If your organization's proxy and firewall rules allow traffic to reach `gkeonprem.googleapis.com` and `gkeonprem.mtls.googleapis.com` (the service names for the GKE On-Prem API), then `gkectl` will be able to delete enrolled clusters.

Run the following command on the admin workstation to delete the cluster:
    
    
    gkectl delete cluster \
      --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
      --cluster CLUSTER_NAME 
    

where

  * `ADMIN_CLUSTER_KUBECONFIG` is the path to the admin cluster's kubeconfig file.
  * `CLUSTER_NAME` is the name of the user cluster you want to delete.



If deletion fails with a message similar to the following:
    
    
    Exit with error:
    ...
    failed to unenroll user cluster CLUSTER_NAME
    failed to create GKE On-Prem API client
    

That means the cluster is enrolled, but `gkectl` was unable to reach the GKE On-Prem API. In this case, the easiest thing to do is use an GKE On-Prem API client to delete the cluster.

If deleting the user cluster fails halfway, you can run `gkectl` with the `--force` flag to ignore the halfway error and continue the deletion.
    
    
    gkectl delete cluster \
    --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
    --cluster CLUSTER_NAME \
    --force
    

**Caution:** When you force delete a cluster, some F5 or vSphere resources might be left over due to ignoring the halfway errors. See the Clean up resources section for information on cleaning up the leftover resources.

If you deleted a cluster that used the Seesaw load balancer, delete the Seesaw VMs. You can do this by deleting the Seesaw VMs in the vSphere user interface.

### Console

If the user cluster is managed by the GKE On-Prem API do the following steps to delete the cluster:

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the user cluster is in.

  3. In the list of clusters, locate the cluster that you want to delete. If the **Type** is **external** , this indicates that the cluster was created using `gkectl` and wasn't enrolled in the GKE On-Prem API. In this case, follow the steps in the `gkectl` tab to delete the cluster.

If the icon in the **Status** column indicates a problem, follow the steps in the gcloud CLI tab to delete the cluster. You will need to add the `--ignore-errors` flag to the delete command.

  4. Click the name of the cluster that you want to delete.

  5. In the **Details** panel, near the top of the window, click delete **Delete**.

  6. When prompted to confirm, enter the name of the cluster and click **Remove**.




###  gcloud CLI 

If the user cluster is managed by the GKE On-Prem API, do the following on a computer that has the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) installed:

  1. Update components:
         
         gcloud components update
         

  2. Use the following command to delete the cluster:
         
         gcloud container vmware clusters delete USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --force \
           --allow-missing \
           --ignore-errors
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster to delete.

     * `PROJECT_ID`: The ID of the project that the cluster is registered to.

     * `LOCATION`: The Google Cloud location associated with the user cluster.

The `--force` flag lets you delete a cluster that has node pools. Without the `--force` flag, you have to [delete the node pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/node-pools/delete) first, and then delete the cluster.

The `--allow-missing` flag is a [standard Google API flag](https://google.aip.dev/135#delete-if-existing). When you include this flag, the command returns success if the cluster isn't found.

The `--ignore-errors` flag ensures that the deletion of a user cluster resource succeeds even if errors occur during deletion.

If the command returns an error that contains the text `failed connecting to the cluster's control plane`, this indicates connectivity issues with either the admin cluster, the [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent), or the on-premises environment.

     * If you think the connectivity issue is transient, for example, because of network problems, wait and retry the command.

     * If retrying the command continues to fail, see [Collecting Connect Agent logs](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/troubleshooting#agent_logs) to troubleshoot issues with the Connect Agent. 

     * If you know that the admin cluster has been deleted, of if the VMs for the admin or the user cluster have been shut down or are otherwise inaccessible, include the `--ignore-errors` flag and retry the command.

**Caution:** When the admin and user clusters are unreachable, and you include `--ignore-errors`, the delete command removes Google Cloud resources only. Some F5 or vSphere resources might be left over. See the Clean up resources section for information on cleaning up the leftover resources.



For information about other flags, see the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/delete).

## Clean up resources

If there were issues when you deleted the cluster, some F5 or vSphere resources might be left over. The following sections explain how to clean up these leftover resources.

#### Clean up a user cluster's VMs in vSphere

To verify that the user cluster's VMs are deleted, perform the following steps:

  1. From the vSphere Web Client's left-hand **Navigator** menu, click the **Hosts and Clusters** menu.

  2. Find the resource pool for your admin cluster. This is the value of [`vCenter.resourcePool`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-resourcepool-field) in your admin cluster configuration file.

  3. Under the resource pool, locate VMs prefixed with the name of your user cluster. These are the control-plane nodes for your user cluster. There will be one or three of these depending on whether your user cluster has a high-availability control plane.

  4. Find the resource pool for your user cluster. This is the value of [`vCenter.resourcePool`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-resourcepool-field) in your user cluster configuration file. If your user cluster configuration file does not specify a resource pool, it is inherited from the admin cluster.

  5. Under the resource pool, locate VMs prefixed with the name of a node pool in your user cluster. These are the worker nodes in your user cluster.

  6. For each control-plane node and each worker node:

     1. From the vSphere Web Client, right-click the VM and select **Power** > **Power Off**.

     2. After the VM is powered off, right-click the VM and select **Delete from Disk**.




#### Clean up a user cluster's F5 partition

If there are any entries remaining in the user cluster's partition, perform the following steps:

  1. From the F5 BIG-IP console, in the top-right corner of the console, switch to the user cluster partition you want to clean up.
  2. Select **Local Traffic** > **Virtual Servers** > **Virtual Server List**.
  3. In the **Virtual Servers** menu, remove all the virtual IPs.
  4. Select **Pools** , then delete all the pools.
  5. Select **Nodes** , then delete all the nodes.



## After you have finished

After the cluster is deleted, you can delete the user cluster's kubeconfig.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
