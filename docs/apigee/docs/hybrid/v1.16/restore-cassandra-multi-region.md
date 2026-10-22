---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/restore-cassandra-multi-region/
title: Restoring in multiple regions \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:43.175785+00:00
---

# Restoring in multiple regions  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/restore-cassandra-multi-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Restoring in multiple regions Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/restore-cassandra-multi-region.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/restore-cassandra-multi-region.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/restore-cassandra-multi-region.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/restore-cassandra-multi-region.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/restore-cassandra-multi-region.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/restore-cassandra-multi-region.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/restore-cassandra-multi-region.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/restore-cassandra-multi-region.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/restore-cassandra-multi-region.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/restore-cassandra-multi-region.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/restore-cassandra-multi-region.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/restore-cassandra-multi-region.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/restore-cassandra-multi-region.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/restore-cassandra-multi-region.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/restore-cassandra-multi-region.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/restore-cassandra-multi-region.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/restore-cassandra-multi-region.html)



This page describes how to _recover_ or _restore_ Cassandra in multiple regions.

In a multi-region deployment, Apigee hybrid is deployed in multiple geographic locations across different datacenters. If one or more regions fail, but healthy regions remain, you can use a healthy region to _recover_ failed Cassandra regions with the latest data.

In the event of a catastrophic failure of all hybrid regions, Cassandra can be _restored_. It is important to note that, if you have multiple Apigee organizations in your deployment, the restore process restores data for **all** the organizations. In a multi-organization setup, restoring only a specific organization is **not** supported.

This topic describes both approaches to salvaging failed region(s):

  * Recover failed region(s) \- Describes the steps to recover failed region(s) based on a healthy region.
  * Restore failed region(s) \- Describes the steps to restore failed region(s) from a backup. This approach is only required if _all_ hybrid regions are impacted.



## Recover failed region(s)

To recover failed region(s) from a healthy region, perform the following steps:

  1. Redirect the API traffic from the impacted region(s) to the good working region. Plan the capacity accordingly to support the diverted traffic from failed region(s).
  2. Decommission the impacted region. For each impacted region, follow the steps outlined in [Decommission a hybrid region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/decommission-region). Wait for decommissioning to complete before moving on to the next step. 
  3. Restore the impacted region. To restore, create a new region, as described in [Multi-region deployment on GKE, GKE on-prem, and AKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region). 



## Restoring from a backup

**Note** : If you want to preserve an existing setup for troubleshooting and root cause analysis (RCA), you should delete all the `org` and `env` components from the Kubernetes cluster _except_ the Apigee controller, and retain the cluster. The cluster will contain the existing Apigee datastore (Cassandra) which you can use for troubleshooting. Create a new Kubernetes cluster and then restore Cassandra in the new cluster.

The Cassandra backup can either reside on Cloud Storage or on a remote server based on your configuration. To restore Cassandra from a backup, perform the following steps:

**Important:** If you installed Apigee hybrid into multiple regions, you must check the overrides file for the region you are restoring to make sure the `cassandra:hostNetwork` is set to `false` before you perform the restoration. To check the `hostNetwork` setting in the region you are trying to restore, use this command: 
    
    
    kubectl -n APIGEE_NAMESPACE get apigeeds -o=jsonpath='{.items[].spec.components.cassandra.hostNetwork}'

  1. Open the overrides file for the region you wish to restore.
  2. Set `cassandra:hostNetwork` to `false`.
  3. Apply the overrides file: 
         
         helm upgrade datastore apigee-datastore/ \
           --install \
           --namespace APIGEE_NAMESPACE \
           -f OVERRIDES_FILE
         

  4. Before continuing, check to make sure the `hostNetwork` is set to `false`: 
         
         kubectl -n APIGEE_NAMESPACE get apigeeds -o=jsonpath='{.items[].spec.components.cassandra.hostNetwork}'

  5. Delete hybrid from the region you are restoring: 
         
         helm delete DATASTORE_RELEASE_NAME \
           --namespace APIGEE_NAMESPACE
         

Where DATASTORE_RELEASE_NAME is the release name of the datastore you installed Cassandra in the region, for example `datastore-region1`.

**Note:** Be careful which release of the datastore component you delete. You can see your releases with the command `helm -n APIGEE_NAMESPACE ls`. 
  6. Restore the desired region from a backup. For more information, see [Restoring a region from a backup](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/restore-cassandra-single-region#restore-gcs).

  7. Remove the dead nodes from the deleted region(s): 
     1. Using the `nodetool status` command, identify all the nodes with `DN` status in the deleted region(s): 
            
            kubectl exec apigee-cassandra-default-0 -n APIGEE_NAMESPACE  -- nodetool -u APIGEE_JMX_USER -pw APIGEE_JMX_PASSWORD status

where: 

        * APIGEE_JMX_USER is the username for the Cassandra JMX operations user. Used to authenticate and communicate with the Cassandra JMX interface. See [`cassandra:auth:jmx:username`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#cassandra-auth-jmx-username).
        * APIGEE_JMX_PASSWORD is the password for the Cassandra JMX operations user. See [`cassandra:auth:jmx:password`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#cassandra-auth-jmx-password).
     2. Remove each node with `DN` status in the deleted region(s): 
            
            kubectl exec apigee-cassandra-default-0 -n APIGEE_NAMESPACE  -- nodetool -u APIGEE_JMX_USER -pw APIGEE_JMX_PASSWORD removenode NODE_HOST_ID

Replace NODE_HOST_ID with the Host ID of each node you identified in the previous step. For example: 
            
            kubectl exec apigee-cassandra-default-0 -n apigee -- nodetool -u my-jmx-id -pw my-jmx-pwd removenode abcdef-f202-438a-8a77-40636317b7c9

     3. Run the `nodetool status` command again and verify that the nodes with `DN` status in the deleted region(s) are gone. 
            
            kubectl exec apigee-cassandra-default-0 -n APIGEE_NAMESPACE  -- nodetool -u APIGEE_JMX_USER -pw APIGEE_JMX_PASSWORD status

  8. Remove the deleted region(s) references and add the restored region(s) references in the `KeySpaces` metadata. 
     1. Get the cassandra datacenter name by using the `nodetool status` option. 
            
            kubectl exec -n APIGEE_NAMESPACE -it apigee-cassandra-default-0 -- bash
                  nodetool  -u APIGEE_JMX_USER -pw APIGEE_JMX_PASSWORD status |grep -i Datacenter

where: 

        * APIGEE_JMX_USER is the username for the Cassandra JMX operations user. Used to authenticate and communicate with the Cassandra JMX interface. See [`cassandra:auth:jmx:username`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#cassandra-auth-jmx-username).
        * APIGEE_JMX_PASSWORD is the password for the Cassandra JMX operations user. See [`cassandra:auth:jmx:password`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#cassandra-auth-jmx-password).
     2. Update the `KeySpaces` replication. 
        1. [Create a client container](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-a-client-container-for-debugging) and connect to the Cassandra cluster through the CQL interface.
        2. Get the list of user keyspaces from CQL interface: 
               
               cqlsh CASSANDRA_SEED_HOST -u APIGEE_DDL_USER -p APIGEE_DDL_PASSWORD
                     --ssl -e "select keyspace_name from system_schema.keyspaces;"|grep -v system

where: 

           * CASSANDRA_SEED_HOST is the Cassandra multi-region seed host. For most multi-region installations, use the IP address of a host in your first region. See [Configure Apigee hybrid for multi-region](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#configure-apigee-hybrid-for-multi-region) and [`cassandra:externalSeedHost`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#cassandra-externalseedhost).
           * APIGEE_DDL_USER and APIGEE_DDL_PASSWORD are the admin username and password for the Cassandra Data Definition Language (DDL) user. The default values are "`ddl_user`" and "`iloveapis123`". You can check the DDL username and password by checking the value stored in the `apigee-datastore-default-creds`secret. You must have admin privileges to check this secret. The following command will return base-64 encoded values for the DDL username and password: 
                 
                 kubectl get secret apigee-datastore-default-creds -n APIGEE_NAMESPACE -o yaml

See [`cassandra.auth.ddl.password`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#cassandra-auth.ddl.password) in the Configuration properties reference and [Command Line Options](https://cassandra.apache.org/doc/4.1/cassandra/tools/cqlsh.html#command-line-options) in the Apache Cassandra cqlsh documentation. 

        3. For each keyspace, run the following command from the CQL interface to update the replication settings: 
               
               ALTER KEYSPACE KEYSPACE_NAME WITH replication = {'class': 'NetworkTopologyStrategy', 'DATACENTER_NAME':3};

where: 

           * KEYSPACE_NAME is the name of the keyspace listed in the previous step's output.
           * DATACENTER_NAME is name of the Cassandra datacenter you obtained with the `nodetool status` option in step 8.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
