---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/management-ui/inconsistent-data-hybrid-ui-mgmt-api/
title: Inconsistent/no data observed for entities in hybrid UI or through Management APIs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:35.271648+00:00
---

# Inconsistent/no data observed for entities in hybrid UI or through Management APIs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/management-ui/inconsistent-data-hybrid-ui-mgmt-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Inconsistent/no data observed for entities in hybrid UI or through Management APIs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/404-support-d) documentation._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptom

Users observe inconsistent data or no data for entities such as API products, Apps, Developers, Key Value Maps (KVM), and Cache intermittently on the Apigee hybrid user interface (UI) and through the Management API. 

## Error messages

No error messages are known to be shown in this scenario. 

## Possible causes

Cause | Description  
---|---  
Cassandra pods not connected to the ring | Cassandra pods of all data centers may not be connected to the common Cassandra ring.  
The nodetool repair was not executed | The `nodetool repair` command may have not executed periodically.  
Network connectivity issues | There could be network connectivity issues between Cassandra pods in different data centers.  
  
## Common diagnosis steps

  1. Fetch the information about one or more entities for which you are seeing this issue, such as API Products, Apps, and so on, using the [Management API](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest) and verify whether or not you could see different results when invoked multiple times. 

On the command line, use the following examples to get your `gcloud` authentication credentials, set environment variables, and run API commands:

**Get API products:**
         
         TOKEN=$(gcloud auth print-access-token)
         ORG=ORGANIZATION_NAME
         
         curl -i -H "Authorization: Bearer $TOKEN" \
         "https://apigee.googleapis.com/v1/organizations/$ORG/apiproducts"

**Get Apps:**
         
         TOKEN=$(gcloud auth print-access-token)
         ORG=ORGANIZATION_NAME
         
         curl -i -H "Authorization: Bearer $TOKEN" \
         "https://apigee.googleapis.com/v1/organizations/$ORG/apps"

**Get Developers:**
         
         TOKEN=$(gcloud auth print-access-token)
         ORG=ORGANIZATION_NAME
         
         curl -i -H "Authorization: Bearer $TOKEN" \
         "https://apigee.googleapis.com/v1/organizations/$ORG/developers"

**Get Key Value Maps (KVMs):**
         
         TOKEN=$(gcloud auth print-access-token)
         ORG=ORGANIZATION_NAME
         
         curl -i -H "Authorization: Bearer $TOKEN" \
         "https://apigee.googleapis.com/v1/organizations/$ORG/keyvaluemaps"

**Get Caches:**
         
         TOKEN=$(gcloud auth print-access-token)
         ORG=ORGANIZATION_NAME
         ENV=ENVIRONMENT_NAME
         
         curl -i -H "Authorization: Bearer $TOKEN" \
         "https://apigee.googleapis.com/v1/organizations/$ORG/environments/$ENV/caches"

  2. If you see no data or different data when the above Management API requests are executed, then it indicates that you are observing the same issue as observed in the UI.



## Cause: Cassandra pods not connected to the Cassandra pods of all data centers

In a multi-region Apigee hybrid deployment, if all Cassandra pods are not connected to the same Cassandra ring, data may not get replicated by all Cassandra pods. As a result, the Management plane will not receive the same dataset for the same query consistently. Perform the following steps to analyze this scenario: 

### Diagnosis

  1. List Cassandra pods:
    
    # list cassandra pods
    kubectl -n apigee get pods -l app=apigee-cassandra

  2. Execute the following command to check the status of all Cassandra pods on each data center. 

**On Apigee hybrid version < 1.4.0:**
         
         # check cassandra cluster status
         kubectl -n apigee get pods \
         -l app=apigee-cassandra \
         --field-selector=status.phase=Running \
         -o custom-columns=name:metadata.name --no-headers \
         | xargs -I{} sh -c "echo {}; kubectl -n apigee exec {} -- nodetool status"

**On Apigee hybrid versions >= 1.4.0:**
         
         # check cassandra cluster status
         kubectl -n apigee get pods \
         -l app=apigee-cassandra \
         --field-selector=status.phase=Running \
         -o custom-columns=name:metadata.name --no-headers \
         | xargs -I{} sh -c "echo {}; kubectl -n apigee exec {} -- nodetool -u jmxuser -pw JMXUSER_PASSWORD status"

  3. Check the result of the above command and verify whether or not all Cassandra pods in all data centers are connected to the Cassandra ring and in **Up and Normal (UN)** status. 

**Example output of a healthy Cassandra ring:**
         
         kubectl -n apigee get pods \
         -l app=apigee-cassandra \
         --field-selector=status.phase=Running \
         -o custom-columns=name:metadata.name --no-headers \
         | xargs -I{} sh -c "echo {}; kubectl -n apigee exec {} -- nodetool -u jmxuser -pw iloveapis123 status"
         
         apigee-cassandra-default-0
         Datacenter: dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.0.2.18  1.32 MiB   256          100.0%            2e6051fe-e3ed-4858-aed0-ac9be5270e97  ra-1
         UN  10.0.4.10  1.49 MiB   256          100.0%            2396e17f-94fd-4d7d-b55e-35f491a5c1cc  ra-1
         UN  10.0.3.14  1.38 MiB   256          100.0%            579cf76e-7d6d-46c8-8319-b7cd74ee87c8  ra-1
         Datacenter: dc-2
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.8.1.12  1.31 MiB   256          100.0%            3e9f24bf-2c10-4cfd-8217-5be6245c2b9c  ra-1
         UN  10.8.2.19  1.24 MiB   256          100.0%            1d2e803d-aa31-487b-9503-1e18297efc04  ra-1
         UN  10.8.4.4   1.28 MiB   256          100.0%            d15ffeef-7929-42c2-a3b1-a3feb85a857b  ra-1
         
         apigee-cassandra-default-1
         Datacenter: dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.0.2.18  1.32 MiB   256          100.0%            2e6051fe-e3ed-4858-aed0-ac9be5270e97  ra-1
         UN  10.0.4.10  1.49 MiB   256          100.0%            2396e17f-94fd-4d7d-b55e-35f491a5c1cc  ra-1
         UN  10.0.3.14  1.38 MiB   256          100.0%            579cf76e-7d6d-46c8-8319-b7cd74ee87c8  ra-1
         Datacenter: dc-2
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.8.1.12  1.31 MiB   256          100.0%            3e9f24bf-2c10-4cfd-8217-5be6245c2b9c  ra-1
         UN  10.8.2.19  1.24 MiB   256          100.0%            1d2e803d-aa31-487b-9503-1e18297efc04  ra-1
         UN  10.8.4.4   1.28 MiB   256          100.0%            d15ffeef-7929-42c2-a3b1-a3feb85a857b  ra-1
         
         apigee-cassandra-default-2
         Datacenter: dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.0.2.18  1.32 MiB   256          100.0%            2e6051fe-e3ed-4858-aed0-ac9be5270e97  ra-1
         UN  10.0.4.10  1.49 MiB   256          100.0%            2396e17f-94fd-4d7d-b55e-35f491a5c1cc  ra-1
         UN  10.0.3.14  1.38 MiB   256          100.0%            579cf76e-7d6d-46c8-8319-b7cd74ee87c8  ra-1
         Datacenter: dc-2
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.8.1.12  1.31 MiB   256          100.0%            3e9f24bf-2c10-4cfd-8217-5be6245c2b9c  ra-1
         UN  10.8.2.19  1.24 MiB   256          100.0%            1d2e803d-aa31-487b-9503-1e18297efc04  ra-1
         UN  10.8.4.4   1.28 MiB   256          100.0%            d15ffeef-7929-42c2-a3b1-a3feb85a857b  ra-1

**Example output of an unhealthy Cassandra ring:**
         
         kubectl -n apigee get pods \
         -l app=apigee-cassandra \
         --field-selector=status.phase=Running \
         -o custom-columns=name:metadata.name --no-headers \
         | xargs -I{} sh -c "echo {}; kubectl -n apigee exec {} -- nodetool -u jmxuser -pw iloveapis123 status"
         
         apigee-cassandra-default-0
         Datacenter: dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.0.2.18  1.32 MiB   256          100.0%            2e6051fe-e3ed-4858-aed0-ac9be5270e97  ra-1** DL  10.0.4.10  1.49 MiB   256          100.0%            2396e17f-94fd-4d7d-b55e-35f491a5c1cc  ra-1
         DL  10.0.3.14  1.38 MiB   256          100.0%            579cf76e-7d6d-46c8-8319-b7cd74ee87c8  ra-1**
         Datacenter: dc-2
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.8.1.12  1.31 MiB   256          100.0%            3e9f24bf-2c10-4cfd-8217-5be6245c2b9c  ra-1
         UN  10.8.2.19  1.24 MiB   256          100.0%            1d2e803d-aa31-487b-9503-1e18297efc04  ra-1** DL  10.8.4.4   1.28 MiB   256          100.0%            d15ffeef-7929-42c2-a3b1-a3feb85a857b  ra-1**
         
         apigee-cassandra-default-1
         Datacenter: dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.0.2.18  1.32 MiB   256          100.0%            2e6051fe-e3ed-4858-aed0-ac9be5270e97  ra-1
         UN  10.0.4.10  1.49 MiB   256          100.0%            2396e17f-94fd-4d7d-b55e-35f491a5c1cc  ra-1
         UN  10.0.3.14  1.38 MiB   256          100.0%            579cf76e-7d6d-46c8-8319-b7cd74ee87c8  ra-1
         Datacenter: dc-2
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.8.1.12  1.31 MiB   256          100.0%            3e9f24bf-2c10-4cfd-8217-5be6245c2b9c  ra-1
         UN  10.8.2.19  1.24 MiB   256          100.0%            1d2e803d-aa31-487b-9503-1e18297efc04  ra-1
         UN  10.8.4.4   1.28 MiB   256          100.0%            d15ffeef-7929-42c2-a3b1-a3feb85a857b  ra-1
         
         apigee-cassandra-default-2
         Datacenter: dc-1
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.0.2.18  1.32 MiB   256          100.0%            2e6051fe-e3ed-4858-aed0-ac9be5270e97  ra-1
         UN  10.0.4.10  1.49 MiB   256          100.0%            2396e17f-94fd-4d7d-b55e-35f491a5c1cc  ra-1
         UN  10.0.3.14  1.38 MiB   256          100.0%            579cf76e-7d6d-46c8-8319-b7cd74ee87c8  ra-1
         Datacenter: dc-2
         ================
         Status=Up/Down
         |/ State=Normal/Leaving/Joining/Moving
         --  Address    Load       Tokens       Owns (effective)  Host ID                               Rack
         UN  10.8.1.12  1.31 MiB   256          100.0%            3e9f24bf-2c10-4cfd-8217-5be6245c2b9c  ra-1
         UN  10.8.2.19  1.24 MiB   256          100.0%            1d2e803d-aa31-487b-9503-1e18297efc04  ra-1
         UN  10.8.4.4   1.28 MiB   256          100.0%            d15ffeef-7929-42c2-a3b1-a3feb85a857b  ra-1

Note that some of the Cassandra pods of the above output are in **DL (Down and Leaving)** status. For more information, see [ nodetool status](https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/tools/toolsStatus.html). 

     * If you notice any Cassandra pods in DL status (as seen in the above example output), then that would be the cause for this issue.
     * When a request is made to fetch the information about any entities either through the hybrid UI or the Management API, if the request hits any of the Cassandra pods which are down, then you will not get any data.



### Resolution

Perform the steps provided in the following section and ensure that Cassandra pods in the problematic data center are connected to the original data center as described in [Multi-region deployment on GKE and GKE on-prem | Apigee](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-region). 

## Cause: The nodetool repair was not executed

If the `nodetool repair` command was not executed periodically as a maintenance task, then there is a possibility for inconsistent data across Cassandra pods. Perform the following steps to analyze this scenario: 

### Diagnosis

  1. Create a [Cassandra client container pod](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/cassandra/ts-cassandra#create-a-client-container-for-debugging) `apigee-hybrid-cassandra-client` for debugging.  

  2. List all the Cassandra pods: 
         
         # list cassandra pods
         kubectl -n=apigee get pods -l app=apigee-cassandra

  3. Connect to one of the Cassandra pod using CQLSH: 
         
         cqlsh apigee-cassandra-default-0.apigee-cassandra-default.apigee.svc.cluster.local -u ddl_user --ssl

  4. List `keyspaces`: 
         
         SELECT * from system_schema.keyspaces;

**Example output:**
         
         ddl_user@cqlsh> SELECT keyspace_name from system_schema.keyspaces;
         
          keyspace_name
         -----------------------------
                          system_auth
          cache_PROJECT_ID_hybrid
                        system_schema
            kms_PROJECT_ID_hybrid
            kvm_PROJECT_ID_hybrid
            rtc_PROJECT_ID_hybrid
                   system_distributed
                               system
                               perses
                        system_traces
          quota_PROJECT_ID_hybrid
         
         (11 rows)

  5. Identify the `keyspaces` from the above result, list and query all entities in each data center using CQLSH. 

Set the consistency level for the CQLSH session to LOCAL_QUORUM by running the following command.
         
         CONSISTENCY LOCAL_QUORUM;

If the entity which is inconsistent is API product:
         
         select * from KMS_KEYSPACE.api_product;

If the entity which is inconsistent is application (`app`):
         
         select * from KMS_KEYSPACE.app;

If the entity which is inconsistent is `developer`:
         
         select * from KMS_KEYSPACE.developer;

If the entity which is inconsistent is key value map:
         
         select * from KVM_KEYSPACE.kvm_map_entry;

If the entity which is inconsistent is `cache`:
         
         select * from CACHE_KEYSPACE.cache_map_entry;

  6. Make a note of the record counts from the output of each of the above queries.
  7. Repeat the above steps for each of the Cassandra pods in all the data centers.
  8. Compare the record counts obtained from all the Cassandra pods.
  9. Identify the Cassandra pods that have inconsistent data.



### Resolution

  1. List Cassandra pods and connect to specific Cassandra pod which had inconsistent data: 
         
         # list cassandra pods
         kubectl -n=apigee get pods -l app=apigee-cassandra
         
         # connect to one cassandra pod
         kubectl -n=apigee exec -it apigee-cassandra-default-0 bash

  2. Execute the `nodetool repair` command on each Cassandra pod on each data center: 

**On Apigee hybrid version < 1.4.0:**
         
         nodetool repair

**On Apigee hybrid versions >= 1.4.0:**
         
         nodetool -u JMX_USERNAME -pw JMX-PASSWORD repair

  3. Follow the diagnosis section again and verify whether or not data has replicated to all Cassandra pods consistently.
  4. Repeat the above steps for all the Cassandra pods which had inconsistent data.



## Cause: Network connectivity issues

If there are network connectivity issues between data centers, Cassandra data may not get replicated consistently to all Cassandra pods in the Cassandra ring. Perform the following steps to analyze this scenario: 

### Diagnosis

  1. List all the Cassandra pods: 
         
         # list cassandra pods
         kubectl -n=apigee get pods -l app=apigee-cassandra

  2. Execute the following `curl` command and telnet to the first Cassandra pod in the second data center (`dc-2`) from the first Cassandra pod in the first data center (`dc-1`) using port `7001`: 
         
         kubectl -n apigee exec -it apigee-cassandra-default-0 bash -- curl -v telnet://DC_2_APIGEE_CASSANDRA_DEFAULT_0_POD_IP:7001

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



## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  1. The Google Cloud Project ID
  2. The Apigee hybrid organization
  3. The `overrides.yaml` file, masking any sensitive information
  4. Kubernetes pod status in all namespaces: 
         
         kubectl get pods -A > kubectl-pod-status`date +%Y.%m.%d_%H.%M.%S`.txt

  5. A kubernetes `cluster-info dump`: 
         
         # generate kubernetes cluster-info dump
         kubectl cluster-info dump -A --output-directory=/tmp/kubectl-cluster-info-dump
         
         # zip kubernetes cluster-info dump
         zip -r kubectl-cluster-info-dump`date +%Y.%m.%d_%H.%M.%S`.zip /tmp/kubectl-cluster-info-dump/*




## References

  * [ Apigee Hybrid Multi-region deployment on GKE and GKE on-prem](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-region)
  * [ Kubernetes Documentation](https://kubernetes.io/docs/home/)
  * [ Cassandra nodetool status command](https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/tools/toolsStatus.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
