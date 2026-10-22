---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/scale-cpu-memory-resources/
title: Scale CPU and memory resources \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:16.499774+00:00
---

# Scale CPU and memory resources  |  AlloyDB Omni using the RPM orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/scale-cpu-memory-resources/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Scale CPU and memory resources Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/scale-cpu-memory-resources)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/scale-cpu-memory-resources)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/scale-cpu-memory-resources)

This page describes how to scale CPU and memory resources using the AlloyDB Omni RPM orchestrator. 

## Before you begin

Before you scale CPU and memory resources, make sure that you have:

  1. [Installed](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-orchestrator) the AlloyDB Omni orchestrator.
  2. Provisioned and [created](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster) your AlloyDB Omni cluster.



## Scale CPU and memory resources

To scale the CPU and memory resources for your AlloyDB Omni database cluster, update your `DBCluster` resource specification:

  1. Open your `DBCluster` database cluster manifest file.

  2. Under the `primarySpec` section, modify the `cpu` and `memory` values in the `resources` block:
         
         DBCluster:
           metadata:
             name: CLUSTER_NAME
           spec:
             # ... existing cluster configuration ...
             primarySpec:
               # ... existing primary configuration ...
               resources:
                 cpu: CPU_COUNT
                 memory: MEMORY_MIN
                 limits:
                   memory: MEMORY_MAX
                 disks:
                 # ...
         

Replace the following:

     * `CLUSTER_NAME`: the name of your database cluster.
     * `CPU_COUNT`: the number of CPUs available to the database instance.
     * `MEMORY_MIN`: the minimum amount of memory allocated to the database instance, for example `16Gi`.
     * `MEMORY_MAX`: the maximum amount of memory allocated to the database instance.
  3. Apply the updated `DBCluster` database cluster manifest using your preferred orchestrator interface. The AlloyDB Omni orchestrator automatically restarts the database to apply the resource changes.

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
         
         ansible-playbook -i "DEPLOYMENT_SPECIFICATION" update.yml -e resource_spec="DBCLUSTER_SPECIFICATION"

Replace the following variables:

     * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).
     * `DBCLUSTER_SPECIFICATION`: path to your cluster specification.

###  `alloydbctl`
    
    alloydbctl apply -d DEPLOYMENT_SPECIFICATION -r DBCLUSTER_SPECIFICATION

Replace the following variables:

     * `DEPLOYMENT_SPECIFICATION`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).
     * `DBCLUSTER_SPECIFICATION`: path to your cluster specification.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
