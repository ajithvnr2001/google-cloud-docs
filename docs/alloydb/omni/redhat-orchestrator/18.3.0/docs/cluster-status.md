---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/cluster-status/
title: Get cluster status \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:39:47.010868+00:00
---

# Get cluster status  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/cluster-status/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Get cluster status Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/cluster-status)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/cluster-status)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/cluster-status)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/cluster-status)

To get the status of your AlloyDB Omni cluster, complete one of the following sets of instructions: 

  * Using Ansible

  * Using the AlloyDB Omni orchestrator CLI




## Before you begin

Before you begin, [create your cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/create-cluster).

## Ansible

To get your cluster's status using Ansible, complete the following instructions:

  1. Create an Ansible [playbook](https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_intro.html) for the `google.alloydbomni_orchestrator.status` role.
         
         - name: STATUS_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
           - role: google.alloydbomni_orchestrator.status
         

Replace the following variables:

     * `STATUS_PLAYBOOK_NAME`: name of your Ansible playbook. For example, `My cluster status`.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  2. Run the playbook.
         
         ansible-playbook STATUS_PLAYBOOK_PATH -i DEPLOYMENT_SPECIFICATION_PATH \
               -e resource_type="RESOURCE_TYPE" -e resource_name=RESOURCE_NAME

Replace the following variables:

     * `STATUS_PLAYBOOK_PATH`: path to the playbook that you created in step one.

     * `DEPLOYMENT_SPECIFICATION_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

     * `RESOURCE_TYPE`: resource type you want the status of. For example, this could be [`DBCluster`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/dbcluster-spec) or [`PgBouncer`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/pgbouncer-spec).

     * (Optional) `RESOURCE_NAME`: name of the resource that you want the status of. For example, this could be the name of the `DBCluster` or `PgBouncer` resource.




## AlloyDB Omni orchestrator CLI

To get your cluster's status using the AlloyDB Omni orchestrator CLI, run the following `alloydbctl` command:
    
    
    alloydbctl get -d DEPLOYMENT_SPECIFICATION_PATH_PATH -t RESOURCE_TYPE -n RESOURCE_NAME

Replace the following variables:

  * `DEPLOYMENT_SPECIFICATION_PATH_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-components).

  * `RESOURCE_TYPE`: resource type you want the status of. For example, this could be [`DBCluster`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/dbcluster-spec) or [`PgBouncer`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/pgbouncer-spec).

  * (Optional) `RESOURCE_NAME`: name of the resource that you want the status of. For example, this could be the name of the `DBCluster` or `PgBouncer` resource.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
