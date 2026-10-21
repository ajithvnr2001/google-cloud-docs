---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/use-pgbouncer-connection-pooler/
title: Use the PgBouncer connection pooler \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:21:22.748243+00:00
---

# Use the PgBouncer connection pooler  |  AlloyDB Omni using the RPM orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/use-pgbouncer-connection-pooler/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/overview)



Send feedback 

#  Use the PgBouncer connection pooler Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/use-pgbouncer-connection-pooler)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/use-pgbouncer-connection-pooler)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/use-pgbouncer-connection-pooler)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/use-pgbouncer-connection-pooler)

This page describes how to configure and bootstrap the PgBouncer connection pooler for an AlloyDB Omni cluster using the RPM orchestrator. 

## Before you begin

Make sure that you have a functioning AlloyDB Omni cluster deployed and that the [orchestrator is installed](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-orchestrator) on your control node. You must also make sure that port `6432` is open on your load balancer or database nodes to allow incoming traffic to PgBouncer.

## Prepare resource specification

Create a resource specification file, for example, `pgbouncer_spec.yaml` that defines the PgBouncer resource. This file describes the connection pooler and its association with your database cluster.
    
    
    PgBouncer:
      metadata:
        name: PGBOUNCER_RESOURCE_NAME
      spec:
        dbclusterRef: CLUSTER_NAME
        allowSuperUserAccess: ALLOW_SUPERUSER_ACCESS
        parameters:
          pool_mode: POOL_MODE
          ignore_startup_parameters: IGNORE_STARTUP_PARAMETERS
          default_pool_size: "DEFAULT_POOL_SIZE"
          max_client_conn: "MAX_CLIENT_CONN"
          max_db_connections: "MAX_DB_CONNECTIONS"
    

Replace the following:

  * `PGBOUNCER_RESOURCE_NAME`: the name of your PgBouncer resource.
  * `CLUSTER_NAME`: the name of your AlloyDB Omni database cluster. Use the same name you declared when you bootstrapped your cluster.
  * `ALLOW_SUPERUSER_ACCESS`: specifies whether to allow superuser access to the database. Set this to `true` or `false`.
  * `POOL_MODE`: specifies when a database connection can be reused by other clients. For more information, see Configure PgBouncer settings.
  * `IGNORE_STARTUP_PARAMETERS`: specifies parameters that PgBouncer doesn't allow so that they are ignored during startup.
  * `DEFAULT_POOL_SIZE`: the maximum number of database connections to allow per user-database pair.
  * `MAX_CLIENT_CONN`: the maximum number of client connections.
  * `MAX_DB_CONNECTIONS`: the maximum number of server connections allowed per database.



### Configure PgBouncer settings

Use the following parameters to configure PgBouncer settings:

Parameter | Description | Default value  
---|---|---  
`pool_mode` | Specifies when a database connection can be reused by other clients.  
Allowed values are as follows: 

  * `session`: database connection is released back to the pool after the client disconnects.
  * `transaction`: database connection is released back to the pool after the transaction finishes.
  * `statement`: database connection is released back to the pool after the query finishes.  
Transactions spanning multiple statements are disallowed in this mode.

| `session`  
`ignore_startup_parameters` | Specifies parameters that PgBouncer doesn't allow so that they are ignored during startup. |   
`default_pool_size` | The maximum number of database connections to allow per user-database pair. | `20`  
`max_client_conn` | The maximum number of client connections. | `100`  
`max_db_connections` | The maximum number of server connections allowed per database, regardless of the user. Set to 0 for unlimited. | `0`  
  
## Bootstrap PgBouncer

To bootstrap the PgBouncer connection pooler, use Ansible or the AlloyDB Omni orchestrator CLI (`alloydbctl`):

### Ansible

To bootstrap PgBouncer using Ansible, you use a playbook that uses the `google.alloydbomni_orchestrator.bootstrap` role:

  1. Create an [Ansible playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html), for example, `bootstrap_pgbouncer.yaml`, that points to your [deployment specification](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components#prepare-deployment-specification-inventory) and resource specification: 
         
         - name: Bootstrap PgBouncer
           hosts: localhost
           vars:
             ansible_user: SSH_USER
             ansible_ssh_private_key_file: SSH_KEY_PATH
           roles:
            - role: google.alloydbomni_orchestrator.bootstrap

Replace the following:

     * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
     * `SSH_KEY_PATH`: the local path to the SSH private key file used to connect to your node.
  2. Run the playbook from your control node, passing the resource specification as an extra variable: 
         
         ansible-playbook PGBOUNCER_BOOTSTRAP_PLAYBOOK -i "DEPLOYMENT_SPECIFICATION" \
             -e resource_spec="PGBOUNCER_SPECIFICATION"

Replace the following variables:

     * `PGBOUNCER_BOOTSTRAP_PLAYBOOK`: the path to the playbook that you created to bootstrap PgBouncer.
     * `DEPLOYMENT_SPECIFICATION`: the path to the deployment specification that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components).
     * `PGBOUNCER_SPECIFICATION`: the path to the resource specification you created in Prepare resource specification.



### `alloydbctl`

You can use the `alloydbctl` command-line utility to apply the PgBouncer configuration directly.

To apply the configuration, execute the `apply` command and specify both your [deployment specification](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components#prepare-deployment-specification-inventory) and the PgBouncer resource specification:
    
    
    alloydbctl apply -d "DEPLOYMENT_SPECIFICATION" -r "PGBOUNCER_SPECIFICATION"

Replace the following variables:

  * `DEPLOYMENT_SPECIFICATION`: the path to the deployment specification that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components).
  * `PGBOUNCER_SPECIFICATION`: the path to the resource specification you created in Prepare resource specification.



## Verify the deployment

Choose the interface you want to use to verify the status and configuration of your PgBouncer resource:

### Ansible

To verify the deployment using Ansible, follow these steps:

  1. Create a verification playbook, for example, `verify_pgbouncer.yaml`, that uses the `google.alloydbomni_orchestrator.status` role:
         
         - name: Verify PgBouncer
           hosts: localhost
           vars:
             ansible_user: SSH_USER
             ansible_ssh_private_key_file: SSH_KEY_PATH
           roles:
             - role: google.alloydbomni_orchestrator.status

Replace the following:

     * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
     * `SSH_KEY_PATH`: the local path to the SSH private key file used to connect to your node.
  2. Run the playbook from your control node, passing your inventory file:
         
         ansible-playbook PGBOUNCER_VERIFY_PLAYBOOK -i "DEPLOYMENT_SPECIFICATION" \
             -e resource_type=PgBouncer -e resource_name="PGBOUNCER_RESOURCE_NAME"

Replace the following variables:

     * `PGBOUNCER_VERIFY_PLAYBOOK`: the path to the playbook that you created to verify the PgBouncer deployment.
     * `DEPLOYMENT_SPECIFICATION`: the path to the deployment specification that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components).
     * `PGBOUNCER_RESOURCE_NAME`: the name of your PgBouncer resource.



### alloydbctl

You can use the `get` command to retrieve the status of your PgBouncer resource:
    
    
    alloydbctl get -t PgBouncer -n PGBOUNCER_RESOURCE_NAME -d "DEPLOYMENT_SPECIFICATION"

Replace the following variables:

  * `PGBOUNCER_RESOURCE_NAME`: the name of your PgBouncer resource.
  * `DEPLOYMENT_SPECIFICATION`: the path to the deployment specification that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components).



## Verify the connection pooler

After the RPM orchestrator completes the setup, verify that you can connect to the database cluster through the connection pooler:
    
    
    psql -h VIRTUAL_IP -p 6432 -U postgres

Replace `VIRTUAL_IP` with the virtual IP address that you configured when you [created a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/create-cluster).

PgBouncer routes your connection to the appropriate database node.

## Delete a PgBouncer connection pooler

You can delete the PgBouncer connection pooler using Ansible or the AlloyDB Omni orchestrator command-line interface (CLI):

### Ansible

To delete a PgBouncer connection pooler using Ansible, follow these steps:

  1. Create an Ansible playbook—for example, `teardown.yaml`—that uses the `google.alloydbomni_orchestrator.delete` role:
         
         - name: Delete PgBouncer
           hosts: localhost
           vars:
             ansible_user: SSH_USER
             ansible_ssh_private_key_file: SSH_KEY_PATH
           roles:
             - role: google.alloydbomni_orchestrator.delete

Replace the following:

     * `SSH_USER`: the username that you use to connect to the nodes in your cluster using SSH.
     * `SSH_KEY_PATH`: the local path to the SSH private key file used to connect to your node.
  2. Run the playbook using the `ansible-playbook` command. You must pass the following `resource_name`:
         
         ansible-playbook PGBOUNCER_DELETE_PLAYBOOK -i "DEPLOYMENT_SPECIFICATION" \
             -e resource_type=PgBouncer -e resource_name="PGBOUNCER_RESOURCE_NAME"

Replace the following variables:

     * `PGBOUNCER_DELETE_PLAYBOOK`: the path to the playbook that you created to delete the PgBouncer connection pooler.
     * `DEPLOYMENT_SPECIFICATION`: the path to the deployment specification that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components).
     * `PGBOUNCER_RESOURCE_NAME`: the name of your PgBouncer resource.



### alloydbctl

To delete your PgBouncer resource, run the `alloydbctl delete` command:
    
    
    alloydbctl delete -d "DEPLOYMENT_SPECIFICATION" -t PgBouncer -n "PGBOUNCER_RESOURCE_NAME"

Replace the following variables:

  * `DEPLOYMENT_SPECIFICATION`: the path to the deployment specification that you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/install-components).
  * `PGBOUNCER_RESOURCE_NAME`: the name of your PgBouncer resource.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
