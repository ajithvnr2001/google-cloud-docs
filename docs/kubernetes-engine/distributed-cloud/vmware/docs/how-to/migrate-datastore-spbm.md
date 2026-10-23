---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-datastore-spbm/
title: Migrate datastore to SPBM \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:45.437034+00:00
---

# Migrate datastore to SPBM  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-datastore-spbm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Migrate datastore to SPBM Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to migrate a vSphere datastore to [Storage Policy Based Management](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) (SPBM).

This page is for Storage specialists who configure and manage storage performance, usage, and expense. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

1.30: GA   
1.29: Preview   
1.16 and earlier: Not available

## Context

There are four places where you can specify a datastore in cluster configuration files:

  * Admin cluster: [vCenter.datastore](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-datastore-field)

  * User cluster at the cluster level, which includes control plane nodes and all worker node pools: [vCenter.datastore](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-datastore-field)

  * User cluster control plane nodes: [masterNode.vsphere.datastore](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-vsphere-datastore-field)

  * User cluster worker node pools: [nodePools[i].vsphere.datastore](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-vsphere-datastore-field)




The inheritance for these fields is as follows:
    
    
    adminCluster.vCenter.datastore ->
      userCluster.vCenter.datastore ->
        (userCluster.masterNode.vsphere.datastore and userCluster.nodePools[i].vsphere.datastore)
    

Examples:

  * If `userCluster.vCenter.datastore` is empty, it inherits the value from `adminCluster.vCenter.datastore`.

  * If `userCluster.nodePools[i].vsphere.datastore` is empty, it inherits the value from `userCluster.vCenter.datastore`.




Similarly, there are four places to specify a storage policy:

  * Admin cluster [vCenter.storagePolicyName](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-storagepolicyname-field)

  * User cluster at the cluster level, which includes control plane nodes and all worker node pools: [vCenter.storagePolicyName](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-storagepolicyname-field)

  * User cluster control plane nodes: [masterNode.vsphere.storagePolicyName](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#masternode-vsphere-storagepolicyname-field)

  * User cluster worker node pools: [nodePools[i].vsphere.storagePolicyName](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#nodepool-vsphere-storagepolicyname-field)




The inheritance for the `storagePolicyName` fields is the same as it is for the `datastore` fields.

## Before you begin

  * This process is a one-way migration. We don't support migrating back to the previous state.
  * The datastore must be compatible with the new storage policy you are going to set.
  * Only high availability (HA) admin clusters are supported. If your admin cluster is non-HA admin, you must first [migrate the admin cluster to HA](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features).



## Migrate a user cluster

The steps that you use for the migration depends on whether you want to migrate the entire user cluster, or if you want to migrate the control plane nodes and worker node pools separately. This option lets you select different storage policies for control plane nodes and worker node pools.

To help with planning a maintenance window, note the following:

  * Migrating the entire cluster requires only one cluster update.

  * Migrating the control plane nodes and worker nodes pools separately requires two cluster updates.




### Entire cluster

Use these steps if you want to migrate the entire cluster including all control plane nodes and worker node pools. Your user cluster version must be at 1.30 or higher.

  1. Modify the user cluster configuration file, as follows:

     1. Set the `vCenter.storagePolicyName` field with the name of the storage policy.

     2. Remove or comment out the following if they are specified:

        * `vCenter.datastore` field
        * `masterNode.vsphere` section
        * `nodepools[i].vsphere.datastore`
        * `nodepools[i].vsphere.storagePolicyName`

The following example configurations show these changes.

Before the changes:
    
    vCenter:
      datastore: ds-1
    

After the changes:
    
    vCenter:
      storagePolicyName: sp-1
      # datastore: ds-1
    

  2. Update the user cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

     * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.




#### Update the bundled `StorageClass`

After you update the configuration settings in the cluster, you need to update the bundled `StorageClass`. 

  1. Get the current default `StorageClass` for the bundled `vsphere-csi-driver`, which is named `standard-rwo`, and save it to a local file called `storage-class.yaml`.
         
         kubectl get storageclass standard-rwo -oyaml \
             --kubeconfig USER_CLUSTER_KUBECONFIG > storage-class.yaml
         

Replace `USER_CLUSTER_KUBECONFIG` with the path of the user cluster kubeconfig.

  2. Make a copy of `storage-class.yaml` as a precaution since you need to make changes to the file:
         
         cp storage-class.yaml storage-class.yaml-backup.yaml
         

  3. Delete the default `StorageClass` from the cluster:
         
         kubectl delete storageclass standard-rwo \
             --kubeconfig USER_CLUSTER_KUBECONFIG
         

  4. Update the configuration in `storage-class.yaml` as follows:

     1. Delete or comment out the following fields:

        * `parameters.datastoreURL`
        * `resourceVersion`
     2. Add the `parameters.storagePolicyName` field and set it to the name of the storage policy.

The following example configurations show these changes.

Before the changes:
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
      name: standard-rwo
    Parameters:
      ...
      datastoreURL: ds//ds-1
    

After the changes:
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
      name: standard-rwo
    Parameters:
      ...
      storagePolicyName: sp-1
    

  5. Apply the modified `StorageClass` to the user cluster:
         
         kubectl apply -f storage-class.yaml \
             --kubeconfig USER_CLUSTER_KUBECONFIG
         




#### Kubeception user clusters only

For Kubeception user clusters, you need to update the `StorageClass` for the user cluster control plane nodes in the admin cluster. Kubeception clusters have the configuration field `enableControlplaneV2` set to `false`. When Controlplane V2 is enabled, the control plane for the user cluster runs in the user cluster itself. When Controlplane V2 isn't enabled, the control plane for the user cluster runs in the admin cluster, which is referred to as kubeception.

Run the following command to determine whether the cluster has Controlplane V2 enabled:
    
    
    kubectl get onpremuserclusters --kubeconfig USER_CLUSTER_KUBECONFIG \
      -n kube-system -o jsonpath='{.items[0].spec.enableControlplaneV2}' && echo
    

If the output is `false`, complete the following steps to update the default `StorageClass` for the user cluster control plane nodes in the admin cluster:

  1. Get the current default `StorageClass` for the bundled `vsphere-csi-driver`, which is named `USER_CLUSTER_NAME-csi`, and save it to a local file called `storage-class-kubeception.yaml`.
         
         kubectl get storageclass USER_CLUSTER_NAME-csi -oyaml \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG > storage-class-kubeception.yaml
         

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of the admin cluster kubeconfig.

  2. Make a copy of `storage-class-kubeception.yaml` as a precaution since you need to make changes to the file:
         
         cp storage-class-kubeception.yaml storage-class-kubeception-backup.yaml
         

  3. Delete the default `StorageClass` from the cluster:
         
         kubectl delete storageclass USER_CLUSTER_NAME-csi \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

  4. Update the configuration in `storage-class-kubeception.yaml` as follows:

     1. Delete or comment out the following fields:

        * `parameters.datastoreURL`
        * `resourceVersion`
     2. Add the `parameters.storagePolicyName` field and set it to the name of the storage policy.

The following example configurations show these changes.

Before the changes:
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
      name: standard-rwo
    Parameters:
      ...
      datastoreURL: ds//ds-1
    

After the changes:
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
      name: standard-rwo
    Parameters:
      ...
      storagePolicyName: sp-1
    

  5. Apply the modified `StorageClass` to the admin cluster:
         
         kubectl apply -f storage-class-kubeception.yaml \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




#### After the migration

If you create a new node pool after a migration, the new pool follows the rules of inheritance according to the updated cluster.

For example, suppose you migrated `vCenter.datastore` to a storage policy.

Now if you create a new node pool and leave both `nodePools[i].vsphere.datastore`and `nodePools[i].vsphere.storagePolicyName` empty, the new node pool inherits the storage policy specified in `vCenter.storagePolicyName`.

### Nodes separately

Use these steps if you want to migrate the control plane nodes and worker node pools separately.

  1. Version 1.29 only: Get the current cluster configuration. This step isn't needed if the user cluster is at version 1.30 or higher.
         
         gkectl get-config cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --cluster-name USER_CLUSTER_NAME \
           --output-dir ./gen-files
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the kubeconfig file for the admin cluster.

     * `USER_CLUSTER_NAME`: the name of the user cluster.

In `./gen-files`, locate `user-cluster.yaml`.

For more information about getting the configuration file, see [Generate configuration files from a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/get-configuration-file-from-cluster).

The generated configuration file has the `datastore` name set at each level: cluster, `masterNode` (for control plane nodes), and `nodepools` (for worker nodes), as shown in the following example:
    
    apiVersion: v1
    kind: UserCluster
    ...
    # VCenter config in cluster level:
    vCenter:
      datastore: ds-1
    ...
    # VCenter config in master node level:
    masterNode:
      vsphere:
        datastore: ds-1
    ...
    # VCenter config in nodepool level:
    nodepools:
    - name: pool-1
      vsphere:
        datastore: ds-1
    - name: pool-2
      vsphere:
        datastore: ds-1
    




#### Migrate control plane nodes

Do the following steps to migrate the control plane nodes:

  1. Make the following changes in the user cluster configuration file:

     * Set `masterNode.vsphere.storagePolicyName` field with the name of the storage policy.
     * Delete or comment out the `masterNode.vsphere.datastore` field.

The following example configurations show these changes.

Before the changes:
    
    masterNode:
      vsphere:
        datastore: ds-1
    

After the changes:
    
    masterNode:
      vsphere:
        # datastore: ds-1
        storagePolicyName: sp-1
    

  2. Update the user cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config USER_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path of the admin cluster kubeconfig file.

     * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.

Wait for the update command to complete before updating node pools.




#### Migrate node pools

Do the following steps to migrate all node pools:

  1. Make the following changes in the user cluster configuration file:

     * Set each `nodePools[i].vsphere.storagePolicyName` field with the name of the storage policy.
     * Delete or comment out each `nodePools[i].vsphere.datastore` field.

The following example configurations show these changes.

Before the changes:
    
    nodepools:
    - name: pool-1
      vsphere:
        datastore: ds-1
    - name: pool-2
      vsphere:
        datastore: ds-1
    

After the changes:
    
    nodepools:
    - name: pool-1
      vsphere:
        # datastore: ds-1
        storagePolicyName: sp-1
    - name: pool-2
      vsphere:
        # datastore: ds-1
        storagePolicyName: sp-1
    

  2. Update the user cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config USER_CLUSTER_CONFIG
         




#### Optionally, update the storage policy at the cluster level

For user clusters, the `datastore` and `storagePolicyName` fields in the cluster level `vCenter` section is a default value used by the `masterNode` and `nodepools` sections. After you have done the previous steps, the cluster level `vCenter` `datastore` and `storagePolicyName` settings won't be used by by any cluster components. You can leave the cluster level `vCenter` section as it is or update it to be consistent with `masterNode` and `nodepools`.

If you leave the setting as it is, we recommend that you add a comment above the cluster level `vCenter` section saying that the setting is ignored because it is overridden by settings in the `masterNode` and `nodepools` sections.

If you prefer, you can change the cluster level `vCenter` section to match the `masterNode` and `nodepools` sections and update the cluster using the following steps:

  1. Modify the user cluster configuration file, as follows:

     * Set the `vCenter.storagePolicyName` field with the name of the storage policy.
     * Remove or comment out the `vCenter.datastore` field.
  2. Update the user cluster:
         
         gkectl update cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config USER_CLUSTER_CONFIG
         

This update command won't make any changes to the cluster, but it updates the server side (`OnPremUserCluster`) `vCenter.datastore` and `vCenter.storagePolicyName` fields.




#### Update the bundled `StorageClass`

After you update the configuration settings, you need to update the bundled `StorageClass`.

  1. Get the current default `StorageClass` for the bundled `vsphere-csi-driver`, which is named `standard-rwo`, and save it to a local file called `storage-class.yaml`.
         
         kubectl get storageclass standard-rwo -oyaml \
             --kubeconfig USER_CLUSTER_KUBECONFIG > storage-class.yaml
         

Replace `USER_CLUSTER_KUBECONFIG` with the path of the user cluster kubeconfig.

  2. Make a copy of `storage-class.yaml` as a precaution since you need to make changes to the file:
         
         cp storage-class.yaml storage-class.yaml-backup.yaml
         

  3. Delete the default `StorageClass` from the cluster:
         
         kubectl delete storageclass standard-rwo \
             --kubeconfig USER_CLUSTER_KUBECONFIG
         

  4. Update the configuration in `storage-class.yaml` as follows:

     1. Delete or comment out the following fields:

        * `parameters.datastoreURL`
        * `resourceVersion`
     2. Add the `parameters.storagePolicyName` field and set it to the name of the storage policy.

The following example configurations show these changes.

Before the changes:
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
      name: standard-rwo
    Parameters:
      ...
      datastoreURL: ds//ds-1
    

After the changes:
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
      name: standard-rwo
    Parameters:
      ...
      storagePolicyName: sp-1
    

  5. Apply the modified `StorageClass` to the user cluster:
         
         kubectl apply -f storage-class.yaml \
             --kubeconfig USER_CLUSTER_KUBECONFIG
         




#### Kubeception user clusters only

For Kubeception user clusters, you need to update the `StorageClass` for the user cluster control plane nodes in the admin cluster. Kubeception clusters have the configuration field `enableControlplaneV2` set to `false`. When Controlplane V2 is enabled, the control plane for the user cluster runs in the user cluster itself. When Controlplane V2 isn't enabled, the control plane for the user cluster runs in the admin cluster, which is referred to as kubeception.

Run the following command to determine whether the cluster has Controlplane V2 enabled:
    
    
    kubectl get onpremuserclusters --kubeconfig USER_CLUSTER_KUBECONFIG \
      -n kube-system -o jsonpath='{.items[0].spec.enableControlplaneV2}' && echo
    

If the output is `false`, complete the following steps to update the default `StorageClass` for the user cluster control plane nodes in the admin cluster:

  1. Get the current default `StorageClass` for the bundled `vsphere-csi-driver`, which is named `USER_CLUSTER_NAME-csi`, and save it to a local file called `storage-class-kubeception.yaml`.
         
         kubectl get storageclass USER_CLUSTER_NAME-csi -oyaml \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG > storage-class-kubeception.yaml
         

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of the admin cluster kubeconfig.

  2. Make a copy of `storage-class-kubeception.yaml` as a precaution since you need to make changes to the file:
         
         cp storage-class-kubeception.yaml storage-class-kubeception-backup.yaml
         

  3. Delete the default `StorageClass` from the cluster:
         
         kubectl delete storageclass USER_CLUSTER_NAME-csi \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

  4. Update the configuration in `storage-class-kubeception.yaml` as follows:

     1. Delete or comment out the following fields:

        * `parameters.datastoreURL`
        * `resourceVersion`
     2. Add the `parameters.storagePolicyName` field and set it to the name of the storage policy.

The following example configurations show these changes.

Before the changes:
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
      name: standard-rwo
    Parameters:
      ...
      datastoreURL: ds//ds-1
    

After the changes:
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
      name: standard-rwo
    Parameters:
      ...
      storagePolicyName: sp-1
    

  5. Apply the modified `StorageClass` to the admin cluster:
         
         kubectl apply -f storage-class-kubeception.yaml \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




## Migrate an admin cluster

Make sure that the admin cluster is also updated with the storage policy name.

  1. Make the following changes in the admin cluster configuration file:

     * Remove or comment out the `vCenter.datastore` field.
     * Set the `vCenter.storagePolicyName` field with the name of the storage policy.
  2. Update the admin cluster:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --config ADMIN_CLUSTER_CONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_KUBECONFIG`: the path to the admin cluster kubeconfig file.
     * `ADMIN_CLUSTER_CONFIG`: the path to the admin cluster configuration file.



## Storage migration with SPBM

After the datastore to SPBM migration, your clusters are now using SPBM now. But the migration doesn't move any storage workloads (such as machine data disks or container volumes) from the old datastore.

To move storage workloads, see [Storage migration with Storage Policy Based Management](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/storage-migration-spbm).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
