---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-disk-cache/
title: Accelerate database performance using disk cache \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:00.245096+00:00
---

# Accelerate database performance using disk cache  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-disk-cache/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  Accelerate database performance using disk cache Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/configure-disk-cache)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/configure-disk-cache)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/configure-disk-cache)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/configure-disk-cache)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/configure-disk-cache)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/configure-disk-cache)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-disk-cache)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/configure-disk-cache)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/configure-disk-cache)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/configure-disk-cache)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/configure-disk-cache)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/configure-disk-cache)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/configure-disk-cache)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/configure-disk-cache)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/configure-disk-cache)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/configure-disk-cache)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/configure-disk-cache)

This page describes how to provision, set up, and use disk caching on AlloyDB Omni to increase performance of your AlloyDB Omni installation. 

In addition to the standard PostgreSQL in-memory shared buffers, AlloyDB Omni disk cache enables storing buffers on fast storage such as solid-state drives (SSDs). Disk caching accelerates data retrieval in AlloyDB Omni installations with data directories located on slower storage.

Like PostgreSQL shared buffers, AlloyDB Omni disk cache is non-persistent, which means cached data is lost on restart.

By default, AlloyDB Omni disk cache uses all storage reported by the file system. You can define the amount of storage reserved for caching data using the `omni_disk_cache_file_size` parameter.

**Note:** To use the disk cache on the AlloyDB Omni Kubernetes operator, you don't need to provision a file system or mount disks. See Enable AlloyDB Omni disk cache for details on how to modify the AlloyDB Omni Kubernetes operator cluster's manifest to include the `ultraFastCache` feature.

## Enable AlloyDB Omni disk cache

To enable disk cache, complete one of the following subsections:

  * Enable disk cache on a generic volume
  * Enable disk cache on a local volume
  * Enable disk cache on an ephemeral volume



### Enable disk cache on a generic volume

You can enable disk cache using a generic volume. 

For enabling disk cache on a generic volume on the AlloyDB Omni Kubernetes operator, you need [a persistent volume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumes) ready ahead of time and a [`storageClass`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#storageclasses).

For example, if you use GKE and don't have the persistent volume and `storageClass` ready, make sure you have performed the following before enabling disk cache on a generic volume:

  1. [Created a cluster with local SSD-based storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#1st-or-2nd-generation).
  2. Formatted your volume to the ext4 file system using step 1 of [Run the local volume static provisioner](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#run-local-volume-static-provisioner).
  3. [Manually created a persistent volume for each SSD in your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#pv) with the `storageClass` that defines persistent storage on a storage device.



To enable disk cache on a generic volume for your database, complete the following steps:

  1. Modify your database cluster manifest to add the `ultraFastCache` attribute to the `features` section of the `spec` section:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
               kind: DBCluster
               metadata:
                 name: CLUSTER_NAME
               spec:
                 databaseVersion: "17.5.0"
                 primarySpec:
                   features:
                     ultraFastCache:
                       cacheSize: DISK_CACHE_SIZE
                       genericVolume:
                         storageClass: "STORAGE_CLASS_NAME"
               ...
               

Replace the following:

     * `DB_CLUSTER_NAME`: the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/deploy-kubernetes#create).
     * `DISK_CACHE_SIZE`: the size of the cache—for example, `100Gi`. It must be greater than `shared_buffers`. This field is optional. If you don't specify the value of this field, AlloyDB Omni uses all space left on the disk, which applies to both AlloyDB Omni in a container and on a Kubernetes cluster.
     * `STORAGE_CLASS_NAME`: the name of the `[storage class](https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1)` of the ultra fast cache volume—for example, `local-storage`.
  2. Reapply the manifest.



### Enable disk cache on a local volume

If you want to use a local volume, you don't have to create [a persistent volume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumes). You can use the following optimization instead.

For example, if you use GKE and don't have the persistent volume and `storageClass` ready, make sure you have performed the following before enabling disk cache on a local volume:

  1. [Created a cluster with local SSD-based storage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#1st-or-2nd-generation).

  2. Formatted your volume to the `ext4` file system using step 1 of [Run the local volume static provisioner](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd-raw#run-local-volume-static-provisioner).




To enable disk cache on a local volume for your database, do the following:

  1. Modify your database cluster manifest to add the `ultraFastCache` attribute to the `features` section of the `spec` section:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: CLUSTER_NAME
         spec:
           databaseVersion: "17.5.0"
           primarySpec:
             features:
               ultraFastCache:
                 cacheSize: DISK_CACHE_SIZE
                 localVolume:
                   path: "LOCAL_VOLUME_PATH"
                   nodeAffinity:
                     required:
                       nodeSelectorTerms:
                       - matchExpressions:
                         - key: "LABEL_KEY"
                           operator: "OPERATOR_VALUE"
                           values:
                           - "LABEL_KEY_VALUE"
         ...
           

Replace the following:

     * `CLUSTER_NAME`: the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/deploy-kubernetes#create).
     * `DISK_CACHE_SIZE`: the size of the cache—for example, `100Gi`. It must be greater than `shared_buffers`. This field is optional. If you don't specify the value of this field, AlloyDB Omni uses all space left on the disk, which applies to both AlloyDB Omni in a container and on a Kubernetes cluster.
     * `STORAGE_CLASS_NAME`: the name of the [storage class](https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1).
     * `LOCAL_VOLUME_PATH`: the path to the local volume—for example, `/mnt/disks/raid/0`.
     * `LABEL_KEY`: the node's label for the key that serves as a location indicator and facilitates even Pod distribution across the cluster—for example, `cloud.google.com/gke-local-nvme-ssd`.
     * `OPERATOR_VALUE`: the key's relationship to a set of values—for example, `In`. Set the parameter to one of the following: 
       * `In`: the values array must be non-empty.
       * `NotIn`: the values array must be non-empty.
       * `Exists`: the values array must be empty.
       * `DoesNotExist`: the values array must be empty.
       * `Gt`: the values array must have a single element, which is interpreted as an integer.
       * `Lt`: the values array must have a single element, which is interpreted as an integer.
     * `LABEL_KEY_VALUE`: the value for your label key—for example, `true`. Set the parameter to an array of string values as follows: 
       * If the operator is `In` or `NotIn`, the values array must be non-empty.
       * If the operator is `Exists` or `DoesNotExist`, the values array must be empty.
       * If the operator is `Gt` or `Lt`, the values array must have a single element, which is interpreted as an integer.



### Enable disk cache on an ephemeral volume

You can enable disk cache using an `emptyDir` volume, which provides temporary storage that is tied directly to your pod's lifecycle. The volume is created when a pod is assigned to a node, and exists as long as the pod runs on that node.

When a pod is removed from a node, the data in the `emptyDir` is deleted permanently. This type of volume is suitable for a cache because it provides temporary, fast storage. The data in the cache doesn't need to be persisted if the pod is rescheduled.

To enable disk cache on an ephemeral volume for your database, complete the following steps: 

  1. Modify your database cluster manifest to add the `ultraFastCache` attribute to the `features` section of the `spec` section, and specify `emptyDirVolume`:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
               kind: DBCluster
               metadata:
                 name: CLUSTER_NAME
               spec:
                 databaseVersion: "17.5.0"
                 primarySpec:
                   features:
                     ultraFastCache:
                       cacheSize: DISK_CACHE_SIZE
                       emptyDirVolume: {}
                 ...
               

Replace the following:

     * `CLUSTER_NAME`: the name of your database cluster. It is the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/deploy-kubernetes#create).
     * `DISK_CACHE_SIZE`: The size of the cache—for example, 200Gi. **Important:** When using an `emptyDir` volume, you must specify a `cacheSize`. If a size is not provided, the cache might consume all available space on the node's disk, which might cause issues on the node because this disk is shared by all pods running on that node.
  2. Reapply the manifest.
**Note:** An `emptyDir` volume does not influence pod scheduling. You must confirm that the pod is scheduled on a node that is backed by a fast storage medium, such as an SSD, by using [node affinity](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/assign-nodes-cluster-scheduling#define-node-affinity) rules in the pod spec.


## Verify the disk cache configuration

After enabling AlloyDB Omni disk cache, verify that the disk cache is accessed by monitoring read and write activity to the disks using available utilities like `iotop` or `iostat`.

Additionally, you can check if the AlloyDB Omni disk cache is open. 

To verify the disk cache configuration for AlloyDB Omni, use the following command.
    
    
      kubectl exec -i $DATABASE_POD -c database -n $DBCLUSTER_NAMESPACE -- cat /obs/diagnostic/postgresql.log | grep "opened omni disk cache"

If your disk caching is configured correctly, the `Successfully opened omni disk cache ...` message displays in the logs.

## What's next

* [About local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd) * [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
