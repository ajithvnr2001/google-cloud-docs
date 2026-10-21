---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/troubleshoot-cluster-creation/
title: Troubleshoot cluster creation \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:14.485006+00:00
---

# Troubleshoot cluster creation  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/troubleshoot-cluster-creation/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Troubleshoot cluster creation Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/troubleshoot-cluster-creation)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/troubleshoot-cluster-creation)

This page shows you how to resolve issues with AlloyDB Omni using the RPM orchestrator. 

## Cluster creation errors

This section lists cluster creation errors that you might encounter and explains how to resolve them.

### Installation fails because privilege escalation isn't enabled

The following issue occurs when the `ansible_user` variable in your installation playbook specifies a non-root user and the play doesn't enable privilege escalation:
    
    
    This command has to be run under the root user.
    

This issue occurs because the `google.alloydbomni_orchestrator.install` role installs packages with the `dnf` package manager, which requires root privileges.

To resolve this issue, do the following:

  1. In your playbook, add `become: true` at the play level, as shown in [Install AlloyDB Omni components using Ansible](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components#install-using-ansible).
  2. Verify that the user in the `ansible_user` variable can run `sudo` on every node in the inventory.
  3. Run the playbook again:
         
         ansible-playbook -i deployment_spec.yaml install.yaml




To verify that the issue is resolved, check that the task `Install SELinux python utilities` reports `ok` or `changed`, and that the play recap shows `failed=0` for every host.

### Bootstrap fails because the data directory doesn't exist on database nodes

The following issue occurs when the bootstrap playbook times out on all database nodes with the message `Timeout when waiting for DB_NODE_1:5432`, and the Node Manager log shows an error related to a missing data directory.

To identify the missing directory, do the following:

  1. Use `journalctl` to check the Node Manager log:
         
         sudo journalctl -u alloydbomni_node_manager

  2. Check the output for a message similar to the following:
         
         service "dbprocess": root data directory does not exist: PG_DATA_DIR
         




These messages include the following values:

  * `DB_NODE_1`: the IP address or fully qualified domain name (FQDN) of a database node.
  * `PG_DATA_DIR`: the host path to the directory where the database data is stored.



This issue occurs because `PG_DATA_DIR` doesn't exist on every database node. The orchestrator expects the directory to exist before bootstrap.

To resolve this issue, do the following:

  1. On every database node, create `PG_DATA_DIR` and mount the external volume to it. For more information, see [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/create-cluster#before-you-begin).
  2. Configure the mount to persist across reboots.
  3. Run the bootstrap playbook again.



To verify that the issue is resolved, run the following command:
    
    
    alloydbctl get -d deployment_spec.yaml -t DBCluster -n CLUSTER_NAME -o yaml

Replace `CLUSTER_NAME` with the name of your database cluster.

The output shows the `DatabaseReady` condition with `status: "True"`.

### Bootstrap fails because `DBCluster` parameter values aren't quoted

The following issue occurs when the `parameters` section of your `DBCluster` specification contains numeric values without quotation marks, and you run the playbook that invokes the `google.alloydbomni_orchestrator.bootstrap` role:
    
    
    invalid parameters in DBCluster resource specification: json: cannot unmarshal number into Go struct field AlInstanceSpec.primarySpec.InstanceSpec.parameters of type string
    

This issue occurs because each entry under the `parameters` field is a key-value string pair, as described in [DBCluster Custom Resource Definition](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/dbcluster-spec#primarySpec.parameters).

To resolve this issue, do the following:

  1. Enclose every value under the `spec.primarySpec.parameters` field in quotation marks, as shown in [Prepare cluster specifications](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/create-cluster#prepare-specifications):
         
         DBCluster:
           spec:
             primarySpec:
               parameters:
                 max_connections: "100"
                 max_wal_size: "2GB"
         

  2. Run the bootstrap playbook again.




To verify that the issue is resolved, run the following command:
    
    
    alloydbctl get -d deployment_spec.yaml -t DBCluster -n CLUSTER_NAME -o yaml

Replace `CLUSTER_NAME` with the name of your database cluster.

The output shows the `DatabaseReady` condition with `status: "True"`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
