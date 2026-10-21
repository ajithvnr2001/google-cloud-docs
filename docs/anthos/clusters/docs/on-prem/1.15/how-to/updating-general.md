---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general/
title: Updating a cluster \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:54.363623+00:00
---

# Updating a cluster  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-general/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Updating a cluster Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/updating-general)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/updating-general)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page discusses what settings you can update in your admin cluster and user clusters.

Typically, you change a single setting in a configuration file, and then run the `gkectl update` command with the appropriate parameters. To update multiple settings, change one setting at a time and run the command repeatedly.

The `gkectl update` command takes one of the following forms, along with the parameters appropriate for the feature you want to update:

  * `gkectl update credentials` \- Use this to [update cluster credentials](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials).

  * `gkectl update admin` \- Run this command after you make a change in the [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file) so as to update the admin cluster.

  * `gkectl update cluster` \- Run this command after you make a change in the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file) so as to update the user cluster.




## What can and cannot be updated in clusters

Many features in both the admin cluster and user clusters cannot be updated after the cluster is created. 

To see what settings can be updated for the admin cluster, run:
    
    
    gkectl update admin --help
    

To see what settings can be updated for a user cluster, run:
    
    
    gkectl update cluster --help
    

## Admin cluster updates

You can update various features of your admin cluster.

### Update OS image type for the admin cluster

You can [update OS image type for the admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-admin-node-image-type) to use either Ubuntu or COS.

### Allocate additional static IP addresses

If your configuration uses static IP addresses, you must check how many you are using and add additional ones if needed, when you [upgrade an admin workstation or admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading#verify_ips).

### Enable or disable node resizing for the control-plane nodes of a user cluster

You can [enable](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-resize#enable_node_resizing_for_the_control-plane_nodes_of_a_user_cluster) or [disable](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-resize#disable_node_resizing_for_the_control-plane_nodes_of_a_user_cluster) automatic resizing of the control-plane nodes for the user cluster. These nodes are in the admin cluster.

### Enable or disable cluster backup

For an admin cluster, you can [enable cluster backup](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-and-restore-an-admin-cluster-with-gkectl#enable_the_admin_cluster_backup_feature) or [disable cluster backup](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/back-up-and-restore-an-admin-cluster-with-gkectl#disable_the_admin_cluster_backup_feature).

### Enable or disable vSphere resource metrics

If you change the value of [`stackdriver.disableVsphereResourceMetrics`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#stackdriver-disablevsphereresourcemetrics-field) in the admin cluster configuration file, run this command to update your configuration:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG_FILE
    

### Update vCenter certificate reference for the admin cluster

If your vCenter certificate has changed, [update the vCenter certificate reference](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-vcenter-certificate). You must update both the admin cluster and all user clusters.

### Enable automatic resizing of addon nodes for the admin cluster (preview)

You can [enable](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-resize#enable_node_resizing_for_the_add-on_nodes_of_an_admin_cluster) or [disable](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-resize#disable_node_resizing_for_the_add-on_nodes_of_an_admin_cluster) automatic resizing of addon nodes for the admin cluster.

### Enable or disable automatic node repair for the admin cluster (preview)

You can enable or disable automatic node repair for your admin cluster by changing the appropriate setting in the admin cluster configuration file, and running the `gkectl update admin` command.

  * [Enable node repair and health checking for an existing admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-repair#enabling_node_repair_and_health_checking_for_an_existing_admin_cluster)

  * [Disable node repair and health checking for an existing admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-repair#disabling_node_repair_and_health_checking_for_an_admin_cluster)




### Enable or disable anti-affinity groups (preview)

If you change the value of `antiAffinityGroups.enabled` in the admin cluster configuration file, run the following command to update your configuration:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG_FILE
    

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of your kubeconfig file. You can omit this flag if the file is in your current directory and has the name `kubeconfig`.

  * `ADMIN_CLUSTER_CONFIG_FILE`: the path of your admin cluster configuration file. You can omit this flag if the file is in your current directory and has the name `admin-cluster.yaml`.


**Note:** If you change `antiAffinityGroups` settings, that triggers the re-creation of admin cluster add-on nodes and user cluster control-plane nodes in the admin cluster through a rolling update so that the corresponding virtual machine antiaffinity rules and node labels can be updated accordingly. This process might cause temporary disruption to the system workloads running on these nodes. Use caution if you make changes of this kind.

### Enable or disable logging to Cloud Audit Logs for the admin cluster

To enable logging to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit), fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#cloudauditlogging-section) section in your admin cluster configuration file, and then update your cluster.

To disable logging to Cloud Audit Logs, remove the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#cloudauditlogging-section) section from your admin cluster configuration file, and then update your cluster.

This section is required in the admin cluster if you want to manage the lifecycle of user clusters in the Google Cloud console.

To update your cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG_FILE
    

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  * `ADMIN_CLUSTER_CONFIG_FILE`: the path of your admin cluster configuration file.




### Enable or disable logging and monitoring for the admin cluster

To enable [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs), fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#stackdriver-section) section in your admin cluster configuration file, and then update your cluster:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG_FILE
    

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  * `ADMIN_CLUSTER_CONFIG_FILE`: the path of your admin cluster configuration file.




To disable Cloud Logging and Cloud Monitoring, remove the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#stackdriver-section) section from your admin cluster configuration file, and then update your cluster.

The `stackdriver` section is required by default, so to remove it, you must include the `--skip-validation-stackdriver` flag:
    
    
    gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config ADMIN_CLUSTER_CONFIG_FILE \
        --skip-validation-stackdriver
    

The `stackdriver` section is required in the admin cluster if you want to manage the lifecycle of user clusters in the Google Cloud console.

### Register an admin cluster

When you first create an admin cluster, you can register it by filling out the `gkeConnect` section in the admin cluster configuration file before creating it. If you did not register the cluster at the time of creation, you can subsequently [register a cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/connecting-to-a-cluster#cluster_registration) by editing the configuration file to add the `gkeConnect` section and then run the `gkectl update admin` command.

This section is required in the admin cluster if you want to manage the lifecycle of user clusters in the Google Cloud console.

### Rotate a connect-register service account key for the admin cluster

To rotate a connect-register service account key, use the `gkectl update credentials` command as described in [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

## User cluster updates

You can update your user clusters by editing the setting in the [user configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file) and then running `gkectl update cluster` with the appropriate parameters. Here are the changes you can make to your user clusters.

### Allocate additional static IP addresses

If your configuration uses static IP addresses, you must check how many you are using and add additional ones if needed, when you make one of these changes:

  * [Resize a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/resizing-a-user-cluster#static-ips).

  * [Create or update a node pool](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/managing-node-pools).

  * [Upgrade a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/upgrading#verify_ips).




### Resize a user cluster by updating the `nodePool` settings

You can [resize a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/resizing-a-user-cluster) by updating the `replicas` value in the `nodePools` section, and then running the `gkectl update cluster` command.

### Enable or disable vSphere resource metrics

You can [enable or disable vSphere resource metrics](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#stackdriver-disablevsphereresourcemetrics-field) in the user cluster configuration file, and then run the `gkectl update cluster` command.

### Update vCenter certificate reference for user clusters

If your vCenter certificate has changed, [update the vCenter certificate reference](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-vcenter-certificate). You must update both the admin cluster and all user clusters.

### Register a user cluster

When you create a cluster, you can register it by filling out the `gkeConnect` section in the user cluster configuration file before creating it. If you did not register the cluster at the time of creation, you can subsequently [register an existing user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/connecting-to-a-cluster#cluster_registration) by editing the configuration file to add the `gkeConnect` section and then run the `gkectl update cluster` command.

### Enable or disable logging and monitoring for a user cluster (preview)

To enable logging and monitoring, fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#stackdriver-section) section in your user cluster configuration file, and then update your cluster:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config USER_CLUSTER_CONFIG_FILE
    

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  * `USER_CLUSTER_CONFIG_FILE`: the path of your user cluster configuration file.




To disable logging and monitoring, remove the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#stackdriver-section) section from your user cluster configuration file, and then update your cluster.

The `stackdriver` section is required by default, so to remove it, you must include the `--skip-validation-stackdriver` flag:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --config USER_CLUSTER_CONFIG_FILE
        --skip-validation-stackdriver
    

### Enable or disable automatic node repair for user clusters

You can enable or disable automatic node repair for your user by changing the appropriate setting in the user cluster configuration file, and running the `gkectl update cluster` command.

  * [Enable node repair and health checking for an existing user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-repair#disabling_node_repair_and_health_checking_for_a_user_cluster)

  * [Disable node repair and health checking for an existing user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-repair#disabling_node_repair_and_health_checking_for_a_user_cluster)




### Auto-resizing a node in a user cluster

To [enable auto-resizing](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-resize) of a node in a user cluster, edit the user cluster configuration file and run the `gkectl update` command.

### Enable or disable cloud audit logging on a user cluster

You can [enable cloud audit logging](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging#enabling_on_an_existing_user_cluster) or [disable cloud audit logging](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/audit-logging#disabling_cloud_audit_logs_on_an_existing_user_cluster).

### Disable vSphere CSI driver

By default, the vSphere CSI driver is enabled. You can [disable the vSphere CSI driver](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/using-vsphere-csi-driver#disabling_vsphere_csi_driver).

### Rotate a connect-register service account key for a user cluster

To rotate a connect-register service account key, use the `gkectl update credentials` command as described in [Rotating service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

### Update Windows Server configuration to use containerd and Windows Dataplane V2

If your configuration includes a node pool of Windows Server OS nodes, note that Docker and Flannel will be deprecated in an upcoming release. We recommend that you update your user clusters now to use containerd and Windows Dataplane V2 instead.

To do this update:

  1. Set `enableWindowsDataplaneV2` to `true` in the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#enabledataplanev2-field).

**Note:** While the cluster is being upgraded from Flannel to Windows Dataplane V2, the pods running on nodes using Flannel cannot communicate with pods running on the newly created nodes.
  2. Run the `gkectl update cluster` command.




### Update MetalLB configuration

You can update the MetalLB address pools in your user cluster configuration file. You can also enable or disable MetalLB in any node pool by updating the `enableLoadBalancer` value in the `nodePools` section. Make the applicable changes in the configuration file, and then call `gkectl update cluster`:
    
    
    gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONIFG --config USER_CLUSTER_CONFIG
    

Replace the following:

  * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

  * `USER_CLUSTER_CONFIG_FILE`: the path of your user cluster configuration file.




### Update node pool host group

You can update the host group associated with your node pool by changing the `vsphere.hostgroups` field in your user cluster node pool configuration, which includes the following operations:

  * Create a new node pool with the specified host group.
  * Provide a host group to an existing node pool that doesn't have a host group.
  * Update an existing node pool from one host group to another.
  * Remove the existing host group from the node pool.



After changing the `vsphere.hostgroups` field, run the `gkectl update cluster` command to update the node pool.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
