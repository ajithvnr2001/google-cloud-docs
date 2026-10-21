---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-graceful-shutdown/
title: Cassandra graceful shutdown \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:22.509378+00:00
---

# Cassandra graceful shutdown  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-graceful-shutdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Cassandra graceful shutdown Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/404-support-d) documentation._

**Note:** This document is applicable for Apigee hybrid users only. 

To ensure data integrity during maintenance, you must shut down the Cassandra pod gracefully before rescheduling the pod.

## Before you begin

Before proceeding with any maintenance that involves restarting Cassandra pods, ensure the current cluster is healthy.

Check the status of the Cassandra cluster: 
    
    
    kubectl -n APIGEE_NAMESPACE -c apigee-cassandra exec apigee-cassandra-default-0 -- bash -c 'nodetool -u cassandra -pw $CASS_PASSWORD status'

Sample output:
    
    
    Datacenter: us-west2
    ====================
    Status=Up/Down
    |/ State=Normal/Leaving/Joining/Moving
    --  Address     Load      Tokens  Owns (effective)  Host ID                               Rack
    UN  10.44.16.4  5.43 MiB  256     100.0%            c873909a-3003-4283-b175-92289967a486  ra-1
    UN  10.44.14.4  5.45 MiB  256     100.0%            8126b7a0-a175-475b-b9be-43b1f9b78487  ra-1
    UN  10.44.18.4  5.42 MiB  256     100.0%            6655989c-1313-4df2-92af-c131c0f223c0  ra-1

All the nodes in the cluster should be in the `UN` (Up/Normal) state.

## Graceful shutdown

To gracefully shut down the Cassandra pod, you can either drain the node or delete the pod.

  * [Drain the node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/) to trigger a graceful shutdown of the Cassandra pod. This action evicts the pod from the current node, and the scheduler attempts to move the pod on another available node. 
    * If a node is available, the pod restarts on that node.
    * If no other node is available, the pod remains in a `Pending` state until you add a new node to the cluster.

After the pod restarts, it automatically updates its IP address within the cluster.

**Note:** This step is only recommended when node requires maintenance. 
  * To force the Cassandra pod to gracefully shut down, you can use the following command to delete the pod:
        
        kubectl delete pod TARGET_CASSANDRA_POD -n APIGEE_NAMESPACE

This command deletes the Cassandra pod, triggering its graceful shutdown process.




## Verification

To confirm that the Cassandra node has shut down gracefully, inspect the logs of the Cassandra container.
    
    
    kubectl logs TARGET_CASSANDRA_POD -n APIGEE_NAMESPACE -c apigee-cassandra

Where TARGET_CASSANDRA_POD is the name of the Cassandra pod that you are checking.

The log entries should indicate successful drain and flush.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
