---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/configure-disk-cache/
title: Accelerate database performance using disk cache \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:25:51.574135+00:00
---

# Accelerate database performance using disk cache  |  AlloyDB Omni using the RPM orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/configure-disk-cache/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/overview)



Send feedback 

#  Accelerate database performance using disk cache Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/configure-disk-cache)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/configure-disk-cache)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/configure-disk-cache)

This page describes how to provision, set up, and use disk caching on AlloyDB Omni to increase performance of your AlloyDB Omni installation. 

In addition to the standard PostgreSQL in-memory shared buffers, AlloyDB Omni disk cache enables storing buffers on fast storage such as solid-state drives (SSDs). Disk caching accelerates data retrieval in AlloyDB Omni installations with data directories located on slower storage.

Like PostgreSQL shared buffers, AlloyDB Omni disk cache is non-persistent, which means cached data is lost on restart.

By default, AlloyDB Omni disk cache uses all storage reported by the file system. You can define the amount of storage reserved for caching data using the `omni_disk_cache_file_size` parameter.

## Enable AlloyDB Omni disk cache

To enable disk cache, see the following section:

  * Enable disk cache on a local volume



### Enable disk cache on a local volume

If you want to use a local volume, you don't have to create [a persistent volume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumes). You can use the following optimization instead.

To enable disk cache on a local volume for your database, do the following:

  1. Modify your database cluster manifest to add the `ultraFastCache` attribute to the `features` section of the `spec` section:
         
         DBCluster:
           metadata:
             name: CLUSTER_NAME
           spec:
             databaseVersion: "18.4.0"
             primarySpec:
               features:
                 ultraFastCache:
                   cacheSize: DISK_CACHE_SIZE
                   localVolume:
                     path: "LOCAL_VOLUME_PATH"
         ...
           

Replace the following:

     * `CLUSTER_NAME`: the name of your database cluster.
     * `DISK_CACHE_SIZE`: the size of the cache—for example, `100Gi`. It must be greater than `shared_buffers`. This field is optional. If you don't specify the value of this field, AlloyDB Omni uses all space left on the disk.
     * `LOCAL_VOLUME_PATH`: the path to the local volume—for example, `/mnt/disks/raid/0`.
  2. Reapply the manifest.

  3. Apply the changes using your preferred orchestrator interface:

###  Ansible 

If you're managing your AlloyDB Omni RPM orchestrator infrastructure directly using Ansible, it triggers updates by running the appropriate playbook and passing the selected `update_action` as an extra variable.

Sample file for `update.yml`:
         
         ---
         - hosts: localhost
           vars:
             update_action: "update_resource_spec"
             ansible_user: your_ssh_user
             ansible_ssh_private_key_file: ~/path/to/private-key
           roles:
             - role: google.alloydbomni_orchestrator.update
         

Run the Ansible command:
         
         ansible-playbook -i DEPLOYMENT_SPECIFICATION update.yml -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following variables:

     * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components).

     * `DBCLUSTER_SPECIFICATION`: path to your cluster specification.

###  `alloydbctl`
    
    alloydbctl apply -d DEPLOYMENT_SPECIFICATION -r DBCLUSTER_SPECIFICATION

Replace the following variables:

     * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components).

     * `DBCLUSTER_SPECIFICATION`: path to your cluster specification.




## Verify the disk cache configuration

After enabling AlloyDB Omni disk cache, verify that the disk cache is accessed by monitoring read and write activity to the disks using available utilities like `iotop` or `iostat`.

Additionally, you can check if the AlloyDB Omni disk cache is open. 

To verify the disk cache configuration for AlloyDB Omni, use the following command.
    
    
    cat LOG_FILE_PATH | grep "opened omni disk cache"

Replace `LOG_FILE_PATH` with the path where AlloyDB Omni logs are being redirected to.

If your disk caching is configured correctly, the `Successfully opened omni disk cache ...` message displays in the logs.

## What's next

* [About local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd) * [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
