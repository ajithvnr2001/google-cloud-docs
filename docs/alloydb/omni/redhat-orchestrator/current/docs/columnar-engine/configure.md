---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/configure/
title: Configure the columnar engine in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.3.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:54:01.942072+00:00
---

# Configure the columnar engine in AlloyDB Omni  |  AlloyDB Omni using the RPM orchestrator: Current (18.3.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/configure/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Configure the columnar engine in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/configure)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/columnar-engine/configure)

This page describes how to enable or disable the columnar engine on an AlloyDB Omni database cluster. It also covers how to configure an appropriate initial size for its column store. 

For a conceptual overview of the AlloyDB columnar engine, see [AlloyDB Omni columnar engine overview](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/overview).

## Enable the columnar engine

To use columnar engine on an instance, set the instance's [`google_columnar_engine.enabled`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/reference/columnar-engine-flags#enabled) flag to `on`.

To set the `google_columnar_engine.enabled` parameter to `on`, complete the following steps:

  1. Open your `DBCluster` database cluster manifest.

  2. Under the `primarySpec` section, add the `google_columnar_engine.enabled` parameter to the `parameters` block:
         
         DBCluster:
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             # ... existing cluster configuration ...
             primarySpec:
               # ... existing primary configuration ...
               parameters:
                 google_columnar_engine.enabled: "on"
         

Replace `DB_CLUSTER_NAME` with the name of the database cluster.

  3. The RPM orchestrator automatically restarts the database to apply the parameter changes. Apply the updated `DBCluster` manifest using either of the following methods:

###  `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "DBCLUSTER_SPECIFICATION"

Replace the following:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.

###  Ansible 

     1. Create an `update.yml` playbook file:
            
            ---
            - hosts: localhost
              vars:
                update_action: "update_resource_spec"
                ansible_user: SSH_USER
                ansible_ssh_private_key_file: SSH_KEY_PATH
              roles:
                - role: google.alloydbomni_orchestrator.update
            

Replace the following:

        * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
        * `SSH_KEY_PATH`: the local path to the SSH private key file used to connect to your nodes.
     2. Run the playbook from your control node, passing the resource specification as an extra variable:
            
            ansible-playbook -i "DEPLOYMENT_SPEC_PATH" update.yml \
              -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following:

        * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
        * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.




## Configure the size of the column store

While the columnar engine is enabled on an instance, AlloyDB Omni allocates a portion of the instance's memory to store its columnar data. Dedicating high-speed RAM to your column store verifies that AlloyDB Omni can access the columnar data as rapidly as possible.

Memory and storage cache together represent the overall capacity of the columnar engine.

### Configure memory

**Warning:** The default value of `google_columnar_engine.memory_size_in_mb` is 1024 MB.

You can set the allocation to a fixed size using the [`google_columnar_engine.memory_size_in_mb`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/reference/columnar-engine-flags#memory-size-in-mb) flag.

To set the `google_columnar_engine.memory_size_in_mb` parameter, complete the following steps:

  1. Open your `DBCluster` database cluster manifest.

  2. Under the `primarySpec` section, add the columnar engine configuration to the `parameters` block:
         
         DBCluster:
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             # ... existing cluster configuration ...
             primarySpec:
               # ... existing primary configuration ...
               parameters:
                 google_columnar_engine.enabled: "on"
                 google_columnar_engine.memory_size_in_mb: "MEMORY_SIZE_MB"
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of the database cluster.
     * `MEMORY_SIZE_MB`: the amount of memory, in megabytes, to allocate to the columnar engine.
  3. The RPM orchestrator automatically restarts the database to apply the parameter changes. Apply the updated `DBCluster` manifest using either of the following methods:

###  `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "DBCLUSTER_SPECIFICATION"

Replace the following:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.

###  Ansible 

     1. Create an `update.yml` playbook file:
            
            ---
            - hosts: localhost
              vars:
                update_action: "update_resource_spec"
                ansible_user: SSH_USER
                ansible_ssh_private_key_file: SSH_KEY_PATH
              roles:
                - role: google.alloydbomni_orchestrator.update
            

Replace the following:

        * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
        * `SSH_KEY_PATH`: the local path to the SSH private key file used to connect to your nodes.
     2. Run the playbook from your control node, passing the resource specification as an extra variable:
            
            ansible-playbook -i "DEPLOYMENT_SPEC_PATH" update.yml \
              -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following:

        * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
        * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.




### Configure storage cache

**Note:** This step is optional for enabling the columnar engine.

You can configure the columnar engine storage cache on either dedicated or shared devices.

#### Dedicated devices

To configure a dedicated device for the columnar engine storage cache, complete the following steps:

  1. Open your `DBCluster` database cluster manifest.

  2. Under the `primarySpec` section, add the `columnarSpillToDisk` attribute with `cacheSize` and `localVolume.path` to the `features` block:
         
         DBCluster:
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             # ... existing cluster configuration ...
             primarySpec:
               # ... existing primary configuration ...
               features:
                 columnarSpillToDisk:
                   cacheSize: STORAGE_CACHE_SIZE
                   localVolume:
                     path: COLUMNAR_CACHE_DIR_PATH
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of the database cluster.
     * `STORAGE_CACHE_SIZE`: the size limit for the columnar engine storage cache—for example, `50Gi`.
     * `COLUMNAR_CACHE_DIR_PATH`: the file system path of the dedicated directory for the columnar engine storage cache—for example, `/mnt/disks/columnarcache`.
  3. Apply the updated `DBCluster` manifest using either `alloydbctl` or Ansible:

###  `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "DBCLUSTER_SPECIFICATION"

Replace the following:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.

###  Ansible 

     1. Create an `update.yml` playbook file:
            
            ---
            - hosts: localhost
              vars:
                update_action: "update_resource_spec"
                ansible_user: SSH_USER
                ansible_ssh_private_key_file: SSH_KEY_PATH
              roles:
                - role: google.alloydbomni_orchestrator.update
            

Replace the following:

        * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
        * `SSH_KEY_PATH`: the local path to the SSH private key file used to connect to your nodes.
     2. Run the playbook from your control node, passing the resource specification as an extra variable:
            
            ansible-playbook -i "DEPLOYMENT_SPEC_PATH" update.yml \
              -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following:

        * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
        * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.




#### Shared devices

If you don't specify `localVolume.path` under `columnarSpillToDisk`, then the columnar engine storage cache shares the disk cache storage configured under `ultraFastCache`.

To configure the columnar engine storage cache on shared devices, complete the following steps:

  1. Open your `DBCluster` database cluster manifest.

  2. Under the `primarySpec` section, add the `columnarSpillToDisk` and `ultraFastCache` attributes to the `features` block:
         
         DBCluster:
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             # ... existing cluster configuration ...
             primarySpec:
               # ... existing primary configuration ...
               features:
                 columnarSpillToDisk:
                   cacheSize: STORAGE_CACHE_SIZE
                 ultraFastCache:
                   cacheSize: ULTRAFAST_CACHE_SIZE
                   localVolume:
                     path: DISK_CACHE_DIR_PATH
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of the database cluster.
     * `STORAGE_CACHE_SIZE`: the size of the columnar storage cache—for example, `50Gi`. If you don't specify a value for this field, 5% of the disk cache is allocated to the columnar engine by default.
     * `ULTRAFAST_CACHE_SIZE`: the maximum size of the ultra fast cache buffer reserved by AlloyDB Omni—for example, `100Gi`. If unset, all remaining disk space at `localVolume.path` is used.
     * `DISK_CACHE_DIR_PATH`: the folder path for the ultra fast cache files—for example, `/mnt/disks/chillcache`.
**Note:** If both `spec.primarySpec.features.ultraFastCache.cacheSize` and `spec.primarySpec.features.columnarSpillToDisk.cacheSize` are specified, their total sum equals the amount of reserved disk space.
  3. Apply the updated `DBCluster` manifest using either `alloydbctl` or Ansible:

###  `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "DBCLUSTER_SPECIFICATION"

Replace the following:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.

###  Ansible 

     1. Create an `update.yml` playbook file:
            
            ---
            - hosts: localhost
              vars:
                update_action: "update_resource_spec"
                ansible_user: SSH_USER
                ansible_ssh_private_key_file: SSH_KEY_PATH
              roles:
                - role: google.alloydbomni_orchestrator.update
            

Replace the following:

        * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
        * `SSH_KEY_PATH`: the local path to the SSH private key file used to connect to your nodes.
     2. Run the playbook from your control node, passing the resource specification as an extra variable:
            
            ansible-playbook -i "DEPLOYMENT_SPEC_PATH" update.yml \
              -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following:

        * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
        * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.




## Enable vectorized join

The columnar engine has a _vectorized join_ feature that can improve the performance of joins by applying vectorized processing to qualifying queries.

After you enable vectorized join, the AlloyDB query planner has the option to apply the vectorized join operator instead of the standard PostgreSQL hash join operator. The planner makes this decision by comparing the cost of executing the query using each method.

To enable vectorized join on an instance, set the instance's [`google_columnar_engine.enable_vectorized_join`](https://docs.cloud.google.com/alloydb/omni/16.8.0/docs/reference/columnar-engine-flags#enable-vectorized-join) flag to `on`.

To set this flag on an instance, run [the `ALTER SYSTEM` PostgreSQL command](https://www.postgresql.org/docs/current/sql-altersystem.html):
    
    
    ALTER SYSTEM SET google_columnar_engine.enable_vectorized_join = 'on';
    

AlloyDB Omni allocates one thread to the vectorized join feature by default. You can increase the number of threads available to this feature by setting the [`google_columnar_engine.vectorized_join_threads`](https://docs.cloud.google.com/alloydb/omni/current/docs/reference/columnar-engine-flags#vectorized-join-threads) flag to a larger value. The maximum value is `cpu_count * 2`.

## Manually refresh your columnar engine

By default, when the columnar engine is enabled it refreshes the column store in the background.

To manually refresh the column engine, run the following SQL query:
    
    
    SELECT google_columnar_engine_refresh(relation =>'TABLE_NAME');
    

Replace `TABLE_NAME` with the name of the table or the materialized view you want to manually refresh.

## Disable the columnar engine

To disable the columnar engine on an instance, set the `google_columnar_engine.enabled` flag to `off`.

To set the `google_columnar_engine.enabled` parameter to `off`, complete the following steps:

  1. Open your `DBCluster` database cluster manifest.

  2. Under the `primarySpec` section, set the `google_columnar_engine.enabled` parameter to `off` in the `parameters` block:
         
         DBCluster:
           metadata:
             name: DB_CLUSTER_NAME
           spec:
             # ... existing cluster configuration ...
             primarySpec:
               # ... existing primary configuration ...
               parameters:
                 google_columnar_engine.enabled: "off"
         

Replace `DB_CLUSTER_NAME` with the name of the database cluster.

  3. The RPM orchestrator automatically restarts the database to apply the parameter changes. Apply the updated `DBCluster` manifest using either of the following methods:

###  `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "DBCLUSTER_SPECIFICATION"

Replace the following:

     * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
     * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.

###  Ansible 

     1. Create an `update.yml` playbook file:
            
            ---
            - hosts: localhost
              vars:
                update_action: "update_resource_spec"
                ansible_user: SSH_USER
                ansible_ssh_private_key_file: SSH_KEY_PATH
              roles:
                - role: google.alloydbomni_orchestrator.update
            

Replace the following:

        * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
        * `SSH_KEY_PATH`: the local path to the SSH private key file used to connect to your nodes.
     2. Run the playbook from your control node, passing the resource specification as an extra variable:
            
            ansible-playbook -i "DEPLOYMENT_SPEC_PATH" update.yml \
              -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following:

        * `DEPLOYMENT_SPEC_PATH`: the path to your deployment specification directory.
        * `DBCLUSTER_SPECIFICATION`: the path to the `DBCluster` manifest that you modified.




## What's next

  * See the [complete list of columnar engine database flags](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/reference/columnar-engine-flags).

  * Try out the codelab [Accelerating analytical queries with columnar engine in AlloyDB Omni](https://codelabs.developers.google.com/alloydb-omni-columnar).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
