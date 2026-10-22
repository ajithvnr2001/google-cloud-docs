---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-data-replication-failure/
title: Cassandra data replication failure \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:04.220055+00:00
---

# Cassandra data replication failure  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/cassandra-data-replication-failure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Cassandra data replication failure Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

When replicating data during a multi-region expansion, the `CassandraDataReplication` status may show an error state and data replication may fail. 

## Error message

When you use `[ kubectl](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands)` to view the rebuild status:
    
    
      kubectl -n apigee get apigeeds \
      -o jsonpath="{.items[].status.cassandraDataReplication}{'\n'}"
    

You see that one or more Cassandra pods show an error state and a message stating the rebuild has failed. For example:
    
    
    {
      "rebuildDetails": {
        "apigee-cassandra-default-0": {
          "message": "failed to rebuild from us-west1: java.lang.IllegalStateException : Unable to find sufficient sources for streaming range (-8567285182390470134,-8567154549835592965] in keyspace system_distributed",
          "state": "error",
          "updated": 1641581899
        },
        …
      }
    }

## Possible causes

Cause | Description | Troubleshooting instructions applicable for  
---|---|---  
Incorrect source region | An incorrect value was specified for the `source.region` within the Cassandra data replication YAML file. | Apigee hybrid  
Network connectivity issues | There could be network connectivity issues between Cassandra pods in different data centers. | Apigee hybrid  
  
## Common diagnosis steps

  1. Fetch the status of the data replication: 
         
         kubectl -n apigee get apigeeds \  
         -o jsonpath="{.items[].status.cassandraDataReplication}{'\n'}"
         

  2. If you see an error with a message similar to the one specified in Error message, then it indicates that you are observing this issue.



## Cause: Incorrect source region

If you specify a source region (`datacenter`) in your data replication YAML file that is different from the actual source `datacenter`, then the data replication will fail. Perform the steps in Diagnosis to analyze this scenario and perform the steps in Resolution to correct it. 

### Diagnosis

  1. List all the Cassandra pods in the source region: 
         
         kubectl -n apigee get pods -l app=apigee-cassandra
         

  2. Get the actual `datacenter` value from any one of the Cassandra pods returned in step 1: 
         
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- \
         nodetool -u JMX_user -pw JMX_password status
         

  3. Get the value used for `source.region` in the Cassandra data replication custom resource (YAML) file you created in [ Multi-region deployment](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-region#configure-apigee-hybrid-for-multi-region). If you are using the example file name found in the Multi-region deployment documentation, then the file should be named `datareplication.yaml`. 
         
         cat datareplication.yaml
         

Example results:
         
         apiVersion: apigee.cloud.google.com/v1alpha1
         kind: CassandraDataReplication
         metadata:
           name: region-expansion
           namespace: apigee
         spec:
           organizationRef: apigee-hybrid-example-org
           force: false
           source:
             **region: "us-west1"**

  4. Check the result of the `nodetool status` output and verify whether or not the `datacenter` value matches the `source.region` value:
         
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- \
         nodetool -u jmxuser -pw iloveapis123 status
         

Example results:
         
         **Datacenter: dc-1**
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address      Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.104.13.2  491.84 KiB  256          100.0%            7254711c-fe0a-4b34-b50f-861109f97936  ra-1
         UN  10.104.11.3  527.36 KiB  256          100.0%            5ec389f0-fd67-4de6-9f21-172d5899ff78  ra-1
         UN  10.104.12.7  838.46 KiB  256          100.0%            7a88be82-1f81-4117-86e3-2cda434c0878  ra-1

  5. Note that the `source.region` (`us-west1`) from the `datareplication.yaml` file does not match the actual `datacenter` value (`dc-1`) from the `nodetool` status output. Follow the steps in Resolution to correct the configuration. 



### Resolution

To correct the data replication, you'll need to delete the data replication job and create it with the correct `datacenter` name. Perform the following steps: 

  1. Delete the current data replication process. If using the example file name found in the [ Multi-region deployment](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-region#configure-apigee-hybrid-for-multi-region) documentation, then the file should be named `datareplication.yaml`. 
         
         kubectl delete -f datareplication.yaml
         

  2. Update the region name in the YAML file to the correct `datacenter` value, e.g. `dc-1`: 
         
         apiVersion: apigee.cloud.google.com/v1alpha1
         kind: CassandraDataReplication
         metadata:
           name: region-expansion
           namespace: apigee
         spec:
           organizationRef: apigee-hybrid-example-org
           force: false
           source:
             **region: "dc-1"**

  3. Apply the updated data replication: 
         
         kubectl apply -f datareplication.yaml
         

  4. Check the rebuild status using the following command and verify that you no longer see the error state previously reported: 
         
         kubectl -n apigee get apigeeds \
           -o jsonpath="{.items[].status.cassandraDataReplication}{'\n'}"
         

  5. If the problem still persists, proceed to Cause: Network connectivity issues.



## Cause: Network connectivity issues

The data replication error may also be the result of connectivity issues between Cassandra nodes. 

**Note:** Connectivity must be checked between all Cassandra nodes in all regions. 

### Diagnosis

Perform the following steps to analyze this scenario: 

  1. List all the Cassandra pods: 
         
         # list cassandra pods
         kubectl -n=apigee get pods -l app=apigee-cassandra

  2. Execute the following commands to telnet to the first Cassandra pod in the second data center (`dc-2`) from the first Cassandra pod in the first data center (`dc-1`) using port `7001`: 
         
         k debug -it apigee-cassandra-default-0 -n apigee --image=nginx -- sh curl -v telnet://DC_2_APIGEE_CASSANDRA_DEFAULT_0_POD_IP:7001

  3. If telnet was successful, an output similar to following is displayed: 
         
         * Rebuilt URL to: telnet://10.0.4.10:7001/
         *   Trying 10.0.4.10...
         * TCP_NODELAY set
         * Connected to 10.0.4.10 (10.0.4.10) port 7001 (#0)

  4. Otherwise, an error similar to following is displayed: 
         
         * Rebuilt URL to: telnet://10.0.4.10:7001/
         *   Trying 10.0.4.10...
         * TCP_NODELAY set
         * connect to 10.0.4.10 port 7001 failed: Connection refused
         * Failed to connect to 10.0.4.10 port 7001: Connection refused
         * Closing connection 0
         curl: (7) Failed to connect to 10.0.4.10 port 7001: Connection refused

The connectivity failure from the Cassandra pod in one data center to the Cassandra pod in another data center indicates that there must be a firewall restriction or some sort of network connectivity issue. 




### Resolution

  1. If this Apigee hybrid deployment is on GKE, check to see if any firewall rules are set that block the traffic from one data center to another and analyze the network connectivity problem by referring to [ VPC firewall rules overview](https://cloud.google.com/vpc/docs/firewalls).
  2. If this Apigee hybrid deployment is on GKE-on-prem, work with the relevant networking team and analyze the network connectivity problem.



If the problem still persists, go to Must gather diagnostic information. 

## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID. 
  2. The Apigee hybrid organization. 
  3. The `overrides.yaml` files from both source and new regions, masking any sensitive information. 
  4. The `CassandraDataReplication` YAML file. 
  5. Cassandra `nodetool status` output: 
         
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- \
         nodetool -u JMX_user -pw JMX_password status
         

  6. Cassandra `nodetool describecluster` output: 
         
         kubectl -n apigee exec -it apigee-cassandra-default-0 -- \
         nodetool -u JMX_user -pw JMX_password describecluster




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
